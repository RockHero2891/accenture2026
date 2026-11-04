from dotenv import load_dotenv

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)

from langchain_core.prompts import (
    PromptTemplate,
)

from langchain_core.output_parsers import (
    StrOutputParser,
)


def construir_cadena(modelo):

    plantilla_explicacion = (
        PromptTemplate.from_template(
            "Explica el concepto de "
            "{concepto} en un párrafo."
        )
    )

    plantilla_resumen = (
        PromptTemplate.from_template(
            "Resume el siguiente texto en "
            "máximo tres oraciones:\n\n"
            "{explicacion}"
        )
    )

    plantilla_lista = (
        PromptTemplate.from_template(
            "Convierte el siguiente resumen "
            "en una lista markdown de viñetas:\n\n"
            "{resumen}"
        )
    )

    cadena = (
        plantilla_explicacion
        | modelo
        | StrOutputParser()
        | (
            lambda explicacion: {
                "explicacion": explicacion
            }
        )
        | plantilla_resumen
        | modelo
        | StrOutputParser()
        | (
            lambda resumen: {
                "resumen": resumen
            }
        )
        | plantilla_lista
        | modelo
        | StrOutputParser()
    )

    return cadena


if __name__ == "__main__":

    load_dotenv()

    modelo = ChatGoogleGenerativeAI(
        model="gemini-3.6-flash",
        temperature=0,
    )

    cadena = construir_cadena(
        modelo
    )

    resultado = cadena.invoke(
        {
            "concepto": "tokenización"
        }
    )

    print(resultado)
    