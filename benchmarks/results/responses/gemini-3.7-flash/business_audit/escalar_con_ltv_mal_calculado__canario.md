# Gemini 3.7 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 17.882s | tokens_per_second: 113.7
- input_tokens: 192 | output_tokens: 2034

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

**No. Ni se te ocurra meter esos $10.000 todavía.**

Tu cálculo tiene dos errores matemáticos graves que transforman lo que crees que es una máquina de imprimir dinero en un pozo sin fondo.

Vamos a rehacer los números:

---

### Los dos errores en tu cálculo

1. **La vida del cliente no son 24 meses:**
   Con un churn mensual del 8%, la vida media de un cliente ($1 / \text{Churn}$) es:
   $$\frac{1}{0,08} = \mathbf{12,5 \text{ meses}}$$
   *(Asumiste el doble de retención de la que realmente tienes).*

2. **Olvidaste aplicar el Margen Bruto al LTV:**
   El LTV no se calcula sobre la facturación bruta; se calcula sobre el margen de contribución. De los $35/mes, a ti te quedan $24,50 ($35 \times 70\%$).

---

### La aritmética real de tu negocio

* **LTV Real:**
  $$\text{LTV} = \frac{\text{Precio} \times \text{Margen}}{\text{Churn}} = \frac{\$35 \times 0,70}{0,08} = \frac{\$24,50}{0,08} = \mathbf{\$306,25}$$

* **LTV / CAC Real:**
  $$\frac{\$306,25}{\$290} = \mathbf{1,05x}$$
  *(No es 2,9x. Es prácticamente 1:1).*

* **CAC Payback Period (Tiempo de recuperación):**
  $$\frac{\$290}{\$24,50/\text{mes}} = \mathbf{11,8 \text{ meses}}$$

---

### ¿Qué pasa si metes los $10.000 este mes?

1. Adquieres **34 clientes** ($\$10.000 / \$290$).
2. Esos 34 clientes te generarán, a lo largo de toda su vida útil (y descontando el costo del servicio), un total acumulado de **$10.412**.
3. **Ganancia neta total del experimento tras más de un año:** **$412**.
4. **Impacto en caja:** Quemas $10.000 en el día 1, y tardas **12 meses solo en recuperar el capital invertido**. El más mínimo fallo en cobros, un pequeño aumento en el CAC al escalar, o costos fijos operativos, y esta campaña te generará pérdidas netas inmediatas.

---

### Diagnóstico

El problema raíz es que **tienes un balde roto**:
* Un churn mensual del **8%** significa que pierdes al **63% de tu base de clientes cada año**.
* Tratar de escalar con publicidad pagada teniendo un churn del 8% mensual y un Payback de 12 meses es quemar dinero para tapar fugas.

### Qué hacer antes de escalar:
1. **Atacar el Churn:** Si bajas el churn al 4%, tu LTV sube a $612 y tu LTV/CAC pasa a 2,1x.
2. **Subir el ARPU / Precios:** Cobrar más por onboarding o añadir tiers superiores.
3. **Optimizar el CAC:** Probar canales orgánicos o mejorar conversión para que el CAC baje de $290 a menos de $100.

**Veredicto:** Guarda los $10.000 en el banco. Arregla la retención primero.