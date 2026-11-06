# Límites de autonomía: Agente de documentación y análisis de texto

## Herramientas y nivel de riesgo

- consultar_documentacion_proyecto: bajo (solo consulta información almacenada en una base documental local y no modifica datos ni ejecuta acciones externas).

- contar_palabras: bajo (solo analiza texto proporcionado por el usuario y devuelve una cantidad de palabras; no realiza modificaciones ni genera efectos fuera de la aplicación).

## Herramientas que requieren aprobación humana

Actualmente ninguna herramienta requiere aprobación humana.

Justificación:

- consultar_documentacion_proyecto es una herramienta de solo lectura. Una selección incorrecta puede producir una respuesta poco útil, pero no genera cambios en sistemas ni pérdidas económicas.

- contar_palabras es una herramienta de análisis. Un error en el resultado no modifica datos ni ejecuta acciones irreversibles.

Si en el futuro se agregan herramientas capaces de enviar correos, eliminar información, modificar registros o ejecutar acciones económicas, dichas herramientas deberán incorporar un mecanismo de aprobación humana antes de ejecutarse.

## Revisión de trazas

Frecuencia:

- Revisión semanal de una muestra representativa de interacciones.
- Revisión inmediata de cualquier comportamiento inesperado reportado por un usuario.

Qué se busca:

- Uso repetido de la misma herramienta varias veces seguidas dentro de una interacción.
- Selección de una herramienta que no corresponde con la intención de la consulta.
- Diferencias entre la observación devuelta por la herramienta y la respuesta final generada por el agente.
- Uso innecesario de herramientas cuando la consulta podía responderse directamente.

Las decisiones del agente pueden verificarse mediante la información almacenada en intermediate_steps y mediante los registros de traza cuando estos se encuentren habilitados.

## Qué hacer ante un comportamiento inesperado

1. Revisar la traza completa de la interacción para identificar qué herramienta fue utilizada y con qué argumentos.

2. Confirmar si la herramienta elegida era la adecuada para la consulta realizada.

3. Revisar los docstrings de las herramientas para verificar que describan claramente cuándo deben utilizarse.

4. Ajustar la descripción de la herramienta si se detectan selecciones incorrectas frecuentes.

5. Revisar el prompt del agente para asegurar que las instrucciones de uso de herramientas sean suficientemente específicas.

6. Ejecutar nuevas pruebas manuales verificando el contenido de intermediate_steps.

7. Si una herramienta genera resultados inconsistentes, deshabilitar temporalmente su uso hasta corregir el problema y validar nuevamente el comportamiento.

## Limitaciones conocidas

- El agente depende de las herramientas disponibles; no puede obtener información fuera de ellas.

- El agente puede elegir una herramienta incorrecta si interpreta equivocadamente la intención de una consulta.

- La memoria conversacional, cuando está habilitada, depende de la correcta gestión de session_id para evitar mezclar conversaciones distintas.

- La revisión de trazas ayuda a detectar errores después de ocurridos, pero no reemplaza las pruebas ni la supervisión del comportamiento del agente.