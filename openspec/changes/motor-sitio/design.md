## Context

Hoy el sitio son 204 URLs que escriben a mano 9 generadores de Python. Se publican con GitHub Pages en modo legacy, desde `main:/docs`.

| Tipo | Cuántas | Generador | Sesión |
|---|---|---|---|
| Comparaciones | 37: 10 por familia, 27 de versión exacta | `generate_comparison.py` | 1 |
| Rankings | 16 | `generate_rankings.py` | 2 |
| Variantes | 6 | `generate_variants.py` | 2 |
| Redirects ya existentes | 2 | `generate_comparison.py` | 1 |
| Fichas | 132 | `generate_model_cards.py` | 1b |
| Landings | 9 | `generate_manual_landings.py` | 1b |
| Home con la calculadora, proveedores, `mismo-modelo-distinto-proveedor` | — | — | 1b |

Todas las páginas comparten `docs/style.css` y llevan un `contrato-pagina` embebido que leen los auditores (`contrato_pagina.py`). El porqué de cada decisión está en `DECISIONES.md` (fila del 11-nov-2026, «Motor del sitio»); este documento dice cómo.

## Goals / Non-Goals

**Goals:**
- Que una página no pueda mostrar en silencio un modelo que salió del ranking.
- Que ninguna cifra se escriba a mano.
- Que la paleta solo pueda salir de los tokens.
- Publicar sin cortar el sitio y con reversa en un commit.

**Non-Goals:**
- Comparaciones por familia nuevas, fichas nuevas, entrada por ocasión y comparador libre (changes 2 en adelante).
- Migrar fichas, landings y home (change 1b).
- El modo oscuro (1b).

## Decisions

### D1. Astro 7 en `sitio/`, estático, compila a `sitio/dist`
`output: "static"`, `build.format: "directory"`, `trailingSlash: "always"`: son las mismas URLs que hoy (`/slug/`). Es la versión que ya usa `sitios/aprenderepite`.

`docs/` no se toca hasta el corte. En el corte, `regenerate_all.py` sincroniza `sitio/dist` → `docs/`, preservando `docs/data/`, `CNAME`, `robots.txt` y la verificación de dominio.

*Alternativa descartada:* GitHub Actions como fuente de Pages. Cambia la configuración de Pages y la reversa deja de ser un `git revert`.

### D2. Python decide, Astro dibuja
`benchmarks/exportar_sitio.py` escribe `sitio/src/datos/` (ignorado por git; se regenera en `prebuild`). Lleva:
- `registro.json`;
- un JSON por página con todo lo que la página muestra: filas, ganadores, campeón, eje por eje, cobertura, FAQ y contrato.

Los generadores separan *calcular* de *escribir HTML*. El cálculo es el mismo código que hoy y conserva sus pruebas. Astro no decide nada: si una plantilla necesita «quién gana», el dato viene en el JSON.

*Alternativa descartada:* reimplementar la lógica en JS. Serían dos autoridades de lo mismo.

### D3. Registro: `benchmarks/registro_paginas.py`
Es la única declaración de qué URLs existen. Deriva las entradas de las configuraciones de los generadores (`COMPARISONS`, `RANKINGS`, `FAMILIES`, `LANDINGS`) y de `models.json` (fichas), y les aplica lo declarado a mano:
- `motor`: `astro` o `legado`;
- `congelada`: `{fecha, motivo}`;
- `redirect_a`.

Campos de cada entrada: `url`, `tipo`, `familias` u `ocasion`, `motor`, `congelada`, `redirect_a`, `generador`.

### D4. Tokens desde `brand.json`, nivel Cercano y claro por defecto
`benchmarks/tokens_sitio.py` lee `themes.light` y `typography` de `brand.json` y escribe `sitio/src/styles/tokens.css` (custom properties). Las plantillas y estilos usan solo `var(--…)`. `check_paleta` se extiende: un hex en `sitio/src` fuera de `tokens.css` falla, y `tokens.css` tiene que coincidir con `brand.json`.

Mecánica Cercano (manual § 3c):
- un kicker `//` por sección;
- verde solo en el CTA y el cursor;
- cards con borde sutil y sin sombra, salvo una destacada;
- esquinas de 2px;
- títulos de más de 6 palabras en Inter 700.

### D5. Validadores del registro: `benchmarks/check_registro.py`
Corren dentro de `npm run build` (en `prebuild` y `postbuild`) y como bloqueantes en `qa.py`, cada uno con su sabotaje:
- **R1** · una página Astro muestra un modelo fuera del ranking vigente (`ranked` falso: retirado, reemplazado, histórico o en evaluación) sin estar congelada.
- **R2** · una cifra visible del HTML compilado no viene de un componente que la marque (`data-cifra`). Las celdas de tabla, `<Cifra>` y los conteos la emiten. Quedan exentos los años, las fechas y una lista con motivo. Se mira lo compilado y no la fuente: así también se caza la cifra escrita en el código de una plantilla.
- **R3** · una URL del sitio publicado (`docs/sitemap.xml` y los directorios de `docs/`) no existe en `dist` ni como página ni como redirect.
- **R4** · un `index.html` de `dist` no tiene entrada en el registro.
- **R5** · un modelo fuera del ranking no tiene motivo registrado, o `ranked` contradice su elegibilidad. Es un error de datos: el export tampoco publica (decisión de Cristian, 11-nov-2026).

**R1 estricta en las comparaciones por familia** (Cristian, 11-nov-2026, opción A). Al 11-nov, las 10 comparaciones por familia mostraban 44 modelos que no rankean, con la etiqueta «no rankea»: 35 del histórico, 4 con examen incompleto, 2 de esfuerzo, 2 en hardware propio y 1 sin motivo (corregido, R5). La tabla lleva solo los rankeados. Al pie de cada comparación va un enlace «Versiones anteriores →» a las fichas de los que salen, así que ninguno queda sin camino.

### D6. Redirects con plantilla propia
`Redirect.astro` escribe meta refresh 0, canonical, `noindex, follow` y el `contrato-pagina` de tipo redirect. Es el patrón que ya usa el sitio, y así `auditar_paginas` los sigue leyendo. No se usa `redirects` de Astro porque no emite el contrato.

### D7. Congeladas
Se compilan con la plantilla de hoy y los datos de hoy. Los modelos históricos siguen en `models.json`, así que ninguna cifra se escribe a mano. Arriba llevan un aviso con la fecha, el motivo y el enlace a la comparación vigente que corresponda. Siguen indexables.

### D8. Legado (sesión 2)
Las páginas `motor: legado` se copian tal cual desde `docs/` a `dist`. `style.css` se genera desde los tokens, así que el tema claro llega al sitio entero el día del corte.

### D9. Paridad: `benchmarks/paridad_sitio.py`
- **URLs:** las mismas de `docs/`, o un redirect declarado.
- **Contenido:** por cada página migrada, el mismo contrato que publica hoy (`recomienda`, `ordena_por`, `filas` por tabla). Las diferencias a propósito se declaran con su motivo: las 16 que redirigen, en el registro, y las filas que salen por R1, con el motivo de elegibilidad de cada modelo.

## Páginas de versión exacta (aprobadas por Cristian el 11-nov-2026)
Redirigen a su comparación por familia (16):

| Destino | Páginas |
|---|---|
| `claude-vs-chatgpt` | `fable-5-vs-gpt-5-5`, `fable-5-vs-gpt-5-6-sol`, `gpt-5.6-vs-fable-5`, `gpt-5.6-vs-claude-opus-4-8`, `gpt-5.6-vs-claude-sonnet-4-6`, `gpt-5.6-luna-vs-claude-haiku-4-5`, `gpt-5.6-terra-vs-claude-sonnet-4-6`, `gpt-5.6-sol-vs-claude-opus-4-8` |
| `claude-haiku-sonnet-opus` | `fable-5-vs-opus-4-8`, `fable-5-vs-claude-sonnet-4-6` |
| `grok-vs-chatgpt` | `grok-4.3-vs-gpt-5-5`, `grok-4.5-vs-gpt-5-6` |
| `grok-vs-claude` | `grok-4.5-vs-claude-sonnet-4-6` |
| `gemini-vs-chatgpt` | `gpt-5.6-vs-gemini-3.5-flash` |
| `deepseek-vs-chatgpt` | `gpt-5.6-vs-deepseek-v4` |
| `gemini-flash-o-pro` | `gemini-3.5-flash-vs-gemini-2.5-flash` |

Quedan congeladas con fecha 11-nov-2026 (11). El motivo: a un lado le falta su página de familia, y se reevalúan en el change 2.
- `gpt-5.6-vs-gpt-5.5`, `gpt-5.6-luna-vs-terra`, `gpt-5.6-terra-vs-sol`, `gpt-5.6-luna-vs-sol`
- `grok-4.5-vs-grok-4.3`
- `glm-5.2-vs-glm-5.1`, `glm-5.2-vs-claude-opus-4-8`
- `fable-5-vs-minimax-m3`, `gpt-5.6-vs-minimax-m3`
- `nemotron-3-ultra-vs-deepseek-v4-flash`
- `diffusiongemma-vs-gemma-4`

Search Console por URL en 16 meses: ninguna pasa de 6 clics. La que más trae, `gpt-5.6-vs-claude-opus-4-8` (6 clics, 372 impresiones), redirige a `claude-vs-chatgpt`.

## Risks / Trade-offs

- [Dos motores durante la transición] → El registro declara el motor de cada URL, y R3 y R4 cubren las dos.
- [El cálculo se separa del HTML en `generate_comparison.py`, 1.382 líneas] → El HTML de Python se sigue generando hasta el corte, y la paridad de contratos compara los dos.
- [Node en el CI] → `npm ci` con lockfile y la versión de Node fijada. `check_ci` mira el paso.
- [Las congeladas siguen indexables] → Llevan fecha y enlace a lo vigente. Si el change 2 crea la familia, pasan a redirect.

## Migration Plan

1. Sesión 1: esqueleto, tokens, registro, R1-R4, paridad, comparaciones y redirects. Todo se compila a `sitio/dist`; nada se publica.
2. Sesión 2: rankings y variantes, legado, guardrails portados, Action, vista previa, OK de Cristian y corte.
3. Reversa: `git revert` del commit del corte. Pages sigue sirviendo `docs/`.
