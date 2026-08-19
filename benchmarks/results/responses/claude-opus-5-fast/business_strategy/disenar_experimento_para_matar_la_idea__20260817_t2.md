# Claude Opus 5 Fast — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 6.57 | quality: 8.0
- latency_total: 24.191s | tokens_per_second: 177.9
- input_tokens: 289 | output_tokens: 4304

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# El experimento: vender el resultado a mano antes de escribir una línea de código

Tu hipótesis real no es "les gustaría". Es: **una agencia pequeña saca la tarjeta y paga $200/mes recurrentes por esto.** Todo lo que no termine en un cobro real es teatro.

Presupuesto: **$0–150. Plazo: 7 días corridos.**

---

## Día 0 — El pre-test gratis (2 horas). Puede matarla antes de empezar.

Abre AgencyAnalytics, DashThis, Whatagraph, Databox y Looker Studio. Anota precios y qué integran.

**Criterio de muerte #0:** si después de 2 horas no puedes escribir en **una sola frase** por qué una agencia dejaría su herramienta actual (o Looker Studio, que es gratis) para pagarte $200 — no tienes un producto, tienes una función de un producto que ya existe. Detente acá y ahorra los 2 meses.

Si sobrevives, sigue.

## Día 0 — Lista de 60 agencias (3 horas)

Clutch.co, LinkedIn (filtro: agencias de 3–15 empleados), directorios locales, grupos de Slack/Facebook de agencias. Nombre, email, fundador.

**Criterio de muerte #0.5:** si no logras armar 60 nombres reales con contacto en 3 horas, tienes un problema de distribución que ningún producto arregla.

## Día 1 — El activo (3 horas, $0)

**No hagas una landing con captura de emails.** Un email es gratis, no prueba nada, y te va a dar un falso positivo que te va a costar 2 meses.

Haz esto en cambio:
- Una página en Carrd/Notion con la oferta concreta.
- Un mockup del reporte en Canva/Figma (2h).
- **Un link de pago de Stripe activo, $200, cobro inmediato.**

La oferta textual: *"Piloto cerrado: 3 agencias. $200/mes, primer reporte en 7 días, cancelas cuando quieras."*

## Días 1–5 — 60 contactos, objetivo 12–15 conversaciones

Email corto o DM. Nada de "¿te interesaría una herramienta que…?". Pregunta por el pasado, no por el futuro:

> "¿Cómo armaste el reporte del mes pasado para tus clientes? ¿Cuánto te tomó?"

En la llamada (15 min), **pide que compartan pantalla y te muestren el último reporte real.** Es el único dato que no miente.

Las 5 preguntas:
1. Muéstrame el reporte de tu cliente más grande del mes pasado.
2. ¿Quién lo armó y cuántas horas le tomó? (real, no estimado)
3. ¿Qué usas hoy y cuánto pagas?
4. ¿Qué probaste antes y por qué lo dejaste?
5. ¿Cuántos clientes tienes y cuál es el retainer promedio?

Y después, el cierre. **No preguntes "¿pagarías $200?".** Di:

> "Estoy corriendo 3 pilotos este mes. $200/mes, primer reporte en 7 días. Te mando el link de pago ahora, ¿lo tomas?"

Silencio. Que respondan ellos.

---

## Los criterios de muerte (escríbelos ANTES de empezar)

| Señal | Qué significa | Acción |
|---|---|---|
| **0 de 15 conversaciones pagan en 7 días** | Nadie compra a $200 | **Abandonar el precio o la idea** |
| >60% ya usan una herramienta y están "bien" | Problema suficientemente resuelto | **Abandonar** |
| Tiempo real reportado < 3h/mes por agencia | El dolor vale $50, no $200 | **Abandonar el precio** |
| Tasa de respuesta al outreach < 10% con lista buena | No es un dolor top-of-mind | Amarillo fuerte |
| Cada agencia te muestra un formato radicalmente distinto | El producto es servicio, no software | **Repensar todo** |
| 3+ pagos en 7 días | Sigue al día 8 | Continuar |

**Regla de honestidad:** "me dijo que le encanta y que lo pruebe cuando esté listo" = **NO**. Cuéntalo como rechazo. Un "sí" sin tarjeta es un no educado.

---

## Días 8–35 — El experimento que realmente mata la idea (si sobreviviste)

Si conseguiste 2–3 pagos: **entrega los reportes a mano.** Tú, con Looker Studio, Excel y 4 horas de trabajo por cliente. Concierge puro. Cero código.

Esto testea las dos cosas que te van a hundir en el mes 3 de desarrollo y que ninguna encuesta te va a revelar:

**1. El infierno de las integraciones.** Vas a pedirles acceso a Google Ads, Meta, GA4, el CRM, HubSpot, la plataforma de email. Si tardas 3 semanas en conseguir credenciales, si la mitad de las APIs requieren app aprobada por Meta (spoiler: sí, y toma meses), si cada cliente tiene fuentes distintas — **tu proyecto de 2 meses es de 10.** Eso es un kill signal de viabilidad, no de demanda.

**2. La renovación del mes 2.** Es el único dato que importa.

**Criterio de muerte final: si de 3 pilotos no renueva al menos 1 al segundo mes, abandona.** Retención cero con entrega manual perfecta significa que el producto automatizado tampoco retiene.

---

## Lo que NO hagas

- **Landing page + "déjanos tu email"** → señal falsa, cuesta 0 al usuario.
- **Encuesta "¿pagarías $200/mes?"** → la gente miente sobre el futuro sistemáticamente. Nadie miente sobre su tarjeta.
- **Preguntarle a amigos o a tu red cercana** → te van a decir que sí por cariño.
- **Un MVP "chiquito" de 2 semanas** → siguen siendo 2 semanas más de las que necesitas para saber.

---

## Resumen

| | |
|---|---|
| **Costo** | $0–150 (Stripe, dominio, tal vez trial de Sales Navigator) |
| **Tiempo hasta primer veredicto** | 7 días |
| **Tiempo hasta veredicto duro** | 35 días |
| **Ahorro si falla** | ~2 meses de tu vida |

---

## Una advertencia sobre cómo vas a interpretar los resultados

Si el resultado es negativo, tu cerebro te va a ofrecer tres salidas: *"el precio estaba mal"*, *"apunté al segmento equivocado"*, *"mi pitch fue malo"*. A veces son verdad. Por eso:

**Antes de empezar, escribe tu predicción numérica:** "de 15 conversaciones espero X pagos". Y escribe qué vas a cambiar si falla y **cuántas iteraciones te permites** (sugerencia: dos — un ajuste de precio, un ajuste de segmento). Si después de tres versiones del experimento sigues en cero pagos, el problema no es el experimento.

El experimento más caro no es el que falla. Es el que diseñaste para no poder fallar.