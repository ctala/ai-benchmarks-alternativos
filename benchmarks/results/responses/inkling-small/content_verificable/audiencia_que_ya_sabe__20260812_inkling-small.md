# Inkling Small — content_verificable/audiencia_que_ya_sabe

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 126.143s | tokens_per_second: 13.2
- input_tokens: 109 | output_tokens: 1663

## Respuesta completa

Tu workflow dice **Success** y tu base de datos sigue igual. No es un bug de n8n: es una mentira técnica.

n8n marca una ejecución como exitosa si ningún nodo lanza una excepción. No verifica si tu lógica hizo algo útil. Un nodo **IF** que evalúa a falso, un **Filter** que descarta todo, un webhook que llega con payload vacío o un **Merge** que recibe cero items no rompen la ejecución: simplemente la salta. El resultado es un log verde con *Items: 0* y una sensación de engaño.

Los culpables más frecuentes:

- **Webhook con body vacío o malparseado**: llega, dispara, pero no hay datos que mapear; el flujo corre sobre aire.
- **IF / Switch por la rama *false*** sin acción posterior: el nodo se ejecuta, pero nada fluye.
- **Filter** o **Split In Batches** con array vacío: pasa, pero no pasa nada.
- **Cron** con variables de entorno faltantes: si tienes *Continue On Fail* activo, el nodo HTTP o DB falla en silencio.
- **Merge / Combine** donde un flujo nunca se activó: el nodo une lo que hay, que es nada.

Cómo detectarlo antes de que te enteres por el cliente:

No mires solo el estado de la ejecución. Abre el panel de datos del último nodo y revisa **Items**. Si dice 0, tu workflow fue un *no-op* elegante. Revisa qué nodos aparecen en verde y cuáles en gris: los grises son los que nunca corrieron.

Hazlo *self-reporting*: pon un nodo **Set** o **Code** al final que exponga `items.length`. Si es 0, conecta un nodo **Throw Error** condicional (o un HTTP que avise a Slack/Discord). Así conviertes un "éxito vacío" en fallo explícito.

Revisa los logs individuales en el panel **Execution**: te muestra el flujo real, no solo el resumen. Si usas webhooks, agrega un nodo **Respond to Webhook** que devuelva el count recibido; si llega 0, sabes que el emisor te envió basura.

En resumen: en n8n, **Success** significa *no explotó*, no *funcionó*. Trata el output como tu fuente de verdad, no el color del nodo. Si tu workflow no tiene un nodo de verificación de output, está en modo confianza ciega.