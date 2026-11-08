# Claude Sonnet 5.5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 14.847s | tokens_per_second: 119.6
- input_tokens: 320 | output_tokens: 1776

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

**No lo aprobaría tal como está: los números no llegan.**

## La cuenta

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas/mes | | 200.000 |
| Suscriptores nuevos (1,5%) | 200.000 × 0,015 | 3.000/mes |
| Compradores (2%) | 3.000 × 0,02 | 60/mes |
| Ingresos | 60 × $30 | **$1.800/mes** |

Con sus propios supuestos "conservadores" llegan a **$1.800, no a $6.000**. Les falta un factor de 3,3x.

## Otros problemas

- **"Recurrentes" no aplica.** Un curso de $30 es un pago único. Esos $1.800 dependen de que entren 3.000 suscriptores nuevos cada mes, así que no hay ingreso que se acumule.
- **La lista acumulada no lo arregla.** Tras 6 meses tendrían unos 18.000 suscriptores, pero el 2% ya está contado sobre cada cohorte. No se suma otra vez, salvo que tengan más productos para venderle a la lista.
- **Visitas no son personas.** Si las 200.000 visitas incluyen usuarios que repiten, la base real de visitantes únicos es menor y los 3.000 suscriptores bajan.
- **Faltan descuentos.** Comisiones de pasarela (~3–6%), reembolsos e impuestos reducen aún más los $1.800.
- **Los plazos son optimistas.** Montar el formulario, la secuencia de emails y la oferta toma tiempo, y los suscriptores no compran el día uno.

## Qué haría falta para llegar a $6.000

Se necesitan 200 ventas de $30 al mes, es decir, una conversión de visita a venta del 0,1%. El plan actual da 0,03%. Algunas formas de cerrar la brecha:

1. **Subir el ticket:** a $100, las mismas 60 ventas dan $6.000. Se logra con un curso premium, un bundle o una comunidad.
2. **Agregar un producto back-end o upsell:** por ejemplo, 60 compradores × $30 más una oferta de $150 con 20% de aceptación.
3. **Mejorar la captación:** un lead magnet bien segmentado o un pop-up de intención de salida puede llevar el 1,5% a 3–4%. Es posible, pero no es lo conservador.
4. **Subir el tráfico:** necesitarían unas 667.000 visitas/mes con las mismas conversiones, y eso no se consigue en 6 meses sin inversión.
5. **Combinar:** por ejemplo, 3% de captación, 3% de compra y un ticket de $60 da 90 ventas × $60 = $5.400, ya cerca.

## Mi recomendación

Devuélvanle el plan a su socio con tres preguntas:
- ¿Las 200.000 son visitas o usuarios únicos?
- ¿Cómo cierran la brecha de 3,3x: precio, más productos o mejor conversión?
- ¿Cuál es el ingreso realmente recurrente (membresía, suscripción) y no solo ventas únicas?

Antes de gastar tiempo en ejecutar, hagan una prueba de 3–4 semanas con el formulario y la oferta para medir sus conversiones reales. Con esos datos reescriben el plan sobre números propios, no sobre benchmarks del sector.