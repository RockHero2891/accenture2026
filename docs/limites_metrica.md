# Límites de la métrica de evaluación

## Qué mide

La métrica compara la coincidencia de palabras entre una respuesta generada y una referencia escrita manualmente. Utiliza precisión, cobertura y F1 sobre texto previamente limpiado y tokenizado.

## Modos de falla conocidos

- Los sinónimos y paráfrasis correctas pueden obtener puntuaciones bajas aunque el significado sea equivalente.

  Ejemplo:
  - Referencia: "El auto es veloz."
  - Respuesta: "El vehículo es rápido."

- Los datos incorrectos pueden obtener puntuaciones relativamente altas cuando el resto del texto coincide.

  Ejemplo:
  - Referencia: "Python fue creado en 1991."
  - Respuesta: "Python fue creado en 1989."

- Las negaciones ausentes o adicionales pueden cambiar completamente el significado sin afectar demasiado la puntuación.

  Ejemplo:
  - Referencia: "Python no es un lenguaje compilado."
  - Respuesta: "Python es un lenguaje compilado."

- Las respuestas incompletas pueden conservar una puntuación aceptable aunque omitan la información principal.

## Muestra revisada

Se revisaron manualmente 10 casos seleccionados a partir de los resultados obtenidos por las métricas:

- 5 casos con menor F1.
- 5 casos con mayor F1.

La revisión utilizó los criterios:

- Corrección factual.
- Completitud.
- Contradicción.

Fecha de revisión: 2026-10-18.

## Recomendación de uso

La métrica F1 es útil para comparar grandes volúmenes de respuestas y detectar posibles desviaciones.

No debe utilizarse como único criterio de evaluación cuando las respuestas incluyan:

- Fechas.
- Números.
- Cifras.
- Nombres propios.
- Negaciones.

En estos casos se recomienda una revisión manual complementaria.
