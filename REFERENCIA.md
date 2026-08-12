# REFERENCIA — lo que ya sabemos, para no volver a averiguarlo

> **Leer ANTES de investigar, proponer o "arreglar" algo.** Este archivo existe porque el
> 12-ago-2026 se perdieron horas re-descubriendo cosas ya sabidas y consultando campos que
> no existen. Si lo que vas a hacer está acá, ya está resuelto o ya está descartado — y en
> los dos casos está el porqué.
>
> Los otros tres docs que hay que leer antes de operar: `CLAUDE.md` (reglas duras),
> `RUNBOOK-MEDICION.md` (cómo medir), `PLAN-V4.1.md` (qué viene).

---

## 1. Nombres de campos — verificados contra los datos

**El error más caro y más tonto del 12-ago: consultar campos que no existen.** Pasó
**cuatro veces**, y cada vez produjo una conclusión falsa que casi se publica. Una query
sobre un campo inexistente **no falla: devuelve vacío**, y vacío parece un hallazgo.

### Existen (en `docs/data/models.json`, por modelo)

| Campo | Poblado | Qué es |
|---|---|---|
| `score_global` | 68/68 | compuesto z-scoreado: calidad 70% + costo 15% + velocidad 7,5% + latencia 7,5% |
| `quality_avg` | 68/68 | calidad titular (suites que puntúan; sin niah ni seguridad) |
| `quality_ci95` | 68/68 | intervalo de confianza 95% |
| `agentic_score` | 68/68 | ⚠️ **SOLO** de `agent_long_horizon` (multi-turno, **sin herramientas**) |
| `tool_calling_score_avg` | 68/68 | ⚠️ **DILUIDO** — ver §3 |
| `long_context_score` | 29/68 | eje niah. Parcial **por diseño**: solo quien rindió niah |
| `security_score` | 27/68 | eje `prompt_injection_es` |
| `cost_input_per_M` / `cost_output_per_M` | 68/68 | precio en el export. **En el config son `cost_input`/`cost_output`** |
| `dims_by_pillar` | 68/68 | `{pilar: {quality_avg}}` — **esto es lo que ordena las páginas pSEO** |
| `ranked` | 68/68 | ≥50 runs + no retirado + no `provider_variant` + no `self_hosted` + examen completo |
| `tested` | 68/68 | ≥20 runs |
| `retired_at` / `retired_reason` / `retired_kind` | desde 12-ago | fecha ISO · causa · `provider`\|`policy`\|`unknown` |
| `weights_url` | (config) | evidencia de `open_source`. Sin esto **no se declara** |

### En cada run (`benchmarks/results/benchmark_*.json`)

`quality` · `content_score` · `answer_score` · `judge_score` · `tool_calling` · `scoring`
(marcador de procedencia) · `prompt_sha` · `tool_calls_made` · `upstream_provider` ·
`response_file` (puntero al `.md` con la entrada y la respuesta completas).

### NO existen — inventados el 12-ago, cada uno costó una conclusión falsa

- `niah_score_avg` → es **`long_context_score`**
- `tool_calling_score` → es **`tool_calling_score_avg`**
- `tool_calls_made` en el JSON **antes del 12-ago** → no se persistía. Una query dio "0 tool
  calls en los 68 modelos" y **casi se publica como hallazgo**. Era el campo, no los modelos.
- `agentic_quality_avg` → es `agentic_quality`

**Regla: antes de escribir una query sobre un campo, enumerá las claves reales.** Cuesta
diez segundos y es la diferencia entre un hallazgo y una vergüenza.

---

## 2. Qué compone cada cosa (y qué NO)

| Métrica | Sale de | NO incluye |
|---|---|---|
| `quality_avg` | todas las suites que puntúan | niah, prompt_injection |
| `agentic_score` | **solo `agent_long_horizon`** | herramientas, tool calling |
| pilar **"Agentes"** (ordena `/mejor-llm-para-agentes/` y `/mejor-llm-para-n8n/`) | quality de `tool_calling`, `task_management`, `customer_support`, `orchestration`, `multi_turn`, `policy_adherence`, `agent_capabilities` | — |
| `long_context_score` | suites `niah_*` | — |
| `security_score` | `prompt_injection_es` | — |

**Las páginas pSEO NO ordenan por `score_global`**: ordenan por `pillar_quality` —capacidad
pura, sin costo ni velocidad— salvo las de precio. Cambiar eso ya se probó y se revirtió:
el compuesto coronaba modelos rápidos y baratos en páginas que prometen decir quién es mejor.

---

## 3. Defectos conocidos del instrumento — NO re-descubrir

Medidos el 12-ago-2026. Están **documentados y priorizados**; no son hallazgos nuevos.

| Defecto | Evidencia | Estado |
|---|---|---|
| **El pilar "Agentes" mide prosa, no herramientas** | las 4 suites con tools tienen correlación **−0,17 a +0,13** entre `quality` y `tool_calling`; en 3 de 4 **manda el juez** (hasta +0,99) | v4.1 (§2.4-2.5 del plan) |
| **`tool_calling_score_avg` diluido** | **87%** de sus runs son tests **sin** herramientas con valor por defecto. Aplasta el rango real de **3,11–8,36** a **6,09–7,28** | v4.1 |
| **`agentic_score` mal nombrado** | correlación **−0,26** con el tool calling real, sobre 68 modelos | v4.1 |
| **`orchestration` es single-turn** | pide narrar + ejecutar en un turno; castiga al modelo *act-first*. Caso: Lightning tool 10,0 → quality 2,5; Qwen tool 0,0 → quality 7,5 | v4.1 |
| **Ruido ±0,58 con `--quick`** | re-medición de 15 modelos: Δ simétrico. Con rango útil de 1,9 puntos, **la mitad es ruido** | `RUNS_PER_TEST` o `pass^k` — v4.1 |
| **Velocidad/latencia medidas single-shot** | pesan 15% del score y el caso de uso (Hermes, n8n) es concurrente. Bench propio del Spark: Glimmer pasa de 11 a 180 tok/s agregados según concurrencia | v4.1 |
| **`max_tokens` 2048 vs 8192 según modelo** | **31,3%** de las respuestas no-thinking truncadas por el harness | v4.1 |
| **`else: return 5.0` en el dispatcher** | hoy **no hay tipos huérfanos** (17 usados, 17 con scorer), pero nada impide el próximo | pendiente, commit propio |
| **Punto ciego de `audit_suites.py`** | no cubre suites con rúbrica determinista (`agent_long_horizon`): devuelve `—` en vez de fallar | anotado |

**Ya arreglados el 12-ago** (no re-arreglar): precios y `PRICING` derivado · `check_endpoints`
sin `.env` · los 3 scorers huérfanos · skip de niah sin margen de salida · `require_parameters`
· juez corriendo donde su veredicto se descarta · persistencia de prompt/`prompt_sha`/
`tool_calls_made`/`upstream_provider` · retiros estructurados y re-verificables.

---

## 4. Lo ya investigado afuera — NO volver a investigar

Verificado contra las fuentes el 12-ago-2026. **Nuestro valor no está en el motor de
medición, está en qué medimos** (ver la regla en `CLAUDE.md`).

| Fuente | Qué hace | Qué tomamos |
|---|---|---|
| **LiveBench** | *"verifiable, objective ground-truth answers... without the use of an LLM judge"* · `max_tokens` 4096 por defecto · refresca preguntas cada mes | verdad objetiva > juez ✅ · budget uniforme (v4.1) |
| **lm-eval-harness** | *"publicly available prompts ensures reproducibility"* · `think_end_token` para recortar CoT | prompts publicados ✅ · recorte de CoT (v4.1) |
| **Artificial Analysis** | Model ≠ Endpoint · Intelligence Index = promedio ponderado con **costo y velocidad APARTE** · CI del 95% | `upstream_provider` ✅ · sacar costo del score (a evaluar) |
| **BFCL** | objective checks sin juez · **state-based evaluation** · **subset matching** de trayectorias · multi-turn con tope de pasos · categoría de alucinación de herramientas | diseño completo de la suite agéntica (v4.1) |
| **τ-bench** | **`pass^k`**: fiabilidad sobre k intentos, no una media | reemplaza subir `RUNS_PER_TEST` (v4.1) |

---

## 5. Decisiones ya tomadas — NO re-litigar

| Decisión | Cuándo | Por qué |
|---|---|---|
| **No migrar a lm-eval-harness** | 12-ago | está hecho para modelos HF y log-likelihood sobre datasets fijos; el nuestro es API generativa en español con suites de casos reales. Migrar sería un rewrite que tira lo único diferencial |
| **No rotar prompts contra contaminación** | 12-ago | LiveBench rota porque los laboratorios lo miran. Nosotros somos una herramienta chica para una comunidad concreta; rotar cuesta toda la serie histórica. **Riesgo conocido y aceptado** |
| **No subir `RUNS_PER_TEST` ahora** | 12-ago | va en la tanda siguiente; con n=3 el error estándar solo cae ~1,7× y probablemente no alcance. Calcular antes de elegir el número |
| **Cambiar prompts de tests que no miden lo que dicen** | 12-ago | *"la comparabilidad de un número equivocado no vale nada"*. Por eso es v4.1 y no un parche |
| **No re-medir antes de arreglar los ejes** | 12-ago | alimentar un eje mal compuesto es pagar dos veces |
| **Juez: Phi-4, y no se cambia** | 13-jul | bakeoff de 6 jueces de 14B a 671B: **todos saturan**, correlación 0,00 con la verdad objetiva. No es problema de tamaño. La solución fue sacar al juez de donde hay verdad verificable |
| **Costo y velocidad siguen en el score (por ahora)** | pendiente | AA los reporta aparte; cambiarlo reordena todo el ranking. Se decide con el dato a la vista, no por analogía |

---

## 6. Invariantes — romper uno invalida el benchmark

1. **Nunca $0 como precio de un modelo del ranking.** Gana el eje costo artificialmente.
2. **Nunca un score escrito a mano en un doc vivo.** El z-score caduca solo. Guardrail:
   `check_consistency.py` — que **no ve los bloques auto-generados**: por eso hay que correr
   `regenerate_all.py` antes de commitear.
3. **Un `(id, name)` = UNA config en `MODELS`.** Dos configs iguales reciben los mismos runs.
4. **Indexar por `key`, nunca por `name`.** `name` colapsa duplicados.
5. **Los prompts no cambian sin bump de versión.** Verificable con `prompt_sha` + `PROMPTS.md`.
6. **`open_source: True` exige `weights_url`.** Alimenta el ranking "solo open-source".
7. **No se regenera producción a mitad de un backfill.**
8. **Una regla sin instrumento que la haga cumplir ya se rompió.** Al agregar una regla, la
   pregunta es qué falla ruidoso si se viola.
9. **Los detectores cazan ausencia; la contaminación es presencia.** Un run contaminado tiene
   número, forma válida y pasa `validate.py`.
10. **Empate perfecto = sospechar del instrumento**, igual que una diferencia demasiado grande.

---

## 7. Herramientas — qué corre y para qué

| Script | Para qué | Cuándo |
|---|---|---|
| `sync_prices.py` | precios contra la API de OpenRouter | antes de cada release |
| `check_endpoints.py` | ¿siguen vivos? `--recheck-retired`: ¿alguno revivió? | antes de un lote y del release |
| `audit_suites.py` | **¿cada suite mide lo que su nombre dice?** | en `regenerate_all` |
| `audit_anomalies.py` | E1-E8: barrido de anomalías en los datos | gate antes de recalibrar |
| `validate.py` | el portero: si no cuadra, no se publica | antes de publicar |
| `check_consistency.py` | scores hardcodeados en docs vivos | antes de cada push |
| `release_diff.py` | el DATASHEET, ordenado por impacto en una decisión | en el release |
| `generate_prompts_catalog.py` | `PROMPTS.md` con los 206 prompts y sus hashes | en `regenerate_all` |
| `rescore_costs.py` | propaga precios nuevos a runs históricos | tras `sync_prices` |
| `rescore_all.py` | re-puntúa calidad. **Archiva los originales solo** | evento deliberado |
| `regenerate_all.py` | pipeline maestro | antes de cualquier commit que toque datos o docs |
