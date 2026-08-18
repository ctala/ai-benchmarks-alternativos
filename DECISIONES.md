<!-- doc: vigente | verificado: 2026-08-13 -->
# Decisiones — índice único

> **Qué es esto y qué NO es.** Es un **índice**, no un lugar nuevo donde escribir. Cada
> fila apunta a dónde vive el detalle. El repo tiene 34 documentos en la raíz y las
> decisiones estaban repartidas en 13 de ellos: el problema nunca fue falta de
> documentación, fue **no saber dónde buscarla**.
>
> **Regla de uso:** antes de proponer un cambio de diseño, buscá acá. Si la decisión ya
> está tomada, se respeta o se revierte explícitamente — no se reabre por olvido.
>
> **Regla de escritura:** una decisión entra acá cuando se toma, en el mismo commit. Una
> línea: qué se decidió, por qué en pocas palabras, y el enlace al detalle. Si no cabe en
> una línea, el detalle va al doc que corresponde y acá queda el puntero.

## Cómo leerlo

- **Vigente** = manda hoy. **Revertida** = se probó y se deshizo (se deja para no repetirla).
- El **por qué** es lo que más caduca de memoria y lo que más cuesta reconstruir. Si una
  fila no tiene por qué, está incompleta.

---

## Qué se publica y cómo se puntúa

| Fecha | Estado | Decisión | Por qué | Detalle |
|---|---|---|---|---|
| 13-ago-2026 | **Vigente** | El titular es el **índice de calidad**; precio y latencia van como columnas, nunca dentro | El compuesto castigaba caro y premiaba barato sin decirlo: Opus 4.6 era #5 en calidad y se publicaba #18 | [PLAN-V4.1 §3](PLAN-V4.1.md) |
| 13-ago-2026 | **Vigente** | Escala **absoluta**: `score_calidad` = `quality_avg` sin z-scorear | El z-score estiraba 1,39 puntos reales a 8 publicados. Y anclado, agregar un modelo no mueve a nadie: se acaban las recalibraciones | [PLAN-V4.1 §3](PLAN-V4.1.md) · [CHANGELOG v4.1.0](CHANGELOG.md) |
| 13-ago-2026 | **Revertida** | ~~Segunda tabla de "mejor valor" (el compuesto)~~ | Correlacionaba **r = 0,943** con el índice de calidad: dos tablas para decir lo mismo | [PLAN-V4.1 §3 corrección](PLAN-V4.1.md) |
| 13-ago-2026 | **Vigente** | Los segundos ejes son **frontera de Pareto** y **calidad por dólar** | Son las únicas métricas que no correlacionan con calidad (deja fuera 69 de 82; r = 0,052). Todo promedio ponderado terminó siendo una copia | [PLAN-V4.1 §3](PLAN-V4.1.md) |
| 13-ago-2026 | **Revertida** | ~~Columna "Rinde" (score² ÷ costo)~~ | **r = 0,999** con ordenar por precio. La calidad varía 1,19× y el costo 772×: "valor" *es* precio | [CHANGELOG v4.1.0](CHANGELOG.md) |
| 14-ago-2026 | **Vigente** | La **dimensión agéntica** (reward de tareas Harbor) se publica **aparte**, nunca dentro del índice de calidad | Misma regla que tool calling y seguridad. El contraste lo prueba solo: Hermes 4 405B tiene calidad 8,20 y saca **0,00** en un agente porque no existe endpoint con herramientas. Promediar las dos cifras miente sobre las dos | [export_for_pages.py](benchmarks/export_for_pages.py) · [tareas-agente/RESULTADOS.md](tareas-agente/RESULTADOS.md) |
| 14-ago-2026 | **Vigente** | El **estado** vale más que el reward: un 0,00 por falta de endpoint ≠ un 0,00 por hacer mal el trabajo | Tres causas distintas (`sin_herramientas`, `rompe_bucle`, `hizo_mal_la_tarea`) que la media colapsa en un número. Ya publiqué una vez un 0,0 que era del harness | `export_harbor.py:FIRMAS` |
| 14-ago-2026 | **Vigente** | Un resultado agéntico **NO se hereda entre proveedores** del mismo id | El lote corrió contra `openrouter/<id>`; NIM/Groq/Ollama Cloud son endpoints distintos. Misma regla que la calidad (Qwen 3.5 397B: 8,42 NIM vs 7,97 Ollama Cloud) | [export_for_pages.py](benchmarks/export_for_pages.py) |
| 14-ago-2026 | **Vigente** | Corridas con `task_checksum` distinto **no se promedian** | Es `prompt_sha` para tareas Harbor: si cambió un test, no es el mismo examen. Medido: 2 de 231 corridas venían de una versión vieja y habrían entrado calladas | `export_harbor.py:_checksum_vigente` |
| 17-jul-2026 | Vigente | Referencia z-score **congelada por versión** para el compuesto | Antes, medir un modelo nuevo movía el score de todos | [README](README.md) |
| — | Vigente | **Nunca $0** como precio de un modelo del ranking | Un "gratis" gana el eje costo artificialmente y engaña la decisión que la calculadora existe para ayudar | [CLAUDE.md](CLAUDE.md) |
| 17-ago-2026 | **Vigente** | La entrada de CHANGELOG se escribe **con el commit**, en `## [No publicado]`, y el nivel de versión lo decide **qué archivo se tocó** | Once commits en una sesión con el CHANGELOG escrito al final y de memoria; el `git reset --hard` del mismo día probó que perder el relato no es hipotético | [VERSIONADO.md](VERSIONADO.md) · `check_changelog.py` |

## Qué se mide y con qué

| Fecha | Estado | Decisión | Por qué | Detalle |
|---|---|---|---|---|
| 13-ago-2026 | **Vigente** | `niah_es` recortada a **128K+** | 8K y 64K daban 78% y 75% de notas perfectas: no distinguían y eran la mitad de la suite más cara | [niah_es.py](benchmarks/tests/niah_es.py) |
| 13-ago-2026 | **Vigente** | `tool_calling_adversarial` entra al examen | Validada en los 82: **0% de runs perfectos** y 2,5× más dispersa que el índice general | `tests/tool_calling_adversarial.py` |
| 13-ago-2026 | **Descartada** | ~~`retrieval_distractores`~~ | Nació saturada: **76% de respuestas perfectas** en los 82; endurecida bajó solo a 70%. Retrieval a contexto moderado ya no discrimina entre modelos actuales — y ese eje ya lo cubre `niah_es` en 128K+ | `tests/retrieval_distractores.py` |
| 13-ago-2026 | **Vigente** | Una suite nueva se valida en **~8 modelos repartidos por el rango**, nunca en dos | Validé con uno bueno y uno malo, dio "separa 1,53", y con los 82 salió 76% saturada. La separación entre dos puntos no mide la dispersión | [RUNBOOK Regla 0.7](RUNBOOK-MEDICION.md) · `validate_suite.py` |
| 15-ago-2026 | **Vigente** | **NO se miden variantes de mayor esfuerzo de razonamiento** (`-thinking`, `Pro` del mismo id/precio) | Es el mismo estallido combinatorio que los proveedores: si se rankea GPT-5.6 Luna Pro, hay que medir Claude con extended thinking, o3 en high, Gemini con thinking budget… y el benchmark se va al infinito. Cristian: *"ahí sí se nos escapa el benchmark"* | esta tabla |
| 18-ago-2026 | **Vigente** | Se mide el **modo por defecto** de cada modelo, nunca un esfuerzo forzado. Y **cuál es ese default —medium o high— se determina empíricamente**, no por lo que diga la documentación | Cristian: *"los thinking aparte no se miden. Solo medimos los default del thinking de cada modelo, que debemos definir si es medium o high de manera empírica"*. Hoy el dataset declara «default del proveedor» en 178 modelos sin saber qué significa: **0 runs tienen `reasoning_tokens` registrados**, así que el dato para decidirlo todavía no se captura | esta tabla · pendiente en ROADMAP |
| 15-ago-2026 | **Vigente** | El criterio para separar «producto» de «esfuerzo» es el **precio**, no el nombre | Objetivo y verificable. GPT-5.6 Luna Pro cuesta **exactamente igual** que Luna ($0,1/$0,6) → es esfuerzo. Gemini 2.5 Pro cuesta $1,25/$10 vs $1,5/$9 del Flash → es producto. Ojo: a igual precio por token, el modo Pro consume MÁS tokens, así que la columna de costo lo subestimaría | `models.py` |
| 15-ago-2026 | **Vigente** | **Medimos al DEFAULT del proveedor**, verificado empíricamente | A OpenAI **nunca** se le manda `reasoning.effort` (GPT-5.x default = `medium`); a Anthropic, extended thinking **apagado**. Las 10 filas `-thinking` del catálogo tienen **0 runs**: la política ya se cumplía de hecho, faltaba escribirla. Es lo que recibe quien llama a la API sin configurar nada — el caso de la audiencia | `adapters.py:force_reasoning` |
| 15-ago-2026 | **Vigente** | Un modelo **sin medir de hace más de un año NO se mide** | El benchmark existe para decidir qué poner en producción hoy. Medir GPT-4o en ago-2026 gasta presupuesto en una decisión que ya nadie toma | `models.py:no_medir` |
| 14-ago-2026 | **Vigente** | **La calidad se mide UNA vez por modelo; el endpoint se mide barato por proveedor** | Medido sobre las 7 mediciones que ya teníamos del mismo id en distinto proveedor: la calidad varía **mediana 0,32** (sobre una población que abarca 1,43 en total), pero la latencia varía **1,8× mediana y hasta 7,5×**. Lo caro (91 suites) es propiedad del MODELO; lo que de verdad cambia entre proveedores —latencia, velocidad, soporte de tools— sale de cualquier corrida o de un ping. Sin esto el benchmark es combinatorio y el presupuesto no lo es | esta tabla · [MODELOS.md](MODELOS.md) |
| 14-ago-2026 | **Vigente** | Se mide un proveedor COMPLETO solo si (a) es la única ruta con herramientas, o (b) el ping muestra Δcalidad > ~0,4 | Nemotron solo tiene tools en NIM; Nemotron Super 49B da Δ0,74 entre proveedores. Son pocos casos y se detectan barato: primero el ping, y solo si hay señal, el lote | `check_endpoints.py` |
| 14-ago-2026 | ⚠️ **Provisoria** | La mediana de 0,32 sale de **7 modelos, no de 70** | Es un indicio, no una ley. Para volverla defendible hay que medir completa alguna variante y ver si cae dentro del rango — la candidata natural es Llama 3.3 70B en Groq, que además responde una pregunta de producción | — |
| 12-ago-2026 | Vigente | **Nunca medir en un endpoint `:free`** | Fallan 69,2% contra 10,9% de los pagos — seis veces más. Rate limits y cuantización distinta no son el modelo | [CLAUDE.md](CLAUDE.md) |
| 12-ago-2026 | Vigente | **No reinventamos el motor de medición**; se adopta de LiveBench, BFCL, τ-bench, Artificial Analysis | Nuestro valor está en QUÉ medimos (español, casos de emprendedor), no en cómo | [CLAUDE.md](CLAUDE.md) · [PLAN-V4.1 §0](PLAN-V4.1.md) |
| — | Vigente | **No se editan prompts** de tests ya medidos | Invalida la comparación con runs previos. `prompt_sha` lo detecta | [CLAUDE.md](CLAUDE.md) |
| — | Vigente | Dos umbrales: **20 runs** para reportar, **50** para rankear | Con 3-12 runs un modelo lidera por azar | [export_for_pages.py](benchmarks/export_for_pages.py) |

## Proceso y control de cambios

| Fecha | Estado | Decisión | Por qué | Detalle |
|---|---|---|---|---|
| 13-ago-2026 | **Vigente** | **Presentación ≠ medición.** La presentación se simula antes y puede cambiar; la medición cambia **una vez por trimestre** | Lo que se rehizo tres veces en dos días costó $0 — el desgaste era rotación de decisiones, no dinero | [PLAN-ESTABILIDAD R1](PLAN-ESTABILIDAD.md) |
| 13-ago-2026 | **Vigente** | Las suites se **agregan, no se reemplazan** | Una suite nueva cuesta $29-43 y no invalida ningún run. Editar una existente invalida todo el histórico | [PLAN-ESTABILIDAD R2](PLAN-ESTABILIDAD.md) |
| 13-ago-2026 | **Vigente** | Calendario: día 1 = release con presentación **congelada**; ventana trimestral para medición | Que dejar de ser sorpresa | [PLAN-ESTABILIDAD §4](PLAN-ESTABILIDAD.md) |
| 12-ago-2026 | Vigente | **Una regla sin instrumento que la haga cumplir es una regla que ya se rompió** | Se pagó cinco veces en un día: reglas correctas, escritas, que fallaban en silencio | [CLAUDE.md](CLAUDE.md) |
| 13-ago-2026 | **Vigente** | Cada superficie nueva llega con su guardrail, en el mismo commit | Corolario de la anterior | [PLAN-ESTABILIDAD R3](PLAN-ESTABILIDAD.md) |
| 14-ago-2026 | **Vigente** | **El mapa de superficies sincronizadas se GENERA, no se escribe** | Un doc a mano con la lista se desincroniza igual que todo lo demás — es el mismo bug un nivel arriba, y es literalmente el que se encontró: la docstring de `check_version` decía "seis superficies" y el código leía cuatro | [SUPERFICIES.md](SUPERFICIES.md) · `generate_superficies.py` |
| 14-ago-2026 | **Vigente** | Un guardrail nombrado en el mapa **tiene que existir en disco**, o el generador falla | Una fila que apunta a un chequeo borrado es una superficie sin quien la haga cumplir, disfrazada de superficie cubierta | `generate_superficies.py:CLASES` |
| 13-ago-2026 | **Vigente** | **El canario es un gate, no una recomendación**: el runner bloquea lotes de >3 modelos sin recibo fresco | Estaba documentado en 6 archivos y exigido en 0. Documentarlo por séptima vez no lo iba a arreglar | [RUNBOOK PASO 0](RUNBOOK-MEDICION.md) · `runner.py:_exigir_canario` |
| 13-ago-2026 | **Vigente** | Un doc curado **no incrusta datos**: si necesita datos, se genera, o el dato se enlaza | `PROVEEDORES.md` lleva 113 días diciendo "GPT-4o, GPT-5.2, o3" con cero menciones a GPT-5.6 | [check_docs.py](benchmarks/check_docs.py) |
| 15-ago-2026 | **Vigente** | **El registro de suites es UNO** (`benchmarks/suites.py`): pilar, etiqueta de menú y la línea humana. Viaja en `models.json`; el sitio no lo copia | Vivía a mano en tres archivos y divergió: **7 suites dichas de dos formas** y 2 sin nombre humano. Peor, **7 de 28 estaban en pilares distintos** según de dónde se mirara, y 3 no figuraban en el mapeo del export — o sea medidas y fuera del promedio de su pilar, en silencio | `suites.py` · `check_suites.py` |
| 15-ago-2026 | **Vigente** | Una página publicada **tiene dueño o motivo escrito**: la genera un `generate_*.py` o está en `HUERFANAS_DECLARADAS` como redirect | Había **3 huérfanas reales** sirviendo datos congelados de junio. No falla nada: carga, se ve bien y miente despacio. Se descubrió preguntando lo contrario de lo habitual — no «¿falta una página?» sino **«¿sobra una?»** | `qa_calculadora.mjs:Q15` |
| 15-ago-2026 | **Vigente** | Una comparación **no corona a un modelo que no rankea** sin decirlo | **22 de 72 lados** estaban coronados por uno no rankeado, 15 de ellos variantes PRO — que por la decisión del 15-ago no compiten. La decisión estaba escrita y las páginas de más tráfico la ignoraban | `generate_comparison.py:campeon` · `qa:Q14` |
| 16-ago-2026 | **Vigente** | **La elegibilidad se decide UNA vez, en el export, y se graba en el dato** (`m["elegible"]`) | Había **76 condicionales de filtrado en 25 archivos**, y cada regla se aplicó solo donde dolía el día que nació (`retired` 13-jul, `sirve_para_agentes` 14-ago). Lo escrito antes no las tenía; lo escrito después las copiaba del vecino | [QA.md](QA.md) · `elegibilidad.py` |
| 16-ago-2026 | **Vigente** | **Un solo comando de QA**, en seis áreas, y corre solo antes de cada push | Las piezas existían sueltas y había que acordarse de cinco comandos. Acordarse es justo lo que falla: tres fallos en un día lo probaron | `qa.py` · `instalar_hooks.py` |
| 16-ago-2026 | **Vigente** | Lo agéntico se ordena por **lo que el modelo LOGRÓ** (tareas Harbor), no por el pilar «Agentes» | Medido contra verdad objetiva: el pilar correlaciona **−0,20** con resolver la tarea; `tool_calling` solo, **+0,58**. Sus nueve suites miden prosa sobre agentes, no ejecución | `generate_rankings.py:score_agentico` · `app.js` |
| 16-ago-2026 | **Vigente** | Un script que reporta éxito **tiene que verificarlo** | `completar_examen` imprimió «✅ exámenes completados» sin correr un solo test, dos veces: el resume tapaba los tests fallidos y el output caía en un directorio que el pipeline no lee. Los dos fallos, en silencio | `completar_examen.py` |

### ⚠️ Cifras que la escala z-scoreada infló (revisar antes de citarlas)

El z-score amplificaba ~6× las diferencias reales. **Toda cifra escrita antes del 13-ago que
compare dos modelos está inflada en esa proporción.** La primera que se corrigió:

| afirmación | decía | real (escala absoluta) |
|---|---|---|
| Efecto del serving (Qwen 3.5 397B, NIM vs Ollama Cloud) | 7,96 vs 5,46 → "2,5 puntos" | **8,42 vs 7,97 → 0,45** |

La conclusión no cambia —medir variantes aparte sigue siendo correcto, 0,45 sobre un rango
de 1,39 mueve muchas posiciones— pero **el tamaño que publicábamos como justificación era
falso**. Lo detectó Cristian: *"el Qwen 3.5 me llama la atención, quizás algo se hizo mal"*.

**Accionable:** al citar cualquier comparación anterior al 13-ago, recalcularla contra
`score_calidad` en vez de copiarla.

**Barrido hecho (13-ago).** Se buscaron en todos los docs vivos las comparaciones numéricas
en prosa —`X vs Y`, `sube de X a Y`, `N puntos de diferencia`, `score X`— y el resultado fue
**mejor de lo temido**: cero afirmaciones con cifras infladas. Las únicas 9 coincidencias eran
la curva de costo (no compara modelos), una cita histórica entrecomillada, y `RECOMENDACIONES.md`,
que se regenera.

Pero el barrido encontró **otra cosa**: `RECOMENDACIONES.md` decía "calidad 8.73/10" para Llama
3.3 70B, y ese 8,73 era su nota **dentro del pilar Contenido** — su calidad global es 7,91.
Quien leyera la cifra la comparaba contra la escala general y se llevaba un modelo 0,8 puntos
mejor de lo que es. **No era un dato falso: era un dato sin su unidad.** Corregido — ahora el
rótulo nombra el pilar.

## Pendientes de decidir

| Tema | Qué falta saber | Dónde |
|---|---|---|
| Niveles de razonamiento | `effort=high` **no** es el techo de Anthropic. Estamos comparando modelos en configuraciones que no sabemos si son equivalentes | [CHANGELOG v4.1.0](CHANGELOG.md) |
| Benchmarks de terceros (SWE-Bench, GPQA) | Solo si la fuente es consultable y automatizable. Copiar de una landing devuelve el problema de cifras que caducan | [PLAN-V4.1 §3.ter](PLAN-V4.1.md) |
| Pilar del blog | Su sección de método explica el compuesto, que ya no se publica. Necesita reescritura, no find-replace | [CHANGELOG v4.1.0](CHANGELOG.md) |
| **Los 2 Nemotron rankeados están en `:free`, contra la regla** | La regla del CLAUDE.md nombra **estos dos modelos por su nombre** y dice medirlos por NIM. Están al revés: las entradas NIM figuran como `provider_variant` (fuera del ranking) y las `:free` son las canónicas. **No se puede invertir hoy**: NIM-omni tiene 24 de 30 suites y NIM-9b tiene 0 runs bajo su id real. Secuencia: **medir las NIM primero** (es gratis, 40 RPM), después invertir los roles. Lo destapó el lote del 13-ago: 18 de 19 fallos eran el omni con *"No endpoints found that support tool use"* | `models.py` · `audit_suites.py` |
| **9 docs citan modelos retirados** | Auditoría 13-ago: `COMPARATIVA`, `SUSCRIPCIONES`, `PROVEEDORES`, `CASOS_DE_USO`, `BENCHMARKS_EXTERNOS`, `THINKING_EXPLAINED` y otros recomiendan modelos que ya no existen — Devstral Small entre ellos. `check_consistency` lo avisa en cada corrida; limpiarlo es trabajo editorial pendiente | `check_consistency.py` |
| **5 docs vigentes sin verificar >90 días** | Ya no depende de que alguien se acuerde: `check_docs.py` los marca en cada corrida. Veredicto por doc abajo | `check_docs.py` |
| **3 suites medidas fuera del promedio de su pilar** | `agent_long_horizon` (91 modelos), `tool_calling_adversarial` (82) y `content_verificable` (92) tienen pilar natural y **no suman al promedio**, porque el mapeo viejo simplemente no las tenía. Las dos primeras son las suites **más agénticas** del benchmark y el pilar Agentes las excluye — eso explica que ese pilar tampoco mostrara a Gemini 3.6 Flash. Meterlas mueve números publicados: es **presentación**, se simula antes contra los runs en disco ($0) y se decide con la simulación a la vista | `suites.py:en_promedio` · `check_suites.py` |
| **`grok-4-1-vs-4-5` compara contra un retirado** | Grok 4.1 Fast ya no tiene endpoint. La página la genera `generate_variants.py` (no está huérfana), pero publica una recomendación que no se puede seguir | `generate_variants.py` |

### Veredicto sobre los 5 docs podridos (13-ago-2026)

**El patrón común: prosa curada con DATOS incrustados.** Un doc editorial no se pudre; lo
que se pudre es la tabla de modelos que alguien pegó adentro. De ahí la regla:

> **Un doc curado no incrusta datos. Si necesita datos, se genera — o el dato se enlaza,
> no se copia.**

| doc | qué pasa | veredicto |
|---|---|---|
| `PROVEEDORES.md` (113d) | El perfil editorial de cada proveedor **sirve** (fundadores, foco, fortalezas). Lo podrido es la lista de modelos incrustada: dice "GPT-4o, GPT-5.2, o3" y **cero menciones** a GPT-5.6, Opus 5 o Tencent Hy3 | **Sacar las listas de modelos**, dejar el perfil. Enlazar a MODELOS.md |
| `NIAH_ES_DESIGN.md` (102d) | Declara `version: v1 piloto` y la suite va por **v3 con grilla recortada hoy**. Documenta una contribución novedosa (primer NIAH público en español) → tiene valor propio | **Actualizar el bloque de versión**, no borrar |
| `NIAH_CROSSREF.md` (102d) | Compara con la literatura inglesa. Esa literatura no cambia | **Marcar `snapshot`** — es una comparación con fecha, no un doc vivo |
| `BENCHMARKS_EXTERNOS.md` (102d) | Es el terreno del candidato v4.2 (SWE-Bench/GPQA). Se toca cuando eso se decida | Revisar **junto con** [§3.ter](PLAN-V4.1.md) |
| `DESCUBRIMIENTOS.md` (110d) | Enlazado desde `generate_tests_md.py` y el sitemap: **se publica**, así que un lector llega ahí | Revisar contenido; es el de mayor riesgo de los cinco |

---

## Lo que sigue EXPUESTO (13-ago-2026)

Preguntado directo por Cristian — *"¿entonces nunca más perderemos info?"*— la respuesta
es **no**. Esto es lo que los guardrails **no** cubren, para que no se confunda "hay
instrumentos" con "está resuelto":

| Riesgo | Estado | Por qué |
|---|---|---|
| Que un guardrail se rompa y nadie note | **cubierto desde hoy** | `test_guardrails.py` les presenta un mundo roto y exige que fallen. Antes: 8 guardrails, 0 pruebas |
| **Duplicidad entre documentos** | ⚠️ **expuesto** | Nada detecta que dos docs digan lo mismo. La dispersión de 34 docs se encontró a mano |
| **Un doc verificado pero equivocado** | ⚠️ **expuesto** | `check_docs` verifica que ALGUIEN LO MIRÓ, no que el contenido sea correcto. Es honesto sobre eso, pero es un techo real |
| **Superficies nuevas sin guardrail** | ⚠️ parcial | La regla R3 lo exige; nada lo verifica. Una página nueva mañana no está cubierta hasta que alguien lo note |
| Pérdida de trabajo si muere una sesión | ⚠️ parcial | Los commits automáticos durante lotes fueron ad-hoc, no un mecanismo |

---

## Los instrumentos que hacen cumplir todo esto

Ninguna de las reglas de arriba se sostiene sola. Lo que las sostiene:

> **El mapa completo de qué tiene que coincidir con qué está en [SUPERFICIES.md](SUPERFICIES.md)**
> (generado). Esta tabla lista los instrumentos; ése lista las superficies que vigilan.

| Guardrail | Qué caza |
|---|---|
| `generate_superficies.py --check` | El mapa de superficies desactualizado · un guardrail nombrado que ya no existe |
| `check_version.py` | Las 7 superficies que declaran versión, desalineadas · falta de tag · falta de CHANGELOG |
| `check_consistency.py` | Un doc vivo citando un score que ya no existe |
| `check_calculator.py` | Umbrales fuera de rango · filtros decorativos · campos que el JS lee y el export dejó de emitir |
| `check_blog_consistency.py` | Cifras caducas en el blog |
| `canario.py` | Invariantes rotos ANTES de lanzar un lote |
| `check_endpoints.py` | Modelos muertos en el ranking |
| `validate.py` · `audit_anomalies.py` · `audit_suites.py` | Integridad de los datos publicados |
| `calculate_costs.py --estimar` / `--gastado` | Estimar antes de gastar · saber cuánto se gastó de verdad |
