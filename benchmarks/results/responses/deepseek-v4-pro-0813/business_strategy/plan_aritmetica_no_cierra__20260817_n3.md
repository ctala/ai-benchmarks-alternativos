# DeepSeek V4 Pro (0813) — business_strategy/plan_aritmetica_no_cierra

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 24.544s | tokens_per_second: 97.0
- input_tokens: 208 | output_tokens: 2380

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

No, no lo apruebo para ejecutar. El plan muere en la multiplicación.

Hagamos la cuenta con sus propios números:

- 200.000 visitas/mes × 1,5% = **3.000 suscriptores/mes**
- 3.000 suscriptores × 2% de compra = **60 compradores/mes**
- 60 compradores × $30 = **$1.800/mes**

Eso es el **30% de los $6.000/mes** que buscan. Faltan **$4.200/mes**.

Además, hay un problema conceptual: si venden un curso de $30 de pago único, eso **no es ingreso recurrente**. Es ingreso mensual por ventas nuevas, pero no MRR real.

Para llegar a $6.000/mes con un producto de $30, necesitan:

- **200 compradores/mes**, no 60.
- Es decir, triplicar con creces la conversión global de visitante a comprador.

Con 200.000 visitas y precio de $30, las opciones serían algo así:

| Palanca | Valor necesario |
|---|---:|
| Conversión a suscriptor | 5% manteniendo 2% de compra |
| Conversión de suscriptor a comprador | 6,67% manteniendo 1,5% de captación |
| Precio del curso | $100 manteniendo conversiones actuales |
| Tráfico mensual | ~666.667 visitas manteniendo conversiones actuales |

O una combinación de mejoras.

Los porcentajes individuales pueden sonar “sanos”, pero el resultado no cierra.  
**No lo apruebo. Hay que ajustar al menos una palanca del modelo y volver a presentarlo.**