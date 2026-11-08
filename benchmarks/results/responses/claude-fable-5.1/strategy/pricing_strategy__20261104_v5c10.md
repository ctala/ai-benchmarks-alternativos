# Claude Fable 5.1 — strategy/pricing_strategy

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.78 | quality: 10.0
- latency_total: 74.917s | tokens_per_second: 73.3
- input_tokens: 290 | output_tokens: 5490

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

# Análisis de subida de precio: $60 → $89/mes

## 0. Diagnóstico previo (importante antes de entrar en los números)

Antes de modelar, dos observaciones que cambian la lectura del problema:

| Métrica | Tu valor | Benchmark SaaS SMB | Lectura |
|---|---|---|---|
| Churn mensual | 7% (~58% anual) | 3–5% aceptable, <2% bueno | **Tu problema real** |
| LTV/CAC | 7.0x | 3x es "saludable" | Estás **sub-invirtiendo en adquisición** o el CAC está mal medido |
| Margen bruto | 86.7% | 75–85% | Excelente |
| Payback CAC | 2.3 meses | 12–18 meses | Extremadamente rápido |

Con 7% de churn pierdes **14 clientes/mes** y necesitas gastar $1,680/mes en CAC solo para no decrecer. La subida de precio es correcta, pero no es la palanca más grande que tienes. Lo muestro con números al final.

---

## 1. LTV/CAC actual y proyectado

**Actual (precio $60):**
- Vida media = 1 / 0.07 = 14.3 meses
- LTV (ingreso) = $60 × 14.3 = **$857** (tú usas $840 con 14 meses, misma lógica)
- LTV (margen bruto) = ($60 − $8) × 14.3 = **$743**
- LTV/CAC = 857 / 120 = **7.1x** (5.9x sobre margen bruto)

**A $89 si el churn NO cambiara (escenario teórico):**
- LTV = $89 × 14.3 = **$1,271** (+48%)
- LTV/CAC = **10.6x**

Esto no va a pasar: el churn y el CAC se moverán. Por eso los escenarios.

---

## 2. Impacto estimado en churn (benchmarks)

Referencias de la industria (ProfitWell/Paddle, OpenView, Price Intelligently):

- Subidas de 10–20% en SMB SaaS: pérdida típica de **2–5%** de la base, concentrada en los primeros 1–3 meses.
- Subidas de 30–50% (tu caso, +48%): pérdida de **8–20%** de la base sin grandfathering; **3–8%** con transición bien gestionada.
- Elasticidad de conversión de nuevos clientes: una subida de 48% reduce la conversión del funnel un **15–35%** → tu CAC efectivo sube proporcionalmente (mismo gasto, menos conversiones).
- El churn "estructural" posterior suele volver al nivel base o quedar 0.5–2 puntos por encima, porque los clientes que se quedan son los que más valor perciben (efecto selección: en muchos casos el churn **baja** a medio plazo).

Dato clave a tu favor: estás a $60 en un rango de competidores de $29–$149. A $89 sigues en la zona media; no te sales del mercado.

---

## 3. Tres escenarios (estado estable tras 6 meses)

Supuestos: 200 clientes base, costo $8/usuario, CAC base $120.

| | **Actual** | **Optimista** | **Realista** | **Pesimista** |
|---|---|---|---|---|
| Pérdida inmediata de base | — | 5% (10) | 12% (24) | 20% (40) |
| Clientes restantes | 200 | 190 | 176 | 160 |
| Churn mensual estable | 7.0% | 7.0% | 8.0% | 9.5% |
| Caída conversión nuevos | — | −10% | −20% | −35% |
| CAC efectivo | $120 | $133 | $150 | $185 |
| **MRR** | **$12,000** | **$16,910** | **$15,664** | **$14,240** |
| Δ MRR | — | **+41%** | **+31%** | **+19%** |
| Margen bruto mensual | $10,400 | $15,390 | $14,256 | $12,960 |
| Vida media (meses) | 14.3 | 14.3 | 12.5 | 10.5 |
| LTV (ingreso) | $857 | $1,271 | $1,113 | $935 |
| LTV (margen) | $743 | $1,158 | $1,013 | $851 |
| **LTV/CAC** | **7.1x** | **9.6x** | **7.4x** | **5.1x** |
| Payback CAC | 2.3 m | 1.6 m | 1.9 m | 2.3 m |

**Punto de equilibrio:** el MRR solo cae si pierdes más de **65 clientes (32.5%)**; el margen bruto solo cae si pierdes más de **71 (36%)**. Ningún benchmark razonable te acerca a eso. **Incluso el escenario pesimista mejora el MRR en ~$2,200/mes.**

---

## 4. Recomendación

**Sí, sube el precio. Pero:**

**a) Subir a $89 es correcto para nuevos clientes.** El riesgo asimétrico está a tu favor: ganancia esperada +$3,600/mes (realista) vs. un escenario de pérdida que requeriría perder un tercio de la base.

**b) Para la base existente, ve a $79, no a $89, en el primer salto** (+32% en lugar de +48%). Razón: la pérdida de base por una subida del 30% está en 5–8% vs. 12–20% para una del 48%. Números:

| Base existente a… | Clientes tras churn extra | MRR de la base |
|---|---|---|
| $60 (sin cambio) | 200 | $12,000 |
| $79 (pérdida ~7%) | 186 | $14,694 |
| $89 (pérdida ~12%) | 176 | $15,664 |

La diferencia son ~$970/mes, pero con $79 conservas 10 clientes más que además generan referidos, reviews y datos. Puedes llevar a esa cohorte a $89 en 12 meses.

**c) La palanca más grande es el churn, no el precio.** Compara:

| Acción | LTV resultante |
|---|---|
| Solo subir a $89 (churn 8%) | $1,113 |
| Solo bajar churn a 4% (precio $60) | $1,500 |
| **Ambas: $89 y churn 4%** | **$2,225** |

Bajar churn de 7% a 4% vale más que la subida de precio. Si no has investigado por qué se van (encuesta de cancelación, análisis de uso en primeros 30 días, onboarding), hazlo en paralelo.

**d) Con LTV/CAC de 7x, estás dejando crecimiento sobre la mesa.** Un ratio saludable es 3–4x; puedes permitirte un CAC de $250–300 y seguir siendo rentable. Si hay canales que hoy descartas por "caros", reconsidéralos.

---

## 5. Estrategia de implementación

**Fase 1 — Nuevos clientes (semana 1):**
- Cambia el pricing público a una estructura de 3 tiers para anclar precio y reducir fricción:
  - **Starter $49** (límites de SKUs/usuarios/almacenes) — captura al segmento sensible al precio que hoy mira a competidores de $29
  - **Pro $89** — tu plan actual, el "recomendado"
  - **Business $149** — multi-almacén, API, soporte prioritario
- Lanza **plan anual a $890/año** (2 meses gratis). El prepago anual reduce churn estructuralmente y mejora caja.
- Si tienes >20 signups/mes, A/B $79 vs $89 durante 60 días. Con menos volumen no tendrás significancia; ve directo a $89.

**Fase 2 — Base existente (meses 2–4):**
- **Aviso con 60 días de antelación**, email personal del fundador, no un banner. Explica qué han ganado desde que entraron (features, soporte) y qué viene.
- **Grandfathering parcial:** mantienes $60 hasta el día X; después pasan a $79 ("precio legacy", 11% bajo el público). Esto convierte la subida en un beneficio relativo.
- **Oferta de lock-in:** quien pague anual antes de la fecha, bloquea $60/mes ($720/año) por 12 meses. Esto te trae caja, baja churn y reduce la fricción emocional del cambio. Espera que un 20–30% la tome.
- Para los 10–15 clientes de mayor valor/más antiguos, llamada directa.

**Fase 3 — Seguimiento (meses 2–6):**
- Monitorea semanalmente: cancelaciones, tickets de soporte mencionando precio, downgrades a Starter, NPS.
- Umbrales de alarma: si la pérdida de base supera 15% en 90 días, pausa la migración de la cohorte legacy y revisa el mensaje/valor, no el precio.
- Acompaña la subida con **una mejora visible** lanzada en la misma ventana (aunque sea pequeña). El cerebro acepta mejor "pagas más por más" que "pagas más por lo mismo".

**Fase 4 — Mes 12:**
- Elimina el precio legacy ($79 → $89) con el mismo protocolo de 60 días.

---

## Resumen en una línea

Sube a $89 para nuevos ahora y a $79 para existentes con 60 días de aviso y opción de bloqueo anual; incluso en el peor caso ganas ~$2k/mes de MRR, pero el verdadero multiplicador es llevar el churn de 7% a 4%, que por sí solo vale más que toda la subida de precio.