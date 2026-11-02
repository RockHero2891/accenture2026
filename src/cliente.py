from consumir_gemini import (
    armar_peticion,
    enviar_peticion,
    extraer_texto,
)

import time
from typing import Callable, Any


def con_reintento(
    funcion: Callable[[], Any],
    intentos: int = 3,
    espera_segundos: int = 2,
) -> Any:
    for intento in range(1, intentos + 1):
        try:
            return funcion()

        except TimeoutError:
            if intento == intentos:
                raise

            print(
                f"Intento {intento} de {intentos} "
                f"falló por límite de uso. Reintentando..."
            )

            time.sleep(espera_segundos)


def consultar_modelo(
    pregunta: str,
) -> str:

    url, body = armar_peticion(pregunta)

    try:
        respuesta = con_reintento(
            lambda: enviar_peticion(url, body)
        )

    except TimeoutError:
        raise RuntimeError(
            "El servicio no respondió tras varios intentos. "
            "Intenta más tarde."
        )

    return extraer_texto(respuesta)


if __name__ == "__main__":
    try:
        respuesta = consultar_modelo(
            "¿Cuál es la capital de Chile?"
        )

        print(respuesta)

    except Exception as error:
        print(error)