# Tencent Hy4 — strategy/pricing_strategy

- model_id: `tencent/hy4`
- success: True  | final: 6.73 | quality: 7.5
- latency_total: 127.169s | tokens_per_second: 100.5
- input_tokens: 201 | output_tokens: 12779

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

## Resumen ejecutivo

**Sí, sube a $89 — pero no a toda la base de golpe y acompaña la subida con más presupuesto de adquisición.** Tu economía por usuario es tan buena (margen bruto de $52 → $81/mes) que incluso en el escenario pesimista el **LTV/CAC se mantiene por encima de 4.9x** y el beneficio bruto mensual sube. El riesgo real no es el precio: es **subir el precio y dejar el presupuesto de marketing quieto**, porque el mayor churn + mayor CAC encogen la base a largo plazo.

---

## 1. LTV/CAC actual y cómo cambiaría

⚠️ **Primero una corrección importante:** tu LTV de $840 es **LTV de ingresos**. El ratio que se usa para decisiones (e inversores) es con **margen bruto**, descontando tus $8/usuario.

| Métrica | Hoy ($60) | Sube a $89, *si el churn no cambiara* |
|---|---|---|
| Precio | $60 | $89 (**+48.3%**) |
| Costo/usuario | $8 | $8 |
| **Margen bruto/mes** | **$52** (86.7%) | **$81** (91.0%, **+55.8%**) |
| Churn / vida media | 7% / 14.0 m (exacto 14.29) | 7% / 14.29 m |
| LTV ingresos | $840 (exacto $857) | **$1,271** |
| **LTV margen** | **$728** (exacto $743) | **$1,157** |
| LTV/CAC (ingresos) | **7.0x** | **10.6x** |
| **LTV/CAC (margen)** | **6.1x** (exacto 6.2x) | **9.6x** |
| Payback del CAC | 2.3 meses | **1.5 meses** |

> Con tus 14 meses redondeados el "naive" sería 9.5x margen / 10.4x ingresos.  
> **Lectura:** ya estás sano (benchmark ≥3x, excelente ≥5x). El techo teórico de la subida es ~9.6x. Todo lo que se pierda de ahí vendrá del churn y del CAC, no del margen.

---

## 2. Impacto estimado en churn (benchmarks SaaS)

Referencias de industria (ProfitWell/Paddle, Price Intelligently, SaaS Capital/OpenView):

- **Elasticidad churn↔precio en SMB SaaS: ε ≈ +0.2 a +0.4.** Es decir, un +10% de precio → **+2–4% de churn *relativo*** (no absoluto).
- Subidas **>30% sin grandfathering** generan un **spike de cancelaciones del 5–15% en 60–90 días** ("sticker shock").
- **Grandfathering o rollout gradual reduce ese spike ~60–70%**.
- Churn mediano para SaaS con ARPU $50–$100: **5–7% mensual**. Al subir de ticket, si el valor percibido acompaña, el churn estable tiende a quedarse en ese rango o incluso bajar (clientes más comprometidos).
- Planes anuales reducen el churn efectivo **30–50%**.

Aplicando `Δchurn% = ε × Δprecio%` con Δprecio = **+48.3%**:

| Escenario | ε asumida | Churn resultante | Justificación |
|---|---|---|---|
| Optimista | −0.15 | **6.5%** | Mejor fit: se van los más sensibles, sube la calidad media |
| Realista | +0.40 | **8.5%** | 7% × 1.193 = 8.35% → redondeo + ruido de migración |
| Pesimista | +0.75 | **10.5%** | 9.5% por elasticidad + spike sostenido, sin contar abandono inicial |

**Spike inicial (con grandfather/gradual):** 2% / 6% / 12% de los 200 clientes. Sin grandfather, el pesimista sería 15–18%.

📌 **Contexto competitivo:** $89 está en el **percentil 50** de tu rango ($29–$149), frente al percentil 26 de $60. Sigue habiendo aire para un tier $119–$139. Pero ojo: con competidores en $29 **no elimines el tier de entrada**, o le regalas los clientes price-sensitive.

---

## 3. Tres escenarios modelados

Supuestos comunes: margen $81/mes, presupuesto de adquisición actual = `200 × 7% × $120 = $1,680/mes` (14 clientes nuevos/mes). El CAC sube porque cae la conversión trial→paid: 0% / +15% / +30%.

### A) Unit economics

| | **Optimista** | **Realista** | **Pesimista** |
|---|---|---|---|
| Churn mensual | 6.5% | 8.5% | 10.5% |
| Vida media | 15.4 m | 11.8 m | 9.5 m |
| CAC | $120 | **$138** | $156 |
| LTV margen | $1,246 | **$953** | $771 |
| LTV ingresos | $1,369 | $1,047 | $848 |
| **LTV/CAC (margen)** | **10.4x** | **6.9x** ✅ | **4.9x** ✅ |
| Payback | 1.5 m | **1.7 m** | 1.9 m |
| CAC máx. sostenible @3x | $415 | $318 | $257 |
| Spike inicial | 2% (4) | 6% (12) | 12% (24) |
| Clientes mes 1 | 196 | **188** | 176 |
| MRR mes 1 | $17,444 | **$16,732** | $15,664 |
| **Gross profit mes 1** | $15,876 | **$15,228** | $14,256 |

> Hoy: GP mes 1 = **$10,400**. **Hasta el pesimista gana +37% en el mes 1.**

### B) Estado estacionario (12 meses) — aquí está la trampa

| Escenario | Si dejas S&M en **$1,680** | Si ajustas S&M para **mantener 200 clientes** | Δ GP neto vs hoy ($8,720/mes) |
|---|---|---|---|
| Optimista | 215 clientes · neto **$15,766** | $1,560/mes · neto **$14,640** | **+68% a +81%** |
| Realista | 143 clientes · neto $9,921 | **$2,346/mes** · neto **$13,854** | +14% / **+59%** |
| Pesimista | 103 clientes · neto **$6,627** ❌ | **$3,276/mes** · neto **$12,924** | −24% / **+48%** |

**Insight clave:** con presupuesto congelado, el escenario realista se estabiliza en ~143 clientes y el pesimista **pierde dinero frente a hoy**. Con presupuesto ajustado, **los tres escenarios ganan**, porque el margen extra ($29/cliente) financia de sobra el CAC más alto (payback < 2 meses).

---

## 4. Recomendación con números concretos

✅ **Apruebo $89 para nuevos clientes desde ya.**  
✅ **Para los 200 actuales: grandfather 12 meses + migración voluntaria incentivada.**  
✅ **Sube el presupuesto de adquisición de $1,680 → $2,350/mes** (escenario realista, +$666). Se paga solo: el GP del mes 1 sube +$4,828.

**Plan realista a 90 días (el que usaría para el board):**

| KPI | Hoy | Target | Guardrail (si se rompe) |
|---|---|---|---|
| Churn mensual | 7.0% | **≤8.5%** | >9.5% → lanzar tier $69 y congelar último escalón |
| CAC efectivo | $120 | **≤$138** | >$160 → revisar messaging, no bajar precio |
| LTV/CAC margen | 6.1x | **6.9x** | <4.5x → pausar rollout |
| Payback | 2.3 m | **1.7 m** | — |
| GP neto/mes | $8,720 | **$13,854 (+59%)** | — |
| NRR | ~100% | **≥105%** | — |

**Incluso si sale pesimista:** 4.9x LTV/CAC y **+$4,204/mes netos (+48%)** siempre que lleves S&M a ~$3,300. El precio no es el problema; la inercia en adquisición sí.

**Upside extra:** si empujas plan anual y bajas el churn efectivo de 8.5% → **5.5%**, el LTV margen realista salta a `81/0.055 = $1,473` → **10.7x LTV/CAC** con el mismo CAC de $138.

---

## 5. Estrategia de implementación

**1. Arquitectura de precios (no un solo número)**
| Tier | Precio | Rol |
|---|---|---|
| Lite | **$59** | Contiene a los sensibles al precio (competencia en $29). No lo quites. |
| **Pro** | **$89** | Tu nuevo estándar |
| Advanced | **$139** | Ancla dentro del techo competidor ($149), deja room para futuro $119 |

**2. Segmenta antes de comunicar.** Cruza los 200 clientes por uso (SKUs, integraciones, seats). Los de uso bajo son tu 6–12% de spike: ofréceles **Lite $59** en lugar de dejarlos ir.

**3. Grandfather + migración (recomendado)**
- Actuales: **$60 congelado 12 meses** (o hasta fin de contrato anual). Aviso con **45 días**.
- Incentivo de migración voluntaria: pasan a **anual $948/año (= $79/mes, ~11% dto.)** + 1 mes gratis + onboarding prioritario si lo hacen en 60 días. **Meta: 30–40% migran en 90 días.**
- Nuevos: **$89** + trial 14 días + garantía 30 días atada a valor ("si no te ahorra X horas de conteo, te devolvemos").

**4. Si no quieres grandfather → gradual (reduce el spike ~50%)**
`Mes 1: $69 → Mes 4: $79 → Mes 7: $89`. Nunca el salto directo de $60→$89 sobre la base instalada.

**5. Comunicación "value-first".** No digas "subimos precio". Di: "nuevo motor de reposición automática / alertas de stock / integración X; Pro pasa a $89, tu tarifa actual se respeta 12 meses". El aumento debe venir detrás de una feature, no delante.

**6. Anualidad como palanca de churn.** Objetivo: **40% de la base en anual** en 2 trimestres → churn efectivo ~5.5%, cash por adelantado, CAC recuperado en 1.7 meses igual.

**7. Dashboard de 90 días + kill-switch**
Semanal: logo churn ≠ revenue churn, trial→paid, CAC efectivo, NRR, tickets de soporte (si el costo/user sube de $8 a $9, el LTV realista solo cae a $941 → 6.8x, sigue sano).  
**Regla de corte:** si en el mes 2 el churn >10% **o** el CAC >$160, activas Lite $69, detienes el escalón final y mantienes grandfather otros 6 meses.

---

### En una frase
**Sube a $89, protege a los 200 con grandfather, reinvierte ~$650/mes extra en adquisición y vigila el CAC con la misma lupa que el churn: ahí está el único escenario donde esta decisión te sale mal.**