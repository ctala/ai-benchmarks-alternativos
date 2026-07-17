# Post-mortem — re-medición limpia + v4.0 (16-17 jul 2026)

Registro honesto de TODOS los errores generados y bugs encontrados durante la limpieza
de datos para el relanzamiento v4.0 del benchmark. El objetivo es que **no se repitan**.
Leer junto con `RUNBOOK-MEDICION.md` (guardrails operativos) antes de la próxima medición.

## Contexto

Al preparar el v4.0 (scoring congelado + wizard) se destapó que el `quality_avg` global
mezclaba runs de procedencia incompatible (vacíos-basura, fórmulas obsoletas, sin marca).
Se decidió la "solución definitiva": archivar la contaminación + re-medir limpio los huecos.
Eso desató una cadena de errores —míos y del código— que quedan documentados acá.

---

## A. Errores de proceso (generados por el operador/agente)

| # | Error | Causa | Fix |
|---|---|---|---|
| 1 | Indexar modelos por `name` en vez de `key` | `{m['name']:m}` colapsa duplicados → se leyó `or-gpt-4.1` vacío en vez de `gpt-4.1` (169 runs) → falso "GPT-4.1 no medido", se borró una sección correcta del pilar | Indexar SIEMPRE por `key` |
| 2 | El "definitivo" que colapsó el ranking | Se metió `_misma_formula` al entry de `aggregate_metrics` → ranking a 6 modelos, GPT-4.1 falso #1 | Filtro de procedencia SOLO en display por-suite + cobertura, NUNCA en quality global |
| 3 | Archivar el agéntico con criterio al revés | Se archivó por "scoring != verificable" antes de corregir `FORMULA_ESPERADA` (que esperaba juez-30-70) → casi se archivan los runs correctos | Corregir la fórmula ANTES de archivar; verificar con `_misma_formula` |
| 4 | Diagnóstico errado de 3 modelos que caían | Se dijo "sin cobertura fresca del backfill" cuando el backfill SÍ los cubrió; el problema real eran runs fallidos. El usuario dudó y acertó | Investigar los fallos reales (success/empty/error) antes de concluir |
| 5 | Estimación de costo 3-4× corta (~$18 dicho, ~$55-70 real) | (a) Se computó sobre registros PROMEDIADOS (1× tokens) pero se paga 3×; (b) reasoning/agentic disparan tokens; (c) Fable vía OpenRouter ~$33 solo. **El usuario tuvo que agregar créditos** | Estimar con ×RUNS_PER_TEST + multiplicador reasoning/agentic + llamar los outliers caros por nombre ANTES de correr |
| 6 | Concurrencia a 10 → rate-limit empties | Se paralelizó a 10 para ir rápido; la carga saturó OpenRouter → respuestas vacías puntuadas 0.0 = contaminación + gaps + parte del sobregasto. Probado: los modelos funcionan limpios aislados | **Baja concurrencia (2 workers) para suites con tools/multi-turn** |
| 7 | Casi re-correr el agentic completo de Fable (~$30) | El launcher incluía los 36 runs de `agent_long_horizon` de Fable | Cortar; solo `--rerun-empty` de los 6 vacíos (~$3) |
| 8 | Enfoque whack-a-mole | Se descubría cada problema cuando saltaba, no por barrido sistemático (el usuario lo marcó) | `audit_anomalies.py` como GATE obligatorio antes de recalibrar |
| 9 | Glob del shell abortó un chequeo | `_res_*` sin match en zsh abortó el script → falso "0 outputs guardados" cuando había 2.398 | Usar `2>/dev/null` / `nullglob` o Python para globs |
| 10 | Audit E6 falso positivo | Se leyó `cost_input` en vez de `cost_input_per_M` → $0 falso en los 67 rankeados | Verificar el nombre real del campo en el export |
| 11 | Seed inline con `chr()` rompió `residual.sh` | Escape roto → syntax error, no arrancó | Escribir launchers limpios (sin hacks de escape) |

## B. Bugs del código encontrados y arreglados

| # | Bug | Fix |
|---|---|---|
| A | Empty-response `success=True` infectaba la calidad (463 runs puntuados ~1.57 en muchos modelos) | Detector E1 + archivar no-mediciones |
| B | `FORMULA_ESPERADA` punto ciego: "sin `expected_answer` → juez"; el agéntico es rúbrica determinista (verificable) | Caso especial `agent_long_horizon` → verificable |
| C | Multi-turn no reintentaba turnos `success=False` (cortaba la trayectoria al primer "sin choices" transitorio) | Retry en turnos fallidos, no solo vacíos |
| D | Agéntico mezclado en `quality` global desde abril (2.881 runs) | Dentro + eje propio (`agentic_score`) |
| E | Procedencia mezclada (E2 fórmula obsoleta + E3 sin marca en quality cruda, ~3.000 runs) | Archivar + re-medir limpio |
| F | Juez rompe con `JSONDecodeError` en `parallel_vs_sequential_judgment` (gap en 3 modelos por el verificador, no el modelo) | 🔄 en verificación (reintentos 3×) |
| G | Hermes 4 405B/70B sin tool calling en su ruta OpenRouter → empties reales + handling messy (empty + solo-rubrica) | Decisión pendiente: score-0 limpio vs excluir |

## C. Hallazgo de diseño (no bug)

**Fragilidad del z-score:** con la calidad apelotonada (top todos 8.1-8.3, std 0.35), el
compuesto queda decidido por costo/velocidad → modelos de calidad top pero caros/lentos
(Opus 4.8 q8.28 → score 6.86) se hunden. No es error: es la razón de que el v4.0 lidere con
el **wizard + páginas por criterio** (calidad sola / valor / presupuesto), no con el compuesto.
Ver `RELANZAMIENTO-V4.md`.

## D. Meta-lección (la que engloba todo)

**Se fue a la velocidad/paralelismo antes que a la robustez** — y eso generó tanto los datos
basura (rate-limit empties) como el sobregasto (×3 no contado + outliers caros). Guardrails
que quedan como estándar:

1. **Baja concurrencia por default** (2 workers) para suites con tools/multi-turn. Subir solo
   tras verificar que no hay empties por rate-limit.
2. **Estimar costo con ×RUNS_PER_TEST y multiplicador reasoning/agentic**, y nombrar los
   modelos caros (Fable/Opus vía OpenRouter) ANTES de correr.
3. **`--rerun-empty` targeted, nunca re-correr suites completas caras.**
4. **Barrido sistemático (`audit_anomalies.py`) como gate**, no arreglar por síntoma.
5. **Verificar antes de afirmar** — "diferencia demasiado grande = sospechar la medición
   propia primero" (el usuario acertó repetidamente con esta heurística).
6. **Los outputs `.md` por modelo/test se guardan** (`results/responses/<timestamp>/`) y son
   auditables — usarlos para diagnosticar en vez de teorizar.

## E. Estado al cierre del post-mortem

- Data limpia para ~65 modelos (E1/E3 en rankeados = 0).
- Pendiente: juez roto (F), decisión Hermes (G), recalibración v4.0 (esperando OK).
- Costo real de la re-medición: ~$55-70 (vs $18 estimado).
