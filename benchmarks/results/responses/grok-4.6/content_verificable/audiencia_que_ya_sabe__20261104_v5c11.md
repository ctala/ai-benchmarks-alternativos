# Grok 4.6 — content_verificable/audiencia_que_ya_sabe

- model_id: `x-ai/grok-4.6`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 28.876s | tokens_per_second: 57.5
- input_tokens: 301 | output_tokens: 1661

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Tu workflow terminó en verde. El caller recibió 200. El cron no protestó. Y no se envió el mail, no se insertó la fila, no se tocó el CRM.

En n8n, *success* solo dice esto: ningún nodo lanzó una excepción no tragada. No dice que hubiera ítems, que se recorriera el camino de negocio, ni que existiera un side-effect.

Los no-ops más frecuentes:

- **Cero ítems, cero ejecución.** Filter, IF, Switch o un HTTP que devuelve `[]` apagan todo lo de abajo. El grafo “completa”. El runData está hueco.
- **Continue On Fail.** El 500 se convierte en un ítem feo (o en nada) y el workflow sigue hasta el final feliz.
- **Respond to Webhook demasiado pronto.** El cliente ya tiene 200; lo que falle después es otra película.
- **2xx de negocio fallido.** `{ "ok": false }` con HTTP 200. n8n no firma tu contrato.
- **Cableado muerto.** Merge mal unido, Switch sin default, loop sobre lista vacía.

Cómo pillarlo sin esperar al usuario:

Abre la execution y cuenta **ítems por nodo**, no el color. Verde + 0 items = no-op. Duración ridícula (80 ms para un “insert”) es otra bandera. Si no guardas data on success, estás ciego.

No asumas el invariante: **aférmalo**. Un guard al final del camino crítico: si `$input.all().length === 0`, `throw` con mensaje de negocio (“no había facturas”). El rojo aquí es la feature. Parsea el body de las APIs y falla tú. En webhooks, responde *después* del trabajo, o responde 200 y deja un rastro auditable del side-effect (id, timestamp, destino). Métricas sobre el nodo que “debería haber escrito algo”: executions success con 0 items ahí son incidentes, no salud.

Success sin efecto no es un bug del runtime. El grafo corre sobre ítems. Si no hay ítems, no hay trabajo. Trátalo como aserción, no como esperanza.