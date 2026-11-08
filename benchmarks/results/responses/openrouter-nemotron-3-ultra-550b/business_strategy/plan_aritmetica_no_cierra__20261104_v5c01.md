# Nemotron 3 Ultra 550B — business_strategy/plan_aritmetica_no_cierra

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 46.27s | tokens_per_second: 17.2
- input_tokens: 219 | output_tokens: 798

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

**NO. No lo apruebes. El plan muere en la multiplicación.**

Hagamos la cuenta del "pañuelo" (la que tu socio debería haber hecho antes de mostrartela):

### El Embudo Real

| Paso | Métrica | Cálculo | Resultado |
| :--- | :--- | :--- | :--- |
| **1. Tráfico** | Visitas/mes | — | **200.000** |
| **2. Captura** | Conversión 1,5% | 200.000 × 0,015 | **3.000 suscriptores nuevos/mes** |
| **3. Venta** | Conversión 2% | 3.000 × 0,02 | **60 compradores/mes** |
| **4. Ingreso** | Ticket $30 | 60 × $30 | **$1.800 / mes** |

---

### La Brecha
*   **Objetivo:** $6.000 / mes
*   **Realidad del plan:** $1.800 / mes
*   **Déficit:** **$4.200 / mes (70% por debajo del target)**

---

### ¿Qué tiene que pasar para que *sí* dé $6k/mes con estos inputs?
Necesitas **3,33x** más resultado. Solo hay tres palancas (o combinaciones):

1.  **Subir precio:** Curso a **$100** (3,3x el precio actual).
2.  **Subir conversión a venta:** Del 2% al **6,6%** (muy agresivo en cold traffic).
3.  **Subir captura:** Del 1,5% al **5%** (top tier, requiere lead magnet brutal + CRO).
4.  **Más tráfico:** **660.000 visitas/mes** (3,3x el actual).
5.  **Recurrencia real (MRR):** Si el $30 es **suscripción mensual** (no pago único) y retienes bien:
    *   Mes 1: $1.800 MRR
    *   Mes 6: ~$10.800 MRR (acumulando 60 nuevos/mes sin churn).
    *   *Pero el plan dice "curso de $30", implica pago único. Si es suscripción, acláralo y modela churn.*

---

### Veredicto de Analista
**Plan rechazado.** No "llega cómodo"; llega al 30% de la meta.

**Devuélvelo con esta pregunta:**
> *"El embudo da $1.800/mes hoy. Para cerrar la brecha de $4.200, ¿qué palanca movemos primero: subimos ticket a $97, metemos upsell de $200, o cambiamos a modelo suscripción $30/mes con <3% churn? Dame el modelo corregido."*

Si no tiene respuesta cuantificada para mañana, no ejecutes.