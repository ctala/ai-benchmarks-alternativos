# Qwen 3.6 35B base (OpenRouter FP8) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.6-35b-a3b`
- success: True  | final: 7.68 | quality: 8.4
- latency_total: 26.126s | tokens_per_second: 117.4
- input_tokens: 217 | output_tokens: 3066

## Respuesta completa

**No. No apruebo los $10.000.** Tu plan se cae en la primera línea de la tabla de unit economics. Antes de meter caja en publicidad, necesitas corregir la aritmética. Te explico por qué:

### 🔍 3 errores en tu cálculo
1. **Ignoras el churn en el LTV.** Con 8% de churn mensual, la vida media del cliente no es 24 meses. Es `1 / 0.08 = 12.5 meses`.
2. **Calculas LTV sobre ingresos, no sobre margen.** El LTV se mide sobre el **margen de contribución**, no sobre el precio de venta. Tu margen bruto es 70%, así que el ingreso útil por mes es `$35 × 0.70 = $24.5`.
3. **Confundes rentabilidad actual con escalabilidad.** Dices que ya eres rentable, pero eso suele ser con tráfico orgánico, referrals o canales de bajo CAC. La publicidad pagada tiene dinámicas distintas: el CAC sube al escalar y el churn suele empeorar con tráfico menos cualificado.

### 📊 Números reales
| Indicador | Tu cálculo | Cálculo correcto |
|-----------|------------|------------------|
| Ingreso útil/mes | $35 | $24.5 |
| Vida media del cliente | 24 meses | 12.5 meses |
| **LTV** | $840 | `$24.5 / 0.08 = **$306.25**` |
| **LTV/CAC** | 2.9 | `$306.25 / $290 ≈ **1.06**` |
| **Payback** | No calculado | `$290 / $24.5 ≈ **11.8 meses**` |

### ⚠️ Por qué esto mata el plan de escalamiento
- **LTV/CAC < 1.5** en SaaS es insaludable. El estándar de mercado es ≥ 3. Con 1.06, estás esencialmente **pagando para perder clientes**.
- **Payback de ~12 meses** significa que recuperas la inversión casi al año. En publicidad pagada, los márgenes se comprimen rápido; cualquier variación en CPA, churn o margen te pone en negativo.
- **Churn del 8% mensual** equivale a ~63% de churn anual. Escalar con ese churn es como llenar un balde con un agujero: cada dólar en ads se evapora en retención.

### ✅ Qué necesitas antes de aprobar
1. **LTV/CAC ≥ 3** (idealmente ≥ 4 en fase de escala agresiva).
2. **Payback ≤ 6 meses** (máximo 12, pero <6 permite reinversión saludable).
3. **Piloto validado:** Invierte $2.000-$3.000 en ads durante 30 días. Mide:
   - CAC real por canal
   - Churn de los clientes adquiridos por ads vs orgánico
   - Margen de contribución neto (incluye soporte, onboarding, etc.)
4. **Acciones correctivas prioritarias:**
   - Reducir churn a <5% mensual (onboarding, engagement, pricing, calidad de tráfico)
   - Bajar CAC a < $100 (optimización de campañas, landing, conversión, referral)
   - Aumentar ARPU o margen (upsell, empaquetado, reducción de COGS)

### 🚦 Veredicto
**No des luz verde a los $10.000.** Sin corregir unidad económica, estás escalando un modelo que quema caja por cliente. Si en 60 días me traes un piloto con `LTV/CAC ≥ 3` y `payback ≤ 6 meses`, hablemos de escalar. Mientras tanto, la prioridad es retención y eficiencia de adquisición, no volumen.

¿Quieres que te arme una hoja de cálculo con las proyecciones por escenario (churn 5%, 8%, 12%) y el punto de equilibrio de ads?