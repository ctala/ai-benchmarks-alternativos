---
name: cerrar-sesion
description: Cerrar la sesión del benchmark dejando todo guardado, verificado y pusheado — QA, CHANGELOG y versión, el blog, el pointer del padre y la memoria, en ese orden. Triggers "cerremos la sesión", "actualiza todo y cerremos", "/cerrar-sesion".
---

# Cerrar sesión — benchmark

Adaptado del skill homónimo del repo padre (`Estrategias/.claude/skills/cerrar-sesion/`). El
original asume un **árbol de submodules**; acá el mapa es otro y por eso existe esta versión:

| Repo | Qué es | Cómo se cierra |
|---|---|---|
| `benchmarks` (este) | **submodule** de Estrategias | commit + push, con su QA bloqueante en el hook |
| `~/Playground/sitios/cristiantala-blog` | **repo hermano**, no submodule | commit + push propios; su pre-push valida contra `models.json` |
| `Estrategias` (padre) | sólo lleva el **pointer** | se commitea DESPUÉS de pushear este repo |

**Principio rector:** un commit de cierre contiene sólo lo que ESTA sesión produjo. El padre
tiene decenas de cambios ajenos permanentes: nunca `git add -A` ahí.

---

## Paso 0 — Pre-flight (read-only)

```bash
bash .claude/skills/cerrar-sesion/scripts/preflight.sh
```

Reporta los tres repos (branch, working tree, commits sin pushear, secret scan) y si el
pointer del padre apunta al HEAD pusheado de este repo. Si dice «todo limpio», terminaste.

---

## Fases

### 1 · Discriminar qué es de la sesión
Clasificá cada archivo: **de la sesión** (entra) o **ajeno/pre-existente** (se deja). Si la
sesión fue larga o se comprimió y no estás seguro de la autoría de un archivo, **listalo y
preguntá**. En el padre, lo ajeno es la norma, no la excepción.

### 2 · Guardar lo que se commitea (antes de commitear)
1. **Artefactos regenerados.** Si la sesión tocó `benchmarks/results/`, `models.py`, `config`,
   tests o `docs/`: `python benchmarks/regenerate_all.py`. Después `generate_mapa.py` si
   aparecieron scripts nuevos.
2. **CHANGELOG (`## [No publicado]`) y versión.** Toda sesión con cambio sustantivo deja su
   línea con el **porqué**, no el qué — el qué se ve en el diff. Si hay release: las 7
   superficies, el tag anotado y `check_version.py --tag`. Ver `VERSIONADO.md`.
3. **DECISIONES.md** si se tomó (o se revirtió) una decisión de diseño: una fila, en el mismo
   commit. Si no, se re-discute en tres semanas.
4. **`ESTADO_SESION.md`**: el estado vivo entre commits, con su fecha de verificación.
5. **Memoria** (auto-memory, fuera de git): aprendizajes durables + su línea en `MEMORY.md`.
   Va antes de cerrar, no después: si la sesión se corta, se pierde.

### 3 · Guards
```bash
python benchmarks/qa.py            # completo; --pre-merge es lo que corre el hook
```
Cero secretos en tracked (lo marca el pre-flight). Si el QA reporta un bloqueante en rojo,
**no se cierra**: se arregla o se documenta por qué queda informativo con fecha de cierre.

### 4 · Commit y push, en este orden
```bash
git add <archivo> <archivo>        # SELECTIVO, nunca -A en el padre
git commit -F -                    # mensaje con el porqué + trailers del harness
git push origin main <refs/tags/vX.Y.Z si hay release>
```
Después, y sólo después, el **pointer del padre**:
```bash
git -C .. add benchmarks && git -C .. commit && git -C .. push
```
El blog, si se tocó, es un cierre aparte: su propio commit, su propio push (su hook verifica
cifras, tablas del pilar y datos marcados) y `IndexNow` si cambió contenido publicado.

### 5 · Gate humano
Mostrar el resumen consolidado —qué se commiteó por repo y qué se va a pushear— y pedir **un**
«ok». Push es outward-facing. Publicar contenido del blog necesita OK aparte.

### 6 · Verificar
Re-correr el pre-flight: 0 commits sin pushear en los repos tocados y el pointer del padre
apuntando al HEAD correcto. Cerrar con una línea por repo.

---

## Reglas duras

**R1. Sólo lo de la sesión.** Duda → preguntar, no barrer.

**R2. Este repo primero, el padre al final.** El pointer se pushea sólo cuando el commit al
que apunta ya está en el remoto; si no, apunta a un commit que nadie puede bajar.

**R3. Staging selectivo.** `git add` archivo por archivo. En el padre, sólo `benchmarks` (y el
archivo propio que se haya tocado).

**R4. El tag se empuja CON su commit,** en el mismo `git push`, y antes de cualquier
`pull --rebase`. Un rebase posterior deja el tag apuntando fuera de main y nada falla:
`git describe` salta al tag anterior. Pasó con v4.13.0, 11 días. Un tag publicado no se mueve:
se crea `vX.Y.Z+main` sobre el commit equivalente.

**R5. El QA bloqueante manda.** Si el hook frena el push, el push está mal — no el hook. Sólo
se salta con `--no-verify` cuando el rojo es demostrablemente ajeno (una carpeta sin versionar
de otra herramienta), y se verifica antes en un checkout limpio del tag.

**R6. Lo que espera aprobación NO se commitea en el repo del blog.** Varias sesiones empujan
su `main`: un commit local sale con el push de cualquiera. Borradores en worktree aparte
(`git worktree add ../blog-borrador-<slug> -b borrador/<slug>`). Pasó el 15-sep.

**R7. Limpiar los artefactos del propio trabajo antes de commitear:** `build.log`, symlinks a
`node_modules`, worktrees y ramas de borrador. Verificar el conteo de archivos esperado antes
del commit, no después.

**R8. Medir los exit codes sin pipe.** `cmd > log; echo $?`, nunca `cmd | tail; echo $?` — eso
lee el código de `tail`. Está en la lista de falsos verdes del repo y se repitió el 16-sep.

**R9. Antes de dar un verde, preguntarse dónde se está mirando.** Un sabotaje sobre un mundo
ya sucio no prueba nada: exigir verde de control antes de romper.

**R10. Memoria antes que push.** Lo durable va a la auto-memory primero.

---

## Qué NO hace

- No publica contenido del blog sin OK textual (regla #5 del repo padre).
- No commitea cambios ajenos, no fuerza push, no resuelve conflictos: si el remoto está
  adelantado, para y avisa.
- No re-mide modelos ni lanza lotes: eso es `RUNBOOK-MEDICION.md`.
