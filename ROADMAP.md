# Roadmap del Benchmark

> Ultima actualizacion: 22 de Mayo de 2026
> Estado del ranking: **v2.6.2 — 113 modelos en config, 72 con cobertura ≥50 runs, 8,000+ runs** evaluados con juez Phi-4. Top 5 compuesto: Llama 4 Scout 17B, Llama 3.1 8B, Llama 3.3 70B, GPT-OSS 20B, Mistral Small 4. Ver [README.md](README.md) y [DATASHEET_2026-05.md](DATASHEET_2026-05.md).
> **Próximo release: Junio 2026** (cadencia mensual). El release de mayo ya salió — ver sección [Ciclo Junio 2026](#ciclo-junio-2026--modelos-nuevos-por-probar) abajo.

---

## Ciclo Junio 2026 — modelos nuevos por probar

> Sección agregada el 22 de mayo 2026 para preparar el **release de junio**. Cadencia mensual establecida en v2.6.1: cada 1ro de mes → regen `models.json` + update INSIGHTS + `DATASHEET` nuevo + CheatSheet PDF + tag semver. El release de **mayo ya salió** (v2.6.x, ver [DATASHEET_2026-05.md](DATASHEET_2026-05.md)). Esta cola reemplaza la de "Lote 3" de abril, ya completada (DeepSeek V4, GPT-OSS, GPT-5.5, Grok, Hermes 4, Gemini 3.1, MiMo V2.5, Mistral Small 4 / Large 3, GLM 5/5.1, Qwen 3-Next, Seed-OSS — todos en config).
>
> Estado base: **113 modelos en config · 72 con cobertura ≥50 runs**.

### Qué entra en el release de junio (checklist)

- [ ] **Probar los modelos nuevos salidos en mayo** (lista candidatos abajo) — al menos los Tier 1 con cobertura ≥50 runs.
- [ ] **`DATASHEET_2026-06.md`**: cambios mayo→junio (ranking, modelos nuevos, hallazgos) comparado contra `DATASHEET_2026-05.md`.
- [ ] **Documentar lo que pasó en mayo** que aún no quede en datasheet/INSIGHTS (cierre del ciclo previo).
- [ ] **Regen estándar** (orden CLAUDE.md): per-model MD → tabla MODELOS → TESTS → `export_for_pages` → sitemap → `sync_doc_counts`.
- [ ] **CheatSheet PDF "Junio 2026"** + **tag semver** (probable v2.7.0).
- [ ] Si avanza el eje de eficiencia operativa (abajo): incluir el piloto en INSIGHTS.

### Por qué seguimos agregando modelos (y por qué esto es una *referencia*, no un veredicto)

Cada mes salen modelos nuevos y los proveedores re-entrenan los existentes. Pero el objetivo NO es coronar un "mejor modelo" universal — es darle a un emprendedor una **base** para decidir, que después valida contra SU workload. El score compuesto pesa quality + costo + tool calling + velocidad + latencia para un perfil LATAM, no es una verdad absoluta.

**Caso real de mayo 2026 que lo deja claro**: Cristian evaluó migrar de **MiniMax M2.7** (su suscripción actual) a **Xiaomi MiMo** (suscripción más cara). En nuestro ranking MiMo V2.5 sale **top-10** (quality 7.27, ~$0.13/1k calls) → "se ve mejor". Pero en uso real **MiMo no completaba las tareas: consumía muchos más tokens** y reventaba el budget de créditos de la suscripción antes de terminar. **El score actual no predijo esto** — porque mide costo por-llamada con un supuesto fijo de tokens, no cuántos tokens gasta cada modelo para *completar* la tarea. De ahí el eje nuevo más abajo.

→ Lección para el lector del benchmark: usalo para **acotar candidatos**, no para cerrar la decisión. El último filtro lo da tu propia tarea, tu proveedor y tu presupuesto.

### Modelos candidatos para junio

> Investigación hecha el 22 de mayo 2026 vía web + **OpenRouter `/v1/models` (fuente primaria)**. ⚠️ Los aggregators de precios (costgoat, pricepertoken, llm-stats) **se contradicen y traen errores de parsing** (uno listó Gemini 3.5 Flash a "$150/1M", GPT-4.1 a $0.10/$0.40). Para precios confiamos en la **API de OpenRouter** o la página oficial del proveedor, NO en aggregators. Igual verificar el ID exacto al momento de agregar. Regla: distinto ID = modelo distinto = se mide.

#### A. Confirmados salidos en mayo 2026 (datos verificados — agregar en junio)

| Modelo | Proveedor | Salió | $ in/out /1M | Notas | Por qué para emprendedores |
|---|---|---|---|---|---|
| **Gemini 3.5 Flash** | Google | 19 may | $1.50 / $9.00 | 1M ctx; sucesor del 2.5 Flash | Velocidad+calidad para contenido/agentes — releva al Flash que ya medimos |
| **Grok 4.3** | xAI | 6 may | $1.25 / $2.50 | 2M ctx | Tool calling + contexto largo; sucesor real de 4.20 (no "Grok 5") |
| **Mistral Medium 3.5** | Mistral | 29 abr | TBD (open) | Coding + multilingüe fuerte | Open, coding barato, español |
| **DeepSeek V4 Flash-Max / Pro-Max** | DeepSeek | 23 abr | TBD (open weights) | Variantes "Max" agentic de V4 | Workhorse open agentic |
| **GPT-5.4 Nano** | OpenAI | may | ~$0.20 / $1.25 | Tier ultra-barato OpenAI | Baseline OpenAI económico |
| **GPT-5.5 Instant** | OpenAI | 23 abr | familia 5.5 | Variante low-latency de 5.5 | Latencia para agentes |

#### B. Sucesores probables aún SIN confirmar release (vigilar)

| Familia | Candidato | Por qué medirlo | Relevancia para Cristian |
|---|---|---|---|
| **MiniMax** | M2.8 / sucesor de M2.7 | Es su sub actual; sucesor directo = re-medir | **Caso activo** — la migración que evalúa |
| **Xiaomi MiMo** | V3 / V2.6 | V2.5/Pro cubiertos; sub $14 bajo evaluación | **Caso activo** — el modelo del caso de tokens |
| **Qwen** | Qwen 3.6 **base** (Apache, pesos en HF) | Solo tenemos 3.6 *Plus* (propietario); falta el base abierto | Usa Qwen 3.5 397B en producción — comparar |
| **DeepSeek** | **R2** (reasoning sucesor de R1) | R1 free quedó viejo; falta reasoning nuevo (V4 ya cubierto) | Razonamiento barato |
| **Kimi (Moonshot)** | K2.7 | Cada minor = ID nuevo, se mide | Open-weights agentic alternativo |
| **Mistral** | Devstral 3 | Devstral Small es nuestro top coding; v3 = re-medir | Coding/agentes baratos |
| **GLM (Z.ai)** | GLM 5.5 | 5/5.1 cubiertos; agentic chino fuerte | Agentes |
| **Meta Llama** | Llama 4.1 / Behemoth | 4 Scout/Maverick cubiertos (Groq domina nuestro top 5) | Open + Groq |
| **Anthropic** | Sonnet 4.7 | 4.6 cubierto; baseline premium | Techo de calidad de referencia |

#### C. Gaps de mercado — filtrados por el lente emprendedor

> Tu punto: no todos los gaps valen para ESTE público. Filtrados para LATAM, agentes N8N/OpenClaw, contenido en español, budget real:

| Proveedor | Modelos | Veredicto | Por qué |
|---|---|---|---|
| **Cohere** | Command A / R+ | ✅ **Sí (alta)** | Multilingüe fuerte (español), RAG, tool calling nativo — encaja directo con el público |
| **Amazon Nova** | Pro / Lite / Micro | ✅ Sí (media) | Ultra-barato + AWS; varios emprendedores ya están en AWS |
| **AI21 Jamba** | 2 Large / Mini | 🟡 Opcional | Solo si aparece caso de docs largos (contratos, libros). NIAH-ES ya cubre long-ctx con GPT-4.1 |
| **Perplexity Sonar** | Sonar / Pro | 🟡 Opcional | Search-augmented útil para research, pero producto nicho con API limitada |
| **IBM Granite** | Granite 4 | ❌ No por ahora | Enterprise; poca tracción en la comunidad emprendedora |
| **OpenAI o3 / o4-mini** | reasoning | ❌ No | GPT-5.x ya cubre OpenAI; thinking es caro y **empeora** multi-turn (hallazgo nuestro) |
| **Reka / Falcon / Hunyuan** | varios | ❌ No | Nicho, sin demanda en el público objetivo |
| **Liquid LFM2** | 8B / 24B | → mover a lista **DGX local** | Tiene sentido como local, no como API de pago |

#### D. Phi-4 como modelo: NO incluir (decisión)

Phi-4 es **el juez** del benchmark y toda la metodología se apoya en que Microsoft NO tiene modelos compitiendo → cero conflicto de interés (ver "Por qué Phi-4 como juez" más abajo). Si lo metemos como competidor:
- Se evaluaría a sí mismo (Phi-4 juzga Phi-4) = **self-enhancement bias**, justo lo que el diseño evita (papers NeurIPS reportan 5-7% de sesgo cuando juez y evaluado comparten origen).
- El workaround (juzgarlo con Gemma/Haiku) lo deja **no comparable** con el resto del ranking (juzgado por Phi-4).

**Veredicto**: mantener Phi-4 **solo como juez**. Si hay curiosidad genuina, correr un experimento aparte ("Phi-4 concursante juzgado por Gemma"), claramente marcado como no-comparable y fuera del ranking principal.

#### E. Priorización del lote de junio

- **Tier 1 (correr sí o sí)**: Gemini 3.5 Flash, Grok 4.3 (confirmados, sucesores de modelos top nuestros) + **MiniMax M2.8** y **MiMo V3** (tus casos activos) + **Cohere Command A** (gap español).
- **Tier 2 (si alcanza budget/tiempo)**: Mistral Medium 3.5, DeepSeek V4 Flash-Max/Pro-Max, Qwen 3.6 base, GPT-5.4 Nano, Amazon Nova.
- **Tier 3 (oportunista)**: Kimi K2.7, Devstral 3, GLM 5.5, Llama 4.1, Sonnet 4.7, GPT-5.5 Instant, AI21 Jamba.

### Higiene de precios — correcciones verificadas APLICADAS (22 may)

> ✅ **Aplicado 22 may 2026**. Se corrigieron en `models.py` + `scoring.py` los precios **verificados vía OpenRouter API**, y se re-scoreó el histórico SOLO de esos modelos con `benchmarks/rescore_costs.py --only "..."` (1.072 runs, 9 modelos). Efecto en el ranking: Opus 4.6 −0.47, Opus 4.7 −0.33 (estaban **sub-costeados**, no sobre-costeados), Qwen 3.6 Plus +0.34, DeepSeek V4 Pro +0.26, Grok 4.20 +0.19, Kimi K2.6 ≈0. **Además el costeo es ahora provider-aware**: `estimate_cost` usa el precio por-entrada del config y el runner lo pasa en cada corrida → el costo depende del proveedor por el que se mide.

| Modelo | Hoy (models.py / scoring.py) | Verificado (OpenRouter API) | Impacto |
|---|---|---|---|
| **Claude Opus 4.7** | $15 / $75 (ambos) | **$5 / $25** | **ALTO** — deja de ser "40-100x más caro"; sube fuerte. Reescribe la narrativa de README/INSIGHTS ("Why Opus doesn't top our benchmark") |
| **DeepSeek V4 Pro** | $1.74 / $3.48 (ambos) | **$0.435 / $0.87** | **ALTO** — 4x más barato; pasa de "medium" a candidato cheap top |
| **DeepSeek V4 Flash** | $0.14 / $0.28 | $0.112 / $0.224 | Bajo |
| **Kimi K2.6** | $0.80/$3.50 (models) · **$1.50/$9.00** (scoring) | $0.73 / $3.49 | Medio — scoring.py muy sobre-estimado; models.py casi ok |
| **Kimi K2** | $0.20/$0.80 (models) · $1.00/$3.00 (scoring) | verificar | Drift interno grande |
| **GPT-5.4** | $5/$15 (models) · $1.25/$10 (scoring) | verificar | Drift interno |
| **GPT-5.5** | $5/$30 (models) · $8/$45 (scoring) | ~$5/$30 (web) | Drift interno; models.py parece correcto |
| **Llama 4 Maverick** | $0.50/$1.00 (models) · $0.40/$2.40 (scoring) | verificar | Drift interno |
| **Gemini 2.5 Flash Lite** | $0.10/$0.40 (models) · $0.075/$0.30 (scoring) | verificar | Drift interno |
| **Claude Haiku 4.5** | $1.00/$5.00 (models) · $0.80/$4.00 (scoring) | verificar | Drift interno |

**✅ Hallazgo mayor — RESUELTO con rescore total (v2.7, 22 may)**: al auditar descubrimos que el costo histórico de la **mayoría** de modelos se guardó con el fallback `(1.0, 3.0)` de `PRICING` (corridas previas a que el modelo estuviera en el dict). Efecto: casi todos quedaron con `cost_score ≈ 7.0` → **la dimensión costo (20% del peso) era casi inerte** y el ranking publicado era de facto quality-dominado. Decisión del usuario: aplicar **rescore provider-aware TOTAL** (`python benchmarks/rescore_costs.py`, 7.483 runs). Resultado: el costo por fin discrimina; gratis/NIM/local y open-source baratos suben (Devstral Small #1, Nemotron Omni NIM, Qwen-Next NIM, Gemma), premium bajan (Gemini 2.5 Pro −0.49, GPT-5.4 −0.47, Opus 4.7 → #66/72). Ver CHANGELOG v2.7.0. **Caveat documentado en README/calculadora**: el tier gratis NIM ($0/call) tiene rate-limit 40 RPM — gran C/B para volumen bajo-medio, no para alto throughput.

**Fix de raíz (estado)**:
1. ✅ `estimate_cost(model, in, out, prices=...)` acepta precio explícito del config (provider-aware); el runner lo pasa → corridas futuras costean por proveedor.
2. ✅ `benchmarks/rescore_costs.py` reescribe el costo histórico desde el config (fuente única); corrió **total** (v2.7).
3. ⏳ Pendiente (deuda menor): hacer que `PRICING` derive de `models.py` o un test que falle si difieren + script `update_prices.py` que consulte la API de OpenRouter y proponga diffs (no aggregators) para verificar el resto del catálogo.

### Eje a diseñar: eficiencia operativa ("cost-to-complete")

**Estado: idea aprobada, medición POR DISEÑAR.** No implementar todavía — primero definir cómo medirlo bien (y que sirva tanto a emprendedores tech como no-tech).

**Motivación**: el caso MiMo/MiniMax de arriba. Nuestro componente Cost (20% del score) asume `tokens_per_call = {input:300, output:1500}` **fijo para todos los modelos**. Eso esconde dos cosas que importan en producción:
1. Un modelo verboso o que sobre-razona gasta 3-5x los tokens para la misma respuesta (caso MiMo → revienta créditos de la sub).
2. Un modelo agentic puede necesitar más *pasadas* (turnos / tool calls) para llegar al objetivo.

**La tensión a capturar** (planteada por el usuario): *"Opus puede demorarse menos pasadas en hacer algo que MiniMax tarda más — pero con MiniMax puedo hacer eso y mucho más."* Hay un frontier, no un ganador único:
- **Capacidad-por-pasada**: modelos premium (Opus, GPT-5.x) terminan en menos turnos → menos fricción y a veces menos tokens totales.
- **Volumen-por-presupuesto**: modelos baratos / de suscripción necesitan más turnos, pero alcanzan para muchas más tareas con el mismo gasto.

El "mejor" depende de dónde caés en ese frontier para TU workload — y eso es justo lo que el benchmark debe ayudar a ubicar, no decidir por vos.

**Candidatos de métrica (a pilotear, ninguno decidido)**:
1. **`turns_to_completion`** — en una tarea agentic de objetivo abierto, ¿cuántos turnos / tool calls necesitó hasta cumplir el objetivo (o rendirse)? Requiere tests con criterio de éxito binario + tope de turnos. El runner ya tiene `multi_turn_script`, pero con turnos fijos — habría que agregar un modo "objetivo abierto / hasta lograrlo".
2. **`tokens_to_completion`** — tokens reales end-to-end (input + output + reasoning) para resolver la tarea, NO por-call. Reemplaza el supuesto fijo de 1500. Captura directo el problema MiMo.
3. **`tasks_per_budget`** — dado $X (o N créditos de sub), ¿cuántas tareas completas rinde cada modelo? = presupuesto / cost-to-complete real. Operacionaliza el "con MiniMax hago eso y mucho más".
4. **Proxy para no-tech** — etiqueta simple por modelo: *"suele resolver al primer intento / necesita 2-3 / itera mucho"* + *"con $20/mes te alcanza para ~N tareas de este tipo"*. En la calculadora: slider de presupuesto → "tareas estimadas/mes" por modelo.

**Preguntas abiertas antes de implementar**:
- ¿Cómo definimos "tarea completada" sin humano en el loop? → rúbrica binaria por test, como ya hacemos en `agent_long_horizon`.
- ¿Los reasoning tokens cuentan? → **Sí**: se facturan y son justo lo que hace caro a Opus "en pocas pasadas". Hay que sumarlos.
- Costo/varianza: los tests open-ended son caros y el pilar Agentes ya mostró alta varianza intra-modelo (INSIGHTS §13). Piloto chico primero.
- ¿Métrica nueva o re-pesar Cost? → probablemente **dimensión nueva** (`efficiency`) + opción en la calculadora, sin romper el score histórico.

**Piloto propuesto (S effort, ~$10-20)**:
- 3-5 tareas open-ended con criterio de éxito (1 coding-debug, 1 contenido-iterativo, 1 agente-N8N, 1 research).
- Modelos: top 10 compuesto + **MiniMax M2.7 + MiMo V2.5 + Opus 4.7** (los 3 del caso real).
- Reportar: `turns_to_completion`, `tokens_to_completion`, `tasks_per_$20`, `completion_rate`.
- Hallazgo esperado: MiMo/MiniMax ganan en `tasks_per_$` pero pueden perder en `completion_rate`/`turns`; Opus gana en turns/completion pero pierde en volumen. **Mostrar ese trade-off explícito ES el aporte** — no coronar un único "mejor".

---

## Regla: mantener 3 cortes de ranking

Cada vez que se actualice el ranking en README, mantener siempre estas 3 vistas:
1. **Ranking global** — todos los modelos
2. **Ranking solo alternativas** — sin Anthropic, sin OpenAI y **sin Google propietarios** (Gemini Flash / Flash Lite / Pro). Sí se permiten modelos open-source de Google (Gemma). Para quienes quieren evitar los proveedores propietarios populares.
3. **Ranking solo open-source** — todos los modelos con `open_source: True` en config (para quienes necesitan licencia abierta, self-hosted, o planean correr en DGX Spark)

El script `generate_per_model_md.py` ya tiene los datos; al migrar a HTML sliders (#9) debe exponer el filtro por licencia además de los sliders existentes.

---

## Completado en v2.1.0 (23 Abril 2026)

- [x] Lote 1 con juez Phi-4: 8 modelos × 91 tests → `benchmark_20260422_204025.json`
- [x] Lote 2 con juez Phi-4: 9 modelos × 91 tests → `benchmark_20260423_051248.json`
- [x] Ranking consolidado publicado en README + CHANGELOG + COMPARATIVA
- [x] Runner con **guardado incremental atómico** + flag **`--resume`** (resumabilidad real)
- [x] Guardado de **respuesta completa** por test en `results/responses/<timestamp>/`
- [x] **MDs navegables por modelo** en `results/per-model/` (17 archivos + index)
- [x] Script `benchmarks/generate_per_model_md.py` para regenerar sin re-correr tests
- [x] Log del runner con modelo, progreso local, elapsed y ETA basado en ventana móvil
- [x] Devstral Medium (`mistralai/devstral-medium`) + Devstral 2 (`mistralai/devstral-2512`) agregados al config

---

## En curso

### Modelos nuevos por agregar (Lote 3)

**Confirmados listos** (IDs verificados):
- [ ] **GPT-OSS 120B** (`openai/gpt-oss-120b`, $0.039/$0.19, Apache 2.0) — candidato fuerte a top 5
- [ ] **GPT-OSS 20B** (`openai/gpt-oss-20b`, $0.03/$0.14, Apache 2.0) — baseline barato
- [ ] **Devstral Medium** (ya en config, falta correr benchmark)
- [ ] **Devstral 2** (ya en config, falta correr benchmark)

**Esperando disponibilidad en OpenRouter**:
- [ ] **GPT-5.5** — anunciado 23 abril 2026, pricing TBD (probable 24-48h)
- [ ] **GPT-5.5 Mini** — si sale

**Alta prioridad** (verificar ID en OpenRouter antes de agregar):
- [ ] **Grok 4.1 Fast** ($0.20/$0.50, xAI) — tool calling de xAI, 2M ctx
- [ ] **DeepSeek R1** — razonamiento puro, hay tier free
- [ ] **DeepSeek V4** ($0.30/$0.50, MIT) — sucesor del V3.2 que quedó #10
- [ ] **Hermes 4** (Nous Research) — modelo agentic open-source
- [ ] **Gemini 3.1 Flash Lite** ($0.25/$1.50) — sucesor del #4 actual
- [ ] **Gemini Flash más nuevo** (Gemini 3.1 Flash o superior, no la Lite) — verificar ID exacto en OpenRouter/Google; supera al 2.5 Flash que hoy está corriendo en Lote 3

**Media prioridad**:
- [ ] Command R+ (Cohere) — enterprise RAG
- [ ] Jamba (AI21) — long context 256K+
- [ ] Phi-4 como modelo (hoy solo es juez)
- [ ] Mistral Small 4, Grok 4.20, Gemini 3.1 Pro

### Proveedores directos (pendiente #7)

Desbloquea modelos que fallan en OpenRouter por falta de tool calling nativo (ej: Llama 4 Maverick con 17 errores 404). Implementar provider adapters para:
- [ ] **Groq** — LPU, velocidad cruda en Llama/Mixtral/Qwen
- [ ] **Fireworks** — muchos open-source con tool calling
- [ ] **Together AI** — similar, fallback

### Ollama Cloud (pendiente #12)

Cristian tiene suscripción a Ollama Cloud activa.
- [ ] Implementar `UnifiedProvider` para Ollama Cloud (endpoint + auth por API key)
- [ ] Tier nuevo `cloud_ollama` en config
- [ ] Testear **`qwen3.5:397b-cloud`** (modelo que Cristian usa en producción para ecosistemastartup.com)
- [ ] Agregar cualquier otro cloud-only útil que no esté en OpenRouter

### DGX Spark (cuando llegue, ~próxima semana)

Hardware: NVIDIA DGX Spark 128GB RAM unificada.
- [ ] Barrido de modelos Ollama que quepan: ~110B Q4, ~70B FP16 cómodos, 122B Q4 ajustado
- [ ] Prioridad: Qwen 3-Next 80B, Qwen 3.5 122B, Qwen3-Coder-Next, LFM2 24B, Ministral-3, Devstral-Small-2, GLM-OCR, Nemotron 120B local
- [ ] Actualizar tags obsoletos en config: `qwen3.5:25b` y `qwen3.5:72b` ya no existen en Ollama
- [ ] Comparar mismo modelo local vs API (calidad idéntica, velocidad distinta, costo muy distinto)
- [ ] Juez local con modelo más grande (Qwen 3.5 72B o 122B como juez alternativo)

---

## Pendiente de sesiones anteriores

### #9 Calculadora de recomendación (HTML con sliders)

HTML estático sin backend que lee los JSON de `results/` y ranquea modelos según ponderación del usuario. Sliders para calidad/velocidad/costo/tool-calling/idioma-español/open-source. Filtros: sólo gratis, sólo self-hosted, tier máximo. Publicable en GitHub Pages.

### Tests nuevos (de roadmap anterior)

- [ ] **n8n_workflow_generation**: workflows funcionales validados vs documentación N8N vía MCP
- [ ] **n8n_debugging**: dar workflow roto, que el modelo lo corrija
- [ ] **contract_review**: detectar cláusulas problemáticas
- [ ] **cv_screening**: rankear CVs con justificación
- [ ] **video_script**: guion para video 60-90s
- [ ] **agent_long_session**: sesiones 30+ min con contexto acumulado
- [ ] **multi_agent_collaboration**: dos modelos colaborando
- [ ] **image_understanding**: tests con vision
- [ ] **cost_optimization_routing**: dado un budget, elegir mix óptimo

### Mejoras al scoring/infra

- [ ] Multi-judge: correr con 2-3 jueces y promediar para reducir sesgo
- [ ] Validación JSON específica en news_seo_writing (parsear y verificar claves)
- [ ] Dashboard web con filtros (complemento al HTML #9, con más dimensiones)
- [ ] Automatizar run mensual con GitHub Actions o cron
- [ ] Delta tracking: comparar resultados entre meses

### Re-correr modelos afectados

- [ ] **Llama 4 Maverick**: 17 errores en OpenRouter → re-correr vía provider directo
- [ ] **Kimi K2**: 17 errores 429 → re-intentar en ventana con menos tráfico o cambiar provider
- [ ] **Gemma 4**: bloqueado hasta que Ollama arregle bug de output vacío en `/api/chat` (workaround: `/api/generate`)

---

## Skills y automatización

Propuesta: crear 2 skills en `.claude/skills/` para evitar olvidar pasos.

### `/add-model <key> <id> <input_price> <output_price>`

Workflow atómico:
1. Agrega entrada al dict `MODELS` en `benchmarks/config.py`
2. Agrega pricing al dict `PRICING` en `benchmarks/scoring.py`
3. Valida que `python benchmarks/runner.py --list-models` lo muestra
4. Propone comando para correr `--quick --judge --judge-model phi4 --models <key>`
5. Al terminar, regenera `results/per-model/` y sugiere commit message

### `/run-benchmark <modelos> [--lote N]`

Wrapper con chequeos previos:
- ¿Ollama corriendo si `--judge`?
- ¿API keys configuradas para los modelos?
- ¿Los modelos existen en config?
- Lanza el runner en background con monitor de checkpoints
- Al terminar, regenera MDs y muestra diff del ranking

---

## Casos de uso pendientes (doc específico por caso)

### Por plataforma de agentes
- [ ] **OpenClaw**: modelo cerebro + sub-tareas + configuración recomendada
- [ ] **Hermes**: modelos compatibles, setup óptimo tool calling
- [ ] **N8N**: nodo AI Agent vs AI Text, workflows recomendados
- [ ] **Claude Code (alternativas)**: setup Roo Code + MiniMax/Devstral/DeepSeek ~$50/mes

### Por tarea
- [ ] Soporte al cliente: modelo + workflow N8N
- [ ] SEO/contenido: pipeline research → escribir → publicar
- [ ] Campañas marketing: copy + análisis + A/B tests
- [ ] Calificación de leads: workflow N8N + CRM + scoring
- [ ] Debugging: modelo + Cursor/Roo Code

### Por presupuesto
- [ ] $0/mes: solo locales (Ollama + DGX Spark) — qué instalar
- [ ] $20/mes: una sola suscripción, cuál
- [ ] $50/mes: combo óptimo 2-3 servicios
- [ ] $100+/mes: setup enterprise con fallbacks

---

## SEO y comunidad

El repo es público y debe servir como funnel para la comunidad de emprendedores.

- [x] Topics/tags GitHub: 19 topics agregados (llm-benchmark, claude-alternatives, gpt-alternatives, n8n, openclaw, etc) — abril 26
- [x] Subdominio propio: `benchmarks.cristiantala.com` con CNAME en GitHub Pages — abril 26
- [x] JSON-LD Schema.org (Dataset + SoftwareApplication + FAQPage) en calculadora — abril 26
- [x] sitemap.xml + robots.txt auto-generado por `generate_sitemap.py` — abril 26
- [x] 6 landing pages dedicadas (alternativas-claude, -chatgpt, -gemini, modelos-n8n, -open-source-local, -baratos-emprendedores) — abril 26
- [x] AGENTS.md + agents-decision-guide.json para que agentes IA consuman el repo — abril 26
- [ ] Badges en README (modelos testeados, última actualización, license, CI)
- [ ] Link a Skool en footer del README y CheatSheet
- [ ] Blog post en cristiantala.com con resultados y link al repo
- [ ] Social cards (Open Graph image dinámica con top 5 actual)
- [ ] CheatSheet PDF regenerado con resultados v2.3
- [ ] Sección "Contributing" + issue templates (agregar modelo, reportar resultado, sugerir test)
- [ ] CheatSheet visualmente atractivo para LinkedIn
- [ ] Submit a Google Search Console + Bing Webmaster

## Mejoras inspiradas en Claw-Eval (decidido 27 abril 2026)

[Claw-Eval](https://github.com/claw-eval/claw-eval) es el benchmark académico de referencia para agentes (PKU + HKU, 498 stars, usado por Meta/Kimi/Qwen/Xiaomi/GLM). Análisis y decisiones para incorporar mejor lo suyo:

### ✅ Sí implementar (priorizado)

- [ ] **HuggingFace dataset publication** (S effort, alta visibilidad)
  - Subir 91 tests + criteria + responses históricos a HuggingFace Datasets
  - Card markdown con metodología, licencia MIT, citation BibTeX
  - SEO académico — facilita que investigadores citen y deriven
  - Backlink desde HF a `benchmarks.cristiantala.com` y al repo

- [ ] **Sub-categorías por pilar** (M effort)
  - Dentro de "Coding" → wordpress, n8n_workflow, scripts, refactor, debugging
  - Dentro de "Contenido" → blog_tecnico, marketing_copy, traduccion, newsletter
  - Dentro de "Agentes" → tool_calling, orquestacion, multi_step
  - Permite filtrar calculadora por sub-caso (no solo el 4-pilar agregado)
  - Score por sub-categoría visible en MD por modelo + JSON

- [ ] **Multi-turn tests NUEVOS diseñados específicamente** (M effort)
  - NO convertir tests existentes — diseñar 8-10 tests fresh para multi-turn
  - Usuario simulado (Phi-4 actuando) hace follow-ups, cambia requisitos
  - Captura: ¿el modelo mantiene contexto? ¿pide clarification cuando hay ambigüedad? ¿maneja cambios de plan?
  - Categoria nueva: `multi_turn/` con tests propios

### 🔄 Considerar al final (por modelo, no para todos)

- [ ] **Pass^N metric** (3x costo × N modelos)
  - **NO aplicar a todos** — definir caso por caso si modelo "lo merece"
  - Útil para: top 5-10 ranking final, modelos que entran a producción de Cristian
  - Validar reproducibilidad sin gastar 3x en cada lote completo

### ⏳ Pipeline largo (interesado, no inmediato)

- [ ] **Sandbox Docker para coding ejecutable** (L effort)
- [ ] **Multimodal real** — image/video/PDF analysis (L effort, requiere V2.5 + Gemini Pro testeo)
- [ ] **Safety dimension explícita** — peso 5-10% del scoring para adversarial tests
- [ ] **arXiv paper** o whitepaper técnico (M effort, autoridad académica)

### ❌ NO implementar (justificado)

- ❌ **Complementar Claw-Eval directamente** — no competimos, complementamos. Audiencias distintas (académicos vs emprendedores). Mantener foco propio.
- ❌ **300 human-verified tasks** — su ventaja es budget académico (PKU + HKU). Nuestro foco es operatividad práctica.

## Estrategia con agentes IA (abril 2026)

11 agentes pre-hechos en `.claude/agents/`. Estrategia por fase:

### Fase 1 — Inteligencia del benchmark (post-cada-lote)
- [ ] **data-scientist**: análisis cuantitativo de los JSONs → `INSIGHTS.md`. Correlaciones, outliers, Pareto frontier, regresiones cross-lote.
- [ ] **business-analyst**: traduce insights a decisiones de negocio (break-even, ROI por perfil)

### Fase 2 — Documentación profunda (cuando cambia arquitectura)
- [ ] **docs-architect**: `ARQUITECTURA.md` con explicación deep del runner, scoring, judge, decisiones de diseño
- [ ] **tutorial-engineer**: `tutoriales/` con 5 guías paso-a-paso (quick start, agregar modelo, tests custom, Phi-4 setup, elegir modelo)

### Fase 3 — Contenido SEO desde insights (semanal)
- [ ] **seo-keyword-strategist**: research keywords trending del mercado IA
- [ ] **seo-content-writer**: blog posts desde hallazgos del data-scientist
- [ ] **content-marketer**: adaptar 1 blog post → LinkedIn / Skool / newsletter / Twitter thread

### Fase 4 — Optimización continua (pre-commit)
- [ ] **seo-content-auditor**: audit cada 2 semanas
- [ ] **seo-meta-optimizer**: optimiza meta tags HTML al cambiar landing pages
- [ ] **seo-structure-architect**: reorganiza si docs crecen mucho

### Automatización pendiente
- [ ] GitHub Action `weekly-content.yml` que invoca Fase 3 semanal y abre PR con drafts de blog/social
- [ ] Hook en `regenerate-auto-artifacts.yml` que invoca Fase 1 post-lote nuevo

### Seguridad (repo público)
- [x] `config.py` en `.gitignore`
- [x] `config.example.py` sólo con placeholders
- [ ] Revisar historial git por keys commiteadas antes
- [ ] Agregar `.env.example` alternativo a `config.py`

---

## Decisiones ya tomadas (mantener)

### Por qué Phi-4 como juez
- Microsoft no tiene modelos en el benchmark → cero conflicto de interés
- Papers (NeurIPS 2024): self-enhancement bias 5-7% cuando juez y evaluado comparten proveedor
- MIT license: cualquiera replica exactamente los resultados
- 14B, 3-9s/eval, cabe en 24GB RAM

### Por qué 4 pilares
- Razonamiento, Coding, Contenido/Marketing, Agentes/Operaciones
- Basado en necesidades reales de un emprendedor solo (one-man army)
- Cada pilar agrupa suites relacionadas → score por área
- El usuario elige modelo según SU pilar más importante

### Por qué no re-usar benchmarks públicos
- LMSYS Arena mide preferencia humana en chat, no utilidad para agentes
- SWE-Bench mide coding puro, no contenido ni estrategia
- Nuestros tests simulan tareas reales: blog, leads, workflows N8N
- Medimos desde Chile (latencia real para LATAM)
- Incluimos costo por llamada en el score (crítico para startups)

---

## Suite `agent_long_horizon` (decisión 29 abril 2026)

Suite multi-turno (8+ turnos) que mide capacidades agénticas reales: context retention, skill orchestration, interruption recovery, goal persistence. Inspirada en Claw-Eval pero adaptada al runner sin Docker sandbox. Plantilla rígida (script de usuario pre-escrito), tools simulados via stubs, rúbricas regex-based.

### ✅ Completado en v2.4.1

- [x] **3 tests piloto** validados con smoke test sobre Llama 3.3 70B Groq (1 por pilar)
- [x] Extension del runner: `run_multi_turn_script()` + `_score_long_horizon()` + dispatch en `evaluate_result()` por `test["type"] == "multi_turn_script"`
- [x] **Sub-agent `agent-eval-designer`** en `.claude/agents/agent-eval-designer.md` — workflow para diseñar tests, refinar rúbricas, validar discriminación
- [x] **Fase 2 — 9 tests restantes** generados batch por el sub-agent (3 por pilar restante)
- [x] Suite total = 12 tests, integrada al benchmark principal (24 suites en lugar de 23)
- [x] Validación con 3 modelos: Llama 3.3 70B (7.50), Mistral Small 4 (7.41), Nemotron 3 Base 33B (6.59) — drop de ~0.15 vs single-turn confirmado

### 🔄 En curso (Lote 10, 29 abril)

- [ ] **27 modelos × 12 tests = 324 runs** corriendo en background
  - Top 20 single-turn (Llama 4 Scout, Llama 3.1 8B, GPT-OSS 20B Groq, Mistral Small 4, Gemini 3.1 Flash Lite, Grok 4.1 Fast, GPT-OSS 120B Cloud, Devstral, MiMo V2.5, MiMo V2.5-Pro, Hermes 4 70B, GPT-4.1, Devstral 2, MiMo V2-Flash, Gemma 4 31B OR/NIM, Nemotron Nano 30B, Gemini 2.5 Flash, Qwen 3-Next 80B Instruct NIM)
  - Must-include MiMo/DeepSeek/Qwen: MiMo V2-Pro Xiaomi, MiMo V2-Omni Xiaomi, MiMo V2-Omni multimodal, DeepSeek V4 Flash NIM, Qwen 3.5 397B NIM
  - Calibradores low: Gemini 3.1 Pro, Step 3.5 Flash, Kimi K2 Thinking, Kimi K2.5
- [ ] **Lote 10b MiniMax** — M2.7, M2.7-Direct, M2.7-Highspeed (suscripción) en paralelo

### ⏳ Pendiente (post-Lote 10)

- [ ] **Ranking inter-modelo `agent_long_horizon` consolidado** publicado en INSIGHTS sección 0
- [ ] **Cross-reference single-turn vs agentic**: identificar modelos que suben (buenos agentes ocultos) y caen (overrated single-turn)
- [ ] **Stack recomendado por rol**: LLM cabecera (orquestador) + sub-agents/skills (coding, content, research, customer support, tool calling) — diferenciado por proveedor disponible
- [ ] **Fase 3 — calibración con Claw-Eval**: para los 6 modelos en común (MiMo V2.5/Pro, Kimi K2.5/K2.6, Qwen 3.5 397B, GPT-5.4, Nemotron 3 Super), comparar agent_long_horizon avg vs Pass³ Claw-Eval. Si r > 0.7 nuestra suite está alineada
- [ ] **Fase 4 — cobertura completa**: correr `agent_long_horizon` en los 70 modelos con ≥50 runs (faltarían ~40 tras Lote 10). 40 × 12 = 480 runs adicionales, ~$10-15
- [ ] **Fase 5 — integración UX**: filtro `min_agent_score` en calculadora, columna agent score en ranking, recomendaciones N8N/OpenClaw priorizan este pilar

---

## Hallazgos del bloque "thinking variants" (29-30 abril 2026)

Test concreto de la sospecha de Approach 1: ¿modelos hybrid suben de score con extended thinking forzado?

### Implementación
- Adapter (`providers/adapters.py`): nuevo parámetro `force_reasoning: bool = False`. Activa via OpenRouter extra_body `{"reasoning": {"effort": "high"}, "include_reasoning": True}`.
- Runner: propaga `force_reasoning` desde config (`model_config.get("force_reasoning")`) al adapter.
- Config: 5 entradas nuevas con `force_reasoning=True` para variantes thinking de Hermes 4 70B/405B, Kimi K2.5, Claude Opus 4.7, Claude Sonnet 4.6.

### Resultados Lote 11 (Hermes 4 + Kimi)

| Modelo | Sin thinking (single-turn) | Con thinking (agent_lh) | Delta |
|---|---|---|---|
| Kimi K2.5 | 6.27 | **7.00** | **+0.73 ⬆** |
| Hermes 4 70B | 7.24 | 6.70 | -0.54 ⬇ SORPRESA |
| Hermes 4 405B | ~6.5-6.8 | 6.30 | -0.3 a -0.5 ⬇ |

⚠️ **Comparación NO exacta**: scores "sin thinking" son single-turn (91 tests promediados), "con thinking" son agent_long_horizon (12 tests). El patrón cualitativo es robusto — Kimi K2.5 GANA con thinking, Hermes 4 PIERDE — pero para una comparación rigurosa hay que correr ambas variantes en agent_long_horizon.

### Hipótesis revisada

- **Thinking ayuda algunos modelos y empeora a otros**. NO es seguro asumir que `reasoning=high` siempre mejora.
- Para Hermes 4 (post-trained sobre Llama 3 con reasoning), forzar reasoning probablemente degrada su capa agéntica multi-turn — "razona demasiado" y pierde foco.
- Para Kimi K2.5 (diseñado hybrid desde el principio por Moonshot), thinking aporta consistentemente.
- **Implicancia para el paper**: hay que reportar AMBAS variantes (con y sin thinking) de modelos hybrid, no asumir cuál es mejor.

### Pendiente del bloque

- [ ] **Claude Opus 4.7 (thinking) + Sonnet 4.6 (thinking)** — variantes agregadas al config, NO lanzadas (esperando confirmación del usuario, costo ~$10)
- [ ] Re-correr Hermes 4 70B y Kimi K2.5 (sin thinking) en suite agent_long_horizon para tener comparación fair
- [ ] Documentar metodología en INSIGHTS sección "Thinking matters: el costo del reasoning explícito"

---

## Suite `agentic_debugging` (decidido 30 abril 2026 tras caso real)

**Contexto**: caso real reportado donde MiniMax M2.7 (top #7 nuestro) NO pudo resolver un problema técnico complejo en contenedor OpenClaw / VPS Hetzner, mientras Opus 4.7 (fuera del top 10 nuestro) lo resolvió en pocos minutos. Esto expone que nuestro coding score NO predice debugging agentic real.

### Qué medirla

Suite nueva (suite 25) con 5-10 tests de debugging real:
- Cada test es un escenario "tengo este bug, resolvelo": Dockerfile mal configurado, env var faltante, networking K8s, permisos, race condition, OOM, etc.
- Multi-turn 10-20 con stubs detallados de logs/configs (similar al approach de `agent_long_horizon` pero con escenarios técnicos de infra)
- Rúbrica focused en:
  1. ¿Identificó root cause correcto?
  2. ¿Propuso fix correcto?
  3. ¿Iteró bien tras feedback "no funcionó"?
  4. ¿Mantuvo hipótesis sobre 10+ turnos sin perder contexto?

### Implementación
- `benchmarks/tests/agentic_debugging.py` (nuevo)
- Reusar el formato `multi_turn_script` del runner (ya está implementado)
- Considera usar el caso real del usuario como **piloto 1** (problema OpenClaw en VPS Hetzner — anonimizado)

### Inversión
- Diseño de 5 tests piloto: 1 día humano
- Smoke test en Llama 3.3 70B + Opus 4.7 + MiniMax: ~$5
- Validación discriminación inter-modelo
- Lote completo en top 10: ~$30-50

### Hallazgo esperado
Hipótesis: Opus 4.7 / GPT-5.x / Claude Sonnet 4.6 dominarán esta suite (consistente con SWE-bench Verified 87.6% Opus). Modelos cheap top single-turn caerán fuerte. **Esto ratifica el aporte académico**: mostrar que el benchmark single-turn NO es predictor de debugging agentic — hay que medir AMBOS.

---

## Validación cruzada con benchmarks académicos estándar (decidido 29 abril 2026)

Para credibilidad académica (paper arXiv) y triangulación con literatura existente.

### Approach 1 — Cita y compara (esta semana, ~2-3h)

NO replicar HumanEval/GSM8K/IFEval/MMLU desde cero — los proveedores ya los reportan. Recopilar y citar.

- [ ] Recopilar scores oficiales de los **top 30 modelos** del benchmark en:
  - **HumanEval** (Pass@1, coding Python aislado)
  - **GSM8K** (math word problems)
  - **IFEval** (instruction following, prompt-level strict)
  - **MMLU** (general knowledge, 5-shot)
  - Fuentes: technical reports oficiales, Open LLM Leaderboard, Papers With Code, blog posts del proveedor
- [ ] Crear archivo `BENCHMARKS_EXTERNOS.md` con tabla cruzada: modelo / nuestro score / HumanEval / GSM8K / IFEval / MMLU / fuente
- [ ] Sección en INSIGHTS: **"Triangulación con benchmarks externos"** — correlación de Spearman entre nuestro ranking y cada uno de los 4
- [ ] Identificar **discrepancias notables**: modelos overrated en HumanEval que fallan en coding aplicado nuestro, modelos underrated que rinden mejor de lo esperado
- [ ] Actualizar paper draft con sección "Cross-validation with established benchmarks" citando los originales con BibTeX

### Approach 2 — Réplica selectiva en español (próxima semana, ~1 semana)

Aporte original donde el gap es real.

- [ ] **NIAH-ES** (Needle-in-Haystack en español)
  - 5 niveles de contexto: 4K, 16K, 64K, 256K, 1M tokens
  - Plantilla bilingüe: needle en español, haystack puede ser corpus español o inglés mixto
  - Top 15 modelos con context window suficiente
  - Suite 25 nueva: `benchmarks/tests/long_context_es.py`
  - Costo estimado: $15-30 (gratis y NIM no soportan >32K en mayoría)
  - Validar con cita a OpenCompass NIAH para metodología
- [ ] **IFEval-ES** (instruction following en español, traducción curada)
  - 500 prompts oficiales de IFEval traducidos al español neutro (no MT, curado humano)
  - Misma rúbrica strict del original
  - Aporte único: primer IFEval-ES público
  - Top 30 modelos
  - Suite 26 nueva: `benchmarks/tests/ifeval_es.py`
  - Costo: ~$5-15 + ~10h trabajo humano de curación

### ❌ NO replicar (justificado)

- **HumanEval-ES**: poco valor incremental, ya está estandarizado en EN, los modelos no se evalúan distinto en coding por idioma del prompt
- **GSM8K-ES**: traducción de problemas matemáticos no agrega — la matemática es language-agnostic
- **MMLU completo**: 14K preguntas, costo prohibitivo, los proveedores ya reportan
- **MT-Bench**: medir preferencia humana ya cubierto por LMSYS Arena, no es nuestro foco

### 🔍 A monitorear (decisión futura)

- **AgentBench / OSWorld / Terminal-Bench 2.0** — cuando crezcamos en agéntica multi-turno con sandbox, evaluar adopción
- **TruthfulQA-ES** — si el gap "modelos que mienten menos" se vuelve más relevante para usuarios LATAM (políticas regulatorias?)
