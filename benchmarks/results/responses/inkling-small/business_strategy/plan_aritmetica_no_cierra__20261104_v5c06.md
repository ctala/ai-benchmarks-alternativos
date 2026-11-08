# Inkling Small — business_strategy/plan_aritmetica_no_cierra

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 27.533s | tokens_per_second: 227.7
- input_tokens: 205 | output_tokens: 6268

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

**No lo apruebes. El plan muere exactamente donde tú dices: en la multiplicación.**

Tu socio tiene una ilusión de tasas. Cree que porque 1,5 % y 2 % suenan “conservadores”, la multiplicación va a llegar sola. No. La mayoría de los planes no mueren por ser ambiciosos; mueren porque el fundador hace la suma mentalmente, no con papel. Aquí está el papel.

---

### 1. El cálculo real (sin magia)

| Paso | Número | Resultado |
|------|--------|-----------|
| Tráfico mensual | 200.000 visitas | — |
| Conversión a suscriptor (1,5 %) | 200.000 × 0,015 | **3.000 suscriptores nuevos/mes** |
| Conversión a comprador (2 %) | 3.000 × 0,02 | **60 compradores/mes** |
| Ticket | $30 | — |
| **Ingreso mensual real** | 60 × $30 | **$1.800/mes** |

Tu socio dice “llegamos cómodos a $6.000/mes recurrentes”. El plan entrega **$1.800**.

Eso es un **gap de 3,3×**. No está cerca; está en otro planeta.

---

### 2. ¿Cómo llegó él a $6.000 en su cabeza?

Hay dos formas en que se miente sin querer:

**Opción A: Confundió “ingreso” con “MRR acumulado” (la más probable).**
Si cada mes suma 60 clientes nuevos y **nunca** se van (0 % churn), a mes 6 tiene 360 clientes × $30 = $10.800 MRR. Eso “suena” a que supera $6.000. Pero eso requiere:
- Que tu curso sea **una suscripción**, no una compra de una vez.
- Que el 2 % sea de **nuevos suscriptores** cada mes, sin fatiga.
- Que **ningún cliente se dé de baja** (en la vida real, un 5-10 % mensual de churn es común; con 10 % mensual, a mes 6 no llegas a 360, llegas a ~280, y con 15 % te quedas en ~240).

Además, para que eso funcione, cada mes debes regenerar **3.000 nuevos suscriptores**, lo que exige **200.000 visitas constantes, de calidad, sin estacionalidad**. Eso no es “conservador”; es una máquina de tráfico que no aparece por poner un formulario.

**Opción B: Pensó que la lista es un tanque que se llena una vez.**
Si captura 3.000 y luego “vende a esa lista”, el 2 % de 3.000 es 60 ventas. Si repite la venta a la misma lista el mes siguiente, o vendes a 3.000 que ya te compraron antes, estás vendiendo a personas que no pueden comprar el mismo curso de $30 otra vez. El 2 % de conversión de email es de **audiencia nueva o activa**, no de una lista que ya compró.

---

### 3. El problema de “recurrentes” que nadie está viendo

El plan dice *“nuestro curso de $30”*. Un curso de precio bajo, de un solo pago, **no genera recurrencia**. Si es MRR, es una suscripción, no un curso de $30 de una vez.

- **Si es venta única:** Son $1.800/mes. Nunca $6.000/mes recurrentes.
- **Si es MRR:** Necesitas **200 clientes activos** para llegar a $6.000.

Para tener 200 clientes activos con 2 % de conversión de lista, necesitas **10.000 suscriptores activos/enviados por mes**.
Para tener 10.000 suscriptores con 1,5 % de captura, necesitas **666.667 visitas/mes**, no 200.000.

Así que el plan tiene una contradicción estructural: **o es un producto de una vez y no hay recurrencia, o es recurrencia y le falta tráfico (o precio) para sostenerlo.**

---

### 4. Lo que mata el plan en la ejecución (no solo en la matemática)

Aunque arregles los números, hay riesgos ocultos que el “2 % conservador” oculta:

- **Fatiga de la lista:** No puedes enviar “comprá el curso” al 2 % de tu lista cada mes sin quemar a los otros 98 %.
- **Tráfico de 200k:** ¿Es orgánico estable? ¿O cuesta dinero/tiempo? Si es orgánico, ¿cuánto tarda en caer si dejas de publicar?
- **Captura de 1,5 %:** En tráfico frío, sin oferta de valor clara, el 1,5 % puede ser 0,5 %. Eso te lleva a 1.000 suscriptores y **$600/mes**.
- **Churn:** Si es MRR, un curso de $30 tiene alta rotación. A 10 % mensual, pierdes la mitad de tu base antes de mes 6.
- **No hay presupuesto de adquisición:** El plan no dice cuánto cuesta conseguir esas 200.000 visitas.

---

### 5. Qué hacer antes de aprobar

No apruebes el plan. Haz este **check de multiplicación** con tu socio antes de gastar un dólar:

1. **Clarifica el modelo:** ¿Es MRR (suscripción) o ingreso por venta de una vez?
2. **Si es MRR:** Define cuánto churn aceptas. Si quieres $6.000 MRR a mes 6, con 10 % churn mensual necesitas ~115 nuevos clientes/mes (no 60). Eso requiere ~383.000 visitas o subir tu captura al 3,8 %.
3. **Si es venta única:** Acepta que son $1.800/mes con esta base. Para llegar a $6.000/mes necesitas **triplicar tráfico o triplicar el ticket** (o subir la conversión de captura/venta).
4. **Pilota:** No ejecutes a 200.000. Testea con 20.000 o con tu lista actual. Mide **realmente** tu tasa de captura y tu tasa de venta antes de escalar.

---

### Veredicto final

> **El plan no llega a $6.000. Llega a $1.800.**  
> Los porcentajes no son el problema; el problema es que la base de tráfico es 3,3× más pequeña de lo que requiere el objetivo.

Tu socio armó una historia de porcentajes sanos, pero no hizo la multiplicación completa. **No lo ejecutes. Corrige la base o el precio, o baja el objetivo a $1.800/mes y construye desde ahí.**

Si querés, te armo la versión corregida con los números exactos para $6.000 (ya sea con más tráfico, con un ticket de $100 o con una captura del 5 %). Pero por ahora: **no apruebes.** El dinero se quema en la multiplicación.