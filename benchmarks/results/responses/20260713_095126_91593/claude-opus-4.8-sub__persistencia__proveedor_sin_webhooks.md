# Claude Opus 4.8 (suscripción) — persistencia/proveedor_sin_webhooks

- model_id: `claude-opus-4-8`
- success: True  | final: 5.93 | quality: 7.2
- latency_total: 59.523s | tokens_per_second: 47.4
- input_tokens: 4 | output_tokens: 2823

## Respuesta completa

## La respuesta corta

Si la plataforma no te avisa, **te construyes el webhook tú**. Un poller que emula el push: consulta cada X, detecta lo nuevo, y dispara *tu propio* webhook interno. El resto de tu automatización no se entera de la diferencia.

Lo importante es la separación:

```
[Poller / detector]  →  POST a tu webhook interno  →  [Flujo de negocio]
   (lo desechable)          (el contrato)              (lo que te importa)
```

Así, si mañana la plataforma sí lanza webhooks, cambias solo la caja de la izquierda. El flujo de negocio nunca se toca.

## Antes de escribir código: 3 cosas que revisar

La doc dice "no hay webhooks", pero eso casi nunca significa "no hay ninguna señal push":

1. **¿Manda emails de notificación?** Si te llega un correo "tienes un mensaje nuevo", eso *es* un webhook con pasos extra. Buzón dedicado + inbound parsing (Postmark inbound, Mailgun routes, o IMAP idle en n8n) → ya tienes push real, latencia de segundos, cero polling.
2. **¿Su propia app web es tiempo real?** Si el chat te muestra mensajes sin refrescar, hay un websocket/SSE detrás. Abre DevTools → Network → WS. No está documentado, pero existe. Es más frágil que polling (rompe sin aviso), pero como *acelerador* con polling de respaldo funciona.
3. **¿Hay un endpoint de "notificaciones"?** Muchas plataformas sin API pública de mensajes sí exponen un feed de notificaciones. Es más barato de pollear que listar todos los hilos.

Si ninguna aplica: polling. Y se hace bien.

## Cómo se monta el poller (las partes que la gente olvida)

**Watermark durable, no en memoria.** Guardas el último evento procesado en algo que sobreviva un reinicio (NocoDB, Redis, un archivo). Si vive en RAM, el primer deploy te duplica o te pierde eventos.

**Deduplica por ID, no por timestamp.** Los timestamps empatan, llegan con skew, y algunas APIs redondean al segundo. La clave de dedupe es el ID estable del mensaje.

**Ventana con solape, no `>` estricto.** No pidas "todo lo mayor a mi último ID". Pide "los últimos N o los de la última hora", y descarta lo ya visto contra tu tabla de IDs. Suena redundante — es lo que te salva cuando el poller estuvo caído 40 minutos, o cuando la plataforma inserta un mensaje con retraso.

**El consumidor debe ser idempotente.** Asume que el mismo evento va a llegar dos veces alguna vez. Si tu flujo manda un email o cobra algo, esto no es opcional.

**Cadencia: haz la cuenta.** Cada 1 min = 43.200 llamadas/mes. Cada 5 min = 8.640. Decide con dos números: cuánta latencia tolera el negocio de verdad (¿responder en 2 min vs 10 min cambia algo?) y qué te cuesta cada llamada. Y si aplica, polling adaptativo: rápido en horario activo, lento de madrugada.

**Backoff ante errores.** 429/5xx → exponencial, no reintentar en loop. Y un circuit breaker: si la fuente lleva 10 fallos seguidos, avisa y para.

## Lo que realmente te va a morder

**El fallo silencioso.** El poller no "explota": se queda ejecutándose y deja de encontrar nada. Cambió el shape de la respuesta, expiró la cookie, la sesión murió. Todo verde, cero eventos, y te enteras a los 3 días.

Antídoto: **alerta por ausencia, no por error.** Un heartbeat que grite si no hubo *poll exitoso* en X minutos, y una segunda alerta si no hubo *ningún evento nuevo* en un período donde históricamente siempre hay. Es la única métrica que detecta esta clase de fallo.

## Aterrizado a tu stack

Como es tu caso, esto encaja directo:

- **Detector:** workflow n8n con Schedule Trigger → llama al endpoint/actor que lista mensajes o notificaciones.
- **Estado:** tabla en NocoDB (`external_id`, `seen_at`, `processed`) como registro de dedupe y watermark.
- **Emisión:** por cada ID nuevo, POST al Webhook Trigger del workflow de negocio.

Dos workflows separados, a propósito. El detector es infraestructura barata y reemplazable; el de negocio es el que tiene la lógica y el que quieres poder probar disparándolo a mano con un curl.

**Un ojo con esto:** ya tienes un patrón de dos-workflows-mismo-nombre en n8n que te ha mordido antes. Nómbralos explícito (`msg-detector` / `msg-handler`) y no reutilices el nombre.

## Regla que te ahorra dolor

Documenta desde el día uno que **esto es un adaptador, no una integración**. Depende de un comportamiento no contractual de un tercero. Va a romperse. La pregunta no es si, es cuándo — y la respuesta correcta a eso es tener la alerta por staleness, no tener un poller "perfecto".