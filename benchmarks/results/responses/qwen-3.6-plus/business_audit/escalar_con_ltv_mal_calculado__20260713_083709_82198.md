# Qwen 3.6 Plus — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 7.54 | quality: 8.4
- latency_total: 52.732s | tokens_per_second: 53.3
- input_tokens: 217 | output_tokens: 2812

## Respuesta completa

**Respuesta corta: No. Con esos números, escalar ahora te va a comer la caja.**

Te recalculo la ecuación unitaria paso a paso. Aquí es donde suelen morir los planes de crecimiento:

### 🔍 Dónde falla tu cálculo
1. **Usas facturación, no margen bruto.** El LTV para decisiones de acquisition se calcula sobre el *profit* real que deja el cliente, no sobre el precio de lista.
2. **Asumes 24 meses fijos.** Con un churn del 8% mensual, la vida media de un cliente no es 24 meses. En SaaS, la expectativa de vida es `1 / churn` = `1 / 0.08` = **12,5 meses**.
3. **Ignoras el payback period y el costo de oportunidad.** Recuperar $290 con $24,50/mes de margen tarda casi un año. Mientras tanto, estás financiando esa adquisición con tu caja o deuda.

### 📊 Recálculo correcto
| Concepto | Fórmula | Resultado |
|----------|---------|-----------|
| Margen bruto mensual por cliente | $35 × 70% | **$24,50** |
| Vida media del cliente | 1 / 0,08 | **12,5 meses** |
| **LTV (margen)** | $24,50 × 12,5 | **$306,25** |
| **LTV / CAC** | $306,25 / $290 | **≈ 1,06** |
| **Payback period** | $290 / $24,50 | **≈ 11,8 meses** |

### ⚠️ Qué significa esto en la práctica
- **LTV/CAC = 1,06**: Estás casi empatando por cliente. No cubres gastos operativos, impuestos, soporte, ni el costo de capital. La regla mínima para escalar con paid ads es **≥ 3,0** (idealmente ≥ 4,0).
- **Payback de ~12 meses**: Con 8% de churn mensual, `(0,92)^11,8 ≈ 37%`. Es decir, **~63% de los clientes se irán antes de que recuperes los $290**. Estás financiando churn con caja.
- **Escalar paid ads suele subir el CAC**. Al inyectar $10k, es probable que tu CAC real suba a $320-$350 por saturación de audiencia o menor calidad de tráfico, empeorando la ratio.

### 🛑 ¿Le das? 
**No. Frena la inversión agresiva hasta corregir la unidad económica.**

### ✅ Qué necesitas para que el plan sea viable
| Métrica | Valor actual | Umbral mínimo para escalar | Cómo llegar |
|--------|--------------|---------------------------|-------------|
| LTV/CAC | 1,06 | ≥ 3,0 | Bajar CAC a ≤ $100 o subir margen/retención |
| Payback | 11,8 meses | ≤ 6 meses | Optimizar onboarding, upsell temprano o reducir CAC |
| Churn mensual | 8% | ≤ 4-5% | Mejorar product-market fit, soporte proactivo, engagement loops |

### 🧪 Siguiente paso recomendado
1. **Prueba con $1.000-$1.500** este mes. Mide CAC real, payback observado y churn a 30/60 días.
2. **Calcula el payback real con cohortes**, no con promedios teóricos.
3. **Ataca el churn primero**: cada 1% que bajes (de 8% a 7%) sube el LTV ~14%. Es la palanca más barata.
4. **Solo escala cuando**: `LTV/CAC ≥ 3` Y `Payback ≤ 6 meses` Y `CAC se mantiene estable al duplicar presupuesto`.

Los números no mienten. Con una ratio de 1,06, escalar es acelerar hacia un muro. Arregla la aritmética unitaria primero; el crecimiento real viene después. ¿Quieres que te arme una hoja de cálculo de cohortes o un simulador de sensibilidad para ver qué palanca mover primero?