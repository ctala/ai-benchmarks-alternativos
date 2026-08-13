# Tencent Hy3 — business_audit/retention_sobre_100_interpretacion

- model_id: `tencent/hy3`
- success: True  | final: 8.77 | quality: 10.0
- latency_total: 58.125s | tokens_per_second: 55.2
- input_tokens: 162 | output_tokens: 3208

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

Hola. Como analista, mi objetivo es darte la lectura exacta de tus métricas, y en este caso específico, la interpretación intuitiva es peligrosa para la salud de tu negocio. 

La respuesta corta es: **No, tu lectura no es correcta, y bajo ningún concepto deberías dejar de preocuparte por el churn.**

Aquí tienes el desglose preciso de lo que está pasando en tu panel:

### 1. El error de concepto: Ingresos vs. Logos (Clientes)
Tu panel muestra **Retención de Ingresos** (en SaaS la llamamos *Net Revenue Retention* o NRR). Un 114% significa que, por cada 100€/$ que generabas el mes pasado con tu base de clientes, este mes estás generando 114€/$ con esa *misma* base, gracias a los upsells (subidas de plan).

Sin embargo, la **Retención de Clientes** (o *Logo Retention*) es una métrica completamente distinta. Según tu contexto, pasaste de 40 a 36 clientes. Eso significa que perdiste 4. 
*   Tu retención de clientes real es: **36 / 40 = 90%**.
*   Tu churn de logos (pérdida de clientes) es del **10% mensual**.

### 2. La lectura menos halagadora (La realidad de tu churn)
No es cierto que "prácticamente no se te va nadie". Estás perdiendo el 10% de tus clientes mes a mes. Si mantienes esa tendencia, tu retención anual de logos rondaría el 28% (es decir, perderías cerca del 72% de tus clientes en un año). 

El 114% de retención de ingresos está **enmascarando** tu problema de churn. Los pocos clientes que se quedaron y subieron de plan están pagando la factura de los que se fueron. Es una situación frágil: estás dependiendo de que los clientes restantes sigan haciendo upsell para compensar las fugas de tu embudo.

### 3. ¿Puedes dejar de preocuparte por el churn y solo captar?
**Absolutamente no.** Si haces eso, caerás en la trampa de la "rueda de hámster":
*   **Tu CAC (Costo de Adquisición) se disparará:** Necesitarás captar al menos 4 o 5 clientes nuevos *cada mes* solo para reponer los que se van, antes de poder crecer ni un solo logo.
*   **Fragilidad del NRR:** Un NRR > 100% es excelente, pero solo es sostenible si el churn de logos es bajo. ¿Qué pasa si los que se quedaron dejan de necesitar los planes altos o si la competencia les capta? Tu NRR caerá por debajo del 100% y tu MRR (Ingreso Recurrente Mensual) empezará a contraerse.
*   **Señal de alarma:** Un 10% de churn mensual indica casi siempre un problema serio de *product-market fit*, de onboarding (no ven valor rápido) o de atención al cliente que debes atajar urgentemente.

**Conclusión del analista:** 
Tienes un motor de expansión (upsell) muy bueno, lo cual es difícil de lograr. Pero tienes una gotera importante en la bañera. Sigue invirtiendo en captación, pero destina recursos inmediatos a entender por qué esos 4 clientes se fueron y cómo reducir ese churn del 10% al 2-3% mensual. Solo entonces tu NRR de 114% será realmente una métrica de éxito y no un parche.