import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno desde .env
load_dotenv()

def obtener_dato_de_prueba(pregunta: str) -> str:
    # Leer la API key desde .env
    api_key = os.getenv("GEMINI_API_KEY")
    modelo = "gemini-3.6-flash"  # este es el modelo que confirmaste que funciona
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={api_key}"

    # Armar el cuerpo de la petición
    body = {
        "contents": [
            {"parts": [{"text": pregunta}]}
        ]
    }

    # Enviar la petición
    respuesta = requests.post(url, json=body)

    # Convertir la respuesta a diccionario
    datos = respuesta.json()

    # Extraer el texto generado
    return datos["candidates"][0]["content"]["parts"][0]["text"]

# Prueba rápida
if __name__ == "__main__":
    print(obtener_dato_de_prueba("Confirma en una frase corta que esta conexión funciona"))
