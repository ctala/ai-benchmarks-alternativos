# Step 3.5 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.96 | quality: 10.0
- latency_total: 31.704s | tokens_per_second: 64.6
- input_tokens: 215 | output_tokens: 2048

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

**No le doy el visto bueno.** Su cálculo de LTV es incorrecto y subestima el riesgo del plan. Aquí está el análisis:

---

### **Errores en su cálculo de LTV**
1. **Vida útil del cliente mal calculada**:  
   Con un churn mensual del 8%, la vida útil esperada no es 24 meses. Se calcula como:  
   \[
   \text{Vida útil (meses)} = \frac{1}{\text{churn mensual}} = \frac{1}{0.08} = 12.5 \text{ meses}
   \]  
   (Si la retención es constante, el 50% de los clientes se pierden en ≈ 8.5 meses).

2. **LTV debe usar el margen bruto, no el precio**:  
   - Margen bruto mensual por cliente = $35 × 70% = **$24.5**.  
   - LTV correcto (sin descuento) = $24.5 × 12.5 ≈ **$306**.  
   - Si usa el precio ($35) en lugar del margen, obtiene $437.5, pero el CAC se paga con margen, no con ingreso bruto.

3. **LTV/CAC real**:  
   \[
   \frac{LTV}{CAC} = \frac{306}{290} \approx 1.06
   \]  
   **Está muy por debajo del umbral saludable (≥3)**. Incluso si usara $437.5 (precio, no margen), sería 1.5, aún inaceptable.

---

### **Problemas adicionales**
- **Payback period**:  
  \[
  \frac{CAC}{\text{Margen br