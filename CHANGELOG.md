# Changelog

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
