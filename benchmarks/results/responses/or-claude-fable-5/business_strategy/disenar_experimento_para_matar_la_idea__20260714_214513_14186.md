# Claude Fable 5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 6.56 | quality: 8.0
- latency_total: 38.031s | tokens_per_second: 53.9
- input_tokens: 289 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, altamente relevante, ofrece una profundidad significativa con insights prácticos, está claramente organizada y es extremadamente útil para un emprendedor.

## Respuesta completa

## Primero: tu hipótesis tiene un problema antes de testearla

"Pagarían $200/mes por reportes automatizados" ya está parcialmente falsada por el mercado: **AgencyAnalytics, Swydo, DashThis y Whatagraph hacen exactamente esto por $49–150/mes.** Entonces tu hipótesis real, la que hay que matar, es:

> *"Las agencias pequeñas pagarán $200/mes por MI versión de esto, pudiendo pagar $59 por AgencyAnalytics."*

Esa es mucho más frágil. Bien: más fácil de matar rápido.

---

## El experimento: pre-venta con dinero real

Nada de encuestas, nada de waitlists, nada de "¿pagarías por esto?". La gente miente gratis. Solo cuenta la tarjeta.

### Qué haces (7 días, ~$150)

**Días 1–2: Prepara el anzuelo (~$50)**
- Landing de una página (Carrd/Framer): "Reportes de cliente automáticos para agencias. $200/mes." Con 3 pantallazos mockeados en Figma. No construyas nada funcional.
- Un Payment Link de Stripe: **depósito de $100, reembolsable**, para reservar lugar de "cliente fundador" con 50% de descuento el primer año.
- El depósito reembolsable es clave: baja la fricción lo suficiente para que digan sí, pero exige el acto físico de sacar la tarjeta.

**Días 2–5: Outreach directo ($0–100)**
- Lista de 50 agencias pequeñas (5–20 personas). LinkedIn + Clutch + directorios de partners de HubSpot/Google.
- Mensaje frío al dueño o al account manager (quien SUFRE los reportes): *"¿Cuántas horas al mes se van en reportes de clientes? Estoy construyendo X. 15 min de llamada."*
- Meta: **15 llamadas de 15 minutos.**

**En cada llamada, en este orden:**
1. "¿Cómo hacen los reportes hoy?" (si dicen "AgencyAnalytics y nos funciona", anota — cada una de estas es una puñalada a tu hipótesis)
2. "¿Cuánto les cuesta hoy en tiempo/dinero?"
3. Muestra los mocks 3 minutos.
4. **El momento de la verdad:** "Estoy tomando 10 clientes fundadores. $100 de depósito reembolsable, te aseguras $100/mes de por vida en vez de $200. Te mando el link ahora mismo, ¿lo pagas en esta llamada?"

No aceptes "mándamelo y lo veo". Eso es un no educado.

---

## Costo y tiempo total

| Concepto | Monto |
|---|---|
| Landing + dominio | ~$30 |
| Mocks en Figma | $0 (tu tiempo) |
| Sales Navigator 1 mes (opcional) | ~$100 |
| Stripe | $0 |
| **Total** | **~$130–150 y 7 días** |

Contra 2 meses de tu vida, es regalado.

---

## Criterio de muerte (defínelo ANTES, por escrito)

De **15 llamadas cualificadas** (agencia real, decisor real):

- **0–1 depósitos pagados → MATA LA IDEA.** No la pivotes esa semana, no racionalices. Muerta.
- **2 depósitos → muerta a $200.** Quizás vive a $79 compitiendo en precio, que es otro negocio (peor).
- **3+ depósitos (20%+ de conversión con dinero real) → sobrevivió el intento de asesinato.** Ahora sí construye, con 3 clientes de diseño esperándote.

### Señales de muerte adicionales (aunque haya algún depósito):
- 8+ de 15 ya usan una herramienta existente y están conformes.
- El dolor que describen no son los reportes sino otra cosa (facturación, retención de clientes) — mataste esta hipótesis pero encontraste una mejor.
- Nadie puede articular cuántas horas pierde en reportes. Si no miden el dolor, no pagan por quitárselo.

---

## Lo que NO cuenta como evidencia de vida

- "Me encanta, avísame cuando lance" → No.
- 40 emails en una waitlist → No.
- Resultados de