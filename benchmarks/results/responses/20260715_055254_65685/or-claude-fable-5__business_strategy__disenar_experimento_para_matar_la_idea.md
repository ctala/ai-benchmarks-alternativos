# Claude Fable 5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 6.54 | quality: 8.0
- latency_total: 41.083s | tokens_per_second: 57.2
- input_tokens: 289 | output_tokens: 2350
- judge_score: 5 | justificación: La respuesta es precisa, altamente relevante, ofrece una profundidad significativa con un enfoque estructurado en fases, es clara y fácil de entender, y es extremadamente útil para un emprendedor que busca validar rápidamente su hipótesis.

## Respuesta completa

# El experimento que mata tu hipótesis en 2 semanas y ~$150

Tu hipótesis tiene 3 supuestos apilados, y basta que UNO falle para que mueras:

1. Los reportes a clientes son un dolor **suficientemente grande** (no solo molesto)
2. Están dispuestos a pagar **$200/mes** específicamente (no $49)
3. Te comprarían **a ti**, hoy, sin producto maduro

Vamos a atacarlos en orden de barato a caro. Si mueres en la Fase 0, te ahorraste hasta las llamadas.

---

## Fase 0: Muerte por Google (2 horas, $0)

Este mercado ya existe. Busca: AgencyAnalytics, DashThis, Swydo, Whatagraph, Looker Studio (gratis).

**Criterio de muerte:** Si hay 3+ competidores establecidos cobrando $50-100/mes por lo mismo, tu hipótesis de $200 ya no es "¿pagarían por reportes automatizados?" sino "¿pagarían 2-4x el precio de mercado por MI versión?" — que es una hipótesis mucho más frágil. No es muerte automática, pero tienes que reformular: ¿qué haces tú que justifica el delta? Si no puedes responder eso en una frase, para aquí.

---

## Fase 1: 15 conversaciones que NO venden nada (5 días, $0-50)

Contacta 30-40 dueños de agencias pequeñas (LinkedIn, comunidades de agencias, grupos de Slack/Facebook). Consigue 15 llamadas de 20 min.

**Regla de oro:** no menciones tu idea. Pregunta sobre su pasado, no su futuro:

- "¿Cómo hiciste los reportes del mes pasado, paso a paso?"
- "¿Cuántas horas te tomó? ¿Quién lo hizo?"
- "¿Qué has intentado ya para resolverlo?" ← **la pregunta asesina**
- "¿Cuánto pagas hoy por herramientas de reporting?"

**Criterios de muerte (cualquiera de estos):**
- Menos de 8 de 15 lo describen como un problema activo (con horas concretas y frustración real, no "sí, sería útil")
- Nadie ha **intentado ya resolverlo** (pagando algo, contratando a alguien, armando spreadsheets frankenstein). Si el dolor fuera real, ya estarían sangrando dinero o tiempo. Un problema en el que nadie ha invertido nada no vale $200/mes.
- El gasto actual promedio en reporting es <$100/mes. Nadie salta de $0 a $200.

---

## Fase 2: Pídeles plata YA (1 semana, ~$100)

Si sobrevives las fases anteriores, la única evidencia válida es **una tarjeta de crédito**. Las opiniones no cuentan; "yo pagaría eso" es la mentira más común del planeta.

**Cómo, sin construir nada:** venta concierge. A los 15 entrevistados + 15 más:

> "Estoy lanzando un servicio que genera tus reportes de clientes automáticamente. Primeros 5 clientes: $99 el primer mes (después $200), reembolsable si no te sirve. Empiezo el lunes. Aquí está el link de pago."

Tú haces los reportes **a mano** por detrás (Looker Studio + copy-paste). El cliente no lo sabe ni le importa. Costo: un link de Stripe y tus horas.

**Criterios de muerte:**
- **0-1 pagos de 30 pitcheados → mata la idea.** Punto.
- 5+ dicen "me encanta, avísame cuando esté listo" pero no pagan → esa ES la muerte, no la validación. El entusiasmo sin pago es el falso positivo clásico.
- Pagan a $99 pero al mes 2, cuando toca $200, se caen todos → mataste el supuesto del precio (quizá tienes un negocio de $79/mes, que es OTRO negocio).

**Criterio de supervivencia:** 3+ pagos reales de 30 pitcheados. Eso no valida la hipótesis completa, pero te da permiso de gastar el siguiente experimento (no los 2 meses de código todavía).

---

## Resumen

| Fase | Tiempo | Costo | Qué mata |
|---|---|---|---|
| 0. Competencia | 2 horas | $0 | El precio de $200 |
| 1. Entrevistas | 5 días | ~$50 | El dolor |
| 2. Pre-venta concierge | 7 días | ~$100 | La disposición a pagar |

**Total: ~2 semanas, ~$150, cero líneas de código.**

Una advertencia final: el riesgo más grande no es diseñar mal el experimento, es **interpretarlo con caridad**. Escribe tus criterios de muerte HOY, antes de la primera llamada, y mándaselos a alguien que te los recuerde. Si en 2 semanas te encuentras diciendo "bueno, técnicamente solo pagó uno, pero es que el timing...", la hipótesis ya murió y el que no se enteró eres tú.