# Claude Sonnet 5.5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 13.523s | tokens_per_second: 120.1
- input_tokens: 320 | output_tokens: 1624

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

**No lo aprobaría tal como está.** Los porcentajes pueden ser razonables, pero el plan no llega a $6.000.

## La cuenta

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas/mes | | 200.000 |
| Suscriptores nuevos | 200.000 × 1,5% | 3.000/mes |
| Compradores | 3.000 × 2% | 60/mes |
| Ingresos | 60 × $30 | **$1.800/mes** |

El plan llega a **$1.800, el 30% del objetivo**. Faltan $4.200/mes, o sea que hay que multiplicar el resultado por 3,3.

Acumular la lista tampoco lo arregla. Si en 6 meses juntan 18.000 suscriptores y el 2% compra, son 360 ventas y $10.800 en total, es decir, el mismo promedio de $1.800/mes.

## Otros problemas

- **No es recurrente.** Un curso de $30 es una venta única. Para tener $6.000 cada mes, tendrían que generar 200 ventas nuevas cada mes.
- **Visitas no es lo mismo que visitantes únicos.** Si las 200.000 incluyen gente que vuelve, la base real para el 1,5% es menor.
- **El 2% es optimista si se aplica a toda la lista.** Es una cifra plausible para un lanzamiento a una audiencia caliente, pero los suscriptores fríos suelen comprar menos.

## Qué haría falta para llegar a $6.000

Necesitan 200 ventas a $30, o su equivalente, y tienen 60. Algunas rutas:

1. **Subir el ticket:** con 60 compradores, el precio tendría que ser **$100**. Es la palanca más realista, con un curso más completo, bundles o un upsell.
2. **Mejorar la conversión:** pasar de 0,03% a 0,1% visita→venta. Por ejemplo, 3% de captura y 3,3% de compra, que son cifras exigentes ambas.
3. **Más tráfico:** unas 667.000 visitas/mes con las mismas tasas. Es difícil en 6 meses.
4. **Combinación realista:** captura del 2,5% (5.000 suscriptores), compra del 3% (150 ventas) y ticket de $40 + upsell de $40 al 20% de los compradores. Da unos $6.000, pero requiere optimizar todo el embudo.

## Mi recomendación

Rehagan el plan partiendo del objetivo hacia atrás: $6.000 → ventas necesarias → suscriptores → tráfico. Luego decidan qué palanca mover (precio, oferta, conversión) y prueben con un test pequeño de 2 o 3 semanas antes de comprometer 6 meses. Con los números actuales, el escenario honesto es **~$1.800/mes**.

¿Quieren que armemos una versión corregida con distintos escenarios (pesimista, base y optimista)?