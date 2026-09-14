# Gemini 3.8 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 16.875s | tokens_per_second: 129.4
- input_tokens: 192 | output_tokens: 2184

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

**No. Frena de golpe.** Si metes esos $10.000 hoy, vas a incinerar el dinero. 

Tu cálculo tiene dos errores matemáticos graves que distorsionan por completo la realidad:

---

### 1. El error de la vida media (Lifespan)
Dijiste que un cliente se queda "unos 2 años" (24 meses). Con un churn del 8% mensual, la matemática dice otra cosa:

$$\text{Vida media} = \frac{1}{\text{Churn mensual}} = \frac{1}{0,08} = \mathbf{12,5\text{ meses}}$$

No son 24 meses; es **prácticamente la mitad**. Para que un cliente dure 24 meses, tu churn tendría que ser del 4,1%.

### 2. El error de calcular LTV sobre Facturación y no sobre Margen
El LTV no se calcula sobre el ingreso bruto ($35), sino sobre el **beneficio bruto** que te deja cada usuario tras pagar infraestructura y comisiones. El CAC se paga con margen, no con facturación.

* Margen en dinero por cliente/mes: $\$35 \times 70\% = \mathbf{\$24,50}$

---

### Los Unit Economics Reales

* **LTV Real:** $\frac{\$24,50}{0,08} = \mathbf{\$306,25}$
* **CAC:** $\$290$
* **Ratio LTV / CAC Real:** $\frac{\$306,25}{\$290} = \mathbf{1,06x}$

Tu ratio no es 2,9x. Es **1,06x**. 
Por cada cliente que compras a $290, recuperas $306,25 a lo largo de un año. Estás ganando **$16,25 brutos en 12 meses por usuario**. Cualquier costo operativo fijo adicional (soporte, salarios, herramientas) hace que esa adquisición sea **a pérdida**.

### El Payback Period (Tiempo de recuperación de caja)
* **Meses para recuperar el CAC:** $\frac{\$290}{\$24,50} = \mathbf{11,8\text{ meses}}$

Tardas 12 meses en recuperar los $290 de publicidad, pero la vida media del cliente es de 12,5 meses. Es decir: **el cliente se da de baja casi en el mismo momento exacto en que terminas de pagar el anuncio con el que lo trajiste.**

---

### Qué pasa si metes los $10.000 este mes
1. Traes ~34 clientes ($10.000 / $290).
2. El mes 1 te generan **$833** de margen bruto.
3. Te quedas con un agujero de flujo de caja inmediato de **-$9.167**.
4. Al escalar presupuesto, el CAC suele subir (fatiga de audiencias), lo que empujaría tu ratio por debajo de 1,0x rápidamente.

### Qué debes hacer antes de tocar paid ads:
1. **Atacar el churn (8% mensual es una hemorragia):** En un año retienes apenas el 36% de una cohorte. Si no retienes, estás echando agua en un balde agujereado.
2. **Subir precios o cobrar anual por adelantado:** Si ofreces un plan anual con descuento (ej. $350/año upfront), cobras de golpe y financias el CAC el día 1, eliminando el riesgo de caja.
3. **No escalar paid ads** hasta que tu LTV/CAC real (con margen aplicado) esté sólidamente por encima de **3x** y tu payback sea menor a **6-8 meses**.