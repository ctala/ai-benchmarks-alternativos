# Qwen 3.7 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.06 | quality: 10.0
- latency_total: 32.097s | tokens_per_second: 90.2
- input_tokens: 217 | output_tokens: 2894

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

No le des el visto bueno. Tu cálculo de LTV contiene un error estructural que invierte completamente la rentabilidad del plan.

### 🔍 Dónde falla tu aritmética
Multiplicar `$35 × 24` asume retención perfecta durante dos años. Con un churn mensual del 8%, eso no ocurre. Además, no aplicas el margen bruto desde el primer mes.

### 📊 Cálculo correcto (estándar de unit economics)
- **Ingreso mensual por cliente (ARPU):** $35
- **Margen bruto mensual:** `$35 × 70% = $24.50`
- **Vida media estimada:** `1 / churn = 1 / 0.08 = 12.5 meses`
- **LTV real:** `$24.50 × 12.5 = $306.25`

*(Nota: esta fórmula es la aproximación estándar para modelos recurrentes. Con descuento financiero sería ligeramente menor, pero suficiente para tomar decisiones).*

### 📉 Métricas reales
| Indicador | Tu cálculo | Real |
|-----------|------------|------|
| LTV | $840 | **$306.25** |
| LTV/CAC | 2.9 | **1.06** |
| Payback Period | N/A | **~11.8 meses** (`$290 ÷ $24.50`) |

### ⚠️ Lo que esto significa en la práctica
- **LTV/CAC de 1.06** está muy por debajo del umbral seguro para escalar con paid ads. El estándar de mercado es **≥ 3**, y como mínimo **≥ 1.5–2** antes de inyectar capital.
- **Payback de ~12 meses** significa que recuperas la inversión casi un año después de adquirir al cliente. Cualquier pico de churn, cambio en el algoritmo de anuncios o variación estacional te dejará en rojo operativo.
- Por cada cliente nuevo, estás destruyendo valor: `$306.25 (LTV) - $290 (CAC) ≈ -$16` en términos estáticos. Con $10,000 de presupuesto, esperarías perder **~$560 solo en adquisición**, sin contar el costo de oportunidad del cash ni el riesgo de deterioro del churn al escalar volumen frío.

### ✅ Qué hacer antes de aprobar cualquier gasto
1. **Reduce el CAC** a `< $150` (optimización creativa, segmentación, canales orgánicos/influencers, referral program).
2. **Baja el churn mensual** a `< 5%` (onboarding mejorado, product-led growth, pricing tiers, win-back flows). Con 5% de churn, la vida media sube a 20 meses y el LTV real a ~$490.
3. **Haz un test controlado**: escala máximo `$1,000–$2,000` validando que LTV/CAC ≥ 2.5 y payback ≤ 9 meses antes de tocar cifras mayores.
4. Si el precio o el margen son rígidos, **replantea el modelo**: ¿puedes vender anual/prepagado para mejorar el cash flow y reducir el payback efectivo?

La aritmética de unit economics no negoció contigo porque "ya eres rentable". Es probable que lo seas con tráfico orgánico o referidos, pero la publicidad pagada expone directamente la estructura de costos. Cuando el LTV/CAC esté sólido por encima de 3 y el payback baje de 9 meses, ahí sí aprietas el botón. Hasta entonces, el crecimiento rápido es solo quema de caja disfrazada.