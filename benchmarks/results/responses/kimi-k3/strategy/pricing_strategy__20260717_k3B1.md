# Kimi K3 — strategy/pricing_strategy

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 6.03 | quality: 7.5
- latency_total: 222.855s | tokens_per_second: 36.8
- input_tokens: 281 | output_tokens: 8192
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y estructurado que un emprendedor podría aplicar directamente.

## Respuesta completa

# Análisis de subida de precio: $60 → $89/mes

## 1. LTV/CAC actual y proyectado

**Situación actual:**

| Métrica | Valor |
|---|---|
| LTV (ingresos) | $60 ÷ 0.07 = **$857** |
| LTV ajustado por margen (precio − $8 costo) | $52 ÷ 0.07 = **$743** |
| LTV/CAC | 857 ÷ 120 = **7.1x** (6.2x por margen) |
| Payback del CAC | 120 ÷ 52 = **2.3 meses** |

**Con $89 (asumiendo churn sin cambios):**

| Métrica | Valor |
|---|---|
| LTV (ingresos) | $89 ÷ 0.07 = **$1,271** |
| LTV por margen | $81 ÷ 0.07 = **$1,157** |
| LTV/CAC | **10.6x** (9.6x por margen) |

**Lectura clave:** el benchmark saludable de SaaS es LTV/CAC > 3x. Estar en **7x es señal clásica de subpricing** (o de subinvertir en crecimiento). Tus unit economics tienen mucho margen para absorber un aumento. Esto respalda la subida.

## 2. Impacto estimado en churn

Dos datos importantes antes de proyectar:

- **Tu churn de 7% mensual ya es alto.** El rango típico de SaaS B2B para pymes es 3-5% mensual. 7% mensual = **~58% de churn anual**, lo que sugiere un problema de valor percibido u onboarding, no de precio.
- **Benchmarks de aumentos de precio en SaaS:** subidas bien ejecutadas de <20% suelen añadir 1-2 puntos de churn temporal que se normaliza en 2-3 meses. Subidas agresivas (>30%, como la tuya de **+48%**) pueden añadir 3-5 puntos si se comunican mal o se fuerzan sin transición.

**Factor a tu favor:** el software de inventario es *sticky* (sistema de registro, costo de migración alto, datos históricos). La elasticidad de tu base instalada será menor que la de un SaaS promedio.

**Número crítico — tu margen de seguridad:**
- Puedes perder hasta **32.6% de tu base** (1 − 60/89) y aún así igualar el MRR actual
- Por margen: hasta **35.8%** (1 − 52/81)

Ningún escenario razonable de una migración bien manejada supera el 20% de pérdida.

## 3. Tres escenarios

**Unit economics por cliente nuevo:**

| Métrica | Actual | Optimista | Realista | Pesimista |
|---|---|---|---|---|
| Churn mensual post-cambio | 7% | 7.5% | 8.5% | 10% |
| CAC (peor conversión) | $120 | $132 (+10%) | $150 (+25%) | $168 (+40%) |
| Vida promedio | 14.3 meses | 13.3 | 11.8 | 10 |
| LTV por margen | $743 | $1,080 | $953 | $810 |
| LTV/CAC (margen) | 6.2x | **8.2x** | **6.4x** | **4.8x** |
| Ganancia neta por cliente | $623 | **$948 (+52%)** | **$803 (+29%)** | **$642 (+3%)** |
| Payback CAC | 2.3 meses | 1.6 | 1.9 | 2.1 |

**Transición de tu base (200 clientes × $60 = $12,000 MRR):**

| | Optimista | Realista | Pesimista |
|---|---|---|---|
| Pérdida de la base | 5% (10) | 12% (24) | 20% (40) |
| MRR resultante | $16,910 | $15,664 | $14,240 |
| vs. actual | **+41%** | **+31%** | **+19%** |

**El riesgo oculto (importante):** hoy pierdes 14 clientes/mes, así que agregas ~14/mes. Si tu gasto de