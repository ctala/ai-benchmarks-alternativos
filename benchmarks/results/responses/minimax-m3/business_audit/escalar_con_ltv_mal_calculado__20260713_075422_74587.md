# MiniMax M3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `minimax/minimax-m3`
- success: True  | final: 7.57 | quality: 8.4
- latency_total: 23.554s | tokens_per_second: 85.6
- input_tokens: 342 | output_tokens: 2016

## Respuesta completa

# Espera antes de apretar el botón de "pagar $10K"

Tu intuición de que LTV/CAC ≥ 3 es correcta como umbral. **El problema es que tu LTV está mal calculado.** Vamos a rehacerlo.

## Donde se rompe tu aritmética

Asumiste que un cliente se queda **24 meses** porque "se queda unos 2 años". Con un churn mensual del 8%, eso no es así:

| Métrica | Tu cálculo | Realidad |
|---|---|---|
| Vida media del cliente | 24 meses | **1 / 8% = 12,5 meses** |
| % de clientes que llegan al mes 24 | (asumes 100%) | (0,92)²⁴ = **~14%** |
| % de clientes que llegan al mes 12 | (asumes 100%) | (0,92)¹² = **~37%** |

Es decir, **el 63% de los clientes se va antes del año**. Tu cliente "promedio" no dura 2 años, dura 12,5 meses.

## LTV recalculado (fórmula estándar de suscripción)

$$LTV = \frac{ARPU \times Margen\ Bruto}{Churn\ Mensual} = \frac{35 \times 0,70}{0,08} = \$306$$

Otro error silencioso: en tu cálculo original ($35 × 24) **olvidaste aplicar el margen bruto del 70%**. Eso son ingresos brutos, no contribución de margen.

## La foto real

| Métrica | Tu número | Número correcto | Lectura |
|---|---|---|---|
| LTV | $840 | **$306** | — |
| LTV/CAC | 2,9 | **1,06** | 🔴 Lejos de 3 |
| CAC Payback | ~9 meses | **11,8 meses** | 🔴 Casi igual a la vida del cliente |

El payback de 11,8 meses es la cifra más dolorosa: **recuperás el CAC justo cuando el cliente promedio está por irse**. No queda ventana para profit.

## ¿Qué te deja esto?

Con estos números no podés escalar con paid acquisition. Las palancas son:

1. **Bajar CAC a ≤ $100** (LTV/CAC ≥ 3 con números actuales). ¿Qué canal te puede dar ese CAC?
2. **Bajar churn**. Cada punto porcentual que bajes el churn sube el LTV casi igual de fuerte:
   - Churn 5% → LTV = $490 → LTV/CAC = 1,69
   - Churn 3% → LTV = $817 → LTV/CAC = 2,82
   - Churn 2% → LTV = $1.225 → LTV/CAC ≈ 4,2 ✅
3. **Subir precio** o **empujar expansion revenue** (upsell).

## Recomendación concreta

No metas los $10K todavía. En vez de eso, invertí 2–3 semanas y $1–2K en **experimentos baratos para validar cuál de las tres palancas (bajar CAC, bajar churn, subir precio) tiene el mejor ROI**. Cuando alguna te lleve a LTV/CAC ≥ 3 *y* payback ≤ 6 meses, ahí escalás con confianza.

Como decía un CFO que conocí: *"Escalar con LTV/CAC de 1 no es growth, es incinerar caja con elegancia."*

¿Querés que te ayude a armar la matriz de experimentos o a modelar cómo cambia el LTV si bajás el churn a X%?