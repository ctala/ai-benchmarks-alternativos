<!-- doc: generado -->
# Benchmark de Modelos AI Alternativos: comparación abierta de LLMs en español para N8N, Hermes y emprendedores

**Versión v4.7.1** | Última actualización: 19 de agosto de 2026 | [📊 Datasheet junio](DATASHEET_2026-06.md) · [📄 CheatSheet PDF julio](cheatsheet/AI_Model_Benchmark_CheatSheet_Julio_2026.pdf) · [📄 Executive Brief julio](cheatsheet/AI_Model_Benchmark_ExecutiveBrief_July_2026.pdf)

> **Encuentra alternativas a Claude, GPT-5 y Gemini** comparadas con <!-- AUTO:tests_marketing -->65,000+<!-- /AUTO --> tests reales: calidad, costo, velocidad, latencia y tool calling. Pensado para emprendedores latinoamericanos que construyen agentes en N8N o Hermes con presupuestos reales.

> 📍 **Qué es este benchmark (y qué NO es)**: este benchmark **NO sustituye** a los benchmarks académicos validados (HumanEval, MMLU, GSM8K, SWE-bench Verified, NIAH original en inglés, MT-Bench, LMSYS Arena). Es un **complemento** diseñado específicamente para **emprendedores hispanohablantes** que necesitan decidir qué modelo usar en situaciones reales (N8N, Hermes, blogs de actualidad, soporte cliente, agentes, contenido en español neutro). Para investigación académica o capacidades fundamentales del modelo, prioriza los benchmarks oficiales — citados en [BENCHMARKS_EXTERNOS.md](BENCHMARKS_EXTERNOS.md). Para **decidir qué modelo poner en producción para un caso de uso aplicado en español**, esto suma información que los benchmarks oficiales no cubren: costo en provider real, latencia desde Latam, español neutro, agentes multi-turno, y debugging real (que medimos vía cross-ref con SWE-bench/Hermes-Eval, NO replicamos).

> ⚠️ **No existe un "mejor modelo" universal.** "Coding" significa cosas distintas si desarrollás *plugins de WordPress*, *templates de N8N*, *scripts de automatización* o *proyectos grandes*. Lo mismo con contenido (blog técnico ≠ copy de marketing ≠ newsletter), soporte al cliente o agentes. **Este benchmark nació porque, como emprendedor, no encontré tests que me ayudaran a decidir para mis casos reales** — ahora existen y son tuyos.

Benchmark de modelos AI para emprendedores y equipos que usan agentes (N8N, Hermes). Evalua modelos en los 4 pilares del emprendedor: **Razonamiento, Coding, Contenido/Marketing, y Agentes/Operaciones**. Incluye LLM-as-Judge local con Phi-4 (Microsoft, cero conflicto de interes) y la nueva suite **`agent_long_horizon`** que mide capacidades agénticas en multi-turno largo (lo que el single-turn no captura).

**Cobertura actual**: <!-- AUTO:tested_count -->156<!-- /AUTO --> modelos con ≥20 runs (<!-- AUTO:total_models -->205<!-- /AUTO --> catalogados, incluido **Claude Fable 5** medido el día 1), juez Phi-4 (servido en vLLM FP16 sobre DGX Spark). **v4.2 (ago 2026)** = **dimensión agéntica**: 74 modelos medidos *dentro de un agente real* (Harbor + Docker + herramientas), resolviendo una cotización de punta a punta. Se publica **aparte del índice de calidad**, porque son preguntas distintas — Hermes 4 405B tiene calidad 8,20 y **0,00** ahí. **v4.1 (ago 2026)** = el titular es el **índice de calidad** en escala **absoluta** (`quality_avg` sin z-scorear, 10 = perfecto en todo el examen): agregar un modelo ya no mueve el score de nadie y una cifra citada no caduca. Precio y latencia se reportan **al lado**, nunca dentro. **v4.0 (jul 2026)** = la **referencia z-score quedó congelada por versión** (`scoring_reference.json`): agregar o medir un modelo nuevo ya no recalcula el score de los demás — se puntúa contra una referencia fija. **v3.0.2 (junio)** = ajuste de **normalización de costos**: todos los modelos se comparan con un costo mínimo de referencia de **$0.001/call**, y los que no tienen equivalente OpenRouter usan su costo real de provider como aproximación estándar. **v2.8 (junio)** = long-context y seguridad como **dimensiones separadas** del score general, tras descubrir que la suite NIAH-es en español nos mentía de [5 formas distintas](DATASHEET_2026-06.md) (needles-secreto, lumping, el juez no ve el needle, overshoot de tokens, needles distintos por tamaño). Con medición limpia, el retrieval long-context **no discrimina** a los modelos top — los diferenciadores reales son el **contexto usable** (declarado ≠ usable: MiniMax M3 dice 1M, usable 512K) y la **resistencia a fuga de credenciales** (Opus 4.8 8.79 rehúsa, los cheap filtran).

## Cómo se puntúa, en 20 líneas

**El titular es el índice de calidad, y va solo.** Escala absoluta 0-10: 10 sería perfecto
en todo el examen. Precio y latencia se reportan **al lado**, nunca mezclados dentro.

> Hasta v4.0 publicábamos un número que mezclaba calidad con precio, y movía modelos sin
> avisar: Claude Opus 4.6 era **#5 en calidad** y salía **#18**. Las dos cifras eran
> verdad, bajo un rótulo que no lo decía.

Lo que **no** entra al titular, y se reporta como dimensión propia:

| dimensión | qué responde |
|---|---|
| **Agéntica** | ¿el modelo puede EJECUTAR una tarea de negocio dentro de un agente? |
| **Seguridad** | ¿resiste que le saquen datos con prompt injection? |
| **Contexto largo** | ¿cuánto contexto usa de verdad, no cuánto declara? |
| **Tool calling** | ¿usa bien las herramientas, o solo dice que puede? |

⚠️ **El índice de calidad NO predice el trabajo agéntico, y está medido:** Hermes 4 405B
tiene calidad **8,20** y saca **0,00** dentro de un agente. Gemini 3.6 Flash es **#76 de
80** en calidad y **#3 de 80** en calidad agéntica. Si vas a poner un modelo a operar,
mirá esa columna, no el promedio.

**Piso para rankear: 50 runs.** Con 3-12 un modelo lidera por azar.

📐 **El detalle del método está en [METODOLOGIA.md](METODOLOGIA.md)** · las decisiones
vigentes, en [DECISIONES.md](DECISIONES.md).

## Ranking — índice de calidad

<!-- AUTO-RANKING-START -->

> Auto-generado por `benchmarks/generate_readme_ranking.py` desde `docs/data/models.json`. **No editar a mano** — el z-score se recalcula con cada modelo nuevo y una tabla escrita a mano queda obsoleta sola.

### Índice de calidad — ¿qué modelo responde mejor?

Solo calidad. **El precio y la velocidad se muestran al lado, no van dentro del número** — un modelo caro no es peor, es caro, y mezclarlo esconde cuál es cuál.

| # | Modelo | Calidad | $/1k calls | Latencia | Provider | Runs |
|---|---|---:|---:|---:|---|---:|
| 1 | **GPT-5.6 Luna** | **8.52** | $0.93 | 11s | openrouter | 162 |
| 2 | **Qwen 3.7 Flash** | **8.49** | $0.20 | 29s | openrouter | 163 |
| 3 | **Tencent Hy3** | **8.49** | $0.83 | 62s | openrouter | 143 |
| 4 | **Gemma 4 31B** | **8.48** | $0.54 | 17s | openrouter | 143 |
| 5 | **Claude Opus 4.8** | **8.48** | $39.00 | 20s | openrouter | 165 |
| 6 | **Claude Opus 4.6** | **8.48** | $39.00 | 33s | openrouter | 213 |
| 7 | **Qwen 3.8 27B** | **8.47** | $4.93 | 65s | openrouter | 686 |
| 8 | **Qwen 3.6 Max** | **8.46** | $9.55 | 107s | openrouter | 173 |
| 9 | **DeepSeek R1 (reasoning)** | **8.45** | $3.96 | 121s | openrouter | 158 |
| 10 | **Inkling Small** | **8.43** | $1.94 | 102s | openrouter | 143 |

### Calidad por dólar — ¿cuánto rinde cada peso?

Calidad dividido por lo que cuesta. **Premia lo barato a propósito**: un modelo de calidad media a $0,10 le gana a uno excelente a $1. Mirá la columna *Calidad* para ver qué estás resignando.

| # | Modelo | Calidad/$ | Calidad | $/1k calls | Provider |
|---|---|---:|---:|---:|---|
| 1 | **Ling 3.0 Flash** | **79.0** | 7.98 | $0.10 | openrouter |
| 2 | **Llama 3.1 8B Instant** | **53.8** | 7.26 | $0.14 | openrouter |
| 3 | **Nex-N2-Mini** | **51.5** | 8.13 | $0.16 | openrouter |
| 4 | **Solar Pro 4** | **42.5** | 8.04 | $0.19 | openrouter |
| 5 | **Poolside Laguna XS 2.1** | **41.7** | 8.26 | $0.20 | openrouter |
| 6 | **Qwen 3.7 Flash** | **41.6** | 8.49 | $0.20 | openrouter |
| 7 | **GPT-OSS 20B** | **36.1** | 7.91 | $0.22 | openrouter |
| 8 | **GPT-OSS 120B** | **28.9** | 8.11 | $0.28 | openrouter |
| 9 | **DeepSeek V4 Flash 0731** | **27.4** | 8.05 | $0.29 | openrouter |
| 10 | **Poolside Laguna S 2.1** | **26.6** | 7.89 | $0.30 | openrouter |

### Frontera de Pareto — ¿cuáles vale la pena siquiera considerar?

Los **13 de 94** modelos que nadie domina: para el resto existe otro que es **a la vez mejor, más barato y más rápido**. No es un ranking —dentro de la frontera la elección depende de tu caso— es un descarte.

| Modelo | Calidad | $/1k calls | Latencia | Provider |
|---|---:|---:|---:|---|
| **GPT-5.6 Luna** | 8.52 | $0.93 | 11s | openrouter |
| **Qwen 3.7 Flash** | 8.49 | $0.20 | 29s | openrouter |
| **Tencent Hy3** | 8.49 | $0.83 | 62s | openrouter |
| **Gemma 4 31B** | 8.48 | $0.54 | 17s | openrouter |
| **Poolside Laguna XS 2.1** | 8.26 | $0.20 | 10s | openrouter |
| **Gemini 3.5 Flash Lite** | 8.23 | $3.84 | 5s | openrouter |
| **GPT-5.4 Mini** | 8.17 | $2.40 | 7s | openai_direct |
| **KAT Coder Air v2.5** | 8.13 | $0.94 | 7s | openrouter |
| **Nex-N2-Mini** | 8.13 | $0.16 | 17s | openrouter |
| **Gemini 3.1 Flash Lite** | 8.09 | $2.33 | 4s | openrouter |
| **Ling 3.0 Flash** | 7.98 | $0.10 | 12s | openrouter |
| **Llama 4 Scout 17B** | 7.88 | $0.48 | 8s | openrouter |
| **Gemini 2.5 Flash Lite** | 7.84 | $0.63 | 5s | openrouter |

> **Piso de ranking: 50 runs.** Solo compiten los 94 modelos con muestra sólida. Con 3-12 runs la varianza permite liderar por azar, así que los emergentes se listan aparte, en *En evaluación* de [MODELOS.md](MODELOS.md), con su score marcado como indicativo.

> **Por qué la calidad va sola.** Hasta v4.0 publicábamos un número que mezclaba calidad con precio, y movía modelos sin avisar: Claude Opus 4.6 es **#5 en calidad** y salía **#18**; Poolside Laguna XS es **#29** y salía **#7**. Las dos cifras eran verdad, pero bajo un rótulo que no lo decía. Ahora el precio se muestra al lado y cada quien decide qué pesa. Es lo mismo que hace [Artificial Analysis](https://artificialanalysis.ai/) con su Intelligence Index.

> **La frontera es frágil a propósito, y conviene saberlo.** Basta un modelo nuevo, bueno y barato para que varios de esta lista queden dominados de un día para otro. Eso es lo que debe pasar. Pero también significa que **depende de que los datos del líder sean correctos**: si la calidad del tope está sobreestimada, la frontera se ensancha.

> **Nada de esto es tu caso exacto.** Si corrés batch de noche, la latencia no te importa y acá está pesando; si atendés usuarios en vivo, te importa el doble. Ajustá los pesos en la [calculadora](https://benchmarks.cristiantala.com/) o mirá las tablas por caso de uso en [MODELOS.md](MODELOS.md).

<!-- AUTO-RANKING-END -->

## 🎛️ Calculadora interactiva

**[https://benchmarks.cristiantala.com/](https://benchmarks.cristiantala.com/)** — encuentra el modelo IA perfecto en 30 segundos.

Filtros: presupuesto mensual, calls/mes, calidad mínima, velocidad mínima, tarea (razonamiento / coding / contenido / agentes), sub-categoría específica, contexto efectivo mínimo, open-source, excluir Big-3 propietarios, tool calling, thinking, multimodal. Ranking por score global ajustable con sliders (quality/costo/velocidad/latencia). Datos del último benchmark, regenerados automáticamente.

> **Tip**: si no sabés qué pesos usar, empezá con el preset que se acerque a tu perfil (Personal, Solopreneur, PyME, Producción) o con las tablas por caso de uso en [MODELOS.md](MODELOS.md).

## Lo que te ahorras al usar este benchmark

Para responder *"qué modelo usar para mi agente N8N / qué tan bueno es Kimi K2.6 vs DeepSeek / cuál es el mejor open-source para code"* tendrías que correr esto tú mismo. Acá ya está hecho:

| Recurso invertido | Cantidad |
|---|---|
| Modelos en config | **<!-- AUTO:total_models -->205<!-- /AUTO --> únicos** |
| Modelos con cobertura completa (≥20 runs) | **<!-- AUTO:tested_count -->156<!-- /AUTO -->** |
| Modelos con datos parciales (1-19 runs) | **17** (incluye variantes thinking de modelos hybrid) |
| Tests por modelo | **186 tests en 31 suites** (incluye multi-turno) |
| Runs preservados en JSON | **<!-- AUTO:tests_marketing -->65,000+<!-- /AUTO -->** (con éxito) |
| Tokens consumidos (preservados) | ~2.5M input + ~7M output |
| **Costo APIs (OpenAI/OpenRouter/MiniMax/Anthropic/Xiaomi)** | **~$350-400 USD** desde el 11 de abril, + gasto continuo de OpenRouter cada mes para las actualizaciones |
| **Suscripciones + modelos simultáneos** (Xiaomi, MiniMax, Claude, Ollama Cloud — varias a la vez para poder probar) | **~$300/mes** |
| **Tiempo wall-clock** del benchmark (cómputo cloud) | **~190h** acumuladas |
| **Tiempo de cómputo local** (Phi-4 judge en Mac M-series + DGX Spark) | **~50h GPU** |
| **Tiempo humano** (diseño de tests, debugging, análisis, docs) | **~80-100h** |
| Iteración de metodología | cientos de runs no documentados antes del scoring v2 |

**Costo real de mantener este benchmark**: APIs **$350-400** acumuladas + **~$300/mes en suscripciones simultáneas** (Xiaomi, MiniMax, Claude, Ollama Cloud — varias a la vez para probar modelos) + gasto continuo de OpenRouter cada mes para las actualizaciones + **130-150h de cómputo** entre cloud y local + **80-100h de trabajo humano** (research, debugging, análisis, docs). Acá ya está hecho — disponible bajo MIT.

> El número "$200+" no es solo lo medido. Hay 4 categorías de costo que el `cost_usd` calculado **NO captura**:
>
> 1. **Iteración de metodología** (cientos de runs antes de instrumentar `cost_usd`/`output_tokens`): exploración de qué tests, qué scoring, qué juez, cómo medir thinking models.
> 2. **Respuestas vacías facturadas a precio completo**: 165+ corridas de thinking models (Kimi K2.6, GPT-5.5, GLM-5.1, Nemotron) consumieron `max_tokens=2048` razonando y devolvieron `content=""`. **OpenRouter cobra esos tokens igual** — el modelo razonó, los tokens se generaron. Solo que no llegaron como respuesta visible.
> 3. **Timeouts cobrados**: requests que sobrepasaron el timeout cliente fueron abortados desde nuestro lado, pero el provider ya había generado la respuesta y nos la facturó.
> 4. **Retries del usuario y del runner**: cada retry con `--rerun-empty` / `--rerun-failed` es una invocación nueva. Algunos tests se corrieron 3-4 veces hasta llegar a un score válido.
>
> El cálculo automático con `python benchmarks/calculate_costs.py --markdown` da una estimación sobre los runs preservados con PRICING actualizado. **El dashboard de OpenRouter reporta más** acumulado — la diferencia incluye iteración de metodología no preservada en JSONs, retries, y otros consumos del usuario en OpenRouter.

Regla práctica: **un emprendedor que quiera replicar este benchmark desde cero gastaría ~$100-200 en APIs + ~50h de trabajo + el costo invisible de iterar la metodología**. Acá ya está hecho con todos los hallazgos — abre [RECOMENDACIONES.md](RECOMENDACIONES.md) y elegí por plataforma + tarea + presupuesto.

## Modelos en suscripción mensual (NO son gratis)

⚠️ **Algunos modelos aparecen con `$0/call` pero requieren pagar suscripción mensual**. La calculadora los marca con `★ Sub $X/mes`. Catálogo de suscripciones disponibles:

| Suscripción | Plan | Precio/mes | Modelos incluidos | Notas |
|---|---|---|---|---|
| **Ollama Cloud** | Pro | **$30** | GPT-OSS 120B, DeepSeek V4 Pro, V4 Flash, Qwen 3.5 397B, Qwen 3.5 default | Rate limit varía. Recomendado para uso mid (1-10k calls/día). |
| **Xiaomi MiMo Standard** | Standard | **$14** | MiMo V2.5, V2.5-Pro, V2-Pro, V2-Omni (4 modelos) | 200M credits/mes. Off-peak 16-24 UTC = 0.8x consumption. |
| **MiniMax Agent Pro** | Agent Pro | **$19** | MiniMax M2.7 Highspeed (acceso a baja latencia) | Generosos límites para agentes (1k+ calls/día). |
| **Anthropic Pro** | Pro | $20 | Claude (web only — NO API access) | NO da acceso API, solo claude.ai. No aplica para automatización. |
| **xAI SuperGrok** | Standard | $30 | Grok 4 / 4.1 (web only — NO API access) | $30/mes o $300/año. Grok 4.3 + multi-agente requieren SuperGrok Heavy $300/mes. No aplica para automatización. |

**Modelos realmente $0/call (sin suscripción)**:
- **NIM gratis (NVIDIA)**: 20 modelos. Rate limit 40 RPM. Marcados `★ NIM 40rpm`.
- **Local**: corren en tu hardware (DGX Spark, Mac M-series, GPU dedicada). Marcados `★ Local`. Costo real = electricidad + amortización del hardware.
- **Groq, OpenRouter, OpenAI, Anthropic API**: pay-as-you-go por token, sin suscripción mensual fija. Costos reales en `$/1k calls` en la calculadora.

## Documentos Principales

### Análisis y decisión
| Documento | Contenido |
|-----------|-----------|
| ⭐ [INSIGHTS.md](INSIGHTS.md) | **Análisis cuantitativo del benchmark**: correlaciones, outliers, Pareto, regresiones, hallazgos sorpresivos |
| [RECOMENDACIONES.md](RECOMENDACIONES.md) | Qué modelo usar por plataforma (N8N, Hermes), tarea y presupuesto |
| [CASOS_DE_USO.md](CASOS_DE_USO.md) | 50+ casos de uso reales de IA para emprendedores |
| [DESCUBRIMIENTOS.md](DESCUBRIMIENTOS.md) | Hallazgos no obvios y bugs de modelos |

### Inventarios y referencia
| Documento | Contenido |
|-----------|-----------|
| [MODELOS.md](MODELOS.md) | Inventario completo: probados, en cola y por agregar al config |
| [TESTS.md](TESTS.md) | 186 tests en 31 suites (auto-generado desde benchmarks/tests/) |
| ⭐ [THINKING_EXPLAINED.md](THINKING_EXPLAINED.md) | **Extended thinking explicado**: qué es, qué modelos lo tienen (thinking-only / hybrid / sin reasoning), cómo lo medimos en el benchmark, hallazgos clave (thinking no siempre ayuda) |
| [BENCHMARKS_EXTERNOS.md](BENCHMARKS_EXTERNOS.md) | Triangulación con HumanEval/GSM8K/IFEval/MMLU oficiales — top 30 modelos, 50/120 celdas con score numérico, hallazgos de validez convergente y discriminante |
| [COMPARATIVA.md](COMPARATIVA.md) | 35+ modelos con precios, open-source/propietario, licencias |
| [SUSCRIPCIONES.md](SUSCRIPCIONES.md) | Suscripciones fijas ($0-$300/mes) + coding plans |
| [PACKS.md](PACKS.md) | Packs por suscripcion + estrategia local+nube |
| [PROVEEDORES.md](PROVEEDORES.md) | Proveedores: fundacion, foco, contexto, open-source |

### Para contribuir o forkear
| Documento | Contenido |
|-----------|-----------|
| 🛠️ [ARQUITECTURA.md](ARQUITECTURA.md) | **Documentación técnica deep**: runner, scoring, judge, decisiones de diseño, recetas para extender |
| 📚 [tutoriales/](tutoriales/) | **5 guías paso a paso**: replicar benchmark, agregar modelo, tests custom, Phi-4 setup, elegir modelo |
| [AGENTS.md](AGENTS.md) | Guía para agentes IA consumidores (Claude Code, Cursor) — JSON machine-readable |
| [ROADMAP.md](ROADMAP.md) | Roadmap y pipeline de mejoras futuras |
| [CHANGELOG.md](CHANGELOG.md) | Historial de cambios |

## Quick Start

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
# Editar .env con tu OPENROUTER_API_KEY (única key obligatoria)
python benchmarks/runner.py --quick                          # Todos los modelos, 1 run
python benchmarks/runner.py --quick --judge                  # Con LLM-as-Judge (Phi-4 local)
python benchmarks/runner.py --models minimax-m2.7 deepseek-v3  # Modelos especificos
python benchmarks/runner.py --tier cheap                     # Solo tier economico
python benchmarks/runner.py --list-models                    # Ver modelos disponibles
python benchmarks/runner.py --list-tests                     # Ver tests disponibles
```

## Modelos Incluidos

El catálogo completo vive en [MODELOS.md](MODELOS.md) y en la [calculadora](https://benchmarks.cristiantala.com/). A junio 2026 hay **145 modelos catalogados** de múltiples providers:

- **Cloud vía OpenRouter**: DeepSeek, Qwen, MiniMax, Mistral, Google Gemini, xAI Grok, Cohere, Poolside, etc.
- **Providers directos**: Anthropic Claude Code, MiniMax directo, Groq, NVIDIA NIM, Xiaomi MiMo, Ollama Cloud.
- **Locales en DGX Spark / Ollama**: Gemma 4, Qwen 3.6 base, Llama 4, Nemotron, DiffusionGemma, Qwen 3.5 family.

> Las listas por tier y precio cambian cada mes. Para la versión actualizada usar `MODELOS.md` o filtrar en la calculadora.

## Preguntas frecuentes (FAQ)

**¿Cuál es la mejor alternativa a Claude para agentes N8N en 2026?**
Depende de la tarea, presupuesto y volumen. Las alternativas consistentes son Qwen 3-Next 80B, Ling 3.0 Flash y Llama 3.3 70B en Groq. El ranking cambia cada mes — ver [calculadora](https://benchmarks.cristiantala.com/) y [MODELOS.md](MODELOS.md) para filtrar por caso de uso.

**¿Vale la pena pagar GPT-5 o Claude Opus si hay alternativas más baratas?**
Para tareas estándar (contenido, traducción, agentes simples), las alternativas open-source/cheap suelen dar resultados comparables. Para razonamiento profundo, código complejo, seguridad de datos sensibles o tool calling crítico, los premium aún tienen ventajas medibles. El delta real está en [INSIGHTS.md](INSIGHTS.md) y [DESCUBRIMIENTOS.md](DESCUBRIMIENTOS.md).

**¿Qué modelos open-source recomiendan para correr local?**
Para hardware ≥64GB RAM (o DGX Spark 128GB): Qwen 3.6 base, Mistral Small 4, Gemma 4 y GPT-OSS. Ver [RECOMENDACIONES.md](RECOMENDACIONES.md) y [docs/modelos-open-source-local/](https://benchmarks.cristiantala.com/modelos-open-source-local/) para guía completa por hardware.

**¿Por qué usar Phi-4 como juez en vez de GPT-4 o Claude?**
Cero conflicto de interés (ningún proveedor del benchmark es también el juez), corre 100% local, gratis, licencia MIT y rúbrica en español. Detalles en sección [Eleccion del modelo juez y sesgo](#eleccion-del-modelo-juez-y-sesgo).

**¿Cómo replico el benchmark en mi propio hardware?**
Ver [Quick Start](#quick-start) y [Como Replicar el Benchmark](#como-replicar-el-benchmark). Necesitás Python 3.10+, Ollama (para Phi-4 judge) y al menos OPENROUTER_API_KEY para empezar.

**¿Puedo usar este benchmark para decidir qué modelo poner en producción?**
Sí — fue diseñado para eso. Pero validá en tu caso específico: replicá 5-10 prompts típicos de tu producto contra los 2-3 finalistas. Ningún benchmark sustituye prompts reales de tu negocio. En la [comunidad Skool](https://www.skool.com/cagala-aprende-repite/about) compartimos plantillas y workshops para esa validación.

## Para agentes IA consumidores (Claude Code, Cursor, etc.)

Este repo está pensado también para que **agentes IA puedan consumirlo y recomendar modelos basados en datos reales**, no en su entrenamiento (que probablemente está desactualizado).

- **[AGENTS.md](AGENTS.md)** — guía de decisión completa con reglas, anti-patterns y templates de respuesta
- **[docs/data/models.json](https://benchmarks.cristiantala.com/data/models.json)** — JSON con todos los modelos, scores por pilar, costos, licencias
- **[docs/data/agents-decision-guide.json](https://benchmarks.cristiantala.com/data/agents-decision-guide.json)** — schema estructurado de casos de uso → modelos recomendados

Ejemplo mínimo en Python:

```python
import json, urllib.request

GUIDE = json.loads(urllib.request.urlopen(
    'https://benchmarks.cristiantala.com/data/agents-decision-guide.json'
).read())

# Agente recibe pregunta sobre N8N templates
caso = next(uc for uc in GUIDE['use_cases'] if uc['id'] == 'coding_n8n_templates')
print(f"Recomendación: {caso['top_models'][0]['model_id']}")
print(f"Razón: {caso['top_models'][0]['reason']}")
```

Si construís un agente que recomiende modelos, leé AGENTS.md primero — la regla #0 es **"no existe un mejor modelo universal"**.

## Comunidad y soporte

- 💬 **[Cágala, Aprende, Repite (Skool)](https://www.skool.com/cagala-aprende-repite/about)** — comunidad de emprendedores latinoamericanos usando IA
- 📧 **[Newsletter Cristian Tala](https://cristiantala.com/newsletter/)** — análisis de modelos y casos reales
- 📺 **[YouTube](https://www.youtube.com/@cristiantalasanchez)** — workshops y tutoriales
- 💼 **[LinkedIn](https://linkedin.com/in/ctala)** — ecosistema startup chileno
- 🐛 **[Issues en GitHub](https://github.com/ctala/ai-benchmarks-alternativos/issues)** — bugs, sugerencias, modelos a agregar
