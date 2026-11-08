# Qwen 3.6 Plus — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 51.234s | tokens_per_second: 57.6
- input_tokens: 217 | output_tokens: 2951

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

**No. Detén la inversión.** Tu aritmética tiene un error estructural que, si escalas con $10.000, te va a comer la rentabilidad.

### 🔍 Dónde falla tu cálculo
1. **Asumes 24 meses de vida, pero el churn dice otra cosa.** Con un churn del 8% mensual, la vida media real de un cliente es `1 / 0,08 = 12,5 meses`, no 24. Después de 12 meses solo queda ~37% de la cohorte; después de 24 meses, ~13%.
2. **El LTV se calcula sobre el margen, no sobre el precio.** La publicidad te cuesta $290, pero solo recuperas el 70% de cada factura.

### 📐 Cálculo correcto
- Ingreso mensual: `$35`
- Margen bruto (70%): `$35 × 0,70 = $24,50/mes`
- Churn mensual: `8% → 0,08`
- **LTV = Margen mensual / Churn = `$24,50 / 0,08 = $306,25`**
- **LTV/CAC = `$306,25 / $290 ≈ 1,06`**

### ⚠️ Lo que significa en la práctica
- Estás **muy por debajo** del umbral saludable de `3:1`. Cada cliente nuevo te deja apenas ~$16 de ganancia bruta vitalicia, antes de soporte, impuestos o costos fijos.
- **Payback period:** `$290 / $24,50 ≈ 11,8 meses`. Con 8% de churn, más del 60% de los clientes se irán antes de que recuperes la inversión.
- Escalar $10k hoy significa adelantar $10k en caja para recuperarlos lentamente, mientras la mayoría de esos clientes churnean. Es una receta para quemar liquidez y destruir margen.

### 🛠 Qué necesitas antes de escalar
| Palanca | Meta mínima | Impacto en LTV/CAC |
|--------|-------------|-------------------|
| Churn mensual | ≤ 4-5% | LTV sube a $490-$612 → ratio 1,7-2,1 |
| CAC | ≤ $80-90 | Ratio ≥ 3,4 |
| Precio o margen | +15-20% | LTV sube proporcionalmente |

**Pasos concretos:**
1. **No gastes $10k.** Prueba con `$500-$1.000` y mide CAC real, payback y retención a 30/60/90 días.
2. **Ataca el churn primero.** Onboarding, activation metrics, soporte proactivo o cambios de pricing. Bajar de 8% a 5% mensual casi duplica tu LTV.
3. **Optimiza adquisición.** Si el CAC sube al escalar (rendimientos decrecientes en ads), tu ratio empeorará. Busca canales con payback < 6 meses o mejora tu conversión orgánica/referral.
4. **Modela el flujo de caja.** Con 8% churn, cada mes pierdes ~8% de la base. Escalar sin corregir retención o CAC es como llenar un balde con agujeros.

### ✅ Regla de fuego para escalar con ads
- `LTV/CAC ≥ 3`
- `Payback ≤ 6 meses`
- `Churn ≤ 5% mensual` (ideal ≤ 3%)
- `CAC estable o decreciente al aumentar spend`

Cuando cumplas estos 4, aceleras con confianza. Hasta entonces, cada dólar en ads te está regalando valor al mercado.

¿Quieres que te arme una hoja de cálculo con 3 escenarios (churn 5%, CAC $150, precio $45, etc.) para ver exactamente qué palanca te lleva al ratio saludable?