# GLM 5.3 Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 59.466s | tokens_per_second: 71.7
- input_tokens: 212 | output_tokens: 4265

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

**No. Los porcentajes están bien; la multiplicación no llega.** El plan produce ~$1.800/mes, no $6.000.

## La cuenta

- 200.000 visitas × 1,5% = **3.000 suscriptores nuevos/mes**
- 3.000 × 2% = **60 ventas/mes**
- 60 × $30 = **$1.800/mes**

Te falta un factor de **3,3x** en alguna palanca.

## La trampa probable: "2% de la lista"

Si tu socio está pensando "2% de *toda* la lista acumulada" (mes 6: 18.000 suscriptores × 2% × $30 = $10.800), ese número es falso por dos razones:

1. Asume que el mismo suscriptor compra el mismo curso de $30 todos los meses.
2. Asume que los que *no* compraron en el primer email compran al 2% en los pitches siguientes. La re-oferta a no-compradores convierte a una fracción de la tasa inicial.

Y aun bajo esa lectura generosa, cruzarían $6.000 en el mes 4 sobre una premisa imposible. El estado estacionario real es $1.800/mes.

## El problema con "recurrente"

Un curso de $30 es venta única. Aunque el mes 6 facturara $6.000, el mes 7 arranca de cero: hay que volver a vender 200 cursos a una cohorte nueva. **No hay nada recurrente en este modelo.** Es una cinta de correr, no renta.

## Para que llegue a $6.000, una de estas tiene que ser verdad

- **600.000 visitas/mes** (3,3x tu tráfico) — poco probable en 6 meses
- **4,5% de opt-in** (3x tu número) — necesita un lead magnet serio
- **6,7% de compra** (3,3x lo asumido) — muy duro con lista fría
- **Precio ~$100**: 60 ventas × $100 = $6.000 con tu funnel exacto. Ojo: a $100 el 2% probablemente cae a ~1% → $3.000
- **Producto recurrente** en lugar del curso único

## Mi contra-propuesta

Combinar dos palancas: curso de $50–60 como front-end (60 ventas × $60 = $3.600 puntuales) **más** una membresía de $15–20/mes. Con 60 miembros nuevos/mes y churn del 5%, al mes 6 tenés ~315 miembros ≈ $4.700/mes y creciendo. Total: ~$8.000/mes en el mes 6, con el recurrencia que el plan promete y no entrega.

Devolvé el plan con esta corrección. Tu intuición es correcta — cada porcentaje es defendible por separado. Y justo por eso el plan no llega: encadenados, producen un tercio del objetivo. Eso es exactamente lo que hay que verificar antes de ejecutar.