# Kimi K2.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 32.769s | tokens_per_second: 62.5
- input_tokens: 231 | output_tokens: 2048

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

**No. No le metas plata todavía.**

Tu aritmética tiene un error fatal que te va a hacer quemar capital. Vamos a rehacer los números paso a paso.

---

### 1. El error en el LTV (Lifetime Value)

Tú asumiste que un cliente dura 24 meses (2 años) como si fuera un dato dado. **Pero el churn es el que dicta cuánto dura un cliente, no tu intuición.**

Con un churn mensual del **8%**, la vida promedio de un cliente es:

> **Vida promedio = 1 ÷ Churn = 1 ÷ 0.08 = 12.5 meses**

No 24 meses. Solo el 13% de tus clientes llega vivo al mes 24 (cálculo: 0.92^24).

**El LTV real (con margen):**
- Ingreso mensual: $35
- Margen bruto: 70% → $24.50 de margen por cliente/mes
- LTV = $24.50 × 12.5 meses = **$306**

Tu LTV real es **$306**, no $840.

---

### 2. El ratio LTV/CAC real

- LTV: $306
- CAC: $290
- **Ratio: 1.05**

Un ratio de 1.05 es **insostenible**. La regla de oro es 3:1 (mínimo 2.5:1 en etapas tempranas). Con 1.05, estás comprando billetes de $1.05 a $1.00. Pierdes plata en cada cliente nuevo cuando sumas costos operativos, equipo y capital de trabajo.

---

### 3. El problema del Payback Period (el asesino silencioso)

Incluso si ignoramos el ratio, mira el cash flow:

- Recuperas $24.50 por mes por cliente.
- Para pagar