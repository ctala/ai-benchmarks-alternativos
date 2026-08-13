# Recomendaciones por Caso de Uso

> **Auto-generado** por `benchmarks/generate_recomendaciones.py` desde `docs/data/models.json`.
> **No editar a mano.** Última regeneración: 2026-08-13 · 82 modelos con muestra sólida (≥50 runs).

## Cómo leer esto (importante)

**No recomendamos "el #1 del ranking".** Los modelos de la cima **empatan estadísticamente en calidad**: la diferencia entre ellos es más chica que el margen de error de la medición. Ordenarlos por decimales de score finge una precisión que los datos no tienen.

Entonces la regla es otra: **si la calidad empata, elegí por precio.** Lo que sigue es, para cada caso, el **más barato de los que empatan arriba** — y al lado, lo que te estarías gastando de más si eligieras el más caro de ese mismo grupo.

Todos los costos asumen **3,000 llamadas/mes** (≈100 por día). Para tu volumen real, usá la [calculadora](https://benchmarks.cristiantala.com/).

---

## Por tarea

### Agentes y automatizaciones (n8n, Hermes)

_El modelo decide y llama herramientas. Necesitás fiabilidad en tool calling._

- **Usá:** **Qwen 3.7 Flash** — ≈$1/mes (calidad 8.17/10)
- **Lo que te ahorrás:** Claude Fable 5 cuesta ≈$234/mes (**383.6× más**) por apenas -0.14 de calidad — dentro del margen de error.
- **Mejor open-source:** **Ministral 14B** — ≈$1/mes (calidad 7.93/10)
- _9 modelos empatan en calidad en este pilar._

### Contenido y marketing (blog, SEO, copy)

_Texto largo en español neutro. El costo manda: es alto volumen._

- **Usá:** **Llama 3.3 70B** — ≈$2/mes (calidad 8.73/10)
- **Lo que te ahorrás:** Claude Fable 5 cuesta ≈$234/mes (**152.9× más**) por apenas +0.09 de calidad — dentro del margen de error.
- _5 modelos empatan en calidad en este pilar._

### Código y debugging

_Generación y corrección de código._

- **Usá:** **Nex-N2-Mini** — ≈$0/mes (calidad 9.60/10)
- **Lo que te ahorrás:** GPT-5.6 Terra Pro cuesta ≈$28/mes (**59.4× más**) por apenas +0.02 de calidad — dentro del margen de error.
- _7 modelos empatan en calidad en este pilar._

### Razonamiento y estrategia

_Análisis, decisiones, problemas con varios pasos._

- **Usá:** **Ling 3.0 Flash** — ≈$0/mes (calidad 8.33/10)
- **Lo que te ahorrás:** Claude Opus 4.7 cuesta ≈$117/mes (**390.0× más**) por apenas +0.00 de calidad — dentro del margen de error.
- _14 modelos empatan en calidad en este pilar._

---

## Por presupuesto

Lo mejor que podés comprar con cada techo de gasto, a 3,000 llamadas/mes. Ordenado por calidad dentro de lo que te alcanza.

| Presupuesto | Modelo | Calidad | Costo real |
|---|---|---:|---:|
| Menos de $10/mes | **Tencent Hy3** | 8.65 | ≈$2/mes |
| Hasta $30/mes | **Tencent Hy3** | 8.65 | ≈$2/mes |
| Hasta $100/mes | **Tencent Hy3** | 8.65 | ≈$2/mes |

---

## El resumen de todo el benchmark

**22 modelos empatan en calidad** en la cima del ranking global.

El más barato de ese grupo — **Qwen 3.7 Flash** — sale **≈$1/mes**.
El más caro — **Claude Fable 5** — sale **≈$234/mes**.

Eso es **383.6× más caro** por una diferencia de calidad de **-0.16 puntos**, que está dentro del margen de error.

Si te llevás una sola cosa de este benchmark, que sea esta.
