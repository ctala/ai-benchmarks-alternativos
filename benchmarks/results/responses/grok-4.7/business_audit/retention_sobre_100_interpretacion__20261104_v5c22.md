# Grok 4.7 — business_audit/retention_sobre_100_interpretacion

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 15.528s | tokens_per_second: 74.9
- input_tokens: 1364 | output_tokens: 1163

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. El 114% no dice que casi no se te vaya nadie, ni que la retención de clientes supere el 100%.

Esa cifra es, casi con seguridad, **retención neta de ingresos** (NRR): ingresos que conservas de la base que ya tenías, más ampliaciones de plan, menos bajas y bajadas de plan. Puede pasar de 100% aunque pierdas clientes, si los que suben de plan aportan más dinero del que se llevan los que se van.

La retención de clientes no puede superar el 100%. En tus números, el mes pasado había 40 de pago y este mes 36. Si no entró nadie nuevo, perdiste 4 logos: un 10% en un mes. Si sí entraste clientes nuevos y aun así el total bajó a 36, la base antigua se redujo en más de 4. En cualquiera de los dos casos, el churn de clientes no es irrelevante.

Qué implica el 114%, y qué no:

- **Sí:** la cohorte antigua, en conjunto, factura más que el mes pasado. Las subidas de plan compensaron con creces el ingreso perdido.
- **No:** que la base esté sana, que el churn sea bajo, ni que puedas ignorarlo. El crecimiento de ingreso está concentrado en menos cuentas. Si se van quienes acaban de subir de plan, el agujero es mayor que el de una baja de un plan barato.

Antes de pasar todo el esfuerzo a captación, separa tres cifras:

1. **Retención de logos** de la cohorte (cuántos de esos 40 siguen).
2. **Retención bruta de ingresos** (GRR): solo lo que queda tras bajas y downgrades, sin contar upgrades. Esa no pasa de 100% y muestra cuánto ingreso se escapa de verdad.
3. **NRR (114%)**: el neto después de expansión.

Un 10% mensual de logos, si se sostiene, no se arregla con adquisición. Merece saber por qué se fueron esos clientes y qué parte del 114% depende de unas pocas subidas de plan.