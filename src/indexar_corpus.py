from dotenv import load_dotenv
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma


load_dotenv()


def indexar_corpus():
    corpus = [
        "El cliente Gemini utiliza reintentos con espera creciente cuando ocurre un TimeoutError.",
        "Los costos de uso se calculan utilizando totalTokenCount y las tarifas vigentes por token.",
        "Las pruebas unitarias utilizan mocks para evitar llamadas reales a la API durante la ejecución.",
        "El agente selecciona herramientas utilizando las descripciones definidas en los docstrings.",
        "La memoria conversacional permite mantener contexto entre interacciones del usuario."
    ]

    metadatas = [
        {"fuente": "cliente_gemini.md"},
        {"fuente": "costos.md"},
        {"fuente": "tests.md"},
        {"fuente": "agente.md"},
        {"fuente": "memoria.md"},
    ]

    ids = [
        "doc0",
        "doc1",
        "doc2",
        "doc3",
        "doc4",
    ]

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=200,
        chunk_overlap=30,
    )

    chunks = splitter.create_documents(
        corpus,
        metadatas=metadatas,
    )

    embeddings = GoogleGenerativeAIEmbeddings(
        model="models/gemini-embedding-001"
    )

    vectorstore = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        ids=ids,
        collection_name="corpus_accenture",
        persist_directory="vectorstore",
    )

    print(
        f"Indexados {len(chunks)} chunks en vectorstore"
    )

    return vectorstore


if __name__ == "__main__":
    indexar_corpus()