## Context

Estado de partida, leído el 3-nov-2026 en `main` (v4.17.0):

- 115 modelos rankeados, 143 tests en 4 pilares, juez Phi-4 vía OpenRouter decidiendo el 31 % de los runs del índice (`simular_sin_juez.py`, control verde 115/115).
- QA bloqueante de 20 chequeos en el hook de pre-push; 35 pruebas de sabotaje; 3 chequeos sin prueba (`check_agentico_publicado`, `check_ci`, `check_presupuesto`); 1 verde vacío encontrado y arreglado hoy (`check_release_mensual`).
- `OCASIONES.md` (borrador) tiene las respuestas de Cristian a las 5 preguntas y `FUENTES-EXTERNAS.md` (borrador) el veredicto por fuente con las páginas primarias verificadas el 3-nov.
- El único antecedente de OpenSpec sobre este benchmark vivió en el repo padre y se archivó a los 6 días con 8 de 43 tareas.
- Nuestro banco Harbor (`tareas-agente/harbor-*`) ya corre sobre el harness de Terminal-Bench 2.0. Los envíos al leaderboard 2.0 están cerrados; el sitio muestra 4.0.

## Goals / Non-Goals

**Goals**
- Que la recomendación por ocasión salga de un filtro duro comunitario más la capa propia (gap español, tareas de founder con datos LATAM, pass^k, modelos baratos y locales), con el precio mensual al volumen declarado.
- Que el conjunto base quede definido por un número, no por una opinión: cobertura de las tres fuentes sobre los 115.
- Que los guardrails merezcan confianza antes de construir encima.
- Que el plan sobreviva sesiones y se cierre.

**Non-Goals**
- Replicar apps o stacks que otro benchmark ya mide (NocoDB, Gmail, Sheets): suspendido por Cristian.
- Cambiar el modelo principal del Spark o gastar en nube sin ok.
- Tocar los prompts de las suites existentes (se agregan o se jubilan, no se editan).

## Decisions

Cada decisión está en `DECISIONES.md` con su porqué; acá solo el puntero y la consecuencia de diseño.

| Decisión (DECISIONES.md, 3-nov-2026) | Consecuencia en el diseño |
|---|---|
| OpenSpec entra, dentro del benchmark y solo para un corte mayor | `openspec/` en la raíz del benchmark; el hub no se toca. `check_specs` S6 exige que el change nombre a `DECISIONES.md` |
| Un change se completa y se archiva; en `main` no queda ninguno | `check_specs.py` S1-S6, bloqueante, nació en verde, 6 pruebas de sabotaje sobre un `openspec/` desechable |
| v5.0.0 mayor por 6 ocasiones | `scoring_reference.json` se recalibra en el release (`--recalibrate --scoring-version v5.0`); el esquema de `models.json` agrega `ocasiones` |
| Enriquecer, no replicar: fuentes comunitarias como filtro duro | `fuentes_externas.py` ingesta con fecha y licencia; las cifras externas viajan como **banda** por fuente, nunca entran al promedio propio |
| Lo no medido se mide con el harness oficial | camino `externos/` declarado en `check_caminos` antes de la primera corrida; la publicación dice «medido por nosotros con el harness oficial vX, N intentos, fecha» |
| Ningún guardrail se debilita durante el corte | la auditoría es la tarea 1 y su tabla es gate; un chequeo que queda obsoleto cambia con su prueba y su fila en el mismo commit |

## Risks / Trade-offs

- **Cobertura chica de las fuentes.** Toolathlon-Verified tiene 7 modelos. Si el conjunto base queda en 15, la recomendación completa cubre pocos modelos y el resto va con «sin dato comunitario». Se acepta: es honesto y se amplía midiendo nosotros.
- **Terminal-Bench cambió de versión.** Las cifras públicas son de 2.0 y el sitio muestra 4.0. Se ingesta la versión que tenga dataset público con trayectorias y se declara cuál.
- **Esquema nuevo rompe `check_consistency` y el blog.** Es el momento de la tentación de aflojar. Regla: el chequeo cambia con su prueba, no se apaga.
- **Spark.** La corrida oficial depende de la GPU y el modelo principal está abajo por decisión de Cristian. No se sube; se espera su ventana.

## Open Questions

- Si Terminal-Bench 2.0 no reabre envíos, ¿publicamos la corrida solo en nuestro sitio y HF, sin PR al leaderboard? Propuesta: sí, con la etiqueta de corrida independiente.
- Volúmenes por defecto de cada ocasión: se parte con los de `OCASIONES.md` y la calculadora los deja cambiar; se revisan con el primer mes de uso.
