# Miniaplicación Gemini API

Proyecto desarrollado durante el Módulo 1 de la Especialización en Inteligencia Artificial.

Permite consumir la API de Gemini mediante Python, procesar respuestas JSON, manejar errores comunes y utilizar prompts estructurados.

---

## Requisitos

- Python 3.10 o superior
- Git
- API Key de Gemini

---

## Clonar el repositorio

```bash
git clone https://github.com/RockHero2891/accenture2026
cd accenture2026
```

---

## Crear entorno virtual

### Windows

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Instalar dependencias

```bash
pip install -r requirements.txt
```

---

## Configurar variables de entorno

Copiar el archivo de ejemplo:

```bash
cp .env.example .env
```

o en Windows:

```powershell
Copy-Item .env.example .env
```

Editar `.env` y agregar:

```env
GEMINI_API_KEY=TU_API_KEY
```

---

## Ejecutar

```bash
python src/consumir_gemini.py
```

---

## Estructura del proyecto

```text
src/
docs/
prompts/
```

### src

Contiene el módulo principal:

- armar_peticion()
- enviar_peticion()
- extraer_texto()

### docs

Contiene:

- evidencia de llamadas a la API
- diagrama de arquitectura
- decisión de arquitectura

### prompts

Contiene:

- banco de prompts
- pruebas de consistencia
- registro de resultados

---

## Funcionalidades

- Consumo de API Gemini
- Manejo de errores
- Variables de entorno seguras
- Prompt de sistema
- Salidas estructuradas en JSON
- Banco de prompts reutilizables

---

## Verificación Gate 1

Ensayo de instalación limpia realizado correctamente.

Resultado:
- Repositorio clonado desde GitHub
- Dependencias instaladas desde requirements.txt
- Variables de entorno configuradas mediante .env
- Miniaplicación ejecutada correctamente contra Gemini API

## Autor

Gabriel Muñoz