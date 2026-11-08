# GLM 5.3 — business_strategy/plan_aritmetica_no_cierra

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 58.802s | tokens_per_second: 77.3
- input_tokens: 212 | output_tokens: 4547

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

**No lo aprobamos. La multiplicación no llega.**

Hagamos la cuenta que el plan no hace:

- 200.000 visitas × 1,5% = **3.000 suscriptores/mes**
- 3.000 suscriptores × 2% = **60 compradores/mes**
- 60 compradores × $30 = **$1.800/mes**

Eso es el **30% del objetivo**. El plan queda corto por $4.200/mes: necesita un 3,3x que no está en ninguna parte de los cuatro pasos.

## Dónde está el error

Casi seguro tu socio está asumiendo que la lista se acumula: 3.000 suscriptores nuevos cada mes, y el 2% de compra aplica sobre la **lista total**, no sobre los nuevos. En ese mundo:

- Mes 1: $1.800 → Mes 2: $3.600 → Mes 3: $5.400 → Mes 4: $7.200

Y sí, cruza $6.000 en el mes 4. Pero ese supuesto dice que el 2% de TODA la lista compra **todos los meses, para siempre**. Eso no es "conservador": ignora el churn, el decaimiento de aperturas, y el hecho de que un curso de $30 se compra una vez (que es justo lo que hace falso llamarlo "recurrente" — es un pago único, no MRR).

Los porcentajes individuales están bien. El problema no era ningún número suelto: era lo que pasa cuando se multiplican.

## Qué tendría que moverse para cerrar la brecha

Cada palanca por sí sola necesita moverse 3,3x:

| Palanca | Hoy | Necesitaría |
|---|---|---|
| Precio | $30 | ~$100 |
| Tasa de compra | 2% | ~6,7% |
| Captura | 1,5% | ~5% |
| Tráfico | 200k | ~667k |

Ninguna es realista en 6 meses. **Combinadas, sí:**

- Precio a $59 (con order bump o upsell para subir el ticket promedio)
- Captura al 2% (con un lead magnet real, no un formulario pelado)
- 3% de compra con una secuencia de emails bien armada

200.000 × 2% × 3% × $59 = **$7.080/mes**. Ahí sí hay margen.

## Para aprobar algo

Vuelve con:

1. **Modelo por cohorte**, no flujo plano — que muestre explícitamente qué pasa con los suscriptores viejos mes a mes.
2. **Ticket promedio > $50** vía upsell, no vía subir el precio a secas.
3. Si el argumento de venta es "recurrente", que sea una **membresía de $10–15/mes**, no un curso de pago único disfrazado de MRR.

Con eso, reviso números otra vez. Tal como está, el plan cumple exactamente lo que predice — y lo que predice son $1.800.