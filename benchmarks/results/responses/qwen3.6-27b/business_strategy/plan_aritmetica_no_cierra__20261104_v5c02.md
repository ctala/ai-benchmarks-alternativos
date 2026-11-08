# Qwen 3.6 27B base (OpenRouter FP8) — business_strategy/plan_aritmetica_no_cierra

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 8.6 | quality: 10.0
- latency_total: 34.597s | tokens_per_second: 58.2
- input_tokens: 218 | output_tokens: 2015

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

**No lo aprobamos.** El plan muere exactamente en la multiplicación.

### 🔍 Desglose matemático real
| Paso | Cálculo | Resultado |
|------|---------|-----------|
| Visitas/mes | 200.000 | 200.000 |
| Conversión a suscriptor (1.5%) | 200.000 × 0.015 | **3.000 nuevos emails/mes** |
| Conversión a compra (2%) | 3.000 × 0.02 | **60 compradores/mes** |
| Ingreso por venta ($30) | 60 × $30 | **$1.800 USD/mes** |

**Objetivo:** $6.000 USD/mes  
**Brecha:** **$4.200 USD/mes (70% por debajo)**

### 🚩 Señales de alerta adicionales
1. **"Recurrentes" vs. producto de $30:** Un curso de $30 suele ser pago único. Si no es suscripción, no es ingreso recurrente. Si lo es, falta modelar churn (tasa de cancelación), que en $30/mes suele ser del 5-10% mensual.
2. **Los porcentajes no son el problema:** 1.5% → 2% son tasas razonables, pero la ecuación no escala al objetivo. La mayoría de los planes fracasan aquí: confían en que "los números se arreglan solos" sin ajustar la variable que falta.
3. **No hay ramp-up ni compounding:** En mes 1 tendrás ~$1.800. En mes 6, si no hay crecimiento de tráfico, optimización de funnel o upsells, seguirás en ~$1.800. La lista crece, pero sin un modelo de monetización escalonado o aumento de tráfico, el techo es bajo.
4. **Costos ocultos:** No se mencionan herramientas, ads, copy, diseño, soporte o impuestos. $1.800 de revenue ≠ $1.800 de profit.

### ✅ Cómo sí llegar a $6.000/mes (elige una o combina)
| Variable | Qué cambiar | Nuevo resultado mensual |
|----------|-------------|--------------------------|
| **Precio** | Subir a $90 (o bundle de 3 cursos) | 60 × $90 = **$5.400** |
| **Tráfico** | Escalar a ~670.000 visitas/mes | 670k × 1.5% × 2% × $30 = **$6.030** |
| **Conversión** | Mejorar funnel a 3% → 4% | 200k × 3% × 4% × $30 = **$7.200** |
| **Modelo** | Suscripción real + onboarding + upsell de $20/mes | 60 × $30 + 30 × $20 = **$2.400** (necesita más volumen o retención >85%) |

### 📌 Decisión
**No ejecutes.** El plan tal cual no llega al objetivo ni en mes 6. Antes de aprobar, pide a tu socio:
1. Confirmar si el $30 es pago único o suscripción.
2. Definir qué variable se va a escalar (tráfico, precio, conversión o retención).
3. Incluir costos operativos y un plan de optimización mensual (A/B testing, secuencias de email, upsells).

Si ajustas una variable clave y remodélas la ecuación, lo revisamos. Hasta entonces, **el funnel no sostiene el objetivo**.