from datetime import date

from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma


load_dotenv()

K = 3


casos_evaluacion = [
    {
        "pregunta": "¿Qué ocurre cuando hay un TimeoutError?",
        "ids_relevantes": {"doc0"}
    },
    {
        "pregunta": "¿Cómo se calculan los costos?",
        "ids_relevantes": {"doc1"}
    },
    {
        "pregunta": "¿Para qué sirven los mocks?",
        "ids_relevantes": {"doc2"}
    },
    {
        "pregunta": "¿Cómo selecciona herramientas el agente?",
        "ids_relevantes": {"doc3"}
    },
    {
        "pregunta": "¿Qué hace la memoria conversacional?",
        "ids_relevantes": {"doc4"}
    }
]


def precision_at_k(ids_recuperados, ids_relevantes):
    if not ids_recuperados:
        return 0.0

    acertados = [
        item
        for item in ids_recuperados
        if item in ids_relevantes
    ]

    return len(acertados) / len(ids_recuperados)


def recall_at_k(ids_recuperados, ids_relevantes):
    if not ids_relevantes:
        return None

    acertados = [
        item
        for item in ids_recuperados
        if item in ids_relevantes
    ]

    return len(acertados) / len(ids_relevantes)


def promediar(valores):
    validos = [
        valor
        for valor in valores
        if valor is not None
    ]

    if not validos:
        return 0.0

    return sum(validos) / len(validos)


def evaluar_recuperacion(retriever, casos, k=3):
    resultados = []

    for caso in casos:
        chunks = retriever.invoke(
            caso["pregunta"]
        )

        ids_recuperados = [
            chunk.id
            for chunk in chunks
        ][:k]

        precision = precision_at_k(
            ids_recuperados,
            caso["ids_relevantes"]
        )

        recall = recall_at_k(
            ids_recuperados,
            caso["ids_relevantes"]
        )

        resultados.append(
            {
                "pregunta": caso["pregunta"],
                "precision": precision,
                "recall": recall,
            }
        )

    precision_promedio = promediar(
        r["precision"]
        for r in resultados
    )

    recall_promedio = promediar(
        r["recall"]
        for r in resultados
    )

    return (
        resultados,
        precision_promedio,
        recall_promedio,
    )


def guardar_resultados(
    resultados,
    precision_promedio,
    recall_promedio,
):
    with open(
        "resultados_evaluacion.txt",
        "w",
        encoding="utf-8"
    ) as archivo:

        archivo.write(
            f"Fecha: {date.today()}\n"
        )

        archivo.write(
            "Configuracion: "
            f"k={K}, "
            "chunk_size=200, "
            "chunk_overlap=30\n\n"
        )

        for resultado in resultados:

            recall_txt = (
                "n/a"
                if resultado["recall"] is None
                else f"{resultado['recall']:.2f}"
            )

            archivo.write(
                f"{resultado['precision']:.2f}  "
                f"{recall_txt}  "
                f"{resultado['pregunta']}\n"
            )

        archivo.write(
            "\n"
            f"promedio -> precision: "
            f"{precision_promedio:.3f}  "
            f"recall: {recall_promedio:.3f}\n"
        )


if __name__ == "__main__":

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    vectorstore = Chroma(
        collection_name="corpus_accenture",
        persist_directory="vectorstore",
        embedding_function=embeddings,
    )

    retriever = vectorstore.as_retriever(
        search_kwargs={"k": K}
    )

    (
        resultados,
        precision_promedio,
        recall_promedio,
    ) = evaluar_recuperacion(
        retriever,
        casos_evaluacion,
        k=K,
    )

    for resultado in resultados:

        recall_txt = (
            "n/a"
            if resultado["recall"] is None
            else f"{resultado['recall']:.2f}"
        )

        print(
            f"{resultado['precision']:.2f}  "
            f"{recall_txt}  "
            f"{resultado['pregunta']}"
        )

    print(
        "\n"
        f"promedio -> precision: "
        f"{precision_promedio:.3f}  "
        f"recall: {recall_promedio:.3f}"
    )

    guardar_resultados(
        resultados,
        precision_promedio,
        recall_promedio,
    )

    print(
        "\nResultados guardados en "
        "resultados_evaluacion.txt"
    )