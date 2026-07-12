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

- **Usá:** **Qwen 3.6 35B base (OpenRouter FP8)** — ≈$5/mes (calidad 8.17/10)
- **Lo que te ahorrás:** Claude Fable 5 (suscripción) cuesta ≈$234/mes (**50.5× más**) por apenas +0.12 de calidad — dentro del margen de error.
- **Si tenés hardware propio:** **DiffusionGemma 26B-A4B (DGX Spark Q8_0)** — ≈$2/mes (calidad 8.39/10)
- _11 modelos empatan en calidad en este pilar._

### Contenido y marketing (blog, SEO, copy)

_Texto largo en español neutro. El costo manda: es alto volumen._

- **Usá:** **DeepSeek V4 Flash (OpenRouter)** — ≈$1/mes (calidad 8.84/10)
- **Lo que te ahorrás:** GPT-5.6 Sol cuesta ≈$140/mes (**143.8× más**) por apenas +0.07 de calidad — dentro del margen de error.
- _15 modelos empatan en calidad en este pilar._

### Código y debugging

_Generación y corrección de código._

- **Usá:** **Mistral Nemo** — ≈$0/mes (calidad 7.91/10)
- **Lo que te ahorrás:** GPT-5.6 Sol cuesta ≈$140/mes (**1268.2× más**) por apenas +0.07 de calidad — dentro del margen de error.
- **Si tenés hardware propio:** **Gemma 4 12B (Spark llama-server Q4_K_M)** — ≈$1/mes (calidad 7.99/10)
- _56 modelos empatan en calidad en este pilar._

### Razonamiento y estrategia

_Análisis, decisiones, problemas con varios pasos._

- **Usá:** **DeepSeek V4 Flash (OpenRouter)** — ≈$1/mes (calidad 8.78/10)
- **Lo que te ahorrás:** Claude Fable 5 (suscripción) cuesta ≈$234/mes (**241.2× más**) por apenas +0.12 de calidad — dentro del margen de error.
- **Si tenés hardware propio:** **Gemma 4 12B (Spark llama-server, reasoning)** — ≈$1/mes (calidad 8.07/10)
- _17 modelos empatan en calidad en este pilar._

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

**13 modelos empatan en calidad** en la cima del ranking global.

El más barato de ese grupo — **DeepSeek V4 Flash (OpenRouter)** — sale **≈$1/mes**.
El más caro — **GPT-5.6 Sol** — sale **≈$140/mes**.

Eso es **143.8× más caro** por una diferencia de calidad de **-0.05 puntos**, que está dentro del margen de error.

Si te llevás una sola cosa de este benchmark, que sea esta.
