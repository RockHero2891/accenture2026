BANCO_DE_PROMPTS = [
    {
        "nombre": "clasificar_sentimiento",
        "system_instruction": (
            "Responde únicamente en JSON válido. "
            "Debe contener las claves "
            "'sentimiento' y 'confianza'."
        ),
        "ejemplo_usuario": (
            "El servicio llegó tarde pero el producto está perfecto."
        ),
        "claves_esperadas": [
            "sentimiento",
            "confianza"
        ]
    },

    {
        "nombre": "resumen_corto",
        "system_instruction": (
            "Responde únicamente en JSON válido. "
            "Debe contener las claves "
            "'resumen' y 'confianza'."
        ),
        "ejemplo_usuario": (
            "La inteligencia artificial permite automatizar tareas y procesar información."
        ),
        "claves_esperadas": [
            "resumen",
            "confianza"
        ]
    },

    {
        "nombre": "clasificar_categoria",
        "system_instruction": (
            "Responde únicamente en JSON válido. "
            "Debe contener las claves "
            "'categoria' y 'confianza'."
        ),
        "ejemplo_usuario": (
            "Necesito ayuda para recuperar mi contraseña."
        ),
        "claves_esperadas": [
            "categoria",
            "confianza"
        ]
    }
]