# Poolside Laguna XS 2.1 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `poolside/laguna-xs-2.1`
- success: True  | final: 6.96 | quality: 6.67
- latency_total: 10.341s | tokens_per_second: 192.1
- input_tokens: 260 | output_tokens: 1986

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

**No, no le doy.** Tu plan de crecimiento tiene errores críticos en los cálculos que lo hacen arriesgado. Vamos a revisar los números con detalle:

---

### **1. Error en el cálculo del LTV (Valor de Vida del Cliente)**
- **Tu cálculo:**  
  LTV = $35 × 24 meses = **$840**  
  (Asumiendo que un cliente dura 2 años).  

- **Realidad:**  
  El **churn mensual del 8%** reduce drásticamente la vida útil promedio de un cliente.  
  - **Fórmula correcta para vida útil (CL):**  
    $$ \text{CL} = \frac{1}{\text{tasa de churn}} = \frac{1}{0.08} = 12.5 \text{ meses} $$  
  - **LTV real:**  
    $$ \text{LTV} = 35 \times 12.5 = \$437.50 $$  

  **Tu LTV es casi la mitad de lo que calculaste.**

---

### **2. LTV/CAC real: 1.5x vs. 2.9x**
- **Tu proporción:**  
  $$ \frac{LTV}{CAC} = \frac{840}{290} = 2.9x $$  

- **Realidad:**  
  $$ \frac{437.50}{290} = 1.5x $$  

  **Un LTV/CAC de 1.5x es peligroso.**  
  - La regla general es que **LTV/CAC ≥ 3x** para una inversión saludable.  
  - Con 1.5x, estás recuperando solo el 50% de tu inversión en CAC.  

---

### **3. Margen de contribución y período de recuperación**
- **Margen bruto del 70%** significa:  
  $$ \text{Margen de contribución} = 35 \times 0.70 = \$24.50/\text{mes} $$  

- **Período de recuperación del CAC ($290):**  
  $$ \frac{290}{24.50} \approx 11.8 \text{ meses} $$  

  **El tiempo para recuperar el CAC es de casi un año.** Esto es crítico si el churn es alto, ya que los clientes se irán antes de que recuperes la inversión.

---

### **4. Riesgos adicionales**
- **Churn del 8% mensual:**  
  - Es muy alto para un modelo SaaS. Un churn tan elevado reduce drásticamente la rentabilidad.  
  - Si el churn sube, el LTV cae aún más (ej.: 10% de churn → CL = 10 meses → LTV = $350).  

- **Escalabilidad de la publicidad:**  
  - Si gastas $10,000 en ads, necesitas generar **al menos 34 clientes** (10,000 / 290 ≈ 34.5) para no perder dinero.  
  - Con un LTV de $437.50 y un CAC de $290, cada cliente genera **$147.50 de ganancia neta**.  
  - 34 clientes × $147.50 = **$5,015 de ganancia neta**.  

  **Esto solo cubriría el CAC, pero no el costo inicial de $10,000.**  

---

### **5. Recomendaciones para un plan viable**
1. **Reduzca el CAC:**  
   - Optimice las campañas de ads para bajar el CAC (ej.: mejor segmentación, canales más eficientes).  
   - Si el CAC baja a **$150**, el LTV/CAC sería:  
     $$ \frac{437.50}{150} = 2.9x $$  

2. **Reduzca el churn:**  
   - Un churn del 5% mensual (CL = 20 meses) daría un LTV de $700 y un LTV/CAC de 2.4x (con CAC de $290).  
   - Un churn del 3% (CL = 33.3 meses) daría un LTV de $1,166 y un LTV/CAC de 4x.  

3. **Pruebe con un presupuesto menor:**  
   - Pruebe con **$1,000 en ads** para validar la eficiencia de las campañas antes de escalar.  

4. **Analice la rentabilidad real:**  
   - Calcule el **CAC pagado** y el **churn real** de los clientes adquiridos con este gasto.  
   - Si el churn es mayor en clientes de ads, el plan no es sostenible.  

---

### **Conclusión**
Tu plan actual **no es viable** con los números actuales. El LTV real es mucho menor, y el CAC está por encima de lo que puedes recuperar. Antes de invertir $10,000, **debes:**
- Reducir el churn (idealmente a <5% mensual).  
- Mejorar la eficiencia de las campañas para bajar el CAC.  
- Validar con un presupuesto más pequeño y medir resultados.  

Si no, corres el riesgo de **perder dinero** al escalar.