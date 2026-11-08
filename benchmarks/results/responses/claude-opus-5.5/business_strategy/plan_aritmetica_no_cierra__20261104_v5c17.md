# Claude Opus 5.5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.24 | quality: 10.0
- latency_total: 13.614s | tokens_per_second: 92.3
- input_tokens: 320 | output_tokens: 1256

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

# No lo aprobaría así: los números del plan llegan a $1.800/mes, no a $6.000

Los porcentajes pueden ser sanos, pero al multiplicarlos el plan no llega al objetivo.

## La cuenta

| Paso | Cálculo | Resultado |
|---|---|---|
| Visitas/mes | — | 200.000 |
| Suscriptores (1,5%) | 200.000 × 0,015 | **3.000** |
| Compradores (2%) | 3.000 × 0,02 | **60** |
| Ingresos | 60 × $30 | **$1.800/mes** |

**Llegan al 30% del objetivo. Faltan $4.200/mes.**

## Qué haría falta para llegar a $6.000

Se necesitan **200 ventas/mes** a $30. Con el resto del plan igual, cada palanca por separado tendría que moverse así:

| Palanca | Plan actual | Necesario | Multiplicador |
|---|---|---|---|
| Conversión a suscriptor | 1,5% | 5% | ×3,3 |
| Conversión a compra | 2% | 6,7% | ×3,3 |
| Precio del curso | $30 | $100 | ×3,3 |
| Tráfico | 200.000 | 667.000 | ×3,3 |

Ninguno de esos saltos es "conservador". La salida más realista es **combinar varias palancas moderadas**. Por ejemplo:
- Opt-in al 2,5% → 5.000 suscriptores
- Compra al 3% → 150 ventas
- Precio de $40 (o un upsell que eleve el ticket promedio) → **$6.000** ✅

## Otro detalle: "recurrentes"

Un curso de $30 es un pago único. Los $6.000 solo serían recurrentes si **cada mes entran suscriptores nuevos** y compran al mismo ritmo. Los que ya compraron no vuelven a comprar el mismo curso. Hay que modelarlo como flujo de nuevos suscriptores, no como una lista que paga todos los meses.

Si la lista acumulada se sigue trabajando, puede haber ventas extra de suscriptores antiguos. Pero es mejor no contar con eso en el plan base.

## Mi recomendación

1. **No ejecutar el plan tal cual con la meta de $6.000.** Con estas cifras, la meta honesta es ~$1.800/mes.
2. **Rediseñarlo con 2 o 3 palancas combinadas**: precio o upsell, mejor lead magnet para el opt-in, y secuencia de emails para la conversión a compra.
3. **Validar rápido**: poné el formulario 2 o 4 semanas y medí las tasas reales antes de comprometerte con la proyección a 6 meses.

¿Querés que armemos juntos la versión corregida con escenarios pesimista, base y optimista?