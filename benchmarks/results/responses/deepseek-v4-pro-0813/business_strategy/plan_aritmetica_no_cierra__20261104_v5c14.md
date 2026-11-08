# DeepSeek V4 Pro (0813) — business_strategy/plan_aritmetica_no_cierra

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 29.967s | tokens_per_second: 58.8
- input_tokens: 287 | output_tokens: 1762

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

No lo apruebo todavía: **sus propios números no llegan a $6.000/mes**.

La multiplicación del plan da:

- **200.000 visitas/mes** × **1,5%** conversión a suscriptor = **3.000 suscriptores/mes**
- **3.000 suscriptores** × **2%** que compran = **60 compradores/mes**
- **60 compradores** × **$30** = **$1.800/mes**

Es decir, el plan genera **$1.800/mes**, no $6.000/mes. Faltan **$4.200/mes**, un 70% del objetivo.

Para llegar a **$6.000/mes** con esos supuestos, necesitarían una de estas cosas:

| Palanca | Valor actual | Valor necesario |
|---|---:|---:|
| Tráfico mensual | 200.000 | ~666.667 visitas |
| Conversión visitante → suscriptor | 1,5% | ~5% |
| Conversión suscriptor → comprador | 2% | ~6,67% |
| Precio del curso | $30 | ~$100 |

O una combinación de varias.

Además, hay que aclarar algo importante: si el curso cuesta **$30 por única vez**, eso **no es ingreso recurrente**. Si la idea es venderlo todos los meses a nuevos suscriptores, igual estaríamos hablando de **$1.800/mes de ingresos nuevos**, no $6.000/mes.

**Veredicto:**  
El plan, tal como está escrito, **no aprueba el objetivo**. No es un problema de que los porcentajes sean “conservadores”, sino de que la multiplicación no cierra.

Para darle luz verde necesitaríamos ajustar al menos una de estas variables: tráfico, conversión, precio, recurrencia real o sumar upsells/ventas complementarias.