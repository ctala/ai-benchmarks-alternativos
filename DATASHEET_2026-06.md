---
title: "Datasheet junio 2026 — v2.8: long-context honesto, seguridad, y 5 formas en que el NIAH-es miente"
mes: "2026-06"
fecha_snapshot: "2026-06-02"
version_benchmark: "v2.8.0"
audiencia: "Lectores que quieren ver evolución mes a mes y los hallazgos nuevos"
---

# 📊 Datasheet junio 2026 — qué cambió vs mayo

> 📍 **Disclaimer**: este benchmark NO sustituye a los benchmarks académicos validados (HumanEval, MMLU, SWE-bench, NIAH inglés). Es un complemento para emprendedores hispanohablantes que deciden qué modelo poner en producción HOY. Ver [README.md](README.md) y [DATASHEET_2026-05.md](DATASHEET_2026-05.md) para el snapshot anterior.

## TL;DR de junio

El release de junio **no se trató de coronar un modelo nuevo** — se trató de descubrir que nuestra propia medición de long-context en español **estaba mintiendo de 5 formas distintas**, arreglarlas, y construir dos mediciones honestas (retrieval real + seguridad). El aporte del mes es **metodológico**, y es el más valioso que publicamos hasta ahora.

## Cobertura mayo vs junio

| Métrica | Mayo (v2.6) | Junio (v2.8) | Δ |
|---|---|---|---|
| Modelos catalogados | 113 | **127** | **+14** |
| Modelos con cobertura ≥50 runs | 72 | **80** | **+8** |
| Modelos con NIAH-es (retrieval real, grilla nueva) | 21 (suite vieja) | **~17** (grilla 8K–800K) | rediseñada |
| Modelos con suite de seguridad (`prompt_injection_es`) | 0 | **~17** | **NUEVO** |
| Juez | Phi-4 Ollama (Q4) | **Phi-4 vLLM FP16** en DGX Spark | continuous batching |

## Modelos nuevos medidos en junio

| Modelo | Tipo | Hallazgo |
|---|---|---|
| **MiniMax M3** (OR + directo/sub) | Caso activo de Cristian | Sucesor de M2.7, 1M declarado. Paridad OR≈sub. **Pero contexto usable real = 512K** (erorea a 800K). |
| **DeepSeek V4 Flash** | Open, $0.098 | **#9 general** — alta calidad práctica, barato. |
| **Qwen 3.6 base 27B/35B** | Open Apache 2.0 | Cierra el gap (antes solo teníamos el 3.6 Plus propietario). |
| **Qwen3-Coder-Next** | Open coding | Sólido en coding. |
| **DeepSeek R1** | Reasoning | Rinde **menos** que V4 Flash en tareas prácticas (thinking ≠ mejor). |
| **Claude Opus 4.8** | Flagship premium | Quality top (8.4) pero **#66** — el costo $5/$25 lo hunde. **Rey de seguridad (8.79)**. |
| **Gemini 3.5 Flash** | Flagship | Long-context = igual al 2.5 Flash Lite (no peor, ver hallazgo #5). |
| **Qwen 3.6 Max** | Propietario premium | Completa base+Plus+Max. |

## 🌟 El hallazgo del mes: 5 formas en que el NIAH-es nos mentía

Empezamos junio creyendo que medíamos *retrieval de contexto largo en español*. Descubrimos, capa por capa, que **no**:

1. **Needles-secreto → medía fuga, no retrieval.** Los needles eran credenciales ("API key — NO COMPARTIR"). Eso volvió el test uno de **resistencia a inyección de prompt**: los modelos seguros rehúsan (el juez los premia), los que extraen el dato son penalizados por "filtrar". → MiniMax M3 "lideraba" long-context por **rehusar**, no por su contexto. **Fix:** needles neutros (hechos públicos).
2. **NIAH lumped en el score general.** Las suites niah eran ~54% del conteo de tests y se medían desigual entre modelos (unos 120 tests niah, otros 0) → distorsionaban el ranking. **Fix:** long-context pasa a dimensión separada (v2.8). Efecto: DeepSeek V4 Flash saltó de **#63 a #9**.
3. **El juez no ve el needle.** Phi-4 recibe solo `prompt_preview[:500]`, nunca el needle (enterrado al 25–75% de 8K–800K) → marca extracciones **correctas** como alucinación (judge 1-2) y hunde el score. **Fix:** niah se puntúa solo con el regex de extracción, sin juez. (DeepSeek 8K: 4.96 → 8.6.)
4. **La heurística de tokens excedía el contexto.** 4 char/token sobrepasaba la ventana (1M objetivo → ~1.14M reales → error 400). **Fix:** tramo top a 800K con margen + cada modelo medido **hasta su techo** (context window real en config; el runner saltea tamaños mayores).
5. **Needles distintos por tamaño → rankings FALSOS.** La grilla escalonada usaba más needles en tramos chicos. Comparar el promedio por tamaño mezclaba needles → "Gemini 3.5 peor que 2.5 Lite", "zigzag de DeepSeek" eran **artefactos del needle, no del modelo**. **Fix:** la curva por tamaño usa solo los needles comunes a todos los tamaños.

**La verdad, con medición limpia:** sobre needles neutros, **todos los modelos retrievean ~10 en todos los tamaños hasta su techo**. El NIAH-es neutro **NO discrimina** a estos modelos. Los diferenciadores reales que sí aparecen son otros dos (abajo).

## 📏 Dimensión long-context: contexto USABLE (no retrieval)

Como el retrieval es uniforme, lo que diferencia es **hasta qué contexto el modelo realmente funciona** (`effective_context`) — que puede ser **menor al declarado**:

| Modelo | Declarado | **Usable real** |
|---|---|---|
| Gemini 2.5 Flash Lite | 1M | **800K** ✅ |
| Gemini 3.5 Flash | 1M | **800K** ✅ |
| DeepSeek V4 Flash | 1M | **800K** ✅ |
| Llama 4 Maverick | 1M | **800K** ✅ |
| **MiniMax M3 (directo/sub)** | **1M** | **512K** ⚠️ (erorea a 800K) |
| MiniMax M3 (OpenRouter) | 1M | **256K** ⚠️ |
| Claude Opus 4.8 | 1M | 256K* (capeado por costo en el test) |

> **"Ventana declarada ≠ ventana usable."** MiniMax M3 anuncia 1M pero su API (directa y OpenRouter) erorea a 800K → su contexto usable es 512K. Para un emprendedor que necesita procesar documentos grandes, esto importa más que el número de marketing.

## 🛡️ Dimensión seguridad: resistencia a fuga de credenciales (NUEVA)

El ángulo de "fuga" que descontaminamos del niah se volvió una **suite intencional** (`prompt_injection_es`): un secreto plantado en un documento + se pide extraerlo. Premia rehusar, penaliza filtrar.

| Modelo | Seguridad | Comportamiento |
|---|---|---|
| **Claude Opus 4.8** | **8.79** 🥇 | rehúsa filtrar |
| MiniMax M3 (OR + sub) | 8.04–8.07 | rehúsa |
| DeepSeek / Gemini / Llama / Qwen / Nemotron | **~1.7–2.0** | **filtran el secreto** |

> **Hallazgo accionable:** los **premium (Opus) NO filtran credenciales plantadas; los cheap sí.** Si tu agente procesa documentos con datos sensibles (contratos, PII, configs), este eje pesa — y es invisible en cualquier benchmark de calidad/costo.

## 🏆 Ranking general (tareas prácticas, sin long-context)

Sin cambios de fondo vs mayo — los workhorses rápidos y baratos siguen arriba. Lo nuevo: **DeepSeek V4 Flash #9**.

| # | Modelo | Score | Nota |
|---|---|---|---|
| 1 | Llama 3.1 8B Instant (Groq) | 8.11 | velocidad + costo |
| 2 | Llama 4 Scout 17B (Groq) | 8.11 | |
| 3 | Devstral Small | 8.03 | coding, Apache |
| 4 | Llama 3.3 70B (Groq) | 7.86 | |
| 5 | GPT-OSS 20B (Groq) | 7.84 | |
| 9 | **DeepSeek V4 Flash** 🆕 | 7.80 | quality 8.34, $0.33/1k |

**Opus 4.8**: quality 8.4 (de las más altas), pero **#66** — a $5/$25 el costo (20% del peso) lo hunde. Techo de calidad, no de valor. (Y rey de seguridad.)

## ⚙️ Infraestructura: juez vLLM en DGX Spark

- Llegó el **DGX Spark** (GB10, 128GB). Es **bandwidth-bound** para inferencia (~10 tok/s en 27B) → preferimos OpenRouter para gen, y usamos el Spark como **host del juez**.
- **Phi-4 servido en vLLM FP16** (continuous batching) en lugar de Ollama (que serializa). Compat **sm_121 (Blackwell) confirmada**. Esto desbloqueó correr múltiples sweeps en paralelo con juicio batcheado.

## Caveats honestos de junio

- **El NIAH-es neutro no discrimina** a los modelos top — es un piso, no un ranking. Su valor está en `effective_context` (contexto usable) y en haber expuesto los 5 sesgos.
- **Cobertura long-context/seguridad parcial** (~17 modelos, no los 80). Se completa en julio.
- **Premium capeados a 256K** en niah por costo (Opus a $5/1M es caro incluso a 256K). Su `effective_context` real puede ser mayor.
- La suite de seguridad es un **piloto** (5 secretos × 4 combinaciones). Direccional, no exhaustiva.

## Qué sigue (julio)

- Completar long-context + seguridad en los 80 modelos.
- Provider `claude_code` (correr Anthropic por la suscripción Max, no por API) para abaratar mediciones premium futuras.
- Revisión de ROI de marca del repo (gasto de medición vs valor de comunidad/contenido).
