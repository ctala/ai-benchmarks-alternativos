# Ling 3.0 Flash VL — business_audit/escalar_con_ltv_mal_calculado

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 9.32 | quality: 10.0
- latency_total: 20.48s | tokens_per_second: 134.7
- input_tokens: 250 | output_tokens: 2759

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

## ❌ No le des. Tus números no cuadran. Vamos a desarmar tu cálculo.

---

### 🔴 Error 1: La vida útil no es 24 meses

Dices que el cliente se queda "unos 2 años", pero tu churn mensual es del **8%**. Eso no da 24 meses de vida. Da:

> **Vida útil promedio = 1 ÷ churn mensual = 1 ÷ 0.08 = 12.5 meses**

Con un 8% mensual, al cabo de 12 meses solo te queda el **~37%** de los clientes originales (0.92¹² ≈ 0.368). No se quedan dos años: se van rápido.

---

### 🔴 Error 2: No aplicaste el margen bruto

El LTV se calcula sobre el **margen**, no sobre el ingreso bruto. Pero incluso usando tu versión generosa (24 meses sin margen), el resultado cambia:

| Escenario | Cálculo | LTV |
|---|---|---|
| **Tu versión** | $35 × 24 meses | $840 |
| **24 meses con margen 70%** | $35 × 24 × 0.70 | $588 |
| **12.5 meses con margen 70%** (el correcto) | $35 × 12.5 × 0.70 | **$306.25** |

---

### 🔴 Error 3: Tu LTV/CAC real es ~1.06, no ~2.9

| | Tu cálculo | Real |
|---|---|---|
| **LTV** | $840 | **$306.25** |
| **CAC** | $290 | $290 |
| **LTV/CAC** | ~2.9 | **~1.06** |

Un LTV/CAC de **1.06** significa que por cada dólar que gastas en adquisición, recuperas **1.06 dólares** en margen bruto a lo largo de la vida del cliente. Estás a un pelo del **punto de equilibrio**, con cero margen para cubrir:

- Salarios del equipo
- Infraestructura operativa
- Atención al cliente
- Retención y soporte
- Cualquier costo fijo

---

### 🔴 Error 4: La matemática del escalado con $10,000

Con $10,000 en publicidad:

- **Clientes adquiridos:** $10,000 ÷ $290 ≈ **34 clientes**
- **Margen bruto mensual inicial:** 34 × $35 × 0.70 = **$833/mes**
- **Margen bruto total en la vida de esos clientes:** 34 × $306.25 = **$10,412**

Recuperas ~$10,412 contra una inversión de $10,000. **Ganas $412 de margen** (un 4%) antes de pagar un solo costo operativo. Y eso asumiendo que el CAC se mantiene igual al escalar (rara vez pasa).

---

### 📊 Resumen visual

```
Tu mundo:     LTV $840  ÷  CAC $290  =  2.9x  → "Escalar" ✅
Mi mundo:     LTV $306  ÷  CAC $290  =  1.06x → "Quemas caja" 🔥
```

---

### ✅ Qué hacer antes de meter los $10,000

1. **Baja el churn antes de escalar.** Con 8% mensual estás perdiendo clientes a una velocidad alarmante. Cada punto de churn que reduzcas multiplica tu LTV. Si bajas el churn al 4% mensual, tu vida útil pasa de 12.5 a 25 meses y tu LTV se duplica a ~$612.

2. **Haz la aritmética con margen, no con ingresos.** Nunca compares ingresos brutos contra CAC.

3. **Objetivo realista:** LTV/CAC ≥ 3x con margen bruto incluido. Con tus números actuales necesitas que el LTV llegue a ~$870, lo que implica (con margen del 70%):
   - Churn mensual ≤ 2.8%, o
   - Precio de ~$118/mes, o
   - CAC de ~$100 (muy difícil sin mejorar la conversión)

4. **Prueba a pequeña escala.** Si quieres validar publicidad pagada, empieza con $1,000, mide el CAC real (no el estimado), y ajusta antes de escalar.

---

**La regla de oro:** Un plan de crecimiento no es un plan de crecimiento si los unit economics no sostienen la escala. Con LTV/CAC de 1.06, escalar publicidad pagada es multiplicar las pérdidas, no los ingresos. Primero arregla la ecuación, después acelera.