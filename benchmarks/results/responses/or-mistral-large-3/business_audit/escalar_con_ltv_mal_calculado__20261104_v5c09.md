# Mistral Large 3 675B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `mistralai/mistral-large-2512`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 12.002s | tokens_per_second: 113.2
- input_tokens: 212 | output_tokens: 1358

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

Vamos a recalcular los números con más precisión, porque hay varios detalles que tu análisis inicial no considera y que pueden hacer que el plan no sea viable. Aquí va el desglose:

---

### 1. **Cálculo correcto del LTV (Lifetime Value)**
Tu cálculo del LTV asume que el cliente se queda **exactamente 24 meses**, pero el churn mensual del 8% implica una **retención decreciente**. La fórmula correcta para el LTV en un modelo de suscripción con churn constante es:

\[
LTV = \frac{\text{ARPU} \times \text{Margen bruto}}{\text{Churn mensual}}
\]

Donde:
- **ARPU** (Average Revenue Per User) = $35/mes.
- **Margen bruto** = 70% → $35 × 0.7 = $24.5/mes.
- **Churn mensual** = 8% → 0.08.

\[
LTV = \frac{24.5}{0.08} = \$306.25
\]

**No es $840, sino $306.25**. El error viene de asumir una vida útil fija en lugar de modelar el churn como una probabilidad mensual.

---

### 2. **LTV/CAC real**
Con un CAC de $290 y un LTV de $306.25:

\[
LTV/CAC = \frac{306.25}{290} = 1.06
\]

Esto está **muy por debajo del umbral mínimo de 3** que mencionas (y que es estándar en la industria para escalar con publicidad pagada). Un ratio de 1.06 significa que **recuperas apenas el 6% más de lo que gastas en adquirir un cliente**, sin considerar otros costos (operativos, impuestos, etc.).

---

### 3. **Payback Period (Período de recuperación del CAC)**
Otro indicador clave: ¿cuánto tardas en recuperar el CAC? Con un margen bruto de $24.5/mes:

\[
\text{Payback Period} = \frac{CAC}{\text{Margen bruto mensual}} = \frac{290}{24.5} \approx 11.8 \text{ meses}
\]

Esto es **demasiado largo**. En publicidad pagada, lo ideal es recuperar el CAC en **menos de 6 meses** (o incluso 3 meses para escalar agresivamente). Si tardas casi 1 año, estás asumiendo un riesgo alto de que el cliente se vaya antes de que recuperes la inversión.

---

### 4. **Sensibilidad al churn**
Tu churn del 8% mensual es **muy alto** para un modelo de suscripción. Para ponerlo en contexto:
- Un churn del 8% mensual implica que **la mitad de tus clientes se van en ~8 meses** (no en 2 años).
- Si el churn sube al 10%, el LTV cae a $245, y el LTV/CAC sería **0.84** (pierdes dinero por cliente).

---

### 5. **¿Qué pasa si inviertes $10,000 en publicidad?**
Con un CAC de $290, esos $10,000 te darían:
\[
\frac{10,000}{290} \approx 34 \text{ clientes nuevos}
\]

Pero con un LTV de $306.25 y un CAC de $290, **ganas solo $16.25 por cliente** (antes de otros costos). Para 34 clientes:
\[
34 \times 16.25 = \$552.5 \text{ de margen bruto adicional}
\]

Esto es **insostenible**. Además, si el churn es alto, muchos de esos clientes se irán antes de que recuperes el CAC.

---

### 6. **Recomendaciones antes de escalar**
1. **Reduce el churn**:
   - Un churn del 8% mensual es el problema raíz. Si lo bajas al 5%, el LTV sube a $490, y el LTV/CAC sería **1.69** (mejor, pero aún no ideal).
   - Si lo bajas al 3%, el LTV sería $816.67, y el LTV/CAC sería **2.82** (ahora sí viable).

2. **Optimiza el CAC**:
   - ¿Puedes bajar el CAC a $200? Con un LTV de $306.25, el ratio sería **1.53** (aún no suficiente, pero más cerca).
   - Prueba canales más baratos (SEO, referidos, contenido orgánico).

3. **Aumenta el precio o el margen**:
   - Si subes el precio a $45/mes (con el mismo margen del 70%), el LTV sería $393.75, y el LTV/CAC sería **1.36**.
   - Si mejoras el margen al 80%, el LTV sería $350, y el LTV/CAC sería **1.21**.

4. **Prueba con un presupuesto pequeño primero**:
   - En lugar de $10,000, prueba con $2,000 y mide el churn y el payback period real. Si los números no mejoran, no escales.

---

### Conclusión
**No des el visto bueno a los $10,000**. Con los números actuales:
- LTV/CAC = **1.06** (debería ser >3).
- Payback period = **11.8 meses** (debería ser <6).
- Churn = **8% mensual** (demasiado alto).

**Prioriza reducir el churn y optimizar el CAC antes de escalar**. Si no puedes mejorar estos indicadores, la publicidad pagada te llevará a quemar dinero rápidamente.