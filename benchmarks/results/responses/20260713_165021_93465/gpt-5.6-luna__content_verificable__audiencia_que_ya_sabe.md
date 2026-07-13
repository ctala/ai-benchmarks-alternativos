# GPT-5.6 Luna — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 7.54 | quality: 8.14
- latency_total: 5.594s | tokens_per_second: 106.4
- input_tokens: 101 | output_tokens: 595
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para expertos en n8n, abordando el problema de manera exhaustiva y ofreciendo soluciones prácticas.

## Respuesta completa

## El workflow terminó en `success`. El problema es que no hizo nada.

En n8n, `success` significa, esencialmente, que ningún nodo lanzó un error no gestionado. No significa que se haya creado el registro, enviado el email o actualizado el CRM.

Hay varias formas de obtener un falso positivo:

- Un `IF` envía cero items por una rama y el workflow termina correctamente.
- Un `Split in Batches` o un loop recibe una lista vacía.
- Un `HTTP Request` devuelve `200` o `202`, aunque el payload contenga `{"ok": false}`.
- `Continue On Fail` convierte un error operativo en datos que el flujo sigue procesando.
- Un `INSERT ... ON CONFLICT DO NOTHING` no falla, pero tampoco inserta nada.
- Un servicio externo acepta la petición y procesa el trabajo de forma asíncrona, sin garantizar el resultado final.

La solución es dejar de usar la ausencia de excepciones como criterio de éxito. Añade comprobaciones explícitas de negocio:

```js
const items = $input.all();

if (items.length === 0) {
  throw new Error('Se esperaban resultados, pero llegaron 0 items');
}

return items;
```

Para respuestas HTTP, valida también el cuerpo, no solo el status code. Para operaciones de escritura, comprueba `rowsAffected`, un ID generado o una respuesta inequívoca del proveedor. Si una condición no se cumple, usa un nodo **Stop And Error** en lugar de permitir que el flujo “termine bien”.

También conviene registrar métricas mínimas: cantidad de items de entrada y salida, IDs afectados, duración y respuesta del sistema externo. Y, cuando el proceso sea asíncrono, separa “petición aceptada” de “operación completada”.

Un workflow observable no solo responde: “no exploté”. Responde: “procesé N elementos y puedo demostrar qué cambió”.