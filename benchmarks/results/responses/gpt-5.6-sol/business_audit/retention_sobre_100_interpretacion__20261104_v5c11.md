# GPT-5.6 Sol — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 6.98 | quality: 8.0
- latency_total: 13.704s | tokens_per_second: 89.2
- input_tokens: 128 | output_tokens: 1222

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Estás mezclando **retención de ingresos** con **retención de clientes**.

### Qué suele significar ese 114%

Si el panel calcula **retención neta de ingresos (NRR)**:

\[
NRR = \frac{Ingresos\ iniciales - bajas - contracciones + expansiones}{Ingresos\ iniciales}
\]

Un 114% significa que los aumentos de plan compensaron las bajas y reducciones y, además, elevaron un 14% los ingresos recurrentes de la cohorte inicial. **No significa que casi ningún cliente se haya ido.**

### Tus clientes cuentan otra historia

Pasaste de 40 a 36 clientes:

- Crecimiento neto de clientes: **−10%**
- Si no captaste clientes nuevos, la retención de clientes fue **90%** y el churn, **10%**.
- Si sí captaste nuevos clientes, la retención real de la cohorte fue **inferior al 90%**, porque tuviste que perder más de cuatro para terminar en 36.

La retención de clientes de una cohorte no puede superar el 100%. Si un indicador lo hace, está incluyendo expansión de ingresos —o incluso altas nuevas—, no está midiendo únicamente clientes retenidos.

### ¿Puedes dejar de preocuparte por el churn?

No. Tu NRR es positiva, pero puede estar ocultando:

- bajas frecuentes entre clientes pequeños;
- dependencia de unos pocos clientes que pagan más;
- concentración de ingresos;
- un límite futuro a las subidas de plan;
- costes de adquisición desperdiciados si los nuevos clientes abandonan pronto.

Conviene revisar por separado:

1. **Retención de clientes o logos:** clientes iniciales que siguen activos.
2. **Churn de clientes:** clientes perdidos / clientes iniciales.
3. **Retención bruta de ingresos (GRR):** excluye expansiones y no puede superar 100%.
4. **NRR:** incluye expansiones, pero debería excluir clientes nuevos.
5. **Ingresos nuevos:** procedentes de captación.
6. **Concentración de la expansión:** cuántos clientes explican ese 114%.

La lectura correcta es: **tienes una expansión de ingresos fuerte, pero una evolución negativa en número de clientes**. Captar sigue siendo importante, pero ignorar el churn podría hacer que estés llenando un cubo con fugas. También verificaría la definición exacta del panel: si ese 114% incluye ingresos de clientes nuevos, no es realmente retención, sino crecimiento de ingresos.