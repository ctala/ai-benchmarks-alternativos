## 1. Sesión 1: motor, registro y comparaciones (nada se publica)

- [ ] 1.1 Proyecto Astro 7 en `sitio/` (estático, `directory`, `trailingSlash: "always"`, `outDir: dist`) con lockfile y Node fijado. Verificar: `npm ci && npm run build` en limpio.
- [ ] 1.2 `tokens_sitio.py` genera `sitio/src/styles/tokens.css` desde `brand.json` (claro, Cercano); `check_paleta` se extiende a `sitio/src`. Verificar: sabotaje con un hex en una plantilla y otro con un token cambiado a mano.
- [ ] 1.3 `registro_paginas.py` con las 205 URLs de hoy: motor, congeladas (11) y redirects (16 + 2 que ya existen). Verificar: el conteo coincide con `docs/` y cada entrada tiene un tipo.
- [ ] 1.4 `check_registro.py` R1-R4, bloqueante en `qa.py` y dentro de `npm run build`. Verificar: un sabotaje por regla en `test_guardrails.py`, con control verde.
- [ ] 1.5 `exportar_sitio.py`: el cálculo de `generate_comparison.py` separado del HTML, con un JSON por comparación. Verificar: las pruebas actuales del generador siguen verdes y el HTML de Python no cambia.
- [ ] 1.6 Plantillas: layout base, `Tabla`, `Cifra`, comparación, `Redirect` y aviso de congelada. Verificar: R1-R4 en verde sobre `dist`.
- [ ] 1.7 `paridad_sitio.py`: las URLs y el contrato de las 37 comparaciones contra `docs/`. Verificar: un sabotaje que cambia una fila o pierde una URL sale en rojo.

## 2. Sesión 2: rankings, legado, guardrails y corte

- [ ] 2.1 Rankings (16) y variantes (6) por el mismo camino (JSON y plantilla). Verificar: paridad de contratos.
- [ ] 2.2 Legado: las páginas `motor: legado` se copian a `dist`, y `style.css` se genera desde los tokens. Verificar: R3 y R4 en verde, y `check_paleta` sobre `dist`.
- [ ] 2.3 Guardrails portados para leer lo compilado: `auditar_paginas`, `check_ganadores`, `check_paleta`, `check_espanol_neutro`, `check_fichas_alcanzables`, `check_agentico_publicado` A3, `check_indice_calidad` I3/I8, `check_calculator`, `check_version`, `check_cortes`, `check_consistency`, `check_cobertura`, `check_version_en_nombre`, y el sitemap y `llms.txt`. Verificar: cada sabotaje adaptado, con control verde.
- [ ] 2.4 Desde `corte-v5-1`: la línea «medido en» en la comparación (1.4.c), un CTA único al go-link sin `skool.com` ni «gratis» (1.4.d) y `dateModified`/`lastmod` solo con cambio de contenido (5.4). Verificar: un guardrail con su sabotaje por cada uno.
- [ ] 2.5 `regenerate_all.py` y el Action: Node, `npm ci`, el build y el sha de `models.json` embebido y verificado. Verificar: todos los pasos del Action en un venv limpio.
- [ ] 2.6 Vista previa en móvil y escritorio, y OK de Cristian. Después, el commit del corte (`dist` → `docs/`), el push con OK y la verificación del sitio en vivo. Verificar: 205 URLs en vivo y la reversa probada en una rama.
- [ ] 2.7 Archivar el change sin tareas abiertas.
