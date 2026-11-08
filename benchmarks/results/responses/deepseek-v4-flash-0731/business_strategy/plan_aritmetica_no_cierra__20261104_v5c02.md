# DeepSeek V4 Flash 0731 — business_strategy/plan_aritmetica_no_cierra

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 9.3 | quality: 10.0
- latency_total: 13.285s | tokens_per_second: 145.4
- input_tokens: 288 | output_tokens: 1932

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

No lo apruebo todavía. El plan tiene un error de multiplicación que lo mata.

**Cálculo real:**

- 200.000 visitas × 1,5% = **3.000 suscriptores/mes**
- 3.000 suscriptores × 2% = **60 compradores/mes**
- 60 × $30 = **$1.800/mes**

La meta es **$6.000/mes**. Con tu curso de $30, necesitas **200 ventas/mes**.

Con 3.000 suscriptores nuevos al mes, tu conversión a compra tendría que ser:

**200 / 3.000 = 6,67%** — no 2%.

O si mantienes el 2%, necesitas **10.000 suscriptores nuevos/mes**, lo que implica una captación del **5%** sobre 200.000 visitas. Eso ya no es conservador.

**Además, hay un problema de “recurrente”:**

Un curso de $30 no es ingreso recurrente. Es venta única. Aunque juntes una lista grande, el 2% de la lista total no se convierte en ventas cada mes: el que ya compró, no vuelve a comprar el mismo curso. El modelo no escala como está pensado.

**Para llegar a $6.000/mes de forma honesta, necesitas al menos una de estas:**

- Subir el precio a **$100** (60 ventas × $100 = $6.000)
- O convertir a **suscripción mensual** (ej. $30/mes con retención real)
- O mejorar la captación al **5%** y la conversión a compra al **2%** — pero eso ya no es conservador, es optimista.

Los porcentajes pueden ser “sanos”, pero la meta no se alcanza con ellos. Hay que rehacer el modelo antes de ejecutar.