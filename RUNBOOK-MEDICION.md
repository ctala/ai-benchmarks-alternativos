# RUNBOOK — medir modelos / backfill de suites (leer ANTES de correr un lote)

Este doc existe porque en la sesión del 14-16 jul 2026 se **redescubrió tres veces**
lo mismo (paralelizar, resume estable, calcular costo antes) y se **re-rompió** dos veces
la integridad del export. Lo que sigue es el patrón correcto **a la primera**. Si vas a
medir algo, empezá acá, no por intuición.

---

## Regla 0 — modelos cloud: NUNCA secuencial

El runner (`runner.py`, loop en `for model_idx, ...`) mide los modelos **uno por uno**.
Para modelos cloud (OpenRouter, API) eso es un error de throughput: el cuello es la
**latencia de red**, no la CPU, y las llamadas son independientes. Medir 60 modelos en
fila = 15-45 h; en paralelo (10 grupos) = ~2 h. La misma diferencia entre "inviable en la
sesión" y "listo en una tarde".

**Patrón: N runners en paralelo, cada uno con SU archivo de resume.** Escrito y probado:

```bash
# 1. partir los keys en N grupos round-robin (balancea rápidos y lentos)
python3 -c "
keys=open('/tmp/keys.txt').read().split(); N=10
for i in range(N): open(f'/tmp/chunk_{i+1:02d}.txt','w').write(' '.join(keys[i::N]))"

# 2. seed de N archivos de resume de nombre FIJO (>= la época del invariante A1)
python3 -c "
import json
for i in range(1,11):
    json.dump({'metadata':{'timestamp':f'20260716_c{i:02d}','partial':True},'results':[]},
              open(f'benchmarks/results/benchmark_20260716_c{i:02d}.json','w'))"

# 3. lanzar los N en paralelo (un solo background task que hace fork interno)
for i in $(seq -w 1 10); do
  .venv/bin/python benchmarks/runner.py --quick --judge --judge-model phi4-or \
    --models $(cat /tmp/chunk_${i}.txt) --allow-anthropic-api --tests <SUITE> \
    --resume benchmarks/results/benchmark_20260716_c${i}.json > /tmp/log_${i}.txt 2>&1 &
done
wait
```

⚠️ **CORRECCIÓN (17-jul, post-mortem):** 10 concurrentes NO es seguro para suites con
**tools o multi-turno** (customer_support, orchestration, agent_capabilities,
agent_long_horizon). Bajo esa carga OpenRouter devuelve **respuestas vacías por rate-limit**
(0 tokens, `in_tok=0`) que el runner puntúa 0.0 → contaminación + gaps + sobregasto. Probado:
los mismos modelos funcionan LIMPIOS aislados. **Regla nueva: baja concurrencia (2 workers)
por default para suites con tools/multi-turno**; subir solo tras confirmar 0 empties. Suites
verificables simples aguantan más. Ver `POST-MORTEM-REMEDICION-20260716.md`.

El juez `phi4-or` (Phi-4 por OpenRouter) NO es el cuello — pero OJO: **rompe con
`JSONDecodeError` en algunos tests** (ej. `parallel_vs_sequential_judgment`), dejando el test
sin puntuar = gap sistemático en varios modelos. Si un test es gap en 3+ modelos a la vez,
sospechar del VERIFICADOR, no de los modelos.

## Regla 0.5 — costo: estimar con ×RUNS_PER_TEST y multiplicador reasoning/agentic

`average_scores` guarda los tokens de UN run (no la suma), así que estimar el costo sobre los
registros promediados **subestima ×3** (se pagan 3 llamadas por test). Además reasoning
(thinking largo) y agentic (multi-turno) disparan los tokens muy por encima del promedio.
**Antes de correr: multiplicar por RUNS_PER_TEST, aplicar factor reasoning/agentic, y nombrar
los modelos caros por separado** (Fable/Opus vía OpenRouter fueron ~$33 de ~$60 totales).
Una re-medición estimada en $18 costó ~$55-70. `--rerun-empty` targeted, nunca re-correr
suites completas caras.

## Regla 1 — resume de nombre FIJO, nunca diff `before/after`

Este entorno **mata los background cada ~5 min**. El resume tiene que ser idempotente: un
archivo de nombre fijo que se re-`--resume`ea. Sembralo vacío y siempre apuntá ahí. El
truco de "listar archivos antes/después para adivinar cuál se creó" es una carrera que
falla cuando el kill llega en los primeros segundos (pasó: el backfill quedó en 2% porque
nunca registraba el archivo). Relanzar = correr el MISMO script; retoma solo, sin re-pagar.

## Regla 2 — costo PRIMERO, no asumido

Antes de lanzar, calculá el costo con los tokens reales de un examen ya medido (no a ojo).
Un error de 13× (estimé $5.66 lo que costaba $76) mandó una corrida innecesaria. Para
verificables sin modelo: `rescore_all.py --dry-run` dice cuántos y cuánto ($1.37 por
10.245 runs, cero llamadas a modelos).

```bash
# census de costo real (tokens de un examen completo × precio del modelo objetivo)
python3 -c "import json; d=json.load(open('docs/data/models.json'))
x=[m for m in d['models'] if m['name']=='Claude Opus 4.8'][0]
print('in',x['total_input_tokens'],'out',x['total_output_tokens'])"
```

## Regla 3 — el runner ya distingue TRES estados de una respuesta vacía

No los toques sin entender (costó horas construirlos, 15-jul):
1. **Vacío transitorio** (hipo de red) → reintenta 1 vez, el reintento la trae.
2. **Rehúso persistente / bloqueo de política** (`api_refusal`, `finish_reason:
   content_filter`) → se PUNTÚA, no se descarta. El mensaje del bloqueo viaja en el campo
   `refusal` (en inglés), NO en `content`. Ante un test de fuga de credenciales, un bloqueo
   es resistencia MÁXIMA (10.0), no "evasivo" (5.0).
3. **Vacío + fallo real** → `success=False`, reparable con `--rerun-failed`/`--rerun-empty`.

Excepción: texto vacío + tool call **solo** es legítimo si el test DA tools.

---

## Integridad del export — la regla que se rompió dos veces

**El filtro de procedencia (`_misma_formula`) NO va en la calidad GLOBAL.** El dataset tiene
~20% de runs sin marca recuperable, repartidos DESIGUAL entre modelos. Filtrar `quality_avg`
por procedencia computa la calidad de cada modelo sobre un mix de suites distinto → colapsa
el ranking (probado: ranked cayó a 6, luego GPT-4.1 falso #1). El filtro va SOLO en:

- **tablas por-suite de DISPLAY** (`quality_by_suite`, `score_by_suite`) — el fix real de
  "Sol vs Fable comparaba poblaciones distintas".
- **cobertura de suite** (`suite_coverage`) — para que una suite entre al score solo cuando
  ≥80% la rindió VÁLIDA.

La calidad global y el conteo de muestra usan la población **CRUDA**: una medida de
velocidad/quality vieja sigue siendo real. La incomparabilidad de fondo se arregla
re-puntuando (`rescore_all.py`), no filtrando.

**Antes de re-medir por un "hueco":** el gate de cobertura ya EXCLUYE del score, de forma
uniforme, las suites bajo 80% — el ranking es justo SIN el backfill. El backfill AGREGA
señal (la suite agéntica separa a Sol/Fable), no repara una injusticia. Decidí con eso en
mente: ¿vale el cómputo, o el gate ya lo maneja?

## Scoring congelado por versión (v4.0+)

El z-score se estandariza contra una referencia **CONGELADA** (`scoring_reference.json`:
`norm_stats` + `norm_stats_by_pillar` + `score_rescale` + `version`), no contra la
población viva. Así **agregar un modelo nuevo NO recalcula el score de los demás** — los
números dejan de caducar solos. Reglas:

- **Corrida normal** (`python benchmarks/export_for_pages.py`): lee la referencia y la
  aplica. **Sin archivo → cae al z-score vivo histórico** (cero regresión) y avisa por
  consola. Nunca congela solo: una corrida sobre dataset parcial no puede fijar basura.
- **Recalibrar** (evento de versión, deliberado):
  `python benchmarks/export_for_pages.py --recalibrate --scoring-version v4.1`
  recalcula desde la población viva, **congela** el archivo y estampa la versión.
- **Cuándo recalibrar:** solo al cortar una versión del benchmark, sobre el dataset
  **completo** (ej. cuando termina un backfill de suite). NO a mitad de una medición.
- **Congelar la referencia protege contra agregar MODELOS, no contra medir más del mismo
  modelo.** Un backfill que agrega runs a modelos existentes SÍ mueve su `quality_avg` →
  su score, aunque la referencia esté congelada. Por eso **no se regenera/despliega
  producción a mitad de un backfill**: se espera a completarlo y se recalibra la versión.
- **Dimensiones aparte** (`niah`, `prompt_injection`, `agent_long_horizon`): el agéntico
  SÍ cuenta en la calidad titular (es donde los premium se diferencian) y ADEMÁS se expone
  como eje propio (`agentic_score`). niah/seguridad van solo como eje. Sacar una de la
  calidad titular reordena el ranking (probado: sacar agéntico hunde a Luna del #1 al #3 y
  flota modelos baratos) — no hacerlo sin decisión explícita.

## Heurística de oro (Cristian, acertó 7 veces seguidas)

**Cuando una diferencia entre modelos se ve "demasiado grande", la primera hipótesis es
error de medición PROPIO, no un hallazgo.** Verificá la fuente Y que la fuente compute bien
(publicación == fuente == población sana) antes de publicar el número.
