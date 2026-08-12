# Plan v4.1 — una sola frontera de comparabilidad

> **Decisión (Cristian, 12-ago-2026): agosto se cierra con v4.1 funcionando.** No se hace
> un release intermedio con lo medido hoy para después rehacerlo. Todo lo que rompe
> comparabilidad entra en ESTE corte, se re-mide una vez, y queda una sola frontera
> documentada en vez de tres archivados sueltos.

## Por qué v4.1 y no v4.0.3

Hoy (12-ago) se encontraron cinco cosas que cambian **cómo se mide**, no solo qué se
publica. Cada una, sola, obliga a archivar y re-medir un pedazo. Juntas, obligan a
re-medir una vez:

| Hallazgo | Qué rompe |
|---|---|
| `max_tokens` 2048 vs 8192 según el modelo | condiciones de examen distintas para el mismo prompt |
| niah rediseñado (needles + grilla + techo) | otra prueba, ya archivados 2.058 runs pre-2-jun |
| Suite `integridad_idioma` nueva | eje que no existía |
| Ruteo sin `require_parameters` | ya corregido y re-medido (19 modelos, 342 runs) |
| Prompts sin persistir | ya corregido: `PROMPTS.md` + `prompt_sha` |

Los dos últimos ya están hechos. Los tres primeros son v4.1.

---

## 0. Lo que dice la investigación (no reinventar la rueda)

Investigado el 12-ago contra las fuentes, no de memoria. **Regla #10 del repo padre.**

| Práctica | Quién | Nosotros |
|---|---|---|
| Prompts publicados | lm-eval-harness: *"publicly available prompts ensures reproducibility and comparability"* · Artificial Analysis | ✅ hecho hoy |
| Ground truth objetivo > juez LLM | LiveBench: *"verifiable, objective ground-truth answers... **without the use of an LLM judge**"* | ✅ desde 13-jul, completado hoy |
| `max_tokens` uniforme | LiveBench: **4096 por defecto**, override explícito | ❌ **v4.1** |
| Recortar la traza de CoT | lm-eval-harness: `think_end_token` | ❌ **v4.1** |
| Model ≠ Endpoint | Artificial Analysis: *"A single model may have multiple endpoints across different providers"* | 🟡 dato crudo desde hoy |
| Costo/velocidad FUERA del ranking | Artificial Analysis: se reportan **aparte** del Intelligence Index | ❌ **a evaluar** |
| Intervalo de confianza publicado | Artificial Analysis: ±1% con evaluaciones repetidas | 🟡 tenemos `quality_ci95`, no se destaca |
| Refresco anti-contaminación | LiveBench: preguntas nuevas cada mes | ⛔ **descartado** (ver abajo) |

### ¿Adoptamos lm-eval-harness?

**No como herramienta; sí como práctica.** Está construido para otra forma: modelos de
HuggingFace, datasets fijos y evaluación por log-likelihood sobre opciones. El nuestro es
API generativa, en español, con suites escritas desde casos reales de emprendedores y
verificadores propios. Migrar sería un rewrite que además tiraría lo único que nos hace
distintos. Lo que **sí** se adopta: prompts publicados (hecho), versionado por hash
(hecho), y `think_end_token` (v4.1).

### Contaminación: descartada, y con argumento

LiveBench rota preguntas cada mes porque publica las suyas. Nosotros acabamos de publicar
206 prompts que llevan desde abril en un repo público. **Decisión de Cristian: no aplica.**
No somos un benchmark que los laboratorios miren para entrenar; somos una herramienta
chica para una comunidad concreta. El costo de rotar prompts (perder toda la serie
histórica cada mes) es enorme y el riesgo es hipotético. Queda anotado como riesgo
conocido y aceptado, no como olvido.

---

## 1. El español necesita 1,62× más tokens — medido, no estimado

Sobre **3.410 respuestas reales** del propio benchmark:

```
2,47 caracteres por token (español)   vs   4,00 de la heurística inglesa
→ el español necesita 1,62× más tokens para el MISMO texto
```

Qué significa en la práctica:

| `max_tokens` | Texto que entra en español | Tests que piden hasta 1.300 palabras |
|---|---|---|
| 2048 (actual, no-thinking) | ~920 palabras | ❌ **no caben** |
| **4096 (propuesto)** | ~1.840 palabras | ✅ con margen |
| 8192 (actual, thinking) | ~3.680 palabras | ✅ sobra |

**Esto explica el 31,3% de respuestas truncadas** en modelos no-thinking: no era que
escribieran de más, era que 2048 tokens en español no alcanzan para lo que el test pide.
El 4096 de LiveBench nos sirve por una razón que ellos no tenían — en español rinde la
mitad.

---

## 2. Los tres cambios de v4.1

### 2.1 `max_tokens` uniforme en 4096

**Un solo presupuesto visible para todos.** Se acabó el 2048/8192 según el modelo.

- Elimina la asimetría: mismo prompt, mismas condiciones.
- Elimina el truncamiento del 31% en no-thinking.
- Cuesta poco: se paga por token generado, no por presupuesto. Solo sube el gasto de los
  que hoy se cortaban.

### 2.2 El razonamiento se recorta, no se presupuesta

El multiplicador ×4 nació de un problema real (los thinking agotaban el budget razonando y
devolvían `content=""`) pero confundió dos presupuestos: los tokens de razonamiento
interno y los de la respuesta que se juzga.

Lo correcto, y es lo que hace lm-eval-harness: **separar la traza del razonamiento de la
respuesta**, juzgar solo la respuesta, y dar a todos el mismo presupuesto visible.

Verificado el 12-ago sobre 10 modelos: `reasoning: {enabled: false}` funciona en 7 de 10
por OpenRouter (GLM 5.2, Kimi K2.6, Qwen 3.7 Flash, Nemotron 3.5 Lightning, DeepSeek V3.2,
MiniMax M3, Ling 3.0 Flash). Fallan con 400 los *always-reasoning*: DeepSeek R1, Muse
Glimmer, Gemini 3.1 Pro.

⚠️ **Apagar el thinking NO es neutral**: en la prueba, Nemotron Lightning respondió 41,98%
y MiniMax M3 respondió 10,93% a un cálculo cuya respuesta es 19,13%. Con razonamiento
acertaban. Por eso **no se apaga el thinking**: se recorta la traza al puntuar y se deja
que cada modelo use su modo nativo. Las variantes `(thinking)` explícitas del catálogo (14
hoy) siguen como comparación aparte.

### 2.3 niah: un prompt canónico por (tipo, tamaño)

| | Hoy | v4.1 |
|---|---|---|
| Combinatoria | 5 tipos × 3 posiciones × 6 tamaños | **5 tipos × 6 tamaños** |
| Tests | 59 | **30** |
| Posición | dimensión propia | **fija por tipo, rotando** — cada tamaño cubre 25/50/75 con tipos distintos |
| Costo estimado | — | **−40%** (~$243 de input sobre 47 modelos con ventana declarada) |

Conserva la señal de *lost in the middle* sin multiplicar tests, y deja un prompt canónico
por celda. **No se materializa el texto**: serían ~35 MB contra 1,1 MB de corpus
commiteado. El prompt "ya existe" como corpus + receta determinista, y `PROMPTS.md`
registra la receta con su hash.

El gate de capacidad ya está corregido (12-ago): reserva el presupuesto de salida antes de
decidir si un tramo entra. Eso solo ya evitaba 378 fallos históricos falsos en 23 modelos.

---

## 3. A evaluar en v4.1 (no decidido): sacar costo y velocidad del score

Artificial Analysis reporta **costo y velocidad aparte** del Intelligence Index. Nosotros
los metemos al compuesto (15% + 7,5% + 7,5%), y el post-mortem de julio ya documentó la
consecuencia sin conectarla con esto:

> *"Fragilidad del z-score: con la calidad apelotonada (top todos 8.1-8.3, std 0.35), el
> compuesto queda decidido por costo/velocidad → Opus 4.8 con calidad 8.28 cae a 6.86."*

Es el mismo diagnóstico que AA resuelve por diseño. **Cambiar esto reordena el ranking
entero**, así que no entra por default: se mide primero cuánto se movería y se decide con
el dato a la vista. El wizard y las páginas por criterio de v4.0 ya iban en esa dirección.

---

## 4. Lo que NO entra en v4.1

- **Los scorers huérfanos ya están** (`json_valid`, `json_exact`, `language_check`,
  12-ago). Falta aplicar `rescore_all.py`: va ANTES de v4.1, con el baseline congelado.
- **`else: return 5.0` → `raise`**: su propio commit, después del rescore validado.
- **`RUNS_PER_TEST`**: medido el ruido (±0,58 con n=1). Decisión de Cristian: próxima
  tanda, no ahora.
- **Rotación de prompts**: descartada (ver §0).
- **Migrar a lm-eval-harness**: descartado (ver §0).

---

## 5. Orden de ejecución

1. **Cerrar el lote de agosto** (11 modelos nuevos) — en curso
2. **`rescore_all.py`** con los 3 scorers → diff contra `baseline_20260812_pre_scorers.json`
   → explicar todo movimiento >0,3 → aplicar
3. **Implementar 2.1 + 2.2 + 2.3** (rama aparte, un cambio a la vez, `audit_anomalies.py`
   y `validate.py` como gate)
4. **Re-medir** lo que cambió de condiciones: suites de contenido (por `max_tokens`) + niah
   completo + `integridad_idioma`
5. **Medir cuánto se movería** sacando costo/velocidad del score → decidir §3
6. `export_for_pages.py --recalibrate --scoring-version v4.1` — el único recalibrado del
   año, sobre dataset completo
7. DATASHEET, CheatSheet, tag `v4.1.0`, `check_consistency.py` en verde

## 6. Criterio de cierre

v4.1 está listo cuando:

- Todo modelo rankeado rindió el **mismo examen en las mismas condiciones** (mismo
  `max_tokens`, mismo tratamiento del razonamiento, mismos prompts verificados por hash)
- `niah` se corre solo donde entra, con prompt canónico por celda
- Ningún run del ranking viene de una medición con condiciones distintas
- `validate.py`, `audit_anomalies.py` y `check_consistency.py` en verde
- El CHANGELOG dice **qué cambió de posición y por qué**, con el diff automático de
  `release_diff.py`
