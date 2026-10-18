import os
import requests
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()

def armar_peticion(pregunta: str):
    """Arma la URL y el body de la petición, validando la entrada"""
    if not pregunta:
        raise ValueError("La pregunta no puede estar vacía")
    api_key = os.getenv("GEMINI_API_KEY")
    modelo = "gemini-3.6-flash"
    url = f"https://generativelanguage.googleapis.com/v1beta/models/{modelo}:generateContent?key={api_key}"
    body = {"contents": [{"parts": [{"text": pregunta}]}]}
    return url, body

def enviar_peticion(url: str, body: dict):
    """Envía la petición y maneja errores de conexión y formato"""
    try:
        respuesta = requests.post(url, json=body)
    except requests.exceptions.ConnectionError:
        raise RuntimeError("No se pudo conectar con el servicio. Intenta de nuevo en unos segundos.")
    try:
        return respuesta.json()
    except requests.exceptions.JSONDecodeError:
        raise RuntimeError("La respuesta del servicio no llegó en el formato esperado.")

def extraer_texto(datos: dict) -> str:
    """Extrae el texto generado, manejando errores de datos faltantes"""
    try:
        return datos["candidates"][0]["content"]["parts"][0]["text"]
    except (KeyError, IndexError):
        raise RuntimeError("La respuesta no trae el texto generado en el lugar esperado.")

def obtener_dato_de_prueba(pregunta: str) -> str:
    """Función principal que coordina todo el flujo"""
    url, body = armar_peticion(pregunta)
    datos = enviar_peticion(url, body)
    return extraer_texto(datos)

# Prueba rápida con manejo de errores
if __name__ == "__main__":
    try:
        resultado = obtener_dato_de_prueba("Confirma en una frase corta que esta conexión funciona")
        print(resultado)
    except (ValueError, RuntimeError) as error:
        print("No se pudo completar la operación:", error)
