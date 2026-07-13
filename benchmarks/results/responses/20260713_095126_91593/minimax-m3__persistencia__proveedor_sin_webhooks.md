# MiniMax M3 — persistencia/proveedor_sin_webhooks

- model_id: `minimax/minimax-m3`
- success: True  | final: 6.89 | quality: 6.94
- latency_total: 6.644s | tokens_per_second: 67.1
- input_tokens: 335 | output_tokens: 446

## Respuesta completa

Construye un polling agent en tu propio servidor: un worker que consulta la API de la plataforma cada N segundos, compara contra el último estado conocido, y cuando detecta algo nuevo ejecuta el flujo.

Las piezas:

1. **Persistencia de estado** — guarda el `last_seen_id` o timestamp del último mensaje procesado (Redis, SQLite, lo que tengas).
2. **Worker con scheduler** — un proceso que se despierta cada N segundos (cron, APScheduler, Celery beat, `while True + sleep`).
3. **Endpoint de la plataforma** — llamas tú al endpoint de mensajes/list, con tu token, pidiendo lo más reciente.
4. **Diff y trigger** — comparas con `last_seen_id`, lo que no conozcas es nuevo, lo persistes, y disparas tu flujo.

Dos cosas a decidir:

- **Intervalo de polling** — depende del SLA que necesites. Cada 30s es razonable para cosas tipo chat; cada 5min si son tickets o pedidos. Más frecuente = más carga y más coste de API (revisa rate limits).
- **Manejo de duplicados y fallos** — el worker debe ser idempotente (no procesar dos veces el mismo ID) y tolerante a fallos transitorios (retry con backoff).

El esqueleto mínimo en Python:

```python
import time, requests

LAST_SEEN_ID = load_last_seen()  # de Redis/SQLite

while True:
    msgs = requests.get(API_URL, headers=auth_headers).json()
    new = [m for m in msgs if m["id"] > LAST_SEEN_ID]
    for m in new:
        trigger_flow(m)
    if new:
        LAST_SEEN_ID = max(m["id"] for m in new)
        save_last_seen(LAST_SEEN_ID)
    time.sleep(POLL_INTERVAL)
```

Cuando te pregunten "y la eficiencia?" — la honestidad técnica es: es menos elegante que un webhook y consume cuota de API constantemente, pero es la solución correcta cuando el proveedor no te da otra. La alternativa de revisar emails o scraping es peor en todos los ejes.