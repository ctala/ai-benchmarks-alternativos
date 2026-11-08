# Ling 3.0 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 48.967s | tokens_per_second: 34.6
- input_tokens: 165 | output_tokens: 1694

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, no puedes dejar de preocuparte. Y de hecho, lo que tienes es más interesante —y más peligroso— de lo que crees. Vamos a desglosarlo.

---

## Lo que dice tu panel vs. lo que está pasando realmente

**Retención de ingresos del 114%** es una métrica de *Net Revenue Retention* (NRR). Significa:

> "Si contabilizo solo los ingresos de los clientes que ya tenían al inicio del mes (sin contar nuevos), esos ingresos netos han crecido un 14%."

Eso se consigue porque los upsells superaron al churn de ingresos. **No significa que retengas al 114% de tus clientes.** Eso es matemáticamente imposible.

Tu retención **de clientes** es otra historia:

| Métrica | Cálculo | Resultado |
|---|---|---|
| **Retención de clientes** | 36 ÷ 40 | **90%** |
| **Churn de clientes** | 4 ÷ 40 | **10% mensual** |
| **Retención de ingresos (NRR)** | Ingresos base existente (netos de churn + upsells) | **114%** |

---

## Por qué el 114% te está engañando

Tu panel está midiendo **dinero**, no **personas**. Y lo que está ocurriendo es una dinámica que debe encender alarmas:

- **Estás perdiendo el 10% de tu base de clientes cada mes.** Eso es un churn elevado.
- **Los que se quedan están subiendo de plan**, y eso compensa numéricamente las bajas y luego some.
- Tu NRR del 114% **solo es posible gracias a los upsells**, no a la fidelidad. Si tus upgrades se desaceleran un mes, ese 114% se convierte en un **-10%** inmediatamente.

En otras palabras: **tu negocio depende de que la gente suba de plan más rápido de lo que se va.** Eso no es estabilidad; es una carrera contra el reloj.

---

## Por qué no puedes ignorar el churn

1. **La base se erosiona.** Estás en un ciclo donde necesitas captar o hacer upgrade constantemente solo para mantener el ritmo. Si el churn se estanca al 10% mensual y los upsells crecen un 14%, aún tienes margen. Pero si el churn sube al 15%, el NRR cae a 105% —y si los upsells se ralentizan, a valores negativos.

2. **El CAC se dispara.** Cada cliente que se va tiene que ser reemplazado por uno nuevo (o por dos upgrades). Si tu coste de adquisición es significativo, estás en una trampa: gastas en captar para compensar pérdidas, no para crecer.

3. **El patrón sugiere un problema de producto o segmento.** Que pierdas clientes y los que queden suban puede indicar que los clientes que se van son los más pequeños (que naturalmente no hacen upgrade) y los que se quedan son los que tienen más valor y buscan más funcionalidad. Eso es una señal de producto, no de éxito.

---

## Lo que deberías hacer

- **Separar las métricas en tu panel:** retención de clientes, churn de clientes, NRR y *expansion revenue* por separado. El 114% sin el contexto del 90% de retención de clientes es una trampa de dashboard.
- **Investigar el churn del 10%:** ¿Por qué se van esos 4 clientes? ¿Es pricing, producto, soporte, o simplemente eran clientes que nunca encajaron?
- **No meter todo el esfuerzo en nueva captación.** Captar es necesario, pero primero necesitas bajar ese churn del 10%. Cada punto de churn que reduces es más eficiente que un nuevo cliente que llega a compensarlo.

**Resumen:** Tu retención de ingresos es buena noticia, pero tu retención de clientes es una mala noticia. Una no anula a la otra. El 114% no es señal de que puedas descuidar el churn; es señal de que el churn te está costando caro y los upsells están pagando la factura.