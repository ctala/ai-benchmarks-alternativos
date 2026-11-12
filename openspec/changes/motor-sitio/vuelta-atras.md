# Vuelta atrás del corte (motor-sitio 2.6)

Escrito el 12-nov-2026 y probado dos veces antes del corte. La segunda prueba, sobre `403863aaa`, es la que vale: es la arquitectura con `publicar_dist.py`. El corte todavía no existe: los hashes se completan el día que se haga.

## Qué se empuja el día del corte

`main` está en `3424e86c3` y es la base de `sitio/motor`, así que el corte es un **avance rápido** de `main` a `sitio/motor` más un commit, en un solo push:

1. **Los commits de `sitio/motor`** (27 al 12-nov). Ahí van el motor (`sitio/`), los guardrails, el Action y el paso de `docs/` a `sitio/legado/` (los generadores de Python escriben ahí). `docs/` queda como la copia de `sitio/dist` que hace `publicar_dist.py`, con 242 archivos, `_astro/` y `.nojekyll` incluidos.
2. **El archivo del change** (2.7): `openspec/changes/motor-sitio/` → `openspec/changes/archive/`. Va en el mismo push porque en `main`, S1 de `check_specs` es rojo con un change activo. Se archiva con todas las tareas marcadas (S5).

## Cómo se vuelve a `docs/` de hoy

Ya no alcanza con revertir un commit. `docs/` dejó de ser la salida de los generadores, así que restaurar solo `docs/` no sirve: P1 falla y la siguiente regeneración vuelve a copiar `dist`. Se restaura **todo el árbol** a `3424e86c3`, menos el change archivado y los dos índices de historia:

```bash
git switch main && git pull --ff-only
git restore --source=3424e86c3 --staged --worktree -- . \
  ':(exclude)openspec/changes/archive' ':(exclude)DECISIONES.md' ':(exclude)CHANGELOG.md'
# a mano: fila en DECISIONES.md («corte revertido el X: motivo») y entrada en CHANGELOG.md
git add DECISIONES.md CHANGELOG.md && git commit -m "revert(sitio): vuelta atrás del corte motor-sitio"
```

Probado en un worktree desechable con el corte y el archivo simulados:

- `git diff 3424e86c3 -- docs` queda **vacío**: `docs/` vuelve byte a byte al de hoy.
- Fuera de `docs/`, lo único distinto de `3424e86c3` es `openspec/changes/archive/…`, `DECISIONES.md` y `CHANGELOG.md`.
- `sitio/` desaparece, y con él el Action que compila. Los generadores vuelven a escribir en `docs/`. Pages sigue sirviendo `docs/` desde `main`: no se toca la configuración.

## El pre-push frena la vuelta atrás, y por qué

El QA de pre-push (`qa.py --pre-merge`) sobre la vuelta atrás simulada dio tres rojos:

| Rojo | ¿Pasa en la vuelta atrás real? |
|---|---|
| S5 de `check_specs`: archivado con 2 tareas sin marcar | **No.** Es de la simulación, que archivó con 2.6 y 2.7 abiertas. El corte real archiva sin tareas abiertas. |
| R8 de `check_cobertura`: «test_guardrails tiene 89 pruebas y llegó a tener 118» | **Sí, siempre.** La vuelta atrás saca las 29 pruebas de sabotaje del motor, y R8 existe justamente para que el conteo no baje. |
| La prueba de R8 en `test_guardrails` | **Sí:** es el mismo rojo, visto desde la prueba. |

Por eso **la vuelta atrás se empuja con `--no-verify`**, con la regla R5 de `cerrar-sesion`: antes se verifica, en un checkout limpio del commit de la vuelta atrás, que R8 es el único rojo. No se debilita R8 para que deje pasar los reverts: un guardrail que se abre para la emergencia queda abierto.

```bash
GIT_SSH_COMMAND='ssh -o ServerAliveInterval=30' git push --no-verify origin main > push.log; echo EXIT $?
```

## Qué pasa con el change si se revierte

- **El archivo se queda archivado en `main`.** Revertirlo dejaría un change activo en `main` y S1 sería rojo.
- La fila de `DECISIONES.md` va en el commit de la vuelta atrás, y la línea del corte en el `tasks.md` archivado queda con esa nota.
- El trabajo para volver a cortar se reabre en una rama nueva desde `sitio/motor`, como un change nuevo (`motor-sitio-recorte`), con solo lo que falló.

## Cuánto se demora

| Paso | Tiempo |
|---|---|
| `git restore` y commit | segundos |
| QA en un checkout limpio, para ver que R8 es el único rojo | ~3 min (184 s en la prueba) |
| Pages publica `docs/` | 1 a 3 min |
| caché de Cloudflare (`max-age=600`) | hasta 10 min |
| **Total hasta verlo en vivo** | **~15 a 20 min** |

## Lo que encontró la primera prueba, y cómo se resolvió

La primera prueba (sobre `cd301aafd`) encontró que la copia `dist` → `docs/` que describía `design.md` no existía, y que los generadores de Python seguían escribiendo en `docs/`: la primera regeneración después del corte habría pisado lo de Astro sin que nada fallara. Se resolvió en `403863aaa`: los generadores escriben en `sitio/legado/` y `publicar_dist.py` es lo único que escribe `docs/` (P1-P3, en el QA, en `regenerate_all` y en el Action).
