# Recomendaciones por Caso de Uso

> **Auto-generado** por `benchmarks/generate_recomendaciones.py` desde `docs/data/models.json`.
> **No editar a mano.** Última regeneración: 2026-07-12 · 98 modelos con muestra sólida (≥50 runs).

## Cómo leer esto (importante)

**No recomendamos "el #1 del ranking".** Los modelos de la cima **empatan estadísticamente en calidad**: la diferencia entre ellos es más chica que el margen de error de la medición. Ordenarlos por decimales de score finge una precisión que los datos no tienen.

Entonces la regla es otra: **si la calidad empata, elegí por precio.** Lo que sigue es, para cada caso, el **más barato de los que empatan arriba** — y al lado, lo que te estarías gastando de más si eligieras el más caro de ese mismo grupo.

Todos los costos asumen **3,000 llamadas/mes** (≈100 por día). Para tu volumen real, usá la [calculadora](https://benchmarks.cristiantala.com/).

---

## Por tarea

### Agentes y automatizaciones (n8n, Hermes)

_El modelo decide y llama herramientas. Necesitás fiabilidad en tool calling._

- **Usá:** **Claude Haiku 4.5 (suscripción)** — ≈$23/mes (calidad 8.76/10)
- **Lo que te ahorrás:** Claude Opus 4.8 (suscripción) cuesta ≈$117/mes (**5.0× más**) por apenas +0.15 de calidad — dentro del margen de error.
- _4 modelos empatan en calidad en este pilar._

### Contenido y marketing (blog, SEO, copy)

_Texto largo en español neutro. El costo manda: es alto volumen._

- **Usá:** **MiniMax M3 (directo / sub)** — ≈$6/mes (calidad 9.17/10)
- **Lo que te ahorrás:** GPT-5.6 Sol cuesta ≈$140/mes (**24.6× más**) por apenas -0.26 de calidad — dentro del margen de error.
- **Mejor open-source:** **DeepSeek R1 (reasoning)** — ≈$12/mes (calidad 9.01/10)
- _10 modelos empatan en calidad en este pilar._

### Código y debugging

_Generación y corrección de código._

- **Usá:** **DeepSeek V4 Flash (OpenRouter)** — ≈$1/mes (calidad 8.40/10)
- **Lo que te ahorrás:** Claude Sonnet 4.6 (suscripción) cuesta ≈$70/mes (**72.4× más**) por apenas -0.14 de calidad — dentro del margen de error.
- _16 modelos empatan en calidad en este pilar._

### Razonamiento y estrategia

_Análisis, decisiones, problemas con varios pasos._

- **Usá:** **DeepSeek R1 (reasoning)** — ≈$12/mes (calidad 9.05/10)
- **Lo que te ahorrás:** Claude Opus 4.8 (suscripción) cuesta ≈$117/mes (**9.8× más**) por apenas +0.21 de calidad — dentro del margen de error.
- _4 modelos empatan en calidad en este pilar._

---

## Por presupuesto

Lo mejor que podés comprar con cada techo de gasto, a 3,000 llamadas/mes. Ordenado por calidad dentro de lo que te alcanza.

| Presupuesto | Modelo | Calidad | Costo real |
|---|---|---:|---:|
| Menos de $10/mes | **MiniMax M3 (directo / sub)** | 8.58 | ≈$6/mes |
| Hasta $30/mes | **DeepSeek R1 (reasoning)** | 8.82 | ≈$12/mes |
| Hasta $100/mes | **DeepSeek R1 (reasoning)** | 8.82 | ≈$12/mes |

---

## El resumen de todo el benchmark

**8 modelos empatan en calidad** en la cima del ranking global.

El más barato de ese grupo — **DeepSeek V4 Flash (OpenRouter)** — sale **≈$1/mes**.
El más caro — **Claude Opus 4.7 (suscripción)** — sale **≈$117/mes**.

Eso es **120.6× más caro** por una diferencia de calidad de **+0.01 puntos**, que está dentro del margen de error.

Si te llevás una sola cosa de este benchmark, que sea esta.
