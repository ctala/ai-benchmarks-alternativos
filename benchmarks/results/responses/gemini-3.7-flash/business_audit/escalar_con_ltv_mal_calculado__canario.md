# Gemini 3.7 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 17.928s | tokens_per_second: 114.1
- input_tokens: 192 | output_tokens: 2046

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

**NO. Frena en seco.** 

Tu plan tiene dos errores graves de aritmética financiera. Si metes esos $10.000 este mes, lo que vas a escalar no es tu negocio, es un agujero negro de flujo de caja.

Aquí está el recalculo real de tus unit economics:

---

### 1. Los dos errores en tu cálculo

* **Error 1: La vida del cliente (Lifetime).** 
  Con un churn mensual del 8%, un cliente no dura 24 meses. La fórmula de vida media es $1 / \text{churn}$:
  $$\frac{1}{0,08} = 12,5 \text{ meses}$$
  Asumiste casi el doble del tiempo real.

* **Error 2: Calculaste el LTV sobre ingresos brutos, no sobre margen.**
  No te puedes quedar con los $35 completos porque el 30% se va en servidores y procesadores. Tu contribución real por mes es:
  $$\$35 \times 70\% = \$24,50 \text{ al mes}$$

---

### 2. Tus números reales

* **LTV Real:** $12,5 \text{ meses} \times \$24,50 = \mathbf{\$306,25}$
* **CAC:** $\$290,00$
* **LTV / CAC Real:** $\frac{\$306,25}{\$290,00} = \mathbf{1,05x}$ *(no 2,9x)*
* **CAC Payback (Tiempo de recuperación):** $\frac{\$290}{\$24,50} = \mathbf{11,8 \text{ meses}}$

---

### 3. La autopsia de los $10.000 en anuncios

Si gastas $10.000 hoy con un CAC de $290:
1. Adquieres **34 clientes**.
2. Desembolsas **$10.000 hoy** de tu bolsillo.
3. Esos 34 clientes te generarán apenas **$833 al mes** de margen bruto.
4. Tardarás **12 meses solo en recuperar los $10.000** (en el mes 12 apenas habrás empatado).
5. Tras 12,5 meses (cuando la mayoría haya cancelado), habrás generado **$10.412**.

> **Ganancia neta total tras un año de riesgo operativo:** **$412 dólares.** 

*(Y esto asumiendo el mejor escenario: al meter $10.000 de golpe, el CAC casi siempre sube por saturación de audiencia, por lo que probablemente saldrías en pérdida directa).*

---

### ¿Qué tienes que arreglar antes de meter dinero a pauta?

El problema raíz no es solo el CAC, es el **churn**:
* **8% de churn mensual es mortal.** Significa que pierdes al **63% de todos tus clientes cada año**. Estás intentando llenar un balde que tiene un agujero enorme en el fondo.
* **Tus metas antes de escalar:**
  1. **Bajar el churn a < 3-4% mensual:** Si bajas el churn al 4%, la vida media sube a 25 meses y tu LTV salta a $612 (LTV/CAC = 2,1x).
  2. **Subir precios o cobrar anual por adelantado:** Si cobras $350/año por adelantado con descuento, financias el CAC el día 1 y eliminas el riesgo de flujo de caja.

**Veredicto:** No apruebo el gasto en publicidad. Si metes esos $10.000 hoy, estás comprando ingresos a cambio de destruir tu liquidez.