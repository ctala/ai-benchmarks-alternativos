# Claude Sonnet 5.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.08 | quality: 8.0
- latency_total: 13.615s | tokens_per_second: 113.3
- input_tokens: 218 | output_tokens: 1542

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, la lectura correcta es bastante menos halagadora.

**Qué mide realmente el 114%**

La retención neta de ingresos (NRR) compara los ingresos actuales de la cohorte que tenías al inicio con los que tenía entonces:

NRR = (MRR inicial + expansión − contracción − MRR perdido por bajas) / MRR inicial

Un 114% significa que las subidas de plan de los clientes que se quedaron compensaron con creces los ingresos de los que se fueron. **No dice nada directo sobre cuánta gente se va.** Un solo cliente grande que triplique su plan puede tapar muchas bajas.

**Tu retención de clientes**

Pasaste de 40 a 36, así que:

- Retención de clientes (logo retention): **90%** como mucho. Si en el mes entraron clientes nuevos, las bajas son más de 4 y la retención es peor.
- Churn de clientes: **10% en un mes**. Es muy alto; si se mantuviera, perderías más del 70% de tus clientes al año.

La retención de clientes no puede superar el 100%, porque sin captación nueva no puedes tener más clientes de los que tenías.

**Por qué no deberías dejar de preocuparte por el churn**

1. **La expansión tiene techo.** Cada cliente solo puede subir de plan un número limitado de veces. El churn, en cambio, es continuo, y tarde o temprano supera a la expansión.
2. **Concentración.** Con 36 clientes, dos o tres upgrades grandes pueden explicar todo el 114%. Si esos clientes se van o dejan de crecer, el número se desploma.
3. **Cubo con fugas.** Si metes más clientes en un producto que pierde el 10% mensual, gastas CAC en reponer lo que se va, y el crecimiento será caro e inestable.
4. **El churn probablemente te está diciendo algo.** Si los que se van son clientes pequeños y los que suben son grandes, quizá tienes un buen producto para un segmento y uno malo para otro.

**Qué miraría en tu lugar**

- **Retención bruta de ingresos (GRR):** igual que el NRR, pero sin contar la expansión. Nunca supera el 100% y muestra el daño real de las bajas.
- **Quién se fue:** tamaño, antigüedad, plan, canal de adquisición y motivo.
- **Distribución de la expansión:** cuántos clientes y qué porcentaje del MRR explican el 114%.
- **Churn por cohortes:** si se van sobre todo en los primeros meses, es un problema de onboarding o de encaje con el cliente.
- **Periodo del dato:** comprueba si el 114% es mensual, trimestral o anual, porque cambia mucho la interpretación.

Captar clientes y reducir el churn no son excluyentes, pero con un 10% de bajas mensuales yo arreglaría primero la fuga, o al menos la trabajaría en paralelo, antes de volcar todo el esfuerzo en captación.