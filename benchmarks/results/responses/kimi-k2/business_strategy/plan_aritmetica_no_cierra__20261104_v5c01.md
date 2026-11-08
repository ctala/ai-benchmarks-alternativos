# Kimi K2 — business_strategy/plan_aritmetica_no_cierra

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 18.22s | tokens_per_second: 38.6
- input_tokens: 238 | output_tokens: 704

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

Vamos a verificar los números paso a paso.

## Verificación del plan

| Paso | Cálculo | Resultado |
|------|---------|-----------|
| **Tráfico** | 200.000 visitas | Base |
| **Suscriptores** | 200.000 × 1,5% | **3.000 suscriptores/mes** |
| **Compradores** | 3.000 × 2% | **60 compras/mes** |
| **Ingreso** | 60 × $30 | **$1.800/mes** |

## El problema

El plan alcanza **$1.800/mes**, no $6.000. Está **$4.200 corto** (70% por debajo del objetivo).

---

## ¿Dónde está el error?

No es en los porcentajes — son razonables. El problema es que **el plan no escala con el tiempo**.

| Mes | Suscriptores nuevos | Compradores | Ingreso del mes | Ingreso acumulado |
|-----|---------------------|-------------|-----------------|-------------------|
| 1 | 3.000 | 60 | $1.800 | $1.800 |
| 2 | 3.000 | 60 | $1.800 | $3.600 |
| ... | ... | ... | ... | ... |
| 6 | 3.000 | 60 | $1.800 | **$10.800 total** |

Ni siquiera sumando 6 meses llegas a $6.000 **recurrentes**. Y esto asume que nadie se da de baja.

---

## Para llegar a $6.000/mes, necesitas alguna de estas combinaciones

| Opción | Cambio necesario |
|--------|------------------|
| A | Subir conversión a suscriptor a **~5%** |
| B | Subir tasa de compra a **~6,7%** |
| C | Subir precio del curso a **~$100** |
| D | Multiplicar tráfico ×3.3 (660.000 visitas) |
| E | **Modelo recurrente**: suscripción mensual de $30 en lugar de pago único |

---

## Mi recomendación

**No apruebes todavía.** El plan tiene un error de diseño, no de ejecución. Los porcentajes son creíbles, pero la aritmética no cierra.

Pregúntale a tu socio: *"¿Cómo llegamos de $1.800 a $6.000? ¿Qué variable estamos subestimando?"*

Si el curso es realmente de **pago único de $30**, necesitas otra fuente de ingresos o un modelo de membresía. Si es una **suscripción mensual de $30**, entonces sí: al mes 6 tendrías ~18.000 suscriptores acumulados y con 2% de conversión mensual sobre la base activa, los números cambian completamente.

¿El curso es pago único o recurrente? Eso redefine todo el análisis.