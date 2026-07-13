# Mistral Small 4 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `mistralai/mistral-small-2603`
- success: True  | final: 8.02 | quality: 8.4
- latency_total: 8.323s | tokens_per_second: 158.8
- input_tokens: 224 | output_tokens: 1322

## Respuesta completa

Vamos a hacer el análisis de unit economics con más precisión para evitar sorpresas. Aquí hay varios puntos críticos que ajustan tu LTV y CAC:

---

### **1. Ajuste del LTV (Lifetime Value)**
Tu cálculo asume que todos los clientes se quedan **exactamente 2 años (24 meses)**, pero con un **churn del 8% mensual**, la realidad es más complicada.

#### **Churn real acumulado:**
La fórmula para calcular la retención acumulada con churn mensual constante es:
**Retención después de *n* meses = (1 - churn)^n**

- **Después de 12 meses:** (1 - 0.08)^12 ≈ **36% de retención**
  (Solo el 36% de los clientes siguen después de un año).
- **Después de 24 meses:** (1 - 0.08)^24 ≈ **13% de retención**
  (Solo el 13% siguen después de dos años).

#### **LTV ajustado:**
Para calcular el LTV real, usamos la fórmula:
**LTV = (Precio × Margen bruto) × Vida promedio esperada**

La **vida promedio esperada** con churn mensual *r* es:
**1 / r** (en meses).
Para *r = 8%*: **1 / 0.08 = 12.5 meses** (no 24).

**LTV real = $35 × 0.70 × 12.5 = $306.25** (no $840).

---

### **2. CAC real (incluyendo costos ocultos)**
Tu CAC de $290 es **bruto** (solo la publicidad). Pero hay otros costos que deben incluirse para calcular el **CAC real**:
- **Procesador de pagos** (ej: Stripe cobra ~2.9% + $0.30 por transacción). Esto reduce tu margen bruto.
  - Si un cliente paga $35, Stripe se queda ~$1.32 ($35 × 0.029 + $0.30).
  - **Margen bruto ajustado = 70% × $35 - $1.32 = $23.18** (no $24.50).

- **Infraestructura/servicios** (si aplican costos adicionales por escalar).

**CAC real = $290 / (1 - costos ocultos) ≈ $290** (en este caso no cambia mucho, pero es importante verificarlo).

---

### **3. LTV/CAC ajustado**
- **LTV ajustado = $306.25**
- **CAC = $290**
- **LTV/CAC = 1.06** (muy por debajo del umbral mínimo de **3**).

Esto significa que **por cada $1 invertido en publicidad, solo recuperas $1.06**, lo que no cubre:
- Costos operativos (soporte, servidores, salarios).
- Riesgo de que el churn aumente al escalar (clientes menos comprometidos).
- Impuestos y otros gastos fijos.

---

### **4. ¿Le doy luz verde?**
**No**, al menos no sin ajustes. Tu modelo actual **pierde dinero en cada cliente adquirido con publicidad**. Para que funcione, necesitas:

#### **Opción 1: Mejorar el LTV**
- **Aumentar el precio** (ej: de $35 a $50/mes).
  - Nuevo LTV ajustado = $50 × 0.70 × 12.5 = $437.50.
  - LTV/CAC = $437.50 / $290 ≈ **1.51** (aún bajo, pero mejor).

- **Reducir el churn** (meta: <5% mensual).
  - Si churn = 5%, vida promedio = 20 meses.
  - LTV = $35 × 0.70 × 20 = $490.
  - LTV/CAC = $490 / $290 ≈ **1.69** (mejor, pero sigue bajo).

#### **Opción 2: Reducir el CAC**
- Optimizar campañas (ej: remarketing, SEO orgánico).
- Mejorar la conversión en landing pages (ej: pruebas A/B).
- **Meta: CAC ≤ $100** para un LTV/CAC ≥ 3.

#### **Opción 3: Combinar ambas**
Ejemplo realista:
- Precio: $50/mes.
- Churn: 6% (vida promedio = 16.7 meses).
- Margen bruto: 70% (después de Stripe).
- **LTV = $50 × 0.70 × 16.7 ≈ $584.50**.
- **CAC objetivo = $195** (para LTV/CAC = 3).
  - Si logras reducir el CAC a $195 con tus $10K ($10K / 51 clientes ≈ $196 CAC), el modelo sería viable.

---

### **Conclusión**
Tu plan actual **no escala con rentabilidad**. Necesitas:
1. **Aumentar el LTV** (precio o retención).
2. **Reducir el CAC** (optimización o canales más baratos).
3. **Prueba a pequeña escala** antes de invertir $10K.

**Recomendación:**
- Corre pruebas con presupuestos pequeños (ej: $1K/mes) y mide el CAC real y churn.
- Si logras un LTV/CAC ≥ 3 **con datos reales**, entonces escala.

*Muchos modelos mueren en la aritmética. Este es uno de esos casos.*