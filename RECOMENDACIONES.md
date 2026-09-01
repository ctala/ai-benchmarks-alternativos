# Recomendaciones por Caso de Uso

> **Auto-generado** por `benchmarks/generate_recomendaciones.py` desde `docs/data/models.json`.
> **No editar a mano.** Última regeneración: 2026-09-01 · 99 modelos con muestra sólida (≥50 runs).

## Cómo leer esto (importante)

**No recomendamos "el #1 del ranking".** Los modelos de la cima **empatan estadísticamente en calidad**: la diferencia entre ellos es más chica que el margen de error de la medición. Ordenarlos por decimales de score finge una precisión que los datos no tienen.

Entonces la regla es otra: **si la calidad empata, elegí por precio.** Lo que sigue es, para cada caso, el **más barato de los que empatan arriba** — y al lado, lo que te estarías gastando de más si eligieras el más caro de ese mismo grupo.

Todos los costos asumen **3,000 llamadas/mes** (≈100 por día). Para tu volumen real, usá la [calculadora](https://benchmarks.cristiantala.com/).

---

## Por tarea

### Agentes y automatizaciones (n8n, Hermes)

_El modelo decide y llama herramientas. Necesitas fiabilidad en tool calling._

- **Usá:** **DeepSeek V3.2** — ≈$5/mes (calidad en Agentes 8.70/10)
- _1 modelos empatan en calidad en este pilar._

### Contenido y marketing (blog, SEO, copy)

_Texto largo en español neutro. El costo manda: es alto volumen._

- **Usá:** **GLM 5.3 Flash** — ≈$1/mes (calidad en Contenido 8.92/10)
- **Lo que te ahorrás:** Claude Fable 5 cuesta ≈$234/mes (**196.6× más**) por apenas +0.17 de calidad — dentro del margen de error.
- _14 modelos empatan en calidad en este pilar._

### Código y debugging

_Generación y corrección de código._

- **Usá:** **Solar Pro 4** — ≈$1/mes (calidad en Coding 9.84/10)
- **Lo que te ahorrás:** Grok 4.6 cuesta ≈$29/mes (**50.5× más**) por apenas -0.18 de calidad — dentro del margen de error.
- **Mejor open-source:** **Poolside Laguna XS 2.1** — ≈$1/mes (calidad en Coding 9.71/10)
- _12 modelos empatan en calidad en este pilar._

### Razonamiento y estrategia

_Análisis, decisiones, problemas con varios pasos._

- **Usá:** **Ling 3.0 Flash** — ≈$0/mes (calidad en Razonamiento 8.33/10)
- **Lo que te ahorrás:** Claude Opus 4.7 cuesta ≈$117/mes (**390.0× más**) por apenas +0.00 de calidad — dentro del margen de error.
- _14 modelos empatan en calidad en este pilar._

---

## Por presupuesto

Lo mejor que puedes comprar con cada techo de gasto, a 3,000 llamadas/mes. Ordenado por calidad dentro de lo que te alcanza.

| Presupuesto | Modelo | Calidad | Costo real |
|---|---|---:|---:|
| Menos de $10/mes | **Qwen 3.8 Flash** | 8.53 | ≈$2/mes |
| Hasta $30/mes | **Qwen 3.8 Flash** | 8.53 | ≈$2/mes |
| Hasta $100/mes | **Qwen 3.8 Flash** | 8.53 | ≈$2/mes |

---

## El resumen de todo el benchmark

**40 modelos empatan en calidad** en la cima del ranking global.

El más barato de ese grupo — **Poolside Laguna XS 2.1** — sale **≈$1/mes**.
El más caro — **Claude Opus 5 Fast** — sale **≈$234/mes**.

Eso es **396.6× más caro** por una diferencia de calidad de **-0.03 puntos**, que está dentro del margen de error.

Si te llevás una sola cosa de este benchmark, que sea esta.
