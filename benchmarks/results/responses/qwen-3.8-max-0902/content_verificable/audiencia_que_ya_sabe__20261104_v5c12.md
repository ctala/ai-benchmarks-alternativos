# Qwen 3.8 Max 0902 — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 95.873s | tokens_per_second: 53.3
- input_tokens: 148 | output_tokens: 5113

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Un “success” en n8n solo significa que el grafo terminó sin excepción no controlada. No significa que haya pasado algo útil. El caso clásico: el trigger trae items, pero un Filter/IF deja la rama principal vacía; los nodos posteriores no se ejecutan o se ejecutan con cero items, y la ejecución cierra en verde. Otro: una expresión devuelve `[]` o `undefined` y el nodo de escritura lo interpreta como “nada que actualizar”. También pasa cuando el Respond to Webhook se coloca antes de la lógica crítica, cuando una rama de Switch no coincide, o cuando un Error Workflow convierte un fallo en 200 para no romper al cliente.

En el visor, no mires solo el check: abre la ejecución y compara input/output por nodo, run index y nodos omitidos.

La detección no debe depender del status. Convierte el no-op en un estado explícito. En el último nodo, cuenta items reales:

```js
const expected = $('Expected').all().length;
const written = $('Written').all().length;
if (expected > 0 && written === 0) {
  throw new Error('No-op detected');
}
```

Si el cero es válido, define un flag como `{noop:true, reason:'sin cambios'}` y devuelve 200 con ese body. Así diferencias vacío legítimo de vacío accidental.

Agrega métricas de ejecución: execution id, workflow, nodo que decidió, cantidad entrada/salida, hash del payload. Mándalo a un log o canal de ops. En producción, monitoriza “success con written=0” como anomalía, no como OK. Si tu workflow debe crear, actualizar o notificar, el contrato no es HTTP 200; es efecto secundario verificado.