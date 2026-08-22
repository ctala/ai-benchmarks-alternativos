# GLM 5.3 — business_audit/retention_sobre_100_interpretacion

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.87 | quality: 8.0
- latency_total: 64.533s | tokens_per_second: 75.7
- input_tokens: 138 | output_tokens: 4885

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, esa lectura es incorrecta en dos puntos distintos. Y la lectura correcta es menos halagadora, pero mucho más útil. Vamos por partes.

## Qué significa realmente un NRR de 114%

La retención neta de ingresos se calcula así:

**NRR = (MRR inicial + expansión − contracción − churn) / MRR inicial**

Un 114% significa que los clientes que ya tenías el mes pasado ahora generan un 14% más de ingresos, *neto de todo*. Es decir: lo que ganaste con subidas de plan superó lo que perdiste con bajas. Nada más. Y nada menos.

## Lo que tus números dicen realmente

- **Retención de clientes: 36/40 = 90%.** Perdiste 4 clientes, un churn mensual del 10%.
- La retención de clientes **nunca puede superar el 100%**. El 114% es de ingresos, no de personas. Estás mezclando dos métricas distintas.

Y ojo: si entre los 36 actuales hay clientes nuevos, el churn real es aún mayor (te fueron más de 4).

Un churn de logos del 10% mensual, si se sostiene, anualiza a ~72% de base perdida al año (0.9¹² ≈ 28% de clientes restantes). Un solo mes puede ser ruido —quizá expiró una cohorte concreta—, pero es una tasa que exige investigación, no celebración.

## Lo que realmente pasó: la expansión está enmascarando el churn

Ejemplo ilustrativo (ajusta con tu MRR real): si partías de $4.000 y los 4 que seieron eran clientes medios (−$400), para llegar a 114% necesitas ~$960 de expansión. Es decir, algo así como **+24% de expansión tapando un −10% de churn**.

Que tu motor de expansión funcione es una buena noticia real. Pero es una mala base para decidir "ignorar el churn", por tres razones:

1. **Balde agujereado.** Cada cliente nuevo entra a un producto que pierde ~10% de su base al mes. Vida esperada ≈ 10 meses (1/tasa de churn). Si tu CAC payback supera eso, la adquisición destruye valor en lugar de crearlo.
2. **Concentración.** Con 36 clientes y varios en planes superiores, tu MRR depende de menos cuentas. Perder una grande ahora duele más que antes.
3. **La expansión se agota.** No puedes subir de plan a los mismos clientes indefinidamente. Cuando la expansión se sature (y se satura), el churn quedará expuesto y el NRR caerá bajo el 100%.

Además: 4 bajas en un mes es una señal de producto/mercado que la métrica agregada esconde. ¿Eran del mismo segmento? ¿De la misma cohorte o canal de adquisición?

## Qué haría yo

- **Pide al panel la retención bruta de ingresos (GRR)**: excluye la expansión y no puede superar el 100%. Ese es tu indicador honesto de retención. Con tus números, probablemente ronde el 85–90%.
- **Habla con los 4 que se fueron** (o analiza su comportamiento). El churn casi siempre es diagnosticable: onboarding, expectativa incumplida, precio, o mal fit del canal.
- **Mira el churn por cohortes de 3–6 meses** antes de asumir que el 10% es tu tasa estructural.
- Y sí, invierte en adquisición —un NRR de 114% es un activo que pocas empresas tienen— pero no "todo el esfuerzo". Con un balde que pierde un 10% al mes, cada euro en captación rinde menos de lo que el panel te hace creer.

**En resumen:** el 114% es una métrica buena que describe un problema real. La expansión te está comprando tiempo; úsalo para arreglar el churn, no para ignorarlo.