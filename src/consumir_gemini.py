import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
modelo = "gemini-3.6-flash"

def armar_peticion(pregunta: str):
    """Arma la URL y el body de la petición"""
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={api_key}"
    body = {
        "contents": [
            {"parts": [{"text": pregunta}]}
        ]
    }
    return url, body

def enviar_peticion(url: str, body: dict):
    """Envía la petición y devuelve la respuesta en JSON"""
    respuesta = requests.post(url, json=body)
    return respuesta.json()

def extraer_texto(datos: dict) -> str:
    """Extrae el texto generado desde la respuesta JSON"""
    return datos["candidates"][0]["content"]["parts"][0]["text"]

def obtener_dato_de_prueba(pregunta: str) -> str:
    """Función principal que coordina las demás funciones"""
    url, body = armar_peticion(pregunta)
    datos = enviar_peticion(url, body)
    return extraer_texto(datos)

# Prueba rápida
if __name__ == "__main__":
    print(obtener_dato_de_prueba("Confirma en una frase corta que esta conexión funciona"))
