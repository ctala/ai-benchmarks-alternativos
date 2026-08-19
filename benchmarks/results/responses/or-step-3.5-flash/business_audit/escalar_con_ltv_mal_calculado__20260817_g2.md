# Step 3.5 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 8.96 | quality: 10.0
- latency_total: 40.233s | tokens_per_second: 50.9
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

**No, no le doy el visto bueno.** Tu cálculo tiene dos errores críticos que invierten la conclusión:

### 1. **Error en la vida útil del cliente (LTV)**
- **Tu suposición:** 2 años (24 meses).  
- **Realidad con 8% de churn mensual:**  
  - Tasa de retención mensual = 92% (1 - 0.08).  
  - Vida útil promedio = 1 / churn mensual = 1 / 0.08 = **12.5 meses**.  
  - *¿Por qué?* Con churn constante, la duración esperada de un cliente es el inverso de la tasa de abandono. 8% mensual es muy alto (equivalente a ~70% anual), por lo que la vida útil se reduce a la mitad de lo que asumes.

### 2. **Error en el cálculo del LTV**
- **Tu fórmula:** Precio × meses = $35 × 24 = $840 (esto es **ingreso bruto**, no utilidad).  
- **LTV correcto:** Debe usar el **margen bruto**, no el precio completo.  
  - Margen mensual por cliente = $35 × 70% = **$24.5**.  
  - LTV = Margen mensual × vida útil = $24.5 × 12.5 = **$306.25**.

---

### **Métricas corregidas:**
| Concepto | Cálculo | Valor |
|----------|---------|-------|
| **LTV** | $24.5 × (1 / 0.08) | $306.25 |
| **CAC** | Dado | $290 |
| **LTV/CAC** | $306.25 / $290 | **1.06** |
| **Payback period** | CAC / Margen mensual = $290 / $24.5 | **11.8 meses** |

---

### **Problemas clave:**
1. **LTV/CAC = 1.06** (no 2.9).  
   - Un ratio saludable para SaaS es ≥ 3.  
   - Incluso ≥ 1.5 es mínimo para considerar escalabilidad.  
   - **Aquí, por cada $1 invertido en CAC, recuperas solo $1.06 en margen de por vida.**  
2. **Payback period (11.