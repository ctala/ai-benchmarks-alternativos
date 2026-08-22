# GLM 5.3 — business_strategy/plan_aritmetica_no_cierra

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.16 | quality: 10.0
- latency_total: 117.231s | tokens_per_second: 73.5
- input_tokens: 212 | output_tokens: 8622

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

**No. Con sus propios números, el plan da $1.800/mes, no $6.000.**

La multiplicación:

- 200.000 visitas × 1,5% = **3.000 suscriptores/mes**
- 3.000 × 2% = **60 compradores/mes**
- 60 × $30 = **$1.800/mes**

Es el 30% del objetivo. El plan queda 70% corto antes de ejecutar nada. Los porcentajes pueden ser sanos individualmente; multiplicados no llegan adonde dice el plan.

**Dónde se esconde el $6.000** (la única lectura que llega):

Si en vez de venderle al 2% de cada cohorte mensual, le vendes al 2% de la lista *acumulada* cada mes: mes 1 $1.800 → mes 4 $7.200 → mes 6 $10.800. Ahí cruzas los $6.000... pero ese modelo se apoya en tres supuestos que el plan no declara:

1. **El 2% compra cada mes sobre TODA la lista.** En 6 meses eso implica que ~11% de la lista compró. Ese es el borde optimista, no el conservador.
2. **"Recurrente" es falso.** Un curso de $30 se compra una vez. Cada mes re-ganas el ingreso desde cero sobre una lista que se agota. Es un activo decreciente, no renta fija.
3. **Cero fricción:** sin bajas, sin fatiga, sin caída de entregabilidad. Una lista real pierde ~25% al año entre desuscripciones e inactivos.

Además, el plan no descuenta costos: comisiones de pago (~4% en un ticket de $30), reembolsos (5-10% es normal en cursos) y plataforma de email ($100-250/mes con 18.000 contactos). Eso se come otro 15-20%.

**La pregunta para tu socio:** ¿los 60 compradores son el 2% de los suscriptores *nuevos* de cada mes, o el 2% de la lista *total*? Si es lo primero, hay un error aritmético y el plan da $1.800. Si es lo segundo, hay tres supuestos ocultos que hay que declarar y validar. En ambos casos, no se ejecuta tal cual.

**Cómo se cierra la brecha de verdad** (necesitas 200 compradores/mes: 3,3× lo que produce el embudo actual):

- **Subir el ticket** con order bump + upsell: $30 → $80-100 de ticket promedio.
- **Subir la captura** de 1,5% a 2,5-3% con un mejor lead magnet (top del sector, alcanzable).
- **Membresía en vez de curso puntual** — eso sí es recurrente: 60 miembros nuevos/mes × $30 con 5% de churn ≈ $9.500/mes en el mes 6 (aunque convertir 2% a una suscripción es más agresivo que a una compra única).
- **Combinación realista:** 4.000 subs/mes × 2,5% × $60 de ticket ≈ $6.000/mes por cohorte, sin depender de una lista que se agota.

**Lo que sí apruebo hoy:** arrancar el test de captura. Validar el 1,5% con tráfico real cuesta poco y en 2-3 semanas sabes si la base del embudo existe. El resto vuelve al tablero con churn, costos y el modelo de compra explícito.

El plan no muere por los porcentajes. Muere por la multiplicación — como siempre.