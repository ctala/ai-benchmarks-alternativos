# Kimi K2.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 106.417s | tokens_per_second: 28.1
- input_tokens: 231 | output_tokens: 2990

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

**No le doy. El plan muere en la aritmética.**

Tus números no son lo que crees. Estás a punto de convertir $10.000 en un agujero de cash con un retorno marginal o negativo. Te corrijo paso a paso.

---

### 1. Tu cálculo de LTV tiene dos errores fatales

**Error A: Estás usando revenue bruto, no margen.**
El LTV debe calcularse sobre lo que realmente te queda después de costos directos (infraestructura, procesador de pagos), no sobre lo que facturas. Con un margen del 70%, tu ganancia neta mensual por cliente es:

> **$35 × 70% = $24,50/mes**

**Error B: Inventaste la vida del cliente.**
Dijiste “unos 2 años”. Eso no es una suposición que puedas tomar; la dicta el churn. Con un churn mensual del **8%**, la vida promedio (esperanza matemática) es:

> **1 ÷ 0,08 = 12,5 meses**

No 24. Solo el **13,5%** de tus clientes llega vivo al mes 24. El otro 86,5% se fue antes.

**LTV real:**
> **$24,50 × 12,5 = $306,25**

---

### 2. Tu ratio real es casi 1:1, no 3:1

| Métrica | Tu cálculo | El cálculo real |
|---------|-----------|----------------|
| **LTV** | $840 | **$306** |
| **CAC** | $290 | $290 |
| **LTV/CAC** | 2,9x | **1,06x** |

Un ratio de **1,06x** no es escalar; es donarle plata a Google y a Facebook. Necesitas **>3x** (y de preferencia con payback corto) para pisar el acelerador.

---

### 3. El payback period te mata

¿Cuánto tardas en recuperar el CAC con el margen mensual?

> **$290 ÷ $24,50 = 11,8 meses**

Con un churn del 8% mensual, la probabilidad de que un cliente sobreviva 12 meses es:

> **(0,92)^12 = 36,7%**

**Traducción:** Más del **63%** de los clientes que compras con ads se van **antes** de que te paguen lo que te costó adquirirlos. Estás apostando a la ruleta con odds en contra.

---

### 4. Qué pasa si metes los $10.000

A $290 por cliente, eso te trae **~34 clientes**.

- Cash que sales a buscar: **$10.000** (hoy).
- Margen bruto total que te devolverán en promedio: **34 × $306 = $10.404**.
- Pero distribuido en **12,5 meses promedio**.
- Y antes de que recuperes la inversión, más de la mitad ya se evaporó.

Es decir: encajas $10.000 hoy para recibir ~$10.400 en un año, si todo sale bien. Eso no es crecimiento; es financiar a tus clientes gratis mientras quemas capital.

---

### 5. Qué arreglar antes de tocar publicidad pagada

Tu problema no es el CAC solo; es la combinación de **churn alto + margen apretado**.

1. **Baja ese churn del 8% mensual.** Eso es catastrófico (equivale a ~63% anual). En SaaS sano, incluso B2C, buscas <5% mensual; en B2B, <2%. Con 8% no tienes negocio recurrente, tienes un embudo con fuga.
2. **Sube el ticket o el margen.** A $35/mes con 70% de margen, no hay suficiente “carne” para pagar $290 de adquisición. Necesitas:
   - Subir precio,
   - Cobrar anualidad por adelantado (cash upfront mejora el payback de 11,8 meses a inmediato),
   - Reducir CAC mejorando conversión o canales.
3. **Meta de salud:** Busca un **LTV/CAC ≥ 3** y un **payback period ≤ 6 meses**. Con tu estructura actual, estás en el lado equivocado de ambas.

---

**Veredicto final:** Con estos números, cada cliente nuevo que compras con publicidad deja a tu empresa más pobre en valor presente. **No metas los $10.000.** Arregla el churn y el margen primero, o escala por canales de CAC cercano a cero (contenido, referrals, partnerships) hasta que la ecuación aguante.

Si quieres, armo un modelo de sensibilidad para ver cuánto debería bajar tu churn (o subir tu precio) para que ese CAC de $290 sea rentable.