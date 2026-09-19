---
name: abrir-sesion
description: Declarar el plan ANTES de trabajo que toque medición, scoring o publicación — alcance, etapas, qué verifica cada una y dónde se para. Una aprobación de alcance en vez de aprobaciones por salto. Triggers "vamos a medir", "cambiemos el índice", "antes de arrancar", "/abrir-sesion".
---

# Abrir sesión — benchmark

Complemento de [`cerrar-sesion`](../cerrar-sesion/SKILL.md). Aquél asegura que nada se pierda al
final; éste asegura que **el alcance esté declarado al principio**.

## Por qué existe (19-sep-2026)

Cristian, después de una sesión que empezó con *«simulemos jubilar lo saturado»* y terminó
publicando v4.15.0, midiendo 36 runs, reescribiendo una página de SEO y tocando el blog:

> *«me preocupa saltarme etapas»*

Tenía razón, y el diagnóstico importa porque es contraintuitivo: **las etapas de verificación no
se saltaron** —se simuló antes de aplicar, se exigió control verde antes de sabotear, el guardrail
nuevo entró con su prueba, nada se publicó sin QA—. Lo que faltó fue el **mapa**: cada salto de
alcance se preguntó por separado, así que nunca hubo un momento donde se viera el tamaño real del
trabajo. Aprobar ocho veces «¿sigo?» no es lo mismo que aprobar una vez «esto es lo que vamos a
hacer».

No se adoptó ninguna herramienta de specs para esto: ver la fila de OpenSpec en `DECISIONES.md`.
El mecanismo ya existe (`PLAN-ESTABILIDAD.md` R1-R3 + el calendario); lo que faltaba era usarlo al
abrir, no sólo al ejecutar.

## Cuándo se usa

**Sí:** medir un lote · cambiar el scoring, el registro de suites o qué entra al índice · publicar
una versión · tocar páginas del sitio o posts del blog · cualquier cosa que vaya a costar dinero.

**No:** responder una pregunta, leer datos, correr el QA, un fix de una línea con su test. Pedir
un plan para eso es fricción, no rigor.

---

## El plan, en seis líneas

Antes de tocar nada, escribir y mostrar:

1. **Objetivo** — qué queda distinto cuando termine, en una frase.
2. **Clase de cambio** (PLAN-ESTABILIDAD R1). Decide todo lo demás:
   - **Presentación** (composición del score, columnas, etiquetas): se **simula antes** contra los
     runs en disco. Cuesta minutos y $0.
   - **Medición** (prompts, suites, `max_tokens`, criterios): sólo en **ventana declarada**, y
     rompe comparabilidad con lo ya medido.
3. **Superficies que toca** — de `SUPERFICIES.md`. Si aparece el blog o `docs/`, hay publicación
   de por medio y eso necesita OK aparte.
4. **Costo** — runs × modelos, USD estimado, y `check_presupuesto.py --necesito <USD>`.
5. **Qué verifica cada etapa** — el instrumento concreto, no «revisar».
6. **Dónde se para** — la lista de lo que NO se hace sin un «ok» textual.

Después: **una** aprobación de alcance. Los hallazgos que aparezcan se reportan y se dimensionan,
pero no amplían el plan solos (R6).

## Checklist de apertura

```bash
bash .claude/skills/cerrar-sesion/scripts/preflight.sh   # ¿se arranca desde limpio?
python benchmarks/check_version.py                        # ¿las 7 superficies coinciden?
python benchmarks/check_presupuesto.py --necesito 5       # si va a medir
python benchmarks/canario.py --models <primer-modelo>     # si el lote es de >3 modelos
```

El canario **caduca a las 12 h** y tarda 20-40 min (18 tests): entra en el plan como etapa, no
como trámite.

---

## Reglas duras

Cada una viene de un fallo real; el detalle está en el CHANGELOG de la fecha.

**R1. El alcance se declara antes y se aprueba una vez.** Ocho «¿sigo?» seguidos no son un plan
aprobado: son ocho oportunidades de no ver el tamaño del trabajo.

**R2. Clasificar presentación vs medición antes de empezar.** Es lo que decide si se simula hoy o
si espera a la ventana. Saltárselo es cómo se reescribe en silencio lo que significa una cifra
que alguien ya citó.

**R3. Simular antes de aplicar, con control verde.** Si el método no reproduce lo YA publicado, no
tiene derecho a opinar sobre el futuro — que se niegue a simular. El 17-sep la simulación
desaconsejó el cambio que la motivó: jubilar suites saturadas *empeora* la discriminación.

**R4. Toda decisión va a `DECISIONES.md` en el mismo commit.** La de OpenSpec vivió tres días sólo
en la memoria de la sesión y Cristian tuvo que volver a preguntar. Una decisión que no está en el
índice no está tomada.

**R5. Consultar el dataset por `key`, nunca por `name`.** El 17-sep lo hice mal dos veces en una
sesión: concluí que a 8 modelos «nunca se les midió» una suite (tenían runs archivados) y que
faltaban sus respaldos (las carpetas usan la key). Las dos veces reporté algo alarmante que los
datos desmintieron.

**R6. Un hallazgo a mitad de camino no amplía el alcance solo.** Se reporta, se dimensiona con
números y se decide. El 17-sep «arreglar una cifra del blog» resultó ser «reescribir una página de
SEO entera»: la diferencia se vio porque se midió antes de proponer.

**R7. Nada en paralelo con una medición.** Los runners leen `suites.py` y `effort.py` en caliente,
`test_guardrails` los sabotea, y varios procesos a la vez hacen que el sistema mate las tareas en
segundo plano por memoria. Pasó el 14 y el 17-sep.

**R8. El plan dice dónde se para.** Push, publicar en el blog, recalibrar y gastar en un lote son
outward-facing o irreversibles: cada uno necesita su «ok» textual, y el plan los lista desde el
principio para que no sean una sorpresa al final.

## Qué NO hace

- No reemplaza a `DECISIONES.md` ni crea una segunda fuente de verdad: el plan es de **esta
  sesión**; lo que se decida se registra allá.
- No sustituye al `RUNBOOK-MEDICION.md` para lanzar un lote, ni al QA para publicar.
- No pide plan para trabajo pequeño: eso es fricción disfrazada de proceso.
