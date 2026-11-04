import re
from collections import Counter

from cliente import consultar_modelo


def limpiar_texto(texto: str) -> str:
    """Normaliza el texto: minúsculas y sin puntuación."""
    if not isinstance(texto, str):
        tipo = type(texto).__name__
        raise TypeError(
            f"limpiar_texto espera str, no {tipo}"
        )

    texto = texto.lower()
    texto = re.sub(r"[^\w\s]", "", texto)
    texto = re.sub(r"\s+", " ", texto).strip()

    return texto


def tokenizar(texto_limpio: str) -> list[str]:
    """Convierte texto limpio en tokens."""
    return texto_limpio.split()


def procesar_texto(texto: str) -> list[str]:
    """Pipeline completo de limpieza y tokenización."""
    texto_limpio = limpiar_texto(texto)
    return tokenizar(texto_limpio)


def vectorizar(tokens: list[str]) -> Counter:
    """Cuenta frecuencia de palabras."""
    return Counter(tokens)


def calcular_coincidencia(
    referencia: str,
    respuesta: str,
) -> tuple[float, float]:

    crudo_ref = referencia.split()
    crudo_resp = respuesta.split()

    comunes_crudo = set(crudo_ref) & set(crudo_resp)

    if crudo_ref:
        pct_crudo = (
            len(comunes_crudo)
            / len(set(crudo_ref))
        )
    else:
        pct_crudo = 0.0

    tokens_ref = procesar_texto(referencia)
    tokens_resp = procesar_texto(respuesta)

    comunes_proc = set(tokens_ref) & set(tokens_resp)

    if tokens_ref:
        pct_proc = (
            len(comunes_proc)
            / len(set(tokens_ref))
        )
    else:
        pct_proc = 0.0

    return pct_crudo, pct_proc


if __name__ == "__main__":

    casos = [
        (
            "¿Qué es Python?",
            "Python es un lenguaje de programación interpretado.",
        ),
        (
            "¿Cuál es la capital de Chile?",
            "Santiago es la capital de Chile.",
        ),
        (
            "¿Qué es una API?",
            "Una API permite la comunicación entre sistemas.",
        ),
    ]

    for numero, (consulta, referencia) in enumerate(
        casos,
        start=1,
    ):
        try:
            respuesta = consultar_modelo(
                consulta
            )

            pct_crudo, pct_proc = (
                calcular_coincidencia(
                    referencia,
                    respuesta,
                )
            )

            print(f"\n[Caso {numero}]")
            print(
                f"Consulta: {consulta}"
            )

            print(
                f"Coincidencia texto crudo: "
                f"{pct_crudo:.1%}"
            )

            print(
                f"Coincidencia texto procesado: "
                f"{pct_proc:.1%}"
            )

        except Exception as error:
            print(
                f"\n[Caso {numero}] "
                f"Error al consultar modelo: "
                f"{error}"
            )