# GPT-OSS 20B — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.1 | quality: 8.0
- latency_total: 4.737s | tokens_per_second: 407.9
- input_tokens: 228 | output_tokens: 1932
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un plan detallado y práctico para refutar la hipótesis con un enfoque en costos y tiempo mínimos.

## Respuesta completa

## Experimento “kill‑your‑hypothesis”  
**Objetivo:** Descubrir, en menos de 5 días y por menos de 50 USD, si *ninguna* agencia de marketing pequeña estaría dispuesta a pagar **$200/mes** por una herramienta de automatización de reportes.

> **Resultado que “mata” la hipótesis**  
> - 0/10 agencias respondieron afirmativamente a la pregunta “¿Estarían dispuestas a pagar $200/mes?”  
> - 1 o 2 agencias dijeron que sí, pero solo si la herramienta fuera *gratis* o “de prueba”.  
> - 0/10 agencias mostraron interés en un plan de pago, aunque sea a menor precio.  

Si cualquiera de los tres puntos anteriores se cumple, la hipótesis queda refutada (en el sentido de que el mercado no está dispuesto a pagar esa cantidad).  

---

## Paso a paso (≤ 5 días, ≤ 50 USD)

| Día | Acción | Herramientas | Costo | Comentarios |
|-----|--------|--------------|-------|-------------|
| 1 | **Diseña una landing page ultra‑simple** (Carrd, Notion, o un “Landing Page” de 1‑página en Webflow con plan gratuito). | Carrd (free) | 0 | Incluye: <br>• Título: “Automatiza tus reportes en 5 min” <br>• Beneficios: “Sin trabajo manual”, “Entrega instantánea” <br>• CTA: “Prueba gratis 14 días” <br>• Formulario: Nombre, email, nombre de agencia, “¿Estarías dispuesto a pagar $200/mes?” (sí/no) |
| 1 | **Integra un formulario de pago mínimo** (Stripe Checkout o PayPal). | Stripe (free) | 0 | Solo para la prueba: crea una “suscripción” de $200/mes con opción de cancelar en 14 días. No necesitas bancarización real; Stripe te permite “prueba de pago” sin cargo real. |
| 1 | **Crea una campaña de anuncios de prueba** (LinkedIn Ads o Facebook Ads). | LinkedIn Ads (budget mínimo 10 USD) | ≈ 10 USD | Target: “Marketing agencies”, “Agency owners”, “Agency managers”, “Nationality: US/UK/CA/EU”, “Size: 1‑10 empleados”. Crea dos anuncios: <br>• Anuncio 1: “Reportes automáticos – 14 días gratis” <br>• Anuncio 2: “¿$200/mes por reportes automáticos?” |
| 1‑3 | **Envía 5 correos “cold” a agencias pequeñas** (usa Hunter.io o LinkedIn Sales Navigator, pero con 5 contactos que ya tengas). | Gmail + Hunter (free tier) | 0 | Plantilla: <br>“Hola X, soy Y de Z. Tenemos una herramienta que automatiza los reportes para agencias de 1‑10 personas. ¿Te interesaría pagar $200/mes o prefieres algo gratuito?” |
| 1‑3 | **Publica en grupos de Slack/Discord de agencias** (ej. *Agency Hackers*, *Marketing Agency Mastermind*). | Slack/Discord | 0 | Mensaje corto: “¿$200/mes por reportes automáticos? ¿Qué opinan?” |
| 3‑5 | **Monitorea respuestas** – 10 días de prueba de 14 días (puedes cerrar la campaña antes). | Google Sheets/Typeform | 0 | Registra cada respuesta: nombre, agencia, “sí/no a $200/mes”, comentario. |
| 5 | **Analiza** – si 0/10 “sí”, o 1/10 “sí” pero con requisito de prueba gratuita, la hipótesis se “mata”. | Excel/Sheets | 0 | Si la hipótesis se mantiene (≥ 3 agencias dispuestas a pagar $200/mes sin condiciones), entonces el experimento no “mata” la hipótesis. En ese caso, debes continuar con un MVP. |

---

## Presupuesto estimado

| Concepto | Costo |
|----------|-------|
| Carrd (free) | 0 |
| Stripe (free) | 0 |
| LinkedIn Ads | 10 USD |
| Anuncios de prueba (Facebook) | 0 (puedes usar el mismo presupuesto en LinkedIn) |
| Herramientas gratuitas (Gmail, Google Sheets, Slack/Discord) | 0 |
| **Total** | **≈ 10 USD** |

> **Nota:** Si tu presupuesto es de 50 USD, puedes duplicar el alcance (más anuncios, más correos) o agregar un pequeño “incentivo” a las respuestas (por ejemplo, un cupón de descuento del 20 % para quien complete la prueba). Eso no cambia la lógica del experimento.

---

## Resultados “killer”

| Resultado | Acción |
|-----------|--------|
| 0/10 agencias dicen “sí” | **Hypothesis killed** – el mercado no paga $200/mes. |
| 1/10 agencias dicen “sí”, pero solo si es gratis | **Hypothesis killed** – no hay disposición a pagar. |
| 0/10 agencias muestran interés en un plan, aunque sea a menor precio | **Hypothesis killed** – el precio es demasiado alto. |
| ≥ 3 agencias “sí” sin condiciones | **Hypothesis not killed** – la idea todavía viable, procede con MVP. |

---

## Por qué este experimento “mata”

1. **Rápido**: la campaña dura solo 5 días y la configuración es instantánea.
2. **Barato**: máximo 10 USD en anuncios, todo lo demás es gratuito.
3. **Concreción**: la pregunta directa (“¿$200/mes?”) elimina ambigüedades.  
4. **Decisión**: cualquier respuesta negativa o condicionada es suficiente para cancelar la idea, ya que tu hipótesis es “pagarán $200/mes”.

---

> **Bottom line:** Si recibes más de 0/10 “sí” o 1/10 “sí” con condición de prueba gratuita, no vale la pena seguir con la construcción de la herramienta. Pon el dinero y el tiempo en algo que sí responda a la necesidad real de las agencias.