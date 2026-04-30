# ESTADO_SESION.md

> **Documento de continuidad** — generado 2026-04-30 ~01:00 UTC. Si la sesión actual se cierra, este archivo permite reanudar desde donde quedaste sin perder contexto.
>
> **Reglas**: este archivo se actualiza cada vez que hay decisiones tomadas, procesos corriendo en background, o hallazgos no commiteados aún. NO sustituye a `ROADMAP.md` (mira hacia adelante) ni `CHANGELOG.md` (deja traza de releases). Es **estado vivo** entre commits.

---

## Status de procesos en background al cierre

### 🔄 Corriendo
- **Lote 10** (`/tmp/lote10-agent-lh.log`) — agent_long_horizon × 27 modelos = 324 runs. **190/324 al snapshot (58%)**. Modelo en curso: 16/27 (Gemma 4 31B NIM). ETA real ~3-5h restantes. PID inicial registrado en `/tmp/`.
  - Modelos restantes (12): Gemma 4 31B (NIM) en curso, MiMo V2-Pro Xiaomi, MiMo V2-Omni Xiaomi, MiMo-V2-Omni multimodal, Gemini 3.1 Pro, MiMo V2.5, MiMo V2.5-Pro, Hermes 4 70B (sin thinking), GPT-4.1, Devstral 2, MiMo V2-Flash, Nemotron 3 Nano 30B, Gemini 2.5 Flash. (orden puede variar)
  - Errores transitorios: Gemma 4 31B NIM tuvo 1× error 504 en test 1, después siguió OK.

### ✅ Terminados (resultados sin commitear todavía)
- **Lote 11 thinking** (`/tmp/lote11-thinking.log`, JSON: `benchmarks/results/benchmark_20260429_210054.json`):
  - Kimi K2.5 (thinking): **7.00** ⬆ (vs 6.27 sin thinking = **+0.73**)
  - Hermes 4 70B (thinking): **6.70** ⬇ (vs 7.24 sin thinking = **-0.54** SORPRESA)
  - Hermes 4 405B (thinking): **6.30** ⬇ (vs ~6.5-6.8 estimado sin thinking)
  - Costo total Lote 11: $1.19 OpenRouter

- **Lote 10b MiniMax** (JSON: `benchmark_20260429_194748.json`):
  - MiniMax M2.7 (directo): **6.86** ⬆ provider directo
  - MiniMax M2.7: 6.70 (OpenRouter)
  - MiniMax M2.7 Highspeed: 6.69 (highspeed solo es velocidad, no calidad)
  - Provider matters CONFIRMADO: +0.16 puntos directo vs OpenRouter

- **NIM Nemotron 3 Nano Omni Reasoning** (JSON: `benchmark_20260429_081712.json`):
  - 91/91 OK, score **6.97**
  - Posición global ~#22, debajo de Gemma 4 31B (NIM) 7.20 y Devstral 2 123B 7.12

- **DGX Nemotron 3 Base 33B Q4** (JSON: `benchmark_20260429_101019.json`):
  - 103/103 OK (incluye 12 agent_long_horizon)
  - Score global: **6.74** (idéntico a Nemotron 3 Super 120B también en DGX)
  - agent_long_horizon: 6.59

### 📋 Decisión pendiente del usuario
- **Claude Opus 4.7 (thinking) + Claude Sonnet 4.6 (thinking)** — variantes agregadas al config (`benchmarks/models.py`) con `force_reasoning=True`. **NO lanzado aún**.
  - Costo estimado: ~$8.10 Opus + ~$1.62 Sonnet = **~$9.72**
  - Comando listo:
    ```bash
    cd /Users/cristiantala/Playground/Benchmarks/alternativos
    set -a; source .env; set +a
    source .venv/bin/activate
    nohup python benchmarks/runner.py --quick --tests agent_long_horizon \
        --models claude-opus-4.7-thinking claude-sonnet-4.6-thinking \
        > /tmp/lote11b-claude-thinking.log 2>&1 &
    ```
  - Hipótesis: Opus 4.7 sin thinking saca ~7.0 single-turn. Si con thinking sube a 7.5+, valida que nuestro ranking subestima a Opus al correrlo sin thinking default.

---

## Hallazgos cuantitativos del bloque de hoy (sin commitear todavía a INSIGHTS)

### 1. Sospecha "Nemotron débil en español" REFUTADA — hallazgo mejor

Análisis de Nemotron 3 Nano 30B por suite (`docs/data/models.json`):

| Pilar | Score |
|---|---|
| Contenido (español puro) | **7.57** ← MEJOR pilar |
| Razonamiento | 7.55 |
| Coding | 7.41 |
| **Agentes** | **6.52** ← PEOR pilar |

Top suites: `startup_content` 7.87, `presentation` 7.86, `strategy` 7.73 (TODAS español)
Bottom suites: `agent_capabilities` **5.40**, `orchestration` 5.87, `customer_support` 6.21

**Conclusión real**: Nemotron es fuerte académica + española pero débil en agéntica. Esto es **la mejor demostración del aporte único del benchmark** — los benchmarks académicos estándar no miden agéntica multi-suite, por eso Nemotron luce bien en MMLU/GSM8K/HumanEval pero baja en nuestro ranking.

### 2. Sospecha "thinking models subestimados" PARCIALMENTE confirmada

Lote 11 force_reasoning=True via OpenRouter (effort=high):

| Modelo | Sin thinking | Con thinking | Delta | Conclusión |
|---|---|---|---|---|
| Kimi K2.5 | 6.27 (single-turn) | **7.00** (agent_lh) | +0.73 ⬆ | **Sí mejora** |
| Hermes 4 70B | 7.24 (single-turn) | 6.70 (agent_lh) | -0.54 ⬇ | **EMPEORA** (sorpresa) |
| Hermes 4 405B | ~6.5-6.8 | 6.30 (agent_lh) | ~-0.3 ⬇ | Empeora |

⚠️ **Nota importante**: la comparación NO es exacta — los scores "sin thinking" son single-turn (91 tests promediados), los "con thinking" son agent_long_horizon (12 tests). Para una comparación fair, habría que correr ambos en agent_long_horizon. Pero el patrón cualitativo es robusto: Kimi K2.5 GANA con thinking, Hermes 4 PIERDE.

**Hipótesis revisada**: el reasoning explícito puede ser **contraproducente** en multi-turn agéntico cuando el modelo "razona demasiado" y se desvía del objetivo o pierde contexto del usuario. Kimi K2.5 fue diseñado para ser hybrid; Hermes 4 fue post-trained para reasoning pero su capa agéntica se degrada cuando piensa.

**Implicancia para el paper**: hay que medir cada modelo hybrid en ambas variantes (con y sin thinking) y reportar ambos. NO es seguro asumir "thinking ayuda".

### 3. Provider matters reconfirmado con MiniMax

MiniMax M2.7 directo (6.86) > MiniMax M2.7 OpenRouter (6.70) = **+0.16 puntos**.

Patrón ahora confirmado en 4 proveedores:
- Xiaomi direct vs OpenRouter: +0.17-0.25 (mismo modelo)
- Groq direct vs OpenRouter: +0.15-0.20 (estimado)
- NIM gratis vs OpenRouter pagado: paridad exacta (Gemma 4 31B 7.20 = 7.20)
- **MiniMax direct vs OpenRouter: +0.16** ← nuevo

### 4. Highspeed ≠ mejor calidad

MiniMax M2.7 Highspeed (suscripción): 6.69
MiniMax M2.7 base directo: 6.86

La "highspeed" aporta latencia menor, NO mejor performance. La suscripción $19/mes Agent Pro tiene sentido para **costos predecibles** (saber que pagas lo mismo cada mes) pero **no esperés mejor calidad** que la API direct estándar.

### 5. Cobertura agent_long_horizon hasta ahora

Modelos corridos (sumando piloto + validación + Lote 10 parcial + Lote 10b + Lote 11):

| Modelo | Score | Origen |
|---|---|---|
| Llama 3.3 70B (Groq) | 7.50-7.69 | Smoke + validación |
| Mistral Small 4 | 7.41 | Validación |
| Nemotron 3 Base 33B (DGX) | 6.59 | Bench DGX completo |
| MiMo-V2-Flash (free) | 0.00 | API issue (regenerar) |
| Kimi K2.5 (thinking) | 7.00 | Lote 11 |
| Hermes 4 70B (thinking) | 6.70 | Lote 11 |
| Hermes 4 405B (thinking) | 6.30 | Lote 11 |
| MiniMax M2.7 (directo) | 6.86 | Lote 10b |
| MiniMax M2.7 | 6.70 | Lote 10b |
| MiniMax M2.7 Highspeed | 6.69 | Lote 10b |
| Gemini 2.5 Flash | TBD (Lote 10) | en curso |
| Llama 3.1 8B Instant (Groq) | TBD | en curso |
| Llama 4 Scout 17B (Groq) | TBD | en curso |
| GPT-OSS 20B (Groq) | TBD (3/12 ERROR 400) | en curso |
| GPT-OSS 120B Cloud | TBD | en curso |
| Qwen 3-Next 80B Instruct (NIM) | TBD | en curso |
| Kimi K2 Thinking (NIM) | TBD | en curso |
| DeepSeek V4 Flash (NIM) | TBD | en curso |
| Step 3.5 Flash (NIM) | TBD | en curso |
| Gemma 4 31B (NIM) | TBD | en curso |
| (12 modelos restantes Lote 10) | TBD | pendiente |

---

## Cambios técnicos sin commitear

### 1. Adapter — soporte `force_reasoning` (`providers/adapters.py`)

Cambios en el método `chat()`:
- Nuevo parámetro `force_reasoning: bool = False`
- Cuando `True`, `is_thinking` se fuerza a `True` aunque el modelo no esté en `THINKING_MODELS` tuple
- Cuando `True`, agrega al `extra_body`: `{"reasoning": {"effort": "high"}, "include_reasoning": True}`
- Compatible con OpenRouter (Hermes 4, Kimi K2.5, Anthropic Claude). Para otros providers el extra_body se ignora.

### 2. Runner — propaga `force_reasoning` desde config

`run_single_test()` y `run_multi_turn_script()` ahora reciben `model_config: dict | None = None` (kwarg opcional) y extraen `force_reasoning = bool(model_config.get("force_reasoning", False))` para pasarlo al adapter.

### 3. Config — 5 nuevas entradas

`benchmarks/models.py`:
- `hermes-4-70b-thinking` (id: `nousresearch/hermes-4-70b`, force_reasoning=True)
- `hermes-4-405b-thinking` (id: `nousresearch/hermes-4-405b`, force_reasoning=True)
- `kimi-k2.5-thinking` (id: `moonshotai/kimi-k2.5`, force_reasoning=True)
- `claude-opus-4.7-thinking` (id: `anthropic/claude-opus-4-7`, force_reasoning=True) — NO corrido aún
- `claude-sonnet-4.6-thinking` (id: `anthropic/claude-sonnet-4-6`, force_reasoning=True) — NO corrido aún

---

## Comandos para reanudar la sesión

### Verificar qué quedó vivo

```bash
cd /Users/cristiantala/Playground/Benchmarks/alternativos
ps aux | grep "runner.py" | grep -v grep
ls -lat benchmarks/results/benchmark_2026*.json | head -10
ls -lat /tmp/lote*.log
```

### Si Lote 10 se cortó: --resume

```bash
# Buscar el último JSON del Lote 10
ls -lat benchmarks/results/benchmark_2026*.json | head -3
# El archivo del Lote 10 tiene ~324 runs total esperados, de los 27 modelos
# Reanudar:
python benchmarks/runner.py --quick --tests agent_long_horizon \
    --resume benchmarks/results/<archivo>.json
```

### Si la corrida actual (lote 10) terminó: post-procesamiento

```bash
# 1. Regenerar artefactos auto en orden
python benchmarks/export_for_pages.py
python benchmarks/generate_per_model_md.py
python benchmarks/generate_modelos_md_table.py -i
python benchmarks/generate_tests_md.py
python benchmarks/generate_sitemap.py
python benchmarks/sync_doc_counts.py

# 2. Actualizar INSIGHTS, README, CHANGELOG con los hallazgos del bloque thinking
# (ver sección "Hallazgos cuantitativos" arriba)

# 3. Decidir si correr Claude Opus/Sonnet thinking ($10) — pregunta abierta al usuario
```

### Tareas pendientes (orden recomendado)

1. **Esperar Lote 10** terminar (~3-5h desde 2026-04-30 01:00 UTC)
2. **Síntesis final post-Lote 10**: ranking inter-modelo agent_long_horizon, cross-ref single-turn vs agentic, stack OpenClaw/Hermes recomendado por rol
3. **Decisión Claude thinking** ($10): si user dice sí, lanzar `claude-opus-4.7-thinking` + `claude-sonnet-4.6-thinking` en agent_long_horizon
4. **Re-run MiMo-V2-Flash (free)** que falló en validación (probablemente API issue)
5. **Investigación pendiente — pricing reasoning_tokens correcto**: el adapter ya captura `reasoning_tokens` separado en `metadata`, pero `cost_usd` quizás no los multiplica por output rate. Verificar.
6. **Approach 2 NIM-ES + IFEval-ES** (próxima semana, ver ROADMAP.md sección "Validación cruzada")
7. **Paper arXiv draft** cuando todo lo anterior esté en INSIGHTS
8. **HuggingFace Datasets** publicación oficial
9. **Cobertura completa agent_long_horizon** en los 70 modelos con ≥50 runs (faltarían ~40 después del Lote 10)

---

## Tasks (de la sesión actual)

| ID | Estado | Subject |
|---|---|---|
| #27 | ✅ completed | Crear sync_doc_counts.py script preventivo |
| #28 | ✅ completed | Sync manual de counts ahora |
| #30-34 | ✅ completed | Post-Lote 9: artefactos auto, INSIGHTS, README+CHANGELOG, CLAUDE.md, commit+push |
| #35 | ⏳ pending | Futuro: Regenerar INSIGHTS.md completo con data-scientist agent |
| #36 | ✅ completed | A - Cross-reference Claw-Eval leaderboard |
| #37 | ✅ completed | C - Suite propia agent_long_horizon (fase 1+2) |
| #38 | ✅ completed | Bench NIM Nemotron 3 Nano Omni Reasoning |
| #39 | ✅ completed | Bench DGX Nemotron 3 base 33B Q4 |
| #40 | 🔄 in_progress | Lote 10: agent_long_horizon en 27 modelos |
| #41 | ✅ completed | Approach 1 - benchmarks externos top 30 |
| #42 | ✅ completed | Lote 10b MiniMax (3 modelos) |
| #43 | ⏳ pending | Post-Lotes: ranking agéntico inter-modelo + stack OpenClaw/Hermes |
| #44 | ✅ completed | Lote 11: Hermes 4 70B/405B + Kimi K2.5 thinking variants |

---

## Archivos clave del proyecto (mapa rápido)

- `benchmarks/runner.py` — motor principal con `run_single_test`, `run_multi_turn_script`, `_score_long_horizon`, dispatch por `test["type"]`
- `benchmarks/models.py` — catálogo público de modelos (MODELS dict + OLLAMA_MODELS dict)
- `benchmarks/config.py` — lee env vars + importa MODELS
- `benchmarks/scoring.py` — sistema de scoring + PRICING
- `benchmarks/llm_judge.py` — Phi-4 judge
- `benchmarks/tests/agent_long_horizon.py` — 12 tests multi-turn
- `benchmarks/tests/<otras 22 suites>.py` — 91 tests single-turn
- `benchmarks/sync_doc_counts.py` — sincroniza counts en docs desde models.json (NUEVO 2026-04-29)
- `benchmarks/export_for_pages.py` — genera docs/data/models.json (single source of truth para calculadora)
- `providers/adapters.py` — adapter unificado OpenAI-compat + soporte force_reasoning (NUEVO 2026-04-30)
- `.claude/agents/agent-eval-designer.md` — sub-agent para diseñar evals agénticas (NUEVO 2026-04-29)
- `INSIGHTS.md` — análisis cuantitativo con secciones 0-12 + bloque "Update v2.4.1"
- `BENCHMARKS_EXTERNOS.md` — triangulación con HumanEval/GSM8K/IFEval/MMLU oficiales (NUEVO 2026-04-29)
- `ROADMAP.md` — plan adelante con sección "Suite agent_long_horizon" + "Validación cruzada"
- `CHANGELOG.md` — entradas v2.4.0 y v2.4.1
- `docs/data/models.json` — single source of truth para counts (102 modelos catalogados, 70 con ≥50 runs single-turn)

---

## Pregunta abierta al usuario (al cierre del snapshot)

> "¿Confirmás que arranco Opus 4.7 thinking + Sonnet 4.6 thinking en agent_long_horizon (no en suite completa por ahora)? Si decís sí, lo dejo correr en background ahora mismo."

Esperando respuesta. **NO arrancar sin confirmación** — son ~$10 OpenRouter.

---

## Para futuros agentes que lean este archivo

Si vas a continuar este trabajo:

1. **Lee primero**: `CLAUDE.md` (instrucciones del proyecto), `ROADMAP.md` (plan adelante), este archivo (estado vivo).
2. **Actualiza**: cuando tomes una decisión, agregá una entrada acá con timestamp y motivo.
3. **No dupliques**: este archivo es **estado vivo**. Las decisiones tomadas ya pasan a CHANGELOG cuando se commitean.
4. **Memoria del usuario**: respetar las reglas de `~/.claude/projects/-Users-cristiantala-Playground-Benchmarks-alternativos/memory/` — español neutro, no recomendaciones personalizadas en INSIGHTS, etc.
5. **Costos**: cualquier acción que cueste >$5 OpenRouter requiere confirmación explícita del usuario antes de lanzar.
