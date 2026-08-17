# Claude Opus 5 Fast — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 4.739s | tokens_per_second: 136.7
- input_tokens: 159 | output_tokens: 648

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

# El "success" que miente

Tu ejecución sale verde. El log dice success. Y el registro nunca llegó a Airtable.

Esto pasa más de lo que crees, y casi siempre por las mismas tres razones.

**1. El nodo se ejecutó con cero items.**

Si un nodo anterior filtra todo, los nodos siguientes no fallan: simplemente no corren. n8n los marca como ejecutados y sigue. Tu HTTP Request nunca disparó, tu Airtable nunca insertó, y la ejecución termina en verde porque técnicamente nada rompió.

**2. La API respondió 200 con un error dentro del body.**

Clásico de Salesforce, HubSpot, muchas APIs internas. Status 200, y en el JSON un `{"success": false, "errors": [...]}`. El nodo HTTP Request solo mira el código HTTP. Todo lo demás le da igual.

**3. Continue On Fail activado y olvidado.**

Lo pusiste para debuggear hace tres meses. Sigue ahí. Ahora los errores viajan como items normales con una propiedad `error` que nadie revisa.

**Cómo detectarlo**

Añade un IF después de cada operación crítica que valide *el resultado*, no la ejecución. ¿El insert devolvió un ID? ¿El array de respuesta tiene longitud? Si no, lanza un Stop and Error explícito.

Para el caso de los cero items, un nodo NoOp con nombre descriptivo en la rama vacía del filtro te ahorra media hora de debugging cuando revises el historial dentro de seis semanas.

Y revisa tus flujos en producción buscando Continue On Fail. Vas a encontrar más de los que recuerdas haber activado.

**La regla:** una ejecución verde te dice que n8n no se rompió. No te dice que tu proceso ocurrió.