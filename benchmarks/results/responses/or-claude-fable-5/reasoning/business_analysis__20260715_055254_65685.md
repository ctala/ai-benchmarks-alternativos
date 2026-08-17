# Claude Fable 5 — reasoning/business_analysis

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.92 | quality: 10.0
- latency_total: 35.762s | tokens_per_second: 74.4
- input_tokens: 254 | output_tokens: 2660
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando análisis detallados y acciones concretas basadas en los datos.

## Respuesta completa

# Análisis de tu SaaS: Enero – Marzo

## 1. Métricas Clave

**ARPU (constante en los 3 meses):** $15/usuario — dato importante que retomaré abajo.

| Métrica | Enero | Febrero | Marzo |
|---|---|---|---|
| Churn rate mensual | 3.75% | 3.85% | 4.59% |
| Growth rate (usuarios/MRR) | — | +12.5% | +9.6% |
| LTV/CAC ratio | 4.9x | 4.5x | 5.2x |
| NRR (aprox.)* | — | ~95.7% | ~95.0% |
| Altas brutas estimadas | — | ~202 | ~198 |

*NRR estimado como (MRR inicial − MRR perdido por churn) / MRR inicial, asumiendo $15/churn. Como tu ARPU es plano, asumo que no hay revenue de expansión. Si tienes datos de upgrades/downgrades, el cálculo sería más preciso.

## 2. Tendencias Preocupantes

🔴 **Churn acelerándose:** subió 22% en relativo (3.75% → 4.59%). Es tu problema #1.

🔴 **Crecimiento desacelerando:** de 12.5% a 9.6% mensual. Nota clave: tus altas brutas están *planas* (~200/mes) — el crecimiento neto cae porque el churn sube, no porque adquieras menos.

🟡 **LTV en descenso:** $420 → $408. Consistente con el churn creciente (LTV = ARPU / churn).

🟡 **CAC bajo en marzo ($78) + pico de churn:** posible señal de que estás adquiriendo usuarios más baratos pero de peor calidad. Correlación a vigilar.

🟡 **ARPU estancado en $15 y NRR <100%:** cero expansión de revenue. Eres un "leaky bucket" — cada dólar de crecimiento depende 100% de adquisición nueva.

## 3. Tres Acciones Concretas

**1. Diagnóstico de churn por cohorte y canal (esta semana)**
Cruza los 68 churns de marzo con: canal de adquisición, antigüedad y uso del producto. Hipótesis a validar: el canal barato de marzo (CAC $78) trae usuarios que no activan. Implementa exit surveys obligatorias.

**2. Crear revenue de expansión (30 días)**
Con ARPU clavado en $15, no tienes tiers ni upsells funcionando. Lanza un plan superior o add-ons dirigidos a tu 20% de usuarios más activos. Llevar NRR de 95% a 100%+ vale más que cualquier campaña de adquisición.

**3. Programa de retención proactiva (30-60 días)**
Define un health score simple (login frequency + uso de features clave). Contacto automatizado a usuarios en riesgo antes del día 30. Ofrece plan anual con descuento (reduce churn mecánicamente y adelanta caja).

## 4. Proyección de Abril (si las tendencias continúan)

Asumiendo que la desaceleración y el churn siguen su trayectoria:

| Métrica | Proyección Abril |
|---|---|
| Growth rate | ~7-7.5% |
| Usuarios | ~1,585 |
| MRR | ~$23,700 |
| Churn rate | ~5.2% → **~78-82 churns** |
| LTV | ~$400 |
| NRR | ~94.5% |

**El dato crítico:** si la curva sigue, en ~4-5 meses tus churns (~200/mes proyectados hacia agosto) igualarán tus altas brutas (~200/mes) y **el crecimiento se detiene por completo**, aunque no cambies nada en adquisición.

**Conclusión:** tu unit economics es sana (LTV/CAC ~5x, muy por encima del benchmark de 3x), así que el problema no es rentabilidad — es retención. Cada punto de churn que recuperes vale más que cualquier optimización de CAC en este momento.

¿Tienes datos de cohortes o de canales de adquisición? Con eso podría afinar el diagnóstico del pico de churn de marzo.