---
title: "Insights del benchmark — qué dice la data antes de elegir un modelo en producción"
fecha: "2026-05-03"
version_benchmark: "v2.6.0"
modelos_analizados: 72
modelos_catalogados: 113
runs_minimas_por_modelo: 50
tests_por_modelo: "91 single-turn + 12 agent_long_horizon + 45 niah_es_lite + 60 niah_es"
pilares: ["Razonamiento", "Coding", "Contenido/Marketing", "Agentes/Operaciones", "Long-context retrieval (NIAH-ES)"]
juez_llm: "Phi-4 (Microsoft, 14B, MIT) via Ollama local"
audiencia: "Emprendedores latinoamericanos que toman decisiones de producción HOY"
fuente_datos: "docs/data/models.json + benchmarks/results/*.json"
pesos_score: {quality: 0.50, cost: 0.20, tool_calling: 0.15, speed: 0.075, latency: 0.075}
total_runs: "9,500+"
---

## 🆕 Update v2.6.0 — Mayo 2026: NIAH ext + GPT-5.5 completo + DeepSeek V4 family + datasheets

Tres avances grandes desde v2.5.2 (1 mayo):

### Lotes mayo (3 mayo, ~9 horas wall-clock)

| Lote | Tests | Modelos | Resultado |
|---|---|---|---|
| **GPT-5.5 completar** | 12 ALH + 45 NIAH-lite = 57 | 1 | ✅ 57/57 OK |
| **NIAH-ES extension lite** | 9 modelos × 45 = 405 | 9 | ✅ 405/405 OK |
| **DeepSeek V4 family** | 3 variantes × 57 = 171 | 3 | V4 Pro Cloud 55/57, V4 Flash Cloud 57/57, V4 Pro NIM 0/7 ❌ |
| **DeepSeek V4 Pro OpenRouter** | 12 ALH + 45 NIAH-lite | 1 | ✅ 57/57 OK |

### Top 10 score compuesto v2.6.0

| # | Modelo | Final | Quality | Cambio vs abril |
|---|---|---|---|---|
| 1 | Llama 4 Scout 17B (Groq) | 7.69 | 7.70 | = (era 8.11, baja por NIAH integrado) |
| 2 | Llama 3.1 8B Instant (Groq) | 7.67 | 7.33 | = |
| 3 | **Devstral Small** | **7.52** | 7.89 | ⬆ de #10 a #3 (NIAH alto sube ranking) |
| 4 | Mistral Small 4 | 7.51 | 7.88 | ⬆ |
| 5 | GPT-OSS 20B (Groq) | 7.47 | 7.10 | ⬇ -1 |
| 6 | **MiMo V2-Omni Xiaomi sub** | **7.46** | 7.27 | ⬆ ingresa al top 10 |
| 7 | MiMo V2.5 (Xiaomi sub) | 7.45 | 7.63 | = |
| 8 | Gemini 3.1 Flash Lite | 7.44 | 7.82 | ⬇ |
| 9 | Nemotron 3 Nano 30B | 7.43 | 7.79 | ⬆ |
| 10 | MiMo V2.5-Pro (Xiaomi sub) | 7.42 | 7.65 | ⬆ |

**Cambio metodológico crítico**: el ranking compuesto ahora **integra NIAH-ES**. Modelos con NIAH-ES corrido tienen score promedio menor (NIAH 5-7 vs single-turn 7-8). NO significa regresión — significa nueva dimensión medida. Devstral Small sube porque su NIAH-ES (7.25) es el mejor, mientras Llama 4 Scout cae de 8.11 a 7.69 absoluto pero mantiene #1.

### Hallazgo crítico mayo: DeepSeek V4 Pro NIM NO funciona en producción

Cascada 504 reproducible **2 veces** (abril 28 + mayo 3). NIM gateway no maneja modelo gigante con prompts largos. Para producción con DeepSeek V4 Pro: usar **OpenRouter pagado** ($1.74/$3.48 per M) o **Ollama Cloud sub** ($30/mes, 97% éxito). **Descartado** NIM Pro como opción productiva.

### MiMo Xiaomi sub family — confirmación como mejor C/B en español

4 modelos MiMo en top 10 (V2-Omni, V2.5, V2.5-Pro, V2-Flash). Suscripción $14/mes da acceso a 4 modelos competentes con español neutro fuerte. **Mejor opción para emprendedores LATAM con presupuesto fijo predecible**.

### NIAH-ES extension — 21 modelos cubiertos (vs 8 abril)

Top 5 NIAH-ES con 21 modelos:

| # | Modelo | Score |
|---|---|---|
| 1 | Devstral Small | **7.25** |
| 2 | Mistral Small 4 | 7.06 |
| 3 | Llama 4 Scout 17B Groq | 6.89 |
| 4 | Llama 3.1 8B Instant Groq | 6.66 |
| 5 | Gemini 3.1 Flash Lite | 6.51 |
| ... | ... | ... |
| último | Claude Opus 4.7 | **4.98** ⬇ |

**Devstral Small mantiene #1 NIAH-ES con cobertura ampliada** — confirmación robusta del hallazgo.

### Datasheets mensuales (convención nueva desde mayo 2026)

- [DATASHEET_2026-04.md](DATASHEET_2026-04.md) — snapshot retroactivo abril
- [DATASHEET_2026-05.md](DATASHEET_2026-05.md) — estado mayo + comparación vs abril
- Convención: cada 1ro de mes datasheet con evolución del benchmark (data, hallazgos, regresiones, modelos agregados)

---

## 🆕 Update v2.5.1 — NIAH-ES v2 full grid (5 needles × 60 tests por modelo)

Lote v2 corrido sobre 8 modelos × 60 tests (5 needles × 4 ctx × 3 pos) = **480 runs en 43 min**, costo ~$50 OpenRouter. La data más robusta del benchmark hasta ahora.

### Ranking NIAH-ES v2 (consolidado)

| # | Modelo | Avg | 4K | 16K | 64K | 256K | Cobertura |
|---|---|---|---|---|---|---|---|
| 1 | **Devstral Small** | **7.25** ⭐ | 7.80 | 7.40 | 6.56 | — | 45/60 |
| 2 | Mistral Small 4 | **7.06** | 7.59 | 7.15 | 6.44 | — | 45/60 |
| 3 | Llama 4 Scout 17B (Groq) | 6.89 | 7.70 | 6.96 | 6.01 | — | 45/60 |
| 4 | Llama 3.3 70B (Groq) | 6.26 | 7.05 | 6.30 | 5.43 | — | 45/60 |
| 5 | Gemini 3.1 Pro | 5.96 | 6.45 | 6.18 | 5.84 | 5.37 | **60/60** ✅ |
| 6 | DeepSeek V4 Flash (NIM gratis) | 5.92 | 6.32 | 5.93 | 5.49 | — | 45/60 |
| 7 | GPT-4.1 | 5.86 | 6.63 | 6.22 | 5.67 | 4.91 | **60/60** ✅ |
| 8 | **Claude Opus 4.7** | **4.98** ⬇ | 5.44 | 5.09 | 4.85 | 4.53 | **60/60** ✅ |

Confirma v1: **Devstral Small es #1 y Opus 4.7 es #último** — patrón robusto con 5 needles.

### ⚠️ Corrección importante de v1: NO hay lost-in-the-middle severo

El piloto v1 (12 tests, 1 needle por slot) reportó "Opus 4.7 cae -3.0 puntos al 50% del 4K (6.0 → 3.1 → 6.3)". **Eso fue ARTEFACTO de N=1**. Con 5 needles promediados (v2), los scores son MUY parecidos entre las 3 posiciones:

| Modelo | 4K-25% | 4K-50% | 4K-75% | Delta máx |
|---|---|---|---|---|
| Claude Opus 4.7 | 5.38 | 5.41 | 5.53 | 0.15 ⬅️ NO drop |
| Devstral Small | 7.81 | 7.84 | 7.75 | 0.09 |
| Mistral Small 4 | 7.54 | 7.54 | 7.69 | 0.15 |
| Llama 3.3 70B | 7.00 | 7.06 | 7.08 | 0.08 |
| Llama 4 Scout | 7.63 | 7.77 | 7.71 | 0.14 |
| GPT-4.1 | 6.51 | 6.72 | 6.67 | 0.21 |
| Gemini 3.1 Pro | 6.47 | 6.43 | 6.44 | 0.04 |
| DeepSeek V4 Flash | 6.24 | 6.39 | 6.33 | 0.15 |

**Lecciones metodológicas**:
1. **N=1 puede generar patrones fantasma**. Lost-in-the-middle reportado en literatura (Liu et al. 2023) puede ser real — pero **no en español neutro con estos needles, en estos modelos, con N=5**.
2. **El needle `discount_code` específicamente sufre al 50%**: en v1 ese era el único needle a esa posición. Necesitaría inspección cualitativa para entender por qué.
3. **Para hallazgos publicables: N≥5 es mínimo**. v1 sirvió de validación de la suite, no de hallazgo definitivo.

### Lo que SÍ es robusto

#### 1. Devstral Small ($0.10/$0.30) supera a Opus 4.7 ($45/M) en NIAH

Con 60 tests cada uno:
- Devstral Small: 7.25 avg
- Claude Opus 4.7: 4.98 avg
- **Delta: +2.27 puntos a favor de Devstral, a 1/450 del costo**

Para tareas de retrieval con context <128K, Devstral Small es mejor opción que Opus 4.7.

#### 2. Gemini 3.1 Pro es el más estable a 256K

- Gemini 3.1 Pro: 5.37 avg en 256K (5.30 / 5.39 / 5.40)
- GPT-4.1: 4.91 avg (4.96 / 4.88 / 4.88)
- Claude Opus 4.7: 4.53 avg (4.46 / 4.52 / 4.61)

**Gemini 3.1 Pro gana cuando el contexto es >128K**. Es la mejor opción premium para long-context retrieval.

#### 3. "1M context declarado" ≠ "retrieval efectivo a 256K"

Solo 3/8 modelos procesan 256K sin error 400 (Opus, GPT-4.1, Gemini 3.1 Pro). Y los 3 degradan a score 4.5-5.4 (vs 6-8 a context chico).

**Modelos con context <256K efectivo en su provider** (todos cap a 128K):
- Devstral Small (declared 256K → OpenRouter cap)
- Llama 4 Scout 17B (declared 10M → Groq preview cap)
- Mistral Small 4 (declared 128K → ✓ correcto)
- DeepSeek V4 Flash (declared 1M → NIM cap)
- Llama 3.3 70B (declared 131K → ✓ correcto)

#### 4. Claude Opus 4.7 es el peor en NIAH-ES (sigue como hipótesis)

Opus 4.7 en 60 tests sigue **último** con 4.98 promedio. Worse que Llama 3.3 70B Groq (6.26) que es 75x más barato. Hipótesis abierta: Opus parafrasea en lugar de extraer texto exacto, lo que no matchea con regex/keywords scoring.

**Acción pendiente**: inspección manual de 5-10 respuestas Opus 4.7 en `benchmarks/results/responses/20260430_200512/` para confirmar la hipótesis.

### Cross-reference con literatura NIAH inglesa (NIAH_CROSSREF.md)

Triangulación con scores oficiales reportados por los proveedores. Hallazgos de la cross-ref (data robusta de papers Gemini 1.5/2.5/3, DeepSeek V4, Llama 3.3/4, Mistral, Anthropic system cards, OpenAI announcement, Greg Kamradt leaderboard):

#### 1. Ranking inglés ≠ ranking NIAH-ES (sorpresa metodológica)

En literatura inglesa los frontier reportan retrieval casi perfecto:
- Gemini 1.5 Pro: 99.7% hasta 1M (single-needle)
- GPT-4.1: 100% all positions all lengths (single-needle, OpenAI announcement)
- Claude 3 Opus: >99% NIAH single-needle 200K

**En NIAH-ES los mismos modelos quedan mid-table** (5.86–5.96 / 10). **Devstral Small (7.25) y Mistral Small 4 (7.06) lideran** — coherente con su entrenamiento multilingüe europeo más fuerte que los frontier US-centric.

**Implicación**: el "100% en NIAH inglés" NO se traduce a "100% en NIAH-ES". El idioma del prompt + needle es factor real en retrieval, no solo el context window.

#### 2. Opus 4.7 último es CONSISTENTE con literatura reciente

Anthropic mismo reporta degradación en variantes multi-needle:
- Claude Opus 4.6: 76% MRCR v2 8-needle 1M
- Claude Sonnet 4.5: 18.5% MRCR v2 8-needle 1M (drop dramático)
- Opus 4.7: regresión adicional según trackers terceros

La familia Claude prioriza razonamiento sobre retrieval puro. Nuestro hallazgo (Opus 4.7 = 4.98 en NIAH-ES) **valida** esa observación de literatura.

#### 3. Llama 4 Scout > Llama 3.3 70B respeta ranking oficial Meta

- Meta: Llama 4 Scout 98% retrieval @10M, Llama 3.3 70B 97.5% multi-needle @128K
- Nuestro: Llama 4 Scout 6.89 > Llama 3.3 70B 6.26
- ✅ El delta cualitativo se preserva (aunque magnitud distinta por idioma)

#### 4. Devstral / Mistral Small son APORTE ÚNICO

Mistral Small NO publica score numérico NIAH oficial (Inspect Evals UK BEIS lo evalúa cualitativamente sin %). Devstral tampoco. **NIAH-ES es el primer benchmark público con número concreto para estos modelos.**

#### 5. Limitaciones declaradas

- Idioma: 100% literatura es inglés
- Métrica: binaria oficial vs 0-10 nuestra
- Variantes: single-needle vs MRCR multi-needle mezcladas
- Generaciones: no medimos Gemini 1.5/2.5 ni Claude 3 (nuestros mediciones son 3.1/4.7 actuales)

Ver `NIAH_CROSSREF.md` para tabla completa con 12 fuentes oficiales citadas.

### v3 con context 1M (5h elapsed, 1 mayo) — HALLAZGO BRUTAL

Lote v3 corrido con 4 modelos × 15 tests (5 needles × 1 ctx 1M × 3 pos) = 60 runs.

**Solo 1 de 4 modelos procesa 1M tokens efectivamente**:

| Modelo | Declared | Tests OK | Score 1M | Causa |
|---|---|---|---|---|
| **GPT-4.1** | 1M | **15/15** ✅ | **4.91** | Único que cumple la promesa |
| Llama 4 Scout 17B Groq | 10M | 0/15 ❌ | — | Groq preview cap a 131K |
| DeepSeek V4 Flash NIM | 1M | 0/15 ❌ | — | NIM cap (~128K efectivo) |
| Gemini 3.1 Pro | 1M | 0/15 ❌ | — | OpenRouter cap |

**3 de 4 proveedores capan el context window declarado por el modelo**. El "1M" o "10M" del marketing solo aplica si:
- El modelo realmente tiene capacidad arquitectural (sí, todos)
- **Y** el provider que usás expone la capacidad completa (no, solo OpenAI directo / OpenRouter para GPT-4.1)

**Implicación crítica**: para tasks que requieren context >256K en producción con esos modelos via los providers que medimos, la mayoría de modelos "1M" son falsa promesa. **GPT-4.1 vía OpenAI directo o OpenRouter es la única opción confirmada.**

**GPT-4.1 a 1M tokens**: score 4.91 promedio, idéntico a su 256K (4.91). NO degrada al duplicar el context — esto SÍ valida el effective 1M de OpenAI.

**Pendiente**: probar Gemini 3.1 Pro vía Google directo (no OpenRouter) y DeepSeek V4 Pro vía Ollama Cloud para confirmar si el cap es del provider intermediario, no del modelo. ETA: 1 día.

### Próximo NIAH (futuro)

- [x] Piloto v1 (12 tests/modelo) — validó la suite
- [x] v2 full grid (60 tests/modelo) — datos robustos
- [x] Cross-ref con literatura NIAH inglesa (NIAH_CROSSREF.md)
- [x] **v3 con context 1M** ← este update (60 runs, GPT-4.1 único que procesa)
- [ ] v3b: Gemini 3.1 Pro vía Google directo (validar si el cap es OpenRouter o Google)
- [ ] DeepSeek V4 Pro vía Ollama Cloud (validar cap NIM vs Ollama)
- [ ] Inspección cualitativa Opus 4.7: paráfrasis vs extraction exacta

---

## 🆕 Update v2.5.0 — NIAH-ES piloto v1 (datos preliminares, ver v2 arriba para resultados consolidados)

Suite NIAH-ES (Needle-in-a-Haystack en español neutro) corrida sobre 8 modelos × 12 tests = 96 runs en 9 minutos wall-clock. Costo total: ~$8 OpenRouter. Ver `NIAH_ES_DESIGN.md` para diseño completo.

### Ranking NIAH-ES — promedio global (4K-256K cuando aplica)

| # | Modelo | Score | 4K | 16K | 64K | 256K | Errores |
|---|---|---|---|---|---|---|---|
| 1 | **Devstral Small** | **7.17** ⭐ | 7.7 | 7.3 | 6.5 | — | 3 (256K falla) |
| 2 | **Llama 4 Scout 17B (Groq preview)** | **6.99** | 7.9 | 7.0 | 6.1 | — | 3 (256K falla, Groq cap) |
| 3 | Mistral Small 4 | 6.88 | 7.2 | 7.3 | 6.1 | — | 3 (256K falla) |
| 4 | Llama 3.3 70B (Groq) | 6.30 | 7.0 | 6.4 | 5.5 | — | 3 (256K falla) |
| 5 | DeepSeek V4 Flash (NIM gratis) | 5.97 | 6.7 | 6.0 | 5.3 | — | 3 (NIM cap) |
| 6 | Gemini 3.1 Pro | 5.92 | 6.3 | 6.3 | 5.8 | 5.3 | 0 ✅ |
| 7 | GPT-4.1 | 5.73 | 6.4 | 6.3 | 5.4 | 4.8 | 0 ✅ |
| 8 | **Claude Opus 4.7** | **4.81** ⬇ | 5.1 | 4.6 | 5.2 | 4.2 | 0 ✅ |

### 🚨 Hallazgo sorpresa: Claude Opus 4.7 es ÚLTIMO en NIAH-ES

Opus 4.7 (top en HumanEval 88.4, MMLU 90+, SWE-bench 87.6, generalmente considerado SOTA) sale **último** en retrieval de needle en español. Score promedio 4.81 vs Devstral Small 7.17 (que es 75x más barato).

**Hipótesis posibles** (a validar):
1. **Opus refusa a "extraer info textual"** y siempre elabora respuesta tipo "según el documento, parece que..." — el regex no matchea cuando el modelo parafrasea en lugar de copiar exacto
2. **Opus es WEAK específicamente en NIAH chiquito** — su 5.1 a 4K es PEOR que cualquier otro modelo en 4K
3. Posible **bias de Anthropic safety**: needle con "API key" puede triggerar safety y devolver "no debería compartir credenciales"

**Acción**: revisar respuestas crudas de Opus 4.7 en `benchmarks/results/responses/20260430_193058/`.

### 💀 Lost-in-the-middle CONFIRMADO en español

Patrón documentado en literatura (Liu et al. 2023 sobre GPT-3.5/4) — **se replica en español**.

Score promedio (5 needles) por posición dentro del haystack:

| Modelo | 4K-25% | 4K-50% | 4K-75% | Drop al medio |
|---|---|---|---|---|
| **Claude Opus 4.7** | 6.0 | **3.1** | 6.3 | **-3.0 ⚠️** (severo) |
| DeepSeek V4 Flash | 7.0 | 6.2 | 6.8 | -0.7 |
| Devstral Small | 7.9 | 7.4 | 7.9 | -0.5 (más robusto) |
| GPT-4.1 | 6.5 | 5.7 | 6.9 | -1.0 |
| Gemini 3.1 Pro | 6.5 | 5.8 | 6.6 | -0.8 |
| Llama 3.3 70B (Groq) | 7.2 | 6.3 | 7.5 | -1.0 |
| Llama 4 Scout (Groq) | 8.0 | 7.7 | 7.9 | -0.2 (mejor) |
| Mistral Small 4 | 7.6 | 6.5 | 7.6 | -1.1 |

**Hallazgos del lost-in-the-middle**:

1. **Opus 4.7 tiene drop de -3.0 puntos al medio del 4K**. Cualquier info crítica que pongas al medio del prompt, Opus la pierde con probabilidad alta.
2. **Devstral Small (-0.5) y Llama 4 Scout (-0.2) son los más robustos** — extraen info al medio casi tan bien como en bordes.
3. **El patrón se INVIERTE en 64K**: muchos modelos sacan MEJOR en 50% que en 25%. Hipótesis: en haystacks grandes, el modelo sub-divide la atención y el 25% queda en un "valle" no atendido.

### 256K — solo Opus 4.7 + GPT-4.1 + Gemini 3.1 Pro lo procesan

| Modelo | 256K-25% | 256K-50% | 256K-75% | Avg |
|---|---|---|---|---|
| **Gemini 3.1 Pro** | 5.66 | 5.31 | 4.82 | **5.26** (más estable) |
| GPT-4.1 | 4.93 | 5.13 | 4.50 | 4.85 |
| Claude Opus 4.7 | **2.64** | 5.28 | 4.85 | 4.26 (25% catastrófico) |

**Modelos que NO procesan 256K** (error 400 esperado):
- Devstral Small, Llama 3.3 70B Groq, Llama 4 Scout Groq (preview cap), Mistral Small 4 OpenRouter, DeepSeek V4 Flash NIM (todos cap a 128K efectivo)

**Hallazgo importante**: el "1M context" o "10M context" declarado por providers (Llama 4 Scout, DeepSeek V4 Flash, GPT-4.1, Gemini 3.1 Pro) **NO se traduce a "1M de retrieval efectivo"**. Solo 3 modelos procesan 256K sin error en sus implementaciones reales (Opus, GPT-4.1, Gemini Pro), y de esos solo Gemini 3.1 Pro mantiene score >5.0 en las 3 posiciones.

### Implicación para producción

**Si tu task requiere context >128K**:
- Solo Gemini 3.1 Pro, GPT-4.1, Claude Opus 4.7 lo procesan
- Pero todos degradan a score ~4-5 (vs ~7 a context chico)
- Costo: Opus 4.7 (~$45/M tokens input) y GPT-4.1 ($2.5/M) son las opciones — Gemini Pro ($2/M) gana en relación calidad-precio

**Si tu task tiene context <64K** (mayoría de casos producción):
- **Devstral Small ($0.10/$0.30)** es el mejor opción C/B — supera a Opus 4.7 a 1/450 del costo
- **Llama 4 Scout 17B Groq** segundo en performance + 280 tok/s = mejor latencia
- **DeepSeek V4 Flash NIM gratis** competitivo si rate limit 40 RPM alcanza

**Si necesitás info crítica al medio del prompt**:
- Devstral Small y Llama 4 Scout son los más robustos a lost-in-the-middle
- **Evitá Opus 4.7 con contexto 4K-16K** — drop de 3 puntos al 50% es severo
- Para mitigar: poné info crítica en bordes (primeras o últimas 25% del prompt)

### Próximos pasos NIAH-ES (ROADMAP)

- [x] Suite implementada + corpus + scoring + script regenerador (commit b74fa84)
- [x] Smoke test Mistral Small 4
- [x] Piloto v1 con 8 modelos (este update)
- [ ] **v2 con 5 needles activos**: 60 tests por modelo (5 needles × 4 ctx × 3 pos), $200-300
- [ ] **v3 con context 1M** en modelos que lo declaran (Gemini 3.x Pro, GPT-4.1, Llama 4 Scout, DeepSeek V4)
- [ ] **Cross-ref con paper Gemini 1.5 NIAH inglés** para validar metodología
- [ ] **Investigar bottom de Opus 4.7**: ¿son refusals, paráfrasis, o falla real de retrieval? Inspección manual de 5 respuestas.

---

## 🆕 Update v2.4.2 — Ranking agent_long_horizon completo + scoring v2

### Nueva fórmula de score (rebalanced 30 abril)

Pesos default ajustados para reflejar mejor las decisiones reales de un emprendedor LATAM:

| Componente | Peso v2.3 (anterior) | Peso v2.4.2 (nuevo) | Por qué cambió |
|---|---|---|---|
| Quality | 35% | **50%** | Es el factor #1 en decisiones reales |
| Cost | 15% | **20%** | Presupuesto importa para emprendedor LATAM |
| Tool calling | 25% | **15%** | Estaba inflado: 83/91 tests reciben 7.0 default (no usan tools) |
| Speed | 5% | **7.5%** | Pipelines async pero la velocidad afecta UX agente |
| Latency | 5% | **7.5%** | Idem |
| Availability | 15% (hardcoded a 7.0) | **eliminado** | No discriminaba |

Curva de cost también mejorada: de buckets discretos (cliffs de 2 puntos en $0.0001 de diferencia) a curva logarítmica suave: $0.001/call → 8.0, $0.01 → 5.0, $0.10 → 2.0, $1.00 → 0.

Ver `THINKING_EXPLAINED.md` y `BENCHMARKS_EXTERNOS.md` para contexto adicional.

### Nuevo Top 10 score compuesto (v2.4.2)

| # | Modelo | Final | Quality | Cost | Provider |
|---|---|---|---|---|---|
| 1 | Llama 4 Scout 17B | 8.11 | 7.93 | 8.83 | Groq direct |
| 2 | Llama 3.1 8B Instant | 8.11 | 7.61 | 8.98 | Groq direct |
| 3 | Llama 3.3 70B | 7.86 | 8.01 | 8.17 | Groq direct |
| 4 | GPT-OSS 20B | 7.84 | 7.51 | 8.80 | Groq direct |
| 5 | Mistral Small 4 | 7.81 | 8.08 | 8.30 | OpenRouter |
| 6 | Gemini 3.1 Flash Lite | 7.73 | 8.01 | 7.85 | OpenRouter |
| 7 | GPT-OSS 120B Cloud | 7.69 | 7.81 | 10.00 | Ollama Cloud |
| 8 | Grok 4.1 Fast | 7.62 | 8.13 | 8.18 | OpenRouter |
| 9 | MiMo V2.5 (Xiaomi) | 7.62 | 7.68 | 8.84 | Xiaomi direct |
| 10 | Devstral Small | 7.61 | 8.03 | 7.63 | OpenRouter |

### Why Opus 4.7 doesn't top our benchmark — y por qué eso valida la metodología

El benchmark v2.4.1 puso a Claude Opus 4.7 en posición ~#30 (final 7.16). Pregunta legítima: ¿está bien si Opus es top en HumanEval (88.4), MMLU (90+), GPQA Diamond (94+), SWE-bench Verified (87)?

Datos cuantitativos descomponen la respuesta:

| Métrica | Opus 4.7 | Llama 3.3 70B (Groq) | Lectura |
|---|---|---|---|
| Score automático (formato + sustancia) | 7.33 | 7.43 | Empate — Opus marginal abajo en formato/criterios |
| Score juez Phi-4 | **4.22** ⬆ | 4.00 | Opus MEJOR para Phi-4 (descarta sesgo del juez) |
| Output tokens promedio (verbosity) | 980 | 991 | Idéntico — Opus NO es más verboso |
| **Quality** (combinado, 50% del final) | 8.08 | 8.01 | Opus marginal arriba |
| **Cost score** (20% del final) | 6.67 | 8.17 | Llama 1.5 puntos arriba |
| **Speed score** (7.5%) | ~3 | ~9 | Llama 6 puntos arriba |
| **Latency score** (7.5%) | ~5 | ~7 | Llama arriba |
| Score final | **7.16** | **7.86** | Llama gana por costo + speed |

**Conclusión metodológica**:

1. **No es sesgo del juez** — Phi-4 (Microsoft, neutral) califica a Opus por encima de Llama. Si hubiera sesgo anti-Anthropic, Opus saldría peor en quality automática.
2. **No es problema de API** — los componentes raw (quality, output tokens) están en el rango esperado.
3. **Es la fórmula** — el score compuesto pondera costo y velocidad. Opus 4.7 es **40-100x más caro** que las alternativas top y **5-10x más lento** (50 tok/s vs 270 tok/s en Groq). Para un emprendedor con $500/mes de presupuesto, pagar 40x más por marginal +0.07 puntos de quality NO es decisión racional.
4. **Esto valida el benchmark** — si tu decisión de producción solo dependiera de quality, los benchmarks académicos (HumanEval/MMLU) ya cubren esa pregunta. Nuestro aporte es medir quality + costo + velocidad + tool calling juntos, en español neutro, simulando casos reales de un emprendedor.

Si solo quieres ranking por quality pura:

| Top quality (sin pesar costo/speed) | Score |
|---|---|
| Gemma 4 31B | 8.19 |
| Grok 4.1 Fast | 8.13 |
| Gemini 3.1 Flash Lite | 8.11 |
| Qwen 3-Next 80B Instruct (NIM) | 8.11 |
| Mistral Small 4 | 8.08 |
| **Claude Opus 4.7** | **8.08** |
| Hermes 4 70B | 8.04 |
| Claude Opus 4.6 | 8.04 |
| Devstral Small | 8.03 |
| Llama 3.3 70B (Groq) | 8.01 |

En quality pura Opus es **top 6**, indistinguible de Llama 3.3 70B y Devstral Small. Es decir: en un test de quality solo, Opus 4.7 es excelente. **Para producción, costo y velocidad cambian la decisión**.

### Ranking inter-modelo agent_long_horizon (multi-turn 8+ turnos)

Suite agéntica con 12 tests multi-turno corridos en **38 modelos**. Top 10 inter-modelo:

| # | Modelo | Score | Tests | Notas |
|---|---|---|---|---|
| 1 | **GPT-OSS 120B (Ollama Cloud)** | **8.15** | 12 | Apache 2.0, gratis con sub Ollama Cloud |
| 2 | Llama 4 Scout 17B (Groq) | 7.86 | 12 | Apache 2.0 |
| 3 | Llama 3.1 8B Instant (Groq) | 7.85 | 12 | Llama 3 small + ultra rápido |
| 4 | Devstral Small | 7.77 | 12 | Apache 2.0 |
| 5 | MiMo V2-Omni (Xiaomi direct) | 7.75 | 12 | Multimodal |
| 6 | GPT-OSS 20B (Groq) | 7.67 | 9/12 | (3 errores 400 Groq + tools) |
| 7 | MiMo V2.5 (Xiaomi) | 7.65 | 12 | Sub $14/mes |
| 8 | Llama 3.3 70B (Groq) | 7.60 | 27 | Validado en múltiples runs |
| 9 | MiMo V2-Pro (Xiaomi direct) | 7.47 | 12 | |
| 10 | Mistral Small 4 | 7.41 | 12 | Apache 2.0 |

**Bottom (modelos top single-turn que pierden agéntica)**:

| # | Modelo | Score | Single-turn ref | Delta |
|---|---|---|---|---|
| 41 | Claude Opus 4.7 (thinking) | 6.33 | 7.16 | -0.83 ⬇ |
| 42 | Kimi K2.6 (thinking) | 6.32 | ~6.5 | -0.18 ⬇ |
| 43 | Hermes 4 405B (thinking) | 6.30 | ~6.5 | -0.20 ⬇ |
| 44 | Qwen 3.5 397B (NIM) | 6.14 | 7.02 | -0.88 ⬇ (cobertura parcial 6/12 OK por 429) |

**Hallazgo crítico para tu pipeline**:

- **Modelos hybrid forzados a thinking EMPEORAN multi-turn agéntico** en 8/9 casos (Hermes 4 70B/405B, Opus 4.7, Sonnet 4.6, Haiku 4.5, Kimi K2.6, Gemini 3.1 Pro, Gemini 2.5 Flash). Excepción: Kimi K2.5 que sube +0.73.
- Hipótesis: el modelo "razona demasiado" en cada turn, pierde foco/contexto del usuario, y se desvía del objetivo en multi-turn.
- **Implicación**: para OpenClaw/Hermes/N8N, **NO actives thinking por default**. Solo activá si tu task específica requiere razonamiento puro (matemática, lógica formal). Para conversación, customer support, content marketing → thinking puede empeorar.

### Hipótesis sobre el desempeño de Opus 4.7 (en investigación)

Aunque la fórmula del score compuesto explica gran parte de la diferencia (Opus 4.7 saca quality 8.08 = top 6, pero costo 40-100x más caro y velocidad 5-10x más lenta lo bajan), **el componente quality automático (7.33) es marginalmente menor** que Llama 3.3 70B (7.43). Eso requiere explicación adicional. Análisis cualitativo de respuestas reales sugiere las siguientes hipótesis (a validar con más data):

#### Tests donde Llama 3.3 70B Groq vence a Opus 4.7 (top 5 deltas)

| Test | Δ score | Hipótesis |
|---|---|---|
| `tool_calling/multi_tool_sequential` | +1.9 | Opus over-thinking en cadenas simples — agrega contexto/justificación entre tool calls |
| `agent_capabilities/skill_execution_complex` | +1.3 | Opus expande con disclaimers; Llama ejecuta directo |
| `multi_turn/content_iteration` | +1.1 | Opus reescribe TODO en cada iter; Llama hace deltas |
| `translation/detect_language_issues` | +1.0 | Opus explica el problema; Llama lo arregla |
| `news_seo_writing/news_json_output_strict` | +1.0 | Opus genera HTML 1.8K tokens en cada artículo (ver ejemplo abajo) |

#### Tests donde Opus vence a Llama (las pocas donde gana)

| Test | Δ score | Hipótesis |
|---|---|---|
| `tool_calling/no_tool_needed` | -2.3 | **Opus es mejor en JUDGMENT — sabe cuándo NO usar tool**. Llama llama tools innecesarios |
| `string_precision/write_config_file` | -1.4 | Opus precisión exacta de strings/configuración técnica |
| `orchestration/error_recovery` | -0.5 | Opus mejor para razonar sobre fallas |

#### Hipótesis 1 — Opus es ELABORADAMENTE verboso (no solo largo)

Output tokens promedio Opus vs Llama: 980 vs 991 (idéntico en agregado). PERO el contenido difiere: en `news_json_output_strict`, el campo `Contenido_HTML` de Opus tiene 8 sub-secciones con párrafos descriptivos largos (judge_score 2.6/5), mientras Llama produce 4-5 sub-secciones más compactas (judge_score esperado >3.5).

**Ejemplo real** (Opus 4.6 en news_json_output_strict, judge=2.6):
> "Este logro es particularmente notable porque se trata de un modelo completamente abierto que compite directamente con soluciones cerradas y propietarias de empresas como OpenAI, Anthropic y Meta. El hecho de que un modelo de código abierto pueda posicionarse tan alto en rankings competitivos demuestra que la brecha entre los modelos abiertos y cerrados se está cerrando rápidamente."

Frases tipo Wikipedia con poca densidad informativa. Un emprendedor publicando un blog quiere "Gemma 4 (31B) es #3 en Arena Leaderboard, Apache 2.0", no 80 palabras de contexto. Phi-4 castiga esto.

#### Hipótesis 2 — Opus expande con meta-comentarios que el juez no premia

Patrón observado en `agent_capabilities/skill_execution_complex`:
- Llama 3.3 70B: ejecuta el skill directamente, devuelve resultado.
- Opus 4.7: "Voy a abordar esta tarea paso a paso. Primero, déjame entender qué necesita el usuario..." → razona inline → ejecuta.

El meta-razonamiento es **útil para el usuario humano** pero el juez automático evalúa el resultado final, no el proceso. Y en agent_long_horizon multi-turn, el meta-razonamiento puede contaminar contexto futuro (de ahí la regresión con thinking forzado).

#### Hipótesis 3 — Output structure: JSON con texto antes/después

En `news_json_output_strict` (rúbrica espera SOLO JSON), Opus a veces agrega prefijos como "Aquí está el JSON solicitado:" o markdown wrapping ` ```json ... ``` `. Llama 3.3 70B produce el JSON crudo. La rúbrica regex penaliza el extra.

⚠️ A validar revisando 5+ respuestas concretas de cada modelo en este test.

#### Hipótesis 4 — Tests con criterios "estilo emprendedor LATAM" no premian estilo asistente formal

Nuestros tests piden cosas como "redacta un email de cold outreach para una startup chilena de SaaS". El "buen email" según los criterios:
- Conciso (60-100 palabras)
- Hook directo
- Call-to-action específico

Opus tiende a producir **emails de 150-200 palabras** con párrafos contextuales tipo "consulting profesional". Técnicamente correcto pero no lo que un emprendedor solo quiere copy-pegar a 200 prospects.

**Llama 3.3 70B genera el email de 80 palabras con CTA directo.** El juez prefiere el de Llama porque cumple los criterios.

#### Hipótesis 5 — Saturación del juez Phi-4

Phi-4 puede tener un techo en cuánto puntúa "muy bien escrito" porque su entrenamiento se basa en respuestas concisas y directas. Modelos como Opus que producen "respuestas de tutor universitario" pueden chocar con ese techo.

Validación pendiente: comparar judge_score con un segundo juez (Claude Haiku 4.5 o Gemma 4 31B) en una muestra de 30 tests para ver si la divergencia Opus-vs-Llama es consistente.

#### Hipótesis 6 — Tests de `agent_capabilities` favorecen ejecución directa, no consulta-asesor

En `agent_team_delegation`, `skill_execution_complex`, etc., el modelo debe **delegar y coordinar**, no explicar. Opus tiene un prior fuerte hacia "asistente que orienta" — explica QUÉ va a hacer antes de hacerlo. Llama 3.3 70B (post-trained más para ejecución) hace primero, explica si pregunta.

#### Plan de validación (próximos pasos)

1. **Inspección manual de 30 respuestas Opus vs Llama** en los 5 tests con mayor delta (multi_tool_sequential, skill_execution_complex, content_iteration, translation/detect_language_issues, news_json_output_strict).
2. **Re-correr Opus 4.7 con sistema "be concise"** en el system prompt — ver si quality sube.
3. **Segundo juez (Gemma 4 31B local)** sobre muestra de 50 tests para verificar consistencia con Phi-4.
4. **Análisis de output tokens distribución** — no solo promedio, sino histograma. Si Opus tiene runs de 3K+ tokens en algunos tests, eso indica verbosidad concentrada.

### Stack recomendado para OpenClaw / Hermes / N8N (basado en datos v2.4.2)

**LLM cabecera (orquestador)** — necesita context retention + skill orchestration + cost-effective:

| Recomendación | Score agente | Justificación |
|---|---|---|
| 🥇 **GPT-OSS 120B (Ollama Cloud)** | 8.15 | #1 agéntico inter-modelo. **Gratis con sub Ollama Cloud**. Apache 2.0. Para usuarios que ya pagan Ollama Cloud. |
| 🥈 **Llama 3.3 70B (Groq)** | 7.60 | Score robusto en multi-turno. 270 tok/s = latencia ultra baja. $1.36/1k calls. Apache 2.0. |
| 🥉 **MiMo V2.5 (Xiaomi sub)** | 7.65 | Excelente C/B con sub $14/mes. Suscripción te da costo predecible. |

**Skills especializados** (delegan tareas específicas desde el cabecera):

| Skill | Modelo recomendado | Score |
|---|---|---|
| **Coding** (workflows N8N, plugins, scripts) | Devstral Small (Apache 2.0) | 7.77 agéntica, 7.61 single-turn |
| **Content** (blog, social, newsletter) | MiMo V2.5 Xiaomi sub o Gemini 3.1 Flash Lite | 7.65 / 7.31 agéntica |
| **Research con tools** (Perplexity-style) | DeepSeek V4 Flash (NIM gratis) o Mistral Small 4 | 6.48 / 7.41 |
| **Customer support multi-turno** | GPT-OSS 120B Cloud o Llama 3.3 70B | 8.15 / 7.60 |
| **Tool calling estructurado** (JSON estricto) | MiMo V2.5 (7.21 tool_calling), Gemini 3.1 Flash Lite (7.10) | |
| **Multimodal** (OCR, video) | MiMo V2-Omni Xiaomi direct | 7.75 |

**Lo que NO recomendamos** para producción a volumen:
- ❌ Claude Opus/Sonnet/Haiku con thinking forzado en multi-turn (empeora)
- ❌ Modelos NIM gigantes (>500B) con prompts largos en NIM (timeouts/429 cascada)
- ❌ Forzar reasoning en cualquier modelo hybrid sin testear primero (excepto Kimi K2.5)

---

# Insights del benchmark — qué dice la data, no el marketing

> 📍 **Disclaimer prominente**: este benchmark **NO sustituye** a los benchmarks académicos validados (HumanEval, MMLU, GSM8K, SWE-bench Verified, NIAH original inglés, MT-Bench, LMSYS Arena). Es un **complemento** para emprendedores hispanohablantes que deciden qué modelo poner en producción para casos aplicados en español neutro (N8N, OpenClaw, Hermes, blogs LATAM, soporte cliente, agentes). Para investigación académica o capacidades fundamentales, prioriza los benchmarks oficiales. Cross-references documentadas en [BENCHMARKS_EXTERNOS.md](BENCHMARKS_EXTERNOS.md) y [NIAH_CROSSREF.md](NIAH_CROSSREF.md).

Este documento es el análisis cuantitativo del benchmark `ai-benchmarks-alternativos` al **29 de abril de 2026** (v2.4). 68 modelos con cobertura ≥50 runs, 91 tests por modelo, juez Phi-4 local. La pregunta que respondemos no es "cuál es el mejor", sino: **qué patrones aparecen en la data cuando comparas precio, velocidad, capacidades y proveedor a la vez**.

Audiencia: emprendedores latinoamericanos eligiendo modelos para producción (OpenClaw, N8N, blogs de actualidad, atención al cliente, herramientas internas). Tono neutro: lo que dice la data, no lo que el marketing quiere que pienses.

---

## 🆕 Update v2.4.1 — Nemotron 3 Nano Omni Reasoning + DGX Lote 2 + suite agent_long_horizon (29 abril 2026, 19:00 ET)

Tres adiciones desde v2.4:

### Nemotron 3 Nano Omni 30B-A3B Reasoning (NIM)

Lanzado por NVIDIA el 20 abril 2026. MoE 30B totales / 3B activos (A3B), thinking + multimodal. Corrido en NIM gateway gratis.

| Métrica | Valor |
|---|---|
| Score global | **6.97** (91/91 OK) |
| Posición global | ~#22 (entre Qwen 3-Next 80B y Nemotron Nano 9B v2) |
| tok/s | ~16 |
| Costo | $0 (NIM gratis) |

**Lectura**: a pesar del thinking + multimodal (que en marketing prometen mejor performance), saca **menos** que Gemma 4 31B (NIM) 7.20 y que Devstral 2 123B 7.12 con la mitad de parámetros activos. Confirma el patrón ya documentado: thinking models pierden en single-turn (consumen budget razonando para tareas que no lo requieren) y multimodal solo brilla en tests donde hay imagen/audio (este benchmark es 100% texto).

### Nemotron 3 Base 33B (DGX Spark Q4_K_M)

Versión base de la familia Nemotron 3, 33B en Q4_K_M corriendo en DGX Spark vía Ollama oficial.

| Métrica | Valor |
|---|---|
| Score global | **6.74** (103/103 OK) |
| tok/s | ~65 (lento por modelo grande Q4) |
| Costo | $0 (hardware propio) |
| Comparable | Idéntico al Nemotron 3 Super 120B también en DGX (6.74 = 6.74). |

**Hallazgo importante — paridad Q4 Base 33B = Q4 Super 120B en DGX**: el modelo 75% más pequeño rinde igual en hardware propio cuantizado. Para uso local en DGX Spark, el Base 33B es la mejor opción C/B (carga más rápido, ocupa 26 GB vs 87 GB del Super). El Super solo valdría si tenés una task que escala con parámetros (long-context, código complejo). Para todo lo demás, el 33B Q4 entrega lo mismo gastando 70% menos VRAM.

### Suite `agent_long_horizon` (nueva)

12 tests multi-turno (8+ turnos) que miden capacidades agénticas reales: context retention, skill orchestration, interruption recovery, goal persistence. Plantilla rígida (sin LLM dinámico haciendo de usuario), tools simulados via stubs, rúbrica regex-based con weights = 1.0.

Smoke + validación con 3 modelos:

| Modelo | Single-turn avg | agent_long_horizon avg | Delta |
|---|---|---|---|
| Llama 3.3 70B (Groq) | 7.64 | 7.50 | -0.14 |
| Mistral Small 4 | 7.54 | 7.41 | -0.13 |
| Nemotron 3 Base 33B (DGX) | 6.74 (global) | 6.59 (12 tests) | -0.15 |
| MiMo-V2-Flash (free) | 7.20 | 0.00 (12/12 fail) | API issue, no representativo |

**Hallazgo**: los 3 modelos top mantienen ranking, con un drop consistente de ~0.15 puntos en agent_long_horizon vs single-turn. La suite NO duplica el ranking single-turn; está midiendo algo diferente pero correlacionado. Próximo paso: validar con un modelo realmente flojo (Step 3.5 Flash 6.38 single-turn, p.ej.) para confirmar que la varianza inter-modelo crece.

**Tests más difíciles** (donde Llama 3.3 70B saca <7.5):
- `context_decay_constraint_12turns` (6.4): tras 13 turnos largos, olvida un constraint inicial
- `constraint_under_pressure` (7.0): bajo presión a inventar fuentes, mantiene línea pero con margen
- `distractor_resistance` (7.2): vuelve al objetivo tras 3 distractores

**Tests fáciles para todos**: `skill_orchestration_correct_choice`, `skill_with_failure_recovery` — los modelos top eligen tools correctamente en tareas estructuradas.

---

## 🚨 Limitación crítica: NO medimos debugging agentic real

**Caso real reportado** (30 abril 2026): un emprendedor enfrentó un **problema técnico complejo en un contenedor OpenClaw corriendo en VPS Hetzner**. Probó resolverlo con MiniMax M2.7 (top #7 en nuestro benchmark) usando OpenCode como agente — **NO pudo solucionarlo**. Cambió a Claude Opus 4.7 (posición fuera del top 10 en nuestro benchmark) — **resolvió el problema en pocos minutos**.

Este caso expone una **limitación seria de nuestro benchmark** que hay que reconocer:

### Lo que NO medimos

| Dimensión | Lo mide | Nosotros lo medimos |
|---|---|---|
| Debugging agentic con sandbox real (Docker, FS, exec) | **SWE-bench Verified** | ❌ NO |
| Multi-turn 20+ con tool feedback real del sistema | **Claw-Eval** (300 tareas verificadas humanamente) | ⚠️ Parcial — `agent_long_horizon` simula tools con stubs hardcoded |
| Resolución de problemas en infra real (K8s, VPS, networking) | **Terminal-Bench 2.0**, OSWorld | ❌ NO |
| Long-context bajo carga (>32K tokens) | **NIAH** (Needle-in-Haystack) | ❌ NO (en ROADMAP como Approach 2) |
| Persistencia / judgment en sesiones largas con hipótesis fallidas | (No hay benchmark estándar) | ❌ NO |

### Por qué nuestro coding score NO predice debugging real

Nuestros tests de coding miden **"¿el modelo PUEDE escribir código correcto?"**, no **"¿el modelo PUEDE resolver un bug real iterando con tools en sandbox hasta que funcione?"**:

- `code_generation`: "Genera función Python para X" — single-turn, criterio determinístico, 1 disparo
- `string_precision`: "Copia exactamente esta API key" — formato verificable
- `news_seo_writing/news_json_output_strict`: JSON estructurado — schema-validable
- `agent_long_horizon`: multi-turn con tools **simulados** (stubs hardcoded) — sin Docker sandbox

Son preguntas distintas. Un modelo puede sacar 8.0+ en quality de coding aplicado y fallar en debugging real porque no tiene el judgment para iterar tras hipótesis fallidas, la tolerancia a contexto largo de 50+ turnos con logs reales, o la persistencia para mantener un objetivo cuando 5 intentos no funcionaron.

### Para debugging agentic real, prioriza estos benchmarks externos

Para tareas tipo "tengo un bug en producción, resuélvemelo", **mirá las métricas que SÍ lo miden**, NO nuestro coding score:

| Modelo | Nuestro Coding | SWE-bench Verified | Aprox |
|---|---|---|---|
| **Claude Opus 4.7** | 7.39 (top 5) | **87.6%** ⭐ | #1 globalmente |
| Claude Sonnet 4.6 | ~7.3 | 77.2% | top 5 |
| Devstral Small (specialist) | 8.03 | N/A reportado | (specialist coding) |
| Llama 3.3 70B (Groq) | 8.01 | ~50% (Llama family base) | mid |
| MiniMax M2.7 | 6.86 | N/A reportado | sin data oficial |
| GPT-5.4 | 7.37 | reportado en system card | top |

**SWE-bench Verified** (Anthropic, 500 tareas debugging reales con repos + tests verificados humanamente) es el benchmark de referencia para esta dimensión. **Opus 4.7 es #1 globalmente con 87.6%** — eso predice mejor su comportamiento en tu VPS Hetzner que cualquier número de nuestro benchmark.

### Implicaciones honestas

1. **Si tu task es generar código nuevo aplicado** (workflows N8N, plugins WP, scripts Python, blog posts en español): nuestro ranking es útil. Devstral Small, Llama 3.3 70B Groq, Mistral Small 4 ganan porque entregan calidad+velocidad+costo.

2. **Si tu task es debugging real con tools en producción**: nuestro ranking NO es predictivo. **Mirá SWE-bench Verified, Claw-Eval (Pass³ multi-trial), Terminal-Bench**. Para casos críticos (incident response, hot-fixes, debugging de infra), Opus 4.7 / GPT-5.x premium siguen valiendo lo que cuestan.

3. **No existe ranking universal**. Esta es la regla #0 del benchmark: "no existe el mejor modelo universal — existen modelos buenos para una tarea, en un volumen, con una restricción". Esta limitación es ejemplo concreto.

### Cómo lo vamos a abordar (ROADMAP)

- ✅ Documentado HOY como caso real validado
- ⏳ **Suite `agentic_debugging` propia** (5-10 tests con escenarios de bugs reales en Docker/K8s/VPS, multi-turn 10-20 con stubs detallados, rúbrica focused en root cause + fix correcto + iteración tras feedback "no funcionó"). Costo estimado: ~$30-50 corriendo en top 10. ETA: 1 semana
- ⏳ **Cross-reference SWE-bench Verified más prominente** en tabla principal cuando hay dato oficial
- ⏳ **Replicar SWE-bench Verified en top 15** (es reproducible, infra pública). Costo: $50-100. ETA: 2-3 días post-paper
- ⏳ **NIAH-ES** (long-context español) en ROADMAP como Approach 2 — cubre parcialmente la dimensión "tolerancia a contexto largo"

---

## ⚠️ Limitaciones críticas a leer ANTES del análisis

El benchmark tiene tres limitaciones estructurales que cambian la interpretación de varios hallazgos:

1. **Single-turn ≠ producción real con tools.** Cada test es un prompt único, sin acceso a herramientas externas. En producción, un modelo "más débil" combinado con búsqueda web (Perplexity, Tavily) o RAG puede superar a un modelo "más fuerte" sin tools. Si tu pipeline usa N8N con tool de búsqueda, el ranking acá no se traduce 1-a-1.

2. **Cobertura desigual entre modelos.** El piso es 50 runs, pero algunos llegan a 91 (cobertura completa de las 23 suites) y otros a 87 ó 68 (con DNS errors o timeouts del proveedor). Devstral 2 123B (NIM) tiene 68 runs con la suite agent_capabilities incompleta — su score 7.12 podría bajar 0.2-0.3 cuando se complete. Cualquier afirmación sobre modelos sub-91 runs es **provisoria**.

3. **El provider importa tanto como el modelo.** El mismo modelo en Groq vs OpenRouter vs NIM puede tener latencia 5× distinta y a veces score ±0.5 puntos por diferencias de cuantización (Q4 vs FP16) o configuración del provider. El ranking global esconde estas diferencias — la sección 3 las cuantifica.

Para decisiones reales: estos hallazgos cuantitativos filtran el 80% de modelos malos. El 20% final lo decides tú con 5-10 prompts típicos de tu caso de uso, en el mismo provider y configuración (con/sin tools) que vas a usar en producción.

---

## Tabla de contenidos

0. [Hallazgos destacados v2.4 — Lote 9 NIM + DGX Spark + DeepSeek V4 + MiMo](#0-hallazgos-destacados-v24)
1. [Correlación precio ↔ calidad por pilar](#1-correlación-precio--calidad-por-pilar)
2. [Outliers — malas compras, joyas y especialistas](#2-outliers--malas-compras-joyas-y-especialistas)
3. [Provider matters — el mismo modelo en distintos proveedores](#3-provider-matters--el-mismo-modelo-en-distintos-proveedores)
4. [Patrones de fragilidad — tool calling y JSON estructurado](#4-patrones-de-fragilidad--tool-calling-y-json-estructurado)
5. [Sensibilidad por idioma — español vs inglés](#5-sensibilidad-por-idioma--español-vs-inglés)
6. [Costo real para el emprendedor N8N — ranking mensual y Pareto](#6-costo-real-para-el-emprendedor-n8n--ranking-mensual-y-pareto)
7. [Regresiones — cuando la versión nueva es peor](#7-regresiones--cuando-la-versión-nueva-es-peor)
8. [Open-source vs propietario — ¿se cerró la brecha?](#8-open-source-vs-propietario--se-cerró-la-brecha)
9. [Anti-patterns del marketing — claims que no se sostienen](#9-anti-patterns-del-marketing--claims-que-no-se-sostienen)
10. [Top 3 hallazgos sorpresivos del v2.4](#10-top-3-hallazgos-sorpresivos-del-v24)
11. [Implicaciones para la próxima iteración](#11-implicaciones-para-la-próxima-iteración)
12. [Datos sospechosos / a re-validar](#12-datos-sospechosos--a-re-validar)

---

## 0. Hallazgos destacados v2.4

### 0.1 Top 10 global — la base sobre la que se construyen los hallazgos

| # | Modelo | Score | Costo $/1k calls | tok/s | Provider | Open |
|---|---|---|---|---|---|---|
| 1 | Llama 4 Scout 17B | **7.67** | 0.54 | 244 | Groq direct | sí |
| 2 | Llama 3.1 8B Instant | **7.66** | 0.14 | 368 | Groq direct | sí |
| 3 | Llama 3.3 70B | **7.64** | 1.36 | 238 | Groq direct | sí |
| 4 | Mistral Small 4 | **7.54** | 0.94 | 110 | OpenRouter | sí |
| 5 | GPT-OSS 20B | **7.53** | 0.47 | 633 | Groq direct | sí |
| 6 | Gemini 3.1 Flash Lite | **7.50** | 2.33 | 148 | Google direct | no |
| 7 | Grok 4.1 Fast | **7.50** | 0.81 | 116 | xAI/OpenRouter | no |
| 8 | GPT-OSS 120B | **7.41** | 0.00 | 75 | Ollama Cloud | sí |
| 9 | Devstral Small | **7.35** | 0.48 | 147 | OpenRouter | sí |
| 10 | MiMo V2.5 | **7.32** | 0.13 | 79 | Xiaomi direct | no |

**Lectura inmediata**: 8 de 10 son open-source. Los 4 modelos en Groq direct (#1, #2, #3, #5) tienen >200 tok/s, score >7.5 y costo <$1.50/1k calls. Esa combinación no existe en proveedores cerrados pagados.

### 0.2 Lote 9 NIM (NVIDIA gateway gratuito, 40 RPM)

15 modelos corridos en NIM gratis. 1,358 runs útiles, 117 errores transitorios (502/504 de gateway, modelos gigantes con prompts largos). El ranking del Lote 9 NIM:

| Modelo NIM | Score | Runs | Domina en |
|---|---|---|---|
| Gemma 4 31B (NIM) | **7.20** | 96 | 14/23 categorías del lote |
| Qwen 3-Next 80B Instruct | 7.17 | 91 | tool_calling, multi-turn |
| Devstral 2 123B | 7.12 | 68 | deep_reasoning #2, string_precision #1 |
| DeepSeek V4 Flash | 7.07 | 87 | balance general |
| Qwen 3.5 397B (NIM) | 7.02 | 91 | code_generation, orchestration |
| Nemotron Nano 9B v2 | 6.91 | 91 | startup_content #1, policy_adherence #1 |
| Mistral Large 3 675B | 6.89 | 87 | orchestration #1 (7.08) |
| GLM 5 (NIM) | 6.87 | 90 | balance |
| Ministral 14B (NIM) | 6.85 | 90 | latency baja |
| GLM 5.1 (NIM) | 6.79 | 182 | regresión vs GLM 5 |
| Nemotron Super 49B v1.5 | 6.77 | 86 | reasoning |
| Qwen 3-Next 80B Thinking | 6.41 | 182 | regresión vs Instruct |
| Step 3.5 Flash | 6.38 | 91 | bottom |
| Kimi K2 Thinking | 6.32 | 90 | bottom |
| Kimi K2.5 (NIM) | 6.27 | 118 | bottom |

**Hallazgo NIM #1 — el modelo gigante NO siempre gana**: Mistral Large 3 (675B parámetros) saca 6.89, mientras Nemotron Nano 9B v2 saca 6.91 con **75× menos parámetros**. Para producción de bajo volumen con NIM, modelos pequeños competentes (9B-30B) son mejor opción que dependencias en los 600B+ que se cuelgan en gateway.

**Hallazgo NIM #2 — Magistral Small (Mistral) descartado**: error 400 instant en 91/91 tests. NIM rechaza algún parámetro del adapter (probablemente algo del thinking mode). Documentado como bloqueante en `MODELOS.md`.

**Hallazgo NIM #3 — DeepSeek V4 Pro inviable en NIM**: 502/504 timeouts en 88 de 91 tests con prompts largos (workshop_outline, perplexity_research). Solo 3 runs útiles. El modelo funciona vía Ollama Cloud y otros providers — el problema es la combinación NIM gateway + thinking + prompts >2k tokens.

### 0.3 DGX Spark Lote 1 (hardware propio, Q4_K_M cuantizado)

Hardware: NVIDIA DGX Spark, 128GB RAM unificada, modelos Q4_K_M (4-bit cuantizado para correr en VRAM disponible). Latencia 9-18 tok/s sostenido. Costo $0.

| Modelo DGX | Score | Runs | tok/s | Notas |
|---|---|---|---|---|
| Gemma 4 31B (Q4_K_M) | 6.84 | 89 | 9.3 | -0.36 vs NIM FP16 (mismo modelo, distinta cuantización) |
| Nemotron 3 Super 120B (Q4_K_M) | 6.74 | 90 | 16.8 | mejor en code/structured/string_precision dentro DGX |

**Hallazgo cuantización**: Gemma 4 31B en Q4_K_M (DGX) saca 6.84 vs 7.20 en FP16 (NIM). **Costo de Q4 = -0.36 puntos** en score (-5%). Para datos sensibles que no pueden salir de la máquina, Q4 es viable. Para producción donde se aceptan APIs externas, FP16 vía NIM gratis es estrictamente mejor.

### 0.4 MiMo V2.5 (Xiaomi) — la suscripción que sorprende

Xiaomi lanzó MiMo en abril 2026 con 7 modelos vía suscripción mensual ($14/mes, off-peak 0.8x consumo). Resultado del benchmark:

| Modelo MiMo | Score | $/1k calls | tok/s |
|---|---|---|---|
| MiMo V2.5 | 7.32 | 0.13 | 79 |
| MiMo V2.5-Pro | 7.26 | 0.25 | 50 |
| MiMo-V2-Flash | 7.20 | 0.46 | 52 |
| MiMo V2-Pro | 7.13 | 0.13 | 45 |
| MiMo V2-Omni | 7.13 | 0.13 | 103 |

**MiMo V2.5 entra al top 10 global con costo subsidiado por suscripción**. La división v2.5 vs v2-Pro muestra mejora real generación a generación (+0.13 puntos). Recomendable evaluar para uso intensivo de contenido en español.

### 0.5 DeepSeek V4 vs Claude Opus

DeepSeek V4 Pro saca 6.48 (con 69 runs). Claude Opus 4.7 saca 7.16. Diferencia +0.68 puntos a favor de Claude. **Costo Claude vs DeepSeek**: $117 vs $5.74 por 1k calls = **20.4× más caro**. Si tu volumen es alto, ¿pagarías 20× para ganar 9.4% de score?

DeepSeek V4 Flash (NIM gratis) saca 7.07 — **más alto que el Pro** y a $0. Esto es típico del patrón: la versión "Pro" del modelo razonador no necesariamente entrega más score en single-turn. Razona más, factura más reasoning tokens, y el output final no necesariamente es mejor.

---

## 1. Correlación precio ↔ calidad por pilar

Spearman rank correlation entre `cost_per_1k_calls_usd` y `score_global` (modelos pagados, n=47, free n=21 separado):

| Categoría | ρ Spearman | p-value | Interpretación |
|---|---|---|---|
| **Global** | **−0.460** | 0.001 | Negativa moderada — caro NO predice mejor |
| Razonamiento | −0.368 | 0.011 | Negativa moderada |
| Coding | −0.338 | 0.020 | Negativa moderada |
| **Contenido** | **−0.603** | <0.001 | **Negativa fuerte — más caro = peor en contenido** |
| Agentes | −0.229 | 0.121 | No significativa |

**Lectura**: la correlación entre precio y calidad **es negativa** en todos los pilares medidos, fuertemente negativa en Contenido. Esto desafía la intuición "más caro debe ser mejor" — en el ecosistema actual, los modelos premium ($15-117 por 1k calls como Claude Opus, GPT-5.5, Gemini Pro) tienden a perder con modelos económicos en single-turn.

**Por qué**: dos hipótesis con respaldo en la data:
- Los modelos premium suelen ser thinking models que consumen reasoning tokens. En single-turn corto, ese razonamiento extra no aporta score y sí cuesta tokens facturados.
- La métrica del juez Phi-4 prioriza calidad de formato, idioma español neutro y sustancia razonable. Los modelos económicos modernos (Llama 3.3, GPT-OSS, Gemma 4) están bien afinados para esos criterios.

**Free tier (n=21, mayormente NIM + Ollama Cloud)**: score promedio 6.82. Pagados (n=47): 7.05. La diferencia (+0.23) es marginal — el free no penaliza fuerte al usuario en calidad promedio.

**Velocidad vs calidad**: ρ = +0.520 (p<0.001). **Más rápido sí correlaciona positivamente con mejor score**. Razón estructural: los modelos en Groq (>200 tok/s) están en el top 10. Esa correlación es de selección de proveedor más que de capacidad inherente del modelo.

---

## 2. Outliers — malas compras, joyas y especialistas

### 2.1 Malas compras (caro + score bajo)

Modelos con costo ≥ $5/1k calls Y score < 7.0. **No deberías estar usando estos para tareas single-turn**:

| Modelo | $/1k | Score | Comentario |
|---|---|---|---|
| GPT-5.5 | 46.50 | 6.44 | Más caro del benchmark, peor que GPT-4.1 (7.23) |
| GPT-5.4 | 24.00 | 6.90 | Pierde con GPT-5.4 Mini (7.16) |
| Claude Sonnet 4.6 | 23.40 | 6.99 | Último Sonnet — perdió contra Llama 3.1 8B (7.66) |
| Gemini 3.1 Pro | 18.60 | 6.41 | Peor que Gemini 3.1 Flash Lite (7.50) a 8× del costo |
| Gemini 2.5 Pro | 15.38 | 6.47 | Misma historia que 3.1 Pro |
| Mistral Large | 9.60 | 6.98 | Mistral Small 4 saca 7.54 a 1/10 del costo |
| Grok 4.20 | 9.60 | 6.92 | Grok 4.1 Fast saca 7.50 a 1/12 |
| DeepSeek V4 Pro | 5.74 | 6.48 | DeepSeek V4 Flash (NIM gratis) saca 7.07 |
| Kimi K2.6 | 5.49 | 6.51 | Versión razonadora — pierde con la Instruct |
| GLM-5.1 | 5.01 | 6.79 | Empate con GLM 5 NIM ($0) |

**Patrón crítico**: TODOS los modelos premium (>$5/1k) que tienen una variante "Mini", "Flash" o "Small" pierden contra esa variante en el benchmark. El single-turn no recompensa el razonamiento extra que justifica el precio premium.

### 2.2 Joyas (barato + score alto)

Modelos con score ≥ 7.20 Y costo ≤ $1.50/1k calls (excluye gratis):

| Modelo | $/1k | Score | tok/s |
|---|---|---|---|
| Llama 4 Scout 17B (Groq) | 0.54 | 7.67 | 244 |
| Llama 3.1 8B Instant (Groq) | 0.14 | 7.66 | 368 |
| Llama 3.3 70B (Groq) | 1.36 | 7.64 | 238 |
| Mistral Small 4 | 0.94 | 7.54 | 110 |
| GPT-OSS 20B (Groq) | 0.47 | 7.53 | 633 |
| Grok 4.1 Fast | 0.81 | 7.50 | 116 |
| Devstral Small | 0.48 | 7.35 | 147 |
| MiMo V2.5 (Xiaomi) | 0.13 | 7.32 | 79 |
| MiMo V2.5-Pro (Xiaomi) | 0.25 | 7.26 | 50 |
| Hermes 4 70B | 0.64 | 7.24 | 64 |
| MiMo-V2-Flash | 0.46 | 7.20 | 52 |
| Gemma 4 31B | 0.99 | 7.20 | 23 |
| Nemotron 3 Nano 30B | 0.32 | 7.20 | 88 |

**13 modelos ofrecen >7.2 de score por menos de $1.50/1k calls**. Cualquier emprendedor con presupuesto restringido tiene 13 candidatos válidos antes de mirar el tier premium.

### 2.3 Joyas gratis (free + score ≥ 7.0)

NIM y Ollama Cloud tienen modelos gratis competitivos:

| Modelo | Score | tok/s | Provider |
|---|---|---|---|
| GPT-OSS 120B | 7.41 | 75 | Ollama Cloud |
| Gemma 4 31B (NIM) | 7.20 | 23 | NVIDIA NIM |
| Qwen 3-Next 80B Instruct | 7.17 | 52 | NVIDIA NIM |
| Devstral 2 123B (NIM) | 7.12 | 42 | NVIDIA NIM (68 runs) |
| DeepSeek V4 Flash | 7.07 | 25 | NVIDIA NIM |
| Qwen 3.5 397B (NIM) | 7.02 | 20 | NVIDIA NIM |

**Hallazgo importante**: 6 modelos gratuitos pasan el umbral 7.0. Para proyectos personales, prototipos o producción de bajo volumen (<40 RPM en NIM), pagas $0 por capacidades top-15 globales.

### 2.4 Frontera de Pareto (cheaper Y better — no dominados)

Solo 3 modelos están en la frontera estricta de Pareto (no existe otro modelo más barato Y con mejor score):

| Modelo | Score | $/1k | Por qué está en Pareto |
|---|---|---|---|
| GPT-OSS 120B (Ollama Cloud) | 7.41 | 0.00 | Top score gratis |
| Llama 3.1 8B Instant (Groq) | 7.66 | 0.14 | Mejor relación calidad/precio absoluta |
| Llama 4 Scout 17B (Groq) | 7.67 | 0.54 | Mejor score de modelos pagados |

Si tu decisión es solo costo vs score, eliges entre estos 3. Cualquier otra elección significa que estás priorizando otra cosa: latencia (Groq tiene el mejor stack), tools (algunos modelos manejan tool_calling mejor), idioma (Devstral, GPT-OSS dominan español), etc.

### 2.5 Especialistas — modelos que dominan suites específicas

Top 1 por suite (los más útiles en su nicho aunque no estén en el top global):

| Suite | Líder | Score suite | Score global |
|---|---|---|---|
| reasoning | GPT-OSS 20B (Groq) | 7.97 | 7.53 |
| deep_reasoning | Llama 4 Scout 17B (Groq) | 7.68 | 7.67 |
| code_generation | Llama 4 Scout 17B (Groq) | 8.04 | 7.67 |
| content_generation | GPT-OSS 20B (Groq) | 8.18 | 7.53 |
| startup_content | GPT-OSS 20B (Groq) | 8.10 | 7.53 |
| creativity | Llama 3.1 8B Instant | 7.92 | 7.66 |
| translation (ES↔EN) | GPT-OSS 20B (Groq) | 8.04 | 7.53 |
| tool_calling | Llama 3.1 8B Instant | 8.45 | 7.66 |
| structured_output | Llama 3.1 8B Instant | 8.00 | 7.66 |
| hallucination (detect) | Llama 4 Scout 17B | 7.88 | 7.67 |
| orchestration | Qwen 3.5 397B (Ollama Cloud) | 7.66 | 6.72 |
| task_management | MiMo V2-Omni (Xiaomi) | 7.96 | 7.13 |
| sales_outreach | Llama 3.3 70B (Groq) | 8.06 | 7.64 |
| presentation | Llama 4 Scout 17B (Groq) | 8.05 | 7.67 |
| string_precision | Devstral Small | 8.12 | 7.35 |
| customer_support | Mistral Small 4 | 8.12 | 7.54 |
| news_seo_writing | GPT-OSS 120B (Ollama Cloud) | 7.44 | 7.41 |
| ocr_extraction | Llama 3.3 70B (Groq) | 7.60 | 7.64 |
| multi_turn | GPT-OSS 20B (Groq) | 7.67 | 7.53 |
| policy_adherence | Llama 4 Scout 17B (Groq) | 7.60 | 7.67 |
| agent_capabilities | Llama 3.1 8B Instant | 7.78 | 7.66 |

**Patrones**:
- **Llama family domina 11/23 suites** — sobre todo el subset Groq-direct.
- **GPT-OSS 20B y 120B** dominan contenido y razonamiento simple.
- **Devstral Small** es el rey absoluto de string_precision (8.12) — útil para ETL/data extraction.
- **Mistral Small 4** lidera customer_support con 8.12, despuntando en respuestas estructuradas y empáticas.
- **Qwen 3.5 397B (Ollama Cloud)** es especialista en orchestration aunque global sea mediocre — útil si tu pipeline es multi-step.

---

## 3. Provider matters — el mismo modelo en distintos proveedores

### 3.1 Gemma 4 31B — tres proveedores, dos cuantizaciones

| Provider | Score | Costo | tok/s | Cuantización |
|---|---|---|---|---|
| OpenRouter | 7.20 | $0.99/1k | 22.8 | FP16 |
| NVIDIA NIM | 7.20 | $0.00 | 22.8 | FP16 |
| DGX Spark local | 6.84 | $0.00 | 9.3 | Q4_K_M |

**Hallazgo**: OpenRouter y NIM dan resultados **idénticos** (7.20 vs 7.20) — confirma que NIM gratis no degrada el modelo. La caída a Q4 cuesta -0.36 puntos (5% del score). Si tu hardware es DGX, ahorras costo y latencia de red pero entregas precisión menor.

### 3.2 Kimi K2.5 — OpenRouter pagado vs NIM gratis

| Provider | Score | Costo |
|---|---|---|
| OpenRouter | 6.27 | $1.26/1k |
| NIM | 6.27 | $0.00 |

**Hallazgo**: 100% de paridad. Pagar OpenRouter para Kimi K2.5 cuando NIM lo da gratis es **dinero quemado**. Aplica para todo modelo del catálogo NIM con equivalente OpenRouter.

### 3.3 Qwen 3.5 397B — Ollama Cloud vs NIM (cuantizaciones distintas)

| Provider | Score | Notas |
|---|---|---|
| Ollama Cloud | 6.72 | Cuantizado para correr en cloud Ollama |
| NIM | 7.02 | FP16 |

**Hallazgo**: NIM da +0.30 puntos sobre Ollama Cloud para el mismo Qwen 3.5 397B. Si tu pipeline usa Qwen 3.5 cloud, **migrar a NIM gratis te sube score y baja costo**. Cuidado: NIM tiene cap de 40 RPM — para volúmenes altos Ollama Cloud sigue siendo la opción.

### 3.4 Llama 3.x y 4 — Groq vs OpenRouter (latencia)

Groq direct vs el mismo modelo vía OpenRouter (que internamente puede rutear a Together, Fireworks o Groq):

- Llama 3.1 8B Instant **Groq**: 7.66 score, 368 tok/s, latencia ~0.5s
- Llama 3.3 70B **Groq**: 7.64 score, 238 tok/s
- Llama 4 Scout **Groq**: 7.67 score, 244 tok/s

Sin equivalente directo del benchmark (porque los corrimos solo en Groq), pero la regla es: **si Groq tiene el modelo, usa Groq**. La LPU entrega 5-10× más velocidad a precio competitivo.

### 3.5 Implicación operativa

El hallazgo más fuerte de esta sección: **el mismo modelo puede tener delta de hasta +0.30 puntos según provider** (Qwen 3.5 NIM vs Cloud), y delta de hasta -0.36 puntos por cuantización (Gemma 4 NIM FP16 vs DGX Q4). Antes de elegir un modelo, decide el provider según tu prioridad:

- **Velocidad ante todo**: Groq direct
- **Costo cero, calidad FP16**: NIM (con cap 40 RPM)
- **Volumen alto sostenido**: Ollama Cloud o OpenRouter pagado
- **Datos sensibles, on-prem**: DGX Spark + Q4_K_M (asume -5% score)

---

## 4. Patrones de fragilidad — tool calling y JSON estructurado

### 4.1 Tool calling — quién maneja bien la sintaxis OpenAI tools

Top 5 en suite `tool_calling`:

| Modelo | Score tool_calling | Score global | Delta |
|---|---|---|---|
| Llama 3.1 8B Instant (Groq) | 8.45 | 7.66 | +0.79 |
| Llama 4 Scout 17B (Groq) | 8.19 | 7.67 | +0.52 |
| Qwen 3.5 (Ollama Cloud) | 8.18 | 6.66 | +1.52 |
| Grok 4.1 Fast | 8.07 | 7.50 | +0.57 |
| Qwen 3.5 397B (Ollama Cloud) | 7.98 | 6.72 | +1.26 |

**Hallazgo crítico**: Qwen 3.5 cloud rinde +1.52 puntos por encima de su score global cuando se le da tools. Esto explica por qué muchos pipelines en producción que usan Qwen + tools funcionan mejor de lo que el ranking single-turn predice.

Bottom 5 en tool_calling:

| Modelo | Score tool_calling | Notas |
|---|---|---|
| Llama 4 Maverick | 6.08 | Sin Groq direct; ranking mediocre por provider |
| Nemotron 3 Super | 6.13 | El modelo grande de NVIDIA falla aquí |
| Step 3.5 Flash (NIM) | 6.29 | Bottom del Lote 9 NIM |
| Kimi K2.6 | 6.35 | Thinking model malgasta tokens en razonamiento de la tool |
| Devstral Medium | 6.58 | Inferior a Devstral Small en este eje |

**Patrón**: **modelos thinking saturan la atención en el reasoning interno y pierden precisión en la sintaxis JSON de tool_calls**. Si tu pipeline depende de tools, evita thinking models a menos que tengas evidencia específica de su tool_calling.

### 4.2 Structured output — tamaño del modelo NO predice mejor JSON

Bottom 8 en suite `structured_output`:

| Modelo | Score | Tamaño |
|---|---|---|
| Qwen 3.5 (Ollama Cloud) | 6.58 | 397B+ |
| Gemini 3.1 Pro | 6.59 | "Pro" tier |
| Step 3.5 Flash (NIM) | 6.62 | mid |
| Qwen 3.6 Plus | 6.69 | propietario tier-Plus |
| Ministral 14B (NIM) | 6.71 | 14B |
| Qwen 3.5 397B (Ollama Cloud) | 6.82 | 397B |
| DeepSeek V4 Pro | 6.82 | flagship razonador |
| Nemotron Super 49B v1.5 (NIM) | 6.83 | 49B |

**Patrón**: **modelos thinking + modelos gigantes son los peores para structured output**. Razón: el reasoning escapa del schema (pone explicaciones antes/después del JSON) y el modelo grande "elabora" cuando el prompt pide brevedad estructurada. Para JSON estricto en producción usa Llama 3.1 8B (Groq, 8.00) o GPT-OSS 20B (7.85).

### 4.3 Agent_capabilities — la suite más frágil

`agent_capabilities` mide multi-step planning + tool selection + JSON Schema obedience en escenarios de agente real. Es la suite más volátil.

Top 5:

| Modelo | Score |
|---|---|
| Llama 3.1 8B Instant (Groq) | 7.78 |
| Mistral Small 4 | 7.76 |
| Llama 3.3 70B (Groq) | 7.67 |
| Grok 4.1 Fast | 7.39 |
| Qwen 3.5 397B (NIM) | 7.32 |

Bottom 5 (excluyendo el cero por incomplitud):

| Modelo | Score | Notas |
|---|---|---|
| Devstral 2 123B (NIM) | 0.00 | Solo 0 runs en esta suite — incompleto, NO confiar |
| Nemotron 3 Super | 4.83 | El modelo grande de NVIDIA es deficiente como agente |
| Qwen 3.6 Plus | 5.27 | Propietario API-only tier-Plus |
| Kimi K2 Thinking (NIM) | 5.35 | Thinking penaliza agent_capabilities también |
| Nemotron 3 Nano 30B | 5.40 | Bueno general, mediocre como agente |

**Hallazgo**: la diferencia entre el #1 (Llama 3.1 8B, 7.78) y la mediana (~6.3) es de 1.5 puntos, **mucho mayor que en otras suites**. Para producción de agentes, elegir bien acá es 3× más importante que en contenido.

---

## 5. Sensibilidad por idioma — español vs inglés

La suite `translation` tiene tests bidireccionales ES↔EN sobre vocabulario técnico, jerga startup y modismos chilenos/mexicanos. El juez Phi-4 fue instrumentado con rúbrica en español neutro.

### 5.1 Top 8 en translation

| Modelo | Score translation | Score global | Delta |
|---|---|---|---|
| GPT-OSS 20B (Groq) | 8.04 | 7.53 | +0.51 |
| Llama 3.3 70B (Groq) | 8.03 | 7.64 | +0.39 |
| Llama 3.1 8B Instant | 8.00 | 7.66 | +0.34 |
| Mistral Small 4 | 7.87 | 7.54 | +0.33 |
| Devstral Small | 7.87 | 7.35 | +0.52 |
| Gemini 3.1 Flash Lite | 7.85 | 7.50 | +0.35 |
| Gemini 2.5 Flash Lite | 7.84 | 7.12 | +0.72 |
| GPT-OSS 120B (Ollama Cloud) | 7.79 | 7.41 | +0.38 |

**Patrón**: los modelos del top 5 traducen **mejor** que su score global. Los GPT-OSS son particularmente fuertes en español neutro. Esto es relevante para LATAM porque la mayoría del entrenamiento web tiene sesgo a inglés — los modelos que sobre-rinden en translation son los menos propensos a producir "spanglish" o anglicismos forzados.

### 5.2 Bottom 8 en translation

| Modelo | Score translation | Notas |
|---|---|---|
| Qwen 3.5 397B (Ollama Cloud) | 5.17 | Mete chino-en-español ocasional, penalizado por la rúbrica |
| Kimi K2 Thinking (NIM) | 5.73 | Modelo chino + thinking → contamina output |
| DeepSeek V4 Pro | 6.03 | Razonador chino, mismo patrón |
| Kimi K2.5 / K2.5 NIM | 6.06 | Idem |
| Step 3.5 Flash (NIM) | 6.10 | Modelo chino, suite bottom |
| Qwen 3.5 default Ollama | 6.12 | Mejor que la versión 397B en este eje |
| Qwen 3-Next 80B Thinking | 6.33 | Thinking penaliza |

**Hallazgo crítico**: 7 de los 8 peores en translation son **modelos chinos** (Qwen, Kimi, Step, DeepSeek). El benchmark detecta el patrón conocido: estos modelos a veces meten caracteres chinos en mid-output cuando el prompt es ambiguo o muy largo. La penalización por idioma del scoring v2 los empuja al bottom.

**Implicación**: si tu pipeline genera contenido público en español neutro (blogs, artículos, copy), los modelos chinos requieren validación extra de output. Para flujos que aceptan revisión humana, no es bloqueante. Para automatización end-to-end, es riesgo.

### 5.3 La excepción Llama (made-in-USA, gana en español)

Los 3 Groq-Llama (3.1, 3.3, 4 Scout) son top 3 en translation con scores 8.00-8.04. **Modelos USA con buen multi-lingual training rinden bien en español neutro de LATAM**. No es paradoja: Meta entrenó Llama con un balance multi-lingüe explícito; Llama 3.3 cubre 8+ idiomas en datos públicos.

---

## 6. Costo real para el emprendedor N8N — ranking mensual y Pareto

Asunción: **10,000 calls/mes** (1k input + 1.5k output tokens por call promedio). Esto modela un blog de actualidad startups con generación moderada, atención al cliente automatizada de bajo volumen, o un agente N8N de 30-40 ejecuciones diarias.

### 6.1 Costos mensuales — los 12 más baratos

| Modelo | Costo $/mes | Score | tok/s | Apto para producción |
|---|---|---|---|---|
| GPT-OSS 120B (Ollama Cloud) | $0.00 | 7.41 | 75 | sí (suscripción Ollama Cloud) |
| Gemma 4 31B (NIM) | $0.00 | 7.20 | 23 | sí (cap 40 RPM) |
| Qwen 3-Next 80B Instruct (NIM) | $0.00 | 7.17 | 52 | sí |
| Devstral 2 123B (NIM) | $0.00 | 7.12 | 42 | sí (parcial: 68 runs) |
| DeepSeek V4 Flash (NIM) | $0.00 | 7.07 | 25 | sí |
| Qwen 3.5 397B (NIM) | $0.00 | 7.02 | 20 | sí |
| Nemotron Nano 9B v2 (NIM) | $0.00 | 6.91 | varies | sí |
| MiMo V2.5 (Xiaomi) | $1.30 | 7.32 | 79 | sí ($14/mes flat fee) |
| MiMo V2-Pro (Xiaomi) | $1.30 | 7.13 | 45 | sí |
| Llama 3.1 8B Instant (Groq) | $1.40 | 7.66 | 368 | sí |
| MiMo V2.5-Pro (Xiaomi) | $2.50 | 7.26 | 50 | sí |
| Nemotron 3 Nano 30B | $3.20 | 7.20 | 88 | sí |

**Observación**: para 10k calls/mes, **6 modelos gratis y 6 más bajo $5/mes** dan score >7.0. Cualquier emprendedor latinoamericano puede operar con presupuesto cercano a $0 en cuotas de modelo si tiene OpenClaw o Ollama Cloud.

### 6.2 Costos mensuales — los 5 más caros

| Modelo | Costo $/mes | Score | Vale la pena? |
|---|---|---|---|
| Claude Opus 4.7 | $1,170 | 7.16 | No vs Llama 4 Scout 7.67 a $5.40/mes |
| Claude Opus 4.6 | $1,170 | 7.04 | No |
| GPT-5.5 | $465 | 6.44 | No |
| GPT-5.4 | $240 | 6.90 | No |
| Claude Sonnet 4.6 | $234 | 6.99 | No |

**Diferencial extremo**: Claude Opus 4.7 cuesta **$1,170/mes** para entregar 7.16 — un score que Mistral Small 4 entrega por $9.40/mes (124× más barato). Para emprendedores, los modelos premium API son operativamente inaccesibles vs alternativas open.

### 6.3 Pareto de costo-eficiencia

Recomendación operativa para 4 perfiles:

- **Bootstrap ($0/mes)**: GPT-OSS 120B (Ollama Cloud, score 7.41) o NIM Gemma 4 31B (7.20). Cero costo recurrente, tope ~25 calls/min.
- **Microemprendimiento ($1-5/mes)**: Llama 3.1 8B Instant (Groq, $1.40, score 7.66, 368 tok/s). Es la mejor opción Pareto absoluta.
- **PYME ($10-30/mes)**: Llama 4 Scout 17B (Groq, $5.40, 7.67), Mistral Small 4 ($9.40, 7.54), o GPT-OSS 20B (Groq, $4.70, 7.53).
- **Volumen alto + multi-tarea ($30-100/mes)**: Llama 3.3 70B Groq ($13.60, 7.64) + Devstral Small ($4.80, 7.35) en pipeline.

---

## 7. Regresiones — cuando la versión nueva es peor

Comparativas v2.4 entre versión anterior y nueva del mismo modelo:

| Anterior | Score | Nueva | Score | Δ |
|---|---|---|---|---|
| GPT-4.1 | 7.23 | GPT-5.5 | 6.44 | **−0.79** |
| Qwen 3-Next 80B Instruct | 7.17 | Qwen 3-Next 80B Thinking | 6.41 | **−0.76** |
| Devstral Small | 7.35 | Devstral 2 (Dic 2025) | 7.22 | −0.13 |
| GLM 5 (NIM) | 6.87 | GLM 5.1 (NIM) | 6.79 | −0.08 |
| Gemini 2.5 Pro | 6.47 | Gemini 3.1 Pro | 6.41 | −0.06 |
| **Avances reales:** | | | | |
| Gemini 2.5 Flash | 7.19 | Gemini 3.1 Flash Lite | 7.50 | +0.31 |
| MiMo V2-Pro | 7.13 | MiMo V2.5-Pro | 7.26 | +0.13 |
| Kimi K2.5 | 6.27 | Kimi K2.6 | 6.51 | +0.24 |
| Qwen 3.5 397B (Ollama Cloud) | 6.72 | Qwen 3.5 397B (NIM) | 7.02 | +0.30 (provider, no modelo) |

**Hallazgo regresión 1 — GPT-5.5 vs GPT-4.1 (−0.79)**: la regresión más severa del benchmark. GPT-5.5 cuesta $46.50/1k calls vs GPT-4.1 a $12.60. El usuario paga 4× más por un score 11% peor. Diagnóstico probable: GPT-5.5 es thinking-by-default y consume budget en reasoning interno antes de responder, agotando max_tokens en prompts complejos.

**Hallazgo regresión 2 — Qwen 3-Next Thinking vs Instruct (−0.76)**: el modelo razonador es **estrictamente peor** que el instruct en single-turn. Por pilar: Razonamiento −0.78, Coding −0.44, Contenido −0.79, Agentes −0.95. **Penalización generalizada**, no solo en suites donde "no se necesita razonar". Esto desafía la intuición — la versión thinking del mismo modelo agrega complejidad sin valor en single-turn.

**Hallazgo regresión 3 — Gemini Pro tier estancado (−0.06)**: Gemini 3.1 Pro (6.41) ≈ Gemini 2.5 Pro (6.47). El upgrade Pro→Pro no aporta. En cambio, Flash Lite mejoró +0.31 (7.19→7.50). **Google está mejorando su tier económico mientras el premium se estanca**.

**Hallazgo regresión 4 — Devstral Small > Devstral 2 (−0.13)**: el "Devstral 2" lanzado en diciembre 2025 (123B) saca 7.22 contra 7.35 del Small original (24B). El modelo más grande es marginalmente peor. Probable razón: el Small está más afinado en string_precision (8.12 vs 7.29 del 2) y eso pesa en su score global.

**Conclusión patrón**: **3 de 5 regresiones son thinking models o tier "Pro" que reemplazan no-thinking** (GPT-4.1→5.5, Qwen Instruct→Thinking, Gemini Pro→Pro). El thinking by default es un anti-pattern para single-turn. Los avances reales vienen del tier Flash Lite / variantes Mini.

---

## 8. Open-source vs propietario — ¿se cerró la brecha?

### 8.1 Promedios

| Categoría | n | Score promedio | Score top |
|---|---|---|---|
| Open-source | 44 | **6.98** | 7.67 (Llama 4 Scout) |
| Propietario | 24 | 6.97 | 7.50 (Gemini 3.1 Flash Lite) |

**Hallazgo**: la diferencia es **0.01 puntos** — virtualmente cero. El **top open-source supera al top propietario** por +0.17 puntos (Llama 4 Scout > Gemini 3.1 Flash Lite). En distribución completa, open-source está al menos en paridad.

### 8.2 Por pilar — top open vs top closed

| Pilar | Top Open | Score | Top Closed | Score | Δ |
|---|---|---|---|---|---|
| Razonamiento | Llama 4 Scout 17B | 7.80 | Gemini 3.1 Flash Lite | 7.55 | +0.25 |
| Coding | Llama 4 Scout 17B | 7.70 | GPT-4.1 | 7.59 | +0.11 |
| Contenido | GPT-OSS 20B (Groq) | 7.87 | Gemini 3.1 Flash Lite | 7.62 | +0.25 |
| Agentes | Llama 3.1 8B Instant | 7.70 | Grok 4.1 Fast | 7.50 | +0.20 |

**En los 4 pilares el top open-source supera al top propietario**. En 2024 esto no era el caso — la brecha era de 0.5+ puntos a favor de Claude/GPT. En abril 2026, **la brecha se cerró y se invirtió** a favor de open-source en single-turn.

### 8.3 Caveat importante

El propietario top en este benchmark es Gemini 3.1 Flash Lite (no Claude Opus o GPT-5). La razón es que **los flagship propietarios son thinking-by-default y eso los penaliza en single-turn corto**. En tareas multi-turn complejas con tool use intensivo (no medidas por este benchmark), Claude Opus probablemente sigue dominando. Pero para 80% de casos del emprendedor LATAM (atención al cliente, blog, copy, traducción), **open-source ya empató o superó a propietario**.

### 8.4 Open-source que vale considerar

Top 10 open-source globales:

| # | Modelo | Score | $/1k | License |
|---|---|---|---|---|
| 1 | Llama 4 Scout 17B | 7.67 | 0.54 | Llama Community |
| 2 | Llama 3.1 8B Instant | 7.66 | 0.14 | Llama Community |
| 3 | Llama 3.3 70B | 7.64 | 1.36 | Llama Community |
| 4 | Mistral Small 4 | 7.54 | 0.94 | Mistral Research |
| 5 | GPT-OSS 20B | 7.53 | 0.47 | OpenAI MIT |
| 6 | GPT-OSS 120B (Ollama Cloud) | 7.41 | 0.00 | OpenAI MIT |
| 7 | Devstral Small | 7.35 | 0.48 | Apache 2.0 |
| 8 | Hermes 4 70B | 7.24 | 0.64 | Llama Community |
| 9 | Devstral 2 (Dic 2025) | 7.22 | 3.12 | Apache 2.0 |
| 10 | Gemma 4 31B | 7.20 | 0.99 | Gemma License |

---

## 9. Anti-patterns del marketing — claims que no se sostienen

Cinco claims comunes en el marketing de modelos AI 2025-2026 que la data del benchmark no respalda:

### 9.1 "Más parámetros = mejor"

Mistral Large 3 (675B params) saca 6.89. Nemotron Nano 9B v2 saca 6.91. **Modelo 75× más pequeño gana por 0.02 puntos**. Llama 3.1 8B saca 7.66 — más alto que casi cualquier modelo 100B+ del benchmark excepto Llama 4 Scout (que es MoE 17B activos / 109B total).

### 9.2 "Thinking by default es mejor"

GPT-5.5, Qwen 3-Next Thinking, Kimi K2.5/K2.6, DeepSeek V4 Pro — **todos los thinking models perdieron contra sus pares non-thinking del mismo proveedor en single-turn**. El thinking aporta cuando hay tools y multi-turn, no en respuestas únicas.

### 9.3 "Premium tier vale el costo"

Claude Opus 4.7 ($117/1k calls) saca 7.16. Llama 4 Scout ($0.54/1k) saca 7.67. **El gap es +0.51 a favor del barato, a 217× menos costo**. Lo mismo aplica a Gemini Pro vs Flash Lite y GPT-5.5 vs GPT-4.1.

### 9.4 "Modelos chinos son la nueva frontera"

Qwen, Kimi, DeepSeek, GLM, Step — **6 de los 10 peores en translation (español neutro) son chinos**. En tareas que requieren español puro sin contaminación de caracteres, es riesgo en producción. Mejoraron en razonamiento puro y código, pero el español público requiere validación humana.

### 9.5 "Modelos multimodales superan a single-modal"

MiMo V2-Omni multimodal saca 6.96. MiMo V2.5 (texto only) saca 7.32. **Misma familia, multimodal pierde 0.36 puntos** en single-turn de texto. Los multimodales tienen capacidad extra (visión, audio) que es valiosa en su nicho — pero diluyen score textual. Si tu producto es 100% texto, no pagues por multimodal.

---

## 10. Top 3 hallazgos sorpresivos del v2.4

### 10.1 NIM gratis ≈ OpenRouter pagado en el mismo modelo

La paridad exacta de Gemma 4 31B (7.20 NIM = 7.20 OpenRouter) y Kimi K2.5 (6.27 NIM = 6.27 OpenRouter) confirma que NVIDIA NIM gratis no degrada el modelo. Para 47 modelos del catálogo NIM con equivalente OpenRouter, **pagar OpenRouter es opcional** — solo justificable si necesitas >40 RPM o features específicos del routing.

Implicación: el ecosistema cambió. NVIDIA está subsidiando inference para incentivar adopción de NIM. Como emprendedor, **migrar pipelines a NIM gratis para volúmenes <40 RPM es ROI inmediato**. Recordar: el cap es por tier de cuenta NIM y se aplica a todos los modelos juntos.

### 10.2 Modelos thinking pierden vs sus pares Instruct en TODOS los pilares

Qwen 3-Next 80B: Instruct 7.17 vs Thinking 6.41 = **−0.76 puntos**. Por pilar: Razonamiento −0.78, Coding −0.44, Contenido −0.79, Agentes −0.95.

Esto NO es: "thinking sirve para razonamiento, no para contenido". Es: **en single-turn, thinking pierde en todo, incluido razonamiento puro**. La hipótesis es que el thinking consume budget de output (tokens facturados como reasoning) y el modelo retorna respuestas más cortas o truncadas. Para producción single-turn, **siempre elegir variante Instruct cuando exista**.

La excepción son tareas multi-turn con tools donde el reasoning intermedio agrega valor — pero el benchmark no las mide directamente.

### 10.3 9B parámetros derrotan a 675B en producción real

Nemotron Nano 9B v2 (NIM, 6.91 global) **lidera startup_content y policy_adherence** del Lote 9 NIM por encima de Mistral Large 3 (675B, 6.89 global). 75× menos parámetros, mejor performance en suites específicas.

Esto contradice la intuición de "modelo más grande = mejor". Lo que mide el benchmark es **balance de capacidades** + **cumplimiento de instrucciones precisas**. Modelos pequeños bien afinados (Nemotron Nano 9B, Llama 3.1 8B) tienen menos espacio para "elaborar" cuando el prompt pide brevedad — y eso correlaciona con mejor score automatizado.

Implicación operativa: para producción de contenido o flujos N8N donde la respuesta es estructurada y corta, **el modelo de 8-30B parámetros es la elección óptima**. Los flagship 100B+ son útiles para razonamiento abierto, no para automatización repetitiva.

---

## 11. Implicaciones para la próxima iteración

### 11.1 Suites pendientes de robustecer

1. **agent_capabilities** — la suite más volátil (rango 4.83 a 7.78 = 2.95 puntos). Necesita más tests para discriminar finos en el tier 7.0+. Hoy el ranking acá es ruidoso.
2. **tool_calling** — falta cobertura en tools complejas (>3 funciones, anidadas). El benchmark actual privilegia un patrón simple que casi todos los modelos modernos manejan.
3. **multi_turn** — la suite es chica (10 tests). Para evaluar producción real con conversación, necesita 3× más cobertura.

### 11.2 Modelos que faltan medir o re-medir

1. **DeepSeek V4 Pro vía Ollama Cloud o provider directo** — 69 runs en NIM con 88 timeouts = ranking actual no-confiable.
2. **Devstral 2 123B (NIM)** — 68 runs vs los 91 esperados. Suite agent_capabilities tiene 0 runs registrados, eso baja el rank artificialmente.
3. **Magistral Small (Mistral)** — bloqueado en NIM por error 400. Probar en Mistral direct.
4. **Llama 4 Maverick** — pendiente de migrar a Groq (hoy en OpenRouter con 7.03). Esperable +0.5 si va a Groq.
5. **Gemini 3.1 Flash** (no Lite) — está pendiente, podría estar entre Flash Lite (7.50) y Pro (6.41).

### 11.3 Métricas a agregar al pipeline

1. **Cost-per-quality-point**: $/1k calls dividido por (score - 5.0). Mide cuánto cuesta cada punto de score sobre el baseline. Útil para Pareto operativo.
2. **Latency p95**: hoy guardamos avg, pero p95 importa más para producción real (un timeout en el percentil alto rompe UX).
3. **Variance entre runs**: misma pregunta, 5 ejecuciones. Modelos con alta varianza son riesgo en producción aunque su mean score sea alto.

### 11.4 Áreas de cobertura que faltan

1. **OCR + visión** (suites: ocr_extraction está, falta visión pura). Solo MiMo V2-Omni y Gemma 4 son medidos como multimodales.
2. **Audio TTS** — Xiaomi MiMo V2.5-TTS está en el catálogo pero no se ha probado.
3. **Mantenimiento de contexto largo** (>32k tokens). El benchmark actual usa prompts <4k. Para casos como análisis de documentos legales o transcripciones, hace falta una suite específica.

---

## 12. Datos sospechosos / a re-validar

Casos donde la data parece anómala y conviene re-correr antes de publicar conclusiones fuertes:

### 12.1 Devstral 2 123B (NIM) — agent_capabilities = 0.00

El modelo tiene 68 runs totales pero la suite `agent_capabilities` registra 0.00 score. Posibles causas: 1) la suite no se corrió completamente por timeouts, 2) el modelo retorna respuestas vacías en esa suite específica. **Hay que re-correr solo agent_capabilities con más timeout** antes de aceptar el ranking 7.12 final.

### 12.2 GPT-5.5 score 6.44 — caída masiva vs GPT-4.1

GPT-5.5 cuesta 4× más que GPT-4.1 y entrega 11% menos score. Si bien la regresión es plausible (thinking-by-default + max_tokens insuficiente), conviene re-correr con `max_tokens × 4 = 8192` explícito para confirmar que no estamos truncando outputs. **Actualmente el adapter ya hace esto** — pero re-validar con runs frescos es prudente.

### 12.3 Llama 4 Maverick — score 7.03 vs los Llama Groq en 7.6+

Maverick está en OpenRouter (no Groq direct) y rinde mucho peor que su par Llama 4 Scout en Groq (7.67). La diferencia de +0.64 entre los dos modelos Llama 4 es enorme y se explica casi totalmente por provider. Re-medir Maverick en Groq sería el test crítico.

### 12.4 Qwen 3.5 397B (Ollama Cloud) — translation 5.17

El score más bajo del benchmark en cualquier suite individual. Podría ser:
1. Bug del adapter Ollama Cloud — alguna config rechaza español.
2. La cuantización específica de Ollama Cloud (no documentada, probablemente Q4 o Q5) degrada el español más que en otros modelos.
3. Genuina contaminación de chino en español en el modelo cloud.

Re-correr 5 prompts en español puro y comparar con NIM (mismo modelo, score 7.02 global) clarifica.

### 12.5 Gemma 4 31B con NIM y OpenRouter idénticos a 4 decimales

7.20 vs 7.20 es plausible — modelos FP16 son determinísticos a temperature=0 — pero a temperature=0.7 (default del benchmark) la coincidencia exacta a 2 decimales requiere que ambos providers estén servidor el mismo build. Vale auditar 1-2 runs lado-a-lado para confirmar y descartar caché compartida.

### 12.6 MiMo Xiaomi — pricing es ambiguo

Reportamos costos $0.13-0.46/1k calls para los MiMo, pero el modelo de Xiaomi es **suscripción flat** ($14/mes con cap de tokens off-peak 0.8x). El cálculo $/1k assume token-by-token pricing extrapolado. Si el usuario satura el cap mensual, el costo por call efectivo sube. **El ranking de MiMo asume volumen moderado** — para volumen alto requiere recálculo.

---

## Anexo A — Cómo leer este benchmark

- **Score global**: media simple de 91 tests con peso igual. Cada test combina criterio automatizado (40%) + LLM-as-Judge Phi-4 (60%, escala 0-5 multiplicada por 2 = 0-10).
- **Score by pillar**: 23 suites agrupadas en 4 pilares (Razonamiento, Coding, Contenido, Agentes). Score por pilar es media de las suites del pilar.
- **Cost per 1k calls**: asume 300 tokens input + 1500 tokens output por call. Es el costo de procesar 1000 requests bajo este perfil.
- **Tokens per second**: media de output_tokens / latency_total a través de los 91 tests. No incluye latencia de red de Chile a USA.
- **Provider matters**: el mismo modelo puede tener score, latencia y costo distintos según provider. Comparar provider explícito es obligatorio antes de elegir.

## Anexo B — Reproducir el análisis

```bash
.venv/bin/python -c "
import json
from scipy.stats import spearmanr
with open('docs/data/models.json') as f:
    data = json.load(f)
tested = [m for m in data['models'] if m['tested'] and m['runs'] >= 50]
paid = [m for m in tested if m['cost_per_1k_calls_usd'] > 0]
costs = [m['cost_per_1k_calls_usd'] for m in paid]
scores = [m['score_global'] for m in paid]
print(spearmanr(costs, scores))
"
```

Salida esperada: `SignificanceResult(statistic=-0.460, pvalue=0.001)`.

Este script confirma la sección 1 del análisis. Cualquier persona puede re-correrlo con `docs/data/models.json` actualizado para validar los hallazgos.

---

**Última actualización**: 29 de abril de 2026 — v2.4 (post-Lote 9 NIM + DGX Spark Lote 1).
**Próxima revisión**: tras Lote 10 o cualquier nuevo proveedor mayor.
**Auto-regenerable**: este documento se reescribe completo desde `docs/data/models.json` con un agente data-scientist. No editar manualmente — los cambios se perderán en la próxima regeneración.
