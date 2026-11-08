# Step 3.5 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 9.01 | quality: 10.0
- latency_total: 19.216s | tokens_per_second: 83.8
- input_tokens: 215 | output_tokens: 1610

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

**No, no le doy.** 

Tu cálculo del LTV es incorrecto porque asumes una vida útil de 24 meses (2 años), pero con un **churn mensual del 8%**, la vida útil esperada es:

\[
\text{Vida útil (meses)} = \frac{1}{\text{churn mensual}} = \frac{1}{0.08} = 12.5 \text{ meses}
\]

No 24 meses. El churn mensual del 8% implica que, en promedio, un cliente se queda **12.5 meses**, no 24.

---

### Recalculemos correctamente:

- **Precio mensual**: $35  
- **Margen bruto**: 70% → margen por cliente/mes = $35 × 0.7 = **$24.5**  
- **Vida útil esperada**: 12.5 meses  
- **LTV** = $24.5 × 12.5 = **$306.25**  

- **CAC**: $290  

\[
\text{LTV/CAC} = \frac{306.25}{290} \approx 1.06
\]

---

### Problemas adicionales:

1. **Ratio LTV/CAC < 3**: El umbral saludable para escalar con publicidad suele ser LTV/CAC ≥ 3. Aquí es ~1.06, lo que significa que recuperas apenas un poco más de lo que inviertes, y eso **antes de considerar costos operativos adicionales** (salarios, overhead, etc.).  
2. **Payback period**: Con un CAC de $290 y un margen mensual de $24.5, el payback toma **~12 meses** (290 / 24.5 ≈ 11.8). Eso es demasiado tiempo; idealmente deberías recuperar el CAC en <12 meses.  
3. **Sensibilidad al churn**: Si el churn aumenta levemente (ej. 9%), el LTV cae a ~$272, y LTV/CAC sería <1. El modelo es frágil.

---

### Conclusión:

**No inviertas los $10,000 en publicidad**. Con estos números, cada nuevo cliente comprado a $290 te deja un margen neto muy bajo (aprox. $16.25 por cliente después de recuperar CAC), lo que no justifica el riesgo ni el capital. Primero debes:

1. **Reducir el churn** (aumentar retención).  
2. **Aumentar el precio** o el margen.  
3. **Reducir el CAC** (optimizar canales).  
4. **Validar** si el churn mensual es realmente constante o si hay cohorts con mejor retención.

Si logras bajar el churn al 5% (vida útil de 20 meses), el LTV sube a ~$490 y LTV/CAC ≈ 1.7, pero aún así está lejos de 3. Necesitas un cambio significativo en la unidad económica antes de escalar.