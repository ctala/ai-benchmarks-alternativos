# Gemini 3.8 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 7.29 | quality: 8.0
- latency_total: 14.459s | tokens_per_second: 100.6
- input_tokens: 126 | output_tokens: 1454

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No, tu interpretación es incorrecta y actuar según esa conclusión sería muy peligroso para tu negocio.**

La métrica del 114% es **Net Revenue Retention (NRR)** —retención neta de ingresos—, no retención de clientes (Logo Retention). 

La lectura correcta de tus datos es la siguiente:

---

### 1. La retención de clientes nunca puede superar el 100%
Físicamente es imposible retener a más del 100% de los clientes existentes: o se quedan (100%) o se van (<100%). Los clientes no se multiplican dentro de su propia cuenta.

Tus números reales de este mes:
* **Logo Churn mensual:** Perdiste 4 de 40 clientes = **10% de churn de clientes en un solo mes**.
* **Retención de clientes (Logo Retention):** **90%**.

Un 10% de churn mensual es una cifra alarmante en SaaS B2B. Si mantienes ese ritmo, habrás perdido a más del **70% de tus clientes actuales en un año**.

---

### 2. Qué significa realmente tu 114% de NRR
Un NRR del 114% solo significa que **el dinero nuevo que pusieron los clientes que ampliaron su plan superó el dinero que perdiste por los 4 que se fueron.**

$$NRR = \frac{\text{MRR inicial} - \text{MRR perdido (churn)} + \text{MRR de expansión}}{\text{MRR inicial}} = 114\%$$

El NRR es una métrica de salud de expansión, pero **puede enmascarar un problema grave de producto.** En tu caso, un puñado de cuentas "power users" está subsidiando el éxodo del resto.

---

### 3. Los riesgos de ignorar esto ahora mismo

1. **Riesgo de concentración:** Tu negocio depende cada vez más de menos clientes. Si el mes que viene uno de los que subió de plan decide marcharse o recortar gasto, tu NRR se desplomará y los ingresos caerán en picado porque la base de clientes es frágil.
2. **El "cubo agujereado":** Si metes todo el esfuerzo en captar clientes nuevos ahora, estarás quemando presupuesto de marketing y ventas (CAC) para llenar un sistema que pierde el 10% de sus usuarios cada 30 días. Tu *Payback Period* se disparará y el *LTV* de la mayoría de clientes será negativo.

---

### Diagnóstico y qué hacer

Tienes tracción y valor real (demostrado por quienes suben de plan), pero tienes un desajuste severo en la base:

1. **No abras el grifo de la adquisición masiva todavía.**
2. **Compara las cohortes:** Analiza qué tienen en común los que subieron de plan frente a los 4 que se fueron. Es muy probable que estés vendiendo a dos perfiles de cliente distintos (ICP) y uno de ellos no encuentra valor en tu software.
3. **Entrevista a los 4 que se fueron:** Necesitas saber si el problema fue onboarding, precio, falta de una funcionalidad clave o que simplemente nunca fueron tu cliente ideal.