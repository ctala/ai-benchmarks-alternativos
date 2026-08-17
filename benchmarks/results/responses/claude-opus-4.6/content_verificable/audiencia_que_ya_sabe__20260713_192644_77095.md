# Claude Opus 4.6 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 8.06 | quality: 10.0
- latency_total: 17.921s | tokens_per_second: 29.9
- input_tokens: 124 | output_tokens: 536
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para la audiencia experta, proporcionando soluciones prácticas y detalladas.

## Respuesta completa

# El "success" que miente: workflows que no hacen nada

Tienes un workflow que lleva semanas en verde. Cero errores, cero alertas. Todo bien, ¿no?

Hasta que alguien pregunta por qué no se están actualizando los registros en el CRM desde hace diez días.

## El problema

n8n marca una ejecución como *success* cuando el flujo termina sin lanzar excepciones. Eso es todo. No valida que hayan pasado datos por él ni que algún nodo haya hecho trabajo real.

Un IF que siempre evalúa `false`, un HTTP Request que devuelve un array vacío, un Switch sin coincidencias… todos terminan limpios. El workflow "funcionó". Solo que no hizo absolutamente nada.

## Dónde mirar

Los puntos ciegos más comunes:

- **Ramas muertas en IF/Switch.** La rama `true` tiene quince nodos; la `false` va directo al final. Cuando la condición cambia (un campo renombrado en la API, un valor nulo inesperado), todo el tráfico se desvía en silencio.
- **Nodos que devuelven `[]`.** Un HTTP Request con filtro puede devolver cero resultados legítimamente… o porque la API cambió su esquema de respuesta.
- **Paginación rota.** Solo procesas la primera página y siempre devuelve datos, pero nunca pasa de ahí.

## Qué hacer

Agrega un nodo al final de cada rama crítica que valide explícitamente el output. Si `$input.all().length === 0`, lanza un error con `throw new Error()` dentro de un Code node. Que n8n lo marque como lo que realmente es: un fallo.

Otra opción: envía una métrica (items procesados, registros actualizados) a un canal de Slack o a una hoja de cálculo. Si el número es cero durante X ejecuciones consecutivas, tienes tu alerta.

**Un workflow sin errores no es un workflow que funciona. Es un workflow que no se ha quejado.**