# Claude Fable 5.1 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 8.07 | quality: 10.0
- latency_total: 18.569s | tokens_per_second: 64.9
- input_tokens: 218 | output_tokens: 1205

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, la lectura no es correcta. Dos aclaraciones importantes:

**1. La retención de clientes nunca puede superar el 100%.**
El 114% es **retención neta de ingresos (NRR)**: ingresos actuales de la cohorte del mes pasado ÷ ingresos del mes pasado de esa misma cohorte. Incluye expansiones (subidas de plan), y por eso puede superar el 100%. Pero no te dice nada sobre cuántos clientes se quedan.

**2. Con tus números, el churn de clientes es alto, no inexistente.**
- 40 → 36 clientes = **10% de churn de logos en un mes** (y eso suponiendo que no entró ningún cliente nuevo; si captaste alguno, perdiste más de 4 y el churn es aún mayor).
- 10% mensual anualizado: 1 − 0,9¹² ≈ **72% de clientes perdidos al año**. Para SaaS B2B, un churn mensual sano suele estar por debajo del 2-3%.

Lo que está pasando: las subidas de plan de unos pocos clientes tapan la fuga de otros. El NRR mide el *neto*, no la *ausencia* de pérdidas.

**Qué deberías mirar junto al NRR:**
- **GRR (retención bruta de ingresos)**: igual que NRR pero sin contar expansiones. Tiene techo en 100% y te dice cuánto ingreso pierdes realmente por bajas y downgrades. Si el NRR es 114% y perdiste 4 de 40, el GRR probablemente ronda el 85-90%, que es flojo.
- **Retención de logos**: 90% este mes.
- **Concentración de la expansión**: ¿cuántos clientes subieron de plan? Si son 3 o 4, tu crecimiento neto depende de muy pocas cuentas; si una de ellas se va el mes que viene, el NRR cae por debajo de 100 de golpe.

**Sobre dejar de preocuparte por el churn:**
Es justo lo contrario. Con 10% de churn mensual, captar clientes nuevos es llenar un cubo con agujeros: necesitas reponer el 10% de la base cada mes solo para no decrecer. Antes de escalar adquisición, conviene saber por qué se fueron esos 4 (precio, falta de uso, producto no encaja, se fueron a competencia), porque el motivo determina si el problema es arreglable.

**Resumen:** el 114% es una buena señal de que a quien se queda le aportas valor creciente, pero la retención de clientes es del 90% mensual, no "por encima del 100%". El churn sigue siendo tu problema principal.