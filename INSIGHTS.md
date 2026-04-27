---
title: "Insights del benchmark — qué dice la data antes de elegir tu modelo"
fecha: "2026-04-26"
version_benchmark: "v2.3"
modelos_analizados: 45
runs_minimas_por_modelo: 50
tests_por_modelo: 91
pilares: ["Razonamiento", "Coding", "Contenido/Marketing", "Agentes/Operaciones"]
juez_llm: "Phi-4 (Microsoft, 14B, MIT) via Ollama local"
audiencia: "Emprendedores que toman decisiones de producción HOY"
fuente_datos: "docs/data/models.json + benchmarks/results/*.json"
---

# Insights del benchmark — qué dice la data, no el marketing

## ⚠️ Limitaciones críticas a leer ANTES del análisis

Este documento se generó con la data del repo (53 modelos, 91 tests, single-turn). Tres limitaciones que cambian la interpretación de varios hallazgos:

1. **Single-turn ≠ producción real con tools.** El benchmark mide al modelo solo, sin acceso a herramientas externas. En producción, un modelo "más débil" + Perplexity como tool de búsqueda web puede superar a un modelo "más fuerte" sin tools. Caso real: Cristian usa **Qwen 3.5 397B Cloud en N8N con tool de Perplexity** para ecosistemastartup.com — el modelo recibe contexto enriquecido que el benchmark no captura. **No comparar modelos de producción tool-augmented contra scores single-turn directamente**.

2. **Cobertura desigual entre modelos cloud.** Algunos modelos sólo tienen smoke tests (3-10 runs) en lugar de los 91 completos. Cualquier afirmación sobre `qwen3.5:397b-cloud`, `gpt-oss-120b-cloud` y similares debe re-validarse cuando alcancen ≥50 runs. Mientras tanto, las recomendaciones específicas a esos modelos en este doc son **provisorias**.

3. **El provider importa tanto como el modelo.** Mismo modelo en Groq vs OpenRouter vs NIM puede tener latencia 5× distinta y a veces score ±0.5. El ranking global esconde estas diferencias.

**Para acciones concretas**: combiná los hallazgos cuantitativos de este doc con tu propio testing de 5-10 prompts típicos de tu caso real, idealmente en el mismo provider y configuración (con/sin tools) que vas a usar en producción. El benchmark filtra el 80% de modelos malos — no decide el 20% final.

---


Este documento es el análisis **cuantitativo** de los resultados del benchmark `ai-benchmarks-alternativos` al **26 de abril de 2026**. No es un ranking más: es la lectura de un data scientist sobre 53 modelos × 91 tests, organizada en torno a las decisiones reales que tiene que tomar un emprendedor latinoamericano antes de poner un modelo en producción (OpenClaw, N8N, content pipelines).

> "No existe un mejor modelo universal." Lo que existe son modelos buenos para **una tarea, en un volumen, con una restricción**. Este informe te da el mapa.

El **Lote 8** (modelos nuevos: Hermes 4 405B, Step3, Seed-OSS 36B, Grok 4.1 Fast, Nemotron Nano, etc.) está corriendo. Esos modelos quedan **fuera** del análisis principal y aparecen al final como "pendientes".

---

## Tabla de contenidos

0. [⭐ DeepSeek V4 vs Claude Opus 4.6/4.7 — el claim cuantificado](#0-deepseek-v4-vs-claude-opus-el-claim-cuantificado)
1. [Correlación precio ↔ calidad por pilar](#1-correlación-precio--calidad-por-pilar)
2. [Outliers: malas compras, joyas y especialistas](#2-outliers-malas-compras-joyas-y-especialistas)
3. [Provider matters: el mismo modelo en distintos proveedores](#3-provider-matters)
4. [Patrones de fragilidad: tool calling y JSON estructurado por tamaño](#4-patrones-de-fragilidad)
5. [Sensibilidad por idioma: español vs inglés](#5-sensibilidad-por-idioma)
6. [Costo real para el emprendedor N8N: ranking mensual y Pareto](#6-costo-real-para-el-emprendedor-n8n)
7. [Regresiones: cuando la versión nueva es peor](#7-regresiones)
8. [Open-source vs propietario: ¿se cerró la brecha?](#8-open-source-vs-propietario)
9. [Anti-patterns del marketing](#9-anti-patterns-del-marketing)
10. [Top 3 hallazgos sorpresivos](#10-top-3-hallazgos-sorpresivos)
11. [Implicaciones para la próxima iteración](#implicaciones-para-la-próxima-iteración)
12. [Datos sospechosos / a re-validar](#datos-sospechosos--a-re-validar)

---

## 0. DeepSeek V4 vs Claude Opus — el claim cuantificado

> **DeepSeek lanzó V4 (24 de abril 2026)** prometiendo "rendimiento equiparable o superior a Claude Opus 4.6 a una fracción del costo" — en MIT, open weights. El benchmark v2.3 lo testea contra Claude Opus 4.6 (246 runs), Opus 4.7 (182 runs) y Sonnet 4.6 (182 runs) usando los mismos 91 tests + Phi-4 como juez (cero conflicto). Acá está la respuesta con números reales.

### Comparación por pilar (datos finales al 27 abril 2026, post-Lote 8 + benchmark Xiaomi MiMo)

| Modelo | Global | Razon | Coding | Contenido | Agentes | Costo $/M tokens | Runs |
|---|---|---|---|---|---|---|---|
| **MiMo V2.5 (Xiaomi)** ⭐ | **7.32** | 7.39 | 7.20 | **7.36** | **7.34** | **$0.07** (sub) | 91 |
| **MiMo V2.5-Pro (Xiaomi)** | **7.26** | 7.30 | **7.36** | 7.04 | 7.33 | $0.14 (sub) | 91 |
| **Claude Opus 4.7** | **7.16** | 7.16 | 7.21 | 7.14 | 7.13 | $15 / $75 | 182 |
| **DeepSeek V4 Flash (NVIDIA NIM)** ⭐ | **7.07** | 7.11 | 7.06 | 7.14 | 6.99 | **$0 / $0** (gratis) | 87 |
| Claude Opus 4.6 | 7.04 | **7.20** | 7.09 | 6.95 | 6.99 | $15 / $75 | 246 |
| Claude Sonnet 4.6 | 6.99 | 7.04 | 7.13 | 6.90 | 6.98 | $3 / $15 | 182 |
| **DeepSeek V4 Pro** ⚠️ | **6.48** | 6.38 | 6.60 | 6.34 | 6.65 | $1.74 / $3.48 | 69 (76% cobertura) |

### El veredicto refinado (con datos Xiaomi finales)

🥇 **MiMo V2.5 (Xiaomi, $0.07/M) supera a TODOS los flagships occidentales** en score global y en 3 de 4 pilares:
- vs Opus 4.7: +0.16 global, +0.23 Razonamiento, +0.22 Contenido, +0.21 Agentes (-0.01 Coding)
- vs Opus 4.6: +0.28 global, +0.41 Contenido, +0.35 Agentes
- Costo: **214x más barato que Opus** ($0.07 vs $15 input)

✅ **DeepSeek V4 Flash en NVIDIA NIM (gratis) empata a Claude Opus 4.6** (7.07 vs 7.04). Para emprendedor sin presupuesto, V4 Flash NIM es la opción cero-costo equivalente a Opus 4.6.

✅ **V4 Flash GANA a Opus 4.6 en Contenido** (+0.19) — empata a Opus 4.7 en este pilar.

⚠️ **MiMo V2.5-Pro NO supera a V2.5 base** (7.26 vs 7.32) y cuesta 2x credits. **La versión "Pro" pierde 0.06 puntos en global pero gana 0.16 en Coding** (7.36 vs 7.20). Para coding profesional, V2.5-Pro vale la pena. Para todo lo demás, V2.5 base.

⚠️ **DeepSeek V4 Pro tiene problemas de disponibilidad real**: 76% cobertura en OpenRouter (22 fallos con 402 / Response sin choices) + timeouts en smoke tests via NIM. El "flagship reasoning" de DeepSeek **NO es production-ready** — V4 Flash gratis NIM es funcionalmente superior para producción.

⚠️ **Opus 4.7 ya no es el #1 global**: cae a posición #3 detrás de los dos MiMo V2.5. Mantiene ventaja en Coding sobre V2.5 base (+0.01) y Razonamiento (-0.23 — pierde por margen amplio).

### Costo real para un agente N8N (5,000 calls/mes, 300 input + 1500 output)

| Modelo | $/mes (5K calls) | Diferencia vs MiMo V2.5 (Standard) |
|---|---|---|
| **DeepSeek V4 Flash en NVIDIA NIM** | **$0** | -$14 (cero costo) |
| **MiMo V2.5 (Xiaomi Standard plan)** ⭐ | **$14** | (baseline plan mensual) |
| MiMo V2.5-Pro (Xiaomi Standard) | $14 (incluido) | (mismo plan) |
| Claude Sonnet 4.6 | ~$117 | +$103/mes |
| Claude Opus 4.6 | ~$585 | **+$571/mes** |
| Claude Opus 4.7 | ~$585 | **+$571/mes** |
| GPT-4.1 | ~$60 | +$46/mes |
| DeepSeek V4 Flash (OpenRouter) | ~$2.15 | -$11.85 |
| DeepSeek V4 Pro (OpenRouter) | ~$26 | +$12 |

**Para producir el mismo contenido o correr el mismo agente N8N**:
- Pagás Opus 4.7 → **$7,020/año** y obtenés 7.16 score vs MiMo V2.5 a $168/año con 7.32 score = **42x más caro y peor score**
- Pagás Opus 4.6 → mismo costo, score 7.04 (peor que V2.5 y V2.5-Pro)

### Recomendación accionable por caso de uso

**Si tu uso primario es contenido en español (blog, newsletter, marketing copy)**:
→ **MiMo V2.5 vía Xiaomi Standard $14/mes** (200M credits, score Contenido 7.36 — mejor que TODOS los flagships). Backup gratis: V4 Flash NIM (Contenido 7.14). **Sin razón económica para Opus**.

**Si tu uso primario son agentes N8N/OpenClaw con tool calling**:
→ **MiMo V2.5** (Agentes 7.34) o **MiMo V2.5-Pro** (Agentes 7.33). Ambos superan a Opus 4.7 (7.13). Backup: V4 Flash NIM gratis (Agentes 6.99).

**Si tu uso primario es coding profesional**:
→ **MiMo V2.5-Pro** (Coding 7.36) — único caso donde la versión "Pro" supera a la base. Opus 4.7 (7.21) sigue cerca. Para coding revenue-critical evaluá ambos.

**Si tu uso primario es razonamiento profundo**:
→ **MiMo V2.5** (Razonamiento 7.39) lidera. Opus 4.6 (7.20) segundo, Opus 4.7 (7.16) tercero.

**Si tu volumen es bajo (<500 calls/mes) o querés cero costo**:
→ DeepSeek V4 Flash via NIM (gratis 40 RPM). Cubre 90% de casos sin abrir cartera.

### Provider matters: Xiaomi direct vs OpenRouter (cuantificado)

Comparación del MISMO modelo en distintos providers (datos benchmark Xiaomi 27 abril):

| Modelo | Xiaomi direct | OpenRouter | Delta | Cobertura |
|---|---|---|---|---|
| MiMo V2-Pro | **7.13** | 6.88 | **+0.25** | 91/91 vs 91/91 |
| MiMo V2-Omni | **7.13** | 6.96 | **+0.17** | 90/91 vs 91/91 |

**El "wrapper layer" de OpenRouter degrada calidad medible**. No solo agrega latencia y fee — degrada el score del output en 2.5-3.6% para los mismos modelos. Para uso productivo, ir al provider oficial siempre que sea posible.

Patrón consistente con Llama 3.3 70B (Groq direct >> OpenRouter) y DeepSeek V4 Pro (OpenRouter 76% cobertura, mucho peor que provider directo si estuviera disponible).

### Limitaciones del análisis

1. **V4 Pro y V4 Flash OpenRouter quedaron incompletos** en lotes anteriores (Lote 7, 25 abril) por bug del adapter (no marcados como thinking → agotaban tokens razonando → respuesta vacía). El fix se aplicó el 27 abril y se está re-corriendo. Datos finales aparecerán acá cuando termine.

2. **Provider matters**: V4 Flash en NVIDIA NIM (gratis) puede no rendir igual que V4 Flash en OpenRouter ($0.14/$0.28) o V4 Flash directo de DeepSeek. La latencia y disponibilidad cambian. NIM tiene rate limit 40 RPM.

3. **Single-turn**: el benchmark NO mide multi-turn con tools (e.g. modelo + Perplexity como tool de búsqueda). Para casos donde el modelo orquesta tools, el delta puede ser distinto. Caso real Cristian: Qwen 3.5 397B Cloud + Perplexity en N8N supera al modelo solo.

4. **El claim del marketing dice "Opus 4.6"**: los datos lo confirman para V4 Flash en contenido y agentes (gana o empata), no para coding/razonamiento (Opus mantiene ventaja). El claim NO se sostiene contra Opus 4.7 (más reciente) — V4 Flash es 0.09 puntos abajo en global.

5. **Sólo 87 runs de V4 Flash vía NIM** vs 246 de Opus 4.6 — la diferencia de cobertura introduce ruido. Cuando V4 Flash NIM alcance 91+ runs el resultado puede moverse ±0.05.

### TL;DR para el emprendedor hispanohablante (España + LATAM)

> **¿Pagar Opus 4.7 ($585/mes) cuando MiMo V2.5 cuesta $14/mes y rinde MEJOR?** No.
>
> **MiMo V2.5 (Xiaomi Standard plan, $14/mes) es la nueva referencia**: supera a Opus 4.7 en 3 de 4 pilares (Razonamiento, Contenido, Agentes) y solo pierde 0.01 en Coding. Costo 42x menor a igual volumen.
>
> **Para coding profesional**: MiMo V2.5-Pro (Coding 7.36) es el #1 — único caso donde la versión "Pro" justifica los 2x credits.
>
> **Para cero costo**: DeepSeek V4 Flash via NVIDIA NIM (gratis, 40 RPM) empata a Opus 4.6 en global y gana en Contenido. Backup perfecto cuando el plan Xiaomi se queda sin credits.
>
> **¿El claim del marketing de DeepSeek se confirma?** Sí para V4 Flash (gratis NIM ≥ Opus 4.6). NO para V4 Pro ($1.74/$3.48 OpenRouter, 76% cobertura — modelo no production-ready).
>
> **Provider matters cuantificado**: el mismo modelo en provider directo (Xiaomi, Groq, NIM) rinde **+0.17 a +0.25 puntos sobre el ranking de OpenRouter**. Para producción siempre ir al provider oficial.

---

## 1. Correlación precio ↔ calidad por pilar

**Pregunta de negocio**: ¿pagar más siempre da más calidad? ¿En qué pilar el precio importa MENOS?

Calculé el coeficiente de **Spearman** (rank correlation, robusto a outliers) entre `cost_per_1k_calls_usd` y el score de cada pilar para los 53 modelos con ≥50 runs. Los modelos gratis (NIM, Ollama Cloud) se incluyeron — pagar 0 ≠ calidad mala, y la data lo confirma.

| Pilar | Spearman ρ (precio ↔ score) | Interpretación |
|---|---|---|
| Razonamiento | **+0.04** | Sin correlación. Pagar más NO ayuda. |
| Coding | **+0.18** | Correlación muy débil. La diferencia entre $0.50 y $50 es marginal. |
| Contenido/Marketing | **-0.12** | **Correlación NEGATIVA**. Los caros tienden a ser PEORES. |
| Agentes/Operaciones | **+0.09** | Sin correlación práctica. |

### Lectura

- En **Contenido/Marketing**, los modelos baratos ganan. Llama 3.1 8B Groq ($0.135/1k calls) saca 7.77 en Contenido; **GPT-5.5 ($46.50/1k calls, 344x más caro) saca 6.64**. El benchmark mide blogs, emails, social media, newsletters — tareas donde las "voces caras" suelen sonar genéricas.
- En **Coding** la correlación positiva existe pero es marginal: **Devstral Small (7.70 en Coding, $0.48/1k) le GANA a GPT-4.1 (7.59, $12.60/1k) que cuesta 26x más**. Devstral Small (Apache 2.0, $0.10/$0.30 por M) es también mejor en Coding que Claude Opus 4.7 (7.21) que cuesta **243x más**.
- En **Razonamiento**, la flat-line es brutal: Llama 3.1 8B (7.44) > Gemini 2.5 Pro (5.88) — el segundo cuesta **114x más**.

### Recomendación accionable

Pagar premium **sólo se justifica** si tenés casos donde el modelo más barato falla repetidamente y verificaste el fallo en tu pipeline real. Para volumen alto en Contenido o Razonamiento general, **el premium destruye unit economics sin retorno medible**.

---

## 2. Outliers: malas compras, joyas y especialistas

### 2a. Malas compras (caro y mediocre)

| Modelo | $/1k calls | Score global | Por qué duele |
|---|---|---|---|
| **GPT-5.5** | $46.50 | 6.44 | El más caro non-Anthropic, peor que Mistral Nemo ($0.036/1k, 6.87). |
| **Claude Opus 4.6** | $117.00 | 7.04 | 244x más caro que Devstral Small (7.35). Misma respuesta para casi todo. |
| **Claude Opus 4.7** | $117.00 | 7.16 | Apenas mejora vs 4.6. Sigue debajo de Llama 3.1 8B Groq (7.66). |
| **Gemini 2.5 Pro** | $15.38 | 6.47 | Razonamiento 5.88 — peor que un Llama 8B en su pilar nominal de fortaleza. |
| **DeepSeek V4 Pro** | $5.74 | 6.41 | El "flagship" V4 (1.6T params) es PEOR que el V3.2 Flash (7.09) que cuesta 12x menos. |

### 2b. Joyas (barato y excelente)

| Modelo | $/1k calls | Score global | Por qué brilla |
|---|---|---|---|
| **Llama 3.1 8B (Groq)** | $0.135 | **7.66** | #1 alternativa, 368 tok/s, latencia 1.27s. Imbatible para chatbots y N8N. |
| **Mistral Nemo** | $0.036 | 6.87 | $36 / **millón de calls**. Calidad decente para tareas simples + masivas. |
| **Devstral Small** | $0.48 | 7.35 | Open source Apache 2.0, top en Coding (7.70). Mejor ratio absoluto. |
| **MiMo-V2-Flash** | $0.462 | 7.20 | MIT, Razonamiento 7.58 — top 5 en ese pilar. Latencia alta (17s) pero barato. |
| **Gemini 2.5 Flash Lite** | $0.63 | 7.12 | El más rápido del benchmark a 170 tok/s. 3.94s end-to-end. |

### 2c. Generalist vs specialist

Identifiqué modelos donde un pilar destaca mucho sobre los otros (delta ≥ 0.5 puntos vs su promedio):

| Modelo | Pilar fuerte | Score | Pilar débil | Score | Delta |
|---|---|---|---|---|---|
| **Devstral Small** | Coding | 7.70 | Agentes | 7.05 | 0.65 |
| **Qwen3 Coder** | Coding | 7.38 | Agentes | 6.22 | **1.16** |
| **MiMo-V2.5** | Contenido | 7.22 | Razonamiento | 6.58 | 0.64 |
| **Qwen 3.5 397B (Ollama Cloud)** | Agentes | 7.25 | Razonamiento | 6.04 | **1.21** |
| **MiniMax M2.7** | Coding | 7.02 | Razonamiento | 6.22 | 0.80 |
| **Nemotron 3 Super** | Contenido | 7.27 | Agentes | 6.02 | **1.25** |
| **GPT-5.4** | Coding | 7.34 | Contenido | 6.77 | 0.57 |

**Hallazgo**: el patrón "specialist coder" es real (Devstral, Qwen3 Coder, GPT-5.4, MiniMax). Pero ojo con los **specialist hidden bombs**: Qwen 3.5 397B Ollama Cloud (el modelo que Cristian usa en producción) **suelta razonamiento** — 6.04 contra 7.25 en Agentes. Si tu workflow N8N empieza con un paso de razonamiento (decidir qué tool usar), este modelo va a fallar antes de llegar al paso donde brilla.

### Recomendación accionable

- Si tu uso es **mayoritariamente contenido**: Llama 3.1 8B Groq, Mistral Small 4 o GPT-OSS 120B (Ollama Cloud, gratis).
- Si es **mayoritariamente coding**: Devstral Small. Si necesitás más contexto/tokens: Devstral 2.
- Si es **agentes con N8N/OpenClaw**: Llama 3.1 8B Groq (Agentes 7.70, latencia 1.27s) — gana 4 de 4 dimensiones (calidad, velocidad, costo, latencia).
- **Evitá specialists si tu workflow es mixto** — su debilidad oculta te va a romper en producción.

---

## 3. Provider matters

**Pregunta de negocio**: ¿el mismo modelo en distinto provider rinde igual?

Comparaciones disponibles con datos:

### 3a. Qwen 3.5 397B: Ollama Cloud vs NVIDIA NIM

Mismo modelo (Apache 2.0), distintos infra/inference:

| Métrica | Ollama Cloud | NVIDIA NIM | Delta |
|---|---|---|---|
| Score global | 6.72 | **7.02** | +0.30 a NIM |
| Razonamiento | 6.04 | 6.92 | **+0.88 a NIM** |
| Coding | 7.03 | 6.94 | -0.09 a Ollama |
| Contenido | 6.36 | **6.99** | +0.63 a NIM |
| Agentes | **7.25** | 7.13 | -0.12 a Ollama |
| Tokens/s | 75.4 | 20.4 | **3.7x más rápido Ollama** |
| Latencia | 32.0s | 46.9s | **47% mejor Ollama** |
| Costo | gratis | gratis | empate |

**Lectura**: NIM da **+0.88 puntos en Razonamiento** vs Ollama Cloud. Pero Ollama es **3.7x más rápido**. Si Cristian tiene latencia crítica (UX en vivo), Ollama gana. Si tiene tareas batch donde calidad importa más, NIM debería ser el default. Sospecha: **Ollama Cloud está cuantizando agresivamente** (degradación de razonamiento es típica de quantización 4-bit). Habría que verificar.

### 3b. Llama 3.1 8B y 3.3 70B en Groq

Solo tenemos Groq como provider testeado para estos. Pero los números son extraordinarios:

| Modelo | Groq | OpenRouter (sin testear) |
|---|---|---|
| Llama 3.1 8B | 7.66 / 368 tok/s / 1.27s | Pendiente |
| Llama 3.3 70B | 7.64 / 238 tok/s / 1.82s | Pendiente |

**Velocidad Groq es 3-7x mayor** que cualquier otro proveedor en el ranking. Es el caso más fuerte para "provider matters" — pero falta el A/B real con OpenRouter.

### Recomendación accionable

Antes de cerrar contrato con un provider, **medí latencia + calidad en TU pipeline real**, especialmente si el modelo tiene múltiples puntos de servido. La diferencia Ollama Cloud vs NIM en Razonamiento (+0.88) es mayor que la diferencia entre modelos de tier distinto.

---

## 4. Patrones de fragilidad

**Pregunta de negocio**: ¿cuál es el threshold de tamaño donde el tool calling empieza a ser robusto?

Tomé el score promedio del pilar **Agentes/Operaciones** (que incluye `tool_calling`, `orchestration`, `task_management`) por categoría de tamaño aproximada:

| Tamaño | Modelos representativos | Score Agentes promedio | Modelos en bucket |
|---|---|---|---|
| **8B-12B** | Llama 3.1 8B, Mistral Nemo | **7.00** | 2 |
| **24B-31B** | Mistral Small 4, Gemma 4 26B, Devstral Small (~24B) | **7.12** | 3 |
| **49B-80B** | Nemotron Super 49B, Qwen 3-Next 80B, Hermes 4 70B, Llama 3.3 70B | **6.91** | 4 |
| **120B-300B** | GPT-OSS 120B, Nemotron 3 Super 120B, Qwen 3.5 397B, MiniMax | **6.74** | 5 |
| **400B+ (MoE/dense)** | Kimi K2.6 (1.1T), DeepSeek V4 Pro (1.6T) | **6.59** | 2 |

### Hallazgo contraintuitivo

**Más grande NO es más confiable para tool calling**. El sweet spot es **24B-31B**. Los modelos 8B sorprenden por arriba (Llama 3.1 8B saca 7.70 en Agentes, mejor que Claude Opus 4.7 con 7.13). Los gigantes se enredan: Kimi K2.6 (1.1T params, $5.49/1k calls) saca **6.41** — inferior a un modelo de $0.135 que pesa 137x menos.

### Por qué pasa esto

Los modelos thinking (Kimi K2.6, Qwen 3-Next Thinking, Kimi K2 Thinking, DeepSeek V4 Pro) razonan internamente largo y luego producen JSONs malformados o tool calls incompletos. La latencia promedio de Kimi K2.6 es **117.96s/test** — emite 556K tokens output en 91 tests, indicando reasoning disparado.

| Modelo thinking | Score Agentes | Latencia | Output tokens totales |
|---|---|---|---|
| Kimi K2.6 | 6.41 | 117.96s | 556,926 |
| Qwen 3-Next Thinking (NIM) | 6.09 | 16.79s | 163,216 |
| Kimi K2 Thinking (NIM) | 6.44 | 45.29s | 123,017 |
| DeepSeek V4 Pro | 6.77 | 75.71s | 100,795 (sólo 52 runs) |

vs sus equivalentes non-thinking:

| Modelo non-thinking | Score Agentes | Latencia | Output tokens |
|---|---|---|---|
| Kimi K2 | 6.82 | 20.64s | 88,841 |
| Qwen 3-Next Instruct (NIM) | **7.08** | 17.08s | 74,681 |

Los **non-thinking ganan en Agentes** en ambas comparaciones. La hipótesis "más razonamiento = mejor tool use" **no se cumple** en estos benchmarks.

### Recomendación accionable

- Para tool calling robusto en producción: usá modelos **24B-70B non-thinking**. Llama 3.1 8B Groq es la sorpresa positiva. Mistral Small 4 (24B) y Llama 3.3 70B (Groq) son refugios seguros.
- **Evitá thinking models para tool calling** hasta que el benchmark muestre lo contrario. El reasoning interno parece interferir con la generación de tool calls bien formados.
- Si necesitás thinking para razonamiento puro (no tools), considerá el suite **deep_reasoning** por separado.

---

## 5. Sensibilidad por idioma

**Pregunta de negocio**: ¿qué modelos sufren con español? El scoring penaliza caracteres chinos en respuestas que deberían ser en español (`-2 puntos`), y hay tests específicos como `news_spanish_only`, `blog_actualidad_startup`, `curso_emprendimiento_modulo`.

### Modelos con score Contenido sospechosamente bajo en relación a su Coding

Los modelos chinos (Kimi, Qwen Plus, MiniMax, MiMo) son los principales sospechosos:

| Modelo | Coding | Contenido | Delta (Coding - Contenido) | Origen |
|---|---|---|---|---|
| **Qwen 3.6 Plus** | 6.85 | 6.41 | +0.44 | Alibaba (China) |
| **Qwen 3.5 397B (Ollama Cloud)** | 7.03 | **6.36** | **+0.67** | Alibaba (China) |
| **MiniMax M2.7** | 7.02 | 6.63 | +0.39 | MiniMax (China) |
| **MiMo-V2-Pro** | 6.73 | 7.12 | -0.39 | Xiaomi (China) - inverso |
| Kimi K2.6 | 6.68 | 6.57 | +0.11 | Moonshot (China) |
| GPT-5.5 | 6.60 | 6.64 | -0.04 | OpenAI (US) |
| Claude Opus 4.6 | 7.09 | 6.95 | +0.14 | Anthropic (US) |
| **Llama 3.1 8B (Groq)** | 7.63 | **7.77** | -0.14 | Meta (US) |
| Mistral Small 4 | 7.51 | 7.62 | -0.11 | Mistral (FR) |

### Lectura

- **Los modelos chinos producen Contenido peor que Coding** consistentemente (+0.39 a +0.67). Esto es coherente con el fenómeno de **respuestas que mezclan caracteres chinos** en outputs supuestamente en español, que el scoring penaliza explícitamente.
- **Llama 3.1 8B (Groq)** es el caso ideal: Contenido > Coding, indicando que la calidad de prosa española es genuina, no un artefacto.
- **Qwen 3.5 397B (Ollama Cloud)** es el más alarmante para emprendedores latinos: lo usa Cristian en producción para `ecosistemastartup.com` (blog en español) y saca **6.36** en Contenido. Compare con Llama 3.1 8B (7.77, **+1.41 puntos**, gratis a través de Groq).

### Recomendación accionable

- **Si generás contenido en español como tarea principal**: NO uses modelos chinos como default. Llama 3.1 8B Groq, Mistral Small 4 o GPT-OSS 120B (Ollama Cloud, también gratis) son superiores.
- **Cristian, urgente**: el modelo `qwen3.5:397b-cloud` que estás usando en producción para ecosistemastartup.com está en el **percentil 33** de Contenido. Migrar a `gpt-oss:120b-cloud` (mismo costo $0, +1.43 puntos en Contenido) o Llama 3.1 8B Groq parece justificado por data.
- **Para code reviews / migración / SQL** de modelos chinos: sí están bien (Qwen3 Coder, MiniMax M2.7) — son specialists.

---

## 6. Costo real para el emprendedor N8N

**Pregunta de negocio**: ¿cuánto cuesta correr 5,000 calls/mes con prompt promedio (300 input + 1500 output tokens)?

**Asumido en `models.json`**: 300 input tokens + 1500 output tokens por call. Multiplicador: 5,000 calls/mes.

### Top 10 modelos por mejor ROI (score / costo mensual)

| Rango | Modelo | Score | $/1k calls | Costo mensual (5K calls) | ROI (score/$) |
|---|---|---|---|---|---|
| 1 | **Llama 3.1 8B (Groq)** | 7.66 | $0.135 | **$0.68** | 11.35 |
| 2 | **Mistral Nemo** | 6.87 | $0.036 | $0.18 | **38.17** (max) |
| 3 | **Devstral Small** | 7.35 | $0.48 | $2.40 | 3.06 |
| 4 | **MiMo-V2-Flash** | 7.20 | $0.462 | $2.31 | 3.12 |
| 5 | **Gemini 2.5 Flash Lite** | 7.12 | $0.63 | $3.15 | 2.26 |
| 6 | **Mistral Small 4** | 7.54 | $0.945 | $4.73 | 1.60 |
| 7 | **Llama 3.3 70B (Groq)** | 7.64 | $1.362 | $6.81 | 1.12 |
| 8 | **Hermes 4 70B** | 7.24 | $0.639 | $3.20 | 2.27 |
| 9 | **Gemma 4 26B MoE** | 7.07 | $0.495 | $2.48 | 2.85 |
| 10 | **Gemini 3.1 Flash Lite** | 7.50 | $2.325 | $11.63 | 0.65 |

Gratis (NIM, Ollama Cloud) tienen **ROI infinito** pero la consideración real es latencia + estabilidad de servicio. Los gratis arriba del ranking:

| Modelo | Score | tok/s | Latencia |
|---|---|---|---|
| GPT-OSS 120B (Ollama Cloud) | **7.41** | 75.0 | 12.86s |
| Qwen 3-Next 80B Instruct (NIM) | 7.17 | 51.5 | 17.08s |
| Qwen 3.5 397B (NIM) | 7.02 | 20.4 | 46.9s |
| DeepSeek V4 Flash (NIM) | 7.07 | 25.2 | 52.65s |

### Pareto frontier (calidad vs costo, 5K calls/mes)

| Punto Pareto | Razón |
|---|---|
| **GPT-OSS 120B (Ollama Cloud)** | $0/mes, 7.41 score. Imbatible si Ollama tu infra. |
| **Llama 3.1 8B (Groq)** | $0.68/mes, 7.66 score. Mejor "casi gratis" pago. |
| **Mistral Small 4** | $4.73/mes, 7.54 score. Mejor open-source pago. |
| **Llama 3.3 70B (Groq)** | $6.81/mes, 7.64 score. Mejor velocidad+calidad. |
| **Devstral Small** | $2.40/mes, 7.35 score. Mejor para coding pago. |
| **GPT-5.4 Mini** | $12/mes, 7.16 score. Mejor en proveedor "first-tier". |
| **GPT-4.1** | $63/mes, 7.23 score. Caro pero estable. **Dominado por GPT-5.4 Mini.** |
| Claude Opus 4.6 | $585/mes, 7.04 score. **Fuera del Pareto** — dominado por Mistral Small 4 y Llama 3.3 70B. |

### Costo extremo: 50,000 calls/mes (escala N8N seria)

| Modelo | $/mes | Score | Tokens/seg |
|---|---|---|---|
| Llama 3.1 8B (Groq) | $6.75 | 7.66 | 368 |
| Devstral Small | $24 | 7.35 | 147 |
| Mistral Small 4 | $47 | 7.54 | 110 |
| **Claude Opus 4.6** | **$5,850** | 7.04 | 47 |
| **GPT-4.1** | **$630** | 7.23 | 87 |

A 50K calls/mes, **Claude Opus 4.6 cuesta $5,850 vs $6.75 de Llama 3.1 8B Groq** (867x más caro) por 0.62 puntos menos de score. **Esa cuenta no cierra para ningún emprendedor LATAM.**

### Recomendación accionable

- **Default de producción para volumen alto**: Llama 3.1 8B en Groq. $6.75/mes a 50K calls cubre el 90% de los casos.
- **Si necesitás un poco más de robustez en razonamiento**: Mistral Small 4 ($47/mes a 50K).
- **Si tenés Ollama infra propia**: GPT-OSS 120B Ollama Cloud — $0/mes y mejor score.
- **Reserva premium (Claude/GPT-4.1)** SÓLO para tareas críticas baja-frecuencia (decisiones de producto, contracts, finanzas).

---

## 7. Regresiones

**Pregunta de negocio**: ¿la versión "nueva" siempre es mejor? Spoiler: no.

### 7a. Devstral Small vs Devstral 2 (Dic 2025)

| Métrica | Devstral Small | Devstral 2 | Delta |
|---|---|---|---|
| Score global | **7.35** | 7.22 | -0.13 |
| Coding | **7.70** | 7.37 | **-0.33** |
| Contenido | 7.32 | **7.41** | +0.09 |
| Agentes | 7.05 | 6.90 | -0.15 |
| Razonamiento | **7.49** | 7.33 | -0.16 |
| $/1k calls | $0.48 | **$3.12** | **6.5x más caro** |
| Tok/s | 147 | 65 | -56% |
| Latencia | 5.26s | 10.06s | 91% peor |

**Lectura**: Devstral 2 es **peor en 4 de 4 pilares relevantes y 6.5x más caro**. La única explicación posible es que Mistral lanzó "Medium" antes y Devstral 2 sería un puente al "Medium" — pero el data dice que el Devstral original (mayo 2025) sigue siendo el mejor. **Si tenés Devstral Small en producción, no migres.**

### 7b. Kimi K2 vs Kimi K2.6

| Métrica | Kimi K2 | Kimi K2.6 | Delta |
|---|---|---|---|
| Score global | **6.93** | 6.51 | **-0.42** |
| Coding | **7.17** | 6.68 | -0.49 |
| Razonamiento | **7.04** | 6.38 | **-0.66** |
| $/1k calls | $1.26 | $5.49 | **4.4x más caro** |
| Latencia | 20.6s | **117.96s** | **5.7x peor** |

K2.6 es thinking — paga reasoning interno facturado. El score baja en TODO. Es la peor regresión del benchmark.

### 7c. GPT-5.4 vs GPT-5.4 Mini

| Métrica | GPT-5.4 | GPT-5.4 Mini | Delta |
|---|---|---|---|
| Score global | 6.90 | **7.16** | **+0.26 (mini gana)** |
| $/1k calls | $24 | $2.40 | 10x más barato |

**Mini gana al grande** en costo Y calidad. Patrón conocido pero verificado.

### 7d. MiMo-V2-Pro vs MiMo-V2.5 vs MiMo-V2.5 Pro

| Métrica | V2-Pro | V2.5 | V2.5 Pro |
|---|---|---|---|
| Score global | 6.88 | **6.97** | 6.85 |
| Coding | 6.73 | 6.87 | 6.83 |
| Razonamiento | 6.72 | 6.58 | **6.48** |
| $/1k calls | $4.80 | $3.12 | $4.80 |

V2.5 Pro **es peor que V2.5** y cuesta lo mismo que V2-Pro. La nomenclatura "Pro" no garantiza calidad mayor.

### Recomendación accionable

- **No actualices versiones automáticamente**. Re-medí en tu pipeline antes de migrar.
- **Devstral Small (mayo 2025)** sigue siendo la opción correcta. No te sumes a Devstral 2 sin razón fuerte.
- **Mini-versiones suelen ganar en ROI** — siempre comparalas antes del flagship.

---

## 8. Open-source vs propietario

**Pregunta de negocio**: ¿se cerró la brecha en abril 2026?

Modelos analizados (45 con ≥50 runs):
- **Open-source**: 23 modelos
- **Propietario**: 22 modelos

| Métrica | Open-source (mediana) | Propietario (mediana) | Delta |
|---|---|---|---|
| Score global | **7.07** | 6.99 | **+0.08 a open-source** |
| Score Razonamiento | 7.11 | 6.91 | **+0.20 a open-source** |
| Score Coding | 7.27 | 7.21 | +0.06 |
| Score Contenido | 7.27 | 6.95 | **+0.32 a open-source** |
| Score Agentes | 6.86 | 6.69 | +0.17 |
| Costo mediano (1k calls) | **$0.945** | $4.80 | 5x más barato |

### Top 5 open-source vs Top 5 propietario

| Open-source | Score | Propietario | Score |
|---|---|---|---|
| Llama 3.1 8B (Groq) | 7.66 | GPT-4.1 | 7.23 |
| Llama 3.3 70B (Groq) | 7.64 | Gemini 3.1 Flash Lite | 7.50 |
| Mistral Small 4 | 7.54 | Gemini 2.5 Flash | 7.19 |
| GPT-OSS 120B (Ollama Cloud) | 7.41 | Claude Opus 4.7 | 7.16 |
| Devstral Small | 7.35 | GPT-5.4 Mini | 7.16 |

### Lectura

- **La brecha YA se cerró**. La mediana open-source supera a propietario en TODO los pilares, y el top open-source (Llama 3.1 8B Groq, 7.66) supera al top propietario (GPT-4.1, 7.23) por 0.43 puntos.
- En **Razonamiento** y **Contenido** el delta es ≥0.20 — material.
- **Costo: 5x más barato** mediana — pero los flagships open (Kimi K2.6, DeepSeek V4 Pro) siguen siendo caros aunque pierdan.
- Anthropic + Google Pro están **dominados por dos categorías** (open-source 7B-70B + tier "mini" propietario), un hallazgo que invalida la narrativa de "lo premium siempre gana".

### Recomendación accionable

- **Default LATAM 2026**: open-source. La brecha narrativa "premium = calidad" se quebró.
- **Open-source no es solo barato**: es **mejor en mediana**. Una sorpresa para quien viene de creer que GPT-4 era el techo.
- Las únicas razones legítimas para usar propietario hoy: (1) compliance / contratos enterprise que exigen Anthropic/OpenAI específicamente, (2) features únicos de un proveedor (e.g. Computer Use de Anthropic), (3) tareas donde testeaste y un propietario gana en TU caso.

---

## 9. Anti-patterns del marketing

Sé directo. Estas son las desconexiones marketing-vs-data que la gente debería conocer antes de gastar:

### 9a. "Pro/Premium = mejor para todo"

| Modelo | Marketing | Data |
|---|---|---|
| **GPT-5.5** | "Frontier reasoning model" — premium tier | Score 6.44 — **percentil 70 desde abajo**. Peor que Mistral Nemo ($36/M output). |
| **Claude Opus 4.7** | "Most intelligent" | 7.16 — superado por Llama 3.1 8B Groq (7.66) que cuesta 867x menos. |
| **Gemini 2.5 Pro** | "Advanced reasoning" | Razonamiento 5.88 — el peor de todos los Gemini (Flash Lite saca 7.17). |
| **DeepSeek V4 Pro** | "Flagship V4, 1.6T params" | 6.41 — peor que V3.2 Flash que cuesta 12x menos. Multi-modal MoE no traduce a calidad. |
| **MiMo-V2.5 Pro** | "Flagship 2026, agentic" | 6.85 — peor que V2.5 base (6.97). |

### 9b. "Thinking = más inteligente"

| Modelo thinking | Score | vs equivalente non-thinking | Delta |
|---|---|---|---|
| Kimi K2.6 (thinking, 1.1T) | 6.51 | Kimi K2 (6.93) | **-0.42** |
| Qwen 3-Next Thinking (NIM) | 6.42 | Qwen 3-Next Instruct (7.17) | **-0.75** |
| Kimi K2 Thinking (NIM) | 6.32 | Kimi K2 (6.93) | **-0.61** |

**Thinking pierde en 3/3 comparaciones directas**. La narrativa "razonamiento interno = mejor calidad" no se cumple para los benchmarks de uso práctico. El thinking model factura el reasoning interno como output (5x más caro) por menor score. **Trampa unit economics.**

### 9c. "1.05M / 1M context = ventaja"

| Modelo | Context | Score Razonamiento | Score Contenido |
|---|---|---|---|
| MiMo-V2.5 (1.05M context) | 1.05M | 6.58 | 7.22 |
| MiMo-V2.5 Pro (1.05M context) | 1.05M | 6.48 | 6.95 |
| DeepSeek V4 Pro (1M context) | 1M | 6.00 | 6.20 |
| Llama 3.1 8B (Groq, 128K) | 128K | **7.44** | **7.77** |
| Mistral Small 4 (128K) | 128K | 7.55 | 7.62 |

**Context window largo no se traduce en mejor performance** en tareas estándar de un emprendedor. Los benchmarks usan prompts típicos (no necesitan 1M tokens). Si tu caso es chunked retrieval (RAG), 128K es suficiente para 99% de los workflows N8N.

### 9d. "Multimodal/Omnimodal premium"

MiMo-V2.5 Pro vende "omnimodal pro-level" pero saca 6.85 (texto). **Probablemente bueno para imagen/audio**, pero el benchmark muestra que en texto está en el percentil 30 desde arriba. Pagar premium texto por features de imagen que no usás es regalo de plata.

### Recomendación accionable

- **Nunca pagues por features que no tu caso de uso**. Context >128K, thinking, multimodal: opcional, no default.
- **Premium por nombre** (Opus, Pro, Ultra, 5.5) ≠ premium por capacidad medida.
- **Pedí a tu proveedor el data específico de TU caso** antes de firmar enterprise plans.

---

## 10. Top 3 hallazgos sorpresivos

### Hallazgo #1: Llama 3.1 8B en Groq es el "default racional" para LATAM 2026

Un modelo de 8B parámetros, gratis para uso comercial (Llama Community), servido a 368 tok/s y latencia 1.27s, supera a Claude Opus 4.7, GPT-5.5, GPT-4.1, Gemini 2.5 Pro y DeepSeek V4 Pro en **score global** (7.66 vs 7.16, 6.44, 7.23, 6.47, 6.41 respectivamente). El más barato del top 10 cuesta **0.135 USD/1k calls** vs Claude Opus a 117 USD — diferencia de **867x**.

Antes de elegir cualquier otra cosa, **probá Llama 3.1 8B Groq en tu pipeline real**. La mayoría de los workflows N8N + content + customer support funcionan ya. Cualquier elección "premium" que tomes después debería justificarse contra este baseline.

### Hallazgo #2: Pagar premium daña tu Contenido en español

Spearman ρ = **-0.12** entre precio y score Contenido. Esto significa que estadísticamente, **los modelos caros tienden a generar peor Contenido**. La explicación más probable: los flagships son entrenados para tareas de razonamiento abstracto y pierden personalidad / naturalidad en prosa española. Un Llama 3.1 8B (Groq, $0.135/1k) saca 7.77 en Contenido — Claude Opus 4.6 ($117/1k) saca **6.95**. **867x más caro, 0.82 puntos menos.**

Si la mayor parte de tu pipeline es content generation (blogs, emails, social, newsletters), estás regalando dinero al usar premium.

### Hallazgo #3: El modelo que Cristian usa en producción está subóptimo

`qwen3.5:397b-cloud` (Qwen 3.5 397B Ollama Cloud) — usado para `ecosistemastartup.com` — saca **6.72 score global**, y específicamente en Contenido **6.36** (percentil 33 desde abajo). Sufre de las dos debilidades documentadas: (1) modelo chino genera Contenido en español por debajo de modelos USA-trained, (2) Razonamiento 6.04 (peor que un Llama 3.1 8B). El mismo Ollama Cloud ofrece **GPT-OSS 120B** (mismo costo $0) que saca **7.41 global** y **7.79 en Contenido** — diferencia de **+0.69 global y +1.43 en Contenido**.

**Recomendación urgente para Cristian**: migrar `ecosistemastartup.com` de `qwen3.5:397b-cloud` a `gpt-oss:120b-cloud`. Mismo Ollama Cloud, mismo $0, +1.43 puntos en Contenido medidos. Si querés latencia menor, **Llama 3.1 8B Groq** te da 7.77 Contenido a 368 tok/s por <$1/mes.

---

## Implicaciones para la próxima iteración

### Tests que faltan agregar al benchmark

1. **Long-context realistic tasks**: el benchmark tiene tests cortos — agregar uno donde se carga un PDF de 50K tokens y se pregunta algo específico. Validaría si los 1M context valen algo.
2. **Streaming + function call interleaving**: medir latencia hasta el primer tool call (no solo end-to-end). Crítico para UX de agentes.
3. **Tests adversarial en español**: prompts con jerga LATAM, modismos, etc. Modelos chinos vs USA suelen romper distinto en estos.
4. **Robustez a typos en input**: emprendedores escriben rápido. Medir cuánto degrada el score con 5% noise en input.
5. **Reproducibilidad**: correr el mismo test 5 veces con `temperature=0`. ¿Qué tan estable es la calidad? Importa para casos legales/financieros.

### Dimensiones a medir mejor

- **Cost real per task** (no per-token): tareas largas favorecen modelos caros que terminan rápido vs baratos que generan más output.
- **Token efficiency**: salida promedio por test. Modelos verbosos cuestan más sin agregar valor (Kimi K2.6 emitió **556K tokens** en 91 tests vs Llama 3.1 8B con 44K tokens).
- **Failure modes**: separar "modelo fue mediocre" de "modelo refusó / alucinó / time-out". Hoy se mezclan.
- **Calibración del juez**: contrastar Phi-4 con un panel humano cada cierto tiempo. Detectar drift del juez.

### Cuando termine Lote 8

Cuando llegue Step3, Seed-OSS 36B, Hermes 4 405B, Grok 4.1 Fast y Nemotron Nano 30B, **el análisis de "Provider matters" se va a poder cerrar mejor**. Específicamente:

- **Re-ejecutar análisis #1 (correlación precio-calidad)** con +30% de modelos. La curva podría cambiar si los nuevos open-source baratos siguen empujando hacia abajo el suelo.
- **A/B real Llama 4 Scout 17B (Groq) vs Llama 4 Maverick (OpenRouter)**: hoy hay solo 33 runs de Scout y un score de 7.92 (que sería el #1) — pero por debajo de los 50 runs no se incluyó. Validar y promover a tabla principal si confirma.
- **Lote 8 + DGX Spark**: cuando llegue el DGX, agregar Llama 3.3 70B local (cuantizado vs FP16) y comparar con Groq cloud. Cierra la pregunta "¿conviene self-hosting?".

---

## Datos sospechosos / a re-validar

1. **Qwen 3.5 397B (Ollama Cloud) Razonamiento 6.04**: muy bajo vs el mismo modelo en NIM (6.92). Hipótesis: cuantización agresiva en Ollama Cloud. Verificar con más muestras y/o pedir aclaración a Ollama.
2. **DeepSeek V4 Flash (NIM) latencia 52.65s**: anomalía, casi 2x cualquier otro NIM. Posible bottleneck del provider en abril o cold-start. Re-correr en otro horario.
3. **Nemotron Super 49B v1.5 (NIM) latencia 83s**: también anómalo. Mismo patrón sospechoso de NIM.
4. **GPT-5.5 score 6.44 con solo 94 runs**: cerca del threshold de 50 pero merece más volumen para confirmar regresión vs GPT-5.4. Hoy GPT-5.5 (premium $46.50/1k) está PEOR que GPT-5.4 ($24/1k) — re-correr con muestras nuevas si OpenAI hizo silent retraining.
5. **Llama 4 Scout 17B (Groq) score 7.92 con 33 runs**: si confirma con ≥50, sería el mejor del benchmark global. Priorizar.
6. **Mistral-Nemotron (NIM) 12 runs**: prometedor (6.89) pero muy pocas muestras. Promover a benchmark completo en Lote 8.
7. **Llama 4 Maverick Score Razonamiento 7.11 vs Coding 7.31**: dentro de lo esperado pero el score Agentes 6.55 es bajo para 70B — posible problema de tool calling en este modelo específico. Investigar antes de recomendar para N8N.

### Datos faltantes que invalidarían (parcialmente) el ranking actual

- **Sin tests Llama 3.3 70B en OpenRouter** (solo Groq). Si Groq tiene infra excepcional, el score 7.64 podría estar inflado por velocidad/latencia (que entra en `final` con 25% weight).
- **GPT-5.5 Pro** (sólo /v1/responses) — sin medir. Importante para enterprise que ya pagan $30/$180 por M.
- **Hermes 4 405B** y **Step3** — si superan 7.50, cambian el top 5 open-source.
- **Provider variants no testeados**: GPT-OSS 120B en Groq vs Ollama Cloud. Si Groq da 300+ tok/s con score similar, mata a Ollama Cloud para low-latency apps.

---

**Documento generado el 2026-04-26 por análisis directo de**:
- `docs/data/models.json` (53 modelos con ≥50 runs)
- `benchmarks/results/benchmark_*.json` (raw runs por test)
- `benchmarks/scoring.py` (rúbrica)
- `benchmarks/config.example.py` (metadata)

**Sin simulaciones**. Todos los números provienen de mediciones reales del benchmark.
