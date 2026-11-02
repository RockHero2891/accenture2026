from unittest.mock import patch, Mock

from requests.exceptions import ConnectionError

import pytest

import cliente


# ----------------------------------
# enviar_peticion
# ----------------------------------

def test_enviar_peticion_connection_error():
    with patch(
        "consumir_gemini.requests.post",
        side_effect=ConnectionError()
    ):
        with pytest.raises(RuntimeError):
            cliente.enviar_peticion(
                "https://test.com",
                {}
            )


def test_enviar_peticion_exito():
    respuesta_falsa = Mock()

    respuesta_falsa.json.return_value = {
        "texto": "respuesta simulada"
    }

    with patch(
        "consumir_gemini.requests.post",
        return_value=respuesta_falsa
    ):
        resultado = cliente.enviar_peticion(
            "https://test.com",
            {}
        )

    assert resultado == {
        "texto": "respuesta simulada"
    }


# ----------------------------------
# con_reintento
# ----------------------------------

def test_con_reintento_agota_intentos():

    def siempre_falla():
        raise TimeoutError("simulado")

    with patch("cliente.time.sleep"):
        with pytest.raises(TimeoutError):
            cliente.con_reintento(
                siempre_falla,
                intentos=3
            )


def test_con_reintento_no_reintenta_value_error():

    def falla():
        raise ValueError("simulado")

    with pytest.raises(ValueError):
        cliente.con_reintento(
            falla,
            intentos=3
        )


def test_con_reintento_exito():

    def funciona():
        return "ok"

    resultado = cliente.con_reintento(
        funciona
    )

    assert resultado == "ok"


# ----------------------------------
# consultar_modelo
# ----------------------------------

def test_consultar_modelo_convierte_error():

    with patch(
        "cliente.con_reintento",
        side_effect=TimeoutError("simulado")
    ):
        with pytest.raises(RuntimeError):
            cliente.consultar_modelo(
                "pregunta"
            )


def test_consultar_modelo_exito():

    respuesta_simulada = {
        "candidates": [
            {
                "content": {
                    "parts": [
                        {
                            "text": "Santiago"
                        }
                    ]
                }
            }
        ]
    }

    with patch(
        "cliente.con_reintento",
        return_value=respuesta_simulada
    ):
        with patch(
            "cliente.armar_peticion",
            return_value=("url", {})
        ):
            resultado = cliente.consultar_modelo(
                "capital"
            )

    assert resultado == "Santiago"