# Decisión de arquitectura: elección de modelo

Fecha: 18/10/2026

## Modelo elegido

Gemini 3.6 Flash

---

## Diagrama de arquitectura

Ver archivo:

`docs/diagrama_arquitectura.png`

El diagrama describe el flujo completo de la miniaplicación:

Usuario → obtener_dato_de_prueba() → armar_peticion() → enviar_peticion() → Gemini API → respuesta JSON → extraer_texto() → Usuario

Incluye además:

- uso de GEMINI_API_KEY desde `.env`
- manejo de excepciones
- procesamiento de `usageMetadata`
- cálculo de costo estimado

---

## Comparación de candidatos

| Criterio | Gemini 3.6 Flash | Gemini 3.8 Flash |
|-----------|-----------|-----------|
| Coste | Menor | Mayor |
| Latencia | Menor | Mayor |
| Calidad de respuesta | Buena | Muy buena |
| Adecuación para asistente simple | Alta | Alta |
| Complejidad | Menor | Mayor |

---

## Justificación

Elegí Gemini 3.6 Flash para esta miniaplicación porque proporciona un equilibrio adecuado entre costo, velocidad de respuesta y calidad.

El proyecto actual corresponde a un asistente simple capaz de recibir una pregunta, consultar el modelo y devolver una respuesta generada.

Durante esta etapa del programa no existe un requerimiento de razonamiento avanzado que justifique utilizar un modelo más costoso.

Por este motivo prioricé una menor latencia y un menor costo operativo, manteniendo un nivel de calidad suficiente para el caso de uso actual.

---

## Alternativa descartada y por qué

Gemini 3.8 Flash fue considerado como alternativa.

La principal ventaja observada es una mejor calidad de respuesta en tareas complejas y de razonamiento más avanzado.

Sin embargo, para esta miniaplicación la mejora de calidad no compensa el aumento esperado en costo y latencia.

Por esa razón se decidió mantener Gemini 3.6 Flash como modelo de trabajo principal en esta etapa del proyecto.