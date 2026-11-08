# Tencent Hy3 — business_strategy/plan_aritmetica_no_cierra

- model_id: `tencent/hy3`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 77.843s | tokens_per_second: 59.9
- input_tokens: 238 | output_tokens: 4660

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

Como analista de crecimiento, mi trabajo es ser el tipo que apaga la emoción con matemáticas frías. Y tenías razón en tu premisa inicial: **la mayoría de los planes mueren en la multiplicación.**

Vamos a hacer la prueba de fuego a los números de tu socio, paso a paso, sin inflar nada:

*   **1. Tráfico:** 200.000 visitas/mes
*   **2. Captura (1,5%):** 200.000 × 0,015 = **3.000 suscriptores/mes**
*   **3. Ventas (2%):** 3.000 × 0,02 = **60 compradores/mes**
*   **4. Facturación:** 60 × $30 = **$1.800/mes**

### Veredicto: ❌ Plan Rechazado (por ahora)

Tu socio asegura que con eso llegan "cómodos" a los $6.000/mes. La realidad desnuda es que esos números generan **$1.800/mes**. Están un **333% por debajo** del objetivo. El plan murió exactamente donde dijiste: en la multiplicación.

### ¿Cuál es el error de concepción?
Hay una confusión entre *nuevos ingresos mensuales* y *ingreso recurrente acumulado* (MRR). 
*   Si el curso de $30 es de **pago único**, vas a facturar $1.800 sueltos por mes. Nunca llegarás a $6.000/mes recurrentes.
*   Si el curso es una **suscripción mensual de $30** y nadie se da de baja (0% de churn), recién en el **mes 4** acumularías $7.200/mes (60 clientes nuevos × 4 meses × $30). Pero el plan lo vende como si la conversión mensual ya fuera el MRR final, lo cual es un salto lógico inválido.

### Para que este plan funcione con las mismas métricas "sanas", necesitamos una de estas tres cosas:
1.  **Más tráfico:** Subir de 200.000 a **~666.000 visitas/mes** (3,3x más volumen).
2.  **Mejor monetización:** Subir el precio de $30 a **$100** por curso/suscripción.
3.  **Mejor conversión a venta:** Que compre el **6,6%** de la lista en vez del 2% (poco realista para un funnel orgánico/frío).

### Conclusión
Los porcentajes (1,5% y 2%) son de hecho conservadores y sanos, pero **no escalan al objetivo de $6.000**. No le des el "sí" todavía. Sentate con tu socio, mostrale esta multiplicación y decidan si ajustan el precio del producto, el volumen de tráfico o la ambición del objetivo a 6 meses.