# Claude Fable 5 (suscripción) — reasoning/business_analysis

- model_id: `claude-fable-5`
- success: True  | final: 7.2 | quality: 10.0
- latency_total: 41.193s | tokens_per_second: 70.6
- input_tokens: 2 | output_tokens: 2908

## Respuesta completa

# Análisis SaaS — Ene-Mar

## 1. Métricas clave

| Métrica | Enero | Febrero | Marzo |
|---|---|---|---|
| Churn rate mensual | 3.75% | 4.33% (52/1,200) | 5.04% (68/1,350) |
| Growth rate (usuarios) | — | +12.5% | +9.6% |
| Growth rate (MRR) | — | +12.5% | +9.6% |
| LTV/CAC | 4.9x | 4.5x | 5.2x |
| NRR* | — | ~95.7% | ~95.0% |
| ARPU | $15.00 | $15.00 | $15.00 |
| Altas brutas | — | 202 | 198 |

*NRR estimado como (MRR inicial − MRR perdido por churn) / MRR inicial. Con ARPU plano en $15, no hay expansión: NRR < 100% por definición.

## 2. Tendencias preocupantes

1. **Churn acelerando: +34% en 2 meses** (3.75% → 5.04%). Es el problema #1. A este ritmo, el churn implícito de tu LTV ($408/$15 = ~27 meses de vida) ya no se sostiene — con 5% de churn real, el LTV honesto es ~$300, no $408.

2. **Crecimiento desacelerando con adquisición plana.** Altas brutas: 202 → 198. Tu crecimiento neto cae porque el churn se come las altas, no porque adquieras menos. Si la tendencia sigue, el crecimiento neto llega a cero en ~8 meses.

3. **Cero expansión de revenue.** ARPU clavado en $15 los 3 meses. NRR de 95% significa que cada mes arrancas con un hoyo de ~$1,000 que debes rellenar con adquisición. Los SaaS sanos tienen NRR >100%.

4. **Bandera amarilla en el CAC de marzo.** Bajó de $92 a $78 (−15%) el mismo mes que el churn saltó a 5%. Posible correlación: canal más barato trayendo usuarios de peor calidad. No lo afirmo como causa — verifica churn por cohorte de canal antes de escalar ese canal.

## 3. Tres acciones concretas

1. **Análisis de cohortes de churn esta semana.** Cruza los 68 churns de marzo con: canal de adquisición, antigüedad y uso del producto en los primeros 14 días. Si los churners vienen del canal barato de marzo, el CAC de $78 es una ilusión. Meta: bajar churn de 5% a 3.5% — eso solo ya recupera ~$330 MRR/mes que componen.

2. **Lanzar palanca de expansión.** ARPU plano = no estás cobrando más a nadie. Opciones rápidas: plan anual con descuento (cash + retención), tier superior, o add-on. Necesitas que NRR cruce 100% para que el crecimiento deje de depender 100% de adquisición.

3. **Intervención de onboarding/activación.** Con churn mensual de 5%, lo más probable es que la fuga esté en los primeros 30-60 días. Email/secuencia de activación + checkpoint humano (o automatizado) al día 7 para usuarios sin uso. Es la palanca más barata contra churn temprano.

## 4. Proyección abril (si las tendencias continúan)

- **Churn rate:** ~5.7% (sigue subiendo ~0.7pp/mes) → **~84 churns**
- **Altas brutas:** ~196 (planas)
- **Usuarios:** 1,480 + 196 − 84 ≈ **1,592** (+7.6%, sigue desacelerando: 12.5% → 9.6% → 7.6%)
- **MRR:** ~**$23,880** (ARPU $15 sin expansión)
- **LTV reportado:** ~$400, pero el real con 5.7% churn sería ~$263 — ojo con decisiones de inversión en adquisición basadas en el LTV viejo
- **NRR:** ~94.5%, siguiendo en caída

**El resumen en una línea:** estás creciendo en bruto pero el balde tiene un hoyo que se agranda. Arregla retención antes de meter más plata en adquisición — cada dólar de CAC hoy compra un usuario que vale menos cada mes.