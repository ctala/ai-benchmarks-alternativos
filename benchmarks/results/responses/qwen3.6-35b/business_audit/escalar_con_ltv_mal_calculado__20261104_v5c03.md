# Qwen 3.6 35B base (OpenRouter FP8) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 38.541s | tokens_per_second: 83.0
- input_tokens: 217 | output_tokens: 3198

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



**No le des.** Tu aritmética tiene tres errores estructurales que hacen que este plan queme caja en lugar de crecer. Como analista de unit economics, mi regla es: si los números base no aguantan un 2x de escala, el plan está muerto.

### 🔍 Errores en tu cálculo
1. **LTV mal calculado:** `35 × 24 = 840` ignora el churn y usa *ingresos*, no *margen*. Con un churn mensual del 8%, la vida media de un cliente es `1 / 0.08 = 12.5 meses`, no 24.
2. **LTV debe basarse en contribución marginal:** Cada mes te quedan `$35 × 70% = $24.50`.
3. **LTV/CAC real:** 
   ```
   LTV = $24.50 / 0.08 = $306.25
   LTV/CAC = $306.25 / $290 ≈ 1.06
   ```
   Dices que es `2.9` y "por encima de 3 más o menos". Matemáticamente es `2.896`, y financieramente es **1.06** cuando se calcula correctamente. La diferencia no es menor, es abismal.

### ⚠️ Qué significa esto en la práctica
- **Payback period:** `$290 / $24.50 ≈ 11.8 meses`. Con un churn del 8%, la probabilidad de que un cliente sobreviva 12 meses es solo `(0.92)^12 ≈ 36%`. Estás financiando la adquisición con caja que muy probablemente no recuperarás.
- **Escalado con publicidad pagada no perdona ratios < 3:** El CAC sube con el volumen (fatiga de creatividades, pujas, segmentación saturada). Un ratio de 1.06 a volumen bajo puede parecer "rentable", pero a $10k/mes se invertirá en clientes marginales con mayor churn y menor retención.
- **Cash flow gap:** `$10,000 en ads → ~34 clientes → $833/mes de margen bruto`. En 6 meses, con 8% de churn mensual, perderás más de $4,500 en valor de clientes no recuperados. Tu flujo de caja se invertirá aunque el LTV sea ligeramente > CAC.

### ✅ Qué hacer antes de aprobar
1. **Objetivo mínimo para paid ads:** `LTV/CAC ≥ 3` y `payback ≤ 6-9 meses`.
2. **Rutas para llegar ahí:**
   - Reducir churn a ≤4% (onboarding, product-led growth, engagement)
   - Subir ARPU o cross-sell (paquetes anuales, add-ons)
   - Bajar CAC a <$100 (orgánico acelerado, referidos, SEO, partnerships)
   - Mejorar margen bruto a ≥80% (optimizar infra, negociar procesadores)
3. **Prueba controlada:** No tires $10k. Asigna $2,000-$3,000, mide por **cohortes**, y solo escala si el payback < 8 meses y el churn no se degrada.
4. **Simula cash flow real:** Usa un modelo de cohortes que incluya retención mensual, margen por mes, y día de pago real. La aritmética agregada miente; las cohortes no.

Si quieres, te armo un modelo de cohortes en 10 minutos con tus datos y te muestro exactamente cuándo y cómo escalar sin quemar caja. Los planes de crecimiento no mueren por mala estrategia, mueren por aritmética descuidada.