# Qwen 3.6 Plus — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 49.89s | tokens_per_second: 57.2
- input_tokens: 218 | output_tokens: 2853

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

No lo apruebes. El plan **muere en la multiplicación** y, tal como está escrito, no llega ni al 30% de tu meta.

### 🔢 Verificación numérica (paso a paso)
| Variable | Cálculo | Resultado |
|---|---|---|
| Tráfico mensual | 200.000 visitas | 200.000 |
| Conversión a suscriptor | × 1,5% | 3.000 leads/mes |
| Conversión a compra | × 2% | 60 ventas/mes |
| Ingreso por venta | × $30 | **$1.800/mes** |

**Meta:** $6.000/mes  
**Gap:** Faltan **$4.200/mes** (solo cubren el 30% del objetivo).

---

### 🚩 Errores estructurales que invalidan la aprobación
1. **La matemática no cierra.** No es un tema de "optimizar después", es un desfase de 3.3x desde el día 1.
2. **"$6.000 recurrentes" es incorrecto.** Un curso de $30 es pago único. Si no hay suscripción, no hay MRR. Si sí hay suscripción, falta modelar *churn*, retención y LTV. No puedes asumir que cada venta se suma linealmente al mes siguiente.
3. **El horizonte de 6 meses no arregla la ecuación.** Si acumulas suscriptores, el MRR crecería, pero solo si el modelo es realmente recurrente y mantienes retención. Con 2% de conversión y $30, necesitarías ~200 compradores activos simultáneos para sostener $6k/mes. Eso requiere infraestructura de retención, no solo captura.

---

### 🔧 Qué se necesita para llegar a $6k/mes (palancas reales)
Para cerrar el gap de $4.200, tu socio debe ajustar **al menos una** de estas variables (o combinar varias):

| Palanca | Valor actual | Valor necesario para $6k | Viabilidad |
|---|---|---|---|
| Precio del curso | $30 | **$99** (manteniendo 2% CVR) | Media/Alta si hay valor percibido |
| Conversión a compra | 2% | **~6.7%** (manteniendo $30) | Baja (requiere funnels agresivos o warm traffic) |
| Ticket promedio | $30 | **$50+** (con upsell/downsell + 4% CVR) | Alta si hay oferta complementaria |
| Modelo recurrente | One-time | Suscripción $30/mes + 75% retención | Requiere producto continuo + onboarding |

---

### ✅ Recomendación de aprobación
**❌ NO aprobar tal cual.** Devuélvelo con estos requisitos obligatorios antes de ejecutar:
1. Corregir la proyección a **$1.800/mes** o presentar un modelo ajustado que cierre matemáticamente los $6k.
2. Definir explícitamente si el modelo es **one-time o recurrente**. Si es recurrente, incluir tasa de retención/churn mensual y proyección de MRR acumulado.
3. Entregar un escenario **Base / Optimista / Conservador** con palancas cuantificadas (tráfico, CVR lead, CVR venta, AOV, retención).
4. Incluir **CAC y margen operativo**. $6k de revenue ≠ $6k de profit. Si el costo de adquisición o plataforma supera el 40%, el plan es insostenible aunque cierre en revenue.

Si tu socio quiere, puedo armarte una **tabla de simulación interactiva** con las 4 palancas para que ajusten precios, conversiones y retención hasta que la multiplicación dé exactamente $6k. ¿Lo revisamos antes de firmar?