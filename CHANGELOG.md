# Changelog

## [1.3.0] - 2026-04-16

### Agregado
- **4 modelos Xiaomi MiMo**: MiMo-V2-Pro ($1/$3, 1T params), MiMo-V2-Flash ($0.09/$0.29, MIT), MiMo-V2-Flash free, MiMo-V2-Omni ($0.40/$2, multimodal)
- **Suite ocr_extraction** (5 tests): Facturas, tarjetas de presentacion, recibos con verificacion matematica, tablas de dashboard, notas manuscritas con OCR errors
- **Suite orchestration** (5 tests): Planificacion multi-paso, recuperacion de errores, descomposicion de workflows, seleccion precisa de herramientas, juicio paralelo vs secuencial
- **Suite multi_turn** (4 tests): Iteracion de contenido con feedback, soporte que escala, cambio de requisitos a mitad de camino, debugging iterativo
- **Suite policy_adherence** (4 tests): Politicas de reembolso bajo presion, proteccion de datos ante ingenieria social, reglas de idioma/tono, limites de alcance de servicio
- **LLM-as-Judge** (`--judge`): Usa Claude Haiku 4.5 via OpenRouter como evaluador automatico. Evalua 5 dimensiones (precision, relevancia, profundidad, claridad, utilidad) + criterios extra por suite (originalidad, empatia, planificacion, etc.). Combina 30% score automatico + 70% juez. Costo ~$0.07 por modelo (~$0.001/evaluacion).
- Total: 77 tests en 19 suites (antes: 59 tests en 15 suites)
- Xiaomi como nuevo proveedor en PROVEEDORES.md y COMPARATIVA.md

### Mejorado (Scoring v2 - correccion de sesgo)
- **Formato reducido de 3 a 2 puntos** en score_content_quality (era 30% del score de calidad, ahora 20%)
- **Secciones requeridas subidas de 3 a 4 puntos** para priorizar contenido sobre formato
- **Busqueda de secciones ahora ignora acentos** ("titulo" encuentra "título") via normalizacion Unicode
- **Penalizacion de caracteres chinos** en respuestas en espanol (hasta -2 pts). Mitiga problema de MiniMax y Qwen.
- **Nuevo score_expected_answer()** que valida respuestas contra criterios especificos:
  - `reasoning`: verifica que key_insights esten presentes (60% de palabras clave)
  - `hallucination_check`: evalua si el modelo dice "no se" en preguntas trampa
  - `creativity_check`: penaliza cliches (-1.5 a -5 puntos segun cantidad)
  - `depth_check`: penaliza frases genericas, premia datos concretos y riesgos
  - `honesty_check`: evalua transparencia sobre incertidumbre
  - `numeric`, `sequence`, `range`: validacion de respuestas factuales
- **Sin juez**: tests con expected_answer usan 40% formato + 60% sustancia
- **Con juez** (`--judge`): usa 30% automatico + 70% LLM-as-Judge

### Por que estos cambios (contexto)
- El scoring anterior daba 30% de los puntos de calidad por formato markdown (headers, bold, listas)
- Tests como deep_reasoning, creativity, hallucination tenian `expected_answer` definido pero NUNCA se validaba
- La lista de cliches en creativity.py existia pero no se usaba en el scoring
- Esto hacia que modelos rapidos y baratos que formateaban bien (Devstral) dominaran sobre modelos con mejor razonamiento
- El nuevo scoring valida sustancia: insights correctos, honestidad, creatividad real, datos precisos
- Los tests multi-turno y policy_adherence miden capacidades criticas para agentes reales que los tests single-turn no capturan
- LLM-as-Judge agrega evaluacion semantica que el scoring regex no puede hacer (calidad de analogias, empatia, utilidad practica)
- Benchmarks de referencia: HELM (Stanford), tau-Bench (Sierra), BFCL (Berkeley), LMSYS Arena

## [0.8.0] - 2026-04-12

### Agregado
- 6 modelos nuevos: Devstral Small, GPT-4.1, GPT-4.1 Mini, Mistral Large, Kimi K2, Kimi K2.5
- Claude Opus 4.6 (el #1 del mundo en Arena)
- 21 modelos en ranking global total
- Nota sobre limitaciones del scoring automatico

### Resultados Destacados
- Devstral Small es #1 (7.40) - open-source Apache 2.0, 171 tok/s, ultra barato
- GPT-4.1 es #2 (7.28) - supera a GPT-5.4 (#19), confirma hallazgo previo
- Claude Opus 4.6 es #13 (6.59) - scoring no captura calidad de razonamiento
- Kimi K2 es #16 (6.49) - decente pero no tan bueno como en benchmark manual previo

### Descubierto
- Scoring automatico favorece formato sobre sustancia
- GPT-4.1 consistentemente supera GPT-5.4 en tests estructurados
- Devstral Small de Mistral es una joya oculta

## [1.1.0] - 2026-04-12

### Agregado
- Suite hallucination: 3 tests (trampas factuales, fidelidad al contexto, citas falsas)
- Suite creativity: 4 tests (hooks sin cliches, analogias, profundidad, storytelling)
- DESCUBRIMIENTOS.md con observaciones no obvias
- Ranking global actualizado con 48 tests por modelo, 951 runs totales
- Recomendaciones expandidas: 11 casos de uso con modelo recomendado
- CheatSheet PDF actualizado a 9 paginas con alucinaciones y creatividad

### Resultados
- Alucinaciones: Claude Sonnet #1 (7.62), Anthropic = mas honesto
- Creatividad: Devstral #1 (6.93), MiniMax ultimo (5.19)
- Claude Opus sube a #9 global (desde #13) con los tests de calidad
- Claude Sonnet sube a #7 global (desde #12)

### Hallazgos
- Claude es el modelo mas honesto pero no el mas creativo
- MiniMax M2.7 es generico y con cliches en contenido
- MiniMax y Qwen a veces responden con caracteres chinos

## [0.7.0] - 2026-04-12

### Agregado
- Llama 4 Maverick via OpenRouter - #6 global, empata con Claude, open-source
- Qwen3 Coder via OpenRouter - #8 global, bueno para coding
- Gemma 4 31B y 26B MoE via OpenRouter - lentos pero funcionales
- Ranking actualizado con 12 modelos (14 contando variantes)
- Tabla solo alternativas (sin Anthropic/OpenAI) con 8 modelos

### Resultados
- Llama 4 Maverick (6.70): Sorpresa, empata con Claude Sonnet 4.6 y es open-source
- Qwen3 Coder (6.62): Solido para coding
- Gemma 4 26B MoE (6.53): Decente pero lento via OpenRouter (19 tok/s)
- Gemma 4 31B (6.42): Mas lento aun (11 tok/s), rate limits frecuentes

## [0.6.0] - 2026-04-11

### Agregado
- GPT-5.4 y GPT-5.4-mini via API directa de OpenAI
- Ranking global con 9 modelos medidos (10 contando duplicados de MiniMax por provider)
- Tabla separada "Solo Alternativas" (sin Anthropic/OpenAI)
- Tabla "Mejor por Categoria" con top 3
- Tabla "Recomendacion para Agentes N8N/OpenClaw"
- Soporte max_completion_tokens para GPT-5.4+

### Resultados
- GPT-5.4 Mini: Sorpresa, gana al GPT-5.4 en todas las categorias
- GPT-5.4 Mini: #1 en tool calling (7.5), ideal para agentes
- DeepSeek V3.2 se mantiene #1 global (7.09)
- Gemini 2.5 Flash Lite: 212 tok/s, el mas rapido por lejos

## [0.5.0] - 2026-04-11

### Agregado
- CLAUDE.md para continuidad entre sesiones de agentes
- Tests de generacion de imagenes MiniMax Image-01 (5/5 exitosos)
- Tests de TTS MiniMax (requiere plan Agent, no funciona con Coding Plan)
- Modelos nuevos: Gemma 4 31B, Gemma 4 26B MoE, Claude Sonnet 4.6, Gemini 2.5 Flash Lite, Qwen3 Coder 480B
- PROVEEDORES.md actualizado
- Image generation results en benchmarks/results/images/

### Descubierto
- MiniMax Coding Plan no incluye TTS (speech-02). Requiere plan Agent ($19/$69)
- MiniMax Image-01 funciona con Coding Plan token key
- Gemma 4 via OpenRouter es lento (~8 tok/s) - mejor correr local en DGX Spark

## [0.4.0] - 2026-04-11

### Agregado
- PROVEEDORES.md: Guia de contexto de cada proveedor (fundacion, foco, fortalezas, open-source)
- Resultados de benchmark en README.md
- Soporte API directa de MiniMax (M2.7 y M2.7 Highspeed)
- Tests de startup_content: blog ecosistemastartup.com, cursos, workshops, newsletters
- Repo privado en GitHub: ctala/ai-benchmarks-alternativos

### Resultados
- Benchmark general: DeepSeek V3.2 (7.05) > MiniMax M2.7 (6.40) > Qwen 3.6 Plus (6.08)
- MiniMax M2.7 vs Highspeed: diferencia marginal (~1%), practicamente iguales
- DeepSeek gana en 6/7 categorias, MiniMax gana en tool calling

### Corregido
- Runner: timeout robusto con signal alarm, output en texto plano
- Model IDs: Qwen 3.6 Plus free deprecado, MiniMax highspeed solo via API directa

## [0.3.0] - 2026-04-11

### Agregado
- PACKS.md: Guia de packs por suscripcion (MiniMax, Qwen, OpenAI, Google, Ollama, OpenRouter, xAI)
- Estrategia de optimizacion local + nube para DGX Spark
- Rankings completos por categoria (6 categorias con top 8-10 modelos cada una)
- Diagrama de routing: que modelo usar para que tarea
- Fecha de ultima actualizacion en todos los documentos

### Modificado
- COMPARATIVA.md: Rankings expandidos con listas completas en vez de solo el lider
- README.md: Version 0.3.0, referencia a PACKS.md

## [0.2.0] - 2026-04-11

### Agregado
- Modelos nuevos: Gemma 4 (31B, 26B MoE), Llama 4 Maverick, MiniMax M2.7 Highspeed
- Columna "Open Source" en todas las comparativas
- Seccion de modelos locales para NVIDIA DGX Spark (128GB)
- Suscripciones de MiniMax (Coding Plan $10-$150, Agent $19/$69)
- Suscripciones de Alibaba/Qwen (Coding Pro $50/mes)
- Ollama Cloud ($0/$20/$100)
- CHANGELOG.md para versionamiento

### Modificado
- Correccion: Anthropic SI funciona con OpenClaw/N8N via API key, la suscripcion Pro/Team NO da acceso API
- Modelos locales expandidos para aprovechar los 128GB del DGX Spark
- Config actualizado con modelos open-source marcados con licencia

## [0.1.0] - 2026-04-11

### Agregado
- Estructura inicial del proyecto
- COMPARATIVA.md con 30+ modelos organizados por tier de costo
- SUSCRIPCIONES.md con todas las suscripciones fijas ($0-$300/mes)
- 7 suites de benchmark con 18 tests totales
- Motor de benchmark (runner.py) con soporte OpenRouter
- Sistema de scoring multi-criterio (calidad, velocidad, costo, tool calling)
- Adaptador unificado para APIs compatibles OpenAI
- Soporte para Ollama local y Ollama Cloud
