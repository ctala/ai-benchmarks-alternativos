---
titulo: Replicá el benchmark en 30 minutos
dificultad: Principiante
tiempo_estimado: 30 minutos
costo_estimado: Menos de $1 USD
requisitos_previos:
  - Python 3.10+ instalado
  - Cuenta en OpenRouter con $5 USD de crédito
  - Terminal (Mac, Linux o WSL en Windows)
---

# Replicá el benchmark en 30 minutos

## Para qué sirve este tutorial

Vas a clonar el repo, configurar **una sola API key**, y correr un benchmark chico contra ~3 modelos. El objetivo es que en media hora **tengas un JSON con resultados reales** que vos generaste, y entiendas dónde se guarda cada cosa. Es la base para todos los tutoriales siguientes.

## Lo que vas a tener al final

- El repo corriendo en tu máquina.
- Un archivo `benchmarks/results/benchmark_<fecha>.json` con scores de los modelos que elegiste.
- Las respuestas completas de cada modelo guardadas en `benchmarks/results/responses/<timestamp>/`.
- Saber leer el output del runner sin googlear nada.

## Paso 1 — Cloná el repo y entrá a la carpeta

```bash
git clone https://github.com/ctala/ai-benchmarks-alternativos.git
cd ai-benchmarks-alternativos
```

**Si falla el clone**: probablemente no tenés `git` instalado. En Mac: `brew install git`. En Ubuntu: `sudo apt install git`.

## Paso 2 — Creá un entorno virtual de Python

```bash
python3 -m venv .venv
source .venv/bin/activate
```

En Windows con PowerShell sería `.\.venv\Scripts\Activate.ps1`.

**Output esperado**: el prompt de tu terminal ahora muestra `(.venv)` adelante. Si no lo ves, no estás en el entorno y los próximos pasos van a fallar.

## Paso 3 — Instalá las dependencias

```bash
pip install -r requirements.txt
```

**Output esperado**: termina con `Successfully installed openai-... httpx-... rich-... ...` (6 paquetes en total).

**Si falla con "command not found: pip"**: probá `python3 -m pip install -r requirements.txt`.

## Paso 4 — Configurá tu API key de OpenRouter

```bash
cp .env.example .env
```

Abrí `.env` con tu editor favorito (`nano .env`, `code .env`, lo que uses) y completá la línea:

```
OPENROUTER_API_KEY=sk-or-v1-XXXXXXXXXXXXXXXXXXXXXXXXX
```

Si no tenés la key todavía, sacala en <https://openrouter.ai/keys> (es gratis crear cuenta, depositás $5-10 USD para empezar — con eso te alcanza para meses de tutoriales).

**Importante**: el archivo `.env` está en `.gitignore`, no se va a subir nunca al repo. No hardcodees keys en `config.py`.

## Paso 5 — Copiá el config de modelos

```bash
cp benchmarks/config.example.py benchmarks/config.py
```

Este archivo tiene la lista de **todos los modelos** que el benchmark conoce (~80). Para el tutorial vamos a correr solo 3 con el flag `--models`.

## Paso 6 — Verificá que todo está OK con un dry-run

```bash
python benchmarks/runner.py --list-models
```

**Output esperado**: una tabla con todos los modelos configurados, su tier (free/cheap/medium/premium), su costo input/output y su provider.

**Si falla con "ModuleNotFoundError"**: te olvidaste de activar el venv. Volvé al Paso 2.

## Paso 7 — Corré el benchmark mínimo

Vamos a correr **un solo suite chico** (`startup_content`, 5 tests de generación de contenido para emprendedores) contra **3 modelos baratos**:

```bash
python benchmarks/runner.py \
  --quick \
  --tests startup_content \
  --models deepseek-v3 mistral-nemo gemini-2.5-flash-lite
```

**Qué hace cada flag**:
- `--quick` → 1 corrida por test (sin esto, son 3 corridas por test = 3× más caro).
- `--tests startup_content` → solo el suite de contenido para startups.
- `--models ...` → la lista de modelos a probar (los tres más baratos del config).

**Output esperado** (resumido):

```
[1/3] DeepSeek V3.2
  blog_actualidad_startup    score: 7.2 | 1,840 ms | $0.0008
  curso_emprendimiento       score: 6.8 | 2,103 ms | $0.0011
  workshop_outline           score: 7.5 | 2,210 ms | $0.0010
  newsletter_startup         score: 7.0 | 1,892 ms | $0.0009
  perplexity_research        score: 6.9 | 1,712 ms | $0.0007

[2/3] Mistral Nemo
  ...

[3/3] Gemini 2.5 Flash Lite
  ...

Resultados guardados en: benchmarks/results/benchmark_20260426_193045.json
```

**Tiempo real**: 5-12 minutos. **Costo real**: $0.05 - $0.30 USD para los 3 modelos × 5 tests.

**Si falla con `401 Unauthorized`**: la key de OpenRouter está mal. Volvé al Paso 4 y verificá que copiaste la key completa, sin espacios.

**Si falla con `model not found`**: el ID de OpenRouter cambió. Probá con otros modelos del `--list-models`.

## Paso 8 — Mirá tus resultados

El runner generó **3 cosas** que tenés que conocer:

### 1. JSON con todos los scores

```bash
ls -lh benchmarks/results/benchmark_*.json | tail -1
```

Abrilo con tu editor. Cada test tiene este formato:

```json
{
  "model": "deepseek-v3",
  "test_name": "blog_actualidad_startup",
  "score": 7.2,
  "latency_total": 1.840,
  "tokens_per_second": 87,
  "input_tokens": 412,
  "output_tokens": 893,
  "cost_usd": 0.00082,
  "response": "...",
  "success": true
}
```

### 2. Respuestas completas en Markdown (auditable)

```bash
ls benchmarks/results/responses/ | tail -1
# devuelve algo como: 20260426_193045
```

```bash
ls benchmarks/results/responses/20260426_193045/ | head -5
```

Vas a ver archivos como `deepseek-v3__startup_content__blog_actualidad_startup.md` con la **respuesta completa que dio el modelo**, palabra por palabra. Esto es oro: podés leer las respuestas y formarte tu propio juicio.

### 3. Tabla resumen en consola

El runner ya la imprimió al final. Si la querés ver con más detalle:

```bash
python -c "
import json
with open('benchmarks/results/benchmark_$(ls benchmarks/results/ | grep '^benchmark_' | tail -1 | sed 's/benchmark_//;s/.json//').json') as f:
    data = json.load(f)
for r in data['results']:
    print(f\"{r['model']:25} {r['test_name']:30} {r['score']:.2f}\")
"
```

(Si te complica, abrí el JSON con un editor y listo.)

## Paso 9 — Mapa mental de dónde mirar qué

```
ai-benchmarks-alternativos/
├── benchmarks/
│   ├── runner.py              ← motor principal (lo que corriste)
│   ├── config.py              ← qué modelos existen (lo copiaste)
│   ├── tests/                 ← carpetas de tests por categoría
│   │   ├── startup_content.py ← el suite que probaste
│   │   └── ...                ← otros 22 suites
│   └── results/
│       ├── benchmark_*.json   ← scores raw (esto generaste)
│       ├── responses/         ← respuestas completas por test
│       └── per-model/         ← MDs navegables (los regenerás en tut 2)
├── docs/
│   └── data/models.json       ← consumido por la calculadora web
├── .env                       ← TUS keys (gitignored)
└── README.md
```

## Próximos pasos

Logrado: tenés el repo corriendo y entendés dónde vive cada cosa. El próximo paso lógico es **agregar un modelo nuevo que vos quieras probar**.

Seguí con: [02 — Agregá tu propio modelo al benchmark](02-agregar-tu-modelo.md)

Si querés saltar al juez local (gratis, evita sesgo): [04 — Setup del LLM-as-Judge con Phi-4](04-configurar-phi4-judge.md)
