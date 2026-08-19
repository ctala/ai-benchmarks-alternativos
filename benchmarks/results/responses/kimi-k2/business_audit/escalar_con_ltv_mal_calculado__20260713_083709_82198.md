# Kimi K2 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 7.55 | quality: 8.14
- latency_total: 18.075s | tokens_per_second: 32.1
- input_tokens: 232 | output_tokens: 580

## Respuesta completa

No le des. Tu aritmética tiene tres muertes silenciosas.

---

## Muerte 1: El LTV real no es $840

Un churn del 8% mensual no da 24 meses de vida. Da esto:

**Vida útil esperada** = 1 ÷ 0,08 = **12,5 meses**

**LTV real** = $35 × 12,5 × 0,70 (margen bruto) = **$306**

*Nota: ya usaste el margen bruto en tu CAC, así que el LTV debe usarlo también para comparación limpia.*

---

## Muerte 2: El CAC está incompleto

Tu CAC de $290 es solo el costo publicitario. Pero hay más:

| Costo omitido | Estimación conservadora |
|-------------|------------------------|
| Costo creativo, agencia o tiempo del founder | +15-20% |
| Sales/CS asistido (si aplica onboarding) | +$0-50 |
| **CAC ajustado** | **~$330-350** |

Usemos **$330** como base conservadora.

---

## Muerte 3: El ratio LTV/CAC real

| Métrica | Tu cálculo | Real |
|--------|-----------|------|
| LTV | $840 | **$306** |
| CAC | $290 | **$330** |
| **Ratio** | 2,9× | **0,93×** |

---

## Veredicto

**Pierdes $24 por cada cliente que adquieres** ($306 − $330), antes de contar equipo, oficina, herramientas.

Con $10.000 quemas ~30 clientes y **recuperas ~$9.180**. Capital destruido: ~$820. Y eso asumiendo que el CAC no sube con la escala (rara vez baja).

---

## Antes de meter un dólar

| Acción | Por qué |
|-------|---------|
| Baja churn a <5% mensual | Duplica tu vida útil |
| Sube precio o ARPU con upsells | El margen salva más que el volumen |
| Testea canales orgánicos | CAC cercano a cero cambia la ecuación |
| Confirma CAC con cohortes de 90 días | El primero mes miente |

¿Tienes datos de cohortes reales de retención? Eso mataría o resucitaría estos números con certeza.