# Claude Sonnet 5.5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 15.117s | tokens_per_second: 115.6
- input_tokens: 320 | output_tokens: 1747

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

**No lo aprobaría tal como está: los porcentajes son razonables, pero la multiplicación no llega a $6.000.**

## La cuenta

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas/mes | | 200.000 |
| Suscriptores nuevos | 200.000 × 1,5% | **3.000/mes** |
| Compradores | 3.000 × 2% | **60/mes** |
| Ingresos | 60 × $30 | **$1.800/mes** |

El plan llega a **$1.800, el 30% del objetivo**. Faltan $4.200/mes, un factor de 3,3x.

## Otros problemas

- **"Recurrentes" no aplica.** Un curso de $30 es un pago único. Esos $1.800 solo se repiten mientras entren 200.000 visitas nuevas cada mes y se sigan captando suscriptores. Si el tráfico cae, el ingreso cae.
- **Visitas no son personas.** Si las 200.000 son sesiones y no usuarios únicos, los visitantes que vuelven no se suscriben dos veces. La base real de conversión puede ser bastante menor.
- **Mes 1 no será mes 6.** La lista empieza en cero, la secuencia de emails tarda en madurar y habrá que iterar el formulario. El ingreso arrancará por debajo de $1.800.
- **El 2% depende del plazo.** ¿Es el 2% dentro de los primeros 30 días del suscriptor, o acumulado a largo plazo? Hay que aclararlo.

## Qué haría falta para llegar a $6.000

Se necesitan **200 ventas/mes** a $30. Algunas combinaciones:

| Palanca | Qué habría que lograr | ¿Realista? |
|---|---|---|
| Solo subir la captura | 5% de visitas a suscriptor (10.000/mes) | Muy difícil |
| Solo subir la compra | 6,7% de suscriptores compra | Difícil |
| Subir el precio | Curso de **$100** con las mismas tasas (60 × $100) | Plausible si el producto lo justifica |
| Mezcla | Captura 2,5% + compra 3% + precio $50 → 5.000 × 3% × $50 = $7.500 | Más alcanzable, pero cada número exige trabajo |
| Añadir ingresos | Upsell, segundo producto o membresía sobre la lista | Es lo que da recurrencia real |

## Mi recomendación

No darle luz verde a este plan, pero tampoco descartarlo. Lo rehaced con estos pasos:

1. **Verificar el dato base:** usuarios únicos reales por mes y su origen (orgánico, redes, etc.).
2. **Rehacer el modelo** con una palanca explícita para cubrir la brecha de 3,3x (precio, oferta de mayor valor o producto recurrente).
3. **Hacer una prueba de 2-4 semanas** con el formulario y una secuencia de emails para medir las tasas reales antes de comprometer seis meses.
4. **Fijar un hito intermedio**, por ejemplo $1.500-2.000 en el mes 2, como señal de que el modelo funciona.

Si quieres, armamos juntos la versión corregida con escenarios pesimista, base y optimista.