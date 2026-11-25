# Accenture2026 – Gate 2: Integración y Orquestación

Proyecto desarrollado durante el Módulo 2 de la Especialización en Inteligencia Artificial.

Este repositorio implementa un flujo RAG (Retrieval-Augmented Generation) completo utilizando Gemini, embeddings, Chroma y recuperación semántica, incorporando además evaluación, observabilidad, seguridad, gobernanza y una decisión fundamentada de personalización.

---

# Funcionalidades implementadas

## RAG

- Chunking mediante RecursiveCharacterTextSplitter.
- Embeddings con Gemini (`gemini-embedding-001`).
- Persistencia local con Chroma.
- Recuperación semántica.
- Construcción dinámica de prompts.
- Soporte para citación de fuentes.

## Evaluación

- Medición de precisión.
- Medición de recall.
- Registro de resultados de evaluación.
- Conjunto de preguntas de validación.

## Observabilidad

- Logging estructurado en JSON.
- Trace ID por consulta.
- Registro de consumo de tokens.
- Registro de latencia.

## Seguridad

- Filtro básico de prompt injection.
- Delimitación explícita de contexto.
- Separación de instrucciones y contexto recuperado.

## Gobernanza

- Versionado de prompts.
- Supervisión humana mediante LangGraph.
- Matriz de riesgos.
- Decisión documentada de personalización.

---

# Requisitos

- Python 3.10 o superior
- Git
- API Key de Gemini

---

# Clonar el repositorio

```bash
git clone https://github.com/RockHero2891/accenture2026.git
cd accenture2026
```

---

# Crear entorno virtual

## Windows

```bash
python -m venv venv
.\venv\Scripts\activate
```

## Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Instalar dependencias

```bash
pip install -r requirements.txt
```

---

# Configurar variables de entorno

Crear un archivo `.env` en la raíz:

```env
GEMINI_API_KEY=TU_API_KEY
```

---

# Estructura principal

```text
src/
├── indexar_corpus.py
├── recuperacion.py
├── evaluacion_recuperacion.py
├── registro_rag.py
├── agente_con_herramientas.py

docs/
├── decision-arquitectura.md
├── limites_autonomia_agente.md
├── limites_metrica.md

vectorstore/

dataset_tuning.py
decision.py
decision_personalizacion.md
logging_rag.py
grafo_supervision.py
matriz_riesgos.py
registro_prompts.py
```

---

# Flujo recomendado

## 1. Indexar el corpus

Genera embeddings y persiste el índice en Chroma.

```bash
python src/indexar_corpus.py
```

Resultado esperado:

```text
Indexados 5 chunks en vectorstore
```

---

## 2. Recuperación semántica

Construye el contexto recuperado y prepara el prompt dinámico.

```bash
python src/recuperacion.py
```

Resultado esperado:

```text
===== PROMPT =====
...
===== CITAS =====
...
```

---

## 3. Evaluar recuperación

Calcula precisión y recall.

```bash
python src/evaluacion_recuperacion.py
```

Genera:

```text
resultados_evaluacion.txt
```

---

## 4. Registrar coste y latencia

Ejecuta consultas instrumentadas.

```bash
python src/registro_rag.py
```

Genera:

```text
registros_latencia_costo.jsonl
```

---

## 5. Logging y trazabilidad

```bash
python logging_rag.py
```

Incluye:

- Trace ID
- Logging JSON
- Registro de consumo
- Mitigación de prompt injection

---

## 6. Versionado de prompts

```bash
python registro_prompts.py
```

Muestra:

- Versiones registradas
- Huellas SHA256 abreviadas
- Diff entre versiones

---

## 7. Supervisión humana

```bash
python grafo_supervision.py
```

Valida:

- Interrupt()
- Command(resume=True)
- Command(resume=False)

---

## 8. Matriz de riesgos

```bash
python matriz_riesgos.py
```

Calcula:

- Probabilidad
- Impacto
- Categoría
- Riesgos al límite

---

## 9. Personalización

```bash
python dataset_tuning.py
```

Valida dataset para PEFT.

```bash
python decision.py
```

Genera:

```text
decision_personalizacion.md
```

---

# Artefactos generados

## Evaluación

```text
resultados_evaluacion.txt
```

## Latencia y coste

```text
registros_latencia_costo.jsonl
```

## Decisión de personalización

```text
decision_personalizacion.md
```

---

# Exclusiones de Git

El proyecto ignora:

```text
.venv/
.env
vectorstore/
```

---

# Estado del Gate 2

Implementadas las dimensiones evaluadas:

- Pipeline RAG funcional
- Recuperación y citación
- Coste y latencia
- Personalización fundamentada
- Observabilidad
- Seguridad y gobernanza

---

# Autor

Gabriel Muñoz

Especialización en Inteligencia Artificial – Accenture 2026