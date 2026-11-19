from typing import TypedDict

from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from langgraph.checkpoint.memory import (
    InMemorySaver,
)

from langgraph.types import (
    interrupt,
    Command,
)


class EstadoDespliegue(
    TypedDict
):
    huella_nueva: str
    aprobado: bool


def proponer(
    estado,
):
    return {}


def supervisar(
    estado,
):
    decision = interrupt(
        {
            "motivo":
            "aprobar despliegue de nuevo prompt",
            "huella_propuesta":
            estado["huella_nueva"],
        }
    )

    return {
        "aprobado": decision
    }


def aplicar(
    estado,
):
    if estado["aprobado"]:
        print(
            "version",
            estado["huella_nueva"],
            "activada",
        )
    else:
        print(
            "version",
            estado["huella_nueva"],
            "rechazada, se mantiene la anterior",
        )

    return {}


grafo = StateGraph(
    EstadoDespliegue
)

grafo.add_node(
    "proponer",
    proponer,
)

grafo.add_node(
    "supervisar",
    supervisar,
)

grafo.add_node(
    "aplicar",
    aplicar,
)

grafo.add_edge(
    START,
    "proponer",
)

grafo.add_edge(
    "proponer",
    "supervisar",
)

grafo.add_edge(
    "supervisar",
    "aplicar",
)

grafo.add_edge(
    "aplicar",
    END,
)

app_despliegue = grafo.compile(
    checkpointer=InMemorySaver()
)

# APROBACION

config = {
    "configurable": {
        "thread_id":
        "despliegue-aprobacion"
    }
}

resultado = app_despliegue.invoke(
    {
        "huella_nueva":
        "prompt-v2",
        "aprobado": False,
    },
    config=config,
)

print(resultado)

print(
    app_despliegue.get_state(
        config
    ).interrupts[0].value
)

resultado = app_despliegue.invoke(
    Command(resume=True),
    config=config,
)

print(resultado)

# RECHAZO

config2 = {
    "configurable": {
        "thread_id":
        "despliegue-rechazo"
    }
}

app_despliegue.invoke(
    {
        "huella_nueva":
        "prompt-v3",
        "aprobado": False,
    },
    config=config2,
)

resultado_rechazo = app_despliegue.invoke(
    Command(resume=False),
    config=config2,
)

print(resultado_rechazo)