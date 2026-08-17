# Claude Sonnet 5 (suscripción) — business_strategy/plan_aritmetica_no_cierra

- model_id: `claude-sonnet-5`
- success: True  | final: 8.09 | quality: 10.0
- latency_total: 76.067s | tokens_per_second: 72.3
- input_tokens: 2 | output_tokens: 5499

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

Hice la multiplicación. No cierra — y no por poco.

## El cálculo tal como está planteado

| Paso | Operación | Resultado |
|---|---|---|
| Visitas → suscriptor | 200.000 × 1,5% | **3.000 suscriptores/mes** |
| Suscriptor → comprador | 3.000 × 2% | **60 compradores/mes** |
| Revenue | 60 × $30 | **$1.800/mes** |

El plan dice "$6.000/mes cómodos". El número real es **$1.800/mes**. Falta un **3,33x**. No es un margen de error, es un tercio del objetivo.

## Un problema antes que el otro: "recurrente" está mal usado

$6.000 USD/mes **recurrente** no puede salir de un curso de **pago único** a menos que definas explícitamente de dónde sale el "mes a mes":

- Si son 3.000 suscriptores **nuevos cada mes** con el mismo funnel, el revenue se estabiliza en $1.800/mes — no crece, no es "recurrente" en el sentido MRR, es "repetible si nada cambia".
- Si asumen que van a re-venderle el mismo curso a la lista acumulada mes tras mes, eso no es realista: quien ya compró no vuelve a comprar el mismo producto.
- Si la intención es nutrir la lista acumulada con nuevas ofertas (urgencia, bundles, upsell), **eso sí puede acercarse a $6K**, pero es un mecanismo que el plan no menciona — hoy dice "le vendemos nuestro curso", singular, una campaña.

Antes de aprobar nada, tu socio necesita responder: ¿de dónde sale el crecimiento mes a mes, si tráfico, conversión y precio quedan fijos? Con esos tres fijos, el techo es $1.800/mes indefinidamente.

## Qué palanca(s) cierran los 3,33x

Ninguna paIanca sola de forma "conservadora" lo logra. Combinaciones que sí, con supuestos igual de agresivos que el original (no descabellados, pero hay que nombrarlos):

**Ruta A — subir dos conversiones + precio**
- Suscriptor: 1,5% → 2,5% (mejor lead magnet, exit intent)
- Compra: 2% → 3% (secuencia de email con urgencia, no solo "el formulario")
- Precio: $30 → $40
- 200.000 × 2,5% = 5.000 → × 3% = 150 compradores × $40 = **$6.000**

**Ruta B — tráfico + compra, precio fijo**
- Tráfico: 200K → 300K (SEO/contenido en 6 meses, verificable si ya hay tracción)
- Suscriptor: se queda en 1,5% (300K × 1,5% = 4.500)
- Compra: 2% → 4,5% (agresivo para un curso frío sin nutrir — normalmente 1-3% es el rango realista de un tripwire de $30)
- 4.500 × 4,5% × $30 ≈ **$6.075** — pero el 4,5% es el supuesto más frágil de los tres

**Ruta C — la que de verdad usa el activo "lista acumulada"**
- Mantener tráfico, suscriptor y compra tal como están ($1.800/mes de "primera compra")
- Sumar una segunda oferta a la lista acumulada (upsell, curso 2, membresía) que capture otro 1-2% de la base creciente
- A los 6 meses la lista acumulada es ~18.000 personas; incluso un 1% adicional en un producto de $50-100 cierra la brecha sin tocar el funnel original

## Veredicto

No lo aprobaría tal cual — el plan, leído literal, entrega el 30% de la meta y llama "recurrente" a algo que no lo es. Antes de ejecutar, que tu socio elija explícitamente **qué palancas mueve** (no "los porcentajes son conservadores" sin más) y qué mecanismo genera el crecimiento mes a mes. Si vuelve con Ruta A o C con supuestos verificables (no solo estimados a ojo), ahí sí tiene sentido correrlo.