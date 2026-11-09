# Recomendaciones por Caso de Uso

> **Auto-generado** por `benchmarks/generate_recomendaciones.py` desde `docs/data/models.json`.
> **No editar a mano.** Última regeneración: 2026-11-09 · 68 modelos con muestra sólida (≥50 runs).

## Cómo leer esto (importante)

**No recomendamos "el #1 del ranking".** Los modelos de la cima **empatan estadísticamente en calidad**: la diferencia entre ellos es más chica que el margen de error de la medición. Ordenarlos por decimales de score finge una precisión que los datos no tienen.

Entonces la regla es otra: **si la calidad empata, elegí por precio.** Lo que sigue es, para cada caso, el **más barato de los que empatan arriba** — y al lado, lo que te estarías gastando de más si eligieras el más caro de ese mismo grupo.

Todos los costos asumen **3,000 llamadas/mes** (≈100 por día). Para tu volumen real, usá la [calculadora](https://benchmarks.cristiantala.com/).

---

## Por tarea

### Agentes y automatizaciones (n8n, Hermes)

_El modelo decide y llama herramientas. Necesitas fiabilidad en tool calling._

- **Usá:** **Qwen 3.5 35B** — ≈$6/mes (calidad en Agentes 8.31/10)
- **Lo que te ahorrás:** Qwen 3.5 397B cuesta ≈$16/mes (**2.7× más**) por apenas +0.29 de calidad — dentro del margen de error.
- _5 modelos empatan en calidad en este pilar._

### Contenido y marketing (blog, SEO, copy)

_Texto largo en español neutro. El costo manda: es alto volumen._

- **Usá:** **Gemma 4 31B** — ≈$2/mes (calidad en Contenido 8.88/10)
- **Lo que te ahorrás:** Claude Fable 5.1 cuesta ≈$234/mes (**144.4× más**) por apenas +0.07 de calidad — dentro del margen de error.
- _22 modelos empatan en calidad en este pilar._

### Código y debugging

_Generación y corrección de código._

- **Usá:** **DeepSeek V4 Flash 0731** — ≈$1/mes (calidad en Coding 9.52/10)
- **Lo que te ahorrás:** GPT-6 Astra cuesta ≈$234/mes (**396.6× más**) por apenas -0.01 de calidad — dentro del margen de error.
- _45 modelos empatan en calidad en este pilar._

### Razonamiento y estrategia

_Análisis, decisiones, problemas con varios pasos._

- **Usá:** **Ling 3.0 Flash** — ≈$0/mes (calidad en Razonamiento 8.53/10)
- **Lo que te ahorrás:** Claude Fable 5.1 cuesta ≈$234/mes (**780.0× más**) por apenas -0.10 de calidad — dentro del margen de error.
- _18 modelos empatan en calidad en este pilar._

---

## Por presupuesto

Lo mejor que puedes comprar con cada techo de gasto, a 3,000 llamadas/mes. Ordenado por calidad dentro de lo que te alcanza.

| Presupuesto | Modelo | Calidad | Costo real |
|---|---|---:|---:|
| Menos de $10/mes | **Qwen 3.8 Flash** | 8.91 | ≈$2/mes |
| Hasta $30/mes | **Qwen 3.8 Flash** | 8.91 | ≈$2/mes |
| Hasta $100/mes | **Qwen 3.8 Flash** | 8.91 | ≈$2/mes |

---

## El resumen de todo el benchmark

**18 modelos empatan en calidad** en la cima del ranking global.

El más barato de ese grupo — **MiMo V2.6 Flash** — sale **≈$1/mes**.
El más caro — **GPT-6 Astra** — sale **≈$234/mes**.

Eso es **168.3× más caro** por una diferencia de calidad de **-0.03 puntos**, que está dentro del margen de error.

Si te llevás una sola cosa de este benchmark, que sea esta.
