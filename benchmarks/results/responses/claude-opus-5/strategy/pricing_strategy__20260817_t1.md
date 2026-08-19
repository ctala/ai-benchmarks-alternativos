# Claude Opus 5 — strategy/pricing_strategy

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 2.58 | quality: 2.5
- latency_total: 108.238s | tokens_per_second: 75.7
- input_tokens: 288 | output_tokens: 8192

## Entrada exacta (lo que recibió el modelo)

**user:**

Mi SaaS de gestion de inventario tiene estos datos:
- CAC actual: $120
- LTV promedio: $840 (14 meses * $60/mes)
- Churn mensual: 7%
- 200 clientes actuales
- Competidores cobran entre $29 y $149/mes
- Mi costo por usuario es ~$8/mes

Estoy considerando subir el precio de $60 a $89/mes.
Analiza:
1. Calcula el LTV/CAC ratio actual y como cambiaria
2. Estima el impacto en churn (usa benchmarks de la industria SaaS)
3. Modela 3 escenarios: optimista, realista, pesimista
4. Dame tu recomendacion con numeros concretos
5. Sugiere una estrategia de implementacion (grandfather, gradual, etc)


## Respuesta completa

# Análisis de pricing: $60 → $89/mes

---

## 0. Primero, una corrección metodológica

Tu LTV de $840 usa **ingreso bruto**, no margen. Para decisiones de pricing hay que usar margen de contribución:

| Métrica | Cálculo | Valor |
|---|---|---|
| Margen bruto/usuario | $60 − $8 | $52 (86.7%) |
| Vida media | 1 / 0.07 | 14.3 meses |
| **LTV (ingreso)** | $60 × 14.3 | **$857** |
| **LTV (margen)** ← usa este | $52 / 0.07 | **$743** |
| MRR actual | 200 × $60 | $12,000 |
| CAC payback | $120 / $52 | **2.3 meses** |

---

## 1. LTV/CAC actual y proyectado

**Actual: 6.2x** (margen) / 7.1x (ingreso)

Esto es una señal roja disfrazada de buena noticia. El benchmark saludable es **3–4x**. Un 6.2x con payback de 2.3 meses significa una de dos cosas (probablemente ambas):

1. **Estás subvalorando el producto** → sí, sube el precio.
2. **Estás subinvirtiendo en adquisición** → deberías estar gastando mucho más en CAC. Con esos números podrías pagar $250 de CAC y seguir sano.

Con solo 200 clientes y payback de 2.3 meses, tu cuello de botella probablemente **no es el precio, es el volumen de adquisición y el churn**.

### El número que decide todo: churn de indiferencia

¿Cuánto puede subir tu churn antes de que el aumento de precio destruya valor?

| Precio | Margen/mes | Churn máximo tolerable | Margen vs. hoy (7%) |
|---|---|---|---|
| $60 (hoy) | $52 | 7.0% | — |
| $69 | $61 | 8.2% | +17% |
| $79 | $71 | **9.6%** | +37% |
| **$89** | **$81** | **10.9%** | **+56%** |
| $99 | $91 | 12.2% | +75% |
| $119 | $111 | 14.9% | +113% |

**A $89, tu churn tendría que subir de 7% a 10.9% (+56% relativo) para que quedes igual.** Eso es muy improbable con una ejecución decente. El aumento tiene un colchón enorme.

---

## 2. Impacto estimado en churn (benchmarks)

Hay que separar **tres efectos distintos** que la gente suele mezclar:

| Efecto | Benchmark de industria | Tu caso (+48% de precio) |
|---|---|---|
| **A. Cancelaciones puntuales** de base existente | Bien ejecutado (aviso 60–90d + narrativa de valor + grandfathering): 1–3%. Mal ejecutado: 10–25% | 3–12% si migras la base |
| **B. Churn recurrente** post-cambio | Sube 0.5–1.5 pts absolutos; en algunos casos **baja** (precio alto filtra clientes serios) | 7% → 7.5–8.5% |
| **C. Conversión trial→pago** | Elasticidad SMB SaaS: −0.3 a −0.8. Un +48% de precio típicamente reduce conversión 15–30% | −15% a −35% → CAC sube 15–50% |

**Contexto importante sobre tu churn de 7%:** eso es 58% anual de logo churn. El benchmark SMB SaaS bueno es 3–5% mensual; best-in-class <2%. **Tu problema principal no es el precio.** Vuelvo a esto en la sección 4.

---

## 3. Tres escenarios

**Supuestos comunes:** ~14 nuevos clientes/mes hoy (equilibrio con 200 clientes al 7%), costo $8/usuario, base migrada al nuevo precio.

### Economía unitaria en estado estable

| | Base | Optimista | Realista | Pesimista |
|---|---|---|---|---|
| Precio | $60 | $89 | $89 | $89 |
| Churn mensual | 7.0% | 7.5% | 8.5% | 11.0% |
| Vida media (meses) | 14.3 | 13.3 | 11.8 | 9.1 |
| CAC | $120 | $138 | $150 | $180 |
| Nuevos/mes | 14 | 13 | 11 | 9 |
| **LTV (margen)** | **$743** | **$1,080** | **$953** | **$736** |
| **LTV/CAC** | **6.2x** | **7.8x** | **6.4x** | **4.1x** |
| CAC payback | 2.3 m | 1.7 m | 1.9 m | 2.2 m |

**Observación clave: incluso el escenario pesimista deja un LTV/CAC de 4.1x**, por encima del umbral de 3x. La economía unitaria no se rompe en ningún escenario.

### Proyección a 12 meses (MRR y margen acumulado)

| | Base | Optimista | Realista | Pesimista |
|---|---|---|---|---|
| Churn puntual mes 0 | — | 5% (−10) | 12% (−24) | 25% (−50) |
| Clientes mes 0 | 200 | 190 | 176 | 150 |
| **Clientes mes 12** | **200** | **180** | **146** | **99** |
| **MRR mes 12** | **$12,000** | **$16,011** (+33%) | **$12,950** (