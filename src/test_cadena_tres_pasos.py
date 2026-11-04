from unittest.mock import MagicMock

from langchain_core.messages import (
    AIMessage,
)

from cadena_tres_pasos import (
    construir_cadena,
)


def test_cadena_conecta_los_tres_pasos():

    modelo_falso = MagicMock()

    modelo_falso.side_effect = [
        AIMessage(
            content=(
                "La tokenización divide "
                "el texto."
            )
        ),
        AIMessage(
            content=(
                "Dividir texto en partes."
            )
        ),
        AIMessage(
            content=(
                "- Punto 1\n"
                "- Punto 2"
            )
        ),
    ]

    cadena = construir_cadena(
        modelo_falso
    )

    resultado = cadena.invoke(
        {
            "concepto": "tokenización"
        }
    )

    assert (
        modelo_falso.call_count
        == 3
    )

    assert "-" in resultado
    