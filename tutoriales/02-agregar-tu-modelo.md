---
titulo: Agregá tu propio modelo al benchmark
dificultad: Principiante
tiempo_estimado: 20-40 minutos
costo_estimado: Menos de $0.50 USD
requisitos_previos:
  - Tutorial 01 completado (repo corriendo, .env con OPENROUTER_API_KEY)
  - Saber qué modelo querés agregar y dónde se hostea (OpenRouter, Groq, NVIDIA NIM, etc.)
---

# Agregá tu propio modelo al benchmark

## Para qué sirve este tutorial

Salió un modelo nuevo que te interesa probar (DeepSeek V4, Kimi K2.7, MiMo V3, lo que sea) y no está en el benchmark. Este tutorial te enseña a **agregarlo en 5 minutos si está en OpenRouter**, o en ~30 minutos si requiere un provider directo (Groq, NVIDIA, MiniMax).

## Lo que vas a tener al final

- Tu modelo nuevo registrado en `config.py`.
- Su pricing registrado en `scoring.py`.
- Resultados frescos del modelo en `benchmarks/results/`.
- El modelo apareciendo en MODELOS.md y en la calculadora web.

## Caso ejemplo

Vamos a agregar un modelo ficticio llamado **Qwen3-Coder Plus** (`qwen/qwen3-coder-plus`) que está en OpenRouter, cuesta $0.30 input / $1.20 output por millón de tokens, no es open source. Cambiá los valores por los del modelo real que querés probar.

## Paso 1 — Conseguí el ID exacto del modelo

Lo más importante: **el ID tiene que ser EXACTO**. Si te equivocás en una letra el runner devuelve `404 model not found`.

### Si el modelo está en OpenRouter

Andá a <https://openrouter.ai/models> y buscá el modelo. El ID está debajo del nombre, formato `provider/model-name`.

```
Qwen3-Coder Plus
qwen/qwen3-coder-plus    ← este es el ID
$0.30 / $1.20 per M tokens
```

### Si el modelo está en otro provider

- **Groq**: <https://console.groq.com/docs/models>
- **NVIDIA NIM**: <https://build.nvidia.com/explore/discover>
- **MiniMax**: <https://www.minimaxi.com/document/algorithm-concept>
- **Ollama Cloud**: <https://ollama.com/search?c=cloud>

Anotá el ID y el pricing oficial.

## Paso 2 — Editá `benchmarks/config.py`

Abrí `benchmarks/config.py` y buscá el dict `MODELS`. Vas a ver bloques como:

```python
"deepseek-v3": {
    "id": "deepseek/deepseek-chat",
    "name": "DeepSeek V3.2",
    "cost_input": 0.14,
    "cost_output": 0.28,
    "tier": "cheap",
},
```

Agregá tu modelo en la sección correcta según su tier de precio:

- `free` → modelos gratis (suele ser :free en OpenRouter)
- `ultra_cheap` → menos de $0.10/M
- `cheap` → $0.10 - $1.00/M
- `medium` → $1.00 - $5.00/M
- `premium` → más de $5.00/M
- `local` → corre en tu máquina (Ollama)
- `cloud_ollama` → Ollama Cloud

Para nuestro ejemplo de Qwen3-Coder Plus ($0.30 / $1.20):

```python
"qwen3-coder-plus": {
    "id": "qwen/qwen3-coder-plus",
    "name": "Qwen3-Coder Plus",
    "cost_input": 0.30,
    "cost_output": 1.20,
    "tier": "cheap",
    "open_source": False,
    "license": "Qwen Commercial",
    "notes": "Variante propietaria de la familia Qwen3-Coder, no se publican pesos.",
},
```

**Tips importantes**:

- La **clave del dict** (`"qwen3-coder-plus"`) es la que vas a usar con `--models qwen3-coder-plus`. Hacelo corto y memorable.
- `open_source: True` SOLO si los pesos están publicados (Apache, MIT, Llama license). Las variantes "Plus" / "Max" de Alibaba son propietarias, leé la sección sobre familia Qwen en `CLAUDE.md`.
- Si es de un provider directo (no OpenRouter), agregá `"provider": "groq"` o `"provider": "nvidia_nim"`, etc.

## Paso 3 — Si NO es OpenRouter, configurá el provider directo

**Saltá este paso si tu modelo está en OpenRouter.**

### Ejemplo: agregar un modelo de Groq

a) Asegurate de tener `GROQ_API_KEY` en tu `.env`:

```
GROQ_API_KEY=gsk_XXXXXXXXX
GROQ_BASE_URL=https://api.groq.com/openai/v1
```

b) En tu entry de `MODELS`, agregá la clave `provider`:

```python
"llama-3.3-groq": {
    "id": "llama-3.3-70b-versatile",   # ID que usa Groq, no el de OpenRouter
    "name": "Llama 3.3 70B (Groq)",
    "cost_input": 0.59,
    "cost_output": 0.79,
    "tier": "cheap",
    "provider": "groq",                 # esto le dice al runner qué adapter usar
    "open_source": True,
    "license": "Llama 3 Community",
},
```

c) Verificá que `providers/adapters.py` ya soporte el provider. Buscá en el archivo `provider_name == "groq"` — si existe, listo. Si no, mirá cómo está implementado `openai_direct` y replicá el patrón (Groq, MiniMax y NVIDIA NIM son todos OpenAI-compatible, así que es cuestión de pasar la base_url y la api_key correctas).

## Paso 4 — Actualizá el pricing en `scoring.py`

Abrí `benchmarks/scoring.py` y buscá el dict `PRICING`. Agregá tu modelo:

```python
PRICING = {
    # ... entries existentes ...
    "qwen3-coder-plus": {"input": 0.30, "output": 1.20},
}
```

**Por qué es necesario**: el runner calcula `cost_usd` por test usando este dict. Si no lo agregás, el costo estimado va a ser $0.

## Paso 5 — Corré un benchmark rápido contra tu modelo

```bash
source .venv/bin/activate

python benchmarks/runner.py \
  --quick \
  --tests startup_content \
  --models qwen3-coder-plus
```

**Output esperado**: 5 tests ejecutados, scores entre 0-10, latencia y costo por test.

**Si falla con `404 model not found`**:
- Revisá el ID en `config.py` letra por letra.
- En OpenRouter, copialo desde la URL del modelo, no lo escribas a mano.

**Si falla con `401 Unauthorized`**:
- Si es OpenRouter: tu key no tiene crédito o no tenés acceso al modelo (algunos requieren request).
- Si es provider directo: la key correcta no está en `.env`.

**Si la respuesta es `content=""` o muy corta**:
- Puede ser un thinking model. Revisá `THINKING_MODELS` en `providers/adapters.py` y agregá el patrón del modelo nuevo.

## Paso 6 — Regenerá los artefactos auto (5 scripts en orden)

Esto es la parte que se olvida todo el mundo. El repo tiene 4 archivos auto-generados que tenés que sincronizar tras agregar un modelo:

```bash
# 1. MDs navegables por modelo (uno por modelo)
python benchmarks/generate_per_model_md.py

# 2. Tabla de MODELOS.md con links a los MDs
python benchmarks/generate_modelos_md_table.py -i

# 3. TESTS.md con prompts completos (no cambia con un modelo nuevo, pero corré por las dudas)
python benchmarks/generate_tests_md.py

# 4. JSON consumido por la calculadora web
python benchmarks/export_for_pages.py
```

(El quinto script es `generate_sitemap.py` y solo importa si publicás en GitHub Pages.)

**Output esperado**: cada script imprime "Generated X files" o similar. Cero errores.

**Tip**: hay una GitHub Action de seguridad (`.github/workflows/regenerate-auto-artifacts.yml`) que corre estos scripts si los olvidaste, pero hacelo manual primero — el commit principal va a quedar más prolijo.

## Paso 7 — Verificá que tu modelo aparezca

```bash
grep "qwen3-coder-plus" benchmarks/results/per-model/README.md
grep "Qwen3-Coder Plus" MODELOS.md
grep "qwen3-coder-plus" docs/data/models.json | head -3
```

**Output esperado**: las 3 líneas devuelven match. Si no, alguno de los scripts del Paso 6 no corrió bien.

Mirá el MD nuevo que se generó:

```bash
ls benchmarks/results/per-model/ | grep qwen3-coder
# qwen_qwen3-coder-plus.md  ← este es el archivo
```

Abrilo: tiene un resumen de scores por suite, ranking dentro de su tier, y links a las respuestas auditables.

## Paso 8 — (Opcional) Corré el benchmark completo

Si querés que tu modelo aparezca con score real en todos los pilares, corré los 23 suites:

```bash
python benchmarks/runner.py \
  --quick \
  --judge --judge-model phi4 \
  --models qwen3-coder-plus
```

(Necesitás Phi-4 instalado — ver tutorial 04. Sin `--judge` también funciona, pero los scores son menos confiables.)

**Tiempo**: 30-90 minutos según el modelo. **Costo**: $0.50 - $3 USD.

## Cuándo NO re-medir un modelo

Regla del repo: **no re-medir modelos ya cubiertos**. Solo se re-corre si:

1. Salió **versión nueva** (Kimi K2.6 → K2.7 = ID distinto = modelo distinto).
2. Cambiaron las **suites o el scoring**.
3. Hubo un **bug del runner** que invalida runs previos.
4. El proveedor anunció **silent retraining** o cambio de pricing.

No re-medir por: refactor, cambios cosméticos, regenerar MDs.

## Próximos pasos

Tenés un modelo nuevo en el benchmark. Ahora la pregunta clave: **¿los tests genéricos miden lo que a vos te importa?** Probablemente no.

Seguí con: [03 — Diseñá un test custom para TU caso de uso](03-disenar-test-custom.md)

Si querés correr benchmarks grandes sin gastar plata en API de juez: [04 — Setup del LLM-as-Judge con Phi-4](04-configurar-phi4-judge.md)
