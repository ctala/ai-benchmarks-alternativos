# Qwen 3.6 35B base (OpenRouter FP8) — persistencia/proveedor_sin_webhooks

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 6.44 | quality: 6.94
- latency_total: 65.21s | tokens_per_second: 31.4
- input_tokens: 191 | output_tokens: 2048

## Respuesta completa

Cuando una plataforma no da webhooks, la única vía es el **polling con estado**. Pero no cualquier polling: uno que sea idempotente, que no te queme la API y que no pierda mensajes si el proceso cae.

Te lo monto en 4 bloques operativos:

### 🔹 1. Patrón base: `Polling + State + Idempotencia`
```
[Scheduler] → [Poller] → [Estado: last_id/timestamp] → [Filtro de duplicados] → [Disparar flujo]
```
- **No consultes siempre desde cero.** Usa `?after=<last_id>` o `?since=<timestamp>` si la API lo permite. Si no, pide los últimos N y haz sliding window.
- **Guarda el estado** en un store ligero y persistente: DynamoDB, Redis, Postgres, o incluso un archivo JSON si es local. Clave: `platform_name:inbox:last_processed_id`.
- **Procesa solo lo nuevo.** Si la API devuelve mensajes en orden diferente o reenvía un lote, la deduplicación evita doble ejecución.

### 🔹 2. Frecuencia y límites
- **Intervalo:** 30s–5min según tu SLA de latencia. Empieza conservador (1–2 min) y ajusta.
- **Backoff exponencial:** Si la API responde 429/5xx, espera `base * 2^attempt` con jitter.
- **Límite de intentos:** Máx 3–4 reintentos antes de ir a dead-letter y alertar.

### 🔹 3. Infraestructura recomendada (elige según tu stack)
| Opción | Cuándo usarla | Componentes |
|--------|---------------|-------------|
| **Serverless** | Quieres cero ops, escala automática | EventBridge Schedule → Lambda → DynamoDB (estado) → Step Functions / SNS → tu flujo |
| **Self-hosted** | Control total, datos sensibles, stack Python/Node | Cron/systemd timer → script con `requests`/`asyncio` → SQLite/Redis → colas (RabbitMQ/Kafka) |
| **Low-code** | Validación rápida, presupuesto flexible | Make/Zapier con módulo "Schedule" + "Polling" + "Router" (cuidado con límites de ejecuciones y costos) |

### 🔹 4. Trampas reales y cómo evitarlas
| Problema | Solución |
|----------|----------|
| **Mensajes perdidos si el poller cae** | Usa un `last_seen_timestamp` + consulta `created_at > last_seen`. Al recuperar, procesa en lote y actualiza el estado solo tras confirmación. |
| **Duplicados por reintentos** | Marca cada mensaje con `process_id` o `message_id`. Antes de ejecutar, verifica en una tabla de `processed_ids` con TTL (ej. 24h). |
| **La API cambia el orden o paginate inconsistente** | No confíes en índices numéricos.