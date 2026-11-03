## 0. Orden desde el comienzo (3-nov-2026)

- [x] 0.1 Rama `corte/v5` desde `main` (v4.17.0). Verificar: `git branch --show-current` = corte/v5.
- [x] 0.2 `openspec init --tools none --language es` dentro del benchmark; el hub no se toca. Verificar: existe `openspec/config.yaml` con schema spec-driven.
- [x] 0.3 `check_specs.py` (S1-S6) con 6 pruebas de sabotaje en `test_guardrails.py` y registrado como bloqueante en `qa.py`. Verificar: `qa.py --pre-merge` verde en la rama; `check_specs.py --rama main` rojo con este change activo.
- [x] 0.4 Filas de `DECISIONES.md`: OpenSpec dentro del benchmark (revierte la del 16-sep), change se archiva, v5.0.0 por ocasiones, enriquecer no replicar, medir con harness oficial, ningún guardrail se debilita. Verificar: `check_claims.py` vigila la afirmación vieja.
- [x] 0.5 `CLAUDE.md`, skill `abrir-sesion` y `CHANGELOG.md` dicen lo mismo que las filas. Verificar: `grep -rn "No se adopt" CLAUDE.md .claude` vacío.

## 1. Auditoría de confianza de los guardrails (gate: nada de v5 avanza sin la tabla leída)

- [x] 1.1 Tabla de los 21 chequeos `check_*` de `qa.py` (20 más `check_specs`, que entró el 3-nov): qué fallo dice cazar, si su prueba de sabotaje inyecta ese fallo o un sustituto cómodo, y si alguna vez cazó algo real según el CHANGELOG. Veredicto por fila: confiable, verde vacío o sin prueba. Archivo: `AUDITORIA-GUARDRAILS-2026-11.md` (snapshot). Verificar: 21 filas, ninguna sin veredicto.
- [x] 1.1b **Antes de 1.2.** `check_cobertura` R5 lee la lista completa de `qa.py` (los 21 `check_*` y las 8 entradas que no lo son), no `regenerate_all.py`. Hasta que esté hecho, «R5 verde» no cuenta como verificación de nada. Verificar: un sabotaje con un chequeo de `qa.py` sin prueba pone R5 en rojo, con control verde primero.
- [x] 1.2 Los 3 sin prueba (`check_agentico_publicado`, `check_ci`, `check_presupuesto`) reciben prueba de sabotaje o una fila que explique por qué no la pueden tener. Verificar: `check_cobertura.py` R5 sigue verde y el conteo de `@prueba` sube. Hecho el 3-nov-2026 junto con 1.1b, en el mismo commit para que R5 no naciera en rojo: `check_agentico_publicado` y `check_presupuesto` tienen prueba, y `check_ci` queda exento hasta 1.6. Se sumaron las entradas que R5 destapó al leer `qa.py` (`auditar_paginas`, `cobertura.py`, el `--check` del censo y el de las tablas del blog). Son 48 pruebas, antes 41, y cada una nueva falla si se rompe su detector.
- [ ] 1.3 Cada verde vacío se arregla igual que `check_release_mensual`: mundo roto fabricado desde el dato real, control verde primero. Verificar: la prueba falla si se le quita el sabotaje. Estado al 3-nov-2026: R5 se cerró con 1.1b; el censo (H7, aparecido en 1.11) sale con 1 cuando está viejo y tiene prueba; `check_secretos` se cierra con 1.7.
- [ ] 1.4 Instrumento para «ningún guardrail se debilita»: el conteo de `@prueba` no baja y ningún chequeo pasa de bloqueante a informativo sin fila en `DECISIONES.md`. Antes, mirar si `check_cobertura.py` ya lo cubre. Verificar: prueba de sabotaje del instrumento.
- [x] 1.5 Cristian lee la tabla y da el ok para seguir. Verificar: su ok textual citado en la tabla. Hecho el 3-nov-2026: «OK a la tabla (1.5)».
- [x] 1.6 El aviso llega: el Action corre en todo push a `main` y una vez al día, y `check_ci` alarma por **días** con el último estado en rojo, no por fallos seguidos (H1). Prueba de sabotaje y fila en `DECISIONES.md`. Verificar: un fallo aislado simulado de hace 10 días hace saltar la alarma.
- [ ] 1.7 Secretos: se adopta gitleaks en `qa.py` y no se escriben patrones propios (H3). Entra bloqueante si nace en verde; si nace en rojo, entra informativo con su motivo escrito. Prueba de sabotaje y fila en `DECISIONES.md`. Verificar: una clave hex de 64 al azar en un archivo versionado lo pone en rojo.
- [x] 1.8 `check_truncamiento` pasa a bloqueante (H4), con su fila en `DECISIONES.md`. Verificar: nace en verde con los 188 modelos. Hecho el 3-nov-2026: `--duro` en `qa.py` y en el Action. `regenerate_all.py` lo sigue corriendo sin `--duro` y con `allow_fail`, y no frena a propósito: el pipeline regenera, y quienes frenan son el QA pre-push y el Action.
- [ ] 1.9 Las 3 pruebas que en CI pasan sin `.env` ni blog (`_t_secretos`, `_t_blog`, `_t_blog_datos`) se marcan «omitida» y se imprimen como tales; el CI clona el blog o esas pruebas usan fixtures (H5). Prueba de sabotaje y fila en `DECISIONES.md`. Verificar: el resumen del CI dice cuántas omitió.
- [ ] 1.10 De las 20 reglas internas sin sabotaje (H6), solo las que prometen algo que no prueban: el bump de `check_changelog` (C2) y las 4 de `check_cortes` (C1, C3, C4 y C5). Cada una con su sabotaje y control verde. El resto queda en la tabla como deuda nombrada. Verificar: cada prueba falla si se le quita el sabotaje.
- [x] 1.11 Las 8 entradas de `qa.py` que no son `check_*` (pytest unitario, `qa_calculadora.mjs`, `auditar_paginas --duro`, `test_guardrails`, `cobertura.py --duro` y los `--check` del censo, de las tablas del blog y de los datos del blog) entran a la tabla con las mismas tres preguntas. Verificar: la tabla tiene 29 filas y ninguna sin veredicto.

- [x] 1.12 Sabotaje para la regla de R5 que pone en rojo una exención huérfana (ya no corre en `qa.py` ni en el pipeline) o ya probada (`test_guardrails` la invoca). Verificar: control verde, y cada uno de los dos casos pone R5 en rojo; la prueba falla si se le quita la regla.
- [x] 1.13 La etiqueta «lo que publican las 71 páginas…» de `qa.py` se deriva del dato en vez de escribirse a mano. Verificar: la etiqueta coincide con el conteo que imprime `auditar_paginas.py` (hoy 187) y cambia sola si se agrega una página.

Orden de la próxima sesión (Cristian, 3-nov-2026, tras cerrar 1.12, 1.13, 1.6 y 1.8): 1.4 (el instrumento de «ningún guardrail se debilita», que protege lo que viene) → 1.9 → 1.10 → 1.7 (gitleaks) al final, porque trae una herramienta nueva.

Límites del grupo 1 (Cristian, 3-nov-2026): ningún chequeo baja de bloqueante a informativo; si un arreglo lo exige, se para y se dimensiona. Push de `corte/v5`: no todavía.

## 2. Fuentes externas y conjunto base

- [ ] 2.1 `benchmarks/fuentes_externas.py`: ingesta Terminal-Bench (dataset HF del leaderboard), Toolathlon-Verified y SWE-bench Pro público; mapea nombres a `key` de `models.py` (nunca por `name`); imprime cobertura sobre los 115. Verificar: el script corre offline sobre una foto guardada con fecha y licencia por fuente.
- [ ] 2.2 Las cifras externas entran a `models.json` como banda por fuente (`externos: {fuente, cifra, version, fecha, licencia}`) y ningún generador las promedia con las propias. Verificar: `test_unitarios.py` tiene un test que falla si una cifra externa entra a `quality_avg`.
- [ ] 2.3 Conjunto base = intersección (medidos por alguna fuente) ∩ (llamables por OpenRouter). Se publica el número y la lista. Verificar: `FUENTES-EXTERNAS.md` deja de ser borrador y cita el número desde el dato, no a mano.
- [ ] 2.4 Los modelos fuera del conjunto base llevan `sin_dato_comunitario: true` y la calculadora lo muestra. Verificar: `qa_calculadora.mjs` lo comprueba.

## 3. Ocasiones

- [ ] 3.1 Registro de las 6 ocasiones en `suites.py` (qué suites y qué fuente externa alimentan cada una) con volúmenes por defecto de `OCASIONES.md`. Verificar: `check_suites.py` falla si una suite del índice no pertenece a ninguna ocasión.
- [ ] 3.2 `export_for_pages.py` emite `ocasiones` por modelo y recalibra con `--recalibrate --scoring-version v5.0` solo en el release. Verificar: simulación contra los runs en disco antes de aplicar, con control verde sobre v4.17.0.
- [ ] 3.3 Programar: jubilar `code_generation` del índice (no se borra); las tareas Harbor propias con instrucción en español se mantienen y se nombran como capa propia. Verificar: `suites.del_indice()` lo refleja y ningún doc vivo cita `code_generation` como vigente.
- [ ] 3.4 Calculadora: selector de ocasión, volúmenes editables, precio mensual al volumen declarado. Verificar: `qa_calculadora.mjs` con un caso por ocasión.
- [ ] 3.5 Páginas y blog: generadores pSEO y `generate_blog_tablas.py` leen ocasiones; `check_consistency` y `check_blog_consistency` se adaptan **con su prueba** en el mismo commit. Verificar: QA verde sin tocar ningún bloqueante a informativo.

## 4. Modelos sin dato comunitario

- [ ] 4.1 Camino `externos/` declarado en `check_caminos.py` (qué puede llamar a un modelo fuera del runner: solo el harness oficial de una fuente, con su versión fijada) y fila en `DECISIONES.md`. Verificar: prueba de sabotaje con un script fuera del camino.
- [ ] 4.2 Qwen 3.8 Flash contra Ornith 1.5 en el harness oficial de Terminal-Bench, mínimo 5 intentos por tarea, en el Spark vía `sparkctl` cuando Cristian autorice la ventana. El modelo principal del Spark no se sube. Verificar: `result.json` por intento y `metadata.yaml` como pide el leaderboard.
- [ ] 4.3 Publicación como corrida independiente («medido por nosotros con el harness oficial vX, N intentos, fecha») en el sitio y referencia desde Hugging Face. Verificar: ok textual de Cristian antes de publicar.

## 5. Release v5.0.0

- [ ] 5.1 `CHANGELOG.md` cierra `[No publicado]` como `[v5.0.0]`; `check_changelog.py --nivel` exige mayor y lo encuentra. Verificar: `check_version.py` con las 7 superficies y el tag.
- [ ] 5.2 QA completo verde en la rama (no solo `--pre-merge`), blog regenerado y verificado cifra por cifra, cheatsheet y datasheet del mes. Verificar: `qa.py` sin tolerancias.
- [ ] 5.3 Ok textual de Cristian para merge a `main` y push. Verificar: citado en el CHANGELOG.
- [ ] 5.4 Archivar este change con `openspec archive corte-v5` antes del merge: `check_specs` S1 no deja un change activo en `main`. Verificar: `openspec/changes/archive/2026-xx-xx-corte-v5/` sin tareas abiertas.
