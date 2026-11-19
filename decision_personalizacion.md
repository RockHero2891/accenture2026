# Decision de personalizacion

## 1. El problema

El proyecto utiliza documentación, contratos y
contenido que cambia periódicamente. Además,
existe una posible necesidad futura de normalizar
solicitudes de eventos en formatos estructurados,
pero actualmente el principal desafío es acceder
a información actualizada y trazable.

## 2. Resultado del metodo de decision

- RAG: 5 puntos
- PEFT: 3 puntos
- Fine-tuning completo: 1 puntos

Tecnicas recomendadas: RAG

## 3. Tecnica elegida y por que

Se elige RAG como estrategia principal.

La información utilizada por el sistema cambia
con frecuencia mediante contratos, documentación,
eventos y otros contenidos que pueden actualizarse
sin necesidad de reentrenar ningún modelo.

El método de decisión favorece RAG porque permite
iterar rápidamente, mantiene costos bajos y evita
la necesidad de construir un dataset grande y
etiquetado.

PEFT podría incorporarse en una etapa futura para
normalizar automáticamente solicitudes de eventos
o extraer información estructurada desde texto
libre, pero actualmente no resuelve el problema
principal del proyecto.

## 4. Que necesitarias para ejecutarla

Actualmente existe un corpus indexado mediante
RAG y almacenado en Chroma.

Para continuar escalando la solución sería
necesario:

- Mantener actualizado el corpus documental.
- Reindexar documentos nuevos cuando se agreguen.
- Incorporar nuevas fuentes de conocimiento.
- Mantener la persistencia del vector store.

Actualmente existen 12 ejemplos etiquetados
en dataset_tuning.py para una posible solución
basada en PEFT.

Tomando como referencia el umbral utilizado
en esta unidad (200 ejemplos etiquetados y
revisados), faltarían al menos 188 ejemplos
adicionales para llegar a un dataset adecuado
para entrenamiento.

Si cada ejemplo requiriera aproximadamente
5 minutos de preparación y revisión, esos
188 ejemplos representarían cerca de 15,7 horas
de trabajo de etiquetado.

Por ese motivo, en el estado actual del proyecto,
RAG sigue siendo la alternativa más eficiente:
el corpus ya existe, puede actualizarse sin
reentrenamiento y permite incorporar nuevo
conocimiento con tiempos de iteración mucho
menores que una estrategia de PEFT o fine-tuning.
