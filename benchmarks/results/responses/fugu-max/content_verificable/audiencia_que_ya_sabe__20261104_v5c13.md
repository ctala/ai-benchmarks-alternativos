# Fugu Max — content_verificable/audiencia_que_ya_sabe

- model_id: `sakana/fugu-max`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 9.786s | tokens_per_second: 82.6
- input_tokens: 192 | output_tokens: 808

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## El workflow terminó bien. ¿Hizo algo?

En n8n, `success` significa que la ejecución terminó sin un error no gestionado. No garantiza que haya ocurrido el efecto que te importa.

Un filtro puede descartar todos los ítems y dejar sin trabajo a los nodos siguientes. Una rama del `IF` puede no recibir ninguno. Un nodo puede manejar el error y continuar. Y una API puede responder `200` aunque haya rechazado la operación a nivel de negocio o no haya cambiado nada. En todos esos casos, la ejecución puede parecer correcta.

La clave es comprobar resultados, no solo estados.

- **Cuenta los ítems en puntos críticos.** Registra cuántos entran y salen de filtros, ramas y bucles. Un cero inesperado es una señal, no un detalle.
- **Define qué significa “hecho”.** Por ejemplo: se creó un registro, se envió un mensaje o se actualizaron N elementos. Comprueba ese resultado explícitamente, en vez de asumirlo por la respuesta del nodo.
- **Haz visibles los casos vacíos.** Si un filtro puede dejar la salida en cero, habilita *Always Output Data* cuando tenga sentido y evalúa después si llegó un ítem válido. Otra opción es diseñar una ruta explícita para “no hubo coincidencias”.
- **Falla ante invariantes rotas.** Si el workflow debía procesar al menos un elemento y no lo hizo, genera un error deliberado o envía una alerta. Así no se confunde un no-op inesperado con una ejecución normal.
- **Mide el efecto externo.** Contrasta la respuesta de la API con una consulta posterior o con el estado esperado, especialmente en operaciones críticas.

Una buena señal de monitorización no es solo “la ejecución terminó”, sino “se cumplió la condición de negocio”.