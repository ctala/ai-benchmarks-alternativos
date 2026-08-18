<!-- doc: vigente | verificado: 2026-08-17 -->
# Versionado y CHANGELOG — el estándar

> **Qué resuelve.** El 17-ago-2026 se hicieron **once commits** en una sesión y el CHANGELOG
> se escribió **al final, de memoria**. Salió bien porque la sesión no se cortó; si se
> cortaba, se perdía el relato de por qué cambió cada cosa — y el porqué es justo lo que
> nadie puede reconstruir después. Ese mismo día un `git reset --hard` se llevó diez
> ediciones sin commitear, así que el riesgo no es teórico.
>
> Este doc define **qué versión le toca a un cambio**, **cuándo se escribe la entrada** y
> **quién lo verifica**. Lo hace cumplir `check_changelog.py`, que corre en el pipeline y
> en el pre-push.

## 1. Los tres niveles, en el idioma de este repo

El semver genérico («cambios incompatibles / funcionalidad / arreglos») no dice nada acá,
porque este repo no publica una API: publica **números que la gente usa para decidir**. El
criterio es qué le pasa a esos números.

| Nivel | Qué significa | Ejemplos reales |
|---|---|---|
| **MAJOR** | **Cambia qué significa el número.** Una cifra citada ayer deja de ser comparable con la de hoy, y todo lo publicado afuera caduca | v4.0 → escala z-score congelada. Una recalibración (`--recalibrate`) |
| **MINOR** | **Cambia qué se mide o qué se publica**, pero la escala sigue significando lo mismo | Suite nueva al índice · el criterio de ranking pasa a ser el examen completo · un eje nuevo en la ficha |
| **PATCH** | **Datos y arreglos que no mueven la interpretación** | Modelos nuevos medidos · un fix de script · un guardrail · docs |

**La regla que decide en la práctica:** si alguien que citó una cifra nuestra tiene que
volver a mirar, es MAJOR. Si tiene que volver a mirar el *ranking* pero la cifra sigue
significando lo mismo, es MINOR. Si no tiene que hacer nada, es PATCH.

## 2. Qué tocaste → qué nivel te toca, como MÍNIMO

Esto no es orientativo: `check_changelog.py` lo verifica comparando los archivos tocados
desde el último tag contra el bump declarado.

| Si el cambio toca… | Mínimo | Por qué |
|---|---|---|
| `scoring_reference.json` (mean/std), la escala del score | **MAJOR** | Es la calibración: cambiarla reescribe todo score publicado |
| `benchmarks/tests/**`, `benchmarks/suites.py`, `providers/adapters.py` (constantes de medición), `benchmarks/scoring.py` | **MINOR** | Es **medición**: cambia el examen. R1 y R2 de `PLAN-ESTABILIDAD.md` aplican — se agrega, no se edita, y va en ventana declarada |
| `benchmarks/export_for_pages.py`, `benchmarks/elegibilidad.py` (criterios de ranking/catálogo) | **MINOR** | Es **presentación**: cambia quién aparece y en qué orden. Se simula antes contra los runs en disco |
| `benchmarks/models.py`, `benchmarks/results/**`, guardrails, generadores, docs | **PATCH** | No mueve la interpretación de ningún número |

Un cambio que toca varias filas se lleva **la más alta**.

## 3. El flujo: la entrada se escribe con el commit, no al final

```
## [No publicado]        ← cada commit agrega su línea acá, en el momento
## [v4.6.0] - 2026-08-17 ← el release cierra la sección: le pone versión y fecha
```

1. **Cada commit que toca código o datos agrega su línea a `## [No publicado]`.** Una línea:
   qué cambió y por qué. Si el cambio merece más, va con su párrafo — pero la línea es
   obligatoria y el párrafo no.
2. **El release cierra la sección**: se le pone `[vX.Y.Z] - AAAA-MM-DD` y un título que diga
   de qué se trató, se bumpean las **7 superficies** (`check_version.py` las lista) y se crea
   el **tag anotado**.
3. **`## [No publicado]` queda vacía otra vez.** Si no lo está después de un release, algo
   se olvidó.

**Por qué así y no «changelog al final»:** porque el porqué se escribe cuando está fresco.
Reconstruirlo tres horas después es escribir lo que uno *recuerda* haber hecho, que no es lo
mismo que lo que hizo. Y si la sesión se corta —o alguien resetea— lo escrito sobrevive.

## 4. El mensaje de commit

```
tipo(ámbito): qué cambió, en una línea y en presente

El PORQUÉ. Qué estaba mal, con el dato que lo prueba. Un commit que dice qué
hizo pero no por qué obliga a arqueología para tocarlo de nuevo.

Co-Authored-By: …
```

**Tipos:** `feat` (algo nuevo que se publica) · `fix` (arregla algo que estaba mal) ·
`data` (mediciones) · `release` (cierra versión) · `docs` · `refactor` (no cambia lo
publicado).

El título dice **qué**, el cuerpo dice **por qué**, con la cifra que lo sostiene. El repo
está lleno de commits que se leen solos años después porque siguen esa forma; el estándar
solo la escribe.

## 5. Qué lo hace cumplir

| Verifica | Instrumento |
|---|---|
| Las 7 superficies declaran la misma versión, con tag y entrada | `check_version.py` |
| Hay commits desde el último tag y `No publicado` está vacía | `check_changelog.py` |
| El bump declarado alcanza para lo que se tocó | `check_changelog.py --nivel` |
| El mapa de superficies no se desincroniza del código | `generate_superficies.py --check` |

Los cuatro corren en el pipeline y en el pre-push. Es la regla de siempre de este repo:
*una regla sin instrumento que la haga cumplir es una regla que ya se rompió.*

## 6. La excepción, declarada

Se puede pushear con `--no-verify` **para respaldar trabajo en una rama**, nunca para
mergear a `main`. Si se usa, el commit tiene que decir qué chequeo se saltó y por qué —
como el del 17-ago, que se saltó `validate.py` porque los datos estaban a medias con los
lotes corriendo, y por eso **no** se regeneraron las páginas.

Respaldar no es publicar. Lo que no se puede es publicar sin que los chequeos pasen.
