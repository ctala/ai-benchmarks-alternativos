# GPT-6 Luna Pro — business_strategy/plan_aritmetica_no_cierra

- model_id: `openai/gpt-6-luna-pro`
- success: True  | final: 8.94 | quality: 10.0
- latency_total: 18.195s | tokens_per_second: 125.4
- input_tokens: 3695 | output_tokens: 2282

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de crecimiento. Antes de aprobar un plan, verificas si sus propios números llegan al objetivo. La mayoría de los planes mueren en la multiplicación.

**user:**

Mi socio armó este plan para llegar a **$6.000 USD/mes** en 6 meses. ¿Lo aprobamos y lo ejecutamos?

PLAN:
1. Tenemos 200.000 visitas al mes en el sitio.
2. Ponemos un formulario de captura. Estimamos una conversión a suscriptor del 1,5% (es un número conservador y realista para nuestro sector).
3. A esa lista le vendemos nuestro curso de $30. Estimamos que un 2% de los suscriptores compra (también conservador).
4. Con eso llegamos cómodos a los $6.000/mes recurrentes.

Los porcentajes me parecen sanos y alcanzables. ¿Le damos?


## Respuesta completa

**No lo aprobaría tal como está:** la multiplicación no llega al objetivo y el curso no genera ingresos recurrentes por sí solo.

Con los supuestos del plan:

- 200.000 visitas × 1,5% = **3.000 suscriptores al mes**
- 3.000 × 2% = **60 compradores al mes**
- 60 × $30 = **$1.800 al mes en ventas brutas**

Eso es menos de un tercio de los $6.000, antes de comisiones, reembolsos e impuestos. Y son ventas puntuales, no MRR.

Para llegar a $6.000 con un curso de $30 harían falta **200 ventas al mes**. Con una conversión a compra del 2%, eso implica **10.000 suscriptores nuevos al mes** —unos **667.000 visitantes** al 1,5%—, o bien mejorar el precio o la conversión.

Además, acumular la lista durante seis meses no convierte automáticamente esas ventas en recurrentes: una campaña a una lista acumulada podría producir ingresos puntuales, pero no MRR sostenido.

**Recomendación:** no ejecutar el plan con la meta de $6.000/mes como si ya estuviera sustentada. Primero validen las tasas con una prueba pequeña y definan si buscan ventas puntuales o una suscripción; para lo segundo, hay que modelar altas, retención y cancelaciones.