# CheatSheet PDF mensual

CheatSheet del benchmark generado mensualmente para emprendedores hispanohablantes.
Resume el estado del benchmark, hallazgos, rankings y recomendaciones en formato PDF
distribuible (LinkedIn, X, blogs, comunidades).

## Versiones

| Mes | PDF | Páginas | Notas |
|---|---|---|---|
| Abril 2026 | `AI_Model_Benchmark_CheatSheet_April_2026.pdf` | 1 (landscape) | Versión legacy con script `generate_pdf_deprecated.py` |
| **Mayo 2026** | `AI_Model_Benchmark_CheatSheet_Mayo_2026.pdf` | **10** | Refactor: data-driven, 9 secciones, QR codes, mes en español destacado |

## Generación

```bash
source .venv/bin/activate
python cheatsheet/generate_cheatsheet.py
```

Output:
- `cheatsheet/AI_Model_Benchmark_CheatSheet_<Mes>_<Año>.pdf`
- `cheatsheet/cheatsheet_<año>_<mes>_v2.html` (HTML intermediario)

## Estructura del cheatsheet (10 páginas)

1. **Cover** — Mes destacado en magenta, stats principales, fórmula del score
2. **Hallazgos clave del mes** — 10 insights con fechas de descubrimiento/validación
3. **Top 10 ranking global** + top 5 quality only
4. **Recomendaciones por caso de uso** — stack agente recomendado por rol
5. **Rankings por categoría** — 6 categorías (Razonamiento, Coding, Contenido, Agentes, Multi-step, NIAH-ES)
6. **Precios y suscripciones** — pay-as-you-go + 4 subs ($14 MiMo, $19 MiniMax, $20 Anthropic Pro, $30 Ollama Cloud)
7. **Estrategia local** — generalizada por VRAM (8GB / 16GB / 24-32GB / 48-64GB / 128GB / 256GB+)
8. **Mapa de proveedores** — 10 providers comparados
9. **Metodología — qué medimos** — 148 tests/modelo en 25 suites + qué NO medimos
10. **CTA final + QR** — calculadora + comunidad Skool + cómo aportar

## Diseño

- A4 landscape, fondo synthwave (#0a0a1a, #1a0a2e, #39ff14, #ff006e, #00d4ff)
- Fuentes: Inter (texto), JetBrains Mono (código/headings)
- QR codes generados con qrcode-pil (`pip install "qrcode[pil]"`)
- Render con WeasyPrint 68.1+

## Política de "guiños" al repo

Cada sección termina con una línea (clase `.guino`) recordando dónde ver
el contenido completo:
- Rankings completos → calculadora benchmarks.cristiantala.com
- Datos crudos → repo GitHub
- Methodología → CLAUDE.md
- Recomendaciones → RECOMENDACIONES.md
- Insights con números → INSIGHTS.md

Esto refuerza al cheatsheet como "puerta de entrada" al benchmark, no como contenido aislado.

## Fechas en hallazgos

Convención desde mayo 2026: cada hallazgo del mes tiene su fecha de
descubrimiento o validación entre paréntesis. Permite rastrear evolución
de hipótesis (e.g. "DeepSeek V4 Pro NIM 504" se reportó 28 abril, validado 3 mayo).

## Convención de release mensual

Cada 1ro de mes (idealmente):
1. Correr lotes pendientes del mes anterior
2. Regenerar `docs/data/models.json`
3. Actualizar `INSIGHTS.md` con sección "Update v2.X.X" del mes
4. Crear `DATASHEET_<año>-<mes>.md`
5. Generar nuevo PDF con `python cheatsheet/generate_cheatsheet.py`
6. Tag semver + push
