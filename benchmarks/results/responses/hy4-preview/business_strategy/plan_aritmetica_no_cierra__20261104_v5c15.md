# Tencent Hy4 preview — business_strategy/plan_aritmetica_no_cierra

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 35.812s | tokens_per_second: 62.9
- input_tokens: 231 | output_tokens: 2253

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

**No, no lo apruebes.** 

Este es el clásico ejemplo de un plan que muere en la multiplicación. Los porcentajes suenan "conservadores y realistas", pero la matemática está rota. Los números no llegan ni cerca al objetivo.

Hagamos la cuenta paso a paso con los datos de tu socio:

1. **De Tráfico a Suscriptores:**
   200.000 visitas × 1,5% (0,015) = **3.000 suscriptores nuevos al mes.**

2. **De Suscriptores a Ventas:**
   3.000 suscriptores × 2% (0,02) = **60 ventas al mes.**

3. **De Ventas a Facturación:**
   60 ventas × $30 USD = **$1.800 USD al mes.**

**La realidad:** El plan genera **$1.800 USD/mes**. Estás facturando el 30% de tu objetivo. Te faltan $4.200 USD para llegar a los $6.000. 

Para llegar a los $6.000 USD necesitas hacer ajustes drásticos. Tienes tres caminos (o una combinación de ellos):

**Camino A: Subir el precio (El más rápido)**
Si mantienes todo igual (60 ventas/mes) y quieres facturar $6.000, necesitas que tu curso valga **$100 USD**. (60 × 100 = 6.000). ¿El mercado está dispuesto a pagar eso por lo que ofrecen? Si la respuesta es sí, este es el camino.

**Camino B: Mejorar las conversiones (El más rentable)**
Para facturar $6.000 con un curso de $30, necesitas **200 ventas** al mes.
*   Si mantienes el 1,5% de captura (3.000 suscriptores), necesitas convertir a ventas al **6,6%** (3.000 × 6,6% = 200). Pasar del 2% al 6,6% de conversión en frío es muy agresivo.
*   Si mantienes el 2% de conversión a venta, necesitas **10.000 suscriptores** nuevos al mes. Con 200.000 visitas, eso significa que tu formulario tiene que convertir al **5%** (200.000 × 5% = 10.000). Un 5% de captura es un excelente número, pero requiere un lead magnet (imán de prospectos) muy potente, no solo "un formulario".

**Camino C: Aumentar el tráfico (El más caro y lento)**
Si tus conversiones (1,5% y 2%) son inamovibles porque son el estándar de la industria, necesitas generar **666.666 visitas al mes** para llegar a los $6.000 USD. 

**Veredicto:**
La estructura del embudo está bien (Tráfico -> Captura -> Venta), pero la matemática no cierra. Pídele a tu socio que rehaga los números y defina qué variable van a atacar: ¿suben el precio del curso, crean un producto de mayor valor o diseñan una estrategia agresiva de conversión? 

Hasta que esa multiplicación no dé $6.000, no gastes un peso en ejecutarlo.