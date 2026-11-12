# Vuelta atrás del corte (motor-sitio 2.6)

Escrito y probado el 12-nov-2026, antes del corte. El corte todavía no existe: los hashes se completan el día que se haga.

## Qué se empuja el día del corte

Un solo push a `main` con dos commits, en este orden:

1. **El corte:** `sitio/dist` → `docs/` (copia sin borrar: `docs/data/`, `CNAME` y `robots.txt` se quedan como están; `dist` trae los mismos archivos que `docs/` más `_astro/`). En la simulación tocó 230 archivos.
2. **El archivo del change** (2.7): `openspec/changes/motor-sitio/` → `openspec/changes/archive/`. Va en el mismo push porque en `main`, S1 de `check_specs` es rojo con un change activo.

## Cómo se vuelve a `docs/` de hoy

```bash
git switch main && git pull --ff-only
git revert --no-edit <hash del commit del corte>      # solo el corte, no el archivo
GIT_SSH_COMMAND='ssh -o ServerAliveInterval=30' git push origin main > push.log; echo EXIT $?
```

- Se revierte **solo el commit del corte**. `docs/` vuelve byte a byte al de hoy (`main` en `3424e86c3`): probado en una rama desechable, `git diff main -- docs` vacío después del revert.
- Pages sigue sirviendo `docs/` desde `main`; no se toca la configuración.

## Qué pasa con el change si se revierte

- **El archivo se queda archivado en `main`.** Revertirlo dejaría un change activo en `main`, S1 sería rojo y el pre-push frenaría el revert. Una vuelta atrás que el QA bloquea no es una vuelta atrás.
- En el mismo commit del revert va una fila en `DECISIONES.md` («corte revertido el X: motivo»), y la línea del corte en el `tasks.md` archivado queda con esa nota.
- El trabajo para volver a cortar se reabre en `sitio/motor` como un change nuevo (`motor-sitio-recorte`) con solo lo que falló. El motor (`sitio/`, los guardrails y el Action) sigue en `main` y no estorba: compila `dist` y no publica nada mientras nadie copie a `docs/`.

## Cuánto se demora

| Paso | Tiempo |
|---|---|
| `git revert` local | segundos |
| pre-push (QA completo) | ~5 min (300 s en el último push) |
| Pages publica `docs/` | 1 a 3 min |
| caché de Cloudflare (`max-age=600`) | hasta 10 min |
| **Total hasta verlo en vivo** | **~15 a 20 min** |

Si el corte se rompe de una forma que tumba el QA (y por eso el pre-push no deja empujar el revert), se revisa en un checkout limpio que el rojo es del corte y no del revert, y solo entonces se empuja con `--no-verify` (regla R5 de `cerrar-sesion`).

## Antes de cortar: lo que esta prueba encontró

La sincronización `dist` → `docs/` que describe `design.md` («`regenerate_all.py` sincroniza `sitio/dist` → `docs/`») **no está implementada**. Además, después del corte los generadores de Python siguen escribiendo en `docs/`: `regenerate_all` reescribe las comparaciones, los rankings y el sitemap, y el Action regenera `docs/sitemap.xml` con `generate_sitemap.py` y lo commitea. La primera regeneración después del corte pisaría lo de Astro con el HTML de Python, sin que nada falle. Hay que resolverlo antes del corte.
