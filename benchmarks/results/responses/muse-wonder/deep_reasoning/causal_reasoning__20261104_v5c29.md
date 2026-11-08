# Muse Wonder — deep_reasoning/causal_reasoning

- model_id: `meta/muse-wonder`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 27.985s | tokens_per_second: 108.5
- input_tokens: 179 | output_tokens: 3037

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

Con 3 datos mensuales no se puede *probar* causalidad, pero sí se puede descartar bastante. La clave es no mirar quejas absolutas, sino **quejas por pedido**.

### 1. Las tasas relevantes

|  | Mes 1 | Mes 2 | Mes 3 |
| :--- | :---: | :---: | :---: |
| Pedidos | 1.000 | 1.200 | 1.100 |
| Quejas | 50 | 90 | 110 |
| **Tasa de quejas** | **50/1000 = 5,0%** | **90/1200 = 7,5%** | **110/1100 = 10,0%** |
| Quejas cada 100 pedidos | 5 | 7,5 | 10 |
| Tiempo promedio | 35 min | 42 min | 38 min |
| Días de lluvia | 5 | 12 | 8 |

La tasa de quejas **se duplicó en 3 meses**: 5% → 7,5% → 10%.
Es un aumento perfectamente lineal de +2,5 puntos porcentuales por mes.

No es ruido chico: con n≈1.000, el intervalo aprox. de la tasa del Mes 1 es 3,6%-6,4% y el del Mes 3 es 8,2%-11,8%. No se solapan.

### 2. Testeando cada hipótesis

**CEO: "Es porque tenemos más pedidos"**

Falso como explicación principal. Si la tasa se hubiera mantenido en 5%:

* Mes 2 esperado: 1.200 x 5% = **60 quejas**. Reales: 90.
* Mes 3 esperado: 1.100 x 5% = **55 quejas**. Reales: 110.

Peor aún: del Mes 2 al Mes 3 los pedidos **bajan** de 1.200 a 1.100 (-8,3%), pero las quejas **suben** de 90 a 110 (+22,2%).

El volumen explica solo 10 de las 40 quejas extra del Mes 1 al 2. El resto es deterioro de la tasa.

**CTO: "Es por la lluvia"**

La lluvia sí explica el tiempo de entrega, pero no las quejas.

Fíjate: 35, 42 y 38 min siguen exactamente el patrón de la lluvia: 5, 12 y 8 días. Correlación lluvia-tiempo ≈ 1,0 en estos 3 puntos.

Pero las quejas no siguen ese patrón:

* Mes 2: más lluvia (12 días), tiempo peor (42 min), 7,5% de quejas.
* Mes 3: menos lluvia (8 días), tiempo mejora (38 min), pero las quejas suben a 10%.

Si la lluvia fuera la causa, el Mes 3 debería estar entre el Mes 1 y el Mes 2, no ser el peor de los tres. Correlación lluvia-tasa de quejas ≈ 0,43, débil y no monótona.

La lluvia parece un factor del *retraso*, no de la *tendencia* de quejas.

**COO: "Hay un problema operacional que empeora cada mes"**

Es la hipótesis más compatible con los datos.

Una vez que controlas por volumen (tasa) y por lluvia (que sube y baja), lo único que sube de forma sostenida mes a mes es la tasa de quejas:

5,0% → 7,5% → 10,0%

Eso es exactamente lo que verías con rotación de riders, menos capacitación, sobrecarga por rider, un restaurante/zona nueva problemática, caída de calidad, etc.: un efecto de *mes*, independiente del clima y del volumen.

### 3. Conclusión

**Más probable: el COO. Segundo: el CTO como factor parcial y transitorio en el Mes 2. Descartado como explicación principal: el CEO.**

Dicho con cuidado: con solo 3 promedios mensuales, "empeora cada mes" describe el patrón, pero todavía no sabemos *qué* operación está empeorando.

### 4. Qué dato necesito para estar seguro

Datos agregados por mes mezclan todo. Necesito datos **por día y por pedido**, idealmente de varias semanas más:

1.  **Desagregación diaria dentro de cada mes:** pedidos, quejas y lluvia por día.
    * Si en un mismo mes los días de lluvia tienen más quejas que los días secos → efecto lluvia real.
    * Si tanto días de lluvia como secos empeoran de un mes a otro → efecto operacional.

2.  **Motivo de la queja por pedido:** demora, comida fría, pedido incompleto, trato, app, etc. Si suben las quejas por demora, es una cosa; si suben las de pedido incompleto, es otra.

3.  **Datos operativos por pedido/día:** rider, zona, restaurante, rider nuevo vs. experimentado, pedidos por rider por hora, tiempo real de ese pedido y si generó queja.

Con eso podrías estimar algo simple: `Prob. de queja = efecto_mes + efecto_lluvia + efecto_tiempo + efecto_zona/rider`. Si el efecto_mes sigue subiendo después de controlar por lluvia y tiempo, el COO tiene razón y además sabrías dónde está el problema.

Sin esa desagregación, seguirán discutiendo sobre 3 promedios que no pueden separar causa de coincidencia.