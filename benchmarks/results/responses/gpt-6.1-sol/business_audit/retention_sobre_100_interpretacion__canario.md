# GPT-6.1 Sol — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 7.11 | quality: 8.0
- latency_total: 11.616s | tokens_per_second: 52.8
- input_tokens: 128 | output_tokens: 613

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. **Retener el 114% de los ingresos no significa retener el 114% de los clientes, ni que casi nadie se vaya.** Puedes perder clientes y aumentar los ingresos porque quienes se quedan suben de plan.

### Qué dicen tus números

Pasaste de **40 a 36 clientes de pago**: tu base cayó un **10% neto**.

- **Si no entró ningún cliente nuevo**, retuviste 36 de los 40: **retención de clientes del 90% y churn de clientes del 10% mensual**.
- **Si entraron clientes nuevos**, la retención de los 40 originales es aún menor: las altas están compensando parte de las bajas.

La retención de una cohorte de clientes **no puede superar el 100%**. El crecimiento del número total de clientes sí puede hacerlo, pero es otra métrica.

### Qué puede significar ese 114%

Si el panel muestra **retención neta de ingresos (NRR)**, significa que los clientes que ya tenías generan ahora un 14% más de ingresos recurrentes, **incluyendo subidas de plan y descontando bajas y reducciones**, pero **sin contar ingresos de clientes nuevos**.

Por ejemplo: esos 40 clientes generaban 10.000 € de MRR; los que siguen generan ahora 11.400 €. Tienes menos clientes, pero más ingresos de esa cohorte.

**Comprueba la definición del panel**: si incluye ingresos de nuevos clientes, ese 114% no sería NRR correctamente calculada.

### ¿Dejar de preocuparte por el churn?

**No. La expansión puede estar ocultando una pérdida importante de clientes.** Un 114% de NRR es una señal favorable de expansión, pero no demuestra por sí solo una base sana. Además, las subidas de plan pueden concentrarse en pocos clientes y no repetirse cada mes.

Antes de volcar todo el esfuerzo en captación, revisaría:
- **Churn de clientes:** cuántos de los 40 originales se fueron y por qué.
- **Retención bruta de ingresos (GRR):** cuánto ingreso conservas sin permitir que las ampliaciones compensen las pérdidas.
- **Concentración de la expansión:** si ese crecimiento depende de unos pocos clientes.

**La lectura correcta es: “la expansión supera las pérdidas de ingresos”, no “no tengo un problema de churn”.** Si ese 10% mensual corresponde realmente a bajas, merece atención prioritaria junto con la captación.