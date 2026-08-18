# Gemini 3.7 Flash — business_strategy/plan_aritmetica_no_cierra

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 11.103s | tokens_per_second: 125.4
- input_tokens: 197 | output_tokens: 1392

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

**No. No lo aprueben.** El plan muere en la multiplicación.

Hagamos los números paso a paso:

### La matemática real de tu plan:
1. **Visitas:** 200.000 / mes.
2. **Nuevos suscriptores (1,5%):** 3.000 leads / mes.
3. **Compradores del curso (2%):** 60 compradores / mes.
4. **Ingresos brutos:** 60 compradores × $30 USD = **$1.800 USD / mes.**

Están proyectando **$1.800 USD/mes**, muy lejos de la meta de **$6.000 USD/mes** (apenas el 30% del objetivo).

---

### Dos errores críticos en el planteamiento:

1. **La brecha matemática:** Les faltan **$4.200 USD al mes** con las tasas estimadas.
2. **La ilusión de la recurrencia:** Un curso de $30 suele ser un pago único, no una suscripción mensual. Eso significa que esos $1.800 no se acumulan: cada mes arrancan de cero y dependen de meter 60 ventas nuevas solo para mantener ese piso.

---

### ¿Qué números necesitan para llegar de verdad a los $6.000/mes?

Para facturar $6.000 con 200.000 visitas, necesitan mover al menos una de estas palancas:

* **Opción A (Subir el Ticket Promedio / AOV):**
  Manteniendo 60 compradores al mes, el ticket promedio debe ser de **$100 USD** (un curso más avanzado, un bundle o agregar un upsell/order bump en el checkout).
* **Opción B (Aumentar la conversión a venta):**
  Si el curso vale $30, necesitan **200 ventas al mes**.
  * Con 3.000 leads, tu lista debe convertir al **6,67%** (muy agresivo para tráfico frío).
* **Opción C (Embudo de dos pasos con membresía):**
  Vender el curso inicial de $30 (front-end) y ofrecer dentro una membresía recurrente de $20-$30/mes para que el ingreso sí sea acumulativo y no empiece en cero cada mes.

**Veredicto:** Devuélvele el plan a tu socio. Para aprobarlo, el modelo debe cerrar con un ticket promedio de $100 o con un embudo que genere 200 ventas/mes.