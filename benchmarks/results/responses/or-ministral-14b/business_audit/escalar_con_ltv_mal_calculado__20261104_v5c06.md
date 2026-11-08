# Ministral 14B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 9.03 | quality: 10.0
- latency_total: 36.42s | tokens_per_second: 54.8
- input_tokens: 212 | output_tokens: 1995

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

Vamos a analizar tus números con más detalle para evitar errores comunes en la aritmética del crecimiento. Hay varios factores críticos que podrían hacer que tu plan falle, incluso si el **LTV/CAC = 2.9** parece atractivo a primera vista. Aquí está el desglose:

---

### **1. LTV Realista (No Lineal)**
Tu cálculo de **LTV = $35 × 24** asume:
- **Churn constante del 8% mensual** (correcto).
- **Ingresos fijos de $35/mes** (incorrecto en muchos casos).

#### **Problema:**
- **El churn no es lineal en términos de ingresos**: Si los clientes cancelan después de 12-24 meses, el LTV real es menor porque no generan ingresos durante todo el período.
- **Fórmula correcta del LTV** (para churn mensual constante):
  \[
  LTV = \text{Precio} \times \left( \frac{1 - (1 + \text{Churn})^{-n}}{\text{Churn}} \right)
  \]
  Donde \( n \) = meses de vida útil promedio (en tu caso, ~24 meses).
  \[
  LTV = 35 \times \left( \frac{1 - (1 - 0.08)^{-24}}{0.08} \right) \approx 35 \times 12.08 \approx **$423**
  \]
  *(No $840, porque el churn reduce el valor acumulado antes de los 24 meses)*.

#### **¿Por qué importa?**
- Con **LTV = $423** y **CAC = $290**, tu **LTV/CAC real = 1.46** (no 2.9).
- **Conclusión:** Tu margen de error es mínimo. Un aumento en el churn, una caída en el precio o un CAC más alto te llevaría a la pérdida.

---

### **2. Margen Bruto vs. Margen de Contribución**
- **Margen bruto del 70%** suena bien, pero:
  - ¿Incluye **costos variables de soporte, marketing recurrente (retención), operaciones o logística**?
  - Si no, tu **margen de contribución** (lo que realmente queda después de costos variables) podría ser menor.
  - **Ejemplo:** Si el soporte cuesta $5/cliente/mes, tu margen real por cliente es:
    \[
    35 \times 0.7 - 5 = 24.5 - 5 = **$19.5/mes**
    \]
    *(Ahora el LTV real sería $19.5 × 12.08 ≈ $236, y LTV/CAC = 0.81. ¡Pérdida!)*.

#### **Acción:**
- **Calcula el margen de contribución real** (no solo bruto).
- Si es < $15/mes, **no escalas con publicidad pagada** sin ajustar precios o reducir CAC.

---

### **3. CAC Inestable**
- **$290 es tu CAC actual**, pero:
  - ¿Es sostenible a escala? Los costos por lead suelen **aumentar** con más volumen (ej: competencia por keywords, fatiga de audiencias).
  - **Regla empírica:** Si tu CAC sube un 20% (a $348), tu LTV/CAC cae a **1.21** (pérdida).
  - **Solución:**
    - Prueba con **$5,000/mes** primero (no $10,000) para validar que el CAC no se dispara.
    - Usa **atribución multi-touch** (no solo último clic) para evitar sobrepagar canales ineficientes.

---

### **4. Churn Oculto o Sesgado**
- **¿Tu churn del 8% es real o optimista?**
  - Si mides churn en los primeros 3 meses (ej: 20%), pero luego baja al 5%, tu LTV real es menor.
  - **Fórmula ajustada para churn no constante:**
    \[
    LTV = \text{Precio} \times \left( \frac{1 - \text{Churn}_1}{(1 + r)} + \frac{1 - \text{Churn}_1 \times \text{Churn}_2}{(1 + r)^2} + \dots \right)
    \]
    *(Donde \( r \) = tasa de descuento, ej: 1% mensual por inflación/oportunidad)*.
  - **Ejemplo:** Si el 15% cancela en el primer mes y luego el 5%:
    \[
    LTV ≈ 35 \times (0.85 + 0.85 \times 0.95 / 1.01 + \dots) ≈ **$300**
    \]
    *(Ahora LTV/CAC = 1.03. Casi en rojo)*.

#### **Acción:**
- **Segmenta el churn por cohortes** (meses de adquisición).
- Si el churn es >10% en los primeros 6 meses, **no escalas** hasta resolver la retención.

---

### **5. Efecto de Red o Network Effects**
- **¿Tu producto tiene efectos de red que reducen el churn?**
  - Si no (ej: SaaS B2C sin viralidad), el churn tiende a ser **más alto a largo plazo**.
  - **Ejemplo:** Si el churn sube al 10% después de 12 meses:
    \[
    LTV ≈ 35 \times 10.5 ≈ **$368** (LTV/CAC = 1.27)
    \]
    *(Aún en riesgo)*.

---

### **6. Prueba Piloto Obligatoria**
Antes de invertir **$10,000**, haz una prueba con:
- **$2,000 - $3,000/mes** durante 3 meses.
- **Objetivos:**
  1. **CAC real:** ¿Se mantiene en $290 o sube?
  2. **Churn post-adquisición:** ¿Aumenta el churn en los primeros 3 meses?
  3. **Margen de contribución:** ¿Los costos variables escalan como esperas?
- **Métrica clave:** **LTV/CAC a 6 meses** (no a 24, porque el churn suele ser peor al inicio).

---

### **7. Alternativas si los Números No Cierran**
Si después de la prueba tu **LTV/CAC < 2**, considera:
1. **Aumentar el precio** (ej: a $45/mes → LTV ≈ $525 → LTV/CAC = 1.81).
2. **Reducir el CAC** (ej: mejorar el embudo, usar lookalike audiences en Meta).
3. **Enfocarte en retención** (ej: programa de referidos, soporte proactivo).
4. **Escalar con orgánico** (SEO, contenido) mientras optimizas paid.

---

### **Veredicto Final: ¿Aprobar los $10,000?**
**NO, a menos que:**
✅ **Hagas una prueba piloto con $2,000-$3,000/mes** durante 3 meses.
✅ **Confirmes que:**
   - El **CAC no supera $300** (con margen de contribución > $15/mes).
   - El **churn post-adquisición no sube al 10%+**.
   - El **LTV real a 6 meses > 2 × CAC**.

**Si los números se mantienen, entonces escala en incrementos del 20-30% mensuales** (ej: $3,000 → $4,000 → $6,000 → $10,000).

---
### **Errores Comunes que Matan Startups**
1. **Asumir churn constante** (siempre es peor al inicio).
2. **Ignorar costos variables** (soporte, marketing de retención).
3. **Escalar antes de validar CAC real** (el CAC siempre sube con volumen).
4. **Usar LTV teórico** (siempre usa datos reales de cohortes).

**Recomendación extra:**
- **Calcula tu "Rule of 40"** (Revenue Growth Rate + Profit Margin ≥ 40%).
  - Si tu crecimiento es lento y el margen bajo, la publicidad pagada puede no ser sostenible.

---
**¿Quieres que profundicemos en algún área?** (ej: cómo calcular margen de contribución real, cómo reducir CAC, o cómo medir churn por cohortes).