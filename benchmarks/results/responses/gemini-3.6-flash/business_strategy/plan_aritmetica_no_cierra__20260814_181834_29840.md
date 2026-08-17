# Gemini 3.6 Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 10.406s | tokens_per_second: 196.4
- input_tokens: 197 | output_tokens: 2044

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

**RECHAZADO.** Ni se te ocurra aprobar esto hoy. 

Tu plan no muere en la ejecución; **murió en la calculadora**. 

Como analista de crecimiento, mi trabajo es evitar que gastes 6 meses de tu vida persiguiendo un fantasma. Vamos a hacer la multiplicación básica que tu socio no hizo:

### 1. La matemática real de tu embudo

* **Tráfico mensual:** 200.000 visitas.
* **Captura (1,5%):** 3.000 nuevos suscriptores al mes.
* **Venta (2%):** 60 compradores al mes.
* **Precio del producto:** $30 USD.
* **Facturación mensual:** 60 × $30 = **$1.800 USD/mes.**

**Te faltan $4.200 USD para llegar al objetivo.** Tu socio te acaba de presentar un plan que solo cubre el **30% de la meta** y te dijo que llegaban "cómodos".

---

### 2. Los errores conceptuales del plan

Además de la matemática rota, el plan tiene dos fallas graves de modelo de negocio:

1. **La ilusión de la "recurrencia":** Dijiste "$6.000/mes recurrentes". Un curso de $30 es un pago único. Si el mes 