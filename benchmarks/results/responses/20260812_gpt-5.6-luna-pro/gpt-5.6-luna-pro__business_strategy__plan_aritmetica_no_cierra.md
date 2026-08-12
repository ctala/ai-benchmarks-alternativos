# GPT-5.6 Luna Pro — business_strategy/plan_aritmetica_no_cierra

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 13.944s | tokens_per_second: 30.1
- input_tokens: 180 | output_tokens: 420

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

No lo aprobaría tal como está: los números no llegan al objetivo.

### Cálculo real

- Visitas: **200.000/mes**
- Captura al 1,5%: **3.000 suscriptores**
- Compra al 2%: **60 compradores**
- Ingreso: **60 × $30 = $1.800/mes**

Hay una brecha de **$4.200/mes**. El plan alcanza solo el **30% del objetivo**.

Además, hay dos problemas conceptuales:

1. **El curso de $30 no genera ingresos recurrentes** salvo que sea una suscripción mensual o haya recompra.
2. Si los 200.000 son visitas mensuales, hay que aclarar si los porcentajes se aplican a visitantes únicos, sesiones y nuevos suscriptores. Tampoco se puede asumir que la lista acumulada produce $6.000 mensuales automáticamente.

### Qué tendría que cambiar

Para alcanzar $6.000/mes con un curso de $30 necesitan:

- **200 ventas mensuales**, no 60.
- Con una conversión de suscriptor a comprador del 2%, necesitarían **10.000 suscriptores nuevos o activos**.
- Con una captura del 1,5%, eso requeriría aproximadamente **666.667 visitas mensuales**.

Alternativamente:

- Manteniendo 3.000 suscriptores, la conversión a compra debería ser de **6,67%**.
- Manteniendo 60 ventas, el precio tendría que ser de **$100**.
- O combinar precio mayor, upsells, productos adicionales y una oferta recurrente.

### Veredicto

**No le damos todavía.** Primero deben rehacer el modelo con una fórmula explícita:

> tráfico × captura × compra × precio = ingresos

Y definir si el objetivo es **facturación mensual**, **ingreso recurrente mensual** o **ingreso acumulado en seis meses**. Con las hipótesis actuales, la proyección correcta es **$1.800/mes**, no $6.000.