def recomendar_estrategia(respuestas):
    puntos = {
        "RAG": 0,
        "Fine-tuning completo": 0,
        "PEFT": 0,
    }

    if respuestas["informacion_cambia_seguido"]:
        puntos["RAG"] += 3

    if respuestas["problema_de_formato_o_tono"]:
        puntos["PEFT"] += 2
        puntos["Fine-tuning completo"] += 1

    if respuestas["dataset_grande_y_de_calidad"]:
        puntos["Fine-tuning completo"] += 2
        puntos["PEFT"] += 1

    if respuestas["presupuesto_limitado_o_iterar_rapido"]:
        puntos["RAG"] += 2
        puntos["PEFT"] += 1

    if respuestas["necesita_multiples_variantes"]:
        puntos["PEFT"] += 2

    maximo = max(puntos.values())

    ganadoras = [
        tecnica
        for tecnica, p in puntos.items()
        if p == maximo
    ]

    return puntos, ganadoras


# ======================================================
# CASO DEL PROYECTO
# ======================================================

respuestas_mi_caso = {
    "informacion_cambia_seguido": True,
    "problema_de_formato_o_tono": True,
    "dataset_grande_y_de_calidad": False,
    "presupuesto_limitado_o_iterar_rapido": True,
    "necesita_multiples_variantes": False,
}


puntos, ganadoras = recomendar_estrategia(
    respuestas_mi_caso
)

print("Puntajes:")
print(puntos)

print()
print("Candidatas:")
print(ganadoras)


# ======================================================
# DOCUMENTO
# ======================================================

documento = f"""# Decision de personalizacion

## 1. El problema

El proyecto utiliza documentación, contratos y
contenido que cambia periódicamente. Además,
existe una posible necesidad futura de normalizar
solicitudes de eventos en formatos estructurados,
pero actualmente el principal desafío es acceder
a información actualizada y trazable.

## 2. Resultado del metodo de decision

- RAG: {puntos["RAG"]} puntos
- PEFT: {puntos["PEFT"]} puntos
- Fine-tuning completo: {puntos["Fine-tuning completo"]} puntos

Tecnicas recomendadas: {", ".join(ganadoras)}

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
"""


with open(
    "decision_personalizacion.md",
    "w",
    encoding="utf-8",
) as archivo:
    archivo.write(documento)

print()
print("decision_personalizacion.md generado")