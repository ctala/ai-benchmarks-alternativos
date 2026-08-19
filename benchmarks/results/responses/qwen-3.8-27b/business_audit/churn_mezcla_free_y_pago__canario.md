# Qwen 3.8 27B — business_audit/churn_mezcla_free_y_pago

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 7.79 | quality: 10.0
- latency_total: 579.177s | tokens_per_second: 14.1
- input_tokens: 227 | output_tokens: 8192

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de retención. Antes de interpretar una métrica, verificas qué población está midiendo realmente.

**user:**

Estoy en pánico. Mi plataforma reporta un churn del 31% este mes y pensé que estaba en 5%. ¿Qué hago?

Datos que me da el panel:
- Usuarios totales que se dieron de baja este mes: 62
- Usuarios totales a inicio de mes: 200
- Churn reportado: 31%

Detalle que encontré exportando la tabla:
- De los 200 usuarios, 178 están en el plan gratuito y 22 son de pago.
- De las 62 bajas, 60 eran del plan gratuito y 2 eran de pago.

¿Qué tan grave es? Dame un plan.


## Respuesta completa



Primero: **no estás perdiendo un 31% de tus clientes de pago**. Estás viendo un churn del **31% de todos los usuarios**, y tu base está muy sesgada hacia el plan gratuito.

Tu panel no está mintiendo matemáticamente: **62 / 200 = 31%**.  
El problema es que está mezclando dos poblaciones muy distintas: **free** y **pago**.

---

## 1. Recalcula el churn por segmento

| Segmento | Usuarios a inicio | Bajas | Churn |
|---|---:|---:|---:|
| Total | 200 | 62 | **31.0%** |
| Gratuito | 178 | 60 | **33.7%** |
| De pago | 22 | 2 | **9.1%** |

Fórmulas:

- **Free churn**: 60 / 178 = **33.7%**
- **Paid churn**: 2 / 22 = **9.1%**
- **Total churn**: 62 / 200 = **31.0%**

El 31% es un promedio ponderado, pero no es el churn que debería usarse para medir la salud del negocio si tu ingreso viene de los usuarios de pago.

---

## 2. ¿Qué tan grave es?

Depende de qué estabas midiendo cuando decías “pensé que estaba en 5%”.

### Caso A: El 5% era tu objetivo de churn para usuarios de pago

Entonces la lectura es esta:

- Objetivo: **5% mensual de pago**
- Real: **9.1% mensual de pago**
- Esperado en 22 usuarios: 22 × 5% = **1.1 bajas**
- Real: **2 bajas**

Es decir: **estás por encima del objetivo, pero la diferencia es pequeña en términos absolutos**: alrededor de **una cuenta de pago extra** respecto al objetivo.

Con solo **22 usuarios de pago**, una sola baja mueve el churn un **4.5%**, y dos bajas lo llevan al **9.1%**. Por lo tanto, hay ruido estadístico. No es necesariamente una crisis estructural, pero sí es una señal que hay que investigar.

**Gravedad para ingresos: naranja.**  
No es un colapso del 31%, pero un churn de pago del 9% mensual sí es alto si se mantiene.

---

### Caso B: El 5% era tu objetivo de churn total, incluyendo free

Entonces el problema no es solo retención, sino **definición del KPI**.

Un churn total del 5% incluyendo usuarios gratuitos es probablemente un objetivo mal calibrado, porque los usuarios free suelen tener más churn que los de pago, especialmente si son nuevos, si no se activan o si son solo top-of-funnel.

**Gravedad para medición: roja.**  
Tu panel actual te está asustando con un KPI que no separa free de pago.

---

## 3. Lo que sí importa para tu negocio

Si los 22 usuarios de pago son tu base que genera ingresos, entonces tu métrica principal no debería ser “churn total de usuarios”, sino:

- **Paid logo churn**: cuántas cuentas de pago se van.
- **MRR churn**: cuánto ingreso recurrente pierdes.
- **Net MRR churn**: pérdida neta considerando upgrades, downgrades y nuevos pagos.
- **Free activation**: cuántos usuarios gratuitos llegan a usar el producto.
- **Free-to-paid conversion**: cuántos free se convierten en pago.
- **D7 / D30 retention**: cuántos usuarios siguen activos a 7 y 30 días.

Si todos tus usuarios de pago pagan lo mismo, entonces:

- **Paid logo churn = 9.1%**
- **MRR churn ≈ 9.1%**

Si pagan distintos planes, necesitas calcularlo con MRR:

\[
\text{MRR churn} = \frac{\text{MRR perdido por bajas}}{\text{MRR a inicio del mes}}
\]

Ejemplo:

- MRR inicial de los 22: \$2,200
- Las 2 bajas sumaban: \$200
- MRR churn: 200 / 2,200 = **9.1%**

Si las 2 bajas eran planes grandes, el impacto puede ser mayor. Si eran planes pequeños, puede ser menor.

---

## 4. Diagnóstico rápido

Tu situación real parece ser esta:

1. **Tu churn total es alto: 31%.**
2. **Pero viene casi todo del