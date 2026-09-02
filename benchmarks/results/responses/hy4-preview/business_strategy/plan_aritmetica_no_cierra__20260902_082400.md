# Tencent Hy4 preview — business_strategy/plan_aritmetica_no_cierra

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 64.278s | tokens_per_second: 59.5
- input_tokens: 231 | output_tokens: 3827

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

**No lo aprobamos. Tu socio acaba de estrellar el plan contra la multiplicación.**

Vamos a hacer los números reales con los datos exactos que me diste:

1. **Tráfico a Suscriptor:** 200.000 visitas × 1,5% de conversión = **3.000 suscriptores nuevos al mes.**
2. **Suscriptor a Cliente:** 3.000 suscriptores × 2% de conversión = **60 ventas al mes.**
3. **Facturación:** 60 ventas × $30 USD = **$1.800 USD al mes.**

El objetivo son **$6.000 USD/mes**. Con este plan, llegás a **$1.800 USD**. A tu socio le está faltando el 70% del objetivo ($4.200 USD todos los meses). 

Además del error matemático, hay dos focos rojos graves en el modelo de negocio que tenés que señalarle:

1. **El mito de lo "recurrente":** Un curso de $30 suele ser un pago único. Si vendés 60 cursos, facturás $1.800 este mes, pero el mes que viene arrancás de cero y tenés que conseguir otras 60 ventas para repetirlo. Eso no es un ingreso recurrente (MRR) a menos que sea una suscripción mensual. 
2. **Si fuera una suscripción mensual:** Asumiendo que los $30 se cobran todos los meses y que **no se te da de baja nadie nunca** (0% de churn, algo directamente imposible en la vida real), recién estarías alcanzando los $6.000 mensuales en el **mes 4** ($1.800 del mes 1 + $1.800 del mes 2 + $1.800 del mes 3 + $1.800 del mes 4 = $7.200). No llegás "cómodo" a los 6 meses.

**¿Qué necesitarían para llegar a los $6.000 USD en el mes 1 con este tráfico?**
Si sus conversiones (1,5% y 2%) son reales y no las pueden mover, les quedan tres caminos (o una combinación de ellos):
* **Subir el precio:** Cobrar el curso a **$100 USD** (60 ventas × $100 = $6.000).
* **Meter un Upsell (High-Ticket):** Mantener el curso de $30 como producto de entrada, pero ofrecerles una mentoría o servicio de **$500 USD** al que entre el 15% de esos alumnos (9 ventas × $500 = $4.500 + los $1.800 iniciales = $6.300).
* **Aumentar el tráfico:** Necesitarían llevar el sitio a **666.000 visitas al mes** para generar 200 ventas de $30.

**Veredicto:** Rechazado. Decile a tu socio que guarde la calculadora, ajuste el embudo y vuelva cuando los números den.