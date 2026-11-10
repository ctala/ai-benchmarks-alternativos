# Muse Ember — deep_reasoning/causal_reasoning

- model_id: `meta/muse-ember`
- success: True  | final: 8.82 | quality: 10.0
- latency_total: 12.492s | tokens_per_second: 444.0
- input_tokens: 179 | output_tokens: 5546

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

Con 3 meses agregados no se puede probar causalidad, pero sí se pueden falsar hipótesis. La clave es no mirar quejas absolutas, sino **tasa de quejas**.

### 1. Las tasas relevantes

| Mes | Pedidos | Quejas | **Tasa de quejas** | Tiempo medio | Lluvia |
|---|---|---|---|---|---|
| 1 | 1.000 | 50 | **50/1.000 = 5,0%** | 35 min | 5 días |
| 2 | 1.200 | 90 | **90/1.200 = 7,5%** | 42 min | 12 días |
| 3 | 1.100 | 110 | **110/1.100 = 10,0%** | 38 min | 8 días |

Cambios:
- Mes 1->2: pedidos +20%, quejas +80%, tasa +2,5 pp (+50% relativa)
- Mes 2->3: pedidos **-8,3%**, quejas **+22,2%**, tasa +2,5 pp (+33% relativa), tiempo -9,5%, lluvia -33%
- Mes 1->3: pedidos +10%, quejas +120%, tasa **+100%**

La tasa se duplica en 3 meses, con un aumento perfectamente lineal de +2,5 pp por mes. No es ruido: el IC95% aproximado es 3,7-6,4% en Mes 1, 6,0-9,0% en Mes 2 y 8,2-11,8% en Mes 3. Mes 1 vs Mes 3: z≈4,4, p<0,001.

El Mes 3 es el mes discriminante: pedidos bajan, lluvia baja y tiempo baja, pero las quejas suben.

### 2. CEO: "Suben porque hay más pedidos"

Si fuera solo volumen, la tasa debería mantenerse en ~5%.

Quejas esperadas con tasa 5%:
- Mes 2: 1.200 x 5% = **60 esperadas vs 90 reales** (+30 de exceso)
- Mes 3: 1.100 x 5% = **55 esperadas vs 110 reales** (+55 de exceso, el doble)

Además, de Mes 2 a 3 hay **100 pedidos menos y 20 quejas más**. Eso contradice directamente la hipótesis.

El CEO confunde numerador con tasa. El volumen explica como máximo una fracción mínima del aumento.

**Hipótesis descartada como explicación principal.**

### 3. CTO: "Suben por la lluvia"

Orden de magnitud:
- Lluvia: Mes 2 (12) > Mes 3 (8) > Mes 1 (5)
- Tasa de quejas: Mes 3 (10%) > Mes 2 (7,5%) > Mes 1 (5%)

No coinciden. Si la lluvia fuera la causa principal, el Mes 3 debería mejorar respecto al Mes 2, porque llovió 33% menos y el tiempo medio también mejoró de 42 a 38 min. En cambio, es el peor mes en tasa.

Una estimación ingenua: si el salto Mes 1->2 (+2,5 pp) se debiera a +7 días de lluvia, los +3 días del Mes 3 vs Mes 1 predecirían una tasa de ~6,1% (~67 quejas), no 10% (110 quejas).

La lluvia *podría* haber contribuido al salto Mes 1->2, donde lluvia y tiempo subieron juntos. Pero no puede explicar el Mes 3.

**Hipótesis insuficiente. Como máximo un factor secundario.**

### 4. COO: "Hay un problema operacional que empeora"

Es la única que predice lo observado: una tendencia al alza de la tasa independiente del volumen, la lluvia y el tiempo medio.

La tasa sube monótonamente 5% -> 7,5% -> 10% mientras pedidos, lluvia y tiempo no son monótonos. Por eliminación, es la más probable.

Matiz importante: el problema operacional **no parece ser solo el tiempo medio**, porque el tiempo medio mejoró en el Mes 3 y las quejas empeoraron. O el problema es otro —comida fría, pedidos erróneos, cancelaciones, trato del rider, preparación en restaurante, app— o el tiempo medio esconde la cola: puede bajar la media pero subir el % de entregas muy tarde (>45/60 min).

### Veredicto

1. **COO > CTO > CEO.** CEO falsado, CTO no explica el Mes 3, COO es consistente con todo.
2. No está probado. Con n=3 puntos agregados, cualquier otra variable que también suba monótonamente —nueva zona, cambio de clientela, personal nuevo, un proceso de queja más fácil— parecería un "problema operacional".

### Qué dato adicional necesitas para estar seguro

Lo más valioso no es otro mes agregado, es **desagregar**:

**1. Serie diaria (90 observaciones en vez de 3).** Es lo que rompe la colinealidad. Con datos diarios puedes comparar dentro del mismo mes: ¿la tasa es más alta en días de lluvia que en días secos? ¿Y la tasa en días secos también sube de mes en mes? Si lo primero es sí y lo segundo también, CTO y COO son ambos verdaderos y puedes cuantificar cada efecto. Si solo sube la base en días secos, es COO.

**2. Quejas por motivo.** ¿Suben las de "tarde" (coherente con lluvia/tiempo) o suben las de "frío, equivocado, faltante, rider"? Si suben motivos no relacionados con el clima, es operacional.

**3. Distribución del tiempo, no solo la media.** Mediana, p90, % >45 min, % cancelados, tiempo en restaurante vs tiempo en moto. La media del Mes 3 puede estar ocultando un empeoramiento de la cola.

**4. Desglose por zona / restaurante / rider / cliente nuevo vs recurrente.** Descarta un efecto Simpson: quizá abrieron una zona nueva mala en el Mes 2-3.

**5. Métricas operacionales independientes de quejas y control de sesgo de reporte.** % a tiempo, cancelaciones, rotación de riders, tamaño de flota, y una encuesta de satisfacción aleatoria post-entrega. Si las quejas suben pero la satisfacción medida activamente no, quizá solo se hizo más fácil quejarse.

Con la serie diaria + motivo de queja + lluvia día a día, podrías ajustar: `tasa_queja_diaria ~ pedidos + lluvia + tendencia_temporal`. Solo entonces podrías separar clima de deterioro operativo.