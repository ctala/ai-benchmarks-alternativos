# Nex-N2-Mini — business_audit/retention_sobre_100_interpretacion

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 6.756s | tokens_per_second: 182.6
- input_tokens: 142 | output_tokens: 1234

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No: **114% de “retención de ingresos” no significa que retuviste a más del 100% de clientes**.

En SaaS, ese indicador suele ser **Net Revenue Retention**, o **NRR**. Mide cuánto ingreso conservaste y expandiste **sobre la base de clientes del inicio del periodo**, no cuántos clientes quedaron.

La fórmula típica es:

> **NRR = MRR inicial + expansiones − contracciones − churn / MRR inicial**

Ejemplo simplificado:

- Mes pasado: 40 clientes de pago.
- Este mes: 36 clientes de pago.
- Perdiste 4 clientes, es decir, **logo retention del 90%**.
- Pero los clientes restantes subieron de plan.
- Si las expansiones fueron suficientemente grandes, el NRR puede quedar en **114%**.

Eso significa:

> “De los ingresos que teníamos al inicio, terminamos reteniendo y expandiendo hasta el 114% de ese monto.”

Pero **no significa**:

> “Retuvimos al 114% de los clientes.”

La retención de clientes, en términos de logos, fue:

> **36 / 40 = 90%**

Así que tienes una señal mixta:

- **Bueno:** expansión de ingresos positiva.
- **Preocupante:** estás perdiendo clientes.
- **Riesgo:** el NRR puede estar enmascarando churn.

No deberías dejar de preocuparte por churn. De hecho, ahora conviene mirar estas métricas:

1. **Logo retention / churn de clientes**
   - Ya sabes que bajó de 40 a 36 clientes.

2. **Gross Revenue Retention, GRR**
   - Mide ingresos retenidos sin contar expansiones.
   - Si GRR es bajo, el negocio depende demasiado de upsells para crecer.

3. **NRR por cohorte**
   - Para ver si los clientes nuevos retienen mejor o peor que los antiguos.

4. **ARPA / ARPU**
   - Si el ingreso por cliente sube, puede ser por upgrades legítimos o porque quedaron solo los clientes más grandes.

5. **Motivos de churn**
   - Si pierdes clientes por valor insuficiente, el crecimiento por expansión puede ser temporal.

En resumen: **NRR de 114% es bueno, pero no te permite ignorar churn**. Significa que tus expansiones superaron pérdidas y contracciones, pero tu retención de clientes cayó al **90%** en ese periodo. Lo ideal sería tener tanto una buena retención de clientes como un NRR saludable.