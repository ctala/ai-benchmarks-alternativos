# GLM 5.3 — content_verificable/audiencia_que_ya_sabe

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.35 | quality: 10.0
- latency_total: 45.938s | tokens_per_second: 71.9
- input_tokens: 107 | output_tokens: 3305

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## Verde no significa que pasó nada

En n8n, una ejecución es "success" cuando termina sin lanzar errores. Eso es todo. Si ningún item llegó al final, o tu rama crítica nunca se ejecutó, sigue siendo verde. Los sospechosos habituales:

- **"Always Output Data"**: un nodo que devuelve 0 items cortaría la ejecución ahí. Con esta opción activa, emite un item vacío y todo lo demás sigue corriendo con nada.
- **200 OK con error en el body**: el HTTP Request solo falla por status code. Si el backend responde `200` con `{"error": "..."}` o un array vacío, tu workflow es verde y no hizo nada.
- **IF/Filter que nunca matchea**: el cron dispara, el nodo de lectura devuelve datos, pero ninguna condición se cumple. Fin de ejecución. Success. Cero trabajo.
- **Error output conectado a nada**: "Continue (using error output)" convierte fallos en datos. Si no los tratas, el workflow termina feliz.

Cómo cazarlo:

1. **Sentinel**: un Code node que haga `throw` si `items.length === 0` en el punto donde debe haber datos. Para validar a mitad de flujo, `$('Node').all().length` es tu amigo. Convierte el silencio en error.
2. **Valida el body, no el status**: tras cada HTTP Request, un IF que compruebe que la respuesta contiene lo que esperas, no solo que llegó.
3. **Alerta por omisión**: no te limites al error workflow. Notifica también cuando una ejecución "exitosa" procesó 0 items. El fallo más peligroso es el que no hace ruido.

Regla mental: el verde solo te dice que no explotó. Comprobar que trabajó es cosa tuya.