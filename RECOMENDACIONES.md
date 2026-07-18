# Recomendaciones por Caso de Uso

> **Auto-generado** por `benchmarks/generate_recomendaciones.py` desde `docs/data/models.json`.
> **No editar a mano.** Última regeneración: 2026-07-18 · 70 modelos con muestra sólida (≥50 runs).

## Cómo leer esto (importante)

**No recomendamos "el #1 del ranking".** Los modelos de la cima **empatan estadísticamente en calidad**: la diferencia entre ellos es más chica que el margen de error de la medición. Ordenarlos por decimales de score finge una precisión que los datos no tienen.

Entonces la regla es otra: **si la calidad empata, elegí por precio.** Lo que sigue es, para cada caso, el **más barato de los que empatan arriba** — y al lado, lo que te estarías gastando de más si eligieras el más caro de ese mismo grupo.

Todos los costos asumen **3,000 llamadas/mes** (≈100 por día). Para tu volumen real, usá la [calculadora](https://benchmarks.cristiantala.com/).

---

## Por tarea

### Agentes y automatizaciones (n8n, Hermes)

_El modelo decide y llama herramientas. Necesitás fiabilidad en tool calling._

- **Usá:** **Qwen 3.6 35B base (OpenRouter FP8)** — ≈$5/mes (calidad 8.10/10)
- **Lo que te ahorrás:** Qwen 3.6 Max cuesta ≈$29/mes (**6.3× más**) por apenas -0.07 de calidad — dentro del margen de error.
- _4 modelos empatan en calidad en este pilar._

### Contenido y marketing (blog, SEO, copy)

_Texto largo en español neutro. El costo manda: es alto volumen._

- **Usá:** **GPT-OSS 120B** — ≈$1/mes (calidad 8.41/10)
- **Lo que te ahorrás:** Claude Fable 5 cuesta ≈$234/mes (**278.6× más**) por apenas +0.06 de calidad — dentro del margen de error.
- _8 modelos empatan en calidad en este pilar._

### Código y debugging

_Generación y corrección de código._

- **Usá:** **DeepSeek V3.2** — ≈$1/mes (calidad 8.69/10)
- **Lo que te ahorrás:** Claude Opus 4.7 cuesta ≈$117/mes (**84.2× más**) por apenas +0.09 de calidad — dentro del margen de error.
- **Mejor open-source:** **Nemotron 3 Super** — ≈$2/mes (calidad 8.62/10)
- _16 modelos empatan en calidad en este pilar._

### Razonamiento y estrategia

_Análisis, decisiones, problemas con varios pasos._

- **Usá:** **MiniMax M3** — ≈$6/mes (calidad 8.42/10)
- **Lo que te ahorrás:** Claude Fable 5 cuesta ≈$234/mes (**41.3× más**) por apenas -0.13 de calidad — dentro del margen de error.
- **Mejor open-source:** **GLM 5** — ≈$9/mes (calidad 8.48/10)
- _12 modelos empatan en calidad en este pilar._

---

## Por presupuesto

Lo mejor que podés comprar con cada techo de gasto, a 3,000 llamadas/mes. Ordenado por calidad dentro de lo que te alcanza.

| Presupuesto | Modelo | Calidad | Costo real |
|---|---|---:|---:|
| Menos de $10/mes | **Qwen 3.6 Plus** | 8.27 | ≈$5/mes |
| Hasta $30/mes | **GPT-5.6 Luna** | 8.41 | ≈$28/mes |
| Hasta $100/mes | **GPT-5.6 Luna** | 8.41 | ≈$28/mes |

---

## El resumen de todo el benchmark

**26 modelos empatan en calidad** en la cima del ranking global.

El más barato de ese grupo — **Ministral 14B** — sale **≈$1/mes**.
El más caro — **GPT-5.6 Sol** — sale **≈$140/mes**.

Eso es **129.2× más caro** por una diferencia de calidad de **+0.04 puntos**, que está dentro del margen de error.

Si te llevás una sola cosa de este benchmark, que sea esta.
