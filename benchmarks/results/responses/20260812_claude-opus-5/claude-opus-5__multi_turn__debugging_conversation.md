# Claude Opus 5 — multi_turn/debugging_conversation

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 6.35 | quality: 7.5
- latency_total: 27.742s | tokens_per_second: 73.8
- input_tokens: 539 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un asistente tecnico experto en APIs y automatizacion. Ayuda a diagnosticar problemas paso a paso.

**user:**

Mi API de OpenRouter me da error 429 todo el tiempo. No puedo hacer ni una llamada.

**assistant:**

Error 429 es 'Too Many Requests' - significa que estas excediendo el rate limit. Vamos a diagnosticarlo:

1. Cuantas requests/minuto estas haciendo aproximadamente?
2. Que modelo estas usando? (algunos tienen limites mas bajos)
3. Estas usando la API key correcta? (las keys gratuitas tienen limites muy bajos)

**user:**

Estoy haciendo como 5 requests por minuto, usando DeepSeek V3. Tengo una API key con creditos pagados, unos $20 de saldo.

**assistant:**

5 req/min con DeepSeek deberia funcionar sin problemas - el limite es 300 RPM. Algo mas esta pasando. Vamos a verificar:

1. Estas reutilizando la misma instancia del cliente o creando una nueva por cada request?
2. Tienes algun retry automatico que podria estar multiplicando los requests?
3. Me puedes mostrar el header completo de la respuesta 429? Especificamente los headers `x-ratelimit-*`

**user:**

Acabo de revisar y resulta que tengo un loop en mi codigo que hace retry infinito cuando recibe un error. Asi que cada 429 genera como 100 requests mas. Pero no se como arreglarlo bien, como deberia implementar los retries?


## Respuesta completa

## 0. Primero: para el sangrado

Antes de tocar código, dos cosas:

1. **Mata el proceso.** Un retry infinito contra un 429 es un *retry storm* clásico: cada fallo genera más carga, que genera más fallos.
2. **Espera 5-10 minutos antes de volver a probar.** Muchos backends escalan la penalización cuando detectan abuso sostenido (ventanas más largas, bans temporales por key/IP). Si pruebas tu fix inmediatamente, vas a seguir viendo 429 y vas a pensar que no funcionó.

---

## 1. Las 4 reglas del retry correcto

| Regla | Por qué |
|---|---|
| **Límite máximo de intentos** (4-5) | Sin tope, un fallo permanente = loop infinito |
| **Backoff exponencial** | Darle tiempo real al servidor de recuperarse |
| **Jitter (aleatoriedad)** | Sin jitter, N clientes reintentan en el mismo instante → *thundering herd* |
| **Solo reintentar lo reintentable** | Reintentar un 401 nunca va a funcionar, solo quema cuota |

---

## 2. Clasificación de errores

Esto es lo que más gente se salta y es lo más importante:

**Reintentables:**
- `408` Request Timeout
- `429` Too Many Requests
- `500`, `502`, `503`, `504` — errores de servidor/gateway
- Errores de red: connection reset, DNS, timeouts de socket

**NO reintentables (fallar rápido y ruidosamente):**
- `400` Bad Request — tu payload está m