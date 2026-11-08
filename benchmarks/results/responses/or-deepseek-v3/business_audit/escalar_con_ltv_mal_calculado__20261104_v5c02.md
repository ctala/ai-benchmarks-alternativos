# DeepSeek V3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.95 | quality: 10.0
- latency_total: 16.905s | tokens_per_second: 39.0
- input_tokens: 202 | output_tokens: 660

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

No, **no le des todavía**. Tus cálculos tienen errores importantes que hacen que la inversión sea riesgosa. El LTV está sobreestimado y el ratio real es mucho más bajo de lo que crees.

Desglosemos los números:

---

### 1. Tu LTV real (con churn)
No puedes simplemente multiplicar $35 × 24 meses, porque cada mes se van el 8% de los clientes.

**LTV = (Precio mensual × Margen bruto) / Tasa de churn mensual**  
= ($35 × 0.70) / 0.08  
= $24.50 / 0.08  
= **$306.25**

Este es el LTV **bruto** (antes de restar CAC u otros costos).  
En modelos más precisos, con descuento del valor del dinero en el tiempo, sería aún un poco menor.

---

### 2. Ratio LTV/CAC real
- LTV (bruto) = **$306**
- CAC = **$290**
- **LTV/CAC = 1.06**

**Esto está muy por debajo de 3**, y apenas supera 1.  
En SaaS B2B/B2C, un ratio < 3 suele ser señal de precaución; < 1.5 es riesgoso para escalar con publicidad.

---

### 3. Tiempo para recuperar el CAC (Payback Period)
Cada cliente te da un margen bruto mensual de $24.50.  
Para recuperar $290 de CAC:  
$290 / $24.50 ≈ **11.8 meses**.

Eso significa que pasas casi un año sin ganar dinero por ese cliente, solo cubriendo el CAC. Con un churn del 8% mensual, muchos se irán antes de que recuperes la inversión.

---

### 4. ¿Por qué tu cálculo inicial fue engañoso?
- Ignoraste el churn en la duración real del cliente.  
  La vida promedio con churn mensual del 8% es 1 / 0.08 = 12.5 meses, no 24.  
- Usaste el precio en lugar del margen bruto.  
- No descontaste flujos futuros.

---

### Recomendaciones antes de escalar:

1. **Reduce el CAC** o **aumenta el precio** (si el mercado lo permite).  
2. **Mejora la retención**: bajar el churn del 8% al 5% casi duplica el LTV.  
3. **Prueba con un presupuesto pequeño** antes de los $10.000: mide si los nuevos clientes tienen el mismo churn.  
4. Considera **canales orgánicos o virales** para complementar.

**Conclusión:** Con LTV/CAC ≈ 1.06, escalar con publicidad pagada te haría perder dinero a largo plazo. Trabaja primero en mejorar los unit economics.