# Claude Fable 5.2 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 8.09 | quality: 10.0
- latency_total: 16.754s | tokens_per_second: 80.7
- input_tokens: 320 | output_tokens: 1352

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

**No lo aprobaría así: con sus propios números, el plan da $1.800/mes, no $6.000.**

## La multiplicación

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas | | 200.000/mes |
| Suscriptores | 200.000 × 1,5% | 3.000/mes |
| Compradores | 3.000 × 2% | 60/mes |
| Ingresos | 60 × $30 | **$1.800/mes** |

Los porcentajes pueden ser sanos, pero el plan llega al 30% del objetivo. Faltan $4.200/mes, es decir, hay que multiplicar el resultado por 3,3.

## Otros dos problemas

1. **No es ingreso recurrente.** Un curso de $30 se paga una sola vez. Los $1.800 solo se repiten mientras entren 3.000 suscriptores nuevos cada mes. La lista acumulada no vuelve a comprar el mismo curso.
2. **Visitas no son visitantes únicos.** Si parte de las 200.000 visitas son personas que regresan, la base real para captar suscriptores es menor y el resultado baja de $1.800.

## Qué haría falta para llegar a $6.000

Se necesitan 200 ventas de $30 al mes. Moviendo una sola palanca:

- **Conversión a suscriptor:** del 1,5% al 5%.
- **Conversión a compra:** del 2% al 6,7%.
- **Precio:** de $30 a $100, manteniendo las mismas conversiones, lo cual es dudoso.
- **Tráfico:** de 200.000 a unas 667.000 visitas.

Ninguna es realista por sí sola. Lo más viable es combinar: por ejemplo, 2,5% de suscripción × 2,5% de compra × $48 de ticket promedio (curso más un upsell) da $6.000.

## Recomendación

Antes de ejecutar, tu socio debería rehacer el plan con una de estas dos salidas:

- **Bajar la meta** a unos $1.800/mes con el plan actual y validar primero que los porcentajes se cumplen.
- **Rediseñar la oferta** para subir el ingreso por suscriptor de $0,60 a $2: un ticket más alto, un upsell o un producto de suscripción, que además sí sería recurrente.

Lanzar el formulario y medir la conversión real sí vale la pena desde ya, porque hoy los dos porcentajes son supuestos.