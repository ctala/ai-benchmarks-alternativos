<!-- doc: snapshot -->
<!-- Fechado a propósito: es la foto de confianza de los guardrails al abrir el corte v5 (tarea 1.1 de openspec/changes/corte-v5). Los arreglos van en sus propios commits y se citan acá, no se reescribe la foto. -->

# Auditoría de confianza de los guardrails — 3-nov-2026

Tarea 1.1 de [`corte-v5`](openspec/changes/corte-v5/tasks.md). Son los **21 chequeos `check_*`
que corre `qa.py`**: los 20 de antes más `check_specs`, que entró hoy. `qa.py` corre además 8
cosas que no son `check_*` (pytest unitario, `qa_calculadora.mjs`, `auditar_paginas`,
`test_guardrails`, `cobertura.py` y los `--check` del censo y del blog). Quedan fuera de esta
tabla y se nombran al final.

## Cómo se midió

1. **Estado hoy.** Corrí los 21 sobre la rama limpia (`corte/v5` @ `a312f0022`) y salieron
   los 21 con exit 0. `check_agentico_publicado` sale con 0 aunque reporta ❌, porque es
   informativo y corre sin `--duro`.
2. **Pruebas de sabotaje.** `test_guardrails.py` dio 41 de 41 en verde, en 14 s. Como cada
   chequeo está en verde sobre el repo limpio y en rojo con su sabotaje, **ninguna prueba
   pasa gracias a deuda que ya estaba**. Ese es el falso verde de `_t_docs` y
   `_t_blog`, y está descartado para todas.
3. **Qué prueba cada sabotaje.** Leí las 41 y crucé cada una con las reglas internas del
   chequeo (C1-C5, S1-S6…). Una prueba que ejerce 1 de 5 reglas prueba esa regla, no el
   chequeo entero.
4. **Si cazó algo real.** Lo busqué en el CHANGELOG. Separo lo que encontró **al nacer**
   (la deuda que lo motivó) de lo que cazó **después**, en uso, que es lo que prueba que
   sirve.
5. **Casos fundacionales.** Donde se podía hacer sin riesgo, reproduje el caso que motivó
   el chequeo.

## Veredictos

- **Confiable:** la prueba inyecta el fallo que el chequeo dice cazar, y el chequeo lo
  caza.
- **Verde vacío:** el chequeo da verde sobre un caso que dice cubrir. Está comprobado
  reproduciéndolo, no supuesto.
- **Sin prueba:** no hay sabotaje en `test_guardrails.py`.

La columna *Alcance de la prueba* dice cuántas reglas internas ejerce el sabotaje. Un
«confiable» con alcance 1/5 es confiable **en esa regla**: las otras cuatro tienen la misma
confianza que un chequeo sin prueba.

## La tabla

| # | Chequeo | Clase en `qa.py` | Qué dice cazar | Alcance de la prueba | ¿Cazó algo real? | Veredicto |
|---|---|---|---|---|---|---|
| 1 | `check_consistency` | bloqueante | un doc vivo que cita un score que ya no existe | 1 sabotaje (cifra inventada junto a «GPT-5.6 Luna» en `MODELOS.md`); el nombre del modelo está fijo en la prueba | al nacer: el README publicaba Grok 4.5 = 6,99 con el sitio en 5,84 (jul) | **confiable** |
| 2 | `check_suites` | bloqueante | que el registro de ejes deje de ser uno solo | 2 de 6 (S2 copia a mano en `app.js`, S6 declarado ≠ promediado); S1, S3, S4 y S5 sin sabotaje | al nacer: la copia de `app.js` divergía en 7 suites | **confiable** (2/6) |
| 3 | `check_effort` | bloqueante | un effort fijo en vez del declarado por modelo, o una foto incompleta | 5 sabotajes (resolver fijo, foto sin modelo, E5, E6, E7); E3 y E4 no tienen uno propio | al nacer: el `medium` fijo del 2-sep; E5/E6 en uso con el experimento del 4-sep | **confiable** |
| 4 | `check_calculator` | bloqueante | umbrales y ejes de la calculadora desalineados con los datos | 2 de 5 (C1 umbral, C5 eje no expuesto); C2, C3 y C4 sin sabotaje | **en uso:** C1 avisó cuando se puso 7,0 a mano en el slider | **confiable** (2/5) |
| 5 | `check_cortes` | bloqueante | un corte por eje que no coincide con `models.json` | 1 de 5 (C2: se cambia el #1 de una página); C1, C3, C4 y C5 sin sabotaje | estuvo **una corrida entera ciego y mudo** (regex roto por `<a class="a-ficha">`); se arregló con C1 exigiendo encontrar la fila | **confiable** (1/5) |
| 6 | `check_claims` | bloqueante | un doc vivo que afirma lo que reemplazó una decisión vigente | 1 de 6 claims; la prueba pega **el string literal** que el chequeo busca | sin registro de una detección en uso | **confiable** (alcance literal: no ve paráfrasis) |
| 7 | `check_cobertura` | bloqueante | una regla aplicada en una superficie y no en las demás | 1 de 7 (R6, la segunda tabla con flag); R1-R5 y R7 sin sabotaje | al nacer: segunda tabla en 2 de 16 páginas, W6 en 2 de 8 promesas | **verde vacío** en R5 (ver H2) |
| 8 | `check_caminos` | bloqueante | medir por fuera del runner | 1 sabotaje (script con `requests.post` a OpenRouter) | **en uso:** marcó `judge_posthoc.py` el 11-oct (Action en rojo) | **confiable**, pero su gate no frenó (ver H1) |
| 9 | `check_specs` | bloqueante | un change de OpenSpec en el aire | 6 de 6 (S1-S6), con control verde en un `openspec/` desechable | nació hoy, sin historia | **confiable** |
| 10 | `check_version` | bloqueante | superficies con versiones distintas, o un tag huérfano | 2 de 4 (V1, V4 en repo desechable con control verde); V2 y V3 quedan implícitos en el control de V4 | **en uso:** v4.13.0 con el tag fuera de main 11 días (motivó V4); schema.org en v4.0 con el hero en v4.1 | **confiable** |
| 11 | `check_changelog` | bloqueante (`--nivel`) | cambios sin entrada **y** un bump que no alcanza | **1 de 2.** La prueba vacía `[No publicado]` (C1) y corre **sin `--nivel`**, así que C2 (el bump) nunca se sabotea aunque la descripción lo nombre | al nacer: v4.1 publicado sin entrada | **confiable** en C1 · C2 sin prueba |
| 12 | `check_presupuesto` | informativo | que no haya saldo para medir | sin sabotaje; la regla pura `disponible()` tiene test unitario | **él mismo fue un falso verde**: miraba solo el tope de la key ($720) con $16,81 en la cuenta. Arreglado | **sin prueba** |
| 13 | `check_secretos` | bloqueante | una credencial real en un archivo versionado | capa 1 (valor literal del `.env`); la capa 2 (patrones) no tiene sabotaje. En CI la prueba pasa sin probar nada (no hay `.env`) | al nacer: la Secret Key de R2 replicada en ~600 archivos | **verde vacío** en el caso que lo fundó (ver H3) |
| 14 | `check_truncamiento` | informativo | una nota construida sobre respuestas cortadas | 1 sabotaje con `--duro`, que `qa.py` no pasa | al nacer: 4 modelos el 17-ago | **confiable** · el motivo para ser informativo caducó (ver H4) |
| 15 | `check_ci` | informativo | el Action de artefactos semanas en rojo | sin sabotaje | sin registro de una detección en uso | **sin prueba**, con un hueco comprobado (ver H1) |
| 16 | `check_agentico_publicado` | informativo | un rankeado publicado sin tarea agéntica | sin sabotaje | al nacer: 11 sin evidencia. **Hoy marca 8** (familia Claude 5.5, GPT-6 Luna y Luna Pro, Ling 3.0 Flash VL, MiMo V2.6 Flash) | **sin prueba** |
| 17 | `check_ganadores` | bloqueante | una página que corona a quien su tabla no sostiene | 1 de 2 (G2: «Gana X» sobre un empate). G1 (el veredicto que nombraba a un #73) no se sabotea, aunque el comentario dice que la prueba cubre «los dos casos» | al nacer: los dos casos del 19-ago | **confiable** (1/2) |
| 18 | `check_release_mensual` | informativo | un reporte del mes que le atribuye una cifra que no es suya | 1 sabotaje, con control verde y datasheet fabricado si falta (arreglado hoy) | **en uso:** marcó 3 parejas sin respaldo al entrar Hy4. **Su prueba fue verde vacío** hasta hoy | **confiable** desde hoy |
| 19 | `check_blog_consistency` | bloqueante | un post con cifras caducadas | 1 sabotaje con control verde; en CI pasa sin probar (no hay blog clonado) | **en uso:** 19 posts con cifras viejas (16-sep). **Su prueba fue verde vacío** hasta el 16-sep | **confiable** |
| 20 | `check_paleta` | bloqueante | un color fuera del manual de marca | P2 (color inventado en `style.css`); P1 es solo informativo | al nacer: 22 colores fuera del manual | **confiable** |
| 21 | `check_fichas_alcanzables` | bloqueante | una página que lista modelos sin enlazar su ficha | 1 de 2 (F2); F1 (la ficha existe en disco) sin sabotaje | **en uso:** encontró 5 páginas sin enlace que se habían escapado del arreglo a mano | **confiable** (1/2) |

**Conteo:** 16 confiables, 2 verdes vacíos (`check_cobertura` R5 y `check_secretos`) y 3 sin
prueba (`check_presupuesto`, `check_ci` y `check_agentico_publicado`). Son 21 filas y todas
tienen veredicto.

## Hallazgos

**H1. El gate solo existe para quien empuja desde esta máquina.** El agente de Cursor metió
`judge_posthoc.py` con PRs mergeados en GitHub el 11-oct (#26 y #27). `check_caminos` lo cazó:
el Action de ese día falló. Pero `main` siguió 23 días con un bloqueante en rojo:

- el hook de pre-push es local y un merge en GitHub no pasa por él;
- el Action corre **después** del merge y solo si se tocan sus `paths`, así que no volvió a
  correr hasta el 3-nov;
- `check_ci` cuenta **corridas** fallidas seguidas (`RACHA_MALA = 3`), no el **tiempo** en rojo.
  Una sola corrida roja que no se repite deja la racha en 1 todo el tiempo que haga falta.

El chequeo funcionó y el canal no. Es la misma lección de los 40 días de agosto. Las opciones
son exigir checks en la protección de rama de `main` o hacer que `check_ci` mire los días
desde el último verde. Las dos son de la sección 1.3, no de hoy.

**H2. `check_cobertura` R5 no mira `qa.py`.** R5 («todo guardrail del pipeline está probado»)
recorre solo los `check_*` que aparecen en `regenerate_all.py`. Ocho de los 21 chequeos del QA
no están ahí: `agentico_publicado`, `changelog`, `ci`, `effort`, `paleta`, `presupuesto`,
`release_mensual` y `specs`. Por eso los 3 sin prueba conviven con R5 en verde. Además, la
tarea 1.2 se verifica con «R5 sigue verde», y hoy eso no dice nada sobre esos tres. Corregirlo
va antes de 1.2 o junto con ella, y entra en el instrumento de 1.4.

**H3. `check_secretos` no caza el caso que lo fundó.** Lo reproduje con un archivo versionado
que tenía una clave hex de 64 caracteres generada al azar (la forma de la Secret Key de R2),
y el resultado fue **exit 0**. La capa 1 solo conoce lo que hay en `.env`, que tiene 2
credenciales (OpenRouter y NIM): las otras 5 API keys están vacías porque viven en Infisical,
y la de R2 no está. La capa 2 no tiene patrón para hex, a propósito, porque un hex de 64 tiene
la misma forma que un `prompt_sha`. La limitación se declaró al nacer (CHANGELOG del 17-ago,
«6 de las 8 API keys vacías»), pero el ✅ dice «ninguna credencial real» sin decir que solo
conoce dos. Además, la capa 2 no tiene sabotaje.

**H4. `check_truncamiento` puede ser bloqueante.** Es informativo «hasta que se archiven los
runs truncados». Hoy dice «ninguno de los 188 modelos con muestra suficiente cruza el umbral»,
o sea que esa condición ya se cumplió. Pasarlo a bloqueante lo fortalece, así que la regla de
no debilitar no lo frena. Igual lleva su fila en `DECISIONES.md` y tu OK.

**H5. En CI, tres pruebas pasan sin probar nada.** `_t_secretos` (sin `.env`), `_t_blog` y
`_t_blog_datos` (sin blog clonado) devuelven verde cuando les falta el insumo. En local sí
prueban. En el Action, el «41 de 41» real es 38.

**H6. La cobertura por regla es baja en los chequeos con varias reglas.** Hay 20 reglas
internas sin sabotaje propio: `check_cortes` C1, C3, C4 y C5; `check_suites` S1, S3, S4 y S5;
`check_calculator` C2, C3 y C4; `check_cobertura` R1-R5 y R7 (seis); `check_ganadores` G1;
`check_fichas_alcanzables` F1, y `check_changelog` C2. No están rotas: no hay evidencia de que
funcionen.

## Las 8 entradas de `qa.py` que no son `check_*` (tarea 1.11, 3-nov-2026)

Al principio estaban fuera de la tabla. Entraron con el ok del 3-nov, con las mismas tres
preguntas. Se suma un cuarto veredicto, **exento**: aplica a la entrada que no puede tener
sabotaje porque ella misma es una prueba. Cada exención lleva su motivo en `check_cobertura` y
su fila en `DECISIONES.md`. Estado de hoy: todas salen con exit 0, salvo `cobertura.py --duro`,
que da exit 1 (68 % contra un piso de 80 %, deuda conocida).

| # | Entrada | Clase en `qa.py` | Qué dice cazar | Alcance de la prueba | ¿Cazó algo real? | Veredicto |
|---|---|---|---|---|---|---|
| 22 | `test_unitarios.py` (pytest, 140 tests) | bloqueante | que una función pura del núcleo rompa su caso borde | no aplica: es un conjunto de pruebas, y cada `assert` es el sabotaje de su función | sí, en uso (lo vigila `cobertura.py`) | **exento** |
| 23 | `qa_calculadora.mjs` (31 chequeos) | bloqueante | que el `app.js` real, wizard incluido, contradiga a los datos | 1 de 31 con sabotaje automático (Q15, página huérfana). W16 se saboteó a mano una vez y no quedó como prueba | **en uso:** Q15 encontró 4 páginas huérfanas, una mintiendo sobre su frescura | **confiable** (1/31) |
| 24 | `auditar_paginas.py --duro` | bloqueante | que una página publicada diga algo que la data no sostiene | sin sabotaje. Su etiqueta en `qa.py` dice «71 páginas» y audita 187 | al nacer: cinco falsos positivos y puntos ciegos en un día, que dieron origen a R7 | **sin prueba** |
| 25 | `test_guardrails.py` | bloqueante | que un guardrail no falle ante su propio fallo | no aplica: es la prueba de los demás. Se cuida con la trampa de argparse de `_correr` y con el control verde antes de sabotear | **en uso:** destapó los falsos verdes de `_t_docs`, `_t_blog` y `_t_release` | **exento** |
| 26 | `cobertura.py --duro` | informativo | que el núcleo baje del piso de 80 % | sin sabotaje | hoy en rojo y honesto (68 %) | **sin prueba** |
| 27 | `generate_censo_proveedores.py --check` | informativo | un censo de proveedores de más de 30 días | sin sabotaje, y **no podría tenerlo**: `--check` devuelve 0 en todas sus ramas | **no.** Hoy `qa.py` imprime «✅ … no está viejo» con un censo de **45 días** | **verde vacío** (ver H7) |
| 28 | `generate_blog_tablas.py --check` | informativo | tablas del pilar desfasadas del ranking | sin sabotaje. Sin blog clonado avisa y pasa | sin registro de una detección en uso | **sin prueba** |
| 29 | `generate_blog_datos.py --check` | bloqueante | un dato marcado en un post con un valor viejo | 1 sabotaje con control verde. En CI pasa sin probar (H5) | nació en verde; sin registro de una detección en uso | **confiable** |

**Conteo de las 29 filas:** 18 confiables, 3 verdes vacíos (`check_cobertura` R5,
`check_secretos` y el `--check` del censo), 6 sin prueba y 2 exentos.

**H7. Un informativo que nunca falla dice ✅ sobre lo que vino a avisar.** Pasa con
`generate_censo_proveedores --check`: imprime el ⚠️ por stdout pero sale con 0, y `qa.py` lee el
exit code. El aviso existe y queda debajo de un ✅. Es el mismo mecanismo de H1, un canal que no
llega. El arreglo no debilita nada: que `--check` salga con 1 cuando el censo está viejo. Sigue
siendo informativo, así que `qa.py` muestra ⚠️ y no frena. Entra con la tarea 1.1b, porque R5
le va a exigir una prueba y a algo que nunca falla no se le puede escribir una.

## Ok de Cristian (tarea 1.5)

3-nov-2026: *«OK a la tabla (1.5).»* Con él vinieron el orden y los límites de lo que sigue,
que ahora están en `tasks.md` como 1.1b y 1.6 a 1.11:

- R5 se arregla antes de 1.2;
- gitleaks reemplaza a los patrones propios;
- `check_truncamiento` pasa a bloqueante;
- las pruebas que se saltan en CI se imprimen como omitidas;
- solo se sabotean las reglas que prometen sin probar (`check_changelog` C2 y `check_cortes`
  C1, C3, C4 y C5);
- las 8 entradas que no son `check_*` entran a la tabla.

Ningún chequeo baja de bloqueante a informativo.

## Arreglos posteriores (la foto de arriba no se reescribe)

3-nov-2026, tareas 1.1b, 1.2 y 1.11, en un solo commit para que R5 no naciera en rojo:

- **R5 (H2) cerrado.** `check_cobertura` R5 lee `qa.CHEQUEOS` y los `check_*` del pipeline, y
  exige que `test_guardrails.py` **invoque** cada script, no que lo nombre. Las exenciones van
  en `EXENTOS_R5`, cada una con su motivo: `test_unitarios.py`, `test_guardrails.py` y
  `check_ci.py`. La de `check_ci.py` es temporal y se borra en 1.6.
- **Con prueba nueva:** `check_presupuesto` (filas 12), `check_agentico_publicado` (16),
  `auditar_paginas` (24), `cobertura.py` (26), `generate_censo_proveedores --check` (27),
  `generate_blog_tablas --check` (28) y R5 mismo. Las pruebas pasaron de 41 a 48.
- **El censo (H7) cerrado.** `--check` sale con 1 cuando el censo está viejo. Sigue siendo
  informativo en `qa.py`, que ahora muestra ⚠️ en vez de ✅.
- **Verificación.** Cada prueba nueva se puso en rojo al romper su detector (7 de 7), y la
  mitad de R5 que exige motivo se probó aparte. La regla de exención huérfana o ya probada no
  tiene sabotaje propio.
- **Lo que sigue abierto:** `check_secretos` (H3, tarea 1.7), `check_ci` (H1, 1.6),
  `check_truncamiento` (H4, 1.8), las pruebas omitidas en CI (H5, 1.9) y las reglas de H6
  que entran por 1.10.


3-nov-2026, tareas 1.12, 1.13 y 1.6:

- **La regla de exenciones de R5 tiene sabotaje (1.12).** Una exención huérfana
  (`check_fantasma.py`) y una ya probada (`check_presupuesto.py`) ponen R5 en rojo nombrando
  al archivo. Quitando cualquiera de las dos ramas de la regla, la prueba falla.
- **La etiqueta de páginas sale del dato (1.13).** `qa.py` la pide a `auditar_paginas.paginas()`:
  dice 187, igual que el auditor, y con una página temporal pasó a 188 sola.
- **`check_ci` (H1) cerrado (1.6).** Mide días con el último estado en rojo (2 de margen), y si
  `origin/main` declara un cron, también el silencio. El Action corre en todo push a `main` y
  una vez al día; el cron rige recién con el merge del corte. Su prueba simula el fallo
  aislado de hace 10 días y el cron que no corre, con controles en verde para un rojo de 3
  horas y para la ausencia sin cron; volver a la racha de 3, apagar el silencio o ignorar el
  YAML la ponen en rojo. Se borró la exención temporal: `EXENTOS_R5` queda con las dos pruebas.
- **`check_truncamiento` (H4) cerrado (1.8).** Bloqueante con `--duro` en `qa.py` y en el
  Action; nace en verde con 188 modelos y un modelo truncado fabricado frena el QA.
- **Lo que sigue abierto:** `check_secretos` (H3, 1.7), las pruebas omitidas en CI (H5, 1.9) y
  las reglas de H6 que entran por 1.10.

3-nov-2026, tareas 1.4 y 1.9:

- **El instrumento del corte (1.4).** `check_cobertura` R8 pone en rojo un bloqueante bajado o
  quitado sin fila en `DECISIONES.md`, un `--duro` perdido desde el tag y un conteo de pruebas
  bajo el máximo desde el tag.
- **H5 cerrado (1.9).** Las pruebas que no pueden correr se declaran omitidas y el resumen las
  nombra. Las dos del blog corren sobre un fixture; quedan omitidas en CI `check_secretos` y
  `generate_blog_tablas`.
- **H6, la parte acordada (1.10).** `check_changelog` C2 y `check_cortes` C1, C3, C4 y C5
  tienen sabotaje; cada regla apagada hace fallar solo su prueba. R5 ya lo tenía (1.1b, 1.12). Las otras 14 siguen como
  deuda nombrada: `check_suites` S1, S3-S5; `check_calculator` C2-C4; `check_cobertura` R1-R4
  y R7; `check_ganadores` G1; `check_fichas_alcanzables` F1.
- **H3 cerrado (1.7).** `check_gitleaks` (gitleaks 8.30.1, bloqueante) caza lo que tiene forma
  de credencial; `check_secretos` sigue con los valores exactos del `.env`. Un hex de 64 sin
  contexto de clave no lo caza ninguno de los dos, y queda dicho: cazarlo pedía un patrón propio.
- **Grupo 1 sin hallazgos abiertos.** El escaneo del historial con gitleaks se reporta aparte.
