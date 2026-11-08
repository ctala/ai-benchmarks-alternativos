# Gemini 3.8 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 23.948s | tokens_per_second: 106.9
- input_tokens: 192 | output_tokens: 2561

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

**No le des. Frena de inmediato.** 

Tu plan no solo no tiene un LTV/CAC de 2,9x, sino que está al borde de la quiebra técnica por unidad. La aritmética real muestra que estás prácticamente cambiando un billete de $100 por uno de $105, asumiendo todo el riesgo financiero y sin contar tus costos fijos.

Aquí está la autopsia de tus números:

---

### 1. Los dos errores graves en tu cálculo

1. **La vida útil (Lifetime):** Un churn mensual del 8% **no** equivale a 24 meses. La fórmula matemática de la vida media es $1 / \text{churn}$:
   $$1 / 0,08 = 12,5 \text{ meses}$$
   Asumiste casi el doble de retención de la que realmente tienes.
2. **Ignoraste el Margen Bruto:** El LTV no se calcula sobre la facturación bruta, sino sobre el **beneficio bruto**. Si entregas el servicio con un margen del 70%, el 30% restante se va en servidores y pasarelas de pago; ese dinero no te pertenece para pagar el CAC.

---

### 2. Tus Unit Economics Reales

* **Margen bruto mensual por cliente:** $\$35 \times 70\% = \mathbf{\$24,50}$
* **Vida media del cliente:** $1 / 0,08 = \mathbf{12,5 \text{ meses}}$
* **LTV Real:** $\$24,50 \times 12,5 = \mathbf{\$306,25}$
* **CAC:** $\mathbf{\$290,00}$

> **LTV / CAC Real:** $\$306,25 / \$290 = \mathbf{1,05x}$

Un ratio de **1,05x** significa que a lo largo de toda la vida del cliente solo ganas **$16,25 brutos**. Con esos $16 no cubres soporte, salarios, desarrollo ni herramientas operativas. Estás perdiendo dinero en términos netos.

---

### 3. La métrica letal: Período de Recuperación (Payback Period)

Para recuperar los $290 que gastaste en adquirir al cliente:
$$\text{Payback} = \$290 / \$24,50 = \mathbf{11,8 \text{ meses}}$$

Tardas casi un año en recuperar el CAC. El problema es la retención compuesta:
* Con un churn del 8% mensual, al mes 12 solo sobrevive el $(1 - 0,08)^{12} = \mathbf{36,8\%}$ de la cohorte.
* **Traducción:** Más del **63% de tus clientes cancelarán antes de haber pagado su propio costo de adquisición**. Los pocos que se quedan apenas subsidian a los que se fueron a pérdida.

---

### 4. Qué pasa si metes $10.000 este mes

1. **Agujero de caja:** Adquirirás aproximadamente 34 clientes ($10.000 / $290). Esos 34 clientes te generarán apenas **$833** de margen bruto el primer mes (y esa cifra caerá 8% cada mes siguiente). Habrás sacado $10.000 de tu banco hoy para recuperarlos a cuenta gotas durante un año.
2. **Saturación de pauta:** Al pasar a $10.000 de golpe, tu CAC casi con certeza subirá por pérdida de eficiencia en las audiencias. Si tu CAC sube tan solo a $310, tu LTV/CAC pasa a ser **menor a 1,0** (destrucción directa de capital).

---

### ¿Qué hacer antes de prender la máquina de anuncios?

Tu cuello de botella no es la adquisición, es la retención y la monetización:

1. **Ataca el Churn (8% mensual es insostenible):** Un churn del 8% mensual significa que pierdes casi dos tercios de tu base de clientes cada año. En SaaS B2B lo ideal es <1.5%; en B2C, <4-5%.
2. **Revisa el Pricing:** Si el valor lo justifica, sube el precio o introduce contratos anuales con descuento para cobrar el CAC por adelantado y eliminar el riesgo de payback.
3. **Optimiza el CAC orgánicamente:** Hasta que tu LTV real no supere los **$870** (o tu CAC no baje a **~$100**), escalar con pauta pagada es quemar el dinero.