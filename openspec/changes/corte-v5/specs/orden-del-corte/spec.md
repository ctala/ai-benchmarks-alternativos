## Purpose

Define cómo se planifica, se vigila y se cierra un corte mayor del benchmark sin dejar el plan en el aire ni debilitar los guardrails.

## ADDED Requirements

### Requirement: El plan de un corte mayor vive en OpenSpec dentro del benchmark
Un corte mayor MUST planificarse como un change de OpenSpec en `openspec/changes/` del propio benchmark, con `proposal.md`, `design.md` y `tasks.md`. El change MUST nombrar a `DECISIONES.md` y MUST NOT repetir el porqué de una decisión: apunta a la fila.

#### Scenario: Change sin puntero a DECISIONES
- **WHEN** un change activo no nombra a `DECISIONES.md` en su propuesta ni en su diseño
- **THEN** `check_specs.py` falla (S6) y el push se bloquea

### Requirement: Ningún change queda en el aire
Como mucho un change MUST estar activo a la vez. Un change activo MUST tener un commit o una fecha de creación de hace 14 días o menos. En `main` MUST NOT haber ningún change activo. Un change archivado MUST NOT tener tareas sin marcar; una tarea que no se hará se marca hecha con «descartada: motivo».

#### Scenario: Change activo en main
- **WHEN** se intenta hacer push a `main` con un change activo en `openspec/changes/`
- **THEN** `check_specs.py` falla (S1) y el hook de pre-push lo bloquea

#### Scenario: Change que nadie toca
- **WHEN** pasan más de 14 días sin un commit que toque el change activo
- **THEN** `check_specs.py` falla (S4) hasta que se avance, se archive o se descarte con motivo

#### Scenario: Archivo con tareas abiertas
- **WHEN** un change archivado conserva una tarea `- [ ]`
- **THEN** `check_specs.py` falla (S5)

### Requirement: Ningún guardrail se debilita durante el corte
Durante un corte mayor un chequeo bloqueante MUST NOT pasar a informativo ni apagarse sin una fila en `DECISIONES.md`. Si el corte deja un chequeo obsoleto, el chequeo MUST cambiar en el mismo commit que su prueba de sabotaje. El conteo de pruebas de sabotaje MUST NOT bajar.

#### Scenario: Chequeo que el esquema nuevo rompe
- **WHEN** `check_consistency.py` falla porque `models.json` cambió de esquema
- **THEN** se adapta el chequeo y su prueba en el mismo commit, y sigue siendo bloqueante

### Requirement: La auditoría de guardrails es gate del corte
Antes de la primera tarea de v5, los chequeos del QA MUST estar auditados en una tabla con veredicto por fila (confiable, verde vacío o sin prueba), y Cristian MUST haberla leído y dado su ok textual.

#### Scenario: Auditoría pendiente
- **WHEN** se intenta avanzar una tarea de los grupos 2 a 5 con el grupo 1 abierto
- **THEN** la sesión se detiene y lo reporta; no se avanza
