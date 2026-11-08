# MiMo V2.6 Flash — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 7.3 | quality: 8.0
- latency_total: 121.893s | tokens_per_second: 32.8
- input_tokens: 199 | output_tokens: 4001

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# El experimento que puede matar tu hipótesis: **preventa con dinero real en 7 días**

Tu hipótesis esconde 4 supuestos. No necesitas testear todos: el más caro de estar equivocado es *"pagarían $200/mes"*. Todo lo demás (que el dolor existe, que lo tengan, que los puedas alcanzar) se testea de paso.

**Regla de oro: no aceptes como señal nada que no sea dinero en tu cuenta.** "Me interesa", "avísame cuando salga", "suena útil" = ruido. Es la forma #1 en que los founders mienten para no abandonar.

---

## Qué haces exactamente (7 días)

**Día 1 — Oferta de una página ($0–25)**
Una sola página (Carrd o Framer gratis) con:
- Promesa concreta: *"Reportes de Google Ads, Meta y GA4 entregados a tus clientes automáticamente. $200/mes."*
- **Un mock del reporte final** (Figma o Google Slides, 2–3h de trabajo). Es tu "producto" — no construyas nada de código.
- Mecanismo de cobro real: **Stripe Payment Link.** Cobra el primer mes ($200) con garantía de reembolso total si no lo entregas en 30 días. O alternativa más suave: depósito de $50 acreditado al primer mes.

**Días 2–5 — 50 contactos calificados ($0)**
- Busca dueños de agencias de **2–15 personas** en Clutch, LinkedIn, Google Maps, comunidades (Slacks, grupos de LATAM/España, r/marketingagency).
- Mensaje personalizado de 3 líneas: que resuelves X, que quieres 15 minutos para enseñarte el mock, link a la página.
- **Mínimo 200 mensajes** para conseguir **15–20 conversaciones**. Si no llegas a 15 conversaciones en 5 días, eso ya es un dato (ver criterios).

**Días 3–7 — Llamadas de 15 min**
En cada llamada, en este orden:
1. *"¿Cómo armar hoy el reporte de tus clientes? ¿Cuánto tiempo te toma?"* (mide el dolor real)
2. Muestras el mock.
3. **Cobras.** *"Son $200 el primer mes, con reembolso si en 30 días no está listo. ¿Te paso el link de pago ahora?"*
4. Si dice que es caro → **baja el precio en vivo** hasta que acepte o se niegue. Apunta el número. Eso te da el techo de precio gratis.

---

## Costo y tiempo

| | |
|---|---|
| Página + Stripe | $0 – $25 |
| Mock del reporte | $0 (2–3h) |
| Outreach | $0 (LinkedIn free / Clutch / Google) |
| Ads (opcional, no recomiendo aún) | $0 |
| **Total cash** | **<$50** |
| **Total tiempo** | **15–20h repartidos en 7 días** |
| **Plataformas de código construidas** | **0** |

---

## Criterios de muerte (esto es lo importante)

| Resultado a los 7 días | Decisión |
|---|---|
| **0 de 15 conversaciones pagan $200** | **MUERE la hipótesis.** Si el dolor existiera de verdad, con 15 dueños calificados esperarías ~3 pagos. Ver 0 tiene probabilidad <4% si la tasa real fuera 20%. Es conclusivo. |
| El dolor no existe: "uso Looker Studio, me toma 20 min, está bien" en 8+ de 15 | **MUERE el producto entero**, no solo el precio. No hay problema que resolver. |
| El dolor existe pero **nadie acepta >$50** | **MUERE la hipótesis de $200.** No construyas: un SaaS de $50/mo con agencias pequeñas necesita ~4× más clientes para sobrevivir. Es otro negocio, casi seguro no viable. |
| **<5 conversaciones en 200 mensajes** | **MUERE el canal de venta directa.** No juzgues la idea todavía: mataste el motion, no el producto. Antes de gastar en ads, testea otro canal ($0). |
| **≥3 de 15 pagan $200** | Solo entonces — y solo entonces — empiezas a construir. |

---

## Acelerador: si quieres matarla en 48h y $0

Salta la página. Busca 10 agencias que **ya conozcas** (antiguos clientes, contactos, amigos de industria), llámalos hoy mismo, ensénales el mock en una llamada de 10 minutos y pídeles el pago en vivo. Si de esos 10 nadie saca la tarjeta en 72 horas, la hipótesis ya está muerta y te ahorraste la semana completa.

---

## Lo que NO cuenta como señal

- Emails capturados en una landing (tasa de conversión a pago real: 1–3%)
- "Me apunto a la lista de espera"
- Upvotes en Reddit/HN/Product Hunt
- Tú mismo usando tu herramienta
- Un solo amigo que dice que pagaría

**El objetivo de estas 7 días es darte permiso para abandonar barato — o para construir con la única prueba que importa: alguien te transfirió $200 por algo que aún no existe.**