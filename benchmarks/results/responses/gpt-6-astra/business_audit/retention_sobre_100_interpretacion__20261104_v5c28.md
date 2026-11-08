# GPT-6 Astra — business_audit/retention_sobre_100_interpretacion

- model_id: `openai/gpt-6-astra`
- success: True  | final: 6.7 | quality: 8.0
- latency_total: 11.975s | tokens_per_second: 39.5
- input_tokens: 128 | output_tokens: 473

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. **Retener ingresos no es lo mismo que retener clientes**, y tus datos muestran que las subidas de plan pueden estar compensando las bajas.

### Qué significa ese 114%
Si el panel se refiere a **retención neta de ingresos (NRR)**, significa que los clientes que ya tenías generan ahora un **14% más de ingresos recurrentes**, sumando las ampliaciones de plan y restando las reducciones y cancelaciones. **No incluye los ingresos de clientes nuevos.** Conviene confirmar la definición y el periodo del panel.

Por ejemplo: si esa misma base generaba 10.000 € mensuales y ahora genera 11.400 €, la NRR es del 114%, aunque algunos clientes se hayan ido.

### Qué dicen tus 40 → 36 clientes
La retención de clientes de una cohorte **no puede superar el 100%**.

- **Si no hubo altas ni reactivaciones**, conservaste 36 de 40: **90% de retención de clientes y 10% de churn mensual**.
- **Si hubo clientes nuevos**, la pérdida de clientes originales fue mayor: el 90% sería un máximo, no tu retención real. Por ejemplo, si entraron 4 nuevos, solo conservaste 32 de los 40 originales: 80% de retención.

Esto supone que comparas la misma base de clientes de pago y el mismo periodo.

### ¿Puedes despreocuparte del churn?
**No: una NRR del 114% es una buena señal de expansión, pero no demuestra que el churn esté controlado.** Puedes estar perdiendo muchos clientes mientras unos pocos que suben de plan sostienen los ingresos. Esa expansión podría no repetirse.

Antes de dedicar todo el esfuerzo a captación, revisaría:
1. **Churn de clientes:** cuántos se van, de qué segmentos y por qué.
2. **Retención bruta de ingresos (GRR):** cuánto ingreso conservas *sin* contar las ampliaciones.
3. **Concentración de la expansión:** si el crecimiento depende de pocos clientes.

**Tu lectura correcta es: “La base existente puede estar facturando más, pero tengo menos clientes; necesito entender las bajas antes de acelerar la captación”.**