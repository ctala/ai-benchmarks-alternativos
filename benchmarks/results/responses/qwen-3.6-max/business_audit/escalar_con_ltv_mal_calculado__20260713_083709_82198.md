# Qwen 3.6 Max — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.6-max-preview`
- success: True  | final: 7.04 | quality: 8.4
- latency_total: 83.071s | tokens_per_second: 33.7
- input_tokens: 217 | output_tokens: 2803

## Respuesta completa

**Verdict: No. No metas esos $10.000 aún. Tu plan se cae en la aritmética.**

Vamos a desmontar el cálculo paso a paso, como corresponde antes de quemar capital en paid media.

### 🔍 Errores en tu cálculo
1. **Vida promedio ≠ 24 meses.** Con un churn mensual del 8%, la vida media de un cliente es `1 / 0.08 = 12,5 meses`, no 24.
2. **LTV se calcula sobre margen, no sobre ingreso bruto.** Tu margen es 70%, así que tu contribución real por cliente es `$35 × 0,70 = $24,50/mes`.
3. **LTV/CAC se evalúa con margen y churn.** Tu fórmula ignora ambos.

### 📊 Números reales (unit economics)
- **LTV bruto (sobre margen):** `$24,50 / 0,08 = $306,25`
- **LTV/CAC real:** `$306,25 / $290 ≈ 1,06x` *(estándar mínimo saludable: ≥3x)*
- **Payback period:** `$290 / $24,50 ≈ 11,8 meses`
- **Retención a mes 12:** `0,92^12 ≈ 37%` → **el 63% de los clientes se va antes de que recuperes el CAC.**
- **Margen acumulado en 12 meses:** `≈ $194` → aún te faltan `$96` para empatar el CAC. La recuperación completa ocurre cerca del mes 15-16, con flujo de caja negativo todo ese tiempo.

### 💥 Qué pasa si metes $10.000 hoy
- Adquieres `~34 clientes`.
- Generan `~$833/mes` de margen bruto inicial.
- Con 8% churn mensual, esa base se erosiona rápido y **no recuperas la inversión publicitaria hasta después de un año**, asumiendo que el CAC no sube (spoiler: en paid ads, casi siempre sube al escalar).
- Esto no es escalar rentabilidad. Es **crecimiento tóxico financiado con caja**.

### ✅ Condiciones para aprobar el plan
Antes de abrir el grifo de paid ads, necesitas que los unit economics aguanten presión:
1. **Bajar churn mensual a ≤4%** (vida media ≥25 meses). Con 8%, ningún CAC razonable funciona.
2. **Reducir CAC a ≤$150** o subir precio/ARPU para que el payback caiga a ≤6 meses.
3. **Validar LTV/CAC ≥3x sobre margen**, no sobre revenue.
4. **Modelar cash flow, no solo LTV estático.** La publicidad se paga hoy; el LTV se cobra en cuotas con fugas.

### 🧭 Siguiente paso recomendado
- Congela el presupuesto de paid ads a nivel de prueba (`$1.000-$2.000`).
- Ataca retención: onboarding, activación, soporte proactivo, pricing tiers o compromisos anuales.
- Mide CAC y payback por cohorte real durante 3 meses.
- Cuando el payback sea ≤6 meses y el LTV/CAC ≥3x **sobre margen**, entonces sí: escala sin miedo.

Tu rentabilidad actual probablemente viene de clientes orgánicos, antiguos o de bajo CAC. **Escalar paid ads con estos números no multiplica ganancias; multiplica pérdidas diferidas.** 

¿Quieres que armemos un modelo de cohortes con tus datos reales para ver en qué mes exacto se quiebra el flujo?