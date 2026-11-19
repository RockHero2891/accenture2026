import json
import time

from contextlib import contextmanager
from datetime import datetime, timezone

from dotenv import load_dotenv
from langchain_google_genai import (
    ChatGoogleGenerativeAI,
    GoogleGenerativeAIEmbeddings,
)
from langchain_chroma import Chroma


load_dotenv()


PROMPT_TEMPLATE = """
Responde la pregunta usando SOLO el contexto de abajo.

Cita la fuente de cada afirmación con su número entre corchetes, como [1].

Si el contexto no alcanza para responder, dilo explícitamente en lugar de inventar información.

Contexto:

{contexto}

Pregunta:

{pregunta}

Respuesta:
"""


def formatear_contexto(chunks_recuperados):
    lineas = []

    for indice, doc in enumerate(
        chunks_recuperados,
        start=1,
    ):
        lineas.append(
            f"[{indice}] {doc.page_content}"
        )

    return "\n\n".join(lineas)


@contextmanager
def medir(tiempos, etapa):
    inicio = time.perf_counter()

    yield

    tiempos[etapa] = (
        time.perf_counter() - inicio
    )


def registrar_consulta(
    pregunta,
    persist_directory="vectorstore",
    k=3,
):
    tiempos = {}

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    chat_model = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash"
    )

    with medir(
        tiempos,
        "embed_y_busqueda",
    ):
        vectorstore = Chroma(
            collection_name="corpus_accenture",
            persist_directory=persist_directory,
            embedding_function=embeddings,
        )

        retriever = vectorstore.as_retriever(
            search_kwargs={"k": k}
        )

        chunks = retriever.invoke(
            pregunta
        )

    contexto = formatear_contexto(
        chunks
    )

    prompt = PROMPT_TEMPLATE.format(
        contexto=contexto,
        pregunta=pregunta,
    )

    with medir(
        tiempos,
        "generacion",
    ):
        respuesta = chat_model.invoke(
            prompt
        )

    registro = {
        "timestamp": datetime.now(
            timezone.utc
        ).isoformat(),
        "pregunta": pregunta,
        "k": k,
        "tiempos_ms": {
            etapa: round(
                segundos * 1000,
                2,
            )
            for etapa, segundos in tiempos.items()
        },
        "tiempo_total_ms": round(
            sum(tiempos.values()) * 1000,
            2,
        ),
        "tokens": (
            dict(respuesta.usage_metadata)
            if respuesta.usage_metadata
            else None
        ),
    }

    return registro


if __name__ == "__main__":

    preguntas = [
        "¿Qué ocurre cuando hay un TimeoutError?",
        "¿Cómo se calculan los costos?",
        "¿Qué hace la memoria conversacional?",
    ]

    for pregunta in preguntas:

        registro = registrar_consulta(
            pregunta=pregunta,
            persist_directory="vectorstore",
            k=3,
        )

        print(
            json.dumps(
                registro,
                indent=2,
                ensure_ascii=False,
            )
        )

        with open(
            "registros_latencia_costo.jsonl",
            "a",
            encoding="utf-8",
        ) as archivo:

            archivo.write(
                json.dumps(
                    registro,
                    ensure_ascii=False,
                )
                + "\n"
            )