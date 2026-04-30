---
title: "NIAH-ES — Needle-in-a-Haystack en español neutro"
fecha: "2026-04-30"
version: "v1 piloto"
audiencia: "Lectores del benchmark + futuros agentes que mantengan o extiendan la suite"
licencia_corpus: "Wikipedia ES (CC BY-SA 4.0)"
---

# NIAH-ES — diseño y proceso

Suite 25 del benchmark `ai-benchmarks-alternativos`. **Aporte único**: primer NIAH público en español neutro LATAM. En abril 2026 sólo había NIAH en inglés/chino o variantes ad-hoc no reproducibles.

## Por qué NIAH

NIAH (Needle-in-a-Haystack) es el benchmark estándar para medir **retrieval de información específica en contexto largo**. La metodología:

1. Construir un haystack (documento muy largo, coherente, en el idioma target)
2. Insertar un needle (información específica, verificable) en una posición concreta
3. Pedirle al modelo que extraiga la info del needle
4. Variar **tamaño del contexto** y **posición del needle** → identificar dónde se degrada cada modelo

**Lo que mide**:
- Effective context window (vs el declarado por el vendor — suelen ser distintos)
- Patrón "lost-in-the-middle" (los modelos olvidan info que está al medio del contexto)
- Robustez del retrieval cuando el needle se rodea de contenido distractor pero coherente

**Lo que NO mide** (y lo decimos honestamente):
- Razonamiento sobre la info recuperada (sólo extrae, no infiere)
- Comprensión del contexto distractor (puede haber ignorado el 99% del haystack)
- Capacidad agentic con tools en sandbox (eso lo mide SWE-bench / Claw-Eval)

## Anatomía de un test

### Haystack

Concatenación de 9 artículos de Wikipedia ES (CC BY-SA 4.0) sobre temas LATAM diversos, ~1.1MB / ~285K tokens estimados:

| Archivo | Tema | Tamaño aprox |
|---|---|---|
| `Argentina.txt` | País Argentina | 45 KB |
| `Historia_de_Chile.txt` | Historia chilena | 140 KB |
| `Historia_de_Colombia.txt` | Historia colombiana | 58 KB |
| `Historia_de_Mexico.txt` | Historia mexicana | 478 KB |
| `Historia_del_Peru.txt` | Historia peruana | 198 KB |
| `Inteligencia_artificial.txt` | Concepto IA | 82 KB |
| `Internet.txt` | Concepto Internet | 52 KB |
| `Lenguaje_de_programacion.txt` | Concepto técnico | 45 KB |
| `Programacion.txt` | Concepto técnico | 17 KB |
| `Sistema_operativo.txt` | Concepto técnico | 24 KB |

**Por qué Wikipedia ES**: dominio público (CC BY-SA), español neutro mantenido por editores de muchos países latinos, contenido coherente narrativa, reproducible (snapshot fijo en repo).

**Reproducibilidad**: corpus committeado al repo en `benchmarks/tests/niah_es_corpus/`. Para regenerar desde Wikipedia (snapshot fresco), usar el script de descarga via API que está documentado en el commit que creó esos archivos.

### Needle

Información específica con elementos que requieren **precisión exacta** (códigos, números, fechas, identificadores). 5 needles distintos rotamos para evitar overfit:

| ID | Tipo | Pattern crítico |
|---|---|---|
| `discount_code` | Código alfanumérico + fecha | `CHILE2026-EARLY` + `15 de junio` |
| `ssh_port` | Puerto + nombre servidor | `48372` + `analytics-prod-cl-01` |
| `budget_q3` | Monto USD + ciudades | `247,800` + `Bogotá` + `CDMX` |
| `investor_meeting` | Fecha + hora + zona horaria | `3 de septiembre 2026 14:30 UTC-3` |
| `api_key` | API key + período | `sk-prod-grw-cl-2026-7f9a2b4e8c1d` + `90 días` |

**Por qué estos**: contienen elementos que el modelo **no puede alucinar fácilmente** (códigos específicos, números arbitrarios, identificadores únicos). El test es claro: o lo extrajo bien, o no.

### Contextos y posiciones (piloto v1)

| Variable | Valores | Total |
|---|---|---|
| Tamaño de contexto | 4K, 16K, 64K, 256K tokens | 4 |
| Posición del needle | 25%, 50%, 75% del haystack | 3 |
| Needles | 5 (rotación determinística) | — |
| **Total tests por modelo** | **12** | |

Posiciones elegidas para **estresar lost-in-the-middle**: 25% y 75% son posiciones "de borde", 50% es el centro donde típicamente se pierde la atención de modelos con contexto largo.

### Scoring

Híbrido binario + LLM-as-Judge, definido en `benchmarks/scoring.py::_score_niah_extraction`:

```
final = pattern_score * 0.7 + keyword_score * 0.3
```

**`pattern_score`** (peso 70%): proporción de regex `exact_patterns` que matchean en la respuesta. Un test con 3 patterns y 2 que matchean = 6.67/10.

**`keyword_score`** (peso 30%): proporción de strings de `keywords` presentes en la respuesta (case-insensitive substring).

**Por qué híbrido**: regex puro es muy estricto (penaliza paráfrasis válidas). Keywords solo es muy permisivo (dice "código" sin decir el código exacto). El híbrido captura ambos: precisión exacta + comprensión semántica.

## Implementación

### Archivos clave

- `benchmarks/tests/niah_es.py` — generador de tests dinámico
- `benchmarks/tests/niah_es_corpus/*.txt` — corpus snapshot (committeado)
- `benchmarks/scoring.py::_score_niah_extraction` — scoring custom
- `benchmarks/runner.py` — registrado como suite 25 en `ALL_TEST_SUITES`

### Generación dinámica

A diferencia del resto de las suites (que tienen tests hardcoded), NIAH-ES **construye los prompts en runtime**. La función `_build_test(needle_idx, ctx_tokens, pos_pct)`:

1. Carga el corpus (~1.1MB) al import del módulo
2. Repite el corpus hasta llegar al tamaño objetivo (`target_chars = ctx_tokens * 4`, heurística español)
3. Inserta el needle en la posición porcentual indicada
4. Construye el prompt: instrucción intro + haystack-con-needle + pregunta

**Heurística de tokens**: 1 token ≈ 4 caracteres en español. Aproximación; la realidad varía ±15% según tokenizer del modelo (cl100k_base, sentencepiece, etc.). Para contextos pequeños la diferencia es marginal; para 256K puede cambiar +/-30K tokens reales — pero el test de "lost-in-the-middle" funciona igual.

### Comportamiento ante context overflow

Si el modelo tiene context window menor al pedido (ej. Mistral Small 4 con 128K vs nuestro test de 256K), el adapter del provider trunca silenciosamente o devuelve error. **Esto es info útil** — registramos el modelo como "no soporta el contexto pedido" y NO falseamos el resultado.

## Modelos recomendados (piloto)

8 modelos selectivos para minimizar costo del piloto pero capturar variedad:

| Modelo | Context window | ¿corre 256K? | Provider | Costo aprox |
|---|---|---|---|---|
| Mistral Small 4 | 128K | ❌ (3 tests fallarán) | OpenRouter | $0.10 |
| Llama 3.3 70B Groq | 131K | ❌ (3 tests fallarán) | Groq direct | $0.05 |
| Devstral Small | 256K | ✅ apenas | OpenRouter | $0.30 |
| Llama 4 Scout 17B | 10M | ✅ holgado | Groq preview | $0.10 |
| GPT-4.1 | 1M | ✅ holgado | OpenRouter | $5.00 |
| Gemini 3.1 Flash Lite | 1M | ✅ holgado | OpenRouter | $1.50 |
| Claude Opus 4.7 | 200K | ⚠️ apenas | OpenRouter | $20.00 |
| DeepSeek V4 Flash (NIM) | 1M | ✅ holgado | NIM gratis | $0 |

**Total piloto estimado**: ~$30-40 en OpenRouter (Opus 4.7 es la mayoría del costo).

## Hipótesis a validar

1. **Effective context vs declared context**: hipótesis fuerte de que ningún modelo retiene el needle al 100% en 256K en posición 50%. Esperamos ver degradación notable en cada modelo.

2. **Lost-in-the-middle**: needle en 25% y 75% extraído mejor que en 50%. Patrón documentado en literatura.

3. **Modelos cheap fallan en context grande**: Llama 3.3 70B y Mistral Small 4 caen a 0% en 256K (no soportan).

4. **Modelos premium siguen ganando en context grande**: GPT-4.1 y Gemini 3.1 Pro mantienen >80% retrieval a 256K. Opus 4.7 hipótesis: top en 4K-64K, baja en 256K (apenas dentro de su 200K).

5. **DeepSeek V4 Flash NIM (1M context, gratis)** es la sorpresa esperada: si retiene >70% a 256K, es la mejor opción C/B para tareas long-context.

## Lecciones que llevamos al diseño

Esta suite incorpora aprendizajes del benchmark hasta v2.4.2:

- ✅ **Datos LATAM neutros**: needles con código `CHILE2026-EARLY`, ciudades Bogotá/CDMX/Santiago, NO inglés
- ✅ **Reproducibilidad estricta**: corpus snapshot en git, no fetch live
- ✅ **Scoring transparente**: regex + keywords, no opaco
- ✅ **Limitaciones documentadas**: NO mide razonamiento, solo extracción
- ✅ **Cost-aware**: piloto reducido $30-40 antes de lote completo $300+
- ✅ **Cross-reference con benchmarks externos**: en INSIGHTS comparamos con Gemini 1.5 Pro NIAH (paper Google), Claude paper "Needle In A Haystack" interno

## Reproducibilidad pública (inputs + outputs)

Política del proyecto: **inputs y outputs de todos los tests son públicos en el repo** para auditoría académica y replicación.

### Outputs por modelo

Cada respuesta del modelo se guarda en `benchmarks/results/responses/<timestamp>/<modelo>__<suite>__<test>.md` con:
- model_id, score final, breakdown (quality, cost, etc.)
- latency, tokens in/out
- Respuesta completa del modelo

**Tamaño**: ~300-550 bytes por archivo (sin el prompt). 100% commiteado al repo.

### Inputs (prompts) — regenerables, NO duplicados

Los prompts de NIAH-ES son grandes (4K-1MB cada uno). Guardarlos por modelo×test sería bloat absurdo (12 tests × 1MB × 8 modelos = 96MB). En su lugar:

**Lo que SÍ se commitea** (todo público, suficiente para regenerar):
- `benchmarks/tests/niah_es_corpus/*.txt` — 9 artículos Wikipedia ES (~1.1MB)
- `benchmarks/tests/niah_es.py` — 5 needles + 4 contextos + 3 posiciones + lógica de generación

**Cómo regenerar el prompt EXACTO de cualquier test**:

```bash
# Listar todos los tests disponibles
python benchmarks/regenerate_niah_test.py --list

# Imprimir el prompt de un test específico
python benchmarks/regenerate_niah_test.py --name niah_es_discount_code_4000_p25

# Guardarlo en archivo (para auditoría)
python benchmarks/regenerate_niah_test.py --name niah_es_api_key_256000_p25 \
    --output /tmp/audit_input.txt
```

Esto es **mejor que duplicar prompts** académicamente:
1. Reproducibilidad estricta — corpus snapshot fijo en git, no cambia
2. Verificable — anyone puede regenerar y comparar bit-a-bit
3. Eficiente — repo no se infla con duplicación
4. Transparente — la lógica de generación es código abierto

### Para auditoría externa (revisores arXiv, comunidad)

```bash
# Clonar el repo
git clone https://github.com/ctala/ai-benchmarks-alternativos
cd ai-benchmarks-alternativos

# Verificar respuesta de un modelo concreto en un test
cat benchmarks/results/responses/20260430_191156/mistral-small-4__niah_es__niah_es_discount_code_4000_p25.md

# Regenerar el prompt EXACTO que recibió el modelo
python benchmarks/regenerate_niah_test.py --name niah_es_discount_code_4000_p25

# Re-correr el test contra otro modelo (validación independiente)
python benchmarks/runner.py --quick --tests niah_es \
    --models <tu-modelo-de-elección>
```

## Próximos pasos (post-piloto)

1. **Smoke test con Mistral Small 4** — verificar que la suite corre sin errores (en curso al 30 abril 18:00 UTC)
2. **Lote completo piloto v1** — 8 modelos × 12 tests = 96 tests (~$30-40)
3. **Análisis de resultados** — generar heatmap (modelo × posición × contexto) en INSIGHTS
4. **v2 con 5 needles activos** (60 tests por modelo, lote completo $200-300) — si v1 muestra discriminación interesante
5. **v3 con corpus 1M** (Llama 4 Scout, Gemini Pro, DeepSeek V4) — para probar el límite real

## ROADMAP de NIAH-ES

| Fase | Estado | Descripción |
|---|---|---|
| Diseño | ✅ Hecho | Este documento |
| Implementación | ✅ Hecho | `niah_es.py`, scoring, integrado al runner |
| Smoke test | 🔄 En curso | Mistral Small 4 (1 modelo, 12 tests) |
| Piloto v1 | ⏳ Pendiente | 8 modelos × 12 tests = 96 tests |
| Análisis + heatmap | ⏳ Pendiente | Sección dedicada en INSIGHTS |
| Lote completo v2 | ⏳ Futuro | 8 modelos × 60 tests (5 needles × 4 ctx × 3 pos) |
| Cobertura completa v3 | ⏳ Futuro | 15 modelos + contexto 1M |
| Cross-ref con NIAH inglés (Gemini paper, Claude paper) | ⏳ Futuro | Validación cruzada con literatura |
