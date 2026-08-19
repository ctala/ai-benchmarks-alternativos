# Kimi K2.5 — business_strategy/plan_aritmetica_no_cierra

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.23 | quality: 10.0
- latency_total: 83.23s | tokens_per_second: 24.6
- input_tokens: 237 | output_tokens: 2048

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

 **No lo apruebes.** 

El plan tiene un agujero matemático de 3.3x. Tu socio multiplicó los porcentajes pero no llegó al objetivo. Hiciste bien en pedir una segunda revisión.

Aquí está la autopsia:

## El cálculo real

| Etapa | Cálculo | Resultado |
|-------|---------|-----------|
| **Tráfico** | 200,000 visitas | 200,000 |
| **Suscriptores** | 200,000 × 1,5% | **3,000/mes** |
| **Compradores** | 3,000 × 2% | **60/mes** |
| **Ingreso** | 60 × $30 | **$1,800/mes** |

**Brecha:** Necesitas $6,000 y el plan genera $1,800. Te faltan **$4,200** (o un 233% más de lo proyectado).

## Por qué falla la lógica del "recurrente"

Tu socio probablemente pensó: *"Si acumulamos suscriptores 6 meses, al final tendremos 18,000 personas y el 2% comprará"*. 

Eso es incorrecto porque:
1. **El 2% es una tasa de conversión de la lista, no mensual.** Una vez que alguien compra un curso de $30, no lo compra de nuevo el mes siguiente (es producto one-time, no SaaS).
2. **Churn:** Los emails se dan de baja, rebotan o dejan de abrir. Tu lista neta crece más lento.
3. **Saturación:** A mes 6, tus 200,000 visitas mensuales ya capturaron a los más interesados; la tasa de conversión tiende a bajar, no a mantenerse.

## Opciones para cerrar la brecha de 3.3x

Para llegar a $6,000/mes con este modelo, necesitas **una** de estas variaciones:

| Variable | Valor actual | Valor necesario | Dificultad |
|----------|--------------|-----------------|------------|
| **Tráfico** | 200,000 | **666,000 visitas/mes** | Alta (SEO/ads) |
| **Opt-in rate** | 1,5% | **5%** | Media (CRO agresivo) |
| **Conversión a venta** | 2% | **6,7%** | Muy alta (copy/urgencia) |
| **Precio** | $30 | **$100** | Media (reestructurar oferta) |
| **Modelo** | One-time | **Suscripción $30/mes** | Alta (cambio de producto) |

## Mi recomendación

**Mándalo de vuelta a la hoja de cálculo con esta pregunta:** *"¿Qué variable del