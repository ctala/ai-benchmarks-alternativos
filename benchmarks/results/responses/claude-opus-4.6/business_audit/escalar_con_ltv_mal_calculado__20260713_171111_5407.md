# Claude Opus 4.6 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 8.05 | quality: 10.0
- latency_total: 27.391s | tokens_per_second: 44.0
- input_tokens: 239 | output_tokens: 1205
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y consejos prácticos para un emprendedor.

## Respuesta completa

# Revisión de tus unit economics

Tu intuición de escalar es buena, pero tu aritmética tiene errores graves. Vamos paso a paso.

---

## Error 1: El lifetime está mal calculado

Con 8% de churn mensual, el lifetime promedio no es 24 meses.

$$\text{Lifetime promedio} = \frac{1}{\text{churn}} = \frac{1}{0.08} = 12.5 \text{ meses}$$

**No 24 meses. La mitad.** El churn del 8% es alto; pierdes casi 1 de cada 12 clientes cada mes.

---

## Error 2: El LTV real es mucho menor

$$\text{LTV (revenue)} = \$35 \times 12.5 = \$437.50$$

Pero además necesitas aplicar tu margen bruto, porque no todo ese ingreso es ganancia disponible para recuperar el CAC:

$$\text{LTV (gross profit)} = \$437.50 \times 0.70 = \$306.25$$

---

## Error 3: El ratio real está al borde

$$\frac{\text{LTV}}{\text{CAC}} = \frac{\$306.25}{\$290} = 1.06$$

| Concepto | Tu cálculo | Cálculo real |
|---|---|---|
| Lifetime | 24 meses | 12.5 meses |
| LTV (revenue) | $840 | $437.50 |
| LTV (gross profit) | no lo calculaste | **$306.25** |
| LTV/CAC | ~2.9 | **1.06** |

Estás recuperando apenas **$16.25 de gross profit por cliente** después de pagar la adquisición. Y eso sin contar soporte, tu salario, herramientas, ni nada operativo.

---

## El problema del payback

Incluso ignorando todo lo anterior, veamos cuánto tardas en recuperar los $290:

$$\text{Contribución mensual por cliente} = \$35 \times 0.70 = \$24.50$$

$$\text{Meses para recuperar CAC} = \frac{\$290}{\$24.50} = 11.8 \text{ meses}$$

Con un lifetime de 12.5 meses, recuperas el CAC apenas un mes antes de que el cliente promedio se vaya. **Estás financiando el crecimiento de otros durante casi un año antes de ver un centavo.**

Si metes $10.000 este mes, adquieres ~34 clientes, y necesitas casi 12 meses para recuperar ese dinero. Mientras tanto, esos clientes se van cayendo por churn desde el mes 1.

---

## Qué haría antes de meter $10.000

**La palanca más rentable no es gastar más en ads, es arreglar el churn.**

Mira el impacto de bajar churn de 8% a 4%:

| Churn | Lifetime | LTV (GP) | LTV/CAC | Payback |
|---|---|---|---|---|
| 8% | 12.5 meses | $306 | 1.06 | 11.8 meses |
| 4% | 25 meses | $612 | 2.11 | 11.8 meses |
| 3% | 33 meses | $808 | 2.79 | 11.8 meses |

Reducir churn a la mitad **duplica tu LTV sin gastar un centavo más en ads.**

### Plan concreto

1. **No escales publicidad todavía** — con estos números, escalar amplifica un problema, no una ventaja.
2. **Diagnostica el churn del 8%** — ¿en qué mes se van? ¿Mes 1-2 (onboarding malo) o gradual (falta de valor percibido)?
3. **Baja churn al 4% o menos** — onboarding, activación, soporte proactivo, lo que haga falta.
4. **Reduce CAC en paralelo** — ¿puedes probar canales orgánicos, referidos, partnerships?
5. **Escala cuando LTV/CAC ≥ 3 con payback ≤ 6 meses** — ahí sí mete $10.000, $50.000, lo que quieras.

---

**Línea final:** tu negocio es rentable porque crece orgánicamente con costos bajos. El momento en que metas $10.000 mensuales en ads con un LTV/CAC de 1.06, esa rentabilidad desaparece. Arregla la retención primero, después escala.