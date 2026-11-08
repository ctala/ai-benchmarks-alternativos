# GLM 5.3 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.81 | quality: 8.0
- latency_total: 106.002s | tokens_per_second: 62.6
- input_tokens: 194 | output_tokens: 6641

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# El experimento: preventa concierge en 2 semanas

**La lógica:** si una agencia no te paga $200/mes cuando *tú, un humano*, les entregas los reportes perfectos y sin esfuerzo de su parte — una oferta estrictamente mejor que cualquier software — tampoco pagarán por el software. El único dato que mata o salva la hipótesis es **dinero cambiando de manos por algo que no existe**. Todo lo demás son opiniones.

---

## Día 0: escribe el criterio de muerte ANTES de empezar

Antes de tocar nada, escribe esto y mándaselo a alguien (cofundador, amigo, tu fridge):

> "Si tengo 30 conversaciones calificadas y **2 o menos pagan el primer mes por adelantado**, la hipótesis muere. No construyo. No 'itero el pitch'. No 'espero a que madure el mercado'."

Esto es lo más importante del experimento. Sin pre-registro, tu cerebro va a renegociar contigo cuando veas los datos.

## Días 1–2: la oferta (no el producto)

Una página en Notion + un **link de pago de Stripe** listo para cobrar en el momento en que alguien diga sí. La oferta:

> "Reportes de clientes para tu agencia, con tu marca, semanales o mensuales, sin que toques nada. $200/mes, cancela cuando quieras. Tomo 10 clientes fundadores; es beta, el onboarding lo hago personalmente contigo. Arrancamos la próxima semana."

Si alguien paga, cumples a mano (Looker Studio + sus exportaciones): ~1–2h por cliente al mes. Aguantable con 5 clientes durante un test. Y honesto: no estás mintiendo, es una beta con onboarding manual.

**Nota antes de escribir la página:** pasa 2 horas mirando AgencyAnalytics, Swydo, Whatagraph. No para copiar. Porque si la mayoría de tus entrevistados ya paga $99 por uno de esos, tu hipótesis real no es "pagarían por reportes automáticos" sino "cambiarían a un desconocido por $200". El experimento no cambia; la lectura del resultado sí.

## Días 3–4: la lista

150 agencias que cumplan **las tres** condiciones (esto es crítico, o vas a testear en la población equivocada):
- 2–20 personas
- 3+ clientes en retainer
- Hacen reportes recurrentes hoy (no "les gustaría hacerlos")

Fuentes: LinkedIn (búsqueda manual), directorios tipo Clutch, grupos de Facebook/WhatsApp de agencias y community managers, referidos. Costo: $0–50.

## Días 5–14: 30 conversaciones

Meta: **30 conversaciones reales con el decisor**. Outreach directo: "trabajo con agencias chicas en reportes de clientes, ¿te robo 10 minutos?". Tasa de respuesta esperada: 15–25%.

En la llamada, tres preguntas de diagnóstico y el cierre:

1. "¿Cuántos clientes en retorno mensual tienen?"
2. "¿Quién arma los reportes hoy y **cuántas horas al mes** le toma en total?"
3. "¿Qué han probado para automatizarlo? ¿Por qué lo dejaron o por qué siguen con eso?"

Luego, sin pedir perdón por el precio:

> "Estoy tomando 10 lugares de clientes fundadores a $200/mes, primer mes por adelantado. ¿Te aparto uno?"

Que te cuelguen es parte del test.

---

## Costo y tiempo

| Concepto | Costo |
|---|---|
| Página + Stripe | $0 (Notion) o ~$15 dominio |
| Lista | $0–50 |
| Outreach manual | $0 |
| **Total de bolsillo** | **<$100** |
| **Tiempo** | **~2 semanas, 60 horas** |

vs. 2 meses construyendo + lo que cueste descubrirlo después.

---

## El veredicto

| Resultado en 30 conversaciones calificadas | Decisión |
|---|---|
| ≤2 pagan | **Muere.** Problema de segmento o precio, no de producto. El código no lo resuelve. |
| 3–4 pagan | Zona gris: revisa precio y segmento antes de escribir una línea de código. |
| ≥5 pagan (≥17%) | Señal de vida. El siguiente riesgo es churn, no demanda — ese es otro experimento. |

¿Por qué 10% como línea? Son conversaciones calificadas, cálidas, con entrega inmediata y descuento de fundador. Si eso no cierra 10%, tu adquisición en frío a escala será mucho peor.

**Señales de muerte que matan aunque la gente pague:**
- El tiempo típico en reportes es <3h/mes por agencia → el dolor cuesta menos de lo que cobras. ROI no cierra nunca.
- La mayoría responde "usamos Looker Studio con una plantilla, gratis, funciona" → el dolor ya está resuelto a costo cero.

---

## Trampas en las que vas a caer (todos caemos)

- **"Me dijeron que está buenísimo"** → vale cero. Solo cuentan pagos.
- **"Prefieren pagar en enero"** → ruido.
- **"Me lo comprarían con X feature"** → ruido hasta que paguen por la feature.
- **"Me ofrecerían $50"** → eso no es ruido, eso es el resultado: mata la hipótesis del precio tal como la formulaste.
- **La trampa suprema:** mover la meta después de ver los datos. Por eso la escribiste el día 0.

Si sales con 5 agencias pagando $200/mes, entras a los 2 meses de código con clientes, ingresos y churn data real. Si sales con cero, perdiste $100 y dos semanas — no 2 meses. Esa asimetría *es* el experimento.