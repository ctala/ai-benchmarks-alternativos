# Tencent Hy4 — deep_reasoning/causal_reasoning

- model_id: `tencent/hy4`
- success: True  | final: 8.49 | quality: 10.0
- latency_total: 56.758s | tokens_per_second: 97.5
- input_tokens: 218 | output_tokens: 5535

## Entrada exacta (lo que recibió el modelo)

**user:**

Una startup de delivery tiene estos datos de los ultimos 3 meses:

Mes 1: 1000 pedidos, 50 quejas, tiempo promedio 35 min, lluvia 5 dias
Mes 2: 1200 pedidos, 90 quejas, tiempo promedio 42 min, lluvia 12 dias
Mes 3: 1100 pedidos, 110 quejas, tiempo promedio 38 min, lluvia 8 dias

El CEO dice: "Las quejas suben porque tenemos mas pedidos".
El CTO dice: "Las quejas suben por la lluvia".
El COO dice: "Hay un problema operacional que empeora cada mes".

Analiza los datos cuantitativamente. Calcula las tasas relevantes.
Determina cual hipotesis es mas probable y por que.
Identifica que dato adicional necesitarias para estar seguro.


## Respuesta completa

Aquí tienes el análisis cuantitativo. El error de los tres directivos es mirar **valores absolutos** en lugar de **tasas**. Al normalizar, el panorama cambia por completo.

### 1. Tasas relevantes (el corazón del análisis)

| Métrica | Mes 1 | Mes 2 | Mes 3 | Δ M1 → M2 | Δ M2 → M3 |
| :--- | :---: | :---: | :---: | :---: | :---: |
| Pedidos | 1.000 | 1.200 | 1.100 | +20,0% | **−8,3%** |
| Quejas (abs) | 50 | 90 | 110 | +80,0% | **+22,2%** |
| **Tasa de quejas (Q/P)** | **5,0%** | **7,5%** | **10,0%** | **+2,5 pp** | **+2,5 pp** |
| Lluvia (días) | 5 | 12 | 8 | +140% | **−33,3%** |
| Tiempo prom. (min) | 35 | 42 | 38 | +20,0% | **−9,5%** |
| Quejas / día de lluvia | 10,0 | 7,5 | **13,8** | −25% | **+83%** |

*(pp = puntos porcentuales)*

---

### 2. Veredicto de las hipótesis

#### ❌ CEO ("Es por más pedidos") — **Refutado**
Si el volumen fuera el motor, al bajar los pedidos en Mes 3 (1.200 → 1.100) las quejas deberían haber bajado. Ocurrió lo contrario: subieron de 90 a 110. Además, de M1 a M2 los pedidos crecieron un 20% pero las quejas un 80%. **La tasa por pedido se duplicó (5% → 10%)**. El volumen amplifica, pero no genera el problema.

#### ⚠️ CTO ("Es por la lluvia") — **Refutado como causa principal**
La lluvia explica razonablemente el *pico* del Mes 2, pero **no explica la tendencia**. En Mes 3 llovió un 33% menos (12 → 8 días) y, sin embargo, la tasa de quejas saltó de 7,5% a 10,0%. Incluso ajustando por clima, pasamos de 7,5 a **13,8 quejas por cada día de lluvia**. Mejoró el clima, empeoró el servicio.

#### ✅ COO ("Problema operacional que empeora cada mes") — **La más probable (con un matiz clave)**
Es la única hipótesis que sobrevive a los datos. La tasa de quejas es **estrictamente monótona y lineal: +2,5 pp exactos cada mes**, con total independencia de que suban o bajen los pedidos, la lluvia *y el tiempo de entrega*.

> **🧠 Hallazgo estadístico:** Si ajustas un modelo aditivo simple `Tasa = Base + Efecto_Lluvia + Efecto_Tiempo + Tendencia_Mensual`, los 3 puntos fuerzan a que las variaciones de lluvia y tiempo se cancelen entre sí, asignando **el 100% del deterioro a un factor constante de +2,5 pp/mes**. Es la huella digital de una degradación estructural latente, no de un evento externo.

**El matiz importante para el COO:** Él probablemente cree que el problema es la *velocidad*, pero el tiempo promedio **mejoró** en Mes 3 (42 → 38 min) mientras las quejas seguían subiendo. El problema operacional **no es de tardanza, es de calidad** (ej. pedidos incompletos, comida fría, errores de empaque, bugs en la app o rotación de riders nuevos).

---

### 3. Qué dato adicional necesito para estar seguro

Con solo 3 filas agregadas, cualquier regresión está sobreajustada (3 datos = 3 variables). Para pasar de "muy probable" a "confirmado", pediría esto, en orden de prioridad:

1. **🔴 Crítico — Taxonomía de las quejas (motivo):** El desglose por categoría (`Tardanza` / `Producto equivocado` / `Frío` / `Cobro` / `Cancelación`). Como el tiempo bajó en M3, predigo que el crecimiento del 10% viene de *errores de picking/packing*. Sin esto, el "problema operacional" sigue siendo una caja negra.
2. **🟠 Metodológico — Microdata diaria (≈90 filas, no 3):** Datos por día/pedido para correr una regresión de Poisson o logística y separar limpiamente el efecto de la lluvia *del día exacto* del efecto *de la semana/mes*. Evita la falacia ecológica de comparar promedios mensuales.
3. **🟠 Operacional — Percentil 90/95 del tiempo (no solo la media):** El promedio de 38 min en M3 puede esconder una varianza rota (ej. 90% de pedidos en 25 min + un 10% en 120 min que concentran todas las quejas). La media engaña; la cola no.
4. **🟡 Contexto — Change-log interno:** ¿Hubo cambio de empaques, nuevo algoritmo de asignación, ingreso masivo de riders o alta de nuevos restaurantes entre Mes 1 y Mes 3? Esto anclaría el "+2,5 pp/mes" a una decisión concreta (ej. desgaste de un proceso mal calibrado).

**Resumen en una frase para el comité:** *"No estamos creciendo mal, estamos degradándonos bien: cada mes fallamos 2,5 puntos más por pedido, incluso cuando llueve menos, vendemos menos y entregamos más rápido. Miren el empaque, no el cronómetro."*