# Mercury 3 — deep_reasoning/causal_reasoning

- model_id: `inception/mercury-3`
- success: True  | final: 9.01 | quality: 10.0
- latency_total: 7.974s | tokens_per_second: 555.2
- input_tokens: 190 | output_tokens: 4427

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

## Análisis cuantitativo

| Mes | Pedidos | Quejas | Quejas por 1.000 pedidos | Días de lluvia | Tiempo promedio |
|---|---:|---:|---:|---:|---:|
| Mes 1 | 1.000 | 50 | **50** | 5 | 35 min |
| Mes 2 | 1.200 | 90 | **75** | 12 | 42 min |
| Mes 3 | 1.100 | 110 | **100** | 8 | 38 min |

La tasa de quejas se calcula como:

\[
\text{Tasa de quejas} = \frac{\text{Quejas}}{\text{Pedidos}} \times 1000
\]

- Mes 1: \(50/1000 \times 1000 = 50\)
- Mes 2: \(90/1200 \times 1000 = 75\)
- Mes 3: \(110/1100 \times 1000 = 100\)

Es decir, la tasa sube de **5% → 7,5% → 10%**.

---

## Evaluación de hipótesis

### 1. CEO: “Las quejas suben porque tenemos más pedidos”

Si solo hubiera más pedidos, la **tasa de quejas** debería mantenerse más o menos constante. Pero aquí la tasa sube todos los meses:

- Mes 1 → 2: +50% en la tasa
- Mes 2 → 3: +33% en la tasa

Además, en el Mes 3 hay **menos pedidos** que en el Mes 2 (1.100 vs 1.200) y aun así hay **más quejas** (110 vs 90).  
Por lo tanto, el volumen de pedidos no explica por sí solo el aumento.

---

### 2. CTO: “Las quejas suben por la lluvia”

La lluvia puede influir, pero los datos no la apoyan como causa principal:

- Mes 1: 5 días de lluvia → 50 quejas
- Mes 2: 12 días de lluvia → 90 quejas
- Mes 3: 8 días de lluvia → 110 quejas

El Mes 3 tiene **menos lluvia** que el Mes 2, pero **más quejas**.  
Sin datos diarios no podemos saber si las quejas ocurrieron realmente en días lluviosos o en días normales. La lluvia puede ser un factor contribuyente, pero no explica la tendencia creciente.

---

### 3. COO: “Hay un problema operacional que empeora cada mes”

Esta es la hipótesis más consistente con los datos:

- Tasa de quejas: 50 → 75 → 100 por 1.000 pedidos
- Aumenta de forma monótona todos los meses
- El aumento es lineal: +25 quejas por cada 1.000 pedidos cada mes

Este patrón sugiere un deterioro operacional: más demoras, peor servicio, más errores, menor calidad de los repartidores, problemas con restaurantes, etc.

---

## Conclusión

La hipótesis **más probable** es la del **COO**: hay un problema operacional que empeora cada mes.  
Es la única que explica que la **tasa de quejas aumente de forma sostenida**, independientemente de los pedidos y de la lluvia.

Eso no significa que la lluvia o el volumen no influyan, pero con los datos disponibles no son la causa principal.

---

## Qué datos adicionales necesitarías

Para estar seguro, necesitarías:

- **Datos diarios**: pedidos, quejas, lluvia, tiempo de entrega y retrasos por día.
- **Motivo de cada queja**: demora, comida fría, pedido incorrecto, mal trato, etc.
- **Datos operativos**: número de repartidores activos, rotación, zonas cubiertas, horas pico, cambios en la operación.
- **Indicadores de calidad**: porcentaje de entregas a tiempo, pedidos con errores, satisfacción del cliente.

Con esos datos se podría hacer una **regresión múltiple** para separar el efecto de:

- Volumen de pedidos
- Lluvia
- Tiempo de entrega
- Tendencia mensual / problema operacional

Así se podría confirmar si el “mes” sigue siendo significativo después de controlar por lluvia y volumen.  
Con solo 3 meses de datos, cualquier conclusión debe tomarse con cautela: **correlación no es causalidad**.