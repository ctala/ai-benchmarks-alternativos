# GLM 5.2 — content_verificable/audiencia_que_ya_sabe

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 40.717s | tokens_per_second: 66.0
- input_tokens: 107 | output_tokens: 2687
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para expertos en n8n, abordando directamente el problema y ofreciendo soluciones prácticas.

## Respuesta completa

Todos hemos estado ahí: el workflow termina en verde, el cron se ejecutó sin pestañear, pero el registro en la base de datos sigue sin aparecer o la API externa no recibió el payload. ¿Por qué n8n celebra un "success" cuando no ha hecho absolutamente nada?

La respuesta es simple: n8n evalúa el éxito de un nodo basándose en si se ejecutó sin lanzar un error interno, no en si realmente procesó datos. Si un nodo recibe un array vacío (0 items), se ejecutará con éxito pero hará cero operaciones.

Esto suele ocurrir por tres motivos:
1. Un nodo *Filter* o *If* descarta todos los items y los manda por una rama muerta.
2. Un nodo *HTTP Request* recibe una respuesta inesperada (ej. `{ "data": [] }` en lugar de un array de objetos) y el mapeo de la siguiente etapa se queda vacío.
3. Un loop que itera sobre cero elementos.

**Cómo detectarlo:**
Deja de confiar en el punto verde. La métrica que importa es el número pequeño que aparece debajo del nombre del nodo. Si dice `0`, tienes un fallo silencioso. 

**Cómo prevenirlo:**
Añade un *Code node* en los puntos críticos de tu pipeline (antes de inserts en DB o llamadas críticas a APIs) con una validación estricta:

```javascript
if (items.length === 0) {
  throw new Error('Payload vacío en [Nombre del Nodo]');
}
return items;
```

Esto forzará el fallo real, disparará tu *Error Trigger* y te ahorrará horas de debuggeo ciego. Recuerda: estar en verde solo significa que el workflow no se rompió, no que haya funcionado.