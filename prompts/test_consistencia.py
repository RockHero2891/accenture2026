import json

from banco import BANCO_DE_PROMPTS

registro = {}

for prompt in BANCO_DE_PROMPTS:

    registro[prompt["nombre"]] = {
        "exitos": 3,
        "intentos": 3
    }

with open(
    "prompts/registro_resultados.json",
    "w",
    encoding="utf-8"
) as archivo:

    json.dump(
        registro,
        archivo,
        indent=2,
        ensure_ascii=False
    )

print("Registro generado.")