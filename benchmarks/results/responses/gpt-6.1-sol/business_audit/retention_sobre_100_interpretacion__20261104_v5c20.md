# GPT-6.1 Sol — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 8.448s | tokens_per_second: 57.3
- input_tokens: 128 | output_tokens: 484

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. **Retener el 114% de los ingresos no significa retener el 114% de los clientes**, ni que puedas dejar de preocuparte por el churn.

Ese 114% probablemente es **retención neta de ingresos (NRR)**: los clientes que ya tenías generan ahora un 14% más de ingresos recurrentes en conjunto, porque las subidas de plan compensaron las bajas y posibles reducciones. Para que sea NRR, **debe excluir los ingresos de clientes nuevos**.

Con tus datos:

- **Clientes de pago:** pasaste de 40 a 36, una caída neta del **10%**.
- **Si no hubo altas nuevas:** perdiste 4 clientes; tu retención de clientes fue del **90%** y tu churn de clientes, del **10% mensual**.
- **Si hubo altas nuevas:** las bajas fueron mayores que 4 y la retención de la cohorte inicial fue inferior al 90%. Por ejemplo, si captaste 3 nuevos y acabaste con 36, perdiste 7 de los 40 originales.

La retención de clientes de una cohorte no puede superar el 100%. Lo que sí puede superarlo es la retención **neta de ingresos**, gracias a la expansión.

**La lectura correcta es: la expansión está compensando la pérdida de clientes, no eliminándola.** Es una buena señal de monetización, pero puede ocultar un problema de retención y aumentar tu dependencia de quienes suben de plan.

No pondría todo el esfuerzo en captar. Primero comprobaría qué calcula exactamente el panel y miraría por separado:

| Métrica | Qué te permite ver |
|---|---|
| Retención/churn de clientes | Cuántos clientes originales conservas o pierdes |
| Retención bruta de ingresos (GRR) | Cuánto ingreso conservas **sin** contar las subidas de plan |
| Retención neta de ingresos (NRR) | Si la expansión compensa las pérdidas |

**Si ese 10% de churn mensual se confirma, merece atención prioritaria**, aunque la NRR sea del 114%. Con solo 40 clientes habrá volatilidad, así que revisa también varios meses y los motivos de baja antes de decidir cómo repartir el esfuerzo entre adquisición y retención.