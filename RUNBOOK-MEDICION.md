<!-- doc: vigente | verificado: 2026-08-12 -->
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

## Regla 0.5 — costo: estimar POR SUITE, nunca con un $/run promedio

```bash
.venv/bin/python benchmarks/calculate_costs.py --estimar <modelo-ya-medido> \
    --precio-in 5.0 --precio-out 25.0
```

**Corré esto antes de cada lote.** Usa el consumo real por suite de un examen ya medido y lo
aplica al precio del modelo objetivo. Marca las suites de contexto largo / multi-turno y avisa
si la referencia está incompleta.

**El promedio de $/run miente, y miente hacia abajo.** No todas las suites cuestan igual, ni
parecido: el costo se concentra en unas pocas y promediarlo lo reparte entre 192 runs hasta
volverlo invisible. Medido el 12-ago-2026 sobre un examen completo:

| suite | tok-in/run | share del costo | share de los runs |
|---|---|---|---|
| `niah_es` | 107.960 | ~74% | 23% |
| `agent_long_horizon` | 19.316 | ~13% | 6% |
| `prompt_injection_es` | 16.172 | ~5% | 10% |
| todo lo demás (26 suites) | ~300 | ~8% | 61% |

Son **86× a 360×** más input por run. `niah_es` es contexto largo de verdad (100K+ tokens de
haystack) y `agent_long_horizon` reenvía la conversación entera en cada turno, así que un test
de 13 turnos paga el contexto 13 veces, creciendo — su costo va con el **cuadrado** de los turnos.

**El fallo que lo motivó:** estimé el Grupo A en $15,09. El examen completo de los dos Claude
Opus costaba **$98,96** — error de **6,6×**. Se cortó a los $18,64, con `niah_es` todavía por
delante en ambos (habría sido +$73). Y lo incómodo: **esta regla ya existía y ya decía que
multi-turno dispara los tokens.** Estaba escrita y no alcanzó, porque no tenía instrumento —
el mismo patrón que el skip de `niah` sin margen de salida y el juez corriendo donde su
veredicto se descarta. Por eso ahora la regla ES el comando de arriba.

### Corolario — `niah_es` y `prompt_injection_es` son OMITIBLES sin perder el ranking

`export_for_pages.py:896-903` los trata como **pilares aparte**: se reportan por separado y un
examen incompleto ahí se marca «no medido»; **no bloquean `ranked` ni contaminan el score**.
Así que en un modelo caro se puede correr el examen que rankea y saltar `niah_es`. No son
equivalentes y no se omiten juntos: en Opus 5 Fast `niah_es` cuesta **$48,77** y
`prompt_injection_es` **$3,55**. La seguridad se mide siempre; el contexto largo es el que se
negocia.

Lo demás que sigue valiendo: `average_scores` guarda los tokens de UN run (no la suma), así que
estimar sobre los registros promediados **subestima ×3** (se pagan 3 llamadas por test). Nombrá
los modelos caros por separado (Fable/Opus vía OpenRouter fueron ~$33 de ~$60 totales). Una
re-medición estimada en $18 costó ~$55-70. `--rerun-empty` targeted, nunca re-correr suites
completas caras.

## Regla 0.7 — una suite NUEVA se valida en una muestra ANTES del examen completo

```bash
.venv/bin/python benchmarks/validate_suite.py --suite <nombre>
```

**Nunca valides una suite con dos modelos.** El 13-ago-2026 escribí dos suites duras y las
probé en uno bueno y uno malo. Las dos parecían discriminar:

```
retrieval_distractores   Qwen 3.7 Flash 8,99  ·  Llama 3.1 8B 7,46   → "separa 1,53"
```

Con los 82 medidos: **76% de respuestas perfectas.** Saturada de nacimiento, igual que las
cinco suites que acabábamos de jubilar por eso mismo. Endurecerla la bajó a 70%. Se
descartó.

**Por qué engaña:** la separación entre dos puntos no mide la dispersión de la
distribución. Un test que el 76% resuelve perfecto igual muestra diferencia entre el mejor
y el peor — y eso fue justo lo que me convenció.

El validador corre la suite en **~8 modelos repartidos por todo el rango** (no dos
extremos) y aplica tres criterios:

| | qué mide | rechaza si |
|---|---|---|
| **S1 saturación** | % de runs con nota perfecta | ≥60% (avisa desde 40%) |
| **S2 dispersión** | sd de la media por modelo vs el índice general | < 1× |
| **S3 rango** | piso y techo reales | nadie baja de 8,0 |

⚠️ **S1 es el que importa.** Probado contra los dos casos conocidos: `tool_calling_adversarial`
(0% saturación) y `retrieval_distractores` (75%) tenían **la misma dispersión, 1,03** — o sea
que S2 solo no habría cazado nada. Lo que separa una suite viva de una muerta es cuánta
gente la resuelve perfecto.

Cuesta centavos. Medir los 82 y descubrirlo después cuesta el lote y, peor, el riesgo de
publicar una suite que no informa.

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

---

# PASO 0 — el canario. Lo EXIGE el runner, no tu memoria

> **Desde el 13-ago-2026 el gate es real.** Un lote de **más de 3 modelos se niega a
> arrancar** sin un recibo de canario de las últimas 12 h
> (`benchmarks/results/_canario_ultimo.json`, que el canario escribe solo). Se salta con
> `--sin-canario`, a propósito y ruidosamente.
>
> Por qué se agregó: el canario estaba documentado en **seis** archivos y exigido en
> **ninguno** — se corría cuando alguien se acordaba. Documentarlo por séptima vez no
> iba a arreglar eso. Es la regla de oro del repo aplicada a sí misma.

```bash
.venv/bin/python benchmarks/canario.py --models <primer-modelo-del-lote>
# Claude por API:  --models claude-opus-5 --extra --allow-anthropic-api
```

**Si sale 🔴, el lote NO se lanza.** Corre 18 tests (3 suites) en 1 modelo y verifica
**invariantes**, no bugs conocidos:

| Invariante | Qué caza |
|---|---|
| Responde y el `content` no viene vacío | thinking sin su patrón en `THINKING_MODELS` |
| Emite tool calls donde el test da herramientas | ruteo, `require_parameters`, proveedor sin tools |
| Registra `upstream_provider` | mediciones que después no se pueden auditar |
| Guarda `prompt_sha` | runs sin trazabilidad de su entrada |
| Tasa de fallo bajo 34% | cualquier cosa sistémica |

**Por qué existe, con los números del 12-ago:** ese día los fallos se partieron en dos
grupos limpios. Los **anticipados** —Glimmer y Muse Spark thinking, 5 de 9 devolviendo
vacío, 19 keys inventadas, 2 modelos muertos en el ranking— **todos tenían un chequeo
previo**. Los **descubiertos tarde** —`temperature` + `require_parameters` (4 runs), skip
de niah sin margen (**378 runs en 23 modelos**), el juez corriendo donde su veredicto se
descarta (meses), `orchestration` midiendo prosa (meses)— **ninguno lo tenía**.

Anticipamos lo que tiene instrumento. No es cuestión de atención.

La diferencia con `audit_suites.py`, `E7`, `E8` y `check_endpoints.py`: esos buscan
problemas **conocidos**. El canario verifica que se cumplan los invariantes, así que caza
**regresiones que todavía no conocemos** — la clase que más duele. El caso que lo motivó
fue un arreglo de la mañana rompiendo algo de la tarde.

> ⚠️ **Su primera versión falló su propia validación**, y quedó como recordatorio: dijo
> "invariantes OK" para un modelo con las 4 pruebas de herramientas caídas, porque
> filtraba por runs exitosos y la lista quedaba vacía. **Un chequeo que no puede fallar no
> es un chequeo.** Si tocás `canario.py`, validalo contra un caso que SABÉS que está roto
> antes de confiar en un verde.

---

# Checklist de pre-vuelo (12-ago-2026) — 6 chequeos, 3 minutos, evitan un lote entero

Cada uno existe porque su ausencia costó un lote o publicó un dato falso **ese mismo día**.
No son teoría: son las seis formas concretas en que se perdió tiempo el 12-ago.

### 1. ¿El modelo es *thinking*? Probalo ANTES de medir

```bash
# una llamada con max_tokens=300 y mirá reasoning_tokens
# si vuelve content="" y reasoning>0 → es thinking y NO está en THINKING_MODELS
```
Muse Glimmer no matcheaba ningún patrón: **medio lote se habría medido en blanco** (content
vacío, score 0). Se cazó antes de pagar. De 11 modelos nuevos, **10 eran thinking y 5
devolvían vacío** con el budget por defecto.

### 2. ¿Las keys del script existen en el catálogo?

```bash
python -c "import sys;sys.path.insert(0,'.');from benchmarks.models import MODELS,OLLAMA_MODELS;\
print([k for k in KEYS if k not in {**MODELS,**OLLAMA_MODELS}])"
```
`--models lightning` (nombre de archivo) en vez de `nemotron-3.5-lightning` (key real) hace
que el runner imprima *"No hay modelos seleccionados"*, **salga con código 0** y el launcher
lo dé por completado. **Falla en silencio, dos vueltas seguidas.** Las 19 keys del script de
re-medición de tools estaban casi todas inventadas; se detectó validando, no corriendo.

### 3. ¿Hay OTRO launcher vivo?

```bash
ps -eo args | grep '[b]enchmarks/runner.py'
```
Relanzar después de un kill sin verificar dejó **dos launchers y 6 runners** peleando por la
misma cuota. Peor: los dos iban a escribir el MISMO archivo de resume. El ETA pasó a 10 h.

### 4. ¿Quién es el cuello — el modelo o el juez?

El modelo tarda ~5 s por test; **el juez phi-4 tardaba 77 s**. `microsoft/phi-4` tiene **un
solo proveedor** en OpenRouter: los runners paralelos hacen cola en el mismo endpoint, así
que **subir la concurrencia empeora el ETA**. Antes de agregar workers, medí dónde se va el
tiempo.

### 5. ¿El juez tiene que correr siquiera?

Solo donde NO hay verdad objetiva. 96 de 147 tests no-niah tienen `expected_answer` y su
veredicto **se descarta**: eran 2,1 h por modelo tiradas. Ya está arreglado en el runner;
si volvés a tocar esa condición, acordate de por qué está.

### 6. ¿A qué PROVEEDOR nos van a rutear?

```bash
curl -s https://openrouter.ai/api/v1/models/<id>/endpoints | jq '.data.endpoints[]|{provider_name,context_length,quantization,status}'
```
OpenRouter es un router. **40 de 68 modelos rankeados tienen proveedores no equivalentes**:
Nemotron 3 Super va de 8.000 a 1.000.000 de contexto según cuál toque; Kimi K2.6 de `int4`
a `bf16`. Nemotron 3.5 Lightning se midió en DeepInfra, que lo sirve con **28.672 de
contexto cuando su spec dice 262.144**, y con `status: -2`.

Desde el 12-ago cada run registra `upstream_provider`. **Endpoint ≠ modelo** — es lo que
Artificial Analysis formaliza como concepto de primera clase.

---

# Reglas de medición que quedaron instaladas

| Regla | Por qué |
|---|---|
| **`require_parameters: true`** cuando la request lleva `tools` o `response_format` | Doc de OpenRouter: sin eso, `tools` es solo *soft preference* y el proveedor puede **ignorarlas en silencio**. El modelo nunca las ve y queda anotado como "no llamó a la herramienta" |
| En OpenRouter se manda **`max_tokens`**, no `max_completion_tokens` | Ningún proveedor declara el segundo: con `require_parameters` filtra a TODOS y devuelve *"No endpoints found"* — incluso en modelos sanos |
| El skip por contexto **reserva el presupuesto de salida** | Un prompt de 128.000 en un modelo de 131.072 no deja lugar ni para un token de respuesta. **378 runs históricos** se perdieron así, contados como fallo del modelo |
| **El español necesita 1,62× más tokens** | Medido sobre 3.410 respuestas: 2,47 chars/token vs 4,00 de la heurística inglesa. Con `max_tokens=2048` entran ~920 palabras y los tests piden hasta 1.300 → **31% de respuestas truncadas por el harness** |
| Cada run guarda **su entrada y su `prompt_sha`** | "No me sirve el resultado si no sé lo que se envió". El catálogo completo está en `PROMPTS.md` |
| **Un launcher por frente**, con resume de nombre fijo y salto de lo ya completo | El entorno mata los background cada ~5 min; relanzar tiene que ser idempotente y no duplicar |

## Heurística de oro (Cristian, acertó 7 veces seguidas)

**Cuando una diferencia entre modelos se ve "demasiado grande", la primera hipótesis es
error de medición PROPIO, no un hallazgo.** Verificá la fuente Y que la fuente compute bien
(publicación == fuente == población sana) antes de publicar el número.
