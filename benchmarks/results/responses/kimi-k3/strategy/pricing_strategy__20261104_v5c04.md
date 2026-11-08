# Kimi K3 — strategy/pricing_strategy

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.74 | quality: 10.0
- latency_total: 336.237s | tokens_per_second: 34.2
- input_tokens: 281 | output_tokens: 11498

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

# Análisis de aumento de precio: $60 → $89/mes (+48%)

**Supuesto clave:** con 200 clientes y 7% de churn, pierdes ~14 clientes/mes. Si tu base está estable, estás agregando ~14 clientes/mes. Uso eso como línea base.

---

## 1. LTV/CAC actual y proyectado

**Fórmula:** LTV = ARPU / churn mensual → Vida útil = 1/0.07 = 14.3 meses (coincide con tus 14)

| Métrica | Actual ($60) | A $89 (sin cambio de churn) |
|---|---|---|
| LTV (revenue) | $857 | $1,271 |
| LTV/CAC | **7.1x** | **10.6x** |
| LTV ajustado por margen (ARPU − $8) | $743 | $1,157 |
| LTV/CAC ajustado | 6.2x | 9.6x |
| Payback de CAC | 2.3 meses | 1.6 meses |

**El número crítico — churn de equilibrio:** el aumento destruye valor solo si el churn sube de 7% a más de **~10.5%** (donde $89/0.105 ≈ $857). Es decir, el churn tendría que aumentar **+3.5 puntos sostenidos** (+50% relativo) para que la jugada sea neutral. Ese es tu margen de seguridad.

---

## 2. Impacto estimado en churn (benchmarks)

Benchmarks de la industria SaaS para aumentos de precio:

- **Aumentos bien ejecutados** (aviso previo + grandfathering + narrativa de valor): +0.5 a 1.5 puntos de churn sostenido, pico transitorio de 3-8% de la base en los primeros 60-90 días
- **Aumentos mal ejecutados** (sin aviso, sin valor agregado): +3 a 5 puntos
- **Productos con altos switching costs** (inventario = datos históricos, integraciones, workflows operativos) tienen elasticidad baja: los clientes no se van por $29/mes si migrar cuesta semanas
- **Advertencia:** un salto de 48% es agresivo. Los aumentos que el mercado absorbe sin fricción suelen ser 10-25%. Por eso la estructura de implementación (sección 5) importa más que el número
- **Red flag independiente:** 7% mensual (58% anual) ya es alto. El benchmark SMB SaaS es 3-5%. Parte del churn que verás post-aumento será churn preexistente "saludando con la mano"

**Mi estimación:** churn sostenido sube a **8-9%**, con pico one-time de 5-10% de la base durante la migración (menos si hay grandfathering).

---

## 3. Tres escenarios

| Métrica | Actual | Optimista (prob. ~25%) | Realista (prob. ~50%) | Pesimista (prob. ~25%) |
|---|---|---|---|---|
| Churn sostenido | 7% | 8% | 9% | 11% |
| Pérdida one-time en migración | — | 8 clientes (4%) | 15 (7.5%) | 25 (12.5%) |
| CAC (por caída de conversión) | $120 | $120 | $132 | $150 |
| Altas/mes | 14 | 14 | 13 | 12 |
| **LTV** | $857 | $1,113 | $989 | $809 |
| **LTV/CAC** | 7.1x | **9.3x** | **7.5x** | **5.4x** |
| Clientes en estado estacionario | 200 | 175 | 144 | 109 |
| **MRR estado estacionario** | $12,000 | **$15,575 (+30%)** | **$12,856 (+7%)** | **$9,708 (−19%)** |
| Margen bruto mensual | $10,400 | $14,175 | $11,664 | $8,829 |

**Valor esperado:** +6% de MRR y LTV/CAC de ~7.4x (vs 7.1x actual). Positivo pero modesto *en estado estacionario*.

**Matiz importante:** el estado estacionario tarda 12-24 meses en llegar. Durante la transición, el MRR sube de inmediato (200 × $89 = $17,800 antes de que el churn erosione). Incluso en el escenario pesimista, los primeros ~10-12 meses generan más caja que el status quo — lo que te da tiempo para corregir.

---

## 4. Recomendación con números

**Sí, sube el precio, pero no de golpe a toda la base.** La matemática favorece el aumento (el churn tendría que empeorar +50% relativo para perder), y $89 sigue en el medio del rango competitivo ($29-$149). Estructura sugerida:

1. **Nuevos clientes a $89 desde ya.** Riesgo casi nulo (no tienen precio de referencia), validas willingness-to-pay real, y si el churn de nuevos se mantiene en ~7-8%, tu LTV/CAC sube a 9.3x
2. **Clientes existentes: migrar a $79 (no $89) con 60-90 días de aviso.** LTV = $79/0.08 = $988 (+15% vs actual) con un aumento percibido de "solo" 32% en vez de 48%. La lealtad se paga sola en churn evitado
3. **Plan anual a $890/año** ($74/mes efectivo, 2 meses gratis). Para existentes: $790/año ($66/mes) si migran en los primeros 30 días. Esto convierte el riesgo de churn en caja adelantada
4. **Crea un tier superior a $129-149** (multi-bodega, API, reportes avanzados). Ancla el $89 y captura el techo del mercado
5. **Guardrail:** si el churn sostenido supera 10.5% dos meses seguidos, revierte o ajusta. Ese es tu stop-loss

**Y lo más importante del análisis:** tu palanca real no es el precio, es el churn. A $89 con 5% de churn, LTV = $1,780 (+108% vs hoy). Cada punto de churn que recortes vale más que el aumento completo. Invierte parte del MRR incremental en onboarding y customer success.

---

## 5. Estrategia de implementación

**Fase 0 (Semana 1):** Segmenta tu base (antigüedad, uso, valor). Identifica las 20-30 cuentas estratégicas para outreach personal. Opcional: encuesta rápida de willingness-to-pay.

**Fase 1 (Semana 2): $89 solo para nuevos.** Actualiza pricing page con 3 tiers ($49 starter limitado / $89 pro / $149 business). Los existentes no ven cambio ni anuncio aún.

**Fase 2 (Mes 2-4): Medir.** Métricas de decisión:
- Conversión visita→trial→pago: si cae <15%, sigues adelante
- Si cae >25%: el mercado te dice que $89 sin valor agregado no se sostiene → considera $79 o agrega features
- Churn de cohortes nuevas a $89 vs cohortes viejas a $60

**Fase 3 (Mes 4): Migración de existentes.**
- Email personal del founder, 60-90 días de aviso, narrativa de valor (qué han recibido, qué viene en el roadmap)
- Tres opciones: (a) mensual a $79, (b) anual a $790 (bloquea 12 meses), (c) downgrade a $49 starter — el downgrade retiene al price-sensitive que si no churnearía
- Nunca cambies precio el mismo mes del anuncio

**Fase 4 (Mes 6+): Optimización.**
- Playbook de salvación: exit survey + oferta de 3 meses al precio anterior para quien cancela
- Revisión trimestral de churn por cohorte, NPS y tickets de soporte
- Instaura cadencia de aumentos pequeños anuales (3-8%): son casi invisibles vs un salto de 48% cada varios años

**Una regla de oro:** jamás subas precio mientras perciban que el valor baja. Sincroniza el anuncio con el lanzamiento de una feature visible o mejora de soporte.

¿Quieres que modele el flujo de caja mes a mes de los 24 meses de transición, o que profundice en la estructura de tiers?