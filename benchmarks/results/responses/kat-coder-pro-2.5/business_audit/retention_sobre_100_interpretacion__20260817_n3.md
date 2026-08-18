# KAT Coder Pro v2.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 10.813s | tokens_per_second: 88.0
- input_tokens: 143 | output_tokens: 952

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa



No, no es correcto. De hecho, es una lectura peligrosa.

**El NRR (Net Revenue Retention) mide ingresos, no clientes.** Un 114% te dice que los dólares que dejó tu base de clientes existente crecieron 14%, pero no te dice cuántos clientes se fueron. Son dos cosas distintas.

En tu caso:
- Tenías 40 clientes, ahora tienes 36
- **Perdiste 4 clientes = 10% de churn de logos**
- Pero los que se quedaron (o algunos de ellos) subieron de plan lo suficiente como para compensar con creces los ingresos perdidos

Esto se llama **"churn enmascarado por expansión"**. Es más común de lo que crees y es una trampa clásica.

**Por qué deberías preocuparte:**

1. **La expansión tiene un techo, el churn no.** Tus clientes actuales no pueden subir de plan infinitamente. Llegará un punto en que el upsell se agote, y entonces el churn que estás ignorando se hará visible de golpe en tus ingresos.

2. **Estás quemando base.** Perder 10% de clientes en un mes es alto. Si mantienes ese ritmo, en 10 meses te quedas sin base, por mucho que los que se quedan paguen más.

3. **El NRR te miente sobre salud del producto.** Un cliente que se va es una señal de que algo no funcionó para él. Si ignoras esas señales porque los ingresos totales suben, estás perdiendo información crítica para mejorar.

**Lo que deberías mirar además del NRR:**

- **Logo Retention Rate** (retención de clientes, no de ingresos): en tu caso, 36/40 = 90%. Eso es lo que realmente importa para entender si tu producto retiene.
- **Churn rate de clientes**: 10% mensual es alto para la mayoría de SaaS B2B. Lo saludable suele estar entre 1-3% mensual.
- **NRR por cohorte**: ¿los clientes que entraron hace 6 meses se quedan y expanden, o los que se van son los antiguos?

**En resumen:** el 114% es una buena noticia financiera a corto plazo, pero el 10% de churn de clientes es una mala noticia de producto a medio plazo. No puedes ignorar lo segundo porque lo primero te hace sentir cómodo. De hecho, es el momento exacto de investigar por qué se van esos 4 clientes: ¿son los planes más bajos? ¿algún segmento específico? Esa información es más valiosa que el NRR ahora mismo.