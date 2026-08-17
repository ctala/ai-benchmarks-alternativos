# GPT-5.6 Luna — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 6.525s | tokens_per_second: 106.7
- input_tokens: 101 | output_tokens: 696
- judge_score: 5 | justificación: La respuesta es precisa, altamente relevante, ofrece una profundidad significativa con insights útiles, está claramente escrita y organizada, y es extremadamente práctica para un emprendedor.

## Respuesta completa

## Cuando n8n dice `success` y no ocurrió nada

En n8n, `success` significa principalmente: *la ejecución terminó sin una excepción no controlada*. No significa que se haya procesado un item, enviado un correo ni actualizado una fila.

Los falsos positivos más comunes:

- Un `IF` envía todos los items por la rama falsa y esa rama termina sin nodos.
- Un `Code` devuelve `[]`; el workflow continúa correctamente, pero no queda trabajo downstream.
- Un nodo tiene `On Error: Continue` o usa una salida de error y el flujo termina “bien”.
- Un `HTTP Request` recibe `200`, aunque el payload indique `{"ok": false}`.
- La operación es asíncrona: el webhook responde antes de que termine el procesamiento.
- Una escritura devuelve cero filas afectadas porque el filtro no encontró ningún registro.

La solución es dejar de usar el estado de ejecución como métrica de negocio. Añade invariantes explícitas:

```js
const items = $input.all();

if (items.length === 0) {
  throw new Error('Invariant failed: no items to process');
}

return items;
```

Después de cada side effect importante, valida la respuesta: código funcional, identificador creado, `affectedRows > 0` o el campo que realmente pruebe el resultado. Si falla, lanza una excepción; no conviertas el error en un objeto que el flujo pueda ignorar accidentalmente.

También conviene registrar un `correlation_id`, el número de items recibidos/procesados y el resultado de cada operación en una tabla de auditoría o sistema de observabilidad. Para flujos críticos, añade una rama explícita de “processed = 0” y alerta cuando aparezca.

Por último, revisa las ejecuciones con datos de entrada y salida, no solo el badge verde. El indicador útil no es “¿terminó?”, sino “¿se cumplió el efecto esperado?”.