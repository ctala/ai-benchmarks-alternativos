# Mistral Large 4.0 — business_audit/retention_sobre_100_interpretacion

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 37.822s | tokens_per_second: 51.0
- input_tokens: 136 | output_tokens: 1930

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Esa lectura es incorrecta, y es justo el tipo de trampa que hace que el 114% parezca halagador cuando en realidad está ocultando un problema grave.

Lo que tu panel probablemente está midiendo es **retención neta de ingresos (NRR, Net Revenue Retention)**, no retención de clientes. Son métricas distintas:

- **Retención de clientes (logo retention)** = clientes que siguen / clientes al inicio.
  Con tus datos: 36 / 40 = **90%**. Es decir, tienes un **churn del 10% mensual**.
- **NRR** = (ingresos al inicio + expansión − contracción − churn) / ingresos al inicio.
  Tu 114% dice que, *en términos de dinero*, la base que te queda paga un 14% más que el mes pasado.

Ambas cosas son ciertas a la vez: **pierdes clientes, pero los que se quedan pagan más**. El 114% no significa que "no se te va nadie"; significa que el upsell de los supervivientes está compensando (en ingresos) la fuga de los 4 clientes.

### Por qué no puedes dejar de preocuparte por el churn

1. **Un churn del 10% mensual es catastrófico si se sostiene.** Si esa tasa se repite, en 12 meses retendrías solo el ~28% de tus clientes (0,9¹² ≈ 0,28). No hay modelo de SaaS sano que sobreviva con ese ritmo de fuga de logos.

2. **El 114% puede estar enmascarando concentración de riesgo.** Si los 4 que se fueron eran de plan bajo y los 36 que quedan subieron de plan, el NRR brilla, pero tu base se está volviendo dependiente de pocos clientes grandes. Si uno de esos grandes se va el mes que viene, el NRR se desploma.

3. **Meter todo en captación con ese churn es quemar dinero.** Estás llenando un cubo con agujeros. Cada cliente nuevo que captas tiene un CAC; si a los 3–4 meses se va (porque tu churn mensual es del 10%), nunca recuperas esa inversión. El LTV se erosiona y el payback del CAC se vuelve infinito.

### Lo que deberías mirar ya

- **GRR (Gross Revenue Retention)**: excluye la expansión. Con churn del 10% y posibles downgrades, tu GRR está probablemente por debajo del 90%, lo que confirma que el negocio base se está contrayendo en clientes.
- **Churn por segmento**: ¿se fueron los de plan básico? ¿los nuevos? ¿los de cierto sector? El patrón te dice si es un problema de producto, de onboarding o de fit de mercado.
- **Concentración de ingresos**: ¿qué % del MRR total representan tus 5 clientes más grandes? Si es alto, el 114% es frágil.

**Conclusión práctica:** no reasignes todo el esfuerzo a adquisición. Primero diagnostica por qué se van esos 4 clientes al mes y estabiliza la retención de logos. Un NRR del 114% con churn del 10% mensual es una señal de alerta, no de celebración. La expansión es buena, pero no puede ser el único motor mientras pierdes un décimo de tu base cada mes.