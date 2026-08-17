# Qwen 3.7 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.09 | quality: 10.0
- latency_total: 26.883s | tokens_per_second: 91.9
- input_tokens: 217 | output_tokens: 2471

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

**No le des luz verde todavía.** Tu cálculo de LTV ignora el efecto compuesto del churn y sobreestima la vida útil del cliente en más del doble. En unit economics, ese error convierte un plan inviable en uno aparentemente rentable. Vamos a la aritmética fría:

### 🔍 Donde falla tu cálculo
1. **Vida útil promedio**: Con churn mensual del 8%, la vida esperada no es 24 meses, es `1 / 0.08 = 12.5 meses`.
2. **Ingreso recurrente real por cliente**: `$35 × 70% margen bruto = $24.50/mes` de contribución neta.
3. **LTV correcto (sin descuento)**: `$24.50 / 0.08 = $306.25`  
   *(Fórmula estándar: `ARPU × Margen Bruto / Churn Mensual`)*

### 📉 Tus números reales
| Métrica | Tu cálculo | Realidad |
|--------|------------|----------|
| LTV    | $840       | **$306** |
| LTV/CAC| 2.9        | **1.06** |
| Payback| No calculado| **11.8 meses** (`$290 / $24.50`) |

### ⚠️ Por qué esto mata el plan de escala
- **LTV/CAC < 1.5** ya es zona de riesgo financiero. Con 1.06, **pierdes dinero con cada cliente nuevo** una vez que el churn se estabiliza.
- **Payback de ~12 meses** congela tu caja. Invertir $10k hoy significa estar negativo en flujo de caja casi un año antes de recuperar lo desembolsado.
- **El CAC no es estático**. Al escalar en ads, compites por mismo inventario, tus CPAs subirán y tu ratio bajará aún más.
- `"Ya soy rentable"` suele ser un indicio de cohortes antiguas con churn menor o sin costo de adquisición imputado. La rentabilidad histórica no garantiza que la unidad económica soporte escala.

### ✅ Condiciones para aprobar (si insistes en escalar)
1. **Llevar LTV/CAC ≥ 2.5** mediante:
   - Reducir churn a ≤ 5% (o mejorar retención early-stage)
   - Aumentar margen o precio manteniendo conversión
   - Optimizar funnel para bajar CAC sin sacrificar calidad
2. **Payback ≤ 6 meses** (`$290 / $24.50` debe caer a ≤ $48/mes de contribución o CAC ≤ $145)
3. **Validación en cohorte**: Testear $2-3k este mes con tracking por cohort. Si el ratio se mantiene o mejora a los 3 meses, entonces escalas.
4. **Proyección de caja**: Modelar 6-12 meses de flujo considerando el payback. Sin colchón, la escala te quebrará antes de rentabilizar.

**Veredicto**: Rechazado en estado actual. La escala no premia la intuición, castiga los errores unitarios. Corrige la fórmula, valida el payback y vuelve cuando el LTV/CAC supere 2.5 con payback < 6 meses. Ahí sí, metemos el gas.