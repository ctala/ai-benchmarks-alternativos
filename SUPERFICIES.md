<!-- doc: generado -->
# Superficies sincronizadas — qué tiene que coincidir con qué

> **AUTO-GENERADO** por `benchmarks/generate_superficies.py`. **No editar a mano.**
> La tabla de versión sale del registro que el guardrail realmente ejecuta
> (`check_version.SUPERFICIES`), no de una copia — por eso no puede desincronizarse.

Este repo publica el mismo hecho en varios lugares a la vez. Cada lugar es una
**superficie**, y una superficie que se queda atrás no rompe nada: el sitio carga, el
pipeline pasa, los auditores dan verde. Simplemente **el repo dice dos cosas distintas
de sí mismo** y quien lea la equivocada se lleva la vieja.

Por eso cada clase de sincronía tiene un instrumento que la hace cumplir. La regla del
repo —*una regla sin instrumento que la haga cumplir es una regla que ya se rompió*—
aplica especialmente acá, porque es donde más barato es olvidarse.

---

## Cómo agregar una superficie nueva

Si vas a publicar un dato que ya existe en otro lado, no lo escribas y sigas: **es una
superficie, y necesita entrar al registro en el MISMO commit.**

1. **¿Es versión?** Agregá una fila a `SUPERFICIES` en `benchmarks/check_version.py`
   (archivo + `patron` o `json_key` + por qué importa). Este doc se regenera solo.
2. **¿Es otra cosa?** Agregala a `CLASES` en `benchmarks/generate_superficies.py` y
   nombrá el guardrail que la hace cumplir. Si todavía no existe, **ese guardrail es
   parte del trabajo**, no un pendiente.
3. Corré `python benchmarks/generate_superficies.py` y commiteá el doc.

**Lo que NO sirve:** documentar la superficie en prosa y confiar en acordarse. Es
exactamente lo que falló — la docstring de `check_version` nombraba seis superficies
mientras el código leía cuatro, y las dos que faltaban estaban desalineadas.

---

## Versión — las 7 superficies que declaran qué versión es ésta

Todas tienen que decir lo mismo. Lo verifica **`benchmarks/check_version.py`**, que corre en `regenerate_all.py` y en el Action.

| Superficie | Qué declara | Por qué importa |
|---|---|---|
| `scoring_reference.json` | la referencia congelada del score | es la fuente de la calibración; si miente, todo score publicado queda sin origen |
| `sitio/legado/data/models.json` | el dataset que sirve el sitio | es lo que consume la calculadora y cualquiera que baje los datos |
| `CHANGELOG.md` | la entrada más reciente | publicar sin entrada es publicar sin traza. Pasó con v4.1 |
| `README.md` | el encabezado | es lo primero que ve un humano y lo que GitHub muestra en la home del repo. El 14-ago decía «Version 3.1.1»: cuatro releases atrás |
| `sitio/legado/index.html` | el hero de la calculadora | es la versión que lee un visitante del sitio |
| `schema.org:version` | el Dataset de schema.org | es lo que leen Google y los crawlers de IA. El 14-ago decía v4.0 mientras el hero decía v4.1, y nada fallaba |
| `schema.org:softwareVersion` | el SoftwareApplication de schema.org | ídem: superficie de buscadores, invisible para quien mira la página |

Y dos condiciones más, que no son archivos:

| Requisito | Por qué |
|---|---|
| **git tag** para la versión declarada | Sin tag no hay punto de retorno: no se puede reconstruir qué se publicó ni comparar contra el release anterior |
| **entrada en el CHANGELOG** | Publicar sin entrada es publicar sin traza |

---

## Las otras clases de sincronía

| Clase | Qué sincroniza | Fuente única | Guardrail |
|---|---|---|---|
| **Conteos** | modelos catalogados · testeados · rankeados · tests · suites, citados en README, ROADMAP, MODELOS.md y las landings | `sitio/legado/data/models.json` | `benchmarks/sync_doc_counts.py` |
| **Scores citados en prosa** | toda cifra de score que aparezca en un doc VIVO (README, MODELOS, CLAUDE, AGENTS, RECOMENDACIONES, COMPARATIVA) | `sitio/legado/data/models.json` | `benchmarks/check_consistency.py` |
| **Campos que la calculadora lee** | cada campo que `sitio/legado/app.js` consume, y cada umbral de filtro | `sitio/legado/data/models.json` | `benchmarks/check_calculator.py` |
| **Cifras del pilar del blog** | el post cornerstone en el repo hermano `cristiantala-blog` | `sitio/legado/data/models.json` | `benchmarks/check_blog_consistency.py` |
| **Cortes por eje del sitio** | las páginas que ordenan por UNA suite en vez de por un promedio | `sitio/legado/data/models.json` | `benchmarks/check_cortes.py` |
| **Afirmaciones de método** | que ningún doc VIVO afirme una metodología que ya se reemplazó | `DECISIONES.md` | `benchmarks/check_claims.py` |
| **Ciclo de vida de la documentación** | la marca `<!-- doc: vigente | verificado: FECHA -->` de cada doc | la fecha de verificación humana | `benchmarks/check_docs.py` |
| **Caminos de medición** | que todo lo que llame a una API de modelos esté sancionado | la lista `SANCIONADOS` | `benchmarks/check_caminos.py` |
| **Ranking v5 e histórico** | quién rankea, quién va al histórico y con qué era, en models.json, la tabla histórico de la calculadora y las fichas por modelo; y la nota pública que una declaración de proveedor pide en su ficha | `examen_v5`, `historico` y `era` de `sitio/legado/data/models.json`; `nota_publica` de `proveedores_declarados.json` | `benchmarks/validate.py` |
| **Tabla histórico de la home** | las filas de la tabla histórico de sitio/legado/index.html, con quién reemplazó a cada modelo y su era, contra el export | `historico`, `reemplazado_por` y `era` de `sitio/legado/data/models.json` (la escribe `generate_historico.py`) | `benchmarks/check_calculator.py` |

### Detalle de cada una

**Conteos** — reescribe los bloques `<!-- AUTO:campo -->…<!-- /AUTO -->`. **Un conteo fuera de un bloque AUTO no se sincroniza**: si lo escribes a mano, caduca solo.

**Scores citados en prosa** — compara lo citado contra el dato. Ignora a propósito los snapshots con fecha (CHANGELOG, DATASHEET_*, INSIGHTS): ésos DEBEN conservar el valor del momento — reescribir la historia sería el bug, no el fix.

**Campos que la calculadora lee** — caza un campo que el JS lee y el export dejó de emitir, y un umbral fuera del rango real de los datos (un filtro que no filtra a nadie es decorativo).

**Cifras del pilar del blog** — un rescoring caduca TODAS las cifras del post — prosa, tablas y FAQ — y puede dejar una recomendación de seguridad peligrosa.

**Cortes por eje del sitio** — Existen porque los promedios esconden: Gemini 3.6 Flash es #3 de 80 en calidad agéntica y #76 de 80 en el índice general, y el pilar Agentes tampoco lo mostraba (#65) porque también promedia. El chequeo avisa cuando se mide una suite decisiva y nadie le hizo su corte, falla si una página quedó desincronizada, y falla si un corte AGÉNTICO corona a un modelo que no corre dentro de un agente — pasó con Llama 3.1 8B, #4 en «tareas largas» y rompe el bucle de herramientas.

**Afirmaciones de método** — `check_consistency` caza CIFRAS caducas; ésta caza CLAIMS caducos — prosa sin números que fue correcta y hoy dice lo contrario. El README llegó a tener un título que decía «Score = combinación ponderada (NO solo calidad)» mientras la decisión vigente era exactamente la opuesta, y sobrevivió a dos versiones. Citar un error está permitido: lo que se prohíbe es sostenerlo.

**Ciclo de vida de la documentación** — avisa cuando un doc VIGENTE lleva >90 días sin que nadie lo mire. Verifica que ALGUIEN LO MIRÓ, no que el contenido sea correcto — es honesto sobre ese techo.

**Caminos de medición** — un instrumento que se puede esquivar escribiendo un script nuevo, se esquiva. Costó cinco pozos ya tapados, re-pisados en una tarde.

**Ranking v5 e histórico** — B4 exige que un rankeado tenga el examen v5 entero y que el histórico no rankee y diga su era; C4 exige que cada ficha publicada del histórico lo diga y que cada nota pública aparezca en su ficha (DECISIONES, 5-nov-2026).

**Tabla histórico de la home** — C6 compara cada fila con el export y falla si una fila o el título dicen «antes del examen v5» de quien lo rindió en la ventana (DECISIONES, 7-nov-2026).
