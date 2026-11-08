# Gemini 3.1 Pro — business_strategy/plan_aritmetica_no_cierra

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 8.26 | quality: 10.0
- latency_total: 20.11s | tokens_per_second: 93.8
- input_tokens: 197 | output_tokens: 1887

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

**NO LO APRUEBES.** Frena todo ahora mismo. 

Tu socio tiene razón en algo: los porcentajes (1,5% y 2%) son realistas. El problema es que **el plan acaba de morir en la multiplicación.** 

Vamos a hacer los números juntos:

1. **Tráfico:** 200.000 visitas / mes.
2. **Suscriptores (1,5%):** 3.000 leads nuevos / mes.
3. **Compradores (2% de los leads):** 60 ventas / mes.
4. **Facturación:** 60 ventas x $30 = **$1.800 USD / mes.**

Están facturando $1.800, no $6.000. Les faltan $4.200 dólares para llegar a la meta. 

Pero además, hay un **segundo error fatal** en el plan: 

Mencionas llegar a $6.000/mes **"recurrentes"**, pero están vendiendo un *curso* de $30. Un curso suele ser un pago único. Si el mes que viene quieres volver a facturar, dependes de que entren otros 3.000 leads nuevos. Para que sea recurrente, tendría que ser una membresía (suscripción mensual), y ahí tendríamos que calcular la tasa de cancelación (*churn rate*).

### ¿Qué necesitan cambiar para que el plan funcione?
Como analista de crecimiento, te digo que tienen 3 palancas. Elijan una para arreglar el plan antes de ejecutar:

*   **Palanca 1: Subir el ticket (La más fácil).** Si mantienen sus tasas de conversión actuales (60 ventas al mes), el producto no puede valer $30. **Debe costar $100 USD** (60 x $100 = $6.000).
*   **Palanca 2: Mejorar la captura (Realista).** Si quieren mantener el precio en $30, necesitan 200 ventas al mes. Para lograr 200 ventas con un 2% de conversión, necesitan 10.000 leads al mes. Eso significa que el formulario de captura debe convertir al **5%** (no al 1,5%).
*   **Palanca 3: Subir el tráfico (La más cara/lenta).** Si mantienen el precio de $30 y las conversiones de 1.5% y 2%, necesitan meter **666.000 visitas al mes** en el sitio web para que la matemática dé.

**Mi recomendación:** Devuélvele el plan a tu socio. Dile que las tasas de conversión son buenas para empezar, pero que a $30 el ticket es demasiado bajo para el volumen de tráfico que tienen. Tienen que rediseñar la oferta (vender algo de $100) o convertir el producto en una verdadera membresía de $30/mes y proyectar la retención a 6 meses. 

Hasta que la matemática en el papel no dé $6.000, no se escribe ni una línea de código ni se lanza nada.