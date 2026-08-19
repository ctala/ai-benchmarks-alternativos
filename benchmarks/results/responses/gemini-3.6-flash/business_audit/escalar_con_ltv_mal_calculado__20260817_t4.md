# Gemini 3.6 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 18.139s | tokens_per_second: 175.1
- input_tokens: 194 | output_tokens: 3177

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

**Detén las máquinas. No le des.** 

Si pones $10.000 en publicidad este mes con estos números, vas a financiar una ilusión de crecimiento que destruirá tu caja. Tu cálculo de LTV tiene **tres errores graves de aritmética e hipótesis** que destruyen por completo la viabilidad del negocio.

Aquí está el desglose de lo que realmente pasa cuando recalculated tus números:

---

### Error 1: De dónde sacas que un cliente dura 2 años?
El ciclo de vida promedio de un cliente (*Lifespan*) no se asume, se calcula con la tasa de churn:
$$\text{Vida media (meses)} = \frac{1}{\text{Churn mensual}} = \frac{1}{0,08} = \mathbf{12,5\text{ meses}}$$

Un cliente no se queda 24 meses. Se queda **12,5 meses**. Acabas de duplicar la vida de tu cliente en tu cabeza.

---

### Error 2: El LTV se calcula sobre el Margen Bruto, no sobre los Ingresos
El *Lifetime Value* es el beneficio bruto que te deja un cliente, no la facturación. No puedes usar los $35 completos porque entregar el servicio te cuesta un 30%.

* **Margen Bruto mensual por cliente:** $35 \times 70\% = \mathbf{\$24,50/mes}$
* **LTV Real:** $24,50 \times 12,5\text{ meses} = \mathbf{\$306,25}$

Tu dijiste que tu LTV era de **$840**. La realidad es que es de **$306,25**.

---

### Error 3: El LTV/CAC Real
Volvamos a calcular tu ratio con los datos reales:

$$\text{LTV/CAC Real} = \frac{\$306,25}{\$290} = \mathbf{1,05x}$$

Un ratio de **1,05x** significa que por cada cliente que compras a $290, recuperas $306,25 a lo largo de un año y medio. Ganaste **$16,25 brutos en un año**. 

Esa ganancia no te alcanza ni para pagar la luz de la oficina, los sueldos del equipo, las herramientas de software ni las devoluciones. **Estás operando en pérdidas operativas por cada cliente pagado.**

---

### El golpe de gracia: El tiempo de recuperación (Payback Period)

Para recuperar los $290 que te cuesta adquirir un cliente generando $24,50 de margen al mes:

$$\text{Payback} = \frac{\$290}{\$24,50} = \mathbf{11,8\text{ meses}}$$

Tardas **12 meses solo en recuperar lo que invertiste en publicidad**. 

Aquí está el desastre: con un churn del 8% mensual, **solo el 36,7% de tus clientes sobreviven hasta el mes 12**. 
Esto significa que **el 63% de los clientes que adquieras se van a ir ANTES de que hayas recuperado el costo de su publicidad**. Los clientes que se quedan tienen que pagar la deuda de los que se fueron.

---

### ¿Qué pasa si metes $10.000 este mes?

1. Compras unos **34 clientes** ($10.000 / $290).
2. Te generan **$833/mes** de margen bruto acumulado.
3. El mes que viene, el 8% de esos clientes se van (te quedan 31).
4. Para cuando recuperes (teóricamente) esos $10.000 dentro de un año, más del 60% de esos 34 clientes ya no existirán. 
5. **Resultado:** Has congelado $10.000 de caja hoy para destruirlos lentamente durante el próximo año.

---

### Diagnóstico y Condiciones para Aprobar el Plan

Tienes una fuga masiva en el cubo (Churn) y una inconsistencia de precios respecto a tu CAC. No aceleres un coche que tiene las ruedas desalineadas.

**Para que te apruebe escalar publicidad, necesitas arreglar una de estas tres cosas:**

1. **Ajustar el Precio/ARPU:** Para un CAC de $290, un ticket de $35/mes es bajísimo a menos que vendas un contrato anual pagado por adelantado. Si cobras el año por adelantado ($35 x 12 = $420), eliminas el riesgo de Payback y financias tu CAC el Día 1.
2. **Atacar el Churn (Urgente):** Un 8% mensual es perder casi el 63% de tu base de clientes al año. Tienes que bajar ese churn a menos del **3% - 4% mensual**.
3. **Reducir el Payback:** Necesitamos que el tiempo de recuperación del CAC sea **menor a 5-6 meses**.

**Veredicto:** **Plan RECHAZADO.** Trabaja en la retención o cambia tu modelo de cobro a planes anuales antes de poner un solo dólar en Ads.