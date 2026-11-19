def puntaje_riesgo(
    probabilidad,
    impacto,
):
    return (
        probabilidad
        * impacto
    )


def categoria_riesgo(
    puntaje,
):
    if puntaje >= 15:
        return "CRITICO"

    if puntaje >= 9:
        return "ALTO"

    if puntaje >= 4:
        return "MEDIO"

    return "BAJO"


def esta_en_el_limite(
    probabilidad,
    impacto,
):
    categoria_actual = (
        categoria_riesgo(
            puntaje_riesgo(
                probabilidad,
                impacto,
            )
        )
    )

    vecinos = [
        (probabilidad + 1, impacto),
        (probabilidad - 1, impacto),
        (probabilidad, impacto + 1),
        (probabilidad, impacto - 1),
    ]

    for p2, i2 in vecinos:

        if not (
            1 <= p2 <= 5
            and
            1 <= i2 <= 5
        ):
            continue

        nueva = categoria_riesgo(
            puntaje_riesgo(
                p2,
                i2,
            )
        )

        if nueva != categoria_actual:
            return True

    return False


mis_riesgos = [

    {
        "riesgo":
        "Inyeccion de prompt mediante documentos recuperados",

        "probabilidad": 4,
        "impacto": 4,

        "mitigacion":
        "Filtro de patrones y contexto delimitado (Bloque 31)"
    },

    {
        "riesgo":
        "Informacion desactualizada en el vector store",

        "probabilidad": 3,
        "impacto": 4,

        "mitigacion":
        "Reindexacion periodica e ids explicitos (Bloque 25)"
    },

    {
        "riesgo":
        "Filtracion de informacion sensible mediante logs",

        "probabilidad": 2,
        "impacto": 5,

        "mitigacion":
        "Registro de huellas y longitudes en lugar de contenido (Bloque 31)"
    },

    {
        "riesgo":
        "Incremento excesivo de costo por consumo de tokens",

        "probabilidad": 3,
        "impacto": 3,

        "mitigacion":
        "Registro de latencia y consumo (Bloque 28)"
    },

    {
        "riesgo":
        "Cambios de prompt sin trazabilidad",

        "probabilidad": 2,
        "impacto": 3,

        "mitigacion":
        "Versionado de prompts (Bloque 32)"
    }

]


for r in mis_riesgos:

    r["puntaje"] = (
        puntaje_riesgo(
            r["probabilidad"],
            r["impacto"],
        )
    )

    r["categoria"] = (
        categoria_riesgo(
            r["puntaje"]
        )
    )

    r["al_limite"] = (
        esta_en_el_limite(
            r["probabilidad"],
            r["impacto"],
        )
    )


for r in sorted(
    mis_riesgos,
    key=lambda x:
    -x["puntaje"],
):

    print(
        f"{r['categoria']:8} ({r['puntaje']:2}) - {r['riesgo']}"
    )

print()

for r in mis_riesgos:

    if r["al_limite"]:

        print(
            "revisar con otra persona:",
            r["riesgo"],
        )