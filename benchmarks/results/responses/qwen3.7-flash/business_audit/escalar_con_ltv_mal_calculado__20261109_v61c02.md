# Qwen 3.7 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.09 | quality: 10.0
- latency_total: 32.825s | tokens_per_second: 77.0
- input_tokens: 217 | output_tokens: 2529

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

**No. Tu plan muere en la aritmética.** Vamos a desmontarlo línea por línea, porque lo que ves arriba no es un plan de crecimiento, es una trampa de cashflow disfrazada de optimismo.

### 🔍 Errores críticos en tu cálculo
1. **Vida media del cliente no son 24 meses.**  
   Con un churn mensual del 8%, la vida media esperada es `1 / 0.08 = 12.5 meses`. A ese ritmo, solo el 36% de los clientes llegan al mes 12. Asumir 2 años es ignorar la exponencialidad del churn.

2. **El LTV no se calcula multiplicando precio × meses.**  
   Debes incluir el margen bruto y el churn. La fórmula estándar para SaaS con churn constante es:  
   `LTV = (ARPU × Margen Bruto) / Churn Mensual`  
   `LTV = ($35 × 0.70) / 0.08 = $24.50 / 0.08 = **$306.25**`

3. **Tu LTV/CAC real es ~1.06, no 2.9.**  
   `$306.25 / $290 ≈ 1.06`  
   En SaaS, un ratio < 1.5 ya es zona roja. < 1.0 significa que estás perdiendo dinero por cada nuevo cliente.

4. **Payback period: 11.8 meses.**  
   `CAC / Ganancia bruta mensual por cliente = $290 / $24.50 ≈ 11.8 meses`  
   Escalar con ads requiere recuperar la inversión en ≤ 12 meses (idealmente ≤ 6-8). Si el churn se acelera un 1%, o tu CPC sube un 10%, el payback se rompe y empiezas a quemar caja neta.

### 💸 Impacto real de meter $10.000 este mes
- Clientes nuevos: `~34` ($10k / $290)
- Inversión upfront: $10.000
- Ingreso bruto esperado en mes 1: `34 × $24.50 = $833`
- **Brecha de caja mes 1: -$9.167**  
  Y esa brecha no desaparece hasta el mes 12. Mientras tanto, si hay estacionalidad, churn mayor al esperado o cambios en el algoritmo de ads, el riesgo es tuyo.

### ✅ Cuándo sí aprobaría escalar con ads
| Métrica | Tu número | Umbral mínimo para escalar |
|---------|-----------|----------------------------|
| LTV/CAC | 1.06      | ≥ 3.0                      |
| Payback | 11.8 meses| ≤ 8 meses                  |
| Churn mensual | 8%  | ≤ 5%                       |
| CAC por canal | $290  | Optimizable a <$150        |

### 🛠 Qué hacer antes de tocar $10k
1. **Reduce churn a ≤5%** (onboarding, product-led triggers, win-back flows). Bajarlo a 5% eleva tu LTV a $588 y tu LTV/CAC a ~2.0.
2. **Añade margen recurrente** (upsell, annual billing con descuento, add-ons). Subir ARPU efectivo a $42 mueve el LTV a $662.
3. **Prueba de fuego con $2.000**: escala en un canal secundario, mide LTV real vs proyectado a 90 días y ajusta CAC antes de apalancar caja.
4. **Si mantienes CAC=$290 y churn=8%**, la única vía sostenible es crecimiento orgánico/referral o venta directa con alto ticket anual.

La aritmética no perdona suposiciones. Escalar con métricas rotas no acelera el crecimiento; solo quema caja más rápido. 

**Veredicto:** ❌ No aprobados los $10k. Vuelve cuando LTV/CAC ≥ 3 y payback ≤ 8 meses. Te ayudo a construir el modelo si ajustas churn, pricing o canales.