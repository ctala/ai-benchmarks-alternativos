# GLM 5.3 — strategy/pricing_strategy

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 242.828s | tokens_per_second: 74.3
- input_tokens: 192 | output_tokens: 18051

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

# Análisis: Subida de $60 → $89/mes (+48%)

**Supuesto clave que faltaba:** con 200 clientes y 7% de churn mensual, pierdes ~14 clientes/mes. Asumo que adquieres **~15 nuevos clientes/mes** (base estable). Todos los escenarios abajo usan esto.

---

## 1. LTV/CAC actual y proyectado

| Métrica | Actual ($60) | A $89 (churn igual) |
|---|---|---|
| LTV bruto | $840 | $1,246 |
| LTV neto (menos COGS $8/mes) | $743 | $1,157 |
| **LTV/CAC** | **7.0** (6.2 neto) | **10.4** (9.6 neto) |
| Payback CAC | 2.3 meses | 1.5 meses |

Tu ratio actual de 7.0 ya es muy saludable (benchmark: >3 es viable, >5 es excelente). Esto indica que **tienes poder de fijación de precio** — probablemente estás subvalorado.

**El número más importante del análisis:** el punto de equilibrio. Tu LTV por cliente se mantiene igual al actual si el churn sube hasta **~10.6% mensual** (de 7%). Es decir, el aumento de 48% te da un colchón de ~50% de deterioro en churn antes de perder dinero por cliente.

---

## 2. Impacto estimado en churn (benchmarks SaaS)

Contexto primero: tu 7% mensual ya está en el **techo del rango SMB (3-7%)**. Retención anual: solo 42%. Tu base es sensible a precio.

Patrones de industria (Price Intelligently/Paddle, OpenView):
- **Grandfathering:** impacto en churn ≈ 0%
- **Migración con aviso de 60+ días:** pérdida única de 5-15% de la base
- **Aumentos >30% en SMB:** conversión de clientes nuevos cae 10-30%
- El churn post-migración suele **normalizarse tras 6-9 meses** (se van los sensibles al precio; los que entran a $89 se autoseleccionan y suelen churnear *menos*)

**Estimación central:** churn 7% → 9-10% durante el lavado, pérdida única de ~10-12% de la base.

---

## 3. Tres escenarios (12 meses)

| | Sin cambio | Optimista | Realista | Pesimista |
|---|---|---|---|---|
| Pérdida única en migración | — | 5% | 12% | 25% |
| Churn mensual post-aumento | 7% | 7.5% | 9% | 12% |
| Nuevos clientes/mes | 15 | 13.5 | 12.5 | 10.5 |
| **Ingresos 12 meses** | **$147K** | $199K (+35%) | $173K (+18%) | $130K (−12%) |
| **Utilidad bruta 12 meses** | **$128K** | $182K (+42%) | $158K (+23%) | $118K (−8%) |
| Clientes al mes 12 | 208 | 184 | 151 | 101 |
| MRR estado estable | $12.9K | $16.0K | $12.4K | $7.8K |

Valor esperado (25/50/25): ~$154K de utilidad bruta → **+$26K vs. no hacer nada**.

**Matiz crítico:** incluso el escenario realista gana en 12 meses (la base actual paga más), pero su MRR de estado estable es solo paridad. El escenario pesimista sí destruye valor. La apuesta se paga, pero el downside existe.

---

## 4. Mi recomendación: sí sube, pero no de golpe para todos

**Sube a $89 solo para clientes nuevos desde ya, y grandfathering de 12 meses para los actuales.**

Los números de este híbrido:
- Utilidad bruta año 1: **~$150K (+$22K vs. base)**
- Downside contenido: incluso si la conversión de nuevos cae 30%, sigues en ~$138K (por encima del baseline)
- El grandfathering es más barato de lo que parece: con 7% de churn, **solo ~42% de tu base actual seguirá viva en 12 meses**. El "costo" de no cobrarles el aumento es ~$8-10K en el año — barato como seguro contra el escenario pesimista.

Justificación de $89: estás en la mitad del rango de competidores ($29-149), margen bruto pasaría de 87% a 91%, y tu payback de 1.5 meses te deja margen para absorber caída en conversión.

**Advertencia paralela:** reducir churn de 7% → 5% sube tu LTV un 40% — más de lo que te daría la subida de precio exitosa. Con retención anual de 42%, el churn es tu problema estructural más grande. No lo ignores mientras haces esto.

---

## 5. Plan de implementación

**Semanas 1-2 — Preparación**
- Segmenta la base por uso y antigüedad; llama personalmente a tu top 20
- Encuesta de disposición a pagar (Van Westendorp) a una muestra

**Semanas 3-8 — Test con nuevos**
- $89 para todos los clientes nuevos ya
- Mide conversión vs. baseline durante 4-6 semanas. Si cae >30%, considera $79

**Mes 2 — Anuncio a la base**
- Aviso de 60-90 días: "tu precio actual garantizado 12 meses; después $89"
- **Ofrece plan anual a $890 (2 meses gratis)** — válvula de escape que reduce churn Y sube tu ARPU de $60 a $74
- Enmarca el aumento con valor/roadmap, sin disculparte en exceso

**Mes 4 — Migración**
- Si hay resistencia fuerte, ofrece un tier degradado a ~$59 con límites de uso (retención antes que pérdida)

**Reglas de aborto (defínelas antes):**
- Churn semanal >2x el baseline por 2 semanas seguidas tras el anuncio → pausa y extiende grandfathering
- Pérdida de base >15% en los primeros 60 días post-migración → vuelve al híbrido

¿Quieres que modele la variante de dos pasos ($75 ahora, $89 en 18 meses) o el impacto de añadir el plan anual al mix?