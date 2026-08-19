# Qwen 3.8 Max — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.8-max`
- success: True  | final: 7.93 | quality: 10.0
- latency_total: 197.221s | tokens_per_second: 47.8
- input_tokens: 256 | output_tokens: 9421

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

No. **Así como está, no lo aprueben ni lo ejecuten.**

Los porcentajes pueden parecer “sanos”, pero la multiplicación no llega al objetivo. Y ese es exactamente el punto: antes de ejecutar, hay que verificar si los números del propio plan dan.

## La cuenta real del plan

Fórmula:

> Ingresos = visitas × conversión a suscriptor × conversión a compra × ticket

Con sus números:

> 200.000 × 1,5% × 2% × USD 30  
> = 200.000 × 0,015 × 0,02 × 30  
> = **USD 1.800/mes**

Desglose:

| Métrica | Cálculo | Resultado |
|---|---:|---:|
| Visitas mensuales | — | 200.000 |
| Suscriptores | 200.000 × 1,5% | 3.000 |
| Compradores | 3.000 × 2% | 60 |
| Ingreso | 60 × USD 30 | **USD 1.800/mes** |

Meta: **USD 6.000/mes**  
Resultado del plan: **USD 1.800/mes**  
Faltante: **USD 4.200/mes**  
Necesitan multiplicar el plan por **3,33x**.

---

## El error probable: confundir “lista acumulada” con ingreso recurrente

Si el curso es un pago único de USD 30, no hay recurrencia automática. Cada mes necesitan nuevos compradores.

Si acumulan suscriptores durante 6 meses:

> 3.000 suscriptores/mes × 6 meses = 18.000 suscriptores

Si el 2% compra alguna vez:

> 18.000 × 2% = 360 ventas totales  
> 360 × USD 30 = USD 10.800 totales en 6 meses

Eso equivale a:

> USD 10.800 / 6 = **USD 1.800/mes en promedio**

Tampoco llegan a USD 6.000/mes.  
Y si dicen “llegamos cómodos”, están confundiendo una venta puntual con ingreso mensual recurrente.

---

## ¿Qué se necesitaría para llegar a USD 6.000/mes?

Con un producto de USD 30, necesitan:

> USD 6.000 / USD 30 = **200 ventas/mes**

Hoy el plan produce:

> 60 ventas/mes

Para llegar a 200 ventas/mes manteniendo las otras variables iguales, necesitan una de estas cuatro cosas:

| Palanca | Situación actual | Para llegar a USD 6.000/mes |
|---|---:|---:|
| Tráfico | 200.000 visitas/mes | **666.667 visitas/mes** |
| Captura | 1,5% | **5,0%** |
| Venta | 2% | **6,67%** |
| Ticket | USD 30 | **USD 100** |

Es decir: el plan actual necesita mejorar una variable principal en **3,33x**, o combinar mejoras más pequeñas entre varias variables.

---

## Ejemplo de plan corregido que sí daría

Una combinación posible:

> 200.000 visitas/mes  
> × 2,5% de captura  
> × 3% de venta  
> × USD 40 de ticket  
> = USD 6.000/mes

Cálculo:

> 200.000 × 0,025 = 5.000 suscriptores  
> 5.000 × 0,03 = 150 ventas  
> 150 × USD 40 = **USD 6.000/mes**

Eso ya es otra conversación. Pero el plan original, con 1,5%, 2% y USD 30, no llega.

---

## Si el producto fuera una suscripción de USD 30/mes, cambia

Si no es un curso de pago único, sino una membresía o suscripción de USD 30/mes, entonces el modelo puede funcionar mejor.

Con el plan actual:

> 3.000 suscriptores nuevos/mes  
> × 2% que se vuelve cliente pago  
> = 60 nuevos clientes pagos/mes

Si no hay churn, en 6 meses tendrían:

> 60 × 6 = 360 clientes activos  
> 360 × USD 30 = **USD 10.800 MRR**

Pero eso solo es válido si:

1. El producto es realmente recurrente.
2. El 2% es conversión a suscripción, no compra única.
3. El churn no se come la cuenta.
4. Los suscriptores no son solo tráfico frío sin intención.

Con churn mensual alto, la cosa cambia. Por ejemplo, con 25% de churn mensual, el MRR a los 6 meses quedaría aproximadamente cerca de USD 5.900, apenas por debajo de la meta. Con 20% de churn, quedaría alrededor de USD 6.600. Es decir: incluso en suscripción, hay que modelar churn.

---

## Preguntas que le haría a tu socio antes de aprobar

1. ¿Las 200.000 visitas son realmente direccionables al formulario?  
   Porque si el formulario solo aparece en una parte del sitio, la conversión efectiva puede ser mucho menor.

2. ¿El 1,5% es sobre visitas totales o sobre visitas que ven el formulario?

3. ¿El 2% de compra es mensual, por campaña o lifetime?

4. ¿El curso es pago único o suscripción?

5. ¿Hay backend, upsell, order bump o segundo producto para subir el ticket?

6. ¿Cuánto cuesta adquirir esas 200.000 visitas?  
   Porque si hay pauta, USD 1.800/mes puede ser incluso pérdida.

---

## Mi recomendación operativa

No ejecuten el plan completo todavía. Ejecuten una prueba de validación de 30 días.

Métricas mínimas a medir:

- Visitas reales a páginas con formulario.
- Impresiones del formulario.
- Tasa de captura real.
- Tasa de confirmación de email.
- Tasa de apertura y clic.
- Visitas a la página de venta.
- Conversión de venta real.
- Ticket promedio.
- Si hay suscripción: churn y retención.

Si la prueba muestra que pueden acercarse a algo como:

> 2,5% captura × 3% venta × USD 40+ ticket

entonces sí tiene sentido invertir más.

Si la prueba se queda en:

> 1,5% captura × 2% venta × USD 30

el negocio no da USD 6.000/mes. Da USD 1.800/mes.

---

## Veredicto

**No lo aprueben así.**

El plan no llega a la meta con sus propios números.  
No es que los porcentajes sean imposibles; es que la multiplicación no da.

Para aprobarlo necesitan una de estas tres cosas:

1. **Más tráfico**: alrededor de 666.000 visitas/mes manteniendo 1,5% y 2%.
2. **Mejor funnel**: por ejemplo, 2,5% de captura y 3% de venta.
3. **Mayor ticket o recurrencia**: subir a USD 100 el producto, meter upsells o convertirlo en suscripción.

Mi respuesta corta:

> **No le den a ejecutar ciegamente. Aprueben primero una versión corregida del modelo o una prueba que demuestre que la matemática puede llegar a USD 6.000/mes.**