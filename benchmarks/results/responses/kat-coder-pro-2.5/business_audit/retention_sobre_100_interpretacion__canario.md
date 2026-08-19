# KAT Coder Pro v2.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 8.78 | quality: 10.0
- latency_total: 10.774s | tokens_per_second: 106.5
- input_tokens: 143 | output_tokens: 1147

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa



No, no es correcto. Estás confundiendo dos métricas distintas y tu conclusión es peligrosa.

### 1. Lo que realmente dice el 114%
Ese número es **Net Revenue Retention (NRR)**, no "retención de clientes". Mide **ingresos**, no personas.

- **NRR > 100%** significa que los clientes que se quedaron (y posiblemente algunos que ampliaron) generaron más dinero que la base del periodo anterior, compensando las bajas.
- **No significa** que no se haya ido nadie. De hecho, tú mismo dices que pasaste de 40 a 36 clientes: **perdiste 4 clientes (10% de churn de clientes)**.

### 2. La trampa de ignorar el churn de clientes
Tu razonamiento ("prácticamente no se va nadie") es incorrecto. Se te fue el **10% de tu base en un solo mes**. Si esa tasa se mantiene, en 10 meses habrás perdido toda tu base inicial (aunque los ingresos se mantengan por expansiones).

El NRR alto puede **enmascarar** un problema de retención de clientes si:
- Los clientes que se van son reemplazados por expansiones de los que quedan.
- Pero cada vez queda una base más pequeña sosteniendo el crecimiento.

### 3. ¿Por qué el NRR es 114% entonces?
Porque los 36 clientes que quedan (o algunos de ellos) **subieron de plan** y aumentaron su gasto promedio. Eso compensó con creces la pérdida de ingresos de los 4 que se fueron.

Pero eso no es sostenible si el churn de clientes sigue alto. Eventualmente, la base se erosiona y las expansiones no pueden compensar.

### 4. ¿Puedes dejar de preocuparte por el churn?
**No.** Debes preocuparte por **dos churns**:
- **Churn de ingresos** (NRR): aquí vas bien (114%).
- **Churn de clientes** (Customer Retention Rate): aquí vas mal (90% de retención, 10% de churn).

Ignorar el churn de clientes es un error estratégico. Los clientes que se van suelen ser señal de:
- Problemas de producto/servicio.
- Mal fit con el mercado.
- Fallos en onboarding o soporte.

### 5. Recomendación inmediata
1. **Investiga por qué se fueron esos 4 clientes.** Haz entrevistas de salida, revisa patrones (¿eran del mismo plan? ¿mismo sector? ¿mismo tiempo de vida?).
2. **No descuides la retención** por tener un NRR bonito. Un NRR alto con churn de clientes alto es una bomba de relojería.
3. **Equilibra esfuerzos:** sí, captura nuevos clientes, pero también invierte en reducir el churn de clientes (mejora de producto, onboarding, soporte proactivo).
4. **Mide ambas métricas** en tu panel: NRR **y** Customer Retention Rate. No te quedes solo con una.

**En resumen:** tu NRR es excelente, pero tu retención de clientes es mediocre. No bajes la guardia.