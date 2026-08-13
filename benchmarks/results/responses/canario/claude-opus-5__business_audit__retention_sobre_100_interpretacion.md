# Claude Opus 5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 31.266s | tokens_per_second: 65.5
- input_tokens: 216 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

## Respuesta corta

No. Estás leyendo dos métricas distintas como si fueran una.

"Retención de ingresos" del 114% (normalmente NRR, *net revenue retention*) mide **euros**, no **clientes**. Tu retención de clientes ese mes fue del 90% (36/40), no del 114%. Ambas cosas son ciertas a la vez y no se contradicen: perdiste clientes y aun así ganaste ingresos, porque las subidas de plan de los que se quedaron taparon el agujero.

## Qué está pasando de verdad

Con los números que das, y asumiendo que los 4 que faltan son bajas netas:

- **Churn de clientes: ~10% mensual.** Si se mantuviera, en 12 meses te quedaría en torno al 28% de una cohorte (0,9¹²). Es decir, ~7 de cada 10 clientes se van en un año.
- **Para llegar a 114% con esa fuga**, la expansión tuvo que ser enorme: si los que se fueron eran de tamaño medio (~10% del MRR), la expansión rondó el 24% del MRR inicial en un solo mes. Eso no viene de "varios" clientes repartidos: viene de unas pocas cuentas.

Y ahí está el riesgo real: **tu 114% depende de un puñado de cuentas que subieron de plan.** Si una de ellas baja o se va el mes que viene, el mismo panel te puede marcar 85% sin que nada más haya cambiado. La métrica es volátil porque la base es pequeña.

## Dos comprobaciones antes de seguir

1. **¿36 son bajas netas o brutas?** Si captaste 3 nuevos y perdiste 7, tu churn no es 10% sino 17,5%. Necesitas los números brutos separados.
2. **¿Tu panel excluye clientes nuevos del cálculo?** La NRR solo debe medir la cohorte que existía al inicio del periodo. Muchos paneles meten el MRR nuevo dentro, y entonces ese 114% no es retención: es crecimiento disfrazado, y no te dice nada sobre si aguantas a los clientes.

## Por qué "todo a captación" es precisamente lo contrario

Con 10% de churn mensual, la vida media de un cliente es de unos 10 meses. Si tu CAC tarda más de eso en recuperarse, cada cliente nuevo que traes **destruye caja**. Estarías echando agua más rápido en un cubo agujereado: se ve movimiento, pero el nivel no sube. Y el churn encarece la captación de forma silenciosa, porque una parte creciente de tus nuevos clientes solo sirve para reponer los que se van, no para crecer.

## Qué mirar en su lugar

- **GRR (retención bruta de ingresos):** igual que la NRR pero sin contar expansión. Nunca pasa de 100% y te dice cuánto pierdes de verdad. Es la métrica honesta.
- **Retención de clientes (logo retention)** por separado, con altas y bajas en bruto.
- **Desglose del Net New MR