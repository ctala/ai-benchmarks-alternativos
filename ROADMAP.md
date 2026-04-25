# Roadmap del Benchmark

> Ultima actualizacion: 23 de Abril de 2026
> Estado del ranking: **v2.1.0 con 17 modelos × 91 tests = 1512 runs** evaluados con juez Phi-4. Top 5: Devstral Small, GPT-5.4 Mini, GPT-4.1, Gemini 2.5 Flash Lite, MiMo-V2-Flash. Ver [README.md](README.md).

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

- [ ] Topics/tags GitHub: ai-benchmark, llm-comparison, n8n, openclaw, startup-tools, ai-agents
- [ ] Badges en README (modelos testeados, última actualización, license, CI)
- [ ] Link a Skool en footer del README y CheatSheet
- [ ] Blog post en cristiantala.com con resultados y link al repo
- [ ] Social cards (Open Graph image) para compartir
- [ ] CheatSheet PDF regenerado con resultados v2.1
- [ ] Sección "Contributing" + issue templates (agregar modelo, reportar resultado, sugerir test)
- [ ] CheatSheet visualmente atractivo para LinkedIn

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
