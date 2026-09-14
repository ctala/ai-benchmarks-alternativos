# Gemini 3.8 Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.65 | quality: 10.0
- latency_total: 13.511s | tokens_per_second: 129.7
- input_tokens: 197 | output_tokens: 1752

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

**No lo aprueben.** El plan muere en la multiplicación básica. 

Hagamos los números paso a paso:

1. **Visitas:** 200.000 al mes
2. **Nuevos suscriptores (1,5%):** 3.000 leads/mes
3. **Compradores (2% de los leads):** 60 ventas/mes
4. **Ingresos:** 60 ventas × $30 = **$1.800 USD/mes**

El plan no llega a los $6.000; **se queda en $1.800**. Les falta un 70% para alcanzar la meta.

---

### Hay dos errores graves en el planteamiento:

1. **La matemática no cierra:** Para facturar $6.000 a $30 por venta, necesitan **200 ventas al mes**, no 60. Eso exigiría que su lista convierta al **6,67%** (muy lejos del 2% conservador que estimaron).
2. **Confusión de modelo ("recurrente"):** Un curso de $30 suele ser un pago único transaccional. Salvo que sea una membresía con cobro mensual (y aun así tendrías que restar la tasa de cancelación o *churn*), cada mes vuelven a empezar desde cero.

---

### ¿Qué tendría que cambiar para que los $6.000 sean viables?

Para llegar a $6.000 con ese mismo tráfico y esfuerzo, deben mover una (o varias) de estas palancas:

* **Subir el precio (la más fácil):** Si mantienen 60 ventas al mes, el ticket promedio debe ser de **$100 USD** (no $30).
* **Mejorar la captura:** Subir la conversión de visita a lead del 1,5% al **5%** (10.000 leads × 2% = 200 ventas = $6.000).
* **Crear un embudo con *Order Bump* / *Upsell*:** Vender el curso a $30, pero ofrecer un producto complementario o asesoría de $150 que suba el valor medio por cliente.

**Veredicto:** Devuélvele el plan a tu socio. La matemática actual genera $1.800, no $6.000.