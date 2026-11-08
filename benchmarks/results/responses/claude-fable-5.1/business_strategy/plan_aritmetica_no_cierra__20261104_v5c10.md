# Claude Fable 5.1 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 8.04 | quality: 10.0
- latency_total: 19.523s | tokens_per_second: 70.2
- input_tokens: 320 | output_tokens: 1370

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

**No. El plan no llega.** Hagamos la multiplicación que falta en el punto 4:

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas | — | 200.000 / mes |
| Suscriptores (1,5%) | 200.000 × 0,015 | **3.000** |
| Compradores (2%) | 3.000 × 0,02 | **60** |
| Ingresos ($30) | 60 × $30 | **$1.800 / mes** |

Con los propios números del plan llegan a **$1.800**, no a $6.000. Es el **30% del objetivo**. Faltan $4.200 al mes, y eso asumiendo que los porcentajes "conservadores" se cumplan.

**Para llegar a $6.000 necesitan 200 ventas/mes, no 60.** Eso implica multiplicar por 3,3 alguna de estas palancas (o combinarlas):

- Conversión a suscriptor: del 1,5% al **5%** (muy ambicioso para un formulario genérico; posible con un lead magnet fuerte).
- Conversión a compra: del 2% al **6,7%** (poco realista en frío; más viable con secuencia de emails + oferta limitada).
- Precio: de $30 a **$100** (la palanca más fácil de mover si el curso lo vale).
- Combinación razonable: 3% suscriptores × 3,3% compra × $30 ≈ $5.900.

Dos observaciones más:

1. **"Recurrentes" es engañoso.** Un curso de $30 de pago único no es ingreso recurrente. Lo que se repite es el flujo de *nuevos* suscriptores cada mes; los que no compraron el mes 1 no van a convertir al 2% otra vez en el mes 2. Si el tráfico baja, el ingreso baja.
2. **"Conservador" sin contraste.** Que un número parezca sano no significa que cierre la cuenta. Antes de discutir si el 1,5% es realista, hay que ver si el 1,5% *sirve*. Acá no sirve.

**Recomendación:** no aprobar tal como está. Pedirle al socio que reconstruya el plan hacia atrás desde las 200 ventas/mes que se necesitan, y que diga explícitamente qué palanca va a mover para pasar de 60 a 200. Si la respuesta es "subir precio" o "agregar un producto de mayor ticket", el plan puede salvarse. Si es "los porcentajes serán mejores de lo que estimamos", es el mismo plan con esperanza encima.