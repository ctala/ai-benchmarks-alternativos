## Why

El sitio (benchmarks.cristiantala.com, 204 URLs) se arma con generadores de Python que escriben el HTML a mano. Una página que nadie regenera queda mostrando modelos que ya salieron del ranking: hoy 24 de las 27 comparaciones de versión exacta están así. Además, posicionan búsquedas que casi nadie hace: en 16 meses, ninguna pasa de 6 clics. La demanda está en las familias: «claude vs chatgpt» tiene 2.900 búsquedas al mes y «comparador de ia», 160. Antes de construir comparaciones por familia, fichas nuevas o la entrada por ocasión, hace falta un motor que no se desactualice. Decisión y motivo en `DECISIONES.md` (fila del 11-nov-2026, «Motor del sitio»).

## What Changes

- **Astro como capa de presentación** (`sitio/`, Astro 7). Lee al compilar los datos que exporta Python. Python sigue siendo la autoridad de los datos y de las decisiones de cada página: quién gana, qué filas, el contrato.
- **Tema Cercano, claro por defecto**, desde los tokens de `~/Playground/brand-manuals/cristian-tala/tokens/brand.json`. Ningún color queda fuera de los tokens. El modo oscuro llega en el change 1b.
- **Registro de páginas** (`benchmarks/registro_paginas.py`). Cada URL se declara con su tipo, sus familias u ocasión, su motor (Astro o legado) y, si está congelada, la fecha y el motivo. Si redirige, el destino. El build falla si una página muestra un modelo fuera del ranking vigente sin estar congelada, si tiene una cifra escrita a mano, si una URL publicada hoy no tiene página ni redirect, o si una página compilada no está en el registro.
- **Las mismas URLs que hoy.** De las 27 comparaciones de versión exacta, 16 redirigen a su comparación por familia y 11 quedan congeladas con fecha y motivo.
- **Guardrails portados** para revisar lo compilado (~14), cada uno con su sabotaje adaptado.
- **Publicación sin cortar:** se compila a `sitio/dist`, se verifica la paridad contra el sitio actual, Cristian aprueba la vista previa y un solo commit compila hacia `docs/`. Pages no cambia de configuración y la reversa es un `git revert`.
- **Lo que llega desde `corte-v5-1`:**
  - la línea «medido en» en la comparación (1.4.c);
  - un CTA único al go-link (1.4.d): hoy 204 páginas enlazan a `skool.com` con CAR cerrada;
  - `dateModified` y `lastmod` solo cuando cambia el contenido (5.4).

Fuera de este change, uno a la vez: el **1b** (fichas, landings y home con la calculadora, y el modo oscuro), las comparaciones por familia y fichas nuevas, la entrada por ocasión y el comparador libre.

## Capabilities

### New Capabilities
- `motor-sitio`: cómo se declara, compila, valida y publica cada página del sitio.

### Modified Capabilities
(ninguna)

## Impact

- `sitio/` nuevo (Astro, `package.json`, `package-lock.json`).
- Generadores: `generate_comparison.py`, y en la sesión 2 `generate_rankings.py` y `generate_variants.py`, emiten un JSON por página además del HTML hasta el corte.
- Guardrails que leen `docs/`: pasan a leer lo compilado.
- `regenerate_all.py` y el Action suman la compilación con Node.
- Cuatro sesiones o más (eran dos; se amplió dos veces el 11-nov: la prosa de rankings sale del dato y el legado pasa a claro; ver DECISIONES). La publicación necesita un OK aparte.
