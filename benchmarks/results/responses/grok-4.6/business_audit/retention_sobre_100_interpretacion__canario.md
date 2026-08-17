# Grok 4.6 — business_audit/retention_sobre_100_interpretacion

- model_id: `x-ai/grok-4.6`
- success: True  | final: 7.96 | quality: 10.0
- latency_total: 160.105s | tokens_per_second: 10.8
- input_tokens: 328 | output_tokens: 1722

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No. La lectura correcta es menos halagadora.**

“Retención de ingresos: 114 %” es casi seguro **retención neta de ingresos (NRR / NDR)**. Puede superar el 100 % porque las expansiones (subidas de plan) compensan el churn y las contracciones. **No significa** que casi no se te vaya nadie ni que la retención de clientes esté por encima del 100 %.

La retención de **clientes/logos** de una cohorte existente no puede superar el 100 %. En tu caso:

- Partías de 40 clientes de pago.
- Ahora tienes 36.
- Has perdido 4 clientes → retención de logos ≈ 90 % y churn de clientes del 10 % (mensual).

Eso es pérdida real de clientes. El 114 % solo indica que los 36 que se quedaron (más las subidas de plan) generaron más ingresos que los 40 iniciales. El crecimiento de ingresos de la base existente enmascara la fuga de logos.

No puedes dejar de preocuparte por el churn ni meter todo el esfuerzo solo en captación. Un 10 % de churn mensual de clientes es elevado para la mayoría de SaaS (incluso con NRR alto). Consecuencias típicas:

- El cubo tiene un agujero grande: cada mes pierdes una fracción relevante de la base.
- Las expansiones vienen de un grupo cada vez más pequeño. No es sostenible a medio plazo.
- Los que se van pueden ser precisamente los que no habrían expandido o los que indican problemas de producto, onboarding, valor percibido o encaje.
- Adquirir para reemplazar churn es más caro y menos eficiente que retener.

Distingue siempre:
- **NRR (neta, la que ves al 114 %)**: incluye expansiones. Puede ser >100 %.
- **GRR (bruta)**: excluye expansiones. Suele estar ≤100 % y muestra mejor cuánto se “escapa” realmente.
- **Retención de logos / clientes**: la que tienes al 90 %. Es la que no puede superar 100 % en la cohorte existente.

Sigue midiendo y actuando sobre el churn de clientes (por qué se fueron esos 4, en qué momento, de qué planes, etc.). El NRR alto es una buena señal de que hay poder de expansión en los que se quedan, pero no sustituye tapar la fuga. Equilibra retención (especialmente logos) y captación; ignorar el churn suele salir más caro. 

Si tienes los importes de MRR inicial vs final o el desglose (expansiones vs churn vs contracciones) se puede afinar más el diagnóstico.