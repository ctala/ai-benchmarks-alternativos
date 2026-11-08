# GPT-6.1 Terra — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 11.304s | tokens_per_second: 51.1
- input_tokens: 101 | output_tokens: 578

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## El «success» que no hizo nada

Un workflow en verde solo confirma que la ejecución terminó sin un error no gestionado. No garantiza que haya producido el efecto que esperabas.

El caso más común: una consulta devuelve cero items. Los nodos posteriores no reciben datos, no hacen trabajo y la ejecución termina correctamente. También puede pasar que un filtro descarte todos los registros, que una rama del **IF** no reciba ninguno o que una API responda con un HTTP 200 pero incluya un error o una lista vacía en el cuerpo.

Hay casos más engañosos: una operación devuelve un identificador de tarea, pero el procesamiento real ocurre después y falla; o tienes activado *Continue On Fail* y el error queda convertido en datos que nadie revisa.

¿Cómo detectarlo?

1. **Define el resultado esperado.** No basta con «ejecutó el nodo»: ¿cuántos registros debía actualizar, mensajes debía enviar o documentos debía crear?
2. **Cuenta en puntos clave.** Registra items obtenidos, descartados, elegibles y confirmados por el sistema destino. Una diferencia inesperada entre ellos merece atención.
3. **Valida la respuesta, no solo el status HTTP.** Comprueba los campos que confirman el efecto real. Si la operación es asíncrona, verifica después su estado final.
4. **Alerta sobre anomalías.** Por ejemplo: cero registros cuando normalmente hay actividad, o menos confirmaciones que items elegibles. Un Error Trigger no cubrirá estos casos si la ejecución acaba en éxito.
5. **Vigila también la ausencia de ejecuciones.** Si el workflow ni siquiera arranca, necesitas una comprobación externa o un heartbeat independiente.

Revisa el recorrido y los datos de cada rama en las ejecuciones guardadas. Y cuidado con *Always Output Data*: puede mantener vivo el flujo con un item vacío y ocultar que no hubo resultados.