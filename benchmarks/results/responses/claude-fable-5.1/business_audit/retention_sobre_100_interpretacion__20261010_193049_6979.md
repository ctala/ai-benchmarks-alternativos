# Claude Fable 5.1 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.97 | quality: 10.0
- latency_total: 32.11s | tokens_per_second: 61.0
- input_tokens: 218 | output_tokens: 1959

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Hay dos métricas distintas mezcladas, y la lectura correcta es bastante menos tranquilizadora.

## Lo que dice el 114% (y lo que no)

**Retención de ingresos (NRR)** compara cuánto facturas hoy a los clientes que ya tenías el mes pasado, incluyendo subidas de plan. Puede superar el 100% porque las expansiones suman.

**Retención de clientes (logo retention)** cuenta cuántos clientes siguen. No puede superar el 100%. La tuya es:

- 36 / 40 = **90% de retención de clientes**
- **10% de churn de clientes al mes**

El 114% no significa que "no se va nadie". Significa que los 36 que se quedaron gastaron suficiente de más para tapar el agujero de los 4 que se fueron y además dejar un 14% de margen.

## Por qué el 10% mensual es un problema serio

Un 10% mensual, sostenido, equivale a perder alrededor del 72% de tu base en un año. Para SaaS eso está muy lejos de lo saludable (B2B pequeño suele moverse en 2–4% mensual; enterprise, bastante menos).

Lo que hoy lo compensa son las expansiones, y eso es frágil por tres motivos:

1. **La expansión tiene techo; el churn no.** Un cliente solo puede subir de plan hasta el plan más alto. Después, deja de aportar expansión y solo puede quedarse o irse.
2. **El churn se acumula.** Cada mes partes de una base más pequeña. La expansión tiene que crecer cada mes solo para mantener el mismo NRR.
3. **Pueden ser los mismos clientes.** Si quienes suben de plan son 5–6 cuentas grandes, tu 114% depende de ellas. Pierde una y el número se da la vuelta.

## El dato que te falta: retención bruta (GRR)

Calcula cuánto ingreso de los 40 clientes del mes pasado conservas hoy **sin contar las expansiones**:

- Ingresos del mes pasado: X
- Menos lo que pagaban los 4 que se fueron
- Menos cualquier bajada de plan
- Resultado / X = GRR

Ese número siempre es ≤ 100% y te dice cuánto agua pierde el cubo antes de que la expansión lo rellene. Si está por debajo de ~90% mensual, el churn es tu prioridad, no la captación.

## Sobre dejar el churn y volcarte en captar

Es la decisión opuesta a la que sugieren tus datos. Con 10% de churn mensual, cada cliente nuevo que captas viene a sustituir uno que se fue, no a hacerte crecer. Pagas CAC para quedarte igual. Arreglar la retención hace que cada euro de adquisición rinda más; ignorarla hace que cada euro rinda menos.

## Matices antes de alarmarte del todo

- **Es un solo mes con 40 clientes.** 4 bajas pueden ser ruido o una coincidencia. Mira tres o seis meses antes de concluir que el 10% es tu tasa real.
- **Importa quién se fue.** Si los 4 eran cuentas mínimas, trials convertidos a medias o un segmento que no es tu cliente objetivo, la gravedad baja. Si eran clientes de más de seis meses pagando lo mismo que el resto, es señal de producto o de soporte.
- **Importa quién subió.** Si la expansión está repartida entre muchos clientes, el 114% es más robusto. Si son dos o tres, es concentración de riesgo.

## Resumen

Tu panel no está mintiendo, pero la métrica que mide no es la que creías. Se te están yendo 1 de cada 10 clientes al mes y lo están tapando los que suben de plan. Eso puede durar unos meses, no indefinidamente. Lo que haría ahora: calcular GRR, listar a los 4 que se fueron con motivo y antigüedad, y mirar la tendencia de churn de clientes de los últimos meses antes de mover presupuesto a adquisición.