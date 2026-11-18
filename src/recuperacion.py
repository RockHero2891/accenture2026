from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
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
    citas = {}

    for i, doc in enumerate(chunks_recuperados, start=1):
        fuente = doc.metadata.get(
            "fuente",
            "desconocida"
        )

        lineas.append(
            f"[{i}] {doc.page_content}"
        )

        citas[i] = fuente

    contexto = "\n\n".join(lineas)

    return contexto, citas


def construir_prompt(
    pregunta,
    persist_directory="vectorstore",
    k=3
):
    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    vectorstore = Chroma(
        collection_name="corpus_accenture",
        persist_directory=persist_directory,
        embedding_function=embeddings,
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": k}
    )

    chunks_recuperados = retriever.invoke(
        pregunta
    )

    contexto, citas = formatear_contexto(
        chunks_recuperados
    )

    prompt = PROMPT_TEMPLATE.format(
        contexto=contexto,
        pregunta=pregunta,
    )

    return prompt, citas


if __name__ == "__main__":
    pregunta = (
        "¿Qué hace la memoria conversacional?"
    )

    prompt, citas = construir_prompt(
        pregunta
    )

    print("\n===== PROMPT =====\n")
    print(prompt)

    print("\n===== CITAS =====\n")
    print(citas)