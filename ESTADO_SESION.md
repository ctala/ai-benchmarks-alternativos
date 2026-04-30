# ESTADO_SESION.md

> **Documento de continuidad** — última actualización 2026-04-30 (cierre de sesión post-v2.4.2). Si la sesión actual se cierra, este archivo permite reanudar desde donde quedaste sin perder contexto.
>
> **Reglas**: este archivo se actualiza cada vez que hay decisiones tomadas, procesos corriendo en background, o hallazgos no commiteados aún. NO sustituye a `ROADMAP.md` (mira hacia adelante) ni `CHANGELOG.md` (deja traza de releases). Es **estado vivo** entre commits.

---

## ✅ Estado al cierre de v2.4.2 (30 abril 2026)

**Todo pusheado, sin procesos en background, repo en estado limpio**.

### Tags semver creados y pusheados

```
v2.4.0 → c7340ac (Lote 9 NIM + DGX Spark Lote 1)
v2.4.1 → 08ae7a9 (Nemotron Omni Reasoning + DGX Lote 2 + suite agent_long_horizon)
v2.4.2 → d62a4cb (scoring rebalanced + síntesis final, 30 abril 2026)
```

### Cobertura final v2.4.2

| Métrica | Valor |
|---|---|
| Modelos catalogados | **113** |
| Modelos con cualquier run | 87 |
| Modelos con ≥50 runs single-turn | **70** |
| Modelos con ≥9 runs en agent_long_horizon | **38** |
| Total runs preservados | **8,475** |
| Lotes consolidados | 18+ |

### Pesos default v2.4.2 (rebalanced)

```python
DEFAULT_WEIGHTS = {
    "quality": 0.50,
    "cost": 0.20,
    "tool_calling": 0.15,
    "speed": 0.075,
    "latency": 0.075,
}
```

(Eliminado `availability` hardcoded a 7.0 que no discriminaba.)

### Top 5 score compuesto (final)

1. Llama 4 Scout 17B (Groq) — **8.11**
2. Llama 3.1 8B Instant (Groq) — 8.11
3. Llama 3.3 70B (Groq) — 7.86
4. GPT-OSS 20B (Groq) — 7.84
5. Mistral Small 4 — 7.81

### Top 5 agent_long_horizon (multi-turn 8+ turnos)

1. **GPT-OSS 120B (Ollama Cloud)** — 8.15 ⭐ (gratis con sub)
2. Llama 4 Scout 17B (Groq) — 7.86
3. Llama 3.1 8B Instant (Groq) — 7.85
4. Devstral Small — 7.77
5. MiMo V2-Omni (Xiaomi direct) — 7.75

### Stack OpenClaw/Hermes recomendado (basado en datos)

| Rol | Modelo | Score |
|---|---|---|
| **Cabecera** (orquestador) | GPT-OSS 120B Cloud | 8.15 agéntico, gratis sub |
| **Coding** (workflows N8N, plugins) | Devstral Small | 7.77 agéntico, Apache 2.0 |
| **Content** (blog, social) | MiMo V2.5 Xiaomi sub | 7.65 agéntico, $14/mes |
| **Customer support multi-turn** | GPT-OSS 120B Cloud o Llama 3.3 70B | 8.15 / 7.60 |
| **Tool calling estructurado** | MiMo V2.5 (7.21 tools) | |
| **Multimodal** | MiMo V2-Omni Xiaomi direct | 7.75 |

### Hallazgos publicables (paper arXiv)

1. **Provider matters cuantificado**: +0.16-0.25 puntos directo vs OpenRouter (4 proveedores: Xiaomi, Groq, NIM, MiniMax)
2. **Thinking forzado EMPEORA multi-turn agéntico** en 8/9 modelos hybrid (única excepción Kimi K2.5 +0.73)
3. **Modelo gigante NO siempre gana**: Mistral Large 3 (675B) 6.89 < Nemotron Nano 9B v2 6.91
4. **Q4 cuantización cuesta -5%**: Gemma 4 31B FP16 7.20 vs Q4_K_M DGX 6.84
5. **Why Opus doesn't top our benchmark**: NO es sesgo del juez (Phi-4 da Opus 4.22 vs Llama 4.00) ni problema API. Es la fórmula compuesta (40-100x más caro, 5-10x más lento). VALIDA el aporte del benchmark.
6. **6 hipótesis cualitativas sobre Opus**: verbosity elaborada, meta-comentarios, JSON con prefijos, estilo asistente formal, posible saturación juez Phi-4, agent_capabilities no premia explicar antes de hacer.

---

## Documentos vigentes (mapa rápido)

### Raíz del proyecto

| Archivo | Estado | Última actualización |
|---|---|---|
| `README.md` | ✅ v2.4.2 | Top 10 nuevo + disclaimer score compuesto + columnas separadas |
| `INSIGHTS.md` | ✅ v2.4.2 | Sección "Why Opus doesn't top" + 6 hipótesis Opus + ranking inter-modelo + stack |
| `CHANGELOG.md` | ✅ v2.4.2 | Entrada completa con todos los cambios |
| `ROADMAP.md` | ✅ | Suite agent_long_horizon + validación cruzada + thinking variants |
| `THINKING_EXPLAINED.md` | ✅ | Doc nuevo: 3 tipos modelos + cómo medimos + hallazgos |
| `BENCHMARKS_EXTERNOS.md` | ✅ | Triangulación HumanEval/GSM8K/IFEval/MMLU |
| `MODELOS.md` | ✅ auto-gen | 69 modelos en tabla |
| `TESTS.md` | ✅ auto-gen | 91 tests en 23 suites |
| `ARQUITECTURA.md` | ✅ sync | Counts actualizados |
| `AGENTS.md` | ✅ sync | Counts actualizados |
| `CLAUDE.md` | ✅ | sync_doc_counts agregado paso 6 |

### Código

| Archivo | Estado | Cambios v2.4.2 |
|---|---|---|
| `providers/adapters.py` | ✅ | parámetro `force_reasoning` (effort=high vía OpenRouter) |
| `benchmarks/runner.py` | ✅ | propaga force_reasoning + dispatch multi_turn_script |
| `benchmarks/scoring.py` | ✅ | nueva fórmula `compute_final_score` + `cost_score_log` |
| `benchmarks/export_for_pages.py` | ✅ | recalcula final desde componentes raw + match estricto (id, name) |
| `benchmarks/sync_doc_counts.py` | ✅ | script preventivo de sincronización |
| `benchmarks/tests/agent_long_horizon.py` | ✅ | 12 tests multi-turno |
| `.claude/agents/agent-eval-designer.md` | ✅ | sub-agent especialista |

### Calculadora

| Archivo | Estado |
|---|---|
| `docs/data/models.json` | ✅ 113 modelos catalogados, 70 con ≥50 runs, default_weights expuesto |
| `docs/index.html` | ✅ cache busting `?v=20260430a` |
| `docs/app.js` | ✅ columnas Quality + Cost + Tools en vista global |
| `docs/style.css` | ✅ |
| `docs/sitemap.xml` | ✅ auto-gen |

---

## Pendientes naturales (próximas sesiones)

Ordenados por valor / esfuerzo:

### 1. Sliders en calculadora (alta prioridad, low esfuerzo)
- Componentes raw (quality_avg, cost_score_avg, etc.) ya están expuestos en `docs/data/models.json`
- Falta: UI con sliders para ajustar pesos en tiempo real, recalcular ranking sin reload
- ETA: 2-4h

### 2. Validación hipótesis Opus 4.7 (mid prioridad, mid esfuerzo)
- 30 respuestas Opus vs Llama 3.3 70B side-by-side en los 5 tests con mayor delta
- Segundo juez (Gemma 4 31B local en DGX) sobre muestra 50 tests para verificar consistencia con Phi-4
- System prompt "be concise" para Opus → ver si quality sube
- Análisis distribución output tokens (no solo promedio)
- ETA: 1 día

### 3. Lote 12 — cobertura completa 91 tests para modelos solo en agent_long_horizon
- 38 modelos tienen agent_long_horizon pero 32 de ellos NO tienen los 91 single-turn
- Re-correr esos 32 × 91 = 2912 runs, ~1-2 días, ~$30-50 OpenRouter
- ETA: 2 días

### 4. NIAH-ES (Approach 2 del roadmap, alta prioridad para paper)
- Suite 25 nueva: long-context español (4K, 16K, 64K, 256K, 1M)
- 15 modelos con context window suficiente
- Aporte original (no existe NIAH-ES público)
- ETA: 1 semana

### 5. Paper arXiv draft
- Estructura sugerida en ROADMAP.md (~12-15 páginas)
- Necesita: 4-5 figuras (scatter precio-calidad, provider matters bar, agentic gap quadrant)
- Endorsement cs.CL si primer envío
- ETA: 2 semanas calendario

### 6. HuggingFace Dataset publicación
- Subir docs/data/models.json + responses como dataset etiquetado
- Da DOI cita-able
- ETA: 1 día

---

## Comandos para reanudar

### Verificar estado al inicio de nueva sesión

```bash
cd /Users/cristiantala/Playground/Benchmarks/alternativos
git status
git log --oneline -5
git tag | tail -5
ls -lat benchmarks/results/benchmark_2026*.json | head -3
ps aux | grep "runner.py" | grep -v grep
```

### Si necesitas reanudar un benchmark cortado

```bash
python benchmarks/runner.py --quick --judge --judge-model phi4 \
    --resume benchmarks/results/<archivo>.json
```

### Si cambiaste pesos en scoring.py y quieres regenerar todo

```bash
source .venv/bin/activate
python benchmarks/export_for_pages.py        # recalcula desde componentes raw
python benchmarks/generate_per_model_md.py   # regenera MDs por modelo
python benchmarks/generate_modelos_md_table.py -i
python benchmarks/generate_tests_md.py
python benchmarks/generate_sitemap.py
python benchmarks/sync_doc_counts.py         # sincroniza counts en docs
```

### Si querés bench thinking de un nuevo modelo hybrid

```bash
# 1. Agregar entrada al config con force_reasoning=True
# Ver ejemplo: claude-opus-4.7-thinking en benchmarks/models.py

# 2. Smoke test (12 tests agent_long_horizon, ~$0.5-15 según modelo)
python benchmarks/runner.py --quick --tests agent_long_horizon \
    --models <key>-thinking
```

---

## Para futuros agentes que lean este archivo

1. **Lee primero**: `CLAUDE.md` (instrucciones del proyecto), `ROADMAP.md` (plan adelante), este archivo (estado vivo).
2. **Actualiza este archivo** cuando tomes una decisión importante o ejecutes algo en background.
3. **No dupliques**: este archivo es **estado vivo**. Las decisiones tomadas pasan a CHANGELOG cuando hay release.
4. **Memoria del usuario**: respetar las reglas de `~/.claude/projects/-Users-cristiantala-Playground-Benchmarks-alternativos/memory/` — español neutro, no recomendaciones personalizadas en INSIGHTS, etc.
5. **Costos**: cualquier acción que cueste >$5 OpenRouter requiere confirmación explícita del usuario antes de lanzar.
6. **Auto-generación**: antes de cualquier commit que toque benchmarks/results/, config, tests o docs/, ejecutar EN ORDEN los 6 scripts de la regla en CLAUDE.md.
7. **Sync con remoto**: usar `git pull --no-rebase` (preferencia del usuario, no rebase).
