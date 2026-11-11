## Context

`corte-v5` se archivó el 8-nov-2026 con sus tareas no construidas marcadas «descartada en v5.0.0: pasa al change `corte-v5-1`». La autoridad del porqué es `DECISIONES.md`.

## Decisions

- **Este change no llega a `main` activo** (`check_specs` S1): vive en su rama y se archiva antes del merge de v5.1.
- **La recalibración no se aplica sin su OK aparte.** `--recalibrate --scoring-version` recalcula y persiste la media/std de `scoring_reference.json`; se simula primero (ROADMAP v5.1, Cristian 5-nov-2026).
- **Ningún chequeo baja de bloqueante a informativo** para hacer entrar una tarea.

## Risks

- El change puede quedar quieto más de 14 días (S4). Si pasa, se cierra o se re-planifica con motivo, no se deja en el aire.
