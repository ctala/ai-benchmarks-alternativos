# KAT Coder Pro v2.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 8.98 | quality: 10.0
- latency_total: 5.644s | tokens_per_second: 105.1
- input_tokens: 143 | output_tokens: 593

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa



No, no es correcto. Estás confundiendo dos métricas distintas.

**Lo que dice el 114% (NRR - Net Revenue Retention):**
Que el ingreso proveniente de los clientes que tenías al inicio del período creció un 14% neto, gracias a que algunos subieron de plan. Es una señal positiva de expansión, pero **solo mide dinero, no personas**.

**Lo que dice tu contexto (churn de clientes):**
Perdiste 4 de 40 clientes. Eso es un **10% de churn de clientes en un solo mes**, lo cual es alto. Si se mantiene, estarías renovando apenas ~28% de tu base al cabo de un año.

**Por qué el NRR puede ser alto aunque el churn duela:**
El NRR pondera por ingresos. Si los clientes que se fueron eran de planes bajos y los que se quedaron (o subieron) son de planes altos, el ingreso neto sube aunque la base de clientes se encoja. Es un efecto de "composición" que oculta la fuga.

**Conclusión operativa:**
No puedes dejar de preocuparte por el churn. Tienes dos problemas separados:
1. **Retención de ingresos:** Bien (114%). Sigue invirtiendo en expansión/upsell.
2. **Retención de clientes:** Mal (10% mensual). Necesitas entender por qué se van esos 4 clientes y si son perfiles que, aunque pagan poco, son semilla de crecimiento futuro o referencia.

Ignorar el churn de clientes porque el NRR se ve bien es un error común y costoso. La base se puede erosionar silenciosamente hasta que el NRR también caiga.