---
titulo: Setup del LLM-as-Judge local con Phi-4
dificultad: Intermedio
tiempo_estimado: 30 minutos (más ~15 min de descarga)
costo_estimado: $0 USD (corre 100% local)
requisitos_previos:
  - Tutorial 01 completado
  - Mac (M1/M2/M3) o Linux con 16GB+ de RAM
  - 10 GB libres en disco
---

# Setup del LLM-as-Judge local con Phi-4

## Para qué sirve este tutorial

Los scores automáticos del runner miden cosas mecánicas (longitud, palabras clave, formato). Eso filtra basura pero no distingue una respuesta excelente de una mediocre. Para eso usamos **LLM-as-Judge**: otro modelo lee las respuestas y las puntúa con criterios cualitativos.

El problema: si usás Claude para juzgar a Claude, infla los scores 5-7%. Si usás GPT para juzgar a GPT, lo mismo. Es **conflicto de interés del benchmark**.

Solución: **Phi-4 corriendo localmente en tu compu**. Es un modelo de Microsoft 14B con licencia MIT, ~9 GB, y nosotros NO evaluamos modelos Microsoft en este benchmark — cero conflicto de interés. Además, gratis para siempre.

## Lo que vas a tener al final

- Ollama instalado y corriendo en tu máquina.
- Phi-4 descargado (9 GB).
- El runner usando Phi-4 como juez automáticamente con `--judge --judge-model phi4`.
- Comparación lado a lado de scores con vs sin juez.

## Por qué juez local

| Opción | Costo | Sesgo | Privacidad |
|--------|-------|-------|------------|
| **Phi-4 local** | $0 | Cero (Microsoft no está en el benchmark) | 100% local, nada sale |
| Claude Haiku API | ~$0.07 por modelo evaluado | Medio (infla scores Anthropic) | Tu data va a Anthropic |
| Gemini Flash API | ~$0.05 por modelo evaluado | Medio (infla scores Google) | Tu data va a Google |
| Sin juez | $0 | N/A | OK | Scores menos confiables para tests cualitativos |

Para benchmarks regulares, Phi-4 local es la opción correcta.

## Paso 1 — Instalá Ollama

Ollama es el "Docker de modelos LLM": una sola app que corre cualquier modelo open-weights con un comando.

### En Mac

```bash
brew install ollama
```

O bajalo directo desde <https://ollama.com/download>.

### En Linux

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### En Windows

Descargá el instalador desde <https://ollama.com/download/windows>. Para benchmarks recomendamos WSL2.

## Paso 2 — Arrancá el servicio Ollama

### En Mac

Abrí la app **Ollama.app** (la que se instaló). Vas a ver un iconito de llama en la barra de menú. Listo.

### En Linux

```bash
ollama serve &
```

(O configurá como systemd service si querés que arranque solo.)

### Verificá que está corriendo

```bash
curl http://localhost:11434/api/tags
```

**Output esperado**:

```json
{"models":[]}
```

(El array está vacío porque todavía no descargaste nada.)

**Si falla con `connection refused`**: Ollama no está arrancado. En Mac abrí la app; en Linux corré `ollama serve` en otra terminal.

## Paso 3 — Descargá Phi-4

```bash
ollama pull phi4
```

**Tiempo**: 10-20 minutos según tu internet (son 9 GB).

**Output esperado**:

```
pulling manifest
pulling 4f9e... 100% ████████████  9.1 GB
pulling 6e4c... 100% ████████████  4.0 KB
verifying sha256 digest
writing manifest
success
```

**Si falla con "no space left"**: necesitás 10+ GB libres. Borrá lo que no uses o usá un modelo más chico (`ollama pull gemma2:9b` también funciona como juez, ~5 GB).

## Paso 4 — Verificá que Phi-4 responde

```bash
ollama run phi4 "Decime en una oración por qué los benchmarks de LLMs son sesgados."
```

**Output esperado**: una respuesta coherente en español de 1-2 oraciones, en ~3-8 segundos.

**Si tarda mucho (>30 seg) o se cuelga**:
- En Mac: revisá Activity Monitor, debería usar 8-12 GB de RAM. Si tu Mac tiene <16 GB total puede swappear feo.
- Probá con `ollama run gemma2:9b "..."` (modelo más chico).

Cerrá la sesión interactiva con `/bye` o `Ctrl+D`.

## Paso 5 — Listá los presets de juez del runner

```bash
cd /ruta/a/ai-benchmarks-alternativos
source .venv/bin/activate
python benchmarks/runner.py --list-judges
```

**Output esperado**:

```
Presets de juez disponibles:
  phi4      → Phi-4 14B (Microsoft, MIT) — local, cero conflicto de interes [DEFAULT]
  gemma4    → Gemma 4 26B (Google) — local, alternativa
  glm-4.7   → GLM-4.7 9B — local, modelo no evaluado
  qwen-72b  → Qwen 3.5 72B — local, mas pesado
  haiku     → Claude Haiku — API, paga
  flash     → Gemini Flash — API, paga
```

## Paso 6 — Corré un benchmark CON juez

Vamos a usar el suite `startup_content` chico, 1 modelo, con Phi-4 juzgando:

```bash
python benchmarks/runner.py \
  --quick \
  --judge --judge-model phi4 \
  --tests startup_content \
  --models deepseek-v3
```

**Output esperado** (extracto):

```
[Judge: phi4 @ http://localhost:11434/v1]

[1/1] DeepSeek V3.2
  blog_actualidad_startup
    automatic score: 7.40
    judge score:     6.50  (rationale: respuesta bien estructurada pero
                            falta profundidad en datos LATAM concretos)
    final score:     6.77  (30% auto + 70% judge)
  ...
```

**Tiempo**: 5-10 min (cada test agrega ~5-15 seg de juicio Phi-4).

**Si Phi-4 no responde**: el adapter intenta `localhost:11434/v1/chat/completions`. Verificá:
1. `curl http://localhost:11434/api/tags` devuelve algo.
2. Tu modelo se llama `phi4:latest`. Si es otro tag, editá `JUDGE_PRESETS` en `benchmarks/llm_judge.py`.

## Paso 7 — Compará scores con vs sin juez

Esto es lo más educativo. Corré el mismo suite **sin juez** primero:

```bash
python benchmarks/runner.py \
  --quick \
  --tests startup_content \
  --models deepseek-v3 mistral-nemo
```

Anotá los scores. Después corrélo **con juez**:

```bash
python benchmarks/runner.py \
  --quick \
  --judge --judge-model phi4 \
  --tests startup_content \
  --models deepseek-v3 mistral-nemo
```

**Lo que vas a observar**:

```
Sin juez:
  DeepSeek V3   blog_actualidad_startup    7.4
  Mistral Nemo  blog_actualidad_startup    7.2  ← parecen casi iguales

Con juez Phi-4:
  DeepSeek V3   blog_actualidad_startup    6.8  ← bajó: era estructura sin sustancia
  Mistral Nemo  blog_actualidad_startup    5.4  ← bajó MUCHO: contenido pobre real
```

El score sin juez infla a modelos que **formatean bien pero dicen poco**. El juez detecta sustancia.

**Patrón típico**: tests débiles (que solo miden longitud + keywords) muestran diferencias chicas; con juez se separan claramente los modelos que generan contenido real de los que rellenan.

## Paso 8 — (Opcional) Probá otros jueces

### Gemma 4 (también local)

```bash
ollama pull gemma2:9b
python benchmarks/runner.py --quick --judge --judge-model gemma4 --tests startup_content --models deepseek-v3
```

Útil para sanity-check: si Phi-4 y Gemma dan scores muy distintos al mismo modelo, hay sesgo en uno de los dos.

### Claude Haiku (API, paga)

Solo si tenés Anthropic API key. Más rápido que Phi-4 pero **NO sirve para juzgar modelos de Anthropic** (sesgo).

```bash
# .env: ANTHROPIC_API_KEY=sk-ant-...
python benchmarks/runner.py --quick --judge --judge-model haiku --tests startup_content --models deepseek-v3
```

Costo: ~$0.07 por modelo evaluado contra los 23 suites.

## Paso 9 — Estándar para benchmarks publicables

Cuando vayas a publicar resultados o tomar decisiones serias:

1. **Siempre con juez** (`--judge --judge-model phi4`).
2. **Documentá el juez** en el commit (ya queda registrado en el JSON).
3. Si el modelo evaluado es de Microsoft, usá otro juez (Gemma 4 está bien).
4. Para ranking global, usá los **mismos jueces** en todos los lotes (no compares scores de Phi-4 con scores de Haiku).

## Tip: cuándo NO usar juez

Para tests de **string_precision**, **tool_calling** o **structured_output** el juez aporta poco — esos tests miden cosas binarias (devolvió el JSON correcto sí/no, llamó la tool correcta sí/no). El score automático ya es muy preciso.

El juez brilla en: contenido, razonamiento, customer support, sales outreach, creativity.

## Próximos pasos

Tenés el setup completo: repo + tu modelo + tu suite + juez local. Es momento de **decidir qué modelo realmente va a producción**.

Cerrá con: [05 — Cómo decidir qué modelo poner en producción](05-elegir-modelo-para-tu-caso.md)
