# GLM 5.3 — business_audit/retention_sobre_100_interpretacion

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.92 | quality: 8.0
- latency_total: 52.249s | tokens_per_second: 74.7
- input_tokens: 138 | output_tokens: 3904

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

# No, en los dos puntos — y tus propios números lo demuestran

El 114% es **retención neta de ingresos (NRR)**: incluye las subidas de plan. Es un métrico de expansión, no de fidelidad. Y la retención de clientes, por definición, no puede superar el 100%: no puedes retener a más clientes de los que tenías.

## Lo que dicen realmente tus datos

| Métrica | Cálculo | Resultado |
|---|---|---|
| Retención de clientes (logo) | 36 / 40 | **90%** |
| Churn mensual de clientes | 4 / 40 | **10%** |
| GRR (retención bruta de ingresos) | ingresos retenidos sin contar subidas | **< 100%** (perdiste clientes que pagaban) |
| NRR | GRR + expansión | **114%** |

Ejemplo ilustrativo (asumiendo ticket uniforme de $100): mes pasado facturas $4.000 con 40 clientes. Se van 4 (−$400). Varios suben de plan (+$960). Resultado: NRR = (4.000 − 400 + 960) / 4.000 = 114%. El churn está ahí, dentro del número — **la expansión lo está tapando, no eliminándolo**.

## Por qué no puedes ignorar el churn

1. **10% mensual es alto.** Si se mantiene, en un año conservas solo ~28% de tu base (0,9¹²). Es un cubo con una fuga seria.
2. **Concentración de riesgo.** Ahora dependes de menos clientes, y especialmente de los que subieron de plan. Si uno de esos se va, el golpe es mucho mayor que hace un mes.
3. **La expansión tiene techo.** No puedes subir de plan a los mismos clientes indefinidamente. Si el churn estructural continúa mientras la expansión se agota, ese 114% se desinfla.
4. **Los que se van son información.** Probablemente hay dos segmentos distintos: uno que encuentra valor creciente y otro que no. Ignorar el churn es ignorar dónde no tienes product-market fit.
5. **Muestra pequeña.** Con 40 clientes, ese 114% puede ser efecto de 2-3 subidas puntuales. Un mes no es tendencia.

## Lo que sí es buena noticia

NRR > 100% significa que crecerías incluso sin captar a nadie nuevo. El motor de expansión funciona. Eso es genuinamente valioso — pero es una razón para *también* cuidar la retención, no para abandonarla: los clientes que suben de plan son exactamente los que no quieres perder.

## Qué haría yo

- **Separa el GRR del NRR en tu panel.** NRR 114% con GRR 98% es excelente. NRR 114% con GRR 88% es "expansión tapando fugas" — historias muy distintas.
- **Analiza quiénes se fueron los 4:** ¿plan de entrada? ¿perfil concreto? ¿primeros 90 días?
- **Mide churn por cohortes** durante al menos 3 meses antes de sacar conclusiones.

Respuesta directa a tu pregunta: no, no puedes dejar de preocuparte por el churn. Tienes un problema de fuga de clientes que hoy es invisible porque la expansión lo compensa — y esa es justo la situación en la que el problema se detecta tarde.