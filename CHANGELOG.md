<!-- doc: snapshot -->
# Changelog

> **Regla de flujo**: todo lo que se marca como completado en ROADMAP.md se migra aquí con el commit correspondiente. El ROADMAP mira hacia adelante, el CHANGELOG deja traza de lo que pasó.

## [No publicado]

- **El canario ahora CONSERVA la evidencia de lo que falla.** Salió 🔴 con «1 de 4 tests
  con herramientas fallaron (parcial, **revisar por qué**)» — y no había con qué
  revisarlo: borraba su archivo temporal siempre, así que el error se iba con él. Hubo
  que reproducir el fallo aparte para descubrir que era transitorio.

  Un detector que te manda a investigar y borra la prueba te obliga a repetir el
  experimento, y un fallo intermitente puede no volver a aparecer. Ahora, **sólo si algo
  falló**, deja `benchmarks/results/_canario_fallo_<modelo>.json` con los runs completos.
  Verificado con un fallo simulado.

- **Descartado que `effort=medium` rompa el tool calling.** Era la hipótesis obvia —
  `reasoning` en `extra_body` + `require_parameters` podría dejar al modelo sin proveedor
  con herramientas— y es falsa: la reproducción directa dio 4/4 con tool calls emitidas,
  y la segunda pasada del canario ✅ 16/18. **Queda sin explicar** que con `medium` fallaran
  5 y 2 de 18 mientras sin effort fue 0 de 18; con n=2 no prueba nada, pero es la señal a
  vigilar y ahora hay evidencia guardada para mirarla.


- **El PDF del mes quedó desactualizado al entrar Hy4, y su guardrail lo cazó.** Con 100
  modelos en vez de 99 se movieron cifras que el cheatsheet ya tenía impresas
  (`check_release_mensual` marcó 3 parejas modelo↔cifra sin respaldo en `models.json`).
  Regenerado: **68 parejas verificadas, 0 sin cuadrar**. Es justo el caso para el que se
  construyó ese chequeo — un release se desincroniza solo cuando cambia el dato debajo.


- **`MAPA.md` no declaraba su estado, y eso rompía el guardrail de OTRO chequeo.** Sin
  `<!-- doc: generado -->`, `check_docs` lo contaba como doc sin estado y devolvía 1;
  eso hacía fallar la prueba de sabotaje de `check_docs`, que exige verde cuando no hay
  vencidos. Un doc nuevo tumbando el guardrail de otro es un acople que sólo aparece
  corriendo la suite entera, no el chequeo que uno acaba de tocar — y lo cazó el
  pre-push, no yo.


## [v4.13.0] - 2026-09-03 — Hy4 entra al ranking (100 modelos), y las fichas dejan de publicar el puesto de otra escala

- ⚠️ **95 de las 100 fichas publicaban un puesto que no correspondía a su nota.**
  `generate_model_cards.py` ordenaba por `score_global` —el z-score interno, abandonado
  como escala publicable en v4.1— mientras el tile dice «Nota de calidad 8,39 /10 · #28
  de 100». La nota de una escala junto al puesto de otra, en la misma línea. Desvío medio
  **8,6 posiciones, máximo 29**: Gemini 3.5 Flash Lite se publicaba **#10 cuando por su
  nota es #39**.

  Tercera aparición del mismo error en dos días (cheatsheet, `release_diff.py`, fichas).
  Por eso el test no comprueba el sort: **lee el HTML publicado** y compara el puesto que
  imprime contra el orden por `quality_avg`. Verificado rompiéndolo.

- **`MAPA.md`: dónde vive cada artefacto, quién lo escribe y quién lo vigila.** Cristian,
  después de verme buscar las fichas en tres rutas equivocadas: *"tenemos que tener ese
  mapa listo y no construirlo cada vez"*. Lo caro no fueron los tres intentos — fue que
  en uno **concluí que faltaban 95 fichas cuando estaban las 100**. El dato ya vivía en
  el código (`check_fichas_alcanzables.py` sabe la ruta); faltaba poder leerlo sin leer
  el código.

  Se **genera** y cada fila se verifica contra el disco: si una ruta no existe, si el
  generador desapareció o si un guardrail fue renombrado, falla ruidoso. Entra al
  pipeline maestro con `--check`. Saboteado en sus tres modos (artefacto movido,
  guardrail renombrado, fila nueva sin regenerar).

- **Tencent Hy4 preview entra al ranking: 8,39, puesto 19 de 100.** Terminó su examen
  completo (213 tests, **cero errores**) y sus 4 tareas agénticas en Harbor (3 perfectas,
  una 0,92 → eje agéntico 9,06, #28). Se midió con la configuración ANTERIOR a v4.12.0
  —sin `effort`, presupuestos viejos—, así que **es comparable con los otros 99**: sus
  runners arrancaron a las 08:24 y el cambio entró a las 14:44.

  El cruce con el uso real se sostiene: Hy4 es **#6 del mundo por tokens procesados y
  rinde #19**. Y contra su antecesor, el titular no es el que parece: Hy3 sale mejor en
  el índice (8,49 vs 8,39), pero **sobre los 193 tests que rindieron ambos el Δ es +0,27
  A FAVOR de Hy4, con t≈1,77 — dentro del ruido** (gana 41, pierde 47, empata 105). O
  sea: son indistinguibles en calidad y **Hy4 cuesta 4,8 veces más**. Mismo hallazgo del
  mes que GLM 5.3 vs su Flash, ahora dentro de Tencent.

## [v4.12.0] - 2026-09-02 — se manda effort=medium, y el presupuesto sube para absorberlo

- **El `effort` no significa lo mismo entre proveedores, y eso limita lo que compra
  mandarlo.** Cristian planteó que *"quizás el por defecto siempre fue high"* — que sería
  la mejor noticia posible, porque haría comparables los 46 thinking ya medidos. Se probó:
  5 modelos × 4 niveles × 5 preguntas, midiendo `reasoning_tokens` reales.

  | modelo | sin param | low | medium | high |
  |---|---:|---:|---:|---:|
  | GLM 5.3 | **619** | 0 | 0 | 112 |
  | GPT-5.6 Luna | 117 | 127 | 123 | 149 |
  | DeepSeek V4 Pro | 457 | 411 | 388 | **369** |
  | Qwen 3.8 Flash | 720 | **1.630** | 731 | 244 |
  | Kimi K2.7 Code | 161 | 414 | **550** | 126 |

  **No hay monotonía en 3 de 5**: en Qwen `low` produce 6,7× más razonamiento que `high`;
  en DeepSeek la pendiente va al revés; en GLM `low` y `medium` lo apagan mientras el
  default razona 619. El default no es `high` — ni ningún nivel fijo.

  Consecuencia: mandar `medium` uniformemente **estandariza el string que enviamos, no el
  esfuerzo real**. Sigue siendo preferible a no mandar nada (el request queda explícito y
  reproducible), pero no compra la comparabilidad entre modelos que uno esperaría. Datos
  crudos en `results/experimento_effort_por_proveedor_20260902.json`.


- ⚠️ **Corrección: las cifras de truncamiento publicadas en v4.11.0 eran falsas.** Decían
  «21,3% de los runs no cabría con `high`» y «se truncaría el 86% de `strategy`». Se
  calcularon sobre `THINKING_MIN_TOKENS = 8.192`, cuando el presupuesto real viene
  **calibrado por suite** desde el 18-ago (32.768 en `strategy`, 65.536 en
  `agent_long_horizon`). Las cifras reales con aquellos techos eran **2,6% y 0,2%**.

  **La conclusión que sostenían se cae con el error**: no había riesgo de truncamiento
  que justificara no forzar el effort. La lección, que ya es regla del repo en otra
  forma: **un techo se lee de `presupuesto_de(suite)`, nunca de la constante** — la
  constante es un piso para call sites viejos, no el presupuesto.

- **Se manda `reasoning: {effort: medium}` a los thinking models** (Cristian, 2-sep).
  Revierte explícitamente la política del 15 y 18-ago de medir «el default del
  proveedor». Motivo: ese default lo elige cada proveedor y no lo controlamos ni lo
  sabemos, así que dos modelos podían estar rindiendo el examen en modos distintos sin
  que se notara. **Un test puede pedir otro** (`"reasoning_effort": "high"` en su dict).

  ⚠️ **Cambia el examen** (PLAN-ESTABILIDAD R2): los 46 thinking rankeados se midieron
  sin el parámetro.

- **Presupuesto de salida subido**: defecto 24.576→32.768, suites largas 32.768→49.152,
  `agent_long_horizon` 65.536→98.304. Cristian: *"igual podemos crecer el max tokens de
  todo, ya que no quiere decir que lo vayan a ocupar todo"* — y es así, **se factura lo
  generado, no el límite**. Hace falta porque el effort **reparte** el presupuesto en vez
  de agregarlo. El techo lo pone el proveedor, no el precio (131.072 «varios lo rechazan
  de plano»), así que se probó: **7 modelos repartidos por el catálogo aceptan
  32k/48k/64k/96k, los cuatro**. Con esto no cabe el **0,03% con medium** y 1,11% con high.

- **El parámetro nuevo casi rompe tres rutas enteras.** El runner llama a los 4 providers
  con la misma firma, y sólo `UnifiedProvider` aceptaba `reasoning_effort`: los otros tres
  habrían dado `TypeError` en runtime **sólo para sus modelos** —Opus/Sonnet/Fable por
  `claude_code`, los `-pro` por `openai_responses`— con el resto del lote en verde. Los
  cuatro alineados y con `test_todos_los_providers_aceptan_lo_que_el_runner_manda`.


- **Tencent Hy4 preview: examen en curso** (122 de 213 tests al momento de este bump).
  Entra al ranking en la próxima regeneración; sin examen completo no rankea.

## [v4.11.0] - 2026-09-02 — el esfuerzo de razonamiento no se fuerza, y ahora está medido

- **Se midió si conviene forzar el esfuerzo de razonamiento. No conviene, y ahora está
  probado.** La política del repo era medir «el modo por defecto de cada proveedor», y
  las filas del 15 y 18-ago pedían **verificarlo empíricamente** — con la nota de que el
  dato no se capturaba porque *«0 runs tienen `reasoning_tokens` registrados»*. Ya se
  capturan, así que se corrió el experimento: 3 modelos × 9 tests de razonamiento con
  `reasoning: {effort: medium}`, contra su propio histórico.

  **Resultado: Δ calidad −0,45 (n=24) y −1.407 tokens de respuesta, con el 79% de las
  respuestas más cortas.** El segundo número es el que manda, porque no pasa por el juez.
  El mecanismo es aritmético: **el effort no agrega presupuesto, reparte el que hay.**
  Sobre `THINKING_MIN_TOKENS = 8.192`, lo que el modelo gasta pensando se lo quita a la
  respuesta — Qwen 3.7 Flash pasó de 5.845 a 1.265 tokens en `business_analysis`.

  Y `high` sería peor: dejaría **1.639 tokens para responder**, truncando el **86% de
  `strategy`**, el 80% de `agent_long_horizon` y el 76% de `startup_content` (medido
  sobre los 59.128 runs exitosos en disco). Es el fallo de abril —165 runs vacíos— pero
  peor, porque **una respuesta cortada puntúa y una vacía no**.

  Queda la bandera `BENCH_REASONING_EFFORT` (default `off`) para re-medirlo el día que
  se suba el presupuesto, sin tener que volver a escribir el envío.

- **El envío del parámetro estaba escrito de una forma que habría tumbado el lote.** Iba
  como `kwargs["reasoning"]`, y `reasoning` no es parámetro del SDK de OpenAI: cada
  llamada a un thinking model moría con *«unexpected keyword argument»*. El módulo
  importa sin ruido, el linter calla y **los modelos normales siguen verdes** — la forma
  más cara de romperse. Lo destapó espiar el request real, no leer el código. Va en
  `extra_body`.

  De ahí el guardrail: **3 tests que espían el request armado sin tocar la red**, y los
  cuatro modos de romperlo verificados en rojo a propósito (default encendido · el
  parámetro arriba · mandado a los no-thinking · mandado a otro proveedor). Se declaró
  `test_unitarios.py` en `check_caminos.py:SANCIONADOS` con su razón: construye la
  llamada para inspeccionarla, y corta antes de la red.


- **Tencent Hy4 preview: examen en curso.** Entró al catálogo el 2-sep por el cruce con
  el uso real —es #6 del mundo por tokens y no lo medíamos— y su lote sigue corriendo
  mientras esto se publica: ~13 h a dos runners, porque razona y tiene 1M de contexto.
  **No aparece en v4.10.0 a propósito**: sin examen completo no rankea. Entra en la
  próxima regeneración, que son dos minutos.

## [v4.10.0] - 2026-09-02 — el cruce con el uso real, y el release del mes verificado contra la fuente

- **`USO_VS_CALIDAD.md`: el cruce entre lo que el mundo usa y lo que rinde.** Los
  benchmarks académicos no daban para un documento —solo 3 de nuestro top 20 tienen score
  en `BENCHMARKS_EXTERNOS.md`, que es de abril, y varios modelos nuevos ni tienen paper—,
  así que el cruce se hizo contra el **ranking de uso real de OpenRouter** (tokens
  procesados, semana al 1-sep). El hallazgo: **el modelo más usado del planeta —12,1T
  tokens/semana— está #67 de 99 en calidad.** Pero en la cima sí coinciden (GLM 5.3 Flash
  #2/#4, Luna #3/#2): el uso no es ciego, es lento.

  La mitad del valor del documento es que **obliga a mostrar lo que nos falta**: tres de
  los diez más usados no están en nuestro ranking —uno sin medir, uno *stealth* que no es
  medible con nuestro estándar, dos por la política de `:free`—. Un ranking que solo se
  compara consigo mismo nunca descubre eso.

- **Tencent Hy4 preview entra al catálogo**, a pedido de Cristian y antes del lanzamiento
  del mes. Es **#6 en uso mundial** (5,72T tokens/semana) y no lo medíamos. Declara
  `reasoning` y **no estaba en `THINKING_MODELS`**: sin ese patrón se habría publicado con
  las respuestas cortadas, como le pasó a Opus 5 en agosto. Canario 18/18; el examen corre
  con 2 runners por la Regla 0.3 del runbook.

- **El PDF del mes publicaba cifras que ningún modelo tiene.** Cristian: *"revisa que no
  haya problemas con la data del datasheet… debemos usar la misma data del benchmark en
  todos lados"*. Al mirarlo aparecieron **tres clases de desfase en los dos generadores
  del release**, ninguno roto — todos VIEJOS:

  1. `generate_cheatsheet.py` ordenaba el top 10 por `score_global`, el z-score
     abandonado en v4.1, y citaba «7,18» donde el sitio dice «8,53».
  2. Usaba `score_by_pillar` en las tablas por categoría: para Qwen 3.8 27B en Coding
     eso da **8,25**, y lo publicado es **9,95**. Doce usos.
  3. La sección de recomendaciones tenía **las cifras escritas a mano dentro de un
     generador data-driven**: «GPT-OSS 120B · 8.15» cuando el valor vivo es 8,03, y
     «Qwen3 Coder · calidad 7.85» cuando es 7,78. Cada mes el PDF reimprimía el número
     del día en que alguien lo tecleó.

  Los tres sobrevivieron por la misma razón: **son generadores que se corren una vez al
  mes.** Entre corrida y corrida nadie los mira, así que un cambio de criterio los deja
  atrás sin hacer ruido. `check_consistency.py` no los cubría a propósito —los datasheet
  son snapshots y deben conservar su valor histórico— y ese «a propósito» dejaba un hueco
  justo el día en que el snapshot se crea.

- **`check_release_mensual.py` cierra ese hueco, y costó tres intentos:**
  · «¿la cifra existe en models.json?» — inútil: «7.18» aparece **15 veces** en el JSON.
  · «buscar el nombre y mirar lo que sigue» — falsos positivos, «GLM 5.3» matchea dentro
    de «GLM 5.3 Flash».
  · lo que funciona: leer **filas de tabla** y verificar la PAREJA modelo↔cifra, que es lo
    único que puede mentir. Hoy vigila 87 parejas entre el datasheet y el PDF.

- **CheatSheet PDF de septiembre generado** (10 páginas). WeasyPrint no encontraba
  `libpango` pese a estar instalado por brew — se resuelve con
  `DYLD_FALLBACK_LIBRARY_PATH=$(brew --prefix)/lib`, anotado para la próxima.

- **Reporte de septiembre publicado** (`DATASHEET_2026-09.md`), el primero desde junio.
  Titular: **la versión cara dejó de comprar calidad, y este mes se puede probar dentro
  de la misma familia** — GLM 5.3 saca 8,52 a $21/mes y su Flash 8,51 a $1; en escribir
  contenido, Claude Opus 5 Fast 9,11 a $234 contra Qwen 3.8 Flash 9,10 a $2. Cada cifra
  del documento se verificó contra `models.json` antes de publicar, incluidas las 12
  filas del top por categoría.

- **`release_diff.py` llevaba desde junio generando el release con el score equivocado.**
  Usaba `score_global` —el z-score que se abandonó en v4.1— así que habría publicado
  «7,18» donde el sitio dice «8,53». No se notó porque el script no se corría desde el
  último datasheet: **un generador que se usa una vez al mes se desincroniza en silencio.**
  Ahora lee `quality_avg`.

- **Y su sección de movimientos era ruido.** Bastaba con moverse 3 puestos para entrar,
  así que al sumar tres modelos nuevos arriba listaba **cuarenta filas con «(+0.00)»**:
  bajaron de puesto porque la lista creció, no porque cambiara nada. El puesto es
  relativo a quién más hay; la nota es del modelo. Ahora sólo entra quien cambió su nota.

- **Al escribir el reporte inventé tres cifras de junio** (catálogo 128, 61 completos,
  20.011 runs) citándolas de memoria. Las reales eran **143, 91 y 10.508**, y el grep
  contra el datasheet de junio las desmintió antes de publicar. Es exactamente lo que el
  documento denuncia de los modelos: un número que suena plausible no es un número
  medido.

- **La versión cara de GLM 5.3 no compra nada medible, y ahora está demostrado dentro de
  la misma familia.** `GLM 5.3` saca **8,52** y cuesta **$21 al mes**; `GLM 5.3 Flash`
  saca **8,51** y cuesta **$1**. Una centésima de diferencia, **18 veces el precio**. Es
  la tesis del benchmark —«los de arriba dan casi la misma calidad; lo que cambia es el
  precio»— probada entre dos SKU del mismo proveedor, que es el caso más difícil de
  discutir.

- **Qwen 3.8 Flash entra como #1 con 8,53, a $2 al mes.** Y con eso el top-4 completo
  cuesta entre $1 y $3 mensuales, mientras **Claude Opus 4.8 queda #8 con 8,48 y $117 al
  mes**: 58 veces más caro por 0,05 puntos menos.

- **El susto: ese #1 estuvo a punto de publicarse inflado.** El primer lote de Qwen 3.8
  Flash devolvió **8,61** —que habría sido el mejor número del catálogo— pero con sólo
  **107 runs de 213 tests**: 64 errores 429 de Alibaba se llevaron 40 tests, y no
  cualquiera, sino los pesados (`business_strategy` 0 de 5, `business_audit` 4 de 10,
  `deep_reasoning` 3 de 6). Al completarlos, la nota **bajó a 8,53**. Sesgo de
  supervivencia de 0,08 puntos, suficiente para inventar un liderazgo que no existía.
  Lo frenó el criterio de examen completo: con `ranked=False` el número no llegó a
  ninguna página.

  La causa del 429 fue nuestra: cuatro runners simultáneos contra un modelo estrenado
  hacía cinco días. Con uno: cero errores. Con dos: uno. **Un modelo recién lanzado
  aguanta menos paralelismo**, y eso ahora está en el runbook.

- **Nombres que confunden, anotado para la próxima:** lo que Qwen anunció el 26-ago como
  «Qwen3.8-Flash-Next» son los **pesos abiertos** (HuggingFace, 125B, preview de la
  arquitectura Qwen4). El SKU servido por API se llama `qwen3.8-flash` a secas, y es el
  que se puede comparar en el plano común — correr los pesos abiertos sería `self_hosted`
  y no rankearía.

- **Cierre de sesión: las lecciones de estos días entran a `CLAUDE.md`, no a un
  post-mortem que nadie relee.** Cuatro reglas nuevas, todas pagadas esta semana: (1) *el
  instrumento tampoco se cree solo, se rompe a propósito* — cinco falsos verdes entre el
  19 y el 22-ago, **cuatro en la verificación y no en el código**; (2) *un chequeo que
  nace en verde puede ser bloqueante, uno que nace en rojo no*, y un `--duro` opcional en
  algo que `qa.py` declara bloqueante es un bloqueante de mentira; (3) *el dato existe y
  el consumidor no lo lee* — `fuera_del_indice` estaba en el JSON y dos módulos filtraban
  por prefijo; (4) *un canal que se pierde en el ruido no existe* — el CI, 40 días en rojo
  avisando por correo a una bandeja de 118.000 mensajes.
- **El estado en `CLAUDE.md` decía v4.0.0 de julio**, con «Tier 1 pendientes» que ya
  estaban medidos hace semanas. Actualizado a v4.9.0 y apuntando a las memorias, que es
  donde vive el porqué de cada pendiente.

- **El QA local y el CI daban veredictos distintos sobre el mismo commit.** El Action
  falló v4.9.0 con «se declaró un MINOR y lo tocado exige MAJOR (scoring_reference.json)»
  mientras en local pasaba en verde. La causa: `scoring_reference.json` declara **dos
  cosas** —qué calibración es (`score_method`, `computed_at`, los mean/std) y de qué
  release es (`version`)— y la segunda se bumpea en CADA release por precedente. En
  local el tag ya existía y el archivo caía del lado viejo del diff; en el CI no, y ahí
  sí lo veía. Mismo commit, dos respuestas, según dónde se corriera.

  Ahora `check_changelog` compara el CONTENIDO ignorando `version`: recalibrar sigue
  exigiendo MAJOR —que es lo único que la regla quería proteger— y ponerle la etiqueta
  del release, no. Verificado con sabotaje: cambiar `score_method` de v4 a v5 vuelve a
  exigir MAJOR.

## [v4.9.0] - 2026-08-22 — los 97 rankeados tienen tarea agéntica, y el CI vuelve a correr

- **«No debería faltar ninguno con tarea agéntica» — y tenía razón, con un argumento que
  ya estaba escrito en el repo.** Faltaban 5: los GPT medidos por `openai_direct`. El
  export exigía `provider == openrouter` para asociar el resultado de Harbor, y a esos
  modelos les aplicaba el criterio de un tercero. Pero la regla de first-party de
  `CLAUDE.md` dice justo lo contrario para la calidad: *«OpenRouter es un intermediario y
  la calidad es la misma… esto SOLO vale para first-party: en Groq/NIM/Ollama Cloud la
  calidad SÍ cambia por serving»*. Cuando OpenRouter enruta `openai/gpt-5.4`, la petición
  termina en OpenAI — misma casa, misma config.

  Ahora heredan sólo los proveedores que son la API del creador. Heredaron **7**: los 5
  GPT y los 2 MiMo de Xiaomi. **Ningún NIM, Groq ni Ollama Cloud**, que es la mitad que
  importa: esos sirven pesos de terceros con su propia cuantización, y ahí la diferencia
  está medida (Qwen 3.5 397B: 8,42 en NIM contra 7,97 en Ollama Cloud).

  **97 de 97 rankeados con tarea real ejecutada.**

- **El Action que regenera los artefactos llevaba 40 días en rojo, y nadie lo sabía.**
  Cristian reenvió el correo de GitHub del último fallo; al mirar el historial, **el
  último run verde fue el 13 de julio**, con 52 de los últimos 60 en rojo. Es el seguro
  del repo —regenera `models.json`, MODELOS.md, el sitemap y corre los guardrails cuando
  alguien no lo hace a mano— y estuvo mes y medio sin correr, mientras `CLAUDE.md` seguía
  diciendo que «el bot regenera los artefactos al hacer push».

  La causa técnica era trivial: `export_for_pages.py` importa `THINKING_MODELS` de
  `providers/adapters.py`, y ese módulo hace `from openai import OpenAI` en su cabecera —
  o sea que **leer una constante de configuración arrastra el SDK entero**, que el Action
  no instalaba. Se agregaron `openai httpx rich` y se verificaron **los 14 pasos en un
  venv limpio**, no solo el que fallaba.

  Lo que no era trivial es por qué nadie se enteró en 40 días: el aviso llega por correo,
  a una bandeja con 118.000 mensajes. **Un canal que se pierde en el ruido es un canal
  que no existe.** Por eso `check_ci.py` vive en el QA local, donde sí se mira.

  Deuda anotada: esas constantes deberían vivir en un módulo sin dependencias. Instalar
  el SDK para leer una tupla es tratar el síntoma.

- **Tercera vez que se publica un modelo sin correrle la tarea agéntica.** Cristian, el
  día del release de GLM 5.3: *"¿de nuevo no usaste harbor antes de publicar un
  modelo?"*. **De nuevo** es la palabra: pasó con 12 modelos, después con 5 GPT, y ahora
  con GLM 5.3 — arreglado a mano las tres veces, sin dejar nada que lo detectara.

  No rompe ninguna página, y por eso no se nota: el modelo entra al ranking, se ve
  completo, y lo único que ocurre es que **el eje agéntico y el wizard no pueden
  recomendarlo**, sin decir por qué. Ahora lo mira `check_agentico_publicado.py` en el
  QA. Al estrenarlo mostró **11 rankeados sin evidencia**, no uno: se corrieron los 6
  medibles (GLM 5.3, DeepSeek V4 Pro 0813, Gemini 3.7 Flash, Step 3.5 Flash, Kimi K2.5,
  Nemotron 3 Super) y quedan **92 de 97** cubiertos. Los 5 restantes son los GPT por
  `openai_direct`: no pueden heredar un resultado medido en OpenRouter —es otro
  endpoint— así que el chequeo los lista como deuda declarada, no como fallo.

- **Los snapshots nuevos de DeepSeek: uno sí, el otro no.** Comparados sobre los MISMOS
  tests, no sobre sus promedios. **Pro 0813 vs el anterior: +0,26** (IC95 [−0,018,
  +0,527]) — la mayor diferencia entre snapshots que hemos medido, y aun así el intervalo
  toca el cero por 0,018. **Flash 0731 vs el anterior: −0,04** (IC95 [−0,319, +0,233]):
  indistinguibles. Lo notable es que esas diferencias mueven **25 y 18 puestos** en la
  tabla sin ser significativas — la mejor ilustración de por qué esta población apretada
  engaña cuando se lee por posición. Se evaluó subirle muestra al Pro base para resolver
  el empate y Cristian lo descartó: es el snapshot viejo, y confirmar una diferencia
  contra algo que igual no se va a usar no cambia ninguna decisión.

- **GLM 5.3 entra al #2 con 8,52 — y el triple de precio SÍ compró calidad.** Se agregó
  el 21-ago porque es la versión nueva del GLM 5.2 que está #6 del leaderboard de
  OpenRouter, y porque su precio de lista llamaba la atención: **$1,40/$4,40 por millón
  contra $0,97/$3,04** de su antecesor. La pregunta era si eso se justificaba. Se
  justifica: **8,52 contra 8,36, y del puesto 20 al 2**. Empata en calidad con GPT-5.6
  Luna, que cuesta **$0,93 por 1.000 llamadas contra $7,02** — o sea que sigue habiendo
  una decisión de precio, pero ya no es «pagás más por lo mismo».

- **LFM2 24B A2B queda anotado sin medir, con su motivo.** Pedido por Cristian.
  Verificado el 21-ago: no está en el catálogo de OpenRouter (422 modelos) y llamarlo da
  404 — la página que aparece al buscarlo es una landing sin proveedor. Tampoco está en
  NIM, y ésas son las dos credenciales activas. Lo sirve Together AI. Va en `models.py`
  con `pendiente_proveedor` y no en una lista aparte, para que cuando alguien pregunte
  «¿lo tenemos?» la respuesta incluya qué falta para medirlo.

- **Auditoría del catálogo contra OpenRouter: del leaderboard no falta ninguno.** Los 20
  modelos del top-10 semanal y mensual están todos. El que parecía faltar —«DeepSeek V4
  Flash 0423»— es el alias base `deepseek/deepseek-v4-flash`, que ya estaba con otro
  nombre. Del catálogo general quedan 13 sin medir, todos de febrero a junio y ninguno
  con tracción: se listan en el reporte, no se miden. Los `Hy-MT2` de Tencent quedaron
  fuera por decisión de Cristian —no hay categoría de traducción— y el dato lo respalda:
  con contexto de 8K reprobarían las suites de contexto largo por formato, no por
  capacidad.

- **La tabla abría con 71 de 96 modelos, y los 25 que faltaban no eran malos.** El
  umbral de calidad venía en 8,0 por defecto y el peor modelo de todo el catálogo mide
  **7,26**: quedaban fuera por un default que nadie eligió. Cristian: *"deberíamos
  mostrar todos los modelos"*. Ahora el default es **`null` = el mínimo real de la
  población**, que resuelve `clampUmbralAlEje()` al cargar los datos — no se escribe un
  número, porque cualquier literal caduca con el próximo lote. Lo probó el propio
  guardrail: al poner 7,0 a mano, `check_calculator` C1 avisó que el primer tramo del
  slider no filtraba a nadie.

- **La ficha pasa a ser una columna; el desplegable, visible.** El enlace vivía bajo el
  nombre del modelo con **`opacity: 0`** —sólo aparecía al pasar el mouse, o sea que en
  móvil no existía— y el chevron era `.8em` en el color de un borde, DESPUÉS del número.
  Cristian: *"el ver la ficha debería ser más notorio y el desplegable también"*. El
  chevron va adelante, en cyan y con área propia; la ficha tiene su columna con botón.

- **`app.js` llegaba a los navegadores con la versión del 13 de agosto.** El HTML lo
  cargaba con `?v=20260813d`, un cache-bust escrito a mano: entre esa fecha y hoy el
  archivo cambió muchas veces —wizard, enlaces a fichas, W16, la columna nueva— y cada
  cambio llegó con el JS viejo a quien ya había entrado al sitio. Se descubrió porque la
  columna «Ficha» no aparecía en local. **`sync_cachebust.py`** lo calcula del hash del
  contenido: el archivo ya sabe cuándo cambió.

- **El sitio publicaba voseo, contra el estándar de español neutro.** *«¿Querés ir más a
  fondo?»* como encabezado de sección y *«movés los pesos vos»* en el bloque de
  metodología — 12 casos en 8 archivos, varios en generadores, o sea replicados en
  decenas de páginas. El estándar existe hace meses y nada lo verificaba.
  **`check_espanol_neutro.py`** revisa las 90 superficies publicables.

- **El bloque de metodología citaba «Los 82 rankeados caen entre 7,26 y 8,65»** — los
  tres números caducados, en la página más visitada y con forma de dato metodológico.
  Ahora salen de `models.json` en runtime.

## [v4.8.0] - 2026-08-21 — el examen se mide con una sola definición, y el ranking pasa a 96

- **DeepSeek V4 Pro (0813) y Kimi K2.5 completaron el examen.** El primero entra
  directo al **#13 de 96** con 8,41 — llevaba semanas fuera del ranking por 41 tests
  sueltos, no por su nota. Kimi K2.5 arrastraba **seis ciclos** de completar-el-examen
  que no completaban nada, por el resume que le mezclaba runs de la variante NIM.

- **A Nemotron 3 Super sí le faltaba algo, y a otros diez también.** Cristian: *"¿pero a
  Nemotron no le falta nada?"*. Rankea con el examen completo —`integridad_idioma` no
  cuenta para el índice— y **a la vez publica `integridad_idioma = 7,56` calculado sobre
  3 de 4 tests**. Al medirlo aparecieron **11 cifras publicadas sobre parte de su
  examen**, dos incómodas: Kimi K2.7 Code publica `dominio_entidad` **9,03 sobre 2 de 6**,
  y Qwen 3.5 35B publica seguridad **2,7 sobre 13 de 20** — la dimensión que alimenta el
  badge «resiste instrucciones ocultas» de las fichas. `completar_examen.py` ahora las
  reporta aparte: completar el ranking y completar una cifra publicada son dos trabajos
  distintos, y mostrarlos como uno solo fue lo que hizo medir de más.

- **«¿Cómo hacemos que no nos pase de nuevo?» → `suites.del_indice()`, y `S5` que la
  protege.** La causa raíz no era una regla mal escrita: `SUITES[s]["en_promedio"]` ya
  decía cuáles cuentan. Lo que faltaba era **una función a la que llamar**, así que cinco
  archivos se escribieron la suya con la misma heurística de prefijos —`("niah",
  "prompt_injection")`— que cubre 2 de las 6 suites fuera del índice. Ahora hay una sola
  definición, los 6 consumidores la usan, y **`S5` en `check_suites.py`** falla si alguien
  vuelve a escribir la tupla. Es la misma forma que ya tenía S2 para las etiquetas: el
  registro es uno y nadie mantiene una copia.

- **«Revisá que todos sean modelos que sí queremos re-medir»** — y tres de los cinco no
  hacía falta medirlos. `completar_examen.py` reportaba como bloqueados a Gemini 3.7
  Flash, Step 3.5 Flash y Nemotron 3 Super por tests de **`integridad_idioma`, una suite
  que no cuenta para el examen ni para el ranking**. Filtraba las suites omitibles por
  PREFIJO de nombre (`niah`, `prompt_injection`), y eso cubre 2 de las 6 que están fuera
  del índice — quedaban sueltas `integridad_idioma`, `dominio_entidad`, `extraer_claims`
  y `verificar_claims_lote`. El dato estaba ahí: cada entrada de `suites_incompletas`
  viene con `fuera_del_indice: true`. Es el patrón de siempre — **el dato existe y el
  consumidor no lo lee** — y la heurística de prefijos era una segunda fuente de verdad
  que se desincronizó de la primera.

- **Y el mismo bug estaba en el export, con las dos respuestas publicadas a la vez.**
  `export_for_pages.py` decía de Nemotron 3 Super `examen_completo: true` **y**
  `ranked: false`, sin ningún otro motivo: adentro del mismo archivo convivían dos
  definiciones del mismo concepto —una miraba las 29 suites del índice, la otra filtraba
  por prefijo—. Alineadas, el ranking pasa de 91 a **94**: entran Nemotron 3 Super,
  Gemini 3.7 Flash y Step 3.5 Flash.

- **`B3` en `validate.py`: examen completo ⟹ rankeado, o un motivo declarado.** Puede no
  rankear por endpoint muerto, variante de proveedor, `:free`, self-hosted o veto
  explícito — todos verificables. Lo que no puede es no haber ninguno. Estrenó marcando
  a los dos GPT-5.6 Pro y un Thinking porque leía sólo el JSON, y `effort_variant` /
  `no_medir` viven en `models.py`: el flag estaba bien puesto, faltaba mirarlo donde
  vive. Verificado saboteándolo.

- **`armar_resume` tenía el fix hecho y nadie lo invocaba.** Su firma era
  `model_name: str | None = None` con la advertencia «NO es opcional en la práctica»
  escrita al lado, y el único llamador lo omitía. El resume de `or-kimi-k2.5` seguía
  trayendo **1.328 runs de «Kimi K2.5 (NIM)»** —misma id, otro modelo—, el runner veía
  `fake_citation_trap` como «ya hecho» y lo salteaba: seis ciclos de completar el examen
  que no completaban nada. El parámetro ya es obligatorio en la firma.

- **Una key inexistente en `--modelos` salía por la puerta del éxito.** Con
  `kimi-k2.5` en vez de `or-kimi-k2.5`, el filtro no matcheaba nada y el script imprimía
  «✅ ningún modelo bloqueado» — el mensaje de «no hay trabajo pendiente». Tres modelos
  sin medir, reportados como si todo estuviera en orden. Ahora falla con exit 1 y sugiere
  la key correcta.

- **Los 5 GPT rankeados sin evidencia agéntica ya tienen tarea real ejecutada** (Harbor:
  86 → 91 modelos por tarea).

- **«¿Lo mismo no nos pasa en otras páginas?»** — Cristian, después del fix de agentes. Sí
  pasaba, en otra forma. Las páginas de variantes coronaban por columna: `Gana 4.20` sobre
  **[8,80 · 9,20 · 9,20 · 9,20]**, tres celdas idénticas y el texto nombrando a una;
  `Gana Terra` sobre dos 10,00. La causa era distinta —`spread` medía máximo menos mínimo
  de la fila entera, así que un rezagado abajo tapaba el empate de arriba— pero el efecto
  para el lector es exactamente el mismo: la tabla muestra números iguales y el texto
  corona a uno. Ahora el empate se mide **en la cima** y el resaltado va a todos los
  empatados, no solo al primero (que era el más barato, por el orden de columnas).

- **Lo que se auditó, y lo que no.** Los 7 rankings: veredicto y tabla coinciden
  (`mejor-llm-open-source` no corona a nadie a propósito — «cuando la medición no
  distingue, lo honesto es no recomendar»). Las 40 comparaciones X-vs-Y ya declaraban
  empate con la tolerancia correcta; solo se alineó el resaltado de celda, que marcaba
  ganador aunque la columna dijera «empate». Las variantes eran las rotas.

- **`check_ganadores.py`** unifica las dos formas bajo una regla: **no se corona a nadie
  por una diferencia que no publicamos.** G1 verifica que el veredicto nombre al #1 de su
  tabla; G2, que ninguna fila con «Gana X» tenga un empate visible en la cima. 23
  afirmaciones bajo vigilancia. Verificado saboteando los dos casos reales.

- **La primera auditoría que corrí dio un falso verde y era mía.** El extractor de cards
  no matcheaba el HTML y devolvía `None` en las 7 páginas, o sea «✅ ninguna discrepa»
  sobre cero datos leídos. Cuarto del día, y el más fácil de creerse porque el resultado
  era el que uno quiere ver.

- **`check_changelog.py` se hacía un bug a sí mismo, y era peligroso.** `_sh()` hace
  `.strip()` del stdout completo, y `git status --porcelain` arranca con un espacio
  (` M archivo`): ese strip **le comía el primer carácter a la primera línea**. El
  síntoma era ruido —`.coverage` llegaba como `coverage` y no matcheaba la lista de
  irrelevantes—, pero la consecuencia no lo es: los prefijos de `NIVEL_POR_PATH` se
  comparan con `startswith`, así que si el primer archivo listado hubiera sido
  `benchmarks/suites.py` se habría leído `enchmarks/suites.py` y **un cambio de medición
  habría pasado como PATCH**, que es lo único que ese chequeo existe para impedir.
  Además `.coverage` sale del control de versiones: lo reescribe el propio QA al correr
  pytest, así que el chequeo modificaba el archivo que después reportaba como pendiente.

## [v4.7.1] - 2026-08-19 — la ficha se lee, el wizard se ve, y la página de agentes deja de contradecirse

> Cada commit que toca código o datos agrega su línea acá, **en el momento**, no al
> cerrar la versión. Estándar: [VERSIONADO.md](VERSIONADO.md).

- **La página de agentes se contradecía a sí misma, y lo vio Cristian.** Publicaba
  *«DeepSeek V3.2 encabeza la tabla en calidad»* con DeepSeek V3.2 **#73, en 7,4**,
  contra 9,4 del primero: *"no entiendo, ¿por qué gana DeepSeek si no tiene el mejor
  puesto? Esto es lo que te decía, tiene que quedar claro para cualquiera"*. No es que
  no se entendiera — era falso.

  Causa: el 16-ago la **tabla** pasó a ordenarse por la tarea real ejecutada (Harbor +
  tool calling) porque el pilar «Agentes» mide escribir *sobre* agentes y **correlaciona
  −0,20 con el desempeño real**. El **veredicto** se quedó calculando por el pilar. Dos
  criterios en una misma página, con el texto afirmando que eran el mismo — y el
  veredicto recomendando por la métrica que va casi al revés de lo que la página
  promete. Ahora el veredicto usa el mismo score que ordena la tabla.

- **Y el empate se declara a la resolución de lo que publicamos.** Sonnet 4.6 (9,4040) y
  Gemma 4 31B (9,3560) caían en bandas distintas por **0,048** — una diferencia que la
  tabla ni puede mostrar: ahí salen «9.4» y «9.4». El texto habría dicho «nadie empata
  con él» encima de dos números idénticos a la vista. Con el margen ajustado al
  redondeo, el veredicto cambia y contesta la duda que lo destapó: **Sonnet 4.6 no le
  gana a los nuevos en agentes — empata con Gemma 4 31B, que cuesta $2/mes contra $70.**

- **«el más barato de los 1 que empatan con él».** Con `band_size = 1` el texto decía que
  el modelo empata consigo mismo, y por el otro camino «1 modelos empatan». Un modelo
  solo en su banda es el caso más limpio que hay y se contaba como el más raro.

- **`C5` en `check_cortes.py`: el veredicto no puede contradecir a su tabla.** C1 no lo
  cazaba porque mira la tabla contra los datos, y la tabla estaba bien: lo que mentía era
  el párrafo de arriba. **C5 se estrenó dando un falso verde** —recorría solo las páginas
  de `criterion == "suite"` y la de agentes es `pillar`, o sea que miraba donde el bug no
  podía estar— y lo detecté saboteando la página a propósito. Tercer falso verde del
  mismo patrón en el día: un guardrail sin su prueba de sabotaje es una promesa.

- **La puerta de entrada era más chica que lo que hay detrás.** Medido: el wizard vivía
  en `max-width: 640px` de los 1100 que da el `main` —el 58% del ancho— mientras la
  calculadora completa, que es el SEGUNDO nivel, usaba los 1052 px enteros con cards de
  preset grandes. Cristian: *"el tamaño donde tenemos Tus Criterios es el ideal, y el
  wizard está más pequeño"*. Ahora comparten ancho y escala: la pregunta pasa de 20 a
  25 px, las opciones de 14,5 a 16,5, el grid a `auto-fit` (4 columnas en desktop, como
  los presets) y el botón a 17 px. El flujo completo entra en una pantalla.

- **La recomendación del wizard no llevaba a ninguna parte.** Tres preguntas, un nombre
  — y el nombre era texto plano. La ficha existía y no había cómo llegar justo cuando el
  interés es máximo. `check_fichas_alcanzables.py` no lo caza porque audita HTML
  generado y esto lo pinta el JS: es el punto ciego de cualquier superficie dinámica.
  Por eso el chequeo va donde sí llega, **W16 en `qa_calculadora.mjs`** (31 chequeos),
  verificado saboteándolo.

- **86 de 91 rankeados ya tienen evidencia agéntica** (81 con las tres tareas), tras el
  lote de Harbor de 12 modelos × 3 tareas × 3 intentos. La columna «Tarea real
  ejecutada» deja de estar vacía para casi toda la tabla.

- **El sitio tenía 30 colores; el manual de marca tiene 10.** Cristian: *"a nivel de
  colores creo que cansa"*. La auditoría: **22 hex fuera del manual** — siete fondos
  oscuros casi idénticos y seis acentos compitiendo (dorado `#ffd700` ×17, naranja,
  morado claro, rojo). Nadie decidió tener 30: cada uno entró en una regla, resolviendo
  un caso puntual, y se quedó. El manual decía «NUNCA inventar colores», estaba escrito,
  y nada lo verificaba. Ahora quedan 13 (10 de marca + 3 grises de UI) y lo hace cumplir
  **`check_paleta.py`**, bloqueante en el QA.

  Tres desvíos que solo aparecen comparando contra la fuente: la card era `#14142a` y el
  manual dice `#1a1a2e`; la prosa era `#dcdcec` contra `#dbdbe5`; y el **morado se usaba
  aclarado a `#b478ff` como color de texto**, que el manual prohíbe explícitamente
  («púrpura acento glow/grid, nunca en texto principal») — que hubiera que aclararlo para
  que contrastara era la señal de que no correspondía. El guardrail estrenó cazando dos
  colores inventados **ese mismo día, por mí**, en el fix de las barras.

- **El h1 llevaba un degradado, que el manual prohíbe.** «Cero degradados decorativos en
  la tipografía»: el titular iba verde→cyan clipeado al texto y se lavaba justo donde
  cruza al cyan. Verde sólido, 14.8:1 AAA.

- **Los títulos nacían pegados al header: 0 px de aire, medido.** Una regla que quitaba
  la línea divisoria del hero se había llevado de paso su `padding-top` — el borde era lo
  que se quería quitar, no el respiro. Y el grid morado del hero se cortaba en línea
  recta porque la máscara se desvanecía sólo hacia arriba; ahora se apaga antes de los
  dos bordes.

- **El wizard estaba enterrado a 471 px**, debajo del titular, el párrafo, la caja del
  curso gratis, el acordeón y la tesis — en un laptop de 768 px quedaba al borde.
  Cristian: *"la gente no entiende lo del wizard"*. No era confuso: había que buscarlo.
  Sube a lo primero después del titular y ahora entra completo en la primera pantalla; el
  contexto baja detrás, para quien lo quiera.

- **La ficha no parecía una ficha, y era cierto.** Eran cuatro elementos sueltos flotando
  en el scroll —titular, KPIs, badges, barras— separados por aire y divisorias: un
  artículo que empieza con datos. Ahora viven dentro de UN marco con borde, las cajas
  internas pierden su propio borde (un borde dentro de otro es ruido) y la procedencia
  cierra abajo, como el pie de una tabla. Mismos datos, un objeto.

- **El #1 de cada ranking era el único que no parecía clickeable.** `enlace_ficha` lo
  envuelve como `<a><strong>…</strong></a>` y `.results-table strong` pintaba blanco por
  encima del cyan del enlace. Justo el modelo que más gente quiere abrir.

- **La ficha abría con el número que hace cerrar la pestaña.** El tile más grande y
  primero era «Puesto global #59 de 91 · mejor que el 36% de los rankeados». Ese mismo
  modelo saca 8,21/10 y es #3 de 91 en Contenido: el puesto global comprime en 91
  posiciones una población que entera cabe en 1,3 puntos — la misma trampa que hizo
  abandonar el z-score en v4.1, servida en el lugar más visible. Ahora abre la **nota de
  calidad**, con el puesto de subtítulo y el rango real al lado, que es el dato que
  desarma la mala lectura. El rango se mide, no se escribe.

- **Un tile nuevo: cuánto sale al mes.** «$39,00 por 1.000 llamadas» no es una unidad en
  la que un founder piense; «$58,50 al mes con 50 llamadas por día» sí. El supuesto va
  escrito dentro del tile — una estimación sin su supuesto a la vista es un número
  inventado — y vive en una constante porque aparece en las 91 fichas. También se cambió
  «más barato que 7 de 91», que es la forma cortés de decir «el 8º más caro» y obliga a
  hacer la resta.

- **El color de las barras decía «reprobado» de un 8,71 sobre 10.** Se pintaba magenta
  por quedar 0,35 bajo la MEDIANA de un grupo que entero cabe en 1,3 puntos. Ahora el
  verde marca lo que sobresale y el resto es neutro, y la leyenda arranca diciendo que la
  nota de la derecha es sobre 10 en vez de pedir que se entienda la escala primero.

- **Los badges dicen la capacidad, no su nombre técnico.** «Tool calling» → «Puede usar
  herramientas»; «1000K de contexto» → «Le caben ~1.700 páginas a la vez»; «Prompt
  injection 8.7/10» → «Resiste bien instrucciones ocultas · 8.7/10». El término técnico
  queda entre paréntesis donde hace falta: el que lo busca lo encuentra y el que no,
  igual entiende qué está comprando.

- **El orden de la ficha sigue la decisión, no la disponibilidad del dato.** «Qué hace
  bien y qué no» —la única sección escrita en el idioma del lector, la que dice *«Decide:
  emitir JSON válido a la primera»*— venía después de tres bloques de números. Sube
  detrás del panorama por pilar, y las alternativas justo después: quien decide que no le
  sirve tiene su salida ahí mismo, no a mitad de scroll.

- **Las 61 páginas que publican modelos ahora dejan llegar a su ficha, y hay quien lo
  verifica.** Cristian: *"desde acá deberíamos ser capaces de llegar al card del modelo"*.
  Se resolvió con UN helper compartido (`enlace_ficha` en `generate_comparison.py`), que
  además omite el enlace si el modelo no tiene ficha — así el arreglo no siembra 404s. Van
  197 enlaces en 16 rankings, 172 en 40 comparaciones y las 5 páginas que faltaban
  (`alternativas-*` y `grok-4-1-vs-4-5`, hasta 20 modelos listados cada una) las encontró
  el guardrail nuevo `check_fichas_alcanzables.py`, no yo. Es bloqueante en `qa.py` y en el
  pipeline desde el primer día, y se puede porque nació en verde.

- **`check_cortes.py` llevaba una corrida entera CIEGO y no se puso rojo: se puso mudo.**
  Envolver el nombre del modelo en `<a class="a-ficha">` rompió el regex que leía el #1 de
  cada tabla —copiado en dos lugares—, así que `m1` daba `None`, el `if` no entraba y las
  8 páginas se saltaban sin decir nada. Ahora el patrón vive en una constante y **C1 exige
  encontrar la fila**: si el HTML cambia de forma otra vez, es un fallo, no un silencio.
  Es el modo de fallo propio de un guardrail que parsea HTML generado — el HTML cambia por
  una razón buena y el control deja de mirar.

- **Un test de guardrail daba verde por ver a argparse rechazar un flag muerto.**
  `_t_truncamiento` invocaba `--todos`, renombrado a `--solo-rankeados` el día anterior:
  argparse salía con 2, el test leía «≠ 0 → cazó el caso» y pasaba **sin correr el
  detector**. `_correr` ahora trata el exit 2 de argparse como fallo del test. El archivo
  que existe para que ningún guardrail sea una promesa era, él mismo, una promesa.

- **Un `--duro` opcional habría hecho de `check_fichas_alcanzables` un bloqueante falso.**
  `qa.py` lo declara bloqueante y lo invoca sin el flag: habría devuelto 0 para siempre.
  Se le quitó la palanca — falla y punto.

- **El veredicto destacado de tres páginas recomendaba un modelo que corre en el Spark.**
  DiffusionGemma 26B-A4B aparecía como «La mejor calidad medida · ≈$2/mes» en
  `/mejor-llm-para-agentes/`, `/mejor-llm-para-n8n/` y `/mejor-llm-para-razonamiento/`, y
  el texto afirmaba que «encabeza la tabla» estando fuera de ella. Nadie que lea esas
  páginas puede usarlo y esos $2 son electricidad ajena. El dato lo decía —
  `elegible.catalogo = False`— y `_verdict_data` filtraba sólo por cantidad de runs. Ahora
  usa `elegibilidad.filtrar`, que es LA función. Lo encontró Cristian mirando el sitio.

- **El wizard ya continúa hacia su ranking en 7 de 8 tareas.** El campo `page` existía en
  `WIZ.tasks` y cuatro tareas lo tenían en `null` con las páginas ya publicadas: verificar
  → `/mejor-llm-para-datos-exactos/`, noticias → `/mejor-llm-en-espanol/`, chat →
  `/mejor-llm-barato/`. «Un poco de todo» sigue sin enlace, que es correcto. Lo vigila W15.

- **La fila desplegable ahora se anuncia.** Cristian: *"me gustó lo de tener la row
  desplegable, pero no se entiende que hay una hasta que le haces click"*. Un affordance
  que sólo se descubre por accidente no existe para la mayoría — el mismo problema que el
  wizard invisible. Va un chevron junto al número que gira al abrir, y la fila reacciona
  al pasar por encima.
- **Desde la tabla se llega a la ficha del modelo** (`ficha ↗`), con `stopPropagation`
  para que no despliegue la fila a la vez: son dos acciones y las elige el usuario. Sólo
  aparece en los RANKEADOS, que son los únicos con ficha generada — enlazar sin
  condicionar mandaría a un 404 desde la pantalla más visitada. Lo vigila W14.

- **El wizard recomendaba para «producción» un modelo que falla la tarea entera.** `piso`
  es el peor de los k intentos (el `pass^k` de τ-bench): 0,00 significa que al menos una
  vez el modelo no hizo el trabajo. `scoreAgentico` ya lo ponderaba, pero ese camino sólo
  corre si el usuario elige TIPO de agente; sin tipo, `wizDecidir` cae a `computeZScore`
  con los pesos del presupuesto y el piso desaparece. Resultado: en el preset más
  exigente en fiabilidad salía Llama 4 Scout (piso 0,00) por delante de tres con piso
  0,44 / 0,89 / 1,00 — y ni por precio, porque Qwen 3.7 Flash cuesta menos y tiene 0,89.
  El criterio sube al filtro de candidatos, donde ninguna ponderación puede diluirlo:
  saca 13 de 84 y deja 71. Con su prueba, W13.

## [v4.7.0] - 2026-08-19 — Cuatro modelos frontier estaban al fondo por un techo nuestro

Esta versión no agrega un eje: **arregla la medición**. Y el titular es cuánto se movió
el ranking al arreglarla:

    Gemini 3.6 Flash    +57 puestos
    Claude Opus 5 Fast  +44
    Claude Opus 5       +37     (estaba #79 de 83)
    Claude Sonnet 5     +26

Ninguno había cambiado: cambió el presupuesto de salida que les dábamos.

**91 modelos rankeados** (antes 83) · 205 catalogados · cero truncamiento en los 167 con
muestra suficiente.


> Cada commit que toca código o datos agrega su línea acá, **en el momento**, no al
> cerrar la versión. El release convierte esta sección en `[vX.Y.Z] - fecha`.
> Estándar y por qué: [VERSIONADO.md](VERSIONADO.md). Lo verifica `check_changelog.py`.

- **A1 del validador acusaba una regresión que no existía**, y bloqueaba el export desde
  el lunes. Decidía si un run era «nuevo» comparando el NOMBRE DEL ARCHIVO contra
  `benchmark_20260716`: como texto, `"benchmark_remedir_…" > "benchmark_20260716"` (la `r`
  va después del `2`), así que 36 runs de ABRIL consolidados por `armar_resume` en
  archivos sin fecha pasaban por nuevos. Ahora se mira la fecha del run, que está en el
  run. `validate.py` quedó en verde: el benchmark se puede publicar.
- Las **14 variantes `-thinking`** quedan declaradas `effort_variant` + `no_medir`, y
  **GPT-4o y Claude Sonnet 4** como `no_medir` por antigüedad. Estaban fuera del ranking
  por casualidad, no por decisión — y cualquier barrido los habría levantado, como pasó
  con los GPT-5.6 Pro y Qwen 2.5 72B. Los quince modelos viejos que SÍ medimos (Llama 4,
  DeepSeek V3, Kimi K2, Gemini 2.5…) se quedan: son opciones vigentes con examen completo,
  y la regla es no EMPEZAR uno viejo, no jubilar los que ya están.
- Re-medición del lote de agosto con el presupuesto por tarea: los modelos que antes se
  cortaban en 2.048 ahora generan hasta 32.768 tokens, y el truncamiento de los runs
  nuevos bajó a 2-5% (dentro de lo normal: un test largo puede tocar el techo en
  cualquier modelo). Los 1.096 runs cortados con el techo viejo quedan en
  `_archive-truncados-20260818/` con su original al lado — son evidencia de que pasó, no
  se borran.
- **El presupuesto de salida pasa a ser por TAREA**, calibrado contra la demanda real:
  2.748 runs de la ruta sin nuestro techo dan p95 8.313 y p99 18.735, y lo que supera 16k
  se concentra en `agent_long_horizon` (19%, p95 29.927) mientras 26 de 31 suites no
  llegan ni a 16k. `agent_long_horizon` 65.536 · cuatro suites medias 32.768 · resto
  24.576. No rompe el `max_tokens` uniforme de LiveBench: ese principio pide el mismo
  límite para todos los MODELOS, no para todas las tareas.
- El multiplicador ×4 sólo aplica ya a los call sites que no pasan la suite: encima del
  presupuesto nuevo daba 131.072 tokens, que varios proveedores rechazan con 400.
- El canario escribe recibo **también cuando falla**. Un rojo dejaba en su lugar el verde
  anterior, y por eso un lote arrancó pese a un «NO lanzar»: el script leyó un recibo de
  12 horas antes, de otro modelo. Ahora además se exige frescura, no sólo `ok`.
- `VERSIONADO.md` + `check_changelog.py`: el estándar de versionado y CHANGELOG, con el
  instrumento que lo hace cumplir. Nace de una sesión con once commits cuyo CHANGELOG se
  escribió al final y de memoria — y del `git reset --hard` del mismo día, que probó que
  perder el relato no es hipotético. El nivel de versión deja de ser criterio y pasa a
  decidirlo **qué archivo se tocó**: `scoring_reference.json` es MAJOR, las suites y los
  criterios de ranking son MINOR, datos y arreglos son PATCH.
- Decisión al índice: se mide el **modo por defecto** de cada modelo, nunca un esfuerzo
  forzado — y cuál es ese default (medium o high) se determina **midiendo**, no leyendo la
  documentación del proveedor. Hoy 178 modelos declaran «default del proveedor» sin que
  sepamos qué significa: **cero runs registran `reasoning_tokens`**, así que el dato que
  lo decidiría no se está capturando. Queda como pendiente con método, no como duda.
- **Once de trece modelos nuevos estaban midiendo con el techo pegado en 2.048** —Seed
  2.1 Turbo cortó el 73% de su examen— porque razonan por default y no estaban en
  `THINKING_MODELS`. La conclusión que casi se publica, «la generación Qwen 3.8 rinde
  peor que la 3.7», era falsa: 3.6 Max y 3.7 Flash, de la misma familia y sí declarados,
  cortan 0%. Seis patrones nuevos y re-medición pendiente.
- El detector de truncamiento **estaba al revés**: miraba sólo los modelos ya rankeados,
  o sea que era ciego justo donde más importa —un modelo nuevo publica su nota por
  primera vez y no hay histórico con qué contrastarla—. Ahora mira todos por defecto.
- Y sube al **canario**, que es donde se evita pagar: si más de la mitad de las
  respuestas del pre-vuelo salen cortadas, el lote no arranca. La técnica ya existía
  —el 12-ago se probaron 9 modelos con `max_tokens=300` y cinco salieron en blanco— pero
  había quedado como anécdota en un comentario, no como paso obligatorio.
- El timeout del canario sube a 75 min y **juzga con lo que alcanzó a medir** si expira:
  al declarar thinking a media docena de familias sus respuestas pasaron de 2.048 a 8.192
  tokens y el canario empezó a morir sin veredicto. Un gate que expira enseña a saltarlo
  con `--sin-canario`, y ahí se pierden los cinco invariantes, no sólo éste.
- LongCat 2.0 queda con el examen interrumpido en 24/143, por decisión: mide **2,5 min
  por test**, cinco veces más lento que Sakana Namazu en el mismo examen y arrancando a
  la misma hora. Con el criterio de examen completo no rankea, y su lentitud es en sí el
  dato que lo descarta para uso en línea.
- El runner **rechaza** los modelos marcados `no_medir` / `effort_variant`, incluso
  pedidos explícitamente por `--models`. Esos flags los miraba la capa que PUBLICA
  (`export_for_pages`, `completar_examen`) y no la que GASTA, así que una decisión de
  catálogo se hacía cumplir *después* de haber pagado el examen. En una mañana entraron
  los dos GPT-5.6 Pro y Qwen 2.5 72B, que llevaba el flag puesto y aun así corrió 76
  tests. Escape declarado: `--incluir-no-medir`, que deja rastro en el comando.
- `check_presupuesto.py`: verifica que haya con qué pagar ANTES de lanzar un lote. Nace
  de la noche del 17-ago, cuando la API key llegó a su tope a las 20:57 y se llevó el
  juez —que puntúa todo—: Opus 5 murió a mitad del examen y dos chunks ni arrancaron. El
  canario ya verificaba que los modelos respondan; nadie verificaba que hubiera con qué
  pagarles. Distingue el tope de la KEY del saldo de la cuenta, que es lo que confundió
  la recarga del día siguiente.
- `qa.py` gana tres chequeos que estaban enganchados al pipeline pero **no al comando de
  QA**, que es donde alguien los busca: credenciales, truncamiento y CHANGELOG. Era el
  mismo patrón que persigue `check_cobertura` — la regla aplicada donde uno se acordó.

## [v4.6.0] - 2026-08-17 — El día que el benchmark se equivocó, y qué se cambió para que se note

Esta versión no agrega un eje: **arregla tres formas distintas de publicar un número que
no se sostiene**, y las tres las destapó Cristian preguntando, no un guardrail. Eso es lo
que se corrigió además del número.

### Opus 5 estaba #79 de 83 por un `max_tokens` nuestro

*"Me llama mucho la atención lo de Opus 5."* Razona por default vía API y no estaba
declarado en `THINKING_MODELS`, así que corría con el techo de 2.048 y **el 31% de su
examen terminaba en `finish_reason="length"`** — cortado a mitad de frase, puntuado igual.
Su p90 de salida era exactamente 2.048; por la ruta de suscripción, que no pasa por el
adapter, es 10.231.

| modelo | examen cortado | brecha de calidad |
|---|---|---|
| Claude Opus 5 Fast | 33% de 167 runs | — |
| Claude Opus 5 | 31% de 173 | 7,68 → 8,49 por la otra ruta |
| Gemini 3.6 Flash | 30% de 174 | — |
| Claude Sonnet 5 | 15% de 222 | 8,04 → 8,86 |

Sobre una población que entera abarca 1,4 puntos. Los cuatro entran a `THINKING_MODELS` y
se re-midieron.

**Por qué ningún detector lo vio** — la pregunta que hizo Cristian: *"eso lo debió detectar
el QA, ¿no?"*. Porque los seis detectores cazan **ausencia** (vacíos, sin procedencia, rutas
muertas, precio $0) y un run truncado no carece de nada: tiene contenido, forma válida,
`success=True` y pasa `validate.py`. Lo que hay es un techo de más. Nuevo
`check_truncamiento.py`, umbral 12% — donde se parte la población, no un número redondo.

### El ranking ya no se decide por cantidad de runs, sino por el examen entero

*"No seguiría poniendo el filtro de 50 runs. Todos deben de tener todos y punto, si no no
son comparables."* El umbral era un proxy y fallaba en las dos direcciones: dos modelos con
50 runs pueden haber rendido tests **distintos**. Hoy manda rendir las 29 suites que puntúan
con todos sus tests — 143 en total, así que quien lo complete tiene ≥143 runs y el viejo
umbral queda subsumido.

Y el examen incompleto ahora saca también del **catálogo**, no solo del ranking: *"solo los
medidos completos aparecen en el benchmark / calculadora"*. «En evaluación» sonaba prudente
y publicaba lo mismo con una etiqueta.

Simulado antes de aplicarlo, como manda PLAN-ESTABILIDAD R1: **83 → 79 rankeados**. La
simulación cazó dos bugs propios antes de publicar — leer «no tiene suites incompletas»
metía 29 modelos con **cero runs** al ranking, y comparar por cantidad sacaba a GPT-5.6 Luna
y MiniMax M3, que habían rendido las **dos** versiones de una suite editada.

Las variantes `-sub` (Claude por suscripción) salen del catálogo público: mismo modelo con
dos filas y números distintos, y el que le aplica al lector es siempre el de la API.

### Cuánto `max_tokens` necesita cada modelo, por tarea

El repo tenía `output_tokens` en cada run desde siempre y no lo publicaba. Ahora está en
cada ficha, **por tarea**, porque quedarse corto **no falla ruidoso: entrega de menos** y
quien consume lo lee como «nada que reportar».

El caso que lo motivó es el gate de noticias de Eco, que este benchmark recomendó cambiar y
falló en producción en dos horas. Nueva suite **`verificar_claims_lote`** (1, 3, 5, 8, 12 y
15 claims sobre el mismo material, con el prompt real de 4.218 caracteres) y scorer
`list_completeness`: la nota es *ítems correctos / ítems **enviados***, así que devolver 2
de 11 perfectos da 1,8 y no 10. Medido:

| | calidad 1→15 claims | tokens con 12 claims | costo /1.000 llamadas |
|---|---|---|---|
| Gemini 2.5 Flash | 10 · 10 · 10 · 8,8 · 9,2 · 9,3 | 869 | $2,637 |
| DeepSeek V4 Flash | 10 · 10 · 10 · 8,8 · 9,2 · 9,3 | **2.492** | **$0,492** |

Curvas idénticas: **el modelo no era el problema**. El nodo tenía `max_tokens: 2000` y la
tarea pide 3.115 con ese modelo. Y el ahorro sobrevive al mayor consumo — 5,37× más barato
aun gastando 2-3× más tokens.

### QA: nueve guardrails no los corría nadie

Cristian: *"revisa bien que no nos falte revisar algo más para los QA, siempre aparece algo
nuevo"*. Cruzados los 24 chequeos contra quién los ejecuta, aparecieron nueve huérfanos.
Cuatro son análisis exploratorios y está bien que se corran a mano; los otros cinco ya
corren en el pipeline y en CI — entre ellos **`test_unitarios`, las 123 pruebas del núcleo,
que existían y el CI no ejecutaba**, y `check_blog_consistency`, nacido de ocho posts con
claims muertos en producción y sin correr desde julio.

Nuevo **`check_secretos.py`**, después de que la Secret Key real de R2 resultara ser el
**fixture** de `string_precision` y se replicara sola a PROMPTS.md, TESTS.md y ~600 archivos
de `results/` — porque cada run guarda su prompt, y el repo es público. Dice también qué no
cubre: 6 de las 8 API keys del `.env` están vacías (viven en Infisical), así que la capa sin
falsos positivos **tampoco habría cazado el caso que la motivó**. Contra eso el único control
real es que los fixtures se **generen**, nunca se copien de un `.env`.

Los dos guardrails nuevos van con su prueba en `test_guardrails` (18/18) y hay un W12 nuevo
en el QA de la calculadora para las tareas que se juzgan por suites y no por pilar.

### Estado de los datos

**El código y los criterios de esta versión están completos; los números todavía no.** Hay
un lote midiendo la re-medición de los cuatro truncados, doce modelos nuevos del catálogo
(Gemini 3.7 Flash, Grok 4.6, DeepSeek V4 Pro 0813, Qwen 3.8 Max y 2.4T, KAT Coder Air/Pro,
LongCat 2.0, Gemini 3.5 Flash Lite, Sakana Namazu, Seed 2.1 Turbo y 2.0 Code) y el backfill
de seguridad e idioma. Los artefactos publicados se regeneran al cerrar ese lote: `validate.py`
bloquea hasta entonces, y con razón — hay `dominio_entidad` parcial en tres modelos y 12 runs
sin sello de fórmula que hay que resolver antes de publicar.

## [v4.5.0] - 2026-08-17 — Verificar un dato entra al índice, y las páginas dejan de adivinarse

### El eje nuevo: verificar un claim contra su fuente

Un eje que ningún benchmark general mide y que decide cualquier flujo que publique sin
humano revisando: **¿la fuente respalda lo que dice el titular?** Se mide en las **dos
direcciones**, que es lo que casi nadie hace — dejar pasar lo inventado publica un dato
falso con fuente citada; bloquear lo que sí estaba tira trabajo ya pagado. Medir una sola
premia al que bloquea todo.

**83 modelos rankeados, rango 6,30 – 8,65, σ 0,37, cero notas perfectas.** Lidera Claude
Opus 4.8 (8,29); entre los baratos, Qwen 3-Next 80B (8,65) y Nemotron 3.5 Lightning (8,59).

Entra al promedio del pilar Contenido y **mueve 77 de 83 modelos de puesto**: GPT-5.4 sube
31, Hermes 4 405B sube 29, Qwen 3.5 35B baja 21. En el ranking global el movimiento es
menor (máximo 10 puestos) porque Contenido es un pilar entre varios. Eso es la suite
haciendo lo que se le pidió: separar al que **escribe** bien del que **verifica** bien, que
hasta hoy eran indistinguibles.

**Nació saturada y no se publicó así.** La v1 tenía seis casos y **cinco daban nota
perfecta en todos los modelos** — 95% de runs perfectos. Yo la había probado en UNO, que es
exactamente el error que la Regla 0.7 del runbook describe. `validate_suite.py` la rechazó
con ocho modelos repartidos por el rango. Las trampas viejas eran de tipografía («42»
contra «4,2»); las nuevas son la distancia entre lo que una fuente **afirma** y lo que un
lector **infiere**: la cuenta que da pero nadie hizo, el plan que no es hecho, la
atribución que no es afirmación.

### El `--aplicar` que no leía su propio reporte

`simular_pilares.py --aplicar` marcó **tres** suites como parte del promedio mientras el
reporte que acababa de imprimir decía que dos tenían **10% de cobertura** y habían fallado
la validación por saturación (una con **100% de runs perfectos y dispersión 0,00**).

Hoy no entraban al score —el export excluye lo que está bajo 80% de cobertura— pero
habrían entrado **solas el día que subiera la cobertura**, sin que nadie lo decidiera. El
gate ahora usa los umbrales de `validate_suite.py` y se niega, nombrando el motivo. Y las
dos notas del registro dicen ahora que están fuera **por saturación, no por cobertura**:
la distinción cambia qué hay que hacer para arreglarlas.

Mismo patrón de siempre: la regla estaba escrita, la imprimía en pantalla, y el código de
abajo no la leía.

### Las páginas declaran lo que publican

Cristian, después del cuarto arreglo seguido en el auditor: *"solucionemos de manera
definitiva lo de las páginas"*.

Los cuatro arreglos anteriores eran **el mismo arreglo**. El auditor infería la estructura
del HTML con expresiones regulares y las 71 páginas tienen **ocho formas distintas**: cada
regex cubría unas y dejaba otras ciegas. P2 mezclaba las filas de dos tablas y declaraba
desordenada una página ordenada; P3 no miraba 10 páginas sin columna de puesto; P4 contaba
«cero filas» en páginas con 48.

Ahora cada página **emite un contrato JSON** con lo que promete —tipo, generador, qué
recomienda, qué ordena, cuántas tablas— y el auditor lo lee. **71 de 71 lo declaran**, y
R7 impide publicar una sin él: un formato nuevo ya no puede entrar en silencio.

Es la tercera vez que este repo resuelve un problema así con el mismo movimiento (el
registro de suites, `m["elegible"]`, y ahora esto): **cuando el dato viaja declarado, nadie
tiene que reconstruirlo.**

### Groq apagó dos endpoints, y el guardrail frenó la publicación

Groq deprecó `llama-3.3-70b-versatile` y `llama-3.1-8b-instant` el 16-ago. Se marcan
retirados, con la aclaración de que **el modelo Llama 3.3 70B sigue vivo en OpenRouter**:
lo que murió es la ruta.

El registro decía antes *«falta GROQ_API_KEY, NO es retired»*, y esa distinción era
correcta y sigue importando — una credencial ausente no es un modelo muerto. Lo que cambió
es que ahora hay evidencia externa.

Al regenerar, el pipeline **bloqueó la publicación**: `/modelos-n8n/` recomendaba el
endpoint recién apagado. Se reemplazó por Qwen 3.7 Flash (tool calling 8,18, el más alto
del corte barato) y Llama 4 Scout 17B para quien prioriza latencia, diciendo lo que se
perdió: **ningún modelo del ranking iguala los 1,3 s de la LPU de Groq** por otra ruta.

Y un dato que el anuncio de Groq no menciona: los reemplazos que recomienda son GPT-OSS, y
**GPT-OSS marca 6,4-6,5 en tool calling contra 8,0 del que reemplaza** — el mismo número
por las dos rutas, así que es el modelo y no el serving. Si el agente solo redacta es buen
cambio; si llama herramientas, es un retroceso.

### Además

- **151 runs de Claude Sonnet 4.6 recuperados**: renombrar el modelo los había dejado
  huérfanos (el export agrupa por `(model_id, name)`) y el modelo figuraba con 0 runs, con
  4 páginas de comparación mostrando un lado vacío. El guardrail nuevo encontró de
  inmediato otro caso preexistente: **Gemma 4 31B con 77 huérfanos** — declarado, pendiente
  de decidir.
- **`/mejor-llm-barato/` ordenaba por una columna que no mostraba.** Era la única página
  que no había pasado por el arreglo de los rankings por pilar. De paso, P2 asumía que
  «mayor es mejor» y marcaba como desordenada una página perfectamente ordenada de menor a
  mayor precio.
- **`check_cobertura.py`**, siete reglas transversales que preguntan lo que ningún
  guardrail preguntaba: *¿esto que hicimos acá, debería estar también allá?* Nació de
  encontrar la segunda tabla en 2 de 16 páginas y W6 verificando 2 de 8 promesas del
  wizard. Encontró, dentro de un guardrail, que el regex de markdown de
  `check_consistency` no tenía el `(?:de\s+)?` que sí tenía el de HTML.

## [v4.4.2] - 2026-08-16 — El QA es uno solo, y la herramienta que desbloqueaba modelos no podía funcionar

### La fuente única de elegibilidad

Cristian: *"tenemos solo una fuente de la verdad, la idea es que todos usen la misma. No
puede recomendar algo que no cumpla lo que estamos haciendo."*

Medido: **76 condicionales de filtrado en 25 archivos** decidiendo a mano si un modelo se
puede recomendar. Y se puede fechar por qué se multiplicaron — cada regla nació de un
fallo distinto y se aplicó **donde dolía ese día**: `score_by_pillar` (25-abr, la
calculadora original), `retired` y `provider_variant` (13-jul, el día que se vio que
Devstral Small llevaba meses **#5 con el endpoint apagado**), `sirve_para_agentes` (14-ago,
por Hermes 4). Lo escrito antes no las tenía; lo escrito después las copiaba del vecino.

`elegibilidad.py` decide **una vez**, en el export, y graba el veredicto en `m["elegible"]`
con tres contextos (`catalogo`, `ranking`, `agentico`) y su motivo legible. Nadie
recalcula. Reproduce exacto el `ranked` anterior: cero drift.

### Un comando de QA, seis áreas, y hook pre-push

`qa.py` corre **11 chequeos bloqueantes en 3 segundos**, agrupados en datos · suites ·
calculadora · páginas · guardrails · versión. `instalar_hooks.py` lo engancha a `pre-push`.
Doctrina completa en [QA.md](QA.md).

**Cobertura del núcleo: 4% → 71%**, con 121 tests unitarios. `scoring.py` de 13% a 79%.

### Lo agéntico se ordena por lo que se LOGRÓ

Corrección de v4.4, medida contra el reward de las tareas Harbor (verdad objetiva,
verificada por pytest):

| qué ordena | correlación con resolver la tarea |
|---|---|
| pilar Agentes (v4.3) | −0,144 |
| pilar Agentes con las dos suites nuevas (v4.4) | **−0,204** |
| `tool_calling` solo | **+0,579** |

Las nueve suites del pilar miden **prosa sobre agentes**, no ejecución. Ahora las tres
superficies ordenan por media y piso de las tareas Harbor. `/modelos-n8n/` dejó de
recomendar **Hermes 4 405B** para poner en un n8n, y la calculadora dejó de ponerlo #3.

### La herramienta para desbloquear modelos no podía funcionar

Al ir a completar 11 tests, `completar_examen --correr` imprimió **«✅ exámenes
completados» sin correr un solo test**, dos veces. Dos bugs encadenados, los dos en
silencio:

1. **El resume consolidaba runs FALLIDOS.** `--resume` saltea por `(modelo, suite, test)`
   sin mirar si el run sirvió; el export solo cuenta `success=True`. Un test que falló las
   cuatro veces quedaba *incompleto para el export y completo para el resume*: se saltaba
   para siempre. GPT-5.5 tenía `social_engineering_attempt` con 4 corridas, las 4
   fallidas — justo el test que faltaba.
2. **El output caía donde el pipeline no mira.** El runner hace `results_file =
   resume_path`, y el resume vivía en `_resume_tmp/resume_*.json`. `load_all_results()`
   solo lee `benchmark_*.json` de `results/`. Aunque los tests hubieran corrido perfecto,
   el resultado se tiraba.

El primero impedía correr; el segundo tiraba lo corrido. Por eso esos modelos llevaban
días bloqueados. Ahora el resume consolida **solo runs exitosos**, el archivo va a
`results/benchmark_completar_*.json`, y el script **verifica** que hayan quedado
desbloqueados antes de reportar éxito — si no, sale con error y dice dónde mirar.

### El detector tampoco conocía las reglas de qué medir

De los 7 modelos que proponía desbloquear, **4 no correspondían**: dos variantes PRO (no
rankean por política, completarles el examen no cambia nada) y dos de más de un año
(Qwen 2.5 de sep-2024 pedía 18 tests, la mitad del gasto). Causa mecánica: `no_medir`
vivía solo en `models.py` y **no se exportaba**, así que ninguna herramienta que lee el
JSON podía verlo.

---

## [v4.4.1] - 2026-08-16 — Lo agéntico se ordena por lo que se LOGRÓ, y las 71 páginas pasan por un auditor

Cristian, tras encontrar tres fallos distintos mirando páginas sueltas: *"haz el análisis
de todas las páginas por favor, seguimos encontrando errores como estos que impiden que
sean páginas útiles."* Tenía razón en el diagnóstico: no eran casualidades de una página,
eran **clases**.

### La corrección que abre todo esto

v4.4 metió `agent_long_horizon` y `tool_calling_adversarial` al pilar Agentes y se
presentó como una mejora. Medido contra la única verdad objetiva que tenemos —el reward
de las tareas Harbor, verificado por pytest sobre artefactos, no por un juez— **fue al
revés**:

| qué ordena | correlación con resolver la tarea |
|---|---|
| pilar Agentes antes (v4.3) | −0,144 |
| pilar Agentes con las dos suites (v4.4) | **−0,204** |
| compuesto 65% pilar + 35% tool calling | +0,444 |
| `tool_calling` solo | +0,579 |

El pilar tiene nueve suites llamadas «Agentes» y **ninguna mide ejecutar con
herramientas**: `agent_long_horizon` mide sostener el hilo *sin* herramientas y
`tool_calling_adversarial` mide *abstenerse*. Revertir tampoco arreglaba: −0,144 también
es negativa. El problema era el pilar entero.

**Ahora lo agéntico se ordena por lo que el modelo LOGRÓ**: media y piso de las tareas
Harbor (60%) con `tool_calling` de desempate (40%), porque la tarea satura. Mismo criterio
en las tres superficies —calculadora, `/mejor-llm-para-agentes/` y `/modelos-n8n/`— y los
modelos que no corren dentro de un agente quedan fuera del listado, no listados con un
badge.

Efecto: `/modelos-n8n/` dejó de tener a **Hermes 4 405B** entre los diez que recomienda
para poner en un n8n; su tarea real es 0,00 porque no existe endpoint que le dé
herramientas. Y la calculadora dejó de ponerlo **#3** del pilar Agentes.

### El auditor de páginas (`auditar_paginas.py`, nuevo)

Barre las 71 páginas y les pregunta lo que ningún guardrail preguntaba: **¿lo que publica
esta página lo sostiene la data?** Seis clases:

| | qué caza |
|---|---|
| **P1** | el orden no predice el caso que la página promete |
| **P2** | ninguna columna explica el orden de las filas |
| **P3** | recomienda retirados, no-aptos o no-rankeados sin salvedad |
| **P4** | muestra vacía o mínima |
| **P5** | frescura falsa |
| **P6** | cifras sin respaldo en `models.json` |

Primera corrida: **146 hallazgos**. Tras verificar uno por uno quedaron **37 reales**; los
otros 109 eran defectos del propio auditor —tolerancia de redondeo demasiado fina, leer
una columna fija en páginas que ordenan por otra, no ver dentro de `<strong>`, contar
filas solo si tenían columna de puesto, exigir monotonía en tablas que son dos bloques—.
Cada corrección quedó escrita en su chequeo, porque el auditor equivocado publica ruido
que entierra los hallazgos de verdad.

### Lo que el auditor destapó y ya está arreglado

- **P2 en 16 páginas: la tabla no explicaba su propio orden.** Los rankings por pilar
  ordenaban por un número que **no estaba en ninguna columna**, y las comparaciones
  mostraban «Global» (el compuesto con costo) mientras ordenaban por calidad media. En
  `/claude-vs-chatgpt/` eso se veía así: el #1 con Global 6,24, el #4 con 6,22 y el #6 con
  **8,41**, el mayor de la tabla. Un lector que intenta verificar el orden concluye, con
  razón, que la tabla está mal. Ahora la columna que ordena es la que se publica.
- **Las variantes PRO ya no encabezan** las tablas de comparación: van al final, donde
  corresponde a algo que por decisión vigente no compite.

Quedan 12 hallazgos medios —deuda editorial conocida, sobre todo variantes PRO citadas en
prosa— y **cero altos**. El auditor corre dentro de `regenerate_all.py` en modo `--duro`:
bloquea por severidad alta, no por deuda.

### Una falsa alarma, anotada

Sospeché que el pipeline daba «✅ sin drift» con un generador explotando. Se probó
rompiendo un import a propósito: **aborta con exit 1**. Lo que había pasado es que mi
`tail -3` cortó el error.

---

## [v4.4.0] - 2026-08-16 — Las dos suites más agénticas entran al pilar Agentes, que llevaba meses sin ellas

Un solo cambio, y no es una mejora: es **arreglar algo que estaba mal y nadie había
decidido**. El titular publicado no se mueve — `score_calidad` y `score_global` cambian en
**cero** modelos. Lo que cambia son los pilares, y bastante.

### Qué estaba pasando

Tres suites medidas tenían pilar natural y **no sumaban al promedio de su pilar**:

| suite | pilar | modelos medidos |
|---|---|---|
| `agent_long_horizon` | Agentes | 91 |
| `tool_calling_adversarial` | Agentes | 82 |
| `content_verificable` | Contenido | 92 |

Las dos primeras son las suites **más agénticas del benchmark** —sostener una tarea larga
y no inventar herramientas— y el pilar Agentes, que es el que se mira para elegir un
modelo de agente, las excluía. La tercera es la única suite de contenido donde se puede
**fallar** (`content_generation` da media 9,37 y no distingue un 8B de Opus), así que
Contenido quedaba apoyado justo en lo que no discrimina.

Nadie lo decidió: el mapeo viejo no las tenía y `export_for_pages` las salteaba en
silencio. Apareció al construir el registro único de suites (v4.3), no por un guardrail.

### La simulación, que es la que decidió

`benchmarks/simular_pilares.py` (nuevo) corre el export con y sin ellas, sobre los runs en
disco, y cuesta $0. La pregunta que importaba no era *"¿cambia?"* —iba a cambiar— sino
**"¿a quién castiga?"**: una suite que entra al promedio castiga al que no la rindió, y si
los que no la rindieron son un grupo con algo en común, el promedio deja de medir calidad
y empieza a medir quién se midió primero. Es la misma trampa por la que `integridad_idioma`
sigue afuera (17% de cobertura).

Se respondió sola: **las tres las rindió el 100% de los modelos rankeados.** No había
sesgo de muestra que justificara excluirlas. Entraron.

### Lo que se movió

| pilar | modelos que cambian de puesto |
|---|---|
| **Agentes** | **77 de 80** |
| **Contenido** | **75 de 80** |

    Poolside Laguna XS 2.1   Agentes  #29 → #5    (+0,42)
    DeepSeek V4 Pro          Agentes  #53 → #28
    Nemotron 3 Nano 30B      Agentes  #78 → #58   (+0,61)
    Inkling Small            Agentes  #18 → #45
    GPT-4.1 Mini             Agentes  #20 → #40
    Llama 3.3 70B            Contenido #16 → #40  (−0,29)
    MiniMax M3               Contenido #30 → #13

**Gemini 3.6 Flash sube del #65 al #50 en el pilar Agentes** — el caso que destapó todo
esto, cuando Cristian dijo *"lo estoy usando en Hermes y funciona muy bien"* contra un
número que decía lo contrario. Sigue lejos de su #3 en calidad agéntica, porque el pilar
promedia nueve ejes y él brilla en dos; para eso están los cortes por eje.

### Nota de versión

`scoring_reference.json` sube a v4.4 y **la calibración NO se recalculó** (sigue
`calibracion_heredada_de: v4.1`): esto no toca el score global. La versión sube igual
porque **92 modelos publican pilares distintos** — sin bump, alguien que citó «Llama 3.3
70B es #16 en Contenido» no tendría contra qué versión compararlo.

---

## [v4.3.0] - 2026-08-15 — El estándar se adopta, el promedio deja de esconder, y el README deja de contradecirse

Tres tareas agénticas medidas, un estándar que ya no es nuestro, y cuatro guardrails
nuevos para clases de fallo que ningún detector cazaba.

### El estándar de tareas dejó de ser propio

`ESTANDAR-TAREAS.md` pasa a ser la [rúbrica de Terminal-Bench Science](https://github.com/harbor-framework/terminal-bench-science/blob/main/rubrics/task-implementation.toml)
—25 criterios, del mismo Harbor que ya usábamos— adaptada de ciencia a negocio, más el
diseño de dominio de [τ²-bench](https://github.com/sierra-research/tau2-bench).

Antes eran 18 reglas deducidas de errores propios, una por una. **Dos de sus criterios
describen exactamente los fallos que costaron correcciones ese mismo día:**
`functional_verification` (no hacer matching de palabras) y `essential_difficulty` (la
dificultad viene del razonamiento, no del formato). Estaban publicados desde antes.

### Tres tareas medidas · US$ 9,3 en total

| tarea | cobertura | hallazgo |
|---|---|---|
| **reunión de socios** | 70 modelos · 229 corridas | **20 de 70 no saben registrar «esto quedó sin decidir»** |
| **ruteo de modelos** | 69 modelos · 231 corridas | satura (88%), pero **4 modelos exponen datos de clientes** |
| **cotizar / facturación** | ya medidas | deuda C7 **descartada con data**, no con opinión |

**El hallazgo de reunión se fortaleció al escribir la regla**: de 14/68 (21%) a 8/70
(11%). Los que quedan no fallaron por no deducir algo tácito — lo incumplieron teniéndolo
delante.

En ruteo, la trampa que más cazó (11 corridas, 7 modelos) fue **asignar por debajo de la
calidad que el trabajo necesita**, y existe por una corrección de Cristian: *«el ruteo no
tiene que ser el más barato, es el mejor resultado al mejor precio»*. Sin ese test la
tarea habría dado 68 de 69 perfectos y no habría medido nada.

### El promedio esconde el eje que decide — ahora hay dos casos medidos

| modelo | índice de calidad | trabajo agéntico |
|---|---|---|
| **Gemini 3.6 Flash** | **#76 de 80** | **#3 de 80** en calidad agéntica |
| **DeepSeek R1** | **#3 del catálogo** | **el peor** de la tarea de ruteo |

El primero salió de que Cristian dijera *«lo estoy usando en Hermes y funciona muy bien»*
contra un número que decía lo contrario. Es top-7 en sostener un hilo largo y en precisión
de datos, y penúltimo escribiendo copy de ventas — y el índice promedia 29 suites.

### Variantes de esfuerzo: NO se rankean, y el criterio es el precio

`gpt-5.6-luna-pro` cuesta **exactamente igual** que `gpt-5.6-luna` ($0,10/$0,60): no es
otro producto, es el mismo modelo razonando más. Rankearlo obligaría a medir Claude con
extended thinking, o3 en high, Gemini con thinking budget — y el benchmark se vuelve
combinatorio. Gemini 2.5 Pro, en cambio, tiene precio propio: es producto y sí rankea.

### Contra qué razonamiento medimos, medido

Se sondeó empíricamente y **corrige algo que se afirmaba mal**: no es cierto que a
Anthropic le vaya el thinking apagado.

    DeepSeek R1   7.585 tok    Claude Opus 5    343    GPT-5.6 Luna  70
    Tencent Hy3     626        Claude Sonnet 5  148    Haiku 4.5      0

Los proveedores razonan por default aunque el cliente no configure nada, y **el default no
es uniforme ni dentro de una familia**. Cada run graba ahora `judge_model` y
`reasoning_tokens`: un cambio de default se verá como corrimiento de distribución.

### El README pasa de 700 a 248 líneas

Tenía un título de sección que **negaba la decisión vigente** («Score = combinación
ponderada (NO solo calidad)») y declaraba «23 suites» cuando son 31. El detalle se mudó a
`METODOLOGIA.md` sin perder los post-mortems que valen.

### Guardrails nuevos (van 8, todos probados contra su propio fallo)

- **`check_claims.py`** — afirmaciones de método caducas. `check_consistency` caza CIFRAS;
  esto caza CLAIMS, prosa sin números que dice lo contrario de lo que hacemos.
- **`completar_examen.py`** — modelos con muestra suficiente FUERA del ranking por
  exámenes a medias. Había **7, bloqueados por 36 tests sueltos** — entre ellos uno con
  calidad 8,60, más alta que el #1 publicado.
- **`sonda_razonamiento.py`** — cuánto razona cada modelo por default, con histórico.
- **`export_harbor`**: el checksum vigente es el **más reciente**, no el mayoritario. Por
  mayoría habría publicado 204 corridas obsoletas **en verde**.
- `no_apto` vs `irregular`: «nunca puede» y «a veces falla» dejan de ser la misma etiqueta.

### Catálogo

Entra **Gemini 3.6 Flash** (129 runs, a mitad de precio que su antecesor). **GLM 5.3**
queda bloqueado con el motivo escrito: salió el 14-ago solo por la API de Z.ai, sin key, y
sus pesos no son públicos todavía.

### Nota de versión

`scoring_reference.json` sube a v4.3 pero **la calibración NO se recalculó**: nada de esto
toca el score. Queda escrito en el archivo (`calibracion_heredada_de: v4.1`).

### Después del tag — el sitio, bajo el mismo dataset

Cinco cambios entraron después de taggear v4.3.0. No mueven un solo número medido, así
que **la versión del dataset no se toca**; van acá porque la regla del repo es que un
cambio publicado sin entrada es un cambio sin traza — y estos cuatro commits estuvieron
justo así hasta que se escribió esto.

- **6 cortes por eje individual en el sitio**, para que la web no quede distinta del repo:
  el promedio de 29 suites es el que escondía a Gemini 3.6 Flash en el #76.
- **La calculadora conocía los cortes a medias**: elegir una subcategoría podía devolver
  un listado vacío, porque el umbral de calidad quedaba fuera del rango de ese eje.
  Arreglado en `clampUmbralAlEje()`.
- **`check_calculator` C5** — el guardrail miraba en una sola dirección. C1-C4 preguntaban
  *"¿se rompió la calculadora porque cambió la data?"*; ninguno preguntaba lo contrario:
  **un eje medido que la calculadora dejó de exponer**. Se mide y no se muestra: nada falla.
- **QA funcional de la calculadora** (`qa_calculadora.mjs`, 16 chequeos): carga el `app.js`
  real contra los datos reales, incluidos los 5 del wizard. El wizard se había roto antes
  sin que nada avisara.
- **Dos columnas nuevas en la tabla** — las que convierten un score en una decisión:

  | columna | qué agrega |
  |---|---|
  | **Índice global** (al elegir un eje) | el puesto general al lado del puesto del eje. Un eje sin su global es medio dato: Gemini 3.6 Flash es #3 en calidad agéntica y #76 en el índice |
  | **Tarea real** | media **y piso** de las tareas Harbor. Antes era un badge ✓ sin número, y `1,00 (piso 1,00)` llevaba la misma marca que `0,67 (piso 0,00)` |

  El caso que las justifica se ve en una fila: `Llama 3.1 8B Instant` sale **#4 en tareas
  largas con 8,20** y ahora muestra al lado *#80 en el índice* y *0,00 piso 0,00* — tres
  señales alineadas donde antes había un 8,20 solo. El piso importa más que la media para
  trabajo desatendido: es la diferencia entre «a veces sale mal» y «no sale mal».

### La fila de dos líneas — y lo que apareció al copiarla

Cristian mandó la tabla de lanzamiento de Qwen3.8: *"ejemplo de cómo otros miden y
comparan"*. Lo que hace bien es barato: cada fila dice **qué mide en humano** arriba
(`Long-horizon office work`) y **el benchmark técnico** abajo (`CoWorkBench`), agrupadas
por sección. Se lee sin saber qué es un benchmark.

Nosotros teníamos la idea escrita **a mano en tres archivos**, y al medirla apareció que
no era un problema cosmético:

| | medido el 15-ago |
|---|---|
| suites dichas de **dos formas distintas** | **7** |
| suites sin nombre humano (id técnico en la cara del usuario) | **2** |
| suites en **pilares distintos** según qué archivo se leyera | **7 de 28** |
| suites medidas que **no sumaban al promedio de su pilar** | **3** |

Las tres últimas son `agent_long_horizon` (91 modelos), `tool_calling_adversarial` (82) y
`content_verificable` (92). Las dos primeras son las suites **más agénticas** del
benchmark, y el pilar Agentes las excluía — nadie lo decidió, `SUITE_TO_PILLAR`
simplemente no las tenía y `export_for_pages` las salteaba en silencio. **Explica algo que
ya estaba anotado sin causa**: que el pilar Agentes tampoco mostraba a Gemini 3.6 Flash.
No era solo que promedia.

Ahora el registro es uno (`benchmarks/suites.py`), viaja en `models.json` y el sitio lo
lee en vez de copiarlo. Meter las tres al promedio mueve números publicados, así que queda
declarado con su motivo (`en_promedio: False` + `nota`) hasta simularlo — no se decide de
pasada.

### Las comparaciones: eje por eje, y el examen parejo

Las 36 páginas `X vs Y` ahora publican una tabla **fila por eje** entre los dos campeones,
agrupada por pilar, con el nombre humano y el id técnico. Es la mejora de más superficie
de esta entrega: son las páginas que traen gente al benchmark.

Lo que **no** se copió de la tabla de Qwen es su punto ciego, y es el que más importa: ahí
**9 de 32 celdas de rivales están vacías** —Muse Glimmer rinde 2 de 8, Opus 4.6 Max 5 de
8— y de las cinco filas donde Qwen se marca ganador, **tres son filas donde Opus no tiene
dato**. Ningún número miente; el sesgo está en qué filas se eligieron. Acá la cobertura va
arriba de la tabla («los dos rindieron los 28 ejes» o «el examen no está parejo»), y un
eje que rindió uno solo sale «sin comparar» y no cuenta para el veredicto.

Al construirlo cayeron tres cosas que nadie estaba mirando:

- **22 de 72 lados estaban coronados por un modelo que no rankea**, 15 de ellos variantes
  PRO — que por la decisión del 15-ago **no compiten**. La decisión estaba escrita y las
  páginas de más tráfico la ignoraban.
- **3 páginas publicadas que ya no genera nadie**, con datos congelados desde junio.
  `minimax-vs-kimi` y `diffusiongemma-vs-gemma-4` vuelven al generador;
  `grok-4.3-vs-gpt-5.5` (duplicado del slug canónico, punto vs guion) pasa a ser un
  redirect de verdad — estaba decidido desde julio y el archivo seguía sirviendo su copia.
- Se descubrieron **preguntando lo contrario de lo habitual**: no «¿falta una página?»
  sino **«¿sobra una?»**. Una huérfana no falla — carga, se ve bien y miente despacio.

### Desde el índice de calidad se llega a cualquier eje

El desplegable de subcategorías ahora aparece también sobre el índice de calidad, con los
28 ejes **agrupados por pilar** (`<optgroup>`), y muestra debajo la línea humana + el id.
Hasta acá, para llegar a `agent_long_horizon` había que saber de antemano que vivía bajo
«Agentes» — y ese eje es justo el que separa un modelo que sirve para un agente de uno que
no.

### Guardrails: van 12, y 20 chequeos funcionales

- **`check_suites.py`** — el registro tiene que seguir siendo uno: nadie puede volver a
  escribir las etiquetas a mano en `app.js`, y toda suite medida necesita nombre humano.
- **Q12–Q15** en el QA funcional: el menú sale del registro · desde el índice de calidad
  se llega a cualquier eje sin vaciar la tabla · ninguna comparación corona a un
  no-rankeado sin la salvedad · ninguna página publicada quedó sin dueño.
- Los dos nuevos **fallan cuando deben** (`test_guardrails.py`, 12 de 12).

Y un test que se arregló a sí mismo: **Q4 fallaba en los 4 presets** al reordenar el menú
— no porque los presets se rompieran, sino porque `baseFiltros()` arrastraba la
subcategoría que dejaba Q1. Un test que depende del orden en que corren los demás no
prueba lo que dice probar.

---

## [v4.2.0] - 2026-08-14 — El benchmark deja de suponer que un buen modelo sirve en un agente

Hasta hoy el sitio respondía *"¿qué modelo es mejor?"*. No respondía la pregunta que
realmente se hace quien va a poner esto a operar su negocio: **¿este modelo puede
ejecutar una tarea, de punta a punta, dentro de un agente?** Resultan ser preguntas
distintas, y ahora hay data para probarlo.

### La dimensión agéntica: 74 modelos medidos dentro de un agente real

No es una suite nueva del runner. Es **Harbor** (el harness de Terminal-Bench) corriendo
`mini-swe-agent` en Docker: el modelo recibe un correo de un cliente, lee el tarifario y
las reglas en disco, decide qué se cobra y qué no, y escribe `cotizacion.json`. Un pytest
verifica el artefacto. **Nada de parsear prosa** — que fue justo lo que produjo seis
falsos negativos en la versión casera de esta misma tarea.

**74 modelos · 231 corridas · 3 intentos cada uno · US$ 2,66 en total.**

| resultado | modelos |
|---|---|
| perfecto en los 3 intentos | 48 |
| parcial (0,44 – 0,97) | 21 |
| **no pueden ejecutarla** | **5** |

### El hallazgo que justifica publicarla aparte

**Hermes 4 405B tiene índice de calidad 8,20 —mejor que 40 de los que resolvieron la
tarea— y saca 0,00**, porque no existe endpoint que le dé herramientas. Verificado contra
la fuente primaria: la documentación de Nous Research dice que Hermes 4 *"no está
recomendado para usar dentro de Hermes Agent… está afinado para chat y razonamiento, no
para el bucle rápido de tool-calling"*.

Promediar 8,20 con 0,00 produce un número que miente sobre las dos cosas. Por eso la
dimensión agéntica **no entra al índice de calidad**, igual que tool calling y seguridad
— y por la misma razón que Artificial Analysis saca costo y velocidad de su índice.

**Y el dato más accionable del lote:** `qwen3-next-80b-a3b` saca **0,81 en `instruct` y
0,00 en `thinking`**. Mismo modelo, mismo tamaño, mismo proveedor. La variante que razona
no sostiene el bucle de herramientas — y sus índices de calidad están casi empatados
(7,93 vs 7,49), así que el ranking no te lo iba a decir nunca.

### El estado vale más que el número

Un reward 0 tiene tres causas que **no significan lo mismo**, y la media las colapsa:

| estado | qué pasó |
|---|---|
| `sin_herramientas` | no existe endpoint con tool use. **Nunca vio el encargo** |
| `rompe_bucle` | tiene herramientas y no sostiene el formato de tool call |
| `hizo_mal_la_tarea` | corrió, entregó, y está mal |

La causa se **deriva de la traza** con firmas explícitas, no se escribe a mano. Ya publiqué
una vez un 0,0 que era del harness y no del modelo.

### En la calculadora

Filtro nuevo: **«Sólo los que COMPLETAN una tarea real dentro de un agente»** — corta 10 de
79 rankeados (5 medidos que no pueden, 5 sin medir). Un modelo sin medición **no pasa**:
mismo criterio conservador que el filtro de contexto efectivo.

Y dos badges que se ven **siempre**, no solo con el filtro activo, porque el dato importa
justo cuando nadie lo fue a buscar: `⛔ no corre en agente` (el único tag rojo del sitio) y
`🤖 agente ✓`.

### Guardrails nuevos, en el mismo commit

- **`export_harbor.py`** — persiste los resultados a `tareas-agente/resultados.json`. Antes
  vivían **solo** en `jobs/`, que está gitignored: un `rm -rf` borraba 222 corridas sin
  dejar rastro. El runner tenía esto resuelto desde siempre; la tarea agéntica, por venir
  de un harness externo, no lo heredó.
- **Corridas con `task_checksum` distinto no se promedian.** Es `prompt_sha` para tareas
  Harbor: si cambió un test, no es el mismo examen. Detectó 2 de 231 corridas que venían de
  una versión vieja y habrían entrado calladas al promedio.
- **Un resultado agéntico no se hereda entre proveedores** del mismo id. El lote corrió
  contra `openrouter/<id>`; NIM y Groq son endpoints distintos. Sin esto, la variante NIM de
  Qwen 3-Next heredaba un "no apto" que nadie midió en NIM.
- **`check_version` ahora lee el schema.org.** Declaraba `v4.0` en dos campos mientras el
  hero decía `v4.1`, y nada fallaba — la superficie que ven Google y los crawlers de IA
  estaba una versión y media atrás.

### Nota de versión

`scoring_reference.json` pasa a `v4.2` pero **la calibración NO se recalculó**: v4.2 agrega
una dimensión que se publica aparte y no toca el score. Los mean/std siguen siendo los de
v4.1, y queda escrito en el archivo (`calibracion_heredada_de`) para que la etiqueta no se
lea como un recálculo que no ocurrió.

---

## [v4.1.0] - 2026-08-13 — Dos ejes, una escala anclada, y tres columnas que decían lo mismo

Cambia **qué publicamos**, no solo cuánto medimos. El hilo: cada número derivado que
mezclaba calidad con precio resultó ser, medido, una de las dos cosas con otro nombre.

### El titular deja de mezclar calidad con precio

`score_global` (calidad 70% + costo 15% + velocidad 7,5% + latencia 7,5%) **castigaba caro
y premiaba barato sin decirlo**: Claude Opus 4.6 era #5 en calidad y se publicaba #18;
Poolside Laguna XS era #29 y se publicaba #7. Las dos cifras eran verdad *con etiqueta*;
ninguna lo era bajo un rótulo que dice `score_global`.

Ahora el titular es el **índice de calidad** y el precio va como columna al lado. Es lo que
hace Artificial Analysis con su Intelligence Index.

### Todo composite terminó siendo una copia. Medido tres veces

| segundo eje candidato | correlación con calidad | veredicto |
|---|---|---|
| compuesto 70/15/7,5/7,5 | **r = 0,943** | copia |
| compuesto v2.9 60/20/10/10 | **r = 0,882** | copia |
| columna "Rinde" (score²÷costo) | **r = 0,999** con *ordenar por precio* | copia |
| **frontera de Pareto** | deja fuera 69 de 82 | **aporta** |
| **calidad por dólar** | **r = 0,052** | **aporta** |

La causa es estructural, no de pesos: el costo z-scoreado aporta ±0,30 al compuesto contra
±1,3 de la calidad. Y con la escala absoluta se ve todavía más crudo — la calidad varía
**1,19×** y el costo **772×**, así que "valor" *es* precio.

Lo que informa son las métricas que **no** son un promedio ponderado: un **descarte** (la
frontera) y un **ratio** (calidad/$).

### Escala absoluta: el índice deja de z-scorearse

`score_calidad` pasa a ser `quality_avg` tal cual — la media de las notas 0-10 por rúbrica,
donde 10 sería perfecto en todo el examen. Con eso **agregar un modelo no mueve el score de
nadie, nunca más**, y una cifra citada deja de caducar sola.

El z-score estiraba una diferencia real de 1,39 puntos hasta 8 puntos publicados: Llama 3.1
8B mide **7,26 sobre 10** y se publicaba como **0,50**, que se lee como inservible.

Rango nuevo: **7,26–8,65**. Se ve apretado porque lo está — y esa es la información.

### Por qué está apretado: 5 de 28 suites ya no distinguen a nadie

| suite | runs con 10,0 perfecto |
|---|---|
| `string_precision` | 96% |
| `niah_es` | 91% |
| `structured_output` | 78% |
| `content_verificable` | 77% |
| `ocr_extraction` | 64% |

Todas usan scoring `verificable` (objetivo, pasa/no pasa) y **los modelos las pasan**. No es
rúbrica blanda: es techo de dificultad. Se ensancha endureciendo las suites, no estirando la
escala. Trabajo de v4.2.

### Recalibración a v4.1

Los 3 scorers huérfanos dejaron de devolver `5.0` de relleno: la calidad media de los mismos
68 modelos subió de 7,926 a 8,114 (+0,64 σ), o sea **+1,48 puntos de inflación** contra una
referencia calibrada para la escala vieja. Referencia regenerada; baselines en
`results/_baselines/`.

### Mediciones

**13 modelos nuevos · 2.155 runs · $77,57 reales.** Rescore de **10.503 runs** desde las
respuestas guardadas, sin re-medir ningún modelo ($1,25).

### Instrumentos nuevos (el tema de v4.0.3, continuado)

- **`calculate_costs.py --estimar`** — proyecta el costo POR SUITE antes de lanzar. Existe
  porque estimé un lote en $15,09 y el examen completo costaba **$98,96** (6,6×). La Regla
  0.5 ya advertía sobre multi-turno y no alcanzó.
- **`calculate_costs.py --gastado`** — el gasto real de un lote, separando lo pagado de lo
  nocional por suscripción. Existe porque reporté $40,45 sumando a mano y la key marcaba
  $77,32: me había saltado siete archivos.
- **`reasoning_tokens` se persiste** — se capturaba solo en Responses API; por OpenRouter,
  que es por donde pasan los 26 thinking rankeados, no se guardaba. Los 3.901 runs de agosto
  no tienen ni uno.
- **Guardrail C3 corregido** — comparaba contra el líder del compuesto cuando ya se publica
  el de calidad, y buscaba el nombre mientras MODELOS.md rotula con el id.

### Correcciones al sitio

- **"Caro" para un modelo de $1,86/mes.** Etiqueta absoluta sobre una medida relativa, con
  acantilado: 29% salía "Aceptable" y 24% "Caro". La columna se eliminó (ver arriba).
- **La lista filtraba en silencio.** Ahora dice "24 de 82 · el que más corta: calidad ≥8,0".
- **La FAQ recomendaba DeepSeek R1 para agentes N8N** — saca 4,23 en tool calling, bajo el
  umbral con que la propia calculadora lo filtra. Ahora es el contraejemplo.
- **La OG image mostraba otro #1** que la página que anuncia.
- **El filtro "sólo con tool calling" no filtraba nada**: usaba capacidad *declarada*, que
  declaran los 82. Ahora usa la nota medida.

### Pendiente, dicho explícitamente

- El **pilar del blog** quedó desactualizado: su sección de método explica el compuesto, que
  es justo lo que dejamos de publicar. Necesita reescritura, no find-replace.
- **23 modelos nuevos** detectados en OpenRouter → lote de septiembre, para medirlos una sola
  vez bajo v4.1.
- **`effort=high` no es el techo de razonamiento de Anthropic.** Estamos comparando modelos
  en configuraciones de razonamiento que no sabemos si son equivalentes.
- **90 runs de `niah_es` con needles v2** (`api_key_*`, 4K y 16K) se escaparon del archivado
  del 2-jun y contaminan la media: miden negativa ante credenciales, no retrieval.

## [v4.0.3] - 2026-08-12 — El día que el instrumento se midió a sí mismo

Sesión larga que empezó siendo "corregir precios" y terminó encontrando **cinco reglas
correctas que nada verificaba**. Ninguna estaba mal escrita; todas fallaban en silencio.

> **La lección que engloba a las demás, y queda en CLAUDE.md:**
> *una regla sin instrumento que la haga cumplir es una regla que ya se rompió y no te
> enteraste.*

### 🔴 Bugs que publicaban datos falsos

| Bug | Consecuencia medida |
|---|---|
| **`check_endpoints.py` nunca cargaba el `.env`** | reportaba SIN CREDENCIAL en los 70 rankeados → **no podía detectar un solo muerto**. El guardrail existía porque Devstral Small estuvo #5 con el endpoint apagado, y llevaba tiempo ciego |
| **`structured_output` publicaba 5,00 fijo** en los 117 modelos | le faltaban los scorers `json_valid`/`json_exact`/`language_check`; caían al `else: return 5.0` |
| **El skip de `niah` ignoraba el presupuesto de salida** | **378 runs históricos perdidos en 23 modelos**, contados como fallo del modelo cuando el prompt nunca cabía |
| **Se mandaban `tools` a proveedores que las ignoran** | doc de OpenRouter: sin `require_parameters` es solo *soft preference*. El modelo nunca las ve y queda anotado como "no llamó a la herramienta" |
| **El juez corría donde su veredicto se descarta** | 96 de 147 tests no-niah tienen verdad objetiva → **2,1 h por modelo** esperando una opinión que el scoring tira |
| **34 precios equivocados** | a **GPT-5.6 Luna se le cobraba 10× de más** siendo #1; **DeepSeek V3.2** —el que corre en producción en Eco— se publicaba **3,7× más barato** de lo que cuesta |

### ✅ Lo que se instaló

**Scoring.** Los 3 scorers huérfanos implementados y validados contra **755 respuestas
reales ya guardadas**: `structured_output` pasó de un valor único a rango 0–10 con 57
valores distintos. Encontró en datos viejos la fuga que motivó el test: `nim-step-3.5-flash`
escribió **硬件** y `mimo-v2.5-or` **直接** en artículos en español. ⚠️ El `rescore_all.py`
que los aplica al histórico **queda pendiente**, con el baseline congelado en
`results/_baselines/`.

**Trazabilidad.** `PROMPTS.md` con los **206 prompts exactos** + `prompt_sha` por run + la
entrada guardada en cada `.md` + la **conversación completa** en multi-turno (antes se
guardaba solo la última respuesta de 8 turnos). Habilitó auditar si algún prompt cambió con
runs a ambos lados: **7 suites sospechosas, 6 cosméticas, `niah` real**.

**Endpoint ≠ modelo.** Cada run registra `upstream_provider`. **40 de 68 rankeados tienen
proveedores no equivalentes**: Nemotron 3 Super va de 8.000 a 1.000.000 de contexto según
cuál toque; Kimi K2.6 de `int4` a `bf16`. Nemotron 3.5 Lightning se midió en un endpoint
con **28.672 de contexto cuando su spec dice 262.144**.

**Retiros.** `retired_at` / `retired_reason` / `retired_kind` estructurados (antes:
comentarios ilegibles para los generadores). La tabla distingue lo que sacó el proveedor de
lo que decidimos nosotros —Phi-4 figuraba como "el proveedor ya no lo sirve" siendo el
juez— y avisa si el modelo **sigue vivo por otra ruta**. Y `--recheck-retired`: **el retiro
no es una puerta de una sola vía**, dos modelos habían resucitado.

**Detectores nuevos.** `E7` (open_source sin evidencia: 108 entradas, **37 rankeadas** y
publicadas en el corte "solo open-source") y `E8` (cero tool calls en una suite entera) —
el primero que caza **presencia** sospechosa y no ausencia.

**Herramientas.** `sync_prices.py` (los precios se sincronizan, no se escriben) ·
`release_diff.py` (el DATASHEET sale de un diff automático, ordenado por impacto en una
decisión) · `generate_prompts_catalog.py`.

### 📊 Datos

- **11 modelos nuevos** al catálogo, elegidos por utilidad para el ICP y no por novedad
  (Nemotron 3.5 Lightning, Muse Glimmer 30B, Laguna S/XS 2.1, Inkling Small, Ling 3.0
  Flash, Solar Pro 4, Qwen 3.7 Flash, Nex-N2-Mini, Tencent Hy3, DeepSeek V4 Flash 0731)
- **342 runs** de suites con herramientas re-medidos con el ruteo garantizado
- **2.501 runs archivados**: 443 de tools + 2.058 de `niah` anteriores al rediseño del 2-jun
- **12.020 runs** re-costeados · **2 modelos retirados** del ranking, **2 resucitados**
- Suite nueva **`integridad_idioma`** (4 tests), eje aparte

### 🔬 Lo que midió el instrumento sobre sí mismo

- **Ruido: ±0,58** con `--quick` (n=1) en las suites con herramientas. Explica mejor que
  cualquier hipótesis por qué `tool_calling` "no discriminaba": con un rango útil de 1,9
  puntos, **más de la mitad es ruido**. Corolario: el par de validación de Flip
  (gpt-oss-20b 6,91 vs llama-3.3 7,18) **está dentro del ruido**.
- **El español necesita 1,62× más tokens** (2,47 chars/token vs 4,00 inglés, medido sobre
  3.410 respuestas). Con `max_tokens=2048` entran ~920 palabras y los tests piden hasta
  1.300 → **31,3% de las respuestas de modelos no-thinking estaban truncadas por el
  harness**, no por el modelo.
- **Examen común: 93%** en las suites que puntúan (116 de 125 tests en los 68 modelos). El
  38% que asustaba al principio era `niah` y `prompt_injection`, que difieren **por
  diseño**.

### 🙅 Dos hipótesis propias que el dato NO sostuvo

Quedan registradas porque el repo vale por sus números, no por tener razón:

1. **"El fallback de ruteo explicaba la anomalía de `tool_calling`".** No. Re-medidos los 19
   modelos expuestos: Δ quality **+0,22 con t=1,61** (no significativo) y **correlación
   +0,07** entre exposición al ruteo y mejora — cero, y con el signo al revés del predicho.
   Hay **un** caso real y grande (Llama 3.3 70B, 55% → 94% de tool calls), no diecinueve.
2. **"Apagar el thinking iguala la cancha".** Verificado: apagarlo **cambia la capacidad**.
   Sin razonar, Nemotron Lightning respondió 41,98% y MiniMax M3 respondió 10,93% a un
   cálculo cuya respuesta es 19,13%. Por eso v4.1 **recorta la traza al puntuar** en vez de
   apagar el razonamiento.

### 📋 Pendiente, con plan escrito

`rescore_all.py` (mueve `quality_avg` de los 117, con baseline congelado) · el
`else: return 5.0` → `raise` en su propio commit · y **v4.1**, que agrupa todo lo que rompe
comparabilidad en **una sola frontera**: `max_tokens` uniforme, traza de razonamiento
recortada y `niah` con prompt canónico por celda. Ver `PLAN-V4.1.md`.

## [v4.0.2] - 2026-08-12 — El guardrail de endpoints dejó de correr ciego (y encontró 2 muertos rankeados)

`check_endpoints.py` existe desde julio porque **Devstral Small estuvo #5 del ranking meses después
de que Mistral apagara su endpoint**, recomendado en 11 páginas del sitio. Resulta que desde
entonces el chequeo **nunca detectó nada, porque nunca pudo**.

### Por qué estaba ciego
`benchmarks/config.py` es el único módulo que corre `load_dotenv()`, y `check_endpoints.py` no lo
importaba. Corriendo dentro de `regenerate_all.py` no leía el `.env`, no encontraba ninguna
credencial y clasificaba **SIN CREDENCIAL a los 70 rankeados**: cero pings reales, cero muertos
posibles, y el pipeline terminaba en verde. Un guardrail que no puede fallar tampoco puede avisar.

Encima, la `OPENROUTER_API_KEY` del `.env` devolvía **401**. Dos fallos apilados: aunque el import
hubiera estado, no habría servido. La key se rotó el 12-ago.

### Corregido
- **`import benchmarks.config`** en `check_endpoints.py`, con el comentario que explica por qué no
  se puede borrar.
- **`DEAD_MARKERS` ampliado** con `"period has ended"` / `"please migrate to"`. Devstral 2 caía al
  bucket genérico `ERROR` —o sea, se publicaba igual— porque OpenRouter usa una redacción que la
  lista no contemplaba. El mensaje además se contradice: *"migrá al slug pago:
  `mistralai/devstral-2512`"*, que es exactamente el slug que se estaba llamando.

### Retirados (`retired: True`) — 2 modelos que estaban en el ranking
| Modelo | Estaba | Runs | Evidencia |
|---|---|---|---|
| **Nemotron Super 49B v1.5** (`or-nemotron-super-1.5`) | **#8** | 128 | 404 "No endpoints found" + ausente del catálogo público de OpenRouter |
| **Devstral 2 (Dic 2025)** (`devstral-2`) | #45 | 136 | 404 + **cero ids `devstral`** en el catálogo + búsqueda en la UI sin resultados |

Ambos confirmados por **tres vías independientes** antes de tocarlos (ping, catálogo público, UI),
y con la cuenta verificada sana (`mistral-large-2512` responde 200 con la misma key). El error
inverso —matar un modelo vivo— ya se cometió una vez con Llama 3.1 8B y cuesta igual de caro.

**Ranking: 70 → 68 rankeados. No entra nadie, y ningún score se movió** (la referencia z-score
congelada de v4.0 funcionando como debe). Sus runs siguen en los datos: alimentan el análisis
histórico y aparecen en la sección *Retirados* de MODELOS.md.

### Matiz importante: no murió el modelo, murió la RUTA
Los dos siguen disponibles vía **NVIDIA NIM**, y ahí los tenemos medidos: `nim-nemotron-super-1.5`
(92 runs) y `nim-devstral-2-123b` (64 runs), ninguno retirado. Decir "el modelo murió" sería
falso. Lo correcto es *"ya no está en OpenRouter"* — que para quien lo integró por ahí es la
misma mala noticia, pero para quien elige modelo es información distinta.

## [v4.0.1] - 2026-08-11 — Precios: un solo punto de verdad (y el ranking se movió)

Corrección de datos, **no de fórmula**. La calidad, los pesos y la referencia z-score congelada
(`scoring_reference.json`, v4.0) quedaron **intactos**: no se recalibró nada y no se midió ningún
modelo nuevo. Lo único que cambió es el precio — que pesa 15% del score y, a diferencia de una
suite constante, **sí mueve el orden**.

### El problema: dos fuentes de precio, y ninguna al día
El costo se escribía a mano en dos archivos distintos (`models.py` y el dict `PRICING` de
`scoring.py`). Cruzados contra la API pública de OpenRouter el 11-ago: **34 precios equivocados en
el catálogo**, y entre los dos archivos **34 ids con valores distintos** más 19 ids que ya no
existen en ninguna parte.

Ya se había arreglado a mano antes. Dos veces. En **v2.6.3 (22-may-2026)** se corrigieron 7
precios "en ambos" archivos, y en junio otro más. El caso que lo prueba: **Grok 4.20** se corrigió
en mayo de `$2/$6` a `$1.25/$2.50`; en agosto `PRICING` decía otra vez `$2.00/$6.00` — el valor
exacto de antes de la corrección. **Un precio a mano no solo caduca: se revierte.**

### Corregido
- **`sync_prices.py` (nuevo)**: sincroniza el catálogo contra `openrouter.ai/api/v1/models`
  (pública, sin auth). Idempotente, con backup, y **nunca escribe $0** (regla dura: un modelo
  gratis gana el eje costo artificialmente). Respeta `free_runtime`. **34 precios corregidos**,
  diff de 52 líneas, **cero cambios fuera de `cost_input`/`cost_output`**.
- **`PRICING` ya no se mantiene a mano: se DERIVA de `MODELS` + `OLLAMA_MODELS`.** Un solo punto
  de verdad. Los 19 ids huérfanos se borraron **después de verificar que no tenían ningún run**
  en los 20.192 del histórico (el único con runs, `minimax/minimax-m2.7-highspeed`, ya matcheaba
  por nombre y nunca usó el fallback). Las 13 entradas en $0 desaparecieron con eso.
  Regla de colisión documentada: cuando un mismo `id` tiene varias entradas con precios distintos
  (8 casos: el mismo modelo por OpenRouter, Groq o NIM), **gana el más caro** — ante la duda,
  nunca sub-costear.
- **Import muerto** de `PRICING` en `export_for_pages.py`: importado y jamás usado, con un
  docstring que decía que recalculaba costo con él. Quitado y el docstring corregido.
- **`rescore_costs.py`** propagó el precio nuevo a los runs históricos: **12.020 de 20.192 runs**
  (idempotente; la 2ª corrida da 0). Toca exactamente 3 campos —`cost_usd`, `cost_score`,
  `final`— verificado sobre el diff completo.

### Delta real del ranking publicado
**20 modelos** se movieron ≥0,05 en `score_global`. Nadie entró ni salió del ranking (70 antes y
después) y el #1 no cambió. Todos los movimientos se explican por su cambio de precio.

| Modelo | Score | Posición | Precio $/M (antes → ahora) |
|---|---|---|---|
| **GPT-5.6 Luna** | 8.34 → **8.80** | #1 → #1 | 1.00/6.00 → **0.10/0.60** (se le cobraba 10× de más) |
| MiMo-V2.5 Pro | 6.49 → 6.79 | #21 → **#12** | 1.00/3.00 → 0.435/0.87 |
| GPT-5.6 Terra | 6.22 → 6.49 | #27 → #22 | 2.50/15.00 → 1.00/6.00 |
| MiMo-V2.5 (omnimodal) | 6.02 → 6.28 | #29 → #27 | 0.40/2.00 → 0.14/0.28 |
| GLM 5.2 | 7.14 → 7.33 | #6 → **#3** | 0.95/3.00 → 0.49/1.54 |
| Qwen 3.6 Plus | 7.17 → 7.00 | #5 → #7 | 0.18/1.07 → 0.325/1.95 |
| Kimi K2 | 5.56 → 5.39 | #36 → #43 | 0.20/0.80 → 0.57/2.30 |
| **DeepSeek V3.2** | 6.47 → 6.34 | #23 → #24 | 0.14/0.28 → **0.2574/1.0287** |
| GLM 5 | 6.86 → 6.77 | #10 → #15 | 0.60/1.92 → 0.95/2.55 |

Los otros 11 se mueven ≤0,17. Cinco son variantes NIM/Ollama Cloud cuyo precio propio no cambió:
se mueven porque el export normaliza el costo al **equivalente OpenRouter**, y ese sí cambió.

**Lo que hay que decir en voz alta:** el #1 subía porque se le cobraba **10× de más**, y
**DeepSeek V3.2 —el modelo que corre en producción en Eco— se publicaba 3,7× más barato de lo que
cuesta**. Al corregirlo baja un puesto. Es el precio de tener el número bien.

### Dos guardrails que fallaban en verde (encontrados de paso, NO arreglados acá)
- **`check_endpoints.py` corre ciego.** Solo `benchmarks/config.py` carga el `.env`, y ese script
  nunca lo importa: cuando lo dispara `regenerate_all.py` reporta **SIN CREDENCIAL en los 70
  modelos** y por lo tanto **nunca puede encontrar un muerto**. Es el chequeo que existe porque
  Devstral Small estuvo #5 meses después de que Mistral apagara su endpoint. Encima, la
  `OPENROUTER_API_KEY` del `.env` hoy devuelve **401**, así que ni cargando el `.env` habría
  servido. (El sync de precios no se ve afectado: ese endpoint es público.)
- **`check_consistency.py` no ve los bloques auto-generados.** Solo caza claims narrativos con la
  palabra "score"; las filas de la tabla `AUTO-RANKING` del README no la tienen. Dio verde con el
  README diciendo 8.34 y `models.json` 8.80. La red para eso es correr `regenerate_all.py` antes
  de commitear — que es lo que se hizo.

### Fuera de alcance a propósito
Los 3 scorers huérfanos (`json_valid`, `json_exact`, `language_check`) y el `else: return 5.0` de
`scoring.py:132` **siguen sin tocarse**: `structured_output` continúa publicando 5,00 fijo en los
117 modelos. Es el arreglo correcto y es el más riesgoso del plan — toca `quality_avg` de todos a
la vez, la misma superficie que colapsó el ranking a 6 modelos en julio. Va con protocolo propio
(baseline + rama aparte + un scorer por vez). Ver `PLAN-AGOSTO-2026.md`.

## [v4.0.0] - 2026-07-17 — Relanzamiento: referencia z-score congelada + limpieza definitiva + pase de UX

### Scoring
- **Referencia z-score CONGELADA por versión** (`scoring_reference.json`, `score_method: zscore_frozen_v4`): agregar/medir un modelo nuevo ya NO recalcula el score de los demás — se puntúa contra la referencia fija. Antes cada lote movía a todos. La referencia solo se recalcula con `export_for_pages.py --recalibrate --scoring-version vX.Y` (evento deliberado).
- **Eje agéntico expuesto** (`agentic_score`): lo agéntico cuenta en la calidad headline Y como eje separado.
- **Refusal policy**: rehusar filtrar credenciales o resistir ingeniería social ya NO penaliza (los tests `refusal_ok` puntúan la negativa como conducta correcta, quality=10).

### Datos
- **Limpieza definitiva**: archivado de runs corruptos (empties de rate-limit, fórmulas obsoletas, suites archivadas) + re-medición limpia. Nuevo campo `total_runs_measured` = esfuerzo total incl. descartados (27.741 = 23.369 activos + 4.372 archivados).
- **Prompt-based tool calling** para modelos sin `tools` nativo (Hermes 4) + verificador robustecido (retries, response_format json, fallbacks).

### Sitio / UX
- Wizard guiado de 3 pasos, logo wordmark texto → root del benchmark, header/footer canónico único, español neutro (cero voseo), structured data dinámico con señales de frescura (dateModified/version), sección "Cómo se mide", tabla de resultados simplificada a 9 columnas.

## [v3.1.2] - 2026-07-12 — Integridad del ranking: dos rankings públicos contradictorios

Auditoría de integridad disparada al preparar contenido sobre GPT-5.6 / Grok 4.5. **No se re-midió
nada** — los runs eran correctos. Lo que estaba roto era la capa que los publica.

### El bug de fondo: el z-score caduca las cifras escritas a mano
El `score_global` es un **z-score normalizado contra toda la población**. Consecuencia
contra-intuitiva: **medir un modelo nuevo recalcula el score de todos los anteriores.** Cualquier
cifra hardcodeada en un doc queda obsoleta sola, sin que nadie toque ese archivo.

Estado encontrado: el README publicaba **Grok 4.5 = 6.99** y **GPT-5.6 Luna = 7.92 (#6)** mientras
el sitio, generado desde `models.json`, mostraba **5.84** y **8.14 (#5)**. Dos números públicos
distintos para el mismo modelo, en un proyecto cuyo único activo es la credibilidad de sus números.

### Corregido
- **Piso de ranking unificado en 50 runs.** `generate_rankings.py` y `generate_comparison.py` ya
  filtraban ≥50 runs; `models.json` y `MODELOS.md` **no**. Resultado: el JSON público rankeaba
  **DeepSeek V4 Pro #3 con 10 runs**, y `MODELOS.md` coronaba a MiniMax M2.7 con 39. Ahora los
  umbrales viven en `export_for_pages.py` (`MIN_RUNS_TESTED=20`, `MIN_RUNS_RANKED=50`) y todo el
  pipeline los importa. Campos nuevos por modelo: `ranked`, `sample_tier` (`solid`/`partial`/
  `preliminary`). Los 21 modelos con muestra chica se publican en **"En evaluación"** con el score
  marcado como indicativo — visibles, pero fuera del podio.
  - **El #1 cambia**: DeepSeek R1 (103 runs) desplaza a MiniMax M2.7 (39 runs, ahora en evaluación).
- **Top-10 del README auto-generado** (`generate_readme_ranking.py`, nuevo). Se escribía a mano.
- **Claim falso de latencia, en 3 superficies.** README, `CLAUDE.md` y `docs/index.html` decían que
  la latencia medía *time-to-first-token*. El código promedia **`latency_total`** (respuesta completa,
  `export_for_pages.py:153`). Agravante: el preset "Chat en vivo" pondera esa dimensión al 25%.
- **Narrativa de Grok 4.5 corregida — con la data, no con la intuición.** La primera versión de esta
  auditoría escribió que "lo hunde la latencia". Sonaba lógico (29,7s de media) y era **falso**:
  descompuesto el z-score, la latencia aporta **−0.009**. Lo hunde el **costo** (z −1.16), y su
  calidad (7.97) está apenas **+0.31σ** sobre una media aplastada. En perfil batch (latencia y
  velocidad a cero) Grok **baja** al #56, no sube. Queda documentado en el README como recordatorio:
  **una historia plausible no es un dato.**
- **Tablas cortadas en móvil (HARD_BLOCK).** `body{overflow-x:hidden}` + `min-width:640px` global +
  tablas pSEO emitidas sin wrapper ⇒ en 360px las columnas de la derecha —**entre ellas el precio**—
  quedaban recortadas y **físicamente inalcanzables**, justo en el canal por donde llega el tráfico
  orgánico. Ahora `min-width` solo aplica dentro de un contenedor scrolleable, y las **14 tablas**
  del sitio (10 de generadores + 4 páginas manuales) van envueltas en `.table-scroll`.

### Guardrail (para que no vuelva)
- **`benchmarks/check_consistency.py`** (nuevo): falla con exit 1 si un doc **vivo** publica un score
  que ya no coincide con `models.json`. Ignora a propósito los **snapshots con fecha** (CHANGELOG,
  DATASHEET_*, INSIGHTS): esos deben conservar el valor del momento — reescribir la historia sería
  el bug, no el fix. Cableado a la **GitHub Action**: si un doc driftea, el build falla.
- `regenerate_all.py` incorpora el generador del README.
- `CLAUDE.md` dejó de duplicar el top-10: ahora apunta a la fuente. Sin cifra copiada, no hay drift.

### Pendiente (auditado, NO corregido — requiere decisión de producto)
- **La calculadora ignora los pesos del usuario al elegir un pilar** (`docs/app.js:393`): devuelve
  `score_by_pillar`, pre-horneado con 70/15/7.5/7.5. Los presets mueven los sliders y el ranking los
  ignora → **la UI le miente al usuario**. Nunca se puede expresar "coding, y no me importa la latencia".
- **La calidad casi no discrimina**: 91% de los modelos entre 7.0 y 8.7 (std 0.58), mientras el ruido
  del juez entre runs del mismo modelo es std ≈1.6–2.1. **El ruido es ~2.7× la señal** que ordena
  medio ranking, y el z-score lo amplifica. El 70% del peso está sobre la dimensión con menos poder
  de separación.
- **`RECOMENDACIONES.md` y `CASOS_DE_USO.md` están fuera de `regenerate_all.py`**: 81 días stale,
  recomiendan modelos que hoy están #66–#75, y `RECOMENDACIONES.md` tiene una sección duplicada.

## [v3.1.1] - 2026-07-10 — GPT-5.6 y Grok 4.5

### Benchmark nuevo
- **GPT-5.6 Luna** (`openai/gpt-5.6-luna`): 180 tests exitosos, score global **7.92**, posición **#6**.
- **GPT-5.6 Terra** (`openai/gpt-5.6-terra`): 174 tests exitosos, score global **7.69**, posición **#14**.
- **GPT-5.6 Sol** (`openai/gpt-5.6-sol`): 174 tests exitosos, score global **7.14**.
- **Grok 4.5** (`x-ai/grok-4.5`): 174 tests exitosos, score global **6.99**; penalizado por latencia alta (~16.7s TTFT) y costo $2/$6.

### Infraestructura
- Nuevo preset de juez `phi4-or` en `benchmarks/llm_judge.py`: Phi-4 vía OpenRouter para cuando el juez local no está disponible.
- Agregados modelos y context windows en `benchmarks/models.py`.

### Costo real del lote
- **$57.23** en modelos + **$1.65** en juez phi4-or = **~$58.88 USD**.

### Docs actualizadas
- `README.md`: versión 3.1.1, top-10 actualizado con GPT-5.6 Luna, sección de novedades, nota metodológica sobre el juez phi4-or y caveat sobre Muse Spark 1.1 (acceso regional bloqueado).
- Nuevas comparaciones pSEO para GPT-5.6 y Grok 4.5 (vs GPT-5.5, Claude Opus 4.8, DeepSeek V4, Gemini 3.5 Flash, MiniMax M3, Claude Sonnet 4.6, Claude Fable 5, y variantes internas Luna/Terra/Sol).
- `docs/data/models.json`, `MODELOS.md`, `TESTS.md`, MDs por modelo, rankings/comparaciones pSEO, sitemap y llms.txt regenerados.

### No medido
- **Muse Spark 1.1 (Meta)**: requiere Meta Model API, no disponible en la región del benchmark al momento del lanzamiento. Pendiente para cuando llegue a OpenRouter o se habilite el acceso regional.

## [v3.1.0] - 2026-07-02 — Release julio 2026

### Nuevo contenido pSEO
- **Landing de review**: `docs/fable-5-review/` — análisis de Claude Fable 5 con datos reales del benchmark (score 6.75, 103 runs, $10/$50 por millón) y comparaciones con Opus 4.8, Sonnet 4.6, MiniMax M3 y DeepSeek R1.
- **Nuevas comparaciones automáticas**: `fable-5-vs-claude-sonnet-4-6`, `fable-5-vs-minimax-m3`, `fable-5-vs-deepseek-r1`.
- **Comparaciones inválidas eliminadas** del generador: `glm-5.2-vs-qwen-3.7-plus`, `claude-opus-4.8-fast-vs-claude-fable-5`, `north-mini-code-vs-devstral-small` (no tenían modelos válidos).
- Regenerados `docs/sitemap.xml` (36 URLs) y `docs/llms.txt`.

### Integridad del benchmark
- Documentada la regla de oro en `AGENTS.md` y `CLAUDE.md`: **no se modifican los prompts ni criterios de `benchmarks/tests/`** para mantener comparabilidad histórica. Cambios de stack de producción van a documentación y generadores pSEO, nunca a los tests.
- Revertidos los cambios de `OpenClaw → Hermes` en `agent_capabilities.py`, `orchestration.py` y `tool_calling.py`.

### Artefactos regenerados
- `docs/data/models.json`, `MODELOS.md`, `TESTS.md`, MDs por modelo, rankings/comparaciones pSEO, sitemap y llms.txt.
- **CheatSheet PDF julio 2026** y **Executive Brief julio 2026**.

## [v3.0.2] - 2026-06-26 — Normalización de costos y comparabilidad global

### Cambio metodológico
- **Costo mínimo de referencia: $0.001/call** para todos los modelos en el cálculo del `score_global`.
  - Aplica a modelos gratis, free tier, suscripción y locales.
  - Evita el `cost_score` artificial de 10.0 que distorsionaba el ranking cuando el costo real era $0.
  - Implementado en `benchmarks/export_for_pages.py` (`MIN_COST_PER_CALL`) y en `cheatsheet/generate_executive_brief.py`.
- **Normalización OpenRouter con fallback a costo real del provider**:
  - Si un modelo tiene equivalente OpenRouter, se usa ese precio como referencia estándar.
  - Si no tiene equivalente, se usa el costo real del provider (`cost_input`/`cost_output` del config) para mantener comparabilidad.
  - El Executive Brief de julio muestra siempre el costo normalizado (OpenRouter o fallback), nunca $0.0000.

### Cambio en cobertura
- Umbral "tested" bajado de **≥50 runs a ≥20 runs**.
  - Motivo: no ocultar modelos emergentes con datos sólidos (por ejemplo Gemma 4 31B con 22 runs).
  - `tested_count` pasa a reflejar modelos con ≥20 runs en `docs/data/models.json`.

### Artefactos regenerados
- `docs/data/models.json` regenerado con costos normalizados y piso aplicado.
- `cheatsheet/AI_Model_Benchmark_ExecutiveBrief_July_2026.pdf` + HTML regenerados con costos normalizados.

### Docs actualizadas
- `README.md`: versión 3.0.2, top-10 global actualizado, nota de normalización de costos, cobertura ≥20 runs.
- `ROADMAP.md`: checklist de julio actualizado.

## [v3.0.1] - 2026-06-26 — DiffusionGemma medido local en DGX Spark

### Benchmark nuevo
- **DiffusionGemma 26B-A4B** (`local-diffusiongemma-26b`) medido vía `llama-diffusion-cli` (llama.cpp PR #24423) en DGX Spark, quantización Q8_0.
- 103 tests (24 suites), 100 runs exitosos, score global **7.05**, posición **#25/91**.
- Mejores pilares: Agentes/Operaciones 7.76, Contenido 7.68, Razonamiento 7.67.
- Debilidad confirmada: `string_precision` 5.26 (copia exacta de credenciales/configs).
- 7 errores en `agent_long_horizon` atribuidos a ctx-size 8K; config ajustado a 262144 para próximas corridas.

### Infraestructura
- Nuevo provider `diffusion_cli` en `providers/adapters.py` (`DiffusionGemmaProvider`): ejecuta el binario por subprocess y parsea métricas/respuesta.
- Scripts auxiliares: `benchmarks/smoke_diffusiongemma.py` y `run_diffusiongemma_codegen.sh`.
- Pipeline maestro de regeneración: `benchmarks/regenerate_all.py`.

### Docs actualizadas
- `INSIGHTS.md`: insight estrella v3.0.1 sobre DiffusionGemma y comparación con Gemma 4 31B.
- `DATASHEET_2026-06.md`: reescrito con cobertura v3.0.1, ranking actualizado y hallazgo del mes.
- `README.md` y `ROADMAP.md`: counts sincronizados vía marcadores AUTO.

## [v3.0.0] - 2026-06-25 — Benchmark de Kimi K2.7 Code, unificación de scores y ajuste de pesos v3.0

### Benchmark nuevo
- **Kimi K2.7 Code** (`moonshotai/kimi-k2.7-code`) corrido vía OpenRouter: 168 tests exitosos (105 tareas prácticas + 45 NIAH-es + 18 seguridad), score global **4.77** con pesos v2.9 / **5.07** con pesos v3.0.
- Configurado como thinking model con `niah_max_context: 131072` (los tests de 256K superan el contexto real al sumar output).
- Timeout por request elevado a **600s** para acomodar thinking models lentos.

### Unificación de scores (MODELOS.md ↔ calculadora)
- `generate_modelos_md_table.py` ahora lee `docs/data/models.json` y usa el mismo `score_global` z-scoreado que la calculadora web.
- Eliminada la discrepancia donde `MODELOS.md` mostraba un promedio lineal distinto.

### Ajuste de pesos v3.0
Tras auditoría de comparabilidad, el score global ahora usa:
- **Quality: 70%** (antes 60%)
- **Costo: 15%** (antes 20%)
- **Velocidad: 7.5%** (antes 10%)
- **Latencia: 7.5%** (antes 10%)

Efecto: el ranking global deja de estar tan sesgado hacia modelos baratos/rápidos y recupera más la señal de calidad real.

### MODELOS.md: tablas por caso de uso
Además del score global, `MODELOS.md` ahora incluye tablas separadas:
- Mejor calidad pura
- Mejor coding
- Mejor razonamiento
- Mejor contenido/marketing
- Mejor relación calidad/costo (pesos v2.9 como referencia)

### Docs actualizadas
- `README.md`: versión 3.0.0, nueva tabla de pesos, top-10 v3.0, calculadora.
- `benchmarks/scoring.py`: `DEFAULT_WEIGHTS` actualizados.
- `docs/data/models.json` y `MODELOS.md` regenerados.

## [v2.9.1] - 2026-06-10 — Claude Fable 5 medido (día 1) + fix del juez remoto + rejudge.py

### Agregado
- **Claude Fable 5** al catálogo: `claude-fable-5` (OpenRouter, $10/$50 verificado vía API — 2x Opus 4.8) + `claude-fable-5-sub` (suscripción Claude Code, costo real $0, mismo cap NIAH 256K que opus-4.8-sub). Tier nuevo SOBRE Opus, adaptive thinking nativo.
- **Corrida completa de Fable 5-sub**: 176 runs, 0 errores, 26 suites, juez Phi-4 (Spark). Resultado: **quality 8.58 vs Opus 4.8 8.81 en los 162 tests compartidos** — Fable NO supera a Opus en promedio. Gana solo en `agent_long_horizon` (+1.21, el delta más grande de la tabla — exactamente su pitch). Pierde en tareas cortas de formato (multi_turn -1.22, policy_adherence -1.05, structured_output -0.98). Global composite: **#38** (el costo 2x lo hunde en un ranking cost-aware). Conclusión: pagar 2x solo se justifica para horizonte largo agéntico.
- **`benchmarks/rejudge.py`**: re-juzgado post-hoc de un results JSON cuando el juez falló — relee respuestas completas de `results/responses/`, evalúa con el preset indicado y recalcula quality/final con la fórmula exacta del runner (30/70). Backup `.pre-rejudge`. Escribe `judge_score` (0-5) compatible con `export_for_pages`.
- **Preset de juez `phi4-spark`**: Phi-4 vía Ollama del DGX Spark (LAN) — mismo modelo/rúbrica que `phi4` local, para máquinas sin phi4 descargado.

### Arreglado
- **Bug del juez con presets remotos** (`llm_judge.py`): el path Ollama hardcodeaba `localhost:11434` e ignoraba el `base_url` del preset → con `phi4-spark` el juez le pegaba al Ollama local sin phi4, recibía `{"error": "model not found"}` y **caía en silencio al score automático en el 100% de los tests**. Detectado auditando scores bajos sospechosos de Fable en `hallucination` (la respuesta era casi perfecta y el auto-scorer la castigaba por formato/concisión). Con juez real: context_faithfulness 5.7→8.2, news_no_hallucination 3.8→6.8. Las corridas previas (Opus 4.8 etc.) no se vieron afectadas — corrieron donde phi4 sí estaba en localhost.

### Lección metodológica
- Ante un score bajo inesperado, **auditar la medición antes de creerle al número**: leer la respuesta guardada, verificar que el juez realmente evaluó (señal: `quality == auto_quality` en todos los tests = juez ausente), y comparar contra el mismo provider (sub vs sub, no sub vs API).

## [v2.7.1] - 2026-05-22 — Catálogo: modelos Grok + suscripción xAI SuperGrok

### Agregado al catálogo (config, PENDIENTE de benchmark)
IDs y precios verificados vía la API pública de OpenRouter (`/api/v1/models`), no aggregators.
- **Grok 4.3** (`x-ai/grok-4.3`, $1.25/$2.50, 1M ctx) — flagship xAI del 30 abr 2026.
- **Grok 4.20 Multi-Agent** (`x-ai/grok-4.20-multi-agent`, $2.00/$6.00, 2M ctx) — variante multi-agente (equivalente "Heavy"; no existe un ID literal `grok-4-heavy` en OpenRouter).
- Pricing añadido a `scoring.py` para ambos.
- Catálogo: 113 → 115 modelos. Quedan `tested=false` hasta correr el runner (requiere `OPENROUTER_API_KEY`; no disponible en el entorno remoto de esta sesión).

### Suscripción
- **xAI SuperGrok** ($30/mes, $300/año) agregada a `SUBSCRIPTIONS`. Siguiendo el precedente de `anthropic_pro`: es plan **consumer sin API access**, así que NO se enlaza a ningún modelo (los Grok se miden vía OpenRouter pay-as-you-go). Listada en README "Modelos en suscripción mensual" y en `subscriptions_catalog` de la calculadora. Nota: Grok 4.3 + multi-agente requieren SuperGrok Heavy $300/mes.

### Hallazgo
- OpenRouter ya **no lista `grok-4.1-fast`** (delistado/renombrado; conserva sus resultados históricos en el ranking) y **no existe `grok-4.1` full** en OpenRouter → no se pudo agregar la versión completa de 4.1 pedida. Documentado en ROADMAP.

## [v2.7.0] - 2026-05-22 — Rescore de costo provider-aware (el costo por fin discrimina)

### Cambio de metodología
Tras la corrección de precios (v2.6.3) se detectó que el costo histórico de la **mayoría** de modelos se había guardado con el fallback `(1.0,3.0)` de `PRICING` (muchas corridas previas a que el modelo entrara al dict) → casi todos con `cost_score ≈ 7.0` → **la dimensión costo (20% del peso) era casi inerte** y el ranking de facto solo-calidad.

Decisión del usuario: aplicar **rescore provider-aware TOTAL**. `benchmarks/rescore_costs.py` (sin `--only`) recalculó cost_usd/cost_score/final de **7.483 runs** usando el precio por-proveedor del config (`models.py`) × tokens reales. Solo cambian campos derivados de precio (verificado: 0 cambios fuera de cost_usd/cost_score/final en 11.013 runs comparados).

### Efecto en el ranking (reordenamiento grande, esperado)
- **Suben** los gratis/NIM/local y open-source baratos: Devstral Small (ahora **#1**, 7.84), Nemotron Omni NIM, Qwen 3-Next NIM, Gemma, Devstral 2 123B NIM, Llama Groq. Deltas de +0.3 a +1.15 (DeepSeek V4 Cloud +1.15, Nemotron NIM +0.86).
- **Bajan** los premium caros: Gemini 2.5 Pro −0.49, GPT-5.4 −0.47, Sonnet 4.6 −0.25, Opus 4.x. Opus 4.7 pasa a **#66/72**.
- Nuevo top-5 global: Devstral Small · Nemotron 3 Nano Omni (NIM) · Qwen 3-Next 80B (NIM) · Gemini 2.5 Flash Lite · Llama 4 Scout (Groq).

### Caveat documentado
- El tier gratis NIM ($0/call) tiene rate-limit 40 RPM: gran C/B para volumen bajo-medio, no necesariamente para alto throughput. README y calculadora lo marcan.

### Docs actualizadas
- README (top-10 v2.7, cobertura, framing de Opus, nota de provider), models.json + MODELOS + per-model MDs regenerados, INSIGHTS con callout v2.7 (tablas detalladas pendientes de regen por data-scientist).

## [v2.6.3] - 2026-05-22 — Corrección de precios verificada (OpenRouter API) + costeo provider-aware

### Precios corregidos (verificados vía OpenRouter `/v1/models`)
Se detectó que varios precios del catálogo estaban stale (pricing viejo copiado) y que `models.py` y el `PRICING` de `scoring.py` tenían drift. Corregidos en ambos:

| Modelo | Antes | Ahora (OpenRouter) |
|---|---|---|
| Claude Opus 4.7 (+thinking) | $15/$75 | **$5/$25** |
| Claude Opus 4.6 | $15/$75 | **$5/$25** |
| DeepSeek V4 Pro (OpenRouter) | $1.74/$3.48 | **$0.435/$0.87** (tier medium→cheap) |
| DeepSeek V4 Flash (OpenRouter) | $0.14/$0.28 | $0.112/$0.224 |
| Kimi K2.6 (+thinking) | $0.80/$3.50 (scoring $1.50/$9) | **$0.73/$3.49** |
| Grok 4.20 | $2/$6 | **$1.25/$2.50** |
| Qwen 3.6 Plus | $0.33/$0.65 | **$0.18/$1.07** |

### Costeo provider-aware
- `estimate_cost(model, in, out, prices=...)` ahora acepta el precio por-entrada del config (provider-specific); `PRICING` queda solo como fallback. El runner pasa `(cost_input, cost_output)` del `model_config` en cada corrida. Arregla la ambigüedad de costear por `id` (un mismo id en NIM gratis vs OpenRouter pago se costeaba igual).
- Nuevo `benchmarks/rescore_costs.py`: re-scorea cost_usd/cost_score/final del histórico desde el config (fuente única), sin re-correr. `--only "n1,n2"` para scoped; sin flag = total.

### Re-score aplicado (scoped a los 9 verificados, 1.072 runs)
- Opus 4.6 −0.47, Opus 4.7 −0.33 (estaban **sub-costeados** con el fallback `(1.0,3.0)`), Qwen 3.6 Plus +0.34, DeepSeek V4 Pro +0.26, Grok 4.20 +0.19, Kimi K2.6 ≈0. Top-10 global sin cambios (ninguno de los 9 estaba ahí).
- Solo se tocaron campos derivados de precio (cost_usd, cost_score, final); quality/tokens/respuestas intactos.

### Hallazgo mayor (pendiente de decisión, ver ROADMAP)
- El costo histórico de la **mayoría** de modelos se guardó con el fallback `(1.0,3.0)` → casi todos con `cost_score ≈ 7.0` → **la dimensión costo (20%) ha sido casi inerte**. Un rescore provider-aware TOTAL arreglaría esto pero reordena todo el ranking (gratis/NIM suben, premium bajan). No aplicado — decisión nivel v2.7.

## [v2.6.2] - 2026-05-07 — Validación de hipótesis sección 12 INSIGHTS

### Hallazgos validados (no nuevos benchmarks, validación cualitativa de los anteriores)

- **Devstral 2 123B (NIM) — DEPRECADO POR PROVIDER**: re-run intentado falla con cascada de error 400 en 29/29 tests. NIM ya no soporta Devstral 2 en mayo 2026 (funcionaba en abril con 68/91 cobertura). Score 7.16 queda **frozen y no re-validable** desde NIM. Nueva implicación documentada: provider stability matters month-to-month.

- **GPT-5.5 — NO MEDIBLE CON ESTA METODOLOGÍA**: experimento con `THINKING_MIN_TOKENS=16384` (vs 8192 default). Smoke OK pero en bench real cada test toma 16-50 min, ETA 181h para 223 tests. Killed tras 12/223 en 9h25min. GPT-5.5 es OVER-thinking — single-shot benchmark no es metodología adecuada. **Revertido a 8192** con comentarios explicativos en `providers/adapters.py`. Score 6.07 queda **provisorio y no comparable**.

- **Opus 4.7 NIAH-ES — REFUSAL PATTERN, no paráfrasis**: auditoría manual de 5 respuestas refuta hipótesis "paráfrasis" (Opus extrae texto exacto cuando responde). Confirma nueva hipótesis: **refusal-prone en credentials/secrets** (test `api_key` scoreó 3.04 por refusal completo). Phi-4 además puede penalizar caveats de seguridad que Opus añade a respuestas correctas (ssh_port, budget). Bottom de Opus en NIAH-ES NO refleja debilidad de retrieval — refleja safety + verbosity penalty.

### Cambios al código
- `providers/adapters.py`: `THINKING_MIN_TOKENS` mantiene 8192, agregado bloque de comentarios documentando el experimento de mayo 7 y la conclusión.

### Cambios a documentación
- `INSIGHTS.md` secciones 12.1, 12.2, 12.5 actualizadas con outcomes validados (vs hipótesis abiertas anteriores).

### Validados también este día (cierre completo de próximos pasos)

- **Llama 4 Maverick Groq direct — NO TESTEABLE**: catálogo Groq confirmado vía API solo tiene Scout 17B, NO Maverick 128E. El +0.56 entre Scout (Groq, 7.69) vs Maverick (OpenRouter, 7.13) NO es atribuible cleanly a provider — son modelos distintos. Sin keys de Together/Fireworks/DeepInfra configuradas. INSIGHTS sección 12.3 reformulada.

- **Variance intra-model análisis — EJECUTADO**: 5 modelos × 5 prompts × 5 reps = 124 runs OK (1 mistral falló empty response). Script `benchmarks/variance_analysis.py`, data `benchmarks/results/variance_20260513_075505.json`. Hallazgos clave:
  - Razonamiento/contenido/NIAH-ES son muy estables run-to-run (stdev ≤ 0.5, mayoría stdev=0.000).
  - **Coding** tiene varianza alta en devstral (stdev 1.145, range 2.80) y llama-3.1-8b (stdev 1.095).
  - **Agentes** es el pilar más inestable: 4/5 modelos con stdev 0.4-1.0.
  - Diferencias <0.3 puntos en ranking top 5 son **indistinguibles estadísticamente** con N=1 single-shot.
  - Phi-4 como juez es consistente: respuestas similares → mismo score exacto.
  - NIAH-ES uniformemente bajo en top 5 (~3.0 todos) con stdev mínimo → ranking NIAH-ES global es robusto.
  - INSIGHTS sección 13 nueva con tabla completa y caveats.

### Pendiente para próxima iteración
- Variance expansion a top 10-15 (tier medio puede tener varianza mayor).
- Variance a temperatura 0 para validar que stdev intra-pilar → 0.0 en todos los pilares.

## [v2.6.1] - 2026-05-04 — CheatSheet PDF refactor (data-driven, 10 páginas, QR codes)

### Refactor del cheatsheet PDF
- Nuevo script `cheatsheet/generate_cheatsheet.py` (data-driven desde models.json)
- Script viejo movido a `cheatsheet/generate_pdf_deprecated.py`

### Cambios visuales/contenido
- **"Mayo 2026" destacado** en cover con color magenta + glow + borde
- **Mes en español** (Mayo en lugar de May vía dict explícito)
- **10 páginas** organizadas por valor descendente:
  1. Cover · 2. Hallazgos clave · 3. Top 10 · 4. Recomendaciones · 5. Rankings categoría
  6. Precios y suscripciones · 7. Estrategia local · 8. Proveedores · 9. Metodología · 10. CTA + QR

### Fixes específicos del feedback de usuario
- ✅ Página 2 vacía eliminada (refactor de page-breaks)
- ✅ "Mayo 2026" prominente en cover (magenta + glow)
- ✅ Hallazgos con fechas individuales (28 abr, 29 abr, 30 abr, 1 mayo, 3 mayo, etc.)
- ✅ Sección "Que medimos" actualizada con suites nuevas: agent_long_horizon (multi-step) + NIAH-ES (aguja en pajar)
- ✅ Latencia confirmada en sección metodología (sí se mide)
- ✅ Suscripciones incluyen MiMo Xiaomi $14/mes (era omisión crítica)
- ✅ Estrategia local generalizada por VRAM/RAM disponible (no solo DGX Spark)
- ✅ Mapa de proveedores actualizado (10 providers: NIM, Local, Xiaomi, MiniMax, Ollama Cloud, Groq, OpenRouter, OpenAI, Anthropic, Google)
- ✅ Página final CTA con QR codes a calculadora + comunidad Skool
- ✅ "Guiños" al repo/calculadora en cada sección

### QR codes embebidos
- QR principal: https://benchmarks.cristiantala.com/ (calculadora interactiva)
- QR comunidad: https://www.skool.com/cagala-aprende-repite/about (Cágala, Aprende, Repite)
- Generación con qrcode[pil] (`pip install "qrcode[pil]"`)

### Convención release mensual
Cada 1ro de mes: regen models.json + INSIGHTS update + DATASHEET nuevo + PDF cheatsheet + tag semver.

## [v2.6.0] - 2026-05-03 — NIAH-ES extension + GPT-5.5 completo + DeepSeek V4 family + datasheets

### Cobertura mayo
- 72 modelos con ≥50 runs single-turn (era 70)
- 49 modelos con runs en agent_long_horizon (era 38)
- 21 modelos con runs en NIAH-ES (era 8)
- ~9,500+ runs preservados (era 8,475)

### Lotes mayo (3 mayo)
- GPT-5.5 completar: 57/57 OK (12 agent_long_horizon + 45 niah_es_lite)
- NIAH-ES extension lite: 9 modelos × 45 = 405/405 OK
- DeepSeek V4 family: V4 Pro Cloud 55/57, V4 Flash Cloud 57/57, V4 Pro NIM 0/7 (descartado), V4 Pro OpenRouter 57/57 OK

### Suite niah_es_lite (nueva)
45 tests sin contexto 256K (5 needles × 3 ctx 4K-64K × 3 pos). Para correr más modelos sin el costo del 256K cap. Decisión user 3 mayo.

### Datasheets mensuales
- DATASHEET_2026-04.md (snapshot retroactivo abril)
- DATASHEET_2026-05.md (estado mayo + comparación vs abril)
Convención mensual establecida: cada 1ro de mes datasheet con cambios vs anterior.

### Disclaimer "complemento, NO sustituto" en 7 docs principales
README, INSIGHTS, NIAH_ES_DESIGN, THINKING_EXPLAINED, BENCHMARKS_EXTERNOS, NIAH_CROSSREF, calculadora (docs/index.html). Posicionamiento: complementarios a HumanEval/MMLU/GSM8K/SWE-bench/NIAH inglés/MT-Bench, NO los reemplazamos.

### Tooling
- benchmarks/commit_model_results.sh (nuevo): commits incrementales por modelo terminado en lugar de esperar al final del lote. Política de publicación inmediata desde 3 mayo.

### Hallazgos confirmados o nuevos
- DeepSeek V4 Pro NIM no funciona en producción (cascada 504 reproducible 2x).
- DeepSeek V4 Pro/Flash Ollama Cloud sub funciona estable (>97% OK).
- DeepSeek V4 Pro OpenRouter funciona pero es caro ($1.74/$3.48 per M).
- Devstral Small mantiene #1 en NIAH-ES con 17 modelos cubiertos (vs 8 abril).
- Cambio metodológico: ranking compuesto ahora integra NIAH-ES — modelos con NIAH corrido tienen score promedio ligeramente menor.

## [v2.5.2] - 2026-05-01 — NIAH-ES v3 1M context + cross-ref con literatura

### Suite niah_es_1m (variante 1M context)
- 4 modelos × 15 tests (5 needles × 1M × 3 pos) = 60 runs
- HALLAZGO BRUTAL: solo 1 de 4 modelos procesa 1M tokens efectivamente

| Modelo | Declared | Tests OK | Score 1M | Causa |
|---|---|---|---|---|
| GPT-4.1 | 1M | 15/15 ✅ | 4.91 | Único que cumple |
| Llama 4 Scout 17B Groq | 10M | 0/15 ❌ | — | Groq preview cap 131K |
| DeepSeek V4 Flash NIM | 1M | 0/15 ❌ | — | NIM cap ~128K |
| Gemini 3.1 Pro | 1M | 0/15 ❌ | — | OpenRouter cap |

GPT-4.1 a 1M score 4.91 — idéntico a su 256K. NO degrada al duplicar
context. Valida effective 1M de OpenAI.

3 de 4 providers capan el context declarado. "1M context" solo aplica
si el modelo tiene capacidad arquitectural Y el provider expone
completa. En 4/2026, para context >256K en producción con estos
modelos via providers populares, GPT-4.1 vía OpenAI directo / OpenRouter
es la única opción confirmada.

### Cross-reference con literatura NIAH inglesa (NIAH_CROSSREF.md)

12 fuentes oficiales citadas: Gemini 1.5/2.5/3 paper, GPT-4.1
announcement, Anthropic system cards, DeepSeek V4 Pro paper, Llama
3.3/4 reports, Mistral Inspect Evals UK BEIS.

Hallazgos del cross-ref:
1. Ranking inglés ≠ ranking NIAH-ES. Frontier reportan 99-100% en
   inglés. Devstral/Mistral lideran NIAH-ES — coherente con
   entrenamiento multilingüe europeo.
2. Opus 4.7 último (4.98) CONSISTENTE con literatura reciente:
   Anthropic mismo reporta degradación en MRCR multi-needle de Claude
   4.x family. Validación cruzada.
3. Llama 4 Scout > Llama 3.3 70B respeta ranking oficial Meta
   (98% @10M vs 97.5% @128K).
4. Mistral Small / Devstral: APORTE ÚNICO. NO publican NIAH oficial.
   NIAH-ES es primer benchmark público con número concreto.
5. Limitaciones: idioma (literatura toda inglés), métrica (binaria
   vs 0-10), variantes (single vs MRCR mezcladas).

### Cobertura post-v3
- 8 modelos con datos NIAH-ES v2 (60 tests cada uno = 480 runs)
- 1 modelo con datos NIAH-ES 1M (GPT-4.1, 15 tests)
- 540 runs NIAH-ES totales preservados

## [v2.5.1] - 2026-04-30 (PM) — NIAH-ES v2 full grid (5 needles × 60 tests, 480 runs)

### Lote NIAH-ES v2 — datos consolidados con N=5

8 modelos × 60 tests (5 needles × 4 ctx × 3 pos) = 480 runs en 43min.
Costo: ~$50 OpenRouter.

Ranking v2 confirma v1:
1. Devstral Small — 7.25 ⭐
2. Mistral Small 4 — 7.06
3. Llama 4 Scout 17B Groq — 6.89
4. Llama 3.3 70B Groq — 6.26
5. Gemini 3.1 Pro — 5.96
6. DeepSeek V4 Flash NIM — 5.92
7. GPT-4.1 — 5.86
8. Claude Opus 4.7 — 4.98 (último, robusto con N=5)

### CORRECCIÓN HONESTA: lost-in-the-middle severo de v1 era ARTEFACTO N=1

v1 reportaba "Opus 4.7 cae -3.0 puntos al 50% del 4K". Con 5 needles
promediados (v2), el delta máximo entre 25%/50%/75% es 0.04-0.21
puntos en TODOS los modelos. NO hay lost-in-the-middle severo en
español neutro con estos modelos top.

Lección metodológica: N=1 puede generar patrones fantasma.
Para hallazgos publicables N≥5 es mínimo. v1 sirvió de validación
de la suite, NO de hallazgo definitivo.

### Lo que SÍ es robusto con N=5

1. **Devstral Small ($0.10/$0.30) supera a Opus 4.7 ($45/M) por +2.27
   puntos en NIAH a 1/450 del costo**.
2. **Gemini 3.1 Pro es el más estable a 256K** (5.37 vs Opus 4.53 /
   GPT-4.1 4.91).
3. **"1M context declarado" ≠ retrieval efectivo a 256K**. Solo 3/8
   modelos procesan 256K sin error.
4. **Opus 4.7 sigue último** (hipótesis paráfrasis vs extraction
   exacta — pendiente inspección manual).

INSIGHTS.md sección "Update v2.5.1 NIAH-ES v2" con tabla, breakdown
por posición (sin lost-in-the-middle), análisis 256K, próximos pasos.

## [v2.5.0] - 2026-04-30 — NIAH-ES + sección "Why Opus" + suscripciones explícitas + sortable calculadora

### Suite NIAH-ES (Needle-in-a-Haystack en español neutro) — APORTE ÚNICO

**Primer NIAH público en español neutro LATAM** (suite 25 del benchmark).

- 12 tests piloto: 1 needle × 4 contextos (4K, 16K, 64K, 256K tokens) × 3 posiciones (25%, 50%, 75%)
- 5 needles distintos con elementos no-alucinables (códigos, números, fechas, identificadores)
- Corpus 9 artículos Wikipedia ES (~1.1MB / ~285K tokens) committeado al repo
- Scoring híbrido: regex `exact_patterns` (70%) + keywords semántico (30%)
- Smoke test Mistral Small 4: scores 7.3 (4K) → 6.0 (64K) → ERROR 400 (256K) — patrón esperado de degradación + falla por context overflow
- `benchmarks/regenerate_niah_test.py` para reproducibilidad: anyone puede regenerar el prompt EXACTO de cualquier test desde corpus + config
- `NIAH_ES_DESIGN.md` con diseño completo + ROADMAP de fases (smoke → piloto v1 → v2 con 5 needles → v3 cobertura completa con 1M context)

### Limitación crítica documentada — debugging agentic real

Caso real reportado (30 abril): MiniMax M2.7 (top #7 nuestro) NO pudo resolver problema técnico complejo en VPS Hetzner / contenedor OpenClaw. Opus 4.7 (fuera del top 10 nuestro) lo resolvió en minutos.

INSIGHTS.md ahora abre con sección "Limitación crítica: NO medimos debugging agentic real":
- Tabla qué mide cada benchmark (SWE-bench, Claw-Eval, Terminal-Bench, NIAH, nuestro)
- Cross-reference SWE-bench Verified con scores oficiales (Opus 4.7 #1 con 87.6%)
- Implicaciones honestas: cuándo confiar en nuestro ranking vs cuándo NO

ROADMAP: nueva suite `agentic_debugging` agendada (5-10 tests bug real con stubs detallados, ETA 1 semana, $30-50). Considera usar caso real del usuario como piloto 1.

### Catálogo de suscripciones explícito

Modelos con `cost=0` ya NO son ambiguos. Nuevo dict `SUBSCRIPTIONS` en `benchmarks/models.py`:
- Ollama Cloud Pro $30/mes (5 modelos)
- Xiaomi MiMo Standard $14/mes (4 modelos)
- MiniMax Agent Pro $19/mes (M2.7 Highspeed)
- Anthropic Pro $20/mes (informativo, web only)

11 modelos con campo `subscriptions: ["key1", "key2"]` (lista — un modelo puede estar en múltiples planes).

Calculadora muestra "★ Sub $14/mes" en lugar de genérico "★ Sub Xiaomi". Tooltip aclara: "NO es gratis — requiere pagar la sub mensual".

README sección dedicada "Modelos en suscripción mensual (NO son gratis)" con tabla de 4 planes + clarificación de qué modelos SÍ son realmente $0 (NIM 40 RPM, local hardware, pay-as-you-go).

### Calculadora — sortable + pills coloreados

- Click en cualquier header (Score, Quality, Costo, Tools, Costo/mes, C/B, tok/s) ordena la tabla
- Toggle asc/desc al re-clickear. Indicador visual ↕/↓/↑
- Pills coloreados en componentes (verde ≥7, amarillo ≥6, rojo <6) consistente con Score global
- Header "Costo↓" + tooltip explícito: "10 = gratis o muy barato, 5 = $0.01/call, 0 = $1.00+/call. Más alto = más barato"

### Documento "Why Opus 4.7 doesn't top our benchmark" + 6 hipótesis

INSIGHTS sección dedicada con datos cuantitativos:
- Phi-4 califica Opus 4.22 vs Llama 4.00 (descarta sesgo del juez)
- Output tokens 980 vs 991 (descarta verbosity)
- Opus es 40-100x más caro y 5-10x más lento — la fórmula compuesta lo penaliza por costo+speed, NO por quality

6 hipótesis cualitativas con evidencia (extracto de respuesta real Opus 4.6 en news_json_output_strict):
1. Opus es ELABORADAMENTE verboso (8 sub-secciones tipo Wikipedia vs 4-5 compactas Llama)
2. Meta-comentarios "voy a abordar esto paso a paso..." que el juez no premia
3. JSON con texto antes/después en tests con rúbrica strict
4. Estilo "asistente formal" no encaja con criterios "estilo emprendedor LATAM"
5. Posible saturación juez Phi-4 con respuestas tipo tutor universitario
6. Tests agent_capabilities favorecen ejecución directa, Opus tiende a explicar antes de hacer

### Cobertura final v2.5.0
- **70 modelos** con ≥50 runs single-turn
- **38 modelos** con ≥9 runs en agent_long_horizon multi-turno
- **NIAH-ES**: 1 modelo (smoke) + 8 modelos planeados para piloto v1
- **113 modelos** catalogados (incluye 12 variantes thinking)
- **8,475+ runs** preservados en JSONs
- **Suite count**: 23 single-turn + agent_long_horizon + niah_es = **25 suites**

## [v2.4.2] - 2026-04-30 — Lote 10 + 11/11b/11c thinking + scoring rebalanced

### Cobertura final v2.4.2
- **70 modelos** con ≥50 runs single-turn
- **38 modelos** con ≥9 runs en agent_long_horizon (multi-turno 8+ turnos)
- **8,000+ runs** preservados en JSONs
- **113 modelos** en config (era 102) con 12 variantes thinking de modelos hybrid

### Lote 10 completo (agent_long_horizon × 27 modelos = 324 runs, 17h wall-clock)
Top 10 inter-modelo agéntico:
1. GPT-OSS 120B (Ollama Cloud) — 8.15 ⭐ #1, gratis con sub
2. Llama 4 Scout 17B (Groq) — 7.86
3. Llama 3.1 8B Instant (Groq) — 7.85
4. Devstral Small — 7.77
5. MiMo V2-Omni (Xiaomi direct) — 7.75
6-10: GPT-OSS 20B, MiMo V2.5, Llama 3.3 70B, MiMo V2-Pro, Mistral Small 4

### Lote 10b MiniMax (3 modelos, 36 runs)
- MiniMax M2.7 (directo): 6.86 ⬆ provider directo
- MiniMax M2.7 OpenRouter: 6.70
- MiniMax M2.7 Highspeed (sub): 6.69 (highspeed = velocidad, NO mejor calidad)
- Provider matters reconfirmado: +0.16 directo vs OpenRouter

### Lote 11 thinking (Hermes 4 70B/405B + Kimi K2.5)
- Kimi K2.5 (thinking): 7.00 (+0.73 vs sin thinking — única excepción que SUBE)
- Hermes 4 70B (thinking): 6.70 (-0.54 vs sin)
- Hermes 4 405B (thinking): 6.30 (-0.5 vs sin)

### Lote 11b Anthropic thinking (4 modelos, 48 runs, $17.44)
- Claude Haiku 4.5 (sin thinking): 6.86 — el MEJOR de Anthropic en agéntica
- Claude Haiku 4.5 (thinking): 6.57 (-0.29)
- Claude Sonnet 4.6 (thinking): 6.47 (-0.5)
- Claude Opus 4.7 (thinking): 6.33 (-0.67)
- **Hallazgo bestial**: Haiku sin thinking ($0.029/test) > Opus thinking ($1.18/test). 40x más barato y mejor en agéntica.

### Lote 11c Gemini family + Kimi K2.6 thinking (4 modelos)
- Gemini 2.5 Flash (thinking): 7.10 (-0.09 vs sin, casi igual)
- Gemini 3.1 Flash Lite (thinking): 7.17
- Gemini 3.1 Pro (thinking): 6.50 (apenas +0.06 vs sin)
- Kimi K2.6 (thinking): 6.32

### Hallazgo robustamente confirmado: thinking forzado EMPEORA multi-turn agéntico
8 de 9 modelos hybrid empeoran con `force_reasoning=high` en agent_long_horizon vs sin thinking. Solo Kimi K2.5 sube. Hipótesis: el modelo razona demasiado por cada turn, pierde foco del usuario, se desvía del objetivo. Implicación para producción: NO activar thinking default en pipelines agente N8N/OpenClaw.

### Scoring v2.4.2 rebalanced
Pesos default cambiados:
- quality 35% → **50%** (factor #1 en decisiones reales)
- cost 15% → **20%** (presupuesto importa para emprendedor LATAM)
- tool_calling 25% → **15%** (era inflado: 83/91 tests reciben default 7.0)
- speed 5% → **7.5%**, latency 5% → **7.5%** (afectan UX de agente)
- availability 15% (hardcoded a 7.0) → **eliminado** (no discriminaba)
- Curva de cost: buckets discretos → log suave ($0.001 → 8.0, $0.01 → 5.0, $0.10 → 2.0)

### Nuevo Top 10 con scoring v2.4.2
1. Llama 4 Scout 17B (Groq) — 8.11
2. Llama 3.1 8B Instant (Groq) — 8.11
3. Llama 3.3 70B (Groq) — 7.86
4. GPT-OSS 20B (Groq) — 7.84
5. Mistral Small 4 — 7.81
6. Gemini 3.1 Flash Lite — 7.73
7. GPT-OSS 120B Cloud — 7.69
8. Grok 4.1 Fast — 7.62
9. MiMo V2.5 (Xiaomi) — 7.62
10. Devstral Small — 7.61

### Why Opus 4.7 doesn't top the benchmark
Sección dedicada en INSIGHTS.md. Opus 4.7 saca **quality 8.08** (top 6 entre todos los modelos), juez Phi-4 le da **4.22** (más alto que Llama 3.3 70B 4.00). NO es sesgo del juez ni problema de API. Lo que cambia: en el score compuesto, Opus es 40-100x más caro y 5-10x más lento → cost score 6.67 vs Llama 8.17, speed score 3 vs 9. Para emprendedor LATAM con presupuesto $500/mes, marginal +0.07 quality NO justifica 40x precio. Si solo quieres quality, ordená por columna `quality_avg`.

### Stack OpenClaw/Hermes recomendado (basado en datos)
- **Cabecera**: GPT-OSS 120B Cloud (8.15 agéntica, gratis con sub)
- **Coding**: Devstral Small (7.77 agéntica, Apache 2.0)
- **Content**: MiMo V2.5 Xiaomi sub o Gemini 3.1 Flash Lite
- **Customer support**: GPT-OSS 120B Cloud o Llama 3.3 70B Groq
- **Tool calling estructurado**: MiMo V2.5 (7.21) o Gemini 3.1 Flash Lite (7.10)

### Infraestructura
- `providers/adapters.py`: parámetro `force_reasoning` que activa `reasoning={effort:high}` + `include_reasoning=true` vía OpenRouter para modelos hybrid
- `benchmarks/runner.py`: propaga `force_reasoning` desde config
- `benchmarks/scoring.py`: nueva fórmula `compute_final_score` con pesos rebalanced + curva log de cost
- `benchmarks/export_for_pages.py`: recalcula `final` desde componentes raw para reflejar nuevos pesos sin re-correr benchmarks; expone componentes (quality/cost/speed/etc.) por modelo para que la calculadora pueda recalcular con sliders custom
- `THINKING_EXPLAINED.md`: nuevo documento que explica los 3 tipos de modelos según thinking, cómo medimos, hallazgos
- `BENCHMARKS_EXTERNOS.md`: nuevo documento con triangulación HumanEval/GSM8K/IFEval/MMLU oficiales
- `.claude/agents/agent-eval-designer.md`: nuevo sub-agent especialista en evals agénticas multi-turn

## [v2.4.1] - 2026-04-29 (PM) — Nemotron 3 Nano Omni Reasoning + DGX Lote 2 + suite agent_long_horizon

### Nuevos modelos benchmarkeados (3)
- **Nemotron 3 Nano Omni 30B-A3B Reasoning (NIM)** — 91/91, score **6.97**. Thinking + multimodal MoE 30B/3B. Lanzado 20 abril 2026 por NVIDIA. Pierde frente a Gemma 4 31B (NIM) 7.20 y Devstral 2 123B 7.12 — confirma patrón "thinking models no ayuda en single-turn".
- **Nemotron 3 Base 33B (DGX Spark Q4_K_M)** — 103/103 (incluyendo agent_long_horizon), score **6.74**. Idéntico al Nemotron 3 Super 120B también en DGX → modelo 75% más pequeño rinde igual en hardware propio Q4. Mejor C/B en local.
- **Llama 3.3 70B + Mistral Small 4** corridos en suite agent_long_horizon (12 tests c/u) para validación.

### Suite `agent_long_horizon` (12 tests multi-turno)
- 4 pilares × 3 tests c/u: context retention, skill orchestration, interruption recovery, goal persistence.
- Plantilla rígida: script de usuario pre-escrito (sin LLM dinámico haciendo de user).
- Tools simulados via stubs hardcoded (sin Docker sandbox).
- Rúbricas regex-based con 6 kinds de check, weights = 1.0 por test.
- Smoke Llama 3.3 70B Groq: 7.69 avg, varianza intra-modelo 6.4-8.3 (1.9 puntos = buena discriminación).
- Validación inter-modelo: Llama 7.50 / Mistral 7.41 / Nemotron 3 Base 33B 6.59 — la suite mantiene ranking pero con drop de ~0.15 puntos vs single-turn (mide algo diferente pero correlacionado).
- Inspirado en Claw-Eval pero adaptado al runner sin Docker.

### Sub-agent `agent-eval-designer`
- `.claude/agents/agent-eval-designer.md` — especialista en evals agénticas multi-turno.
- Workflow para generar tests, refinar rúbricas, validar discriminación.
- Generó los 9 tests fase 2 de la suite agent_long_horizon en una pasada batch.

### Runner extension
- `run_multi_turn_script()` — N llamadas en cadena con historial completo.
- `_score_long_horizon()` — aplica rúbrica con 6 kinds de check.
- `evaluate_result()` dispatcheado por `test["type"] == "multi_turn_script"`.

### Cobertura final v2.4.1
- 70 modelos con ≥50 runs (antes 68)
- 7,958 runs totales (antes 7,725)
- 102 modelos en config (antes 99)

## [v2.4.0] - 2026-04-29 — Lote 9 NIM + DGX Spark Lote 1

### Cobertura
- **68 modelos con ≥50 runs** (antes 61), **7,725 runs** ejecutados (antes 7,223), 99 modelos en config (antes 88).
- **Lote 9 NIM** completado: 1,358 runs, 117 errores. Top 3 NIM: 🥇 Gemma 4 31B (NIM) 7.20 — 🥈 Nemotron Nano 9B v2 (NIM) 6.91 — 🥉 GLM 5.1 (NIM) 6.79.
- **DGX Spark Lote 1** completado: Gemma 4 31B Q4_K_M (89/91 = 6.84) + Nemotron 3 Super 120B Q4_K_M (90/91 = 6.74). 9-18 tok/s sostenido en hardware propio.
- **Hallazgo Gemma 4 31B**: NIM 7.20 vs DGX Q4_K_M 6.84 = -0.36 puntos por cuantización. Sigue siendo competitivo para correrlo local sin pagar.
- **Magistral Small (NIM) descartado**: error 400 instant en 91/91 — modelo rechaza algún parámetro en el adapter.
- **DeepSeek V4 Pro (NIM) descartado**: 502/504 timeouts en NIM gateway con prompts largos. Funciona bien via Ollama Cloud (smoke test confirmado).

### Sincronización de docs (#desync)
- **`benchmarks/sync_doc_counts.py`** (nuevo) — script preventivo que lee `docs/data/models.json` (single source of truth) y reescribe counts (X modelos, X+ tests, X lotes) en README, AGENTS, INSIGHTS, ARQUITECTURA, MODELOS, agentes y landing pages SEO. Excluye blogs y CHANGELOG (históricos dated).
- **Agregado a la regla de auto-generación** en `CLAUDE.md` como paso 6.
- **30+ referencias desactualizadas** corregidas en una sola pasada (53→68, 5K→7K tests, 7→16 lotes, 45 modelos × 91 → recalculado).

### Refactor export
- `export_for_pages.py` ahora hace merge de `MODELS` (cloud) + `OLLAMA_MODELS` (locales DGX/Mac) → los DGX models aparecen en la calculadora.
- Total catálogo: 99 modelos (antes 88).

### Capability flags
- `_infer_capabilities()` en `export_for_pages.py` infiere `tool_calling`, `thinking`, `multimodal` por modelo desde patterns conocidos. Permite override manual en config.
- Calculator UX: filtros por capability con guía colapsable de 6 categorías + cards semánticos.

### Calidad calculadora (UX)
- Sub-categorías cascade: 4 pilares × 23 suites con dropdown que se expande al elegir tarea.
- Presets: Personal/Solopreneur/Pyme/Producción con preset de defaults razonable.
- Costo-Beneficio columna con badges semánticos (Excelente/Bueno/Aceptable/Caro/Gratis-contextual).
- Free labels específicos por provider: ★ NIM 40rpm / ★ Sub Ollama / ★ Sub Xiaomi / ★ Local / ★ Sin pago.
- Default budget=500, calidad=6.5, sin límite de resultados.
- WCAG AA touch targets, cache busting via `?v=YYYYMMDDx`.

## [Unreleased] - 2026-04-25 (continúa)

### NVIDIA NIM provider (#19)
- Provider `nvidia_nim` agregado al runner. Base URL `https://integrate.api.nvidia.com/v1` (OpenAI-compatible).
- Free tier 40 RPM = perfecto para benchmarks secuenciales (cada test ~5-30s, no excede el límite).
- `NVIDIA_NIM_API_KEY` en `.env`, smoke test OK con Nemotron Super 49B v1.5 (8.3s para "hola").
- 135+ modelos en el catálogo. 8 agregados al config (claves `nim-*`):
  - `nim-nemotron-super-1.5` (versión v1.5 del Nemotron Super que ya medimos)
  - `nim-nemotron-ultra-253b` (más grande de la familia)
  - `nim-qwen3-next-instruct` y `nim-qwen3-next-thinking` (Qwen 3-Next 80B, próxima gen)
  - `nim-mistral-nemotron` (colab Mistral × NVIDIA)
  - `nim-kimi-k2-thinking` (variante thinking del K2 — comparar con K2.6)
  - `nim-deepseek-v4-flash` (mismo modelo que OpenRouter, comparar latencia/calidad)
  - `nim-qwen3.5-397b` (mismo Cristian usa en producción via Ollama Cloud — comparar)
- 8 nuevos modelos = potencial de 8 × 91 = 728 tests gratis en próximo Lote 6.

### Agregado
- **`OpenAIResponsesProvider`** en `providers/adapters.py` — soporta el endpoint `/v1/responses` de OpenAI requerido por `gpt-5.5-pro` y `o1-pro`. Estos modelos NO funcionan en `/v1/chat/completions` (404 en 58/58 tests del Lote 4).
- Mapping de `messages` → `instructions` (system) + `input` (user concatenado).
- Captura `reasoning_tokens` separados en `result.metadata` cuando el SDK los expone (`usage.output_tokens_details.reasoning_tokens`).
- Smoke test con `gpt-5.5-pro` "Di solo hola": 15 input + 46 output + **39 reasoning** tokens. Confirma cuantitativamente que el reasoning interno de pro models es ~85% del costo facturado.
- Provider key `"openai_responses"` en config para rutear modelos a este endpoint.
- `gpt-5.5-pro` ya no está bloqueado para correr en lotes futuros.

### Documentación de costos honesta (`Lo que te ahorras` en README)
- `PRICING` dict en `scoring.py` ampliado: agregados Anthropic (Claude Opus/Sonnet/Haiku 4.x), Kimi K2/K2.5/K2.6, Mistral Large, Llama 4 family, Qwen 3.6 Plus, MiniMax, DeepSeek V4 Flash/Pro, DeepSeek R1, gpt-oss 20/120B. Corregidos GPT-5.4/5.4-mini/5.5 con tarifas reales.
- Recálculo: $14 → $48 sobre runs preservados (antes Claude/Kimi caían en fallback `(1.0, 3.0)`).
- Documentadas 4 categorías de costo invisible: iteración de metodología, vacíos facturados, timeouts cobrados, retries.
- Dashboard real OpenRouter: $100+ acumulado al cierre de v2.2.1 (vs los $48 calculados — diferencia es la iteración pre-tracking no preservada en JSONs).

### Reglas y estándares
- **Corte "Solo Alternativas"** ahora excluye también modelos Google propietarios (Gemini Flash/Flash-Lite/Pro). Sí permite open-source de Google (Gemma). Tabla del README reducida de 20 a 17 modelos. Documentado en `CLAUDE.md` y `ROADMAP.md`.
- **Estándar de no re-medir** en `CLAUDE.md`: re-correr SÓLO si versión nueva del modelo, suites/tests cambiados, bug del runner, o cambio visible del proveedor. NO por refactors/cosméticos.

### Inventario y documentación pública
- **`MODELOS.md`** (nuevo) — inventario único de cobertura: 28 probados + 20 en config sin probar + ~10 mercado por agregar. Plan Lote 6 priorizado.
- **`TESTS.md`** (nuevo, auto-generado) — 91 tests en 23 suites con prompt + criterios visibles. Script `benchmarks/generate_tests_md.py` para regenerar tras agregar/cambiar tests.
- **`benchmarks/calculate_costs.py`** (nuevo) — calcula costos reales sumando todos los JSONs y recalculando con `PRICING` actual. Comando `--markdown` para tabla pegable.

### DeepSeek V4
- Agregados al config: `deepseek-v4-flash` (0.14/0.28, 284B params, 1M context) y `deepseek-v4-pro` (1.74/3.48, 1.6T params, 1M context). IDs verificados via OpenRouter.

### Recovery 402 (post-saldo bajo OpenRouter)
- Detectado: thinking models con `max_completion_tokens=8192` requieren reserva worst-case ~$74/request. Con saldo bajo, OpenRouter rechazó con 402 todos los Kimi K2.6 (47 + 9 = 56 tests + 1 GLM-5.1).
- Tras recarga del usuario: `--rerun-failed` recupera los runs sin afectar los exitosos. Recovery 1 (GLM-5.1, 1 test) y Recovery 2 (Kimi K2.6 Lote 3, 9 tests) completados. Recovery 3 (Kimi vs Opus, 47 tests) en curso.

## [2.2.1] - 2026-04-25 (post-Lote 3 / Lote 4 GPT-5.5)

### Por que v2.2.1
- Auditoria sistematica de empty responses revelo 165+ runs con `success=True` y `content=""` distribuidos en 4 lotes. Detectada raiz: thinking models agotando max_tokens en reasoning interno.
- 6 timeouts de GPT-5.5 a 181s causados por httpx read_timeout=60s × 3 retries.
- GPT-5.5 Pro inservible en chat/completions (404), requiere endpoint Responses.

### Mejorado (`providers/adapters.py`)
- **Constantes a nivel de modulo** para que el estandar este visible y editable sin tocar la logica:
  - `THINKING_MODELS`: tupla de prefijos (gpt-5*, o1*, o3*, glm-5*, kimi-k2.6, nemotron*)
  - `FIXED_TEMP_MODELS`: tupla de modelos que solo aceptan temperature=1.0
  - `THINKING_TOKEN_MULTIPLIER = 4` (era hardcoded)
  - `THINKING_MIN_TOKENS = 8192` (piso absoluto para thinking)
  - `HTTP_READ_TIMEOUT_S = 240.0` (era 60.0)
- Adapter omite `temperature` para FIXED_TEMP_MODELS para evitar HTTP 400.
- Adapter usa `max_completion_tokens` en thinking models y aplica el multiplicador automaticamente.

### Resultados Lote 4 (GPT-5.5)
- GPT-5.5 score final: **6.42** (era 5.76 antes del fix de max_tokens, antes de eso quedaba `content=""` por agotar budget razonando).
- 6 tests strategy/workshop/creativity recuperados con scores 6.3-6.7 tras subir HTTP_READ_TIMEOUT a 240s.
- 10 tests tool_calling/customer_support/orchestration/agent siguen empty: bug cosmetico #23 (content=None cuando hay tool_calls), no afecta el scoring.
- GPT-5.5 Pro: 58/58 tests fallaron con 404. Requiere endpoint Responses API. Excluido del benchmark hasta task #21.

### Documentado (este commit)
- README.md: tabla de "Estandar del benchmark para thinking models" con las 7 constantes, sus valores y razones (nivel etiqueta).
- CLAUDE.md: misma tabla mas explicacion de cuando editar cada constante.
- DESCUBRIMIENTOS.md: seccion "Lote 4 + Hallazgos tecnicos" con
  - Cost multiplier de thinking models (3-4× facturacion real)
  - Audit de 165+ runs vacios por agotar max_tokens
  - Patron 8-empty = bug cosmetico de tool_calling
  - HTTP read_timeout 60s vs 240s
  - FIXED_TEMP_MODELS rechazo de temperature distinta de 1.0
  - GPT-5.5 Pro endpoint Responses (404 en chat/completions)
  - Atomic incremental save: 10.5h perdidos en Lote 1 sin checkpoint
  - Qwen 3.6 Plus marcado proprietary (no open-source)

## [2.2.0] - 2026-04-25

### Por que v2.2 (Lote 3 + 10 modelos nuevos)
- Lote 3 con juez Phi-4 (10 modelos × 91 tests = 910 runs). Total acumulado: **27 modelos × 91 tests = 2457 runs evaluados**. Ranking global re-calculado.
- 3 cortes en README: global, sin Anthropic/OpenAI, **solo open-source** (nuevo).

### Resultados destacados Lote 3
- **Devstral Small mantiene #1 (7.35)** tras agregar 10 modelos.
- **Devstral 2 (dic 2025) entra #5** pero NO supera al Small original.
- **Gemma 4 26B sorprende #10** — open-source pequeño compitiendo con Claude Opus.
- **MiMo-V2-Pro decepciona #20** — el flagship Xiaomi rinde MENOS que MiMo-V2-Flash (#6).
- **GPT-5.4 #14 vs GPT-5.4 Mini #2** — el Mini supera al grande.
- **Gemini 2.5 Pro #25** — el flagship Google rinde peor que su propio Flash Lite.
- **Kimi K2.6 ÚLTIMO #27 (5.76)** — peor que K2 original.
- **Mistral Nemo aceptable #21 ($0.02/$0.02)** — baseline ultra económico.

### Tiempo invertido (todos los lotes desde abril 11)
| Concepto | Wall-clock |
|---|---|
| Pre-v2.1 (16 sesiones abril 11-15) | ~12 h |
| Kimi K2.6 vs Claude (abril 22) | 2.9 h |
| Agent capabilities 13 modelos (abril 22) | 0.5 h |
| Lote 1 PERDIDO sin checkpoint (704/728) | 10.5 h |
| Lote 1 v2.1 oficial (728 runs) | 7.0 h |
| Lote 2 v2.1 (819 runs) | 14.0 h |
| Lote 3 v2.2 (910 runs) | 17.7 h |
| **Total** | **≈ 65 h wall-clock** |

3515 runs ejecutados (2811 guardados, 704 perdidos en Lote 1 sin checkpoint), equivalentes a 8 jornadas laborales o 2.7 días de cómputo continuo. No incluye refactors del runner, investigación, ni documentación.

### Documentado
- README v2.2 con 3 cortes de ranking + tabla por categoría con 27 modelos
- Mejor por categoría re-calculado con los 10 nuevos
- Recomendaciones por caso de uso actualizadas

## [2.1.1] - 2026-04-23 / 2026-04-24

### Agregado
- **MDs navegables por modelo** en `benchmarks/results/per-model/` (17 archivos + index README). Cada MD tiene resumen global, tabla por pilar/suite, tests expandibles con judge score y preview de respuesta. Directamente auditable desde GitHub, sin infra.
- **Script `benchmarks/generate_per_model_md.py`**: regenera los MDs desde los JSON sin re-correr tests. Acepta `--inputs` para consolidar varios lotes.
- **Log del runner mejorado**: cada línea muestra progreso global + nombre corto del modelo + progreso local por modelo (N/91) + suite/test + descripción corta del test + elapsed total + ETA basado en promedio móvil de últimos 20 tests.
- **Devstral Medium** (`mistralai/devstral-medium`, $0.40/$2.00, Apache 2.0) y **Devstral 2** (`mistralai/devstral-2512`, $0.40/$2.00, Apache 2.0) agregados al config. Pendiente: correr benchmark en Lote 3.
- **Provider Ollama Cloud**: nuevo `UnifiedProvider("ollama_cloud", ..., "https://ollama.com/v1")` en runner. Activar con `OLLAMA_CLOUD_API_KEY` en config.py (crear key en https://ollama.com/settings/keys). Modelos con `"provider": "ollama_cloud"` rutean al endpoint cloud. `config.example.py` incluye ejemplos: `qwen3.5:397b-cloud` (el que Cristian usa en prod para ecosistemastartup.com), `qwen3.5:cloud`, `gpt-oss:120b-cloud`.
- **Lote 3 en curso** (arrancado 2026-04-24): 10 modelos × 91 tests = 910 runs. Modelos: devstral-medium, devstral-2, gpt-5.4, mimo-v2-pro, gemini-flash, gemini-pro, kimi-k2.6, claude-opus-4.6, gemma-4-26b, mistral-nemo.
- **Migración a `.env`**: todas las API keys (OPENROUTER, OPENAI, MINIMAX, OLLAMA_CLOUD) ahora viven en `.env` gitignored en lugar de hardcoded en `config.py`. Usa `python-dotenv`. `.env.example` committed como template. `config.py` y `config.example.py` sólo definen dicts (MODELS, OLLAMA_MODELS) y leen keys via `os.getenv()`.
- **Regla de 3 cortes en README**: al actualizar rankings mantener siempre (1) global, (2) sin Anthropic/OpenAI, y (3) solo open-source. Documentado en CLAUDE.md y ROADMAP.md.

### Documentado
- **ROADMAP.md** re-escrito desde cero: estado real v2.1, queue inmediato (modelos nuevos identificados), skills propuestos (`/add-model`, `/run-benchmark`), plan para DGX Spark y Ollama Cloud.
- **CLAUDE.md** actualizado: archivos clave nuevos, workflow con regeneración de MDs, regla de flujo ROADMAP↔CHANGELOG.

## [2.1.0] - 2026-04-23

### Por que v2.1 (first full Phi-4 run)
- **1512 corridas** evaluadas con Phi-4 judge: 17 modelos × 91 tests. Primer run completo del benchmark v2 con juez local.
- Ranking v1 (sin juez) queda obsoleto. v2.1 es la primera "verdad" con scoring completo.

### Agregado
- **Guardado incremental atomico en runner.py**: dump a JSON tras cada test, no al final. Si se corta no se pierde nada.
- **Flag `--resume <archivo.json>`**: retoma desde un benchmark parcial, saltea tests ya completados.
- **Guardado de respuesta completa por test**: cada request genera un `.md` auditable en `benchmarks/results/responses/<timestamp>/<modelo>__<suite>__<test>.md`. El JSON lleva `response_file` con path relativo.

### Resultados destacados (Phi-4 judge, 91 tests/modelo)
- **Top 5**: 1) Devstral Small 7.35, 2) GPT-5.4 Mini 7.32, 3) GPT-4.1 7.29, 4) Gemini 2.5 Flash Lite 7.22, 5) MiMo-V2-Flash 7.20
- **Devstral Small domina** como #1 overall y top en creatividad (7.70), string precision (7.66), traducción (7.87)
- **MiMo-V2-Flash sorprende**: #1 en razonamiento (7.58), contenido ES (7.51), code (7.74), strategy (7.78), productividad (7.66) — a $0.09/$0.29 per M (MIT)
- **GPT-5.4 Mini sube del #8 (v1) al #2**: el juez revaloriza su equilibrio calidad/velocidad (117 tok/s)
- **Llama 4 Maverick top en agentes (7.32)** pero 17 tests fallan por falta de tool calling nativo en OpenRouter
- **Kimi K2 17 errores 429** por rate limits sostenidos del provider
- **GLM-5.1 último (6.25)**: muy flojo en code/reasoning/contenido a pesar del branding agentic
- **Modelos chinos (MiniMax, Qwen, GLM) y Nemotron** agrupados al final del ranking

### Modelos nuevos evaluados en este run
- GPT-4.1 (directo, no Mini), GPT-5.4 Mini, Claude Opus 4.7, Kimi K2, Qwen 3.6 Plus, Qwen3 Coder, Mistral Large, Nemotron 3 Super, GLM-5.1

### Documentado
- README.md actualizado con ranking real de 17 modelos × 91 tests
- Mejor por categoría expandido a 12 categorías con Phi-4 judge
- Recomendaciones por caso de uso re-escritas con los nuevos datos

## [2.0.0] - 2026-04-22

### Por que v2.0 (breaking changes)
- Scoring v2 + LLM-as-Judge cambia todos los scores. Rankings anteriores no son comparables.
- Tests reorganizados en 4 pilares del emprendedor (razonamiento, coding, contenido, agentes)
- Juez cambiado de Gemma 4 a Phi-4 (Microsoft) por cero conflicto de interes
- Claude Code removido de suscripcion Pro $20 (21 abril 2026) - contexto actualizado

### Agregado
- **4 suites nuevas**: strategy (3 tests), sales_outreach (3 tests), translation (3 tests), agent_capabilities (5 tests)
- **Phi-4 como juez local**: Microsoft no tiene modelos en el benchmark = cero sesgo. MIT license, 14B, 3-9s/eval, $0.
- **6 modelos nuevos**: GLM-5.1 (#1 SWE-Bench Pro), Kimi K2.6, MiMo-V2-Flash/Pro, Nemotron 3 Super, Claude Opus 4.7
- **CASOS_DE_USO.md**: 50+ casos reales de IA para emprendedores organizados en 8 categorias
- **Compatibilidad con coding tools**: Info sobre que modelos funcionan con Claude Code, Roo Code, Cursor, etc.
- Total: **91 tests en 23 suites**, 30+ modelos configurados

### Mejorado
- Tests organizados en 4 pilares: Razonamiento, Coding, Contenido/Marketing, Agentes/Operaciones
- Adapter soporta thinking models (max_completion_tokens) para GLM-5.1, Kimi K2.6, Nemotron, GPT-5.4
- Judge usa /api/generate nativo para Ollama (fix: gemma4 devuelve vacio en /api/chat)
- Timeout subido a 300s para articulos largos
- Contexto actualizado: Claude Code ya no en suscripcion Pro $20

### Documentado
- Por que Phi-4 como juez (cero conflicto, MIT, replicable)
- Sesgo de LLM-as-Judge con referencias a papers (NeurIPS 2024, self-enhancement bias 5-7%)
- DESCUBRIMIENTOS.md actualizado con hallazgos de string precision y news SEO

## [1.3.0] - 2026-04-16

### Agregado
- **4 modelos Xiaomi MiMo**: MiMo-V2-Pro ($1/$3, 1T params), MiMo-V2-Flash ($0.09/$0.29, MIT), MiMo-V2-Flash free, MiMo-V2-Omni ($0.40/$2, multimodal)
- **Suite ocr_extraction** (5 tests): Facturas, tarjetas de presentacion, recibos con verificacion matematica, tablas de dashboard, notas manuscritas con OCR errors
- **Suite orchestration** (5 tests): Planificacion multi-paso, recuperacion de errores, descomposicion de workflows, seleccion precisa de herramientas, juicio paralelo vs secuencial
- **Suite multi_turn** (4 tests): Iteracion de contenido con feedback, soporte que escala, cambio de requisitos a mitad de camino, debugging iterativo
- **Suite policy_adherence** (4 tests): Politicas de reembolso bajo presion, proteccion de datos ante ingenieria social, reglas de idioma/tono, limites de alcance de servicio
- **LLM-as-Judge** (`--judge`): Sistema de evaluacion con auto-deteccion de juez. Prioridad: 1) Gemma 4 31B local via Ollama ($0, bajo sesgo), 2) Claude Haiku via OpenRouter (~$0.07/modelo). Evalua 5 dimensiones (precision, relevancia, profundidad, claridad, utilidad) + criterios extra por suite (originalidad, empatia, planificacion, coherencia contextual, cumplimiento de politicas). Combina 30% score automatico + 70% juez. Presets: gemma4, glm4, qwen3.5, haiku, gemini-flash. Tambien acepta model IDs directos.
- **Documentacion de sesgo del juez**: El modelo juez introduce sesgo (~5-7% de inflacion para modelos del mismo proveedor). Documentado en README, llm_judge.py, y CHANGELOG con tabla de tradeoffs por juez. Resultados JSON registran que juez se uso.
- **9 modelos nuevos de Abril 2026**: Nemotron 3 Nano ($0.05/$0.20), Nemotron 3 Super ($0.10/$0.50), Mistral Small 4 ($0.15/$0.60, Apache), Grok 4.1 Fast ($0.20/$0.50), Gemini 3.1 Flash Lite ($0.25/$1.50), Devstral 2 ($0.40/$2.00, MIT), GLM-5.1 ($0.95/$3.15, MIT, #1 SWE-Bench Pro), Gemini 3.1 Pro ($2.00/$12.00), Grok 4.20 ($2.00/$6.00)
- **Seccion "Como Replicar el Benchmark"** en README: guia paso a paso desde cero, costos estimados, como agregar modelos
- Total: 77 tests en 19 suites (antes: 59 tests en 15 suites)
- 3 proveedores nuevos: Xiaomi (MiMo), NVIDIA (Nemotron), xAI (Grok) en PROVEEDORES.md y COMPARATIVA.md

### Mejorado (Scoring v2 - correccion de sesgo)
- **Formato reducido de 3 a 2 puntos** en score_content_quality (era 30% del score de calidad, ahora 20%)
- **Secciones requeridas subidas de 3 a 4 puntos** para priorizar contenido sobre formato
- **Busqueda de secciones ahora ignora acentos** ("titulo" encuentra "título") via normalizacion Unicode
- **Penalizacion de caracteres chinos** en respuestas en espanol (hasta -2 pts). Mitiga problema de MiniMax y Qwen.
- **Nuevo score_expected_answer()** que valida respuestas contra criterios especificos:
  - `reasoning`: verifica que key_insights esten presentes (60% de palabras clave)
  - `hallucination_check`: evalua si el modelo dice "no se" en preguntas trampa
  - `creativity_check`: penaliza cliches (-1.5 a -5 puntos segun cantidad)
  - `depth_check`: penaliza frases genericas, premia datos concretos y riesgos
  - `honesty_check`: evalua transparencia sobre incertidumbre
  - `numeric`, `sequence`, `range`: validacion de respuestas factuales
- **Sin juez**: tests con expected_answer usan 40% formato + 60% sustancia
- **Con juez** (`--judge`): usa 30% automatico + 70% LLM-as-Judge

### Por que estos cambios (contexto)
- El scoring anterior daba 30% de los puntos de calidad por formato markdown (headers, bold, listas)
- Tests como deep_reasoning, creativity, hallucination tenian `expected_answer` definido pero NUNCA se validaba
- La lista de cliches en creativity.py existia pero no se usaba en el scoring
- Esto hacia que modelos rapidos y baratos que formateaban bien (Devstral) dominaran sobre modelos con mejor razonamiento
- El nuevo scoring valida sustancia: insights correctos, honestidad, creatividad real, datos precisos
- Los tests multi-turno y policy_adherence miden capacidades criticas para agentes reales que los tests single-turn no capturan
- LLM-as-Judge agrega evaluacion semantica que el scoring regex no puede hacer (calidad de analogias, empatia, utilidad practica)
- Benchmarks de referencia: HELM (Stanford), tau-Bench (Sierra), BFCL (Berkeley), LMSYS Arena

## [0.8.0] - 2026-04-12

### Agregado
- 6 modelos nuevos: Devstral Small, GPT-4.1, GPT-4.1 Mini, Mistral Large, Kimi K2, Kimi K2.5
- Claude Opus 4.6 (el #1 del mundo en Arena)
- 21 modelos en ranking global total
- Nota sobre limitaciones del scoring automatico

### Resultados Destacados
- Devstral Small es #1 (7.40) - open-source Apache 2.0, 171 tok/s, ultra barato
- GPT-4.1 es #2 (7.28) - supera a GPT-5.4 (#19), confirma hallazgo previo
- Claude Opus 4.6 es #13 (6.59) - scoring no captura calidad de razonamiento
- Kimi K2 es #16 (6.49) - decente pero no tan bueno como en benchmark manual previo

### Descubierto
- Scoring automatico favorece formato sobre sustancia
- GPT-4.1 consistentemente supera GPT-5.4 en tests estructurados
- Devstral Small de Mistral es una joya oculta

## [1.1.0] - 2026-04-12

### Agregado
- Suite hallucination: 3 tests (trampas factuales, fidelidad al contexto, citas falsas)
- Suite creativity: 4 tests (hooks sin cliches, analogias, profundidad, storytelling)
- DESCUBRIMIENTOS.md con observaciones no obvias
- Ranking global actualizado con 48 tests por modelo, 951 runs totales
- Recomendaciones expandidas: 11 casos de uso con modelo recomendado
- CheatSheet PDF actualizado a 9 paginas con alucinaciones y creatividad

### Resultados
- Alucinaciones: Claude Sonnet #1 (7.62), Anthropic = mas honesto
- Creatividad: Devstral #1 (6.93), MiniMax ultimo (5.19)
- Claude Opus sube a #9 global (desde #13) con los tests de calidad
- Claude Sonnet sube a #7 global (desde #12)

### Hallazgos
- Claude es el modelo mas honesto pero no el mas creativo
- MiniMax M2.7 es generico y con cliches en contenido
- MiniMax y Qwen a veces responden con caracteres chinos

## [0.7.0] - 2026-04-12

### Agregado
- Llama 4 Maverick via OpenRouter - #6 global, empata con Claude, open-source
- Qwen3 Coder via OpenRouter - #8 global, bueno para coding
- Gemma 4 31B y 26B MoE via OpenRouter - lentos pero funcionales
- Ranking actualizado con 12 modelos (14 contando variantes)
- Tabla solo alternativas (sin Anthropic/OpenAI) con 8 modelos

### Resultados
- Llama 4 Maverick (6.70): Sorpresa, empata con Claude Sonnet 4.6 y es open-source
- Qwen3 Coder (6.62): Solido para coding
- Gemma 4 26B MoE (6.53): Decente pero lento via OpenRouter (19 tok/s)
- Gemma 4 31B (6.42): Mas lento aun (11 tok/s), rate limits frecuentes

## [0.6.0] - 2026-04-11

### Agregado
- GPT-5.4 y GPT-5.4-mini via API directa de OpenAI
- Ranking global con 9 modelos medidos (10 contando duplicados de MiniMax por provider)
- Tabla separada "Solo Alternativas" (sin Anthropic/OpenAI)
- Tabla "Mejor por Categoria" con top 3
- Tabla "Recomendacion para Agentes N8N/OpenClaw"
- Soporte max_completion_tokens para GPT-5.4+

### Resultados
- GPT-5.4 Mini: Sorpresa, gana al GPT-5.4 en todas las categorias
- GPT-5.4 Mini: #1 en tool calling (7.5), ideal para agentes
- DeepSeek V3.2 se mantiene #1 global (7.09)
- Gemini 2.5 Flash Lite: 212 tok/s, el mas rapido por lejos

## [0.5.0] - 2026-04-11

### Agregado
- CLAUDE.md para continuidad entre sesiones de agentes
- Tests de generacion de imagenes MiniMax Image-01 (5/5 exitosos)
- Tests de TTS MiniMax (requiere plan Agent, no funciona con Coding Plan)
- Modelos nuevos: Gemma 4 31B, Gemma 4 26B MoE, Claude Sonnet 4.6, Gemini 2.5 Flash Lite, Qwen3 Coder 480B
- PROVEEDORES.md actualizado
- Image generation results en benchmarks/results/images/

### Descubierto
- MiniMax Coding Plan no incluye TTS (speech-02). Requiere plan Agent ($19/$69)
- MiniMax Image-01 funciona con Coding Plan token key
- Gemma 4 via OpenRouter es lento (~8 tok/s) - mejor correr local en DGX Spark

## [0.4.0] - 2026-04-11

### Agregado
- PROVEEDORES.md: Guia de contexto de cada proveedor (fundacion, foco, fortalezas, open-source)
- Resultados de benchmark en README.md
- Soporte API directa de MiniMax (M2.7 y M2.7 Highspeed)
- Tests de startup_content: blog ecosistemastartup.com, cursos, workshops, newsletters
- Repo privado en GitHub: ctala/ai-benchmarks-alternativos

### Resultados
- Benchmark general: DeepSeek V3.2 (7.05) > MiniMax M2.7 (6.40) > Qwen 3.6 Plus (6.08)
- MiniMax M2.7 vs Highspeed: diferencia marginal (~1%), practicamente iguales
- DeepSeek gana en 6/7 categorias, MiniMax gana en tool calling

### Corregido
- Runner: timeout robusto con signal alarm, output en texto plano
- Model IDs: Qwen 3.6 Plus free deprecado, MiniMax highspeed solo via API directa

## [0.3.0] - 2026-04-11

### Agregado
- PACKS.md: Guia de packs por suscripcion (MiniMax, Qwen, OpenAI, Google, Ollama, OpenRouter, xAI)
- Estrategia de optimizacion local + nube para DGX Spark
- Rankings completos por categoria (6 categorias con top 8-10 modelos cada una)
- Diagrama de routing: que modelo usar para que tarea
- Fecha de ultima actualizacion en todos los documentos

### Modificado
- COMPARATIVA.md: Rankings expandidos con listas completas en vez de solo el lider
- README.md: Version 0.3.0, referencia a PACKS.md

## [0.2.0] - 2026-04-11

### Agregado
- Modelos nuevos: Gemma 4 (31B, 26B MoE), Llama 4 Maverick, MiniMax M2.7 Highspeed
- Columna "Open Source" en todas las comparativas
- Seccion de modelos locales para NVIDIA DGX Spark (128GB)
- Suscripciones de MiniMax (Coding Plan $10-$150, Agent $19/$69)
- Suscripciones de Alibaba/Qwen (Coding Pro $50/mes)
- Ollama Cloud ($0/$20/$100)
- CHANGELOG.md para versionamiento

### Modificado
- Correccion: Anthropic SI funciona con OpenClaw/N8N via API key, la suscripcion Pro/Team NO da acceso API
- Modelos locales expandidos para aprovechar los 128GB del DGX Spark
- Config actualizado con modelos open-source marcados con licencia

## [0.1.0] - 2026-04-11

### Agregado
- Estructura inicial del proyecto
- COMPARATIVA.md con 30+ modelos organizados por tier de costo
- SUSCRIPCIONES.md con todas las suscripciones fijas ($0-$300/mes)
- 7 suites de benchmark con 18 tests totales
- Motor de benchmark (runner.py) con soporte OpenRouter
- Sistema de scoring multi-criterio (calidad, velocidad, costo, tool calling)
- Adaptador unificado para APIs compatibles OpenAI
- Soporte para Ollama local y Ollama Cloud
