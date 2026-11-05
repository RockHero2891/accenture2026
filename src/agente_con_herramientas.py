from dotenv import load_dotenv

from langchain_core.tools import tool

from langchain_core.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
)

from langchain_google_genai import (
    ChatGoogleGenerativeAI,
)

from langchain_classic.agents import (
    AgentExecutor,
    create_tool_calling_agent,
)


load_dotenv()


@tool
def consultar_documentacion_proyecto(
    consulta: str,
) -> str:
    """
    Busca información sobre componentes del proyecto.

    Usar cuando el usuario pregunta cómo funciona
    una característica del sistema o necesita
    información documental específica.
    """

    documentos = {
        "reintentos": (
            "El cliente reintenta hasta "
            "3 veces ante TimeoutError."
        ),
        "costos": (
            "Los costos se estiman utilizando "
            "totalTokenCount."
        ),
        "tokenizacion": (
            "La tokenización divide el texto "
            "en tokens antes de procesarlo."
        ),
    }

    consulta = consulta.lower()

    for clave, texto in documentos.items():
        if clave in consulta:
            return texto

    return (
        "No encontré información para "
        "esa consulta."
    )


@tool
def contar_palabras(
    texto: str,
) -> str:
    """
    Cuenta cuántas palabras tiene un texto.

    Usar cuando el usuario necesita conocer
    la cantidad de palabras de un contenido.
    """

    cantidad = len(texto.split())

    return (
        f"El texto contiene "
        f"{cantidad} palabras."
    )


modelo = ChatGoogleGenerativeAI(
    model="gemini-3.6-flash"
)

herramientas = [
    consultar_documentacion_proyecto,
    contar_palabras,
]

prompt_agente = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            (
                "Eres un asistente que utiliza "
                "las herramientas disponibles "
                "cuando son necesarias."
            ),
        ),
        (
            "human",
            "{entrada}",
        ),
        MessagesPlaceholder(
            "agent_scratchpad"
        ),
    ]
)

agente = create_tool_calling_agent(
    modelo,
    herramientas,
    prompt_agente,
)

ejecutor_agente = AgentExecutor(
    agent=agente,
    tools=herramientas,
    verbose=True,
    return_intermediate_steps=True,
)


def extraer_texto_respuesta(
    resultado,
):
    respuesta = resultado["output"]

    if isinstance(
        respuesta,
        str,
    ):
        return respuesta

    if isinstance(
        respuesta,
        list,
    ):
        textos = []

        for bloque in respuesta:

            if (
                isinstance(
                    bloque,
                    dict,
                )
                and "text" in bloque
            ):
                textos.append(
                    bloque["text"]
                )

        return "\n".join(
            textos
        )

    return str(
        respuesta
    )


def mostrar_traza(
    resultado,
):

    print(
        "\nHerramientas utilizadas:"
    )

    pasos = resultado[
        "intermediate_steps"
    ]

    if not pasos:
        print("- Ninguna")
        return

    for accion, observacion in pasos:

        print(
            f"- {accion.tool}"
        )

        print(
            f"  Observación: "
            f"{observacion}"
        )


if __name__ == "__main__":

    print(
        "\n=== PRUEBA 1 ==="
    )

    resultado = (
        ejecutor_agente.invoke(
            {
                "entrada": (
                    "¿Cómo funcionan "
                    "los reintentos?"
                )
            }
        )
    )

    print(
        "\nRespuesta:"
    )

    print(
        extraer_texto_respuesta(
            resultado
        )
    )

    mostrar_traza(
        resultado
    )

    print(
        "\n=== PRUEBA 2 ==="
    )

    resultado = (
        ejecutor_agente.invoke(
            {
                "entrada": (
                    "Cuenta las palabras "
                    "de este texto: "
                    "hola mundo desde "
                    "langchain"
                )
            }
        )
    )

    print(
        "\nRespuesta:"
    )

    print(
        extraer_texto_respuesta(
            resultado
        )
    )

    mostrar_traza(
        resultado
    )
    