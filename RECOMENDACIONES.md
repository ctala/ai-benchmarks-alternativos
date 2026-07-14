# Recomendaciones por Caso de Uso

> **Auto-generado** por `benchmarks/generate_recomendaciones.py` desde `docs/data/models.json`.
> **No editar a mano.** Última regeneración: 2026-07-14 · 64 modelos con muestra sólida (≥50 runs).

## Cómo leer esto (importante)

**No recomendamos "el #1 del ranking".** Los modelos de la cima **empatan estadísticamente en calidad**: la diferencia entre ellos es más chica que el margen de error de la medición. Ordenarlos por decimales de score finge una precisión que los datos no tienen.

Entonces la regla es otra: **si la calidad empata, elegí por precio.** Lo que sigue es, para cada caso, el **más barato de los que empatan arriba** — y al lado, lo que te estarías gastando de más si eligieras el más caro de ese mismo grupo.

Todos los costos asumen **3,000 llamadas/mes** (≈100 por día). Para tu volumen real, usá la [calculadora](https://benchmarks.cristiantala.com/).

---

## Por tarea

### Agentes y automatizaciones (n8n, Hermes)

_El modelo decide y llama herramientas. Necesitás fiabilidad en tool calling._

- **Usá:** **Qwen 3.6 35B base (OpenRouter FP8)** — ≈$5/mes (calidad 8.11/10)
- **Lo que te ahorrás:** Qwen 3.6 Max cuesta ≈$29/mes (**6.3× más**) por apenas -0.03 de calidad — dentro del margen de error.
- _6 modelos empatan en calidad en este pilar._

### Contenido y marketing (blog, SEO, copy)

_Texto largo en español neutro. El costo manda: es alto volumen._

- **Usá:** **GPT-OSS 120B** — ≈$1/mes (calidad 8.23/10)
- **Lo que te ahorrás:** GPT-5.6 Sol cuesta ≈$140/mes (**166.1× más**) por apenas +0.04 de calidad — dentro del margen de error.
- _18 modelos empatan en calidad en este pilar._

### Código y debugging

_Generación y corrección de código._

- **Usá:** **Nemotron 3 Nano Omni 30B-A3B Reasoning** — ≈$0/mes (calidad 8.53/10)
- **Lo que te ahorrás:** Mistral Large cuesta ≈$29/mes (**None× más**) por apenas -0.06 de calidad — dentro del margen de error.
- _14 modelos empatan en calidad en este pilar._

### Razonamiento y estrategia

_Análisis, decisiones, problemas con varios pasos._

- **Usá:** **Qwen3 Coder** — ≈$3/mes (calidad 8.29/10)
- **Lo que te ahorrás:** Claude Opus 4.8 cuesta ≈$117/mes (**40.6× más**) por apenas +0.12 de calidad — dentro del margen de error.
- _11 modelos empatan en calidad en este pilar._

---

## Por presupuesto

Lo mejor que podés comprar con cada techo de gasto, a 3,000 llamadas/mes. Ordenado por calidad dentro de lo que te alcanza.

| Presupuesto | Modelo | Calidad | Costo real |
|---|---|---:|---:|
| Menos de $10/mes | **GLM 5** | 8.37 | ≈$9/mes |
| Hasta $30/mes | **DeepSeek R1 (reasoning)** | 8.39 | ≈$12/mes |
| Hasta $100/mes | **DeepSeek R1 (reasoning)** | 8.39 | ≈$12/mes |

---

## El resumen de todo el benchmark

**16 modelos empatan en calidad** en la cima del ranking global.

El más barato de ese grupo — **DeepSeek V4 Flash (OpenRouter)** — sale **≈$1/mes**.
El más caro — **GPT-5.6 Sol** — sale **≈$140/mes**.

Eso es **143.8× más caro** por una diferencia de calidad de **-0.08 puntos**, que está dentro del margen de error.

Si te llevás una sola cosa de este benchmark, que sea esta.
