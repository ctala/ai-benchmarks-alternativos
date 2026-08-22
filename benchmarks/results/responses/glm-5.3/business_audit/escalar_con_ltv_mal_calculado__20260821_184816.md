# GLM 5.3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 59.597s | tokens_per_second: 75.2
- input_tokens: 206 | output_tokens: 4483

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

No le des. Los números no dan, y el cálculo tiene dos errores grandes.

**Error 1: La vida útil.** Con churn mensual de 8%, la vida promedio de un cliente es 1/0.08 = **12.5 meses**, no 24. Tus propios datos se contradicen: o el churn es 8% y la vida es ~12.5 meses, o la vida es 2 años y el churn real es ~4%. Los dos no pueden ser ciertos a la vez. Revisa tus cohortes y decide cuál es el real.

**Error 2: El margen.** El LTV se calcula sobre utilidad bruta, no sobre ingresos. $35 × 70% = **$24.50/mes** por cliente.

**El recálculo:**
- LTV = $35 × 0.70 / 0.08 = **~$306**
- LTV/CAC = 306 / 290 = **1.06**

No es 2.9 — y de paso, 2.9 está por *debajo* de 3, no por encima. El número real es ~1: estás comprando $1.05 de utilidad bruta por cada $1 de publicidad, repartados a lo largo de más de un año, antes de gastos operativos. Después de opex, cada cliente comprado pierde dinero.

**El dato que más me preocupa — el payback:**
- Recuperas el CAC en 290 / 24.50 = **~11.8 meses**
- Pero solo el 37% de tus clientes sobrevive 12 meses (0.92¹²)
- Traducción: **~63% de los clientes que pagues nunca devuelven su CAC.**

**Qué pasaría con los $10,000:** compras ~34 clientes que generan ~$10,600 de utilidad bruta *total, de por vida*. Ganancia neta del experimento: ~$600 en un año+, antes de opex y sin descontar el valor del dinero en el tiempo. Es capital muerto.

**Incluso en tu escenario más generoso** (vida útil real de 24 meses, churn ~4%): LTV = 35 × 0.7 × 24 = $588, ratio = 2.0, payback ~12 meses. Todavía no justifica "escalar fuerte". Y ojo: el CAC marginal suele *subir* conforme aumentas el gasto, así que el ratio empeora al escalar, no mejora.

**Para que sí le des, necesitas alguna de estas:**
- CAC ≤ ~$100 (ratio de 3 con tus números actuales)
- Churn ≤ ~3% (vida útil de 3+ años)
- ARPU ~$100/mes con el churn actual

**Mi sugerencia:** tu rentabilidad actual viene de canales orgánicos — no la arriesgues metiendo $10k a fondo. Si quieres avanzar, destina $1,500–2,000 como test para medir CAC *por canal*: ese $290 quizás es un promedio que esconde un canal a $120 y otro a $500. Escala solo lo primero.

El plan no muere por la ambición; muere porque 24 meses no sale de un churn de 8%. Arregla la retención o el CAC primero, y la aritmética después te da luz verde.