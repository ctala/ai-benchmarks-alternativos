# Gemini 3.7 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.78 | quality: 10.0
- latency_total: 15.338s | tokens_per_second: 116.6
- input_tokens: 192 | output_tokens: 1789

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

**NO. Frena en seco.** Si metes esos $10.000 hoy, vas a incinerar el dinero.

Tu cálculo tiene dos errores matemáticos graves que distorsionan por completo tu realidad:

---

### 1. Los errores en tu aritmética

* **Error 1: La vida útil del cliente (Lifetime).**  
  Con un churn mensual del 8%, la vida media de un cliente no son 24 meses, son **12,5 meses** ($1 / 0,08$). Asumiste el doble de retención de la que realmente tienes.
* **Error 2: Confundiste Facturación con Margen.**  
  El LTV no se calcula sobre los ingresos brutos, sino sobre el **margen de contribución bruto**. No puedes usar el dinero que se va en servidores y pasarelas de pago para pagar el CAC.

---

### 2. El recálculo real

* **Margen bruto mensual por cliente:** $\$35 \times 70\% = \$24,50$
* **Vida media del cliente:** $1 / 0,08 = 12,5\text{ meses}$
* **LTV Real:** $\$24,50 \times 12,5 = \mathbf{\$306,25}$ (no $840)
* **CAC:** $\$290$

$$\text{LTV / CAC Real} = \frac{\$306,25}{\$290} = \mathbf{1,05}$$

---

### 3. El diagnóstico

* **Estás cambiando $290 para recibir $306,25 a lo largo de un año:** Tu beneficio neto por cliente tras recuperar el CAC es de apenas **$16,25**. Eso sin contar salarios, soporte, herramientas ni costos fijos. En términos netos, **estás perdiendo dinero por cada cliente que compras**.
* **El Payback es letal:** Tardas **11,8 meses** en recuperar el CAC ($\$290 / \$24,50$). 
* **El efecto del Churn en el Payback:** Con un 8% de churn mensual, para el mes 12 **solo te queda el 36,7% de la cohorte** ($(1 - 0,08)^{12}$). La gran mayoría de tus clientes se habrán ido *antes* de que recuperes lo que te costó adquirirlos.

---

### 4. Qué pasa si metes los $10.000 este mes:
* Adquieres **34 clientes**.
* En el mes 1 generas apenas **$833 de margen bruto** frente a un desembolso de **$10.000**.
* Tu flujo de caja colapsará antes de que esa cohorte madure.

---

### ¿Qué tienes que arreglar antes de escalar?

Tu problema raíz es el **churn (8% mensual es una fuga masiva)** y un **CAC demasiado alto para un ticket de $35**.

1. **Baja el Churn:** Si reduces el churn al **3% mensual**, la vida sube a 33 meses y tu LTV pasa a **$816** (LTV/CAC = 2,8).
2. **Sube el ARPU / Expansión:** Cobra más o introduce planes anuales con descuento para cobrar por adelantado y eliminar el riesgo de payback.
3. **Baja el CAC:** $290 para un producto de $35/mes no es sostenible a menos que tu retención sea casi perfecta o tu modelo sea B2B anual.