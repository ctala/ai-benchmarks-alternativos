# Nex-N2-Mini — business_strategy/plan_aritmetica_no_cierra

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 9.24 | quality: 10.0
- latency_total: 16.694s | tokens_per_second: 191.9
- input_tokens: 217 | output_tokens: 3203

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

**No lo aprobamos así.** El plan no llega a $6.000 USD/mes; según sus propios números llega a **$1.800 USD/mes**.

Cálculo:

| Paso | Cálculo | Resultado |
|---|---:|---:|
| Visitas al mes | — | 200.000 |
| Conversión a suscriptor | 200.000 × 1,5% | 3.000 suscriptores |
| Conversión a compra | 3.000 × 2% | 60 compradores |
| Precio del curso | 60 × $30 | **$1.800 USD** |

El objetivo es **$6.000 USD/mes**, así que necesitan **200 ventas al mes** a $30.

Con la lista estimada de 3.000 suscriptores:

- Conversión necesaria: **6,67%**, no 2%.
- O, manteniendo 2% de conversión, necesitan **10.000 suscriptores al mes**, no 3.000.
- O, manteniendo 3.000 suscriptores y 2% de conversión, necesitan un ticket promedio de **$100**, no $30.

Además: si el curso de $30 es una compra única, **no es ingreso recurrente**. Sería ingreso recurrente solo si fuera una membresía o suscripción mensual de $30.

Mi lectura: **los porcentajes pueden ser razonables, pero la multiplicación no cierra**.

Aprobación: **no para ejecutar como plan de $6.000/mes**.  
Sí podría aprobarse como experimento de captura, pero con una versión corregida:

- O aumentar conversión de compra a ~6,7%.
- O aumentar ticket promedio a ~$100.
- O convertir la oferta en membresía recurrente.
- O escalar la lista a ~10.000 suscriptores activos/mes.

**No le damos todavía.**