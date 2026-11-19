import json

from collections import Counter
from google.genai import types


# ======================================================
# DATASET
# ======================================================

ejemplos_raw = [
    (
        "Buscamos una banda para un festival de verano en Concepcion para unas 3000 personas y necesitamos una cotizacion esta semana.",
        {
            "tipo_evento": "festival",
            "prioridad": "alta",
            "requiere_contacto": "si"
        }
    ),
    (
        "Estamos organizando un festival universitario para 2000 asistentes y necesitamos confirmar disponibilidad cuanto antes.",
        {
            "tipo_evento": "festival",
            "prioridad": "alta",
            "requiere_contacto": "si"
        }
    ),
    (
        "Queremos contratar una banda para un festival regional el proximo verano.",
        {
            "tipo_evento": "festival",
            "prioridad": "media",
            "requiere_contacto": "si"
        }
    ),
    (
        "Necesitamos musica en vivo para un evento corporativo de fin de ano para 500 invitados.",
        {
            "tipo_evento": "corporativo",
            "prioridad": "media",
            "requiere_contacto": "si"
        }
    ),
    (
        "Somos una empresa y queremos una presentacion para el lanzamiento de un producto.",
        {
            "tipo_evento": "corporativo",
            "prioridad": "media",
            "requiere_contacto": "si"
        }
    ),
    (
        "Buscamos una banda para una convencion empresarial el mes proximo.",
        {
            "tipo_evento": "corporativo",
            "prioridad": "alta",
            "requiere_contacto": "si"
        }
    ),
    (
        "Estamos organizando un matrimonio para 150 invitados y queremos conocer disponibilidad.",
        {
            "tipo_evento": "matrimonio",
            "prioridad": "media",
            "requiere_contacto": "si"
        }
    ),
    (
        "Necesitamos musica en vivo para una celebracion de matrimonio el proximo enero.",
        {
            "tipo_evento": "matrimonio",
            "prioridad": "media",
            "requiere_contacto": "si"
        }
    ),
    (
        "Tenemos un pub en Concepcion y queremos bandas para los viernes.",
        {
            "tipo_evento": "bar_local",
            "prioridad": "baja",
            "requiere_contacto": "si"
        }
    ),
    (
        "Buscamos musica para una tocata en nuestro bar el fin de semana.",
        {
            "tipo_evento": "bar_local",
            "prioridad": "baja",
            "requiere_contacto": "si"
        }
    ),
    (
        "Queremos contratar una banda para una fiesta privada de 40 personas.",
        {
            "tipo_evento": "evento_privado",
            "prioridad": "media",
            "requiere_contacto": "si"
        }
    ),
    (
        "Estamos organizando una celebracion privada en una parcela familiar.",
        {
            "tipo_evento": "evento_privado",
            "prioridad": "baja",
            "requiere_contacto": "si"
        }
    ),
]


examples = [
    types.TuningExample(
        text_input=texto,
        output=json.dumps(
            salida,
            ensure_ascii=False,
        ),
    )
    for texto, salida in ejemplos_raw
]


# ======================================================
# BALANCE
# ======================================================

def chequear_balance(ejemplos_raw, clave):
    categorias = Counter(
        salida[clave]
        for _, salida in ejemplos_raw
    )

    return categorias


balance = chequear_balance(
    ejemplos_raw,
    "tipo_evento",
)

print("=== BALANCE ===")

for categoria, cuenta in balance.most_common():
    print(f"{categoria}: {cuenta}")

print()


# ======================================================
# VALIDACION
# ======================================================

def validar_dataset(
    examples,
    claves_esperadas,
):
    problemas = []
    vistos = set()

    for i, ej in enumerate(examples):

        if (
            not ej.text_input
            or not ej.text_input.strip()
        ):
            problemas.append(
                f"ejemplo {i}: text_input vacio"
            )

        if (
            not ej.output
            or not ej.output.strip()
        ):
            problemas.append(
                f"ejemplo {i}: output vacio"
            )
            continue

        if ej.text_input in vistos:
            problemas.append(
                f"ejemplo {i}: text_input duplicado"
            )

        vistos.add(
            ej.text_input
        )

        try:
            salida = json.loads(
                ej.output
            )

        except json.JSONDecodeError:

            problemas.append(
                f"ejemplo {i}: output no es JSON valido"
            )

            continue

        for clave in claves_esperadas:

            if clave not in salida:
                problemas.append(
                    f'ejemplo {i}: output no tiene la clave "{clave}"'
                )

    return problemas


problemas = validar_dataset(
    examples,
    (
        "tipo_evento",
        "prioridad",
        "requiere_contacto",
    ),
)

print(
    f"{len(examples)} ejemplos, "
    f"{len(problemas)} problemas encontrados"
)

for problema in problemas:
    print(" -", problema)

print()

print("Primer ejemplo:")
print(examples[0])