# Claude Opus 5 (suscripción) — business_audit/retention_sobre_100_interpretacion

- model_id: `claude-opus-5`
- success: True  | final: 7.97 | quality: 10.0
- latency_total: 75.63s | tokens_per_second: 53.9
- input_tokens: 2 | output_tokens: 4074

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

## No. Estás leyendo dos métricas distintas como si fueran una

"Retención de ingresos" (NRR / net revenue retention) mide **plata**, no **personas**. Y solo mide la plata de la cohorte inicial: toma los 40 clientes que tenías el mes pasado, ve cuánto facturan hoy esos mismos 40, y compara. Las bajas restan; los upgrades suman. Un número puede tapar al otro.

Tus dos métricas del mes:

| Métrica | Valor | Qué dice |
|---|---|---|
| Retención de ingresos (NRR) | 114% | Los que quedaron pagan más que todo el grupo antes |
| Retención de clientes (logo) | **90%** | Se te fue 1 de cada 10, en un mes |

Son compatibles. Y la segunda es la que manda para decidir dónde poner esfuerzo.

## Lo que significa 90% mensual

Un 10% de churn mensual, sostenido:

- **0,90^12 = 28%.** De 100 clientes de hoy, en 12 meses quedan 28.
- Vida promedio del cliente: **~10 meses**.
- Para no encoger necesitas reponer **~3,6 clientes al mes** antes de crecer un peso.

Eso no es "prácticamente no se me va nadie". Es una cubeta con un agujero al que le estás echando agua más rápido de lo que sale... a veces.

**Y ojo con un detalle que cambia todo:** dijiste 40 → 36. Si en el mes captaste clientes nuevos, esos 36 los incluyen, y entonces la fuga real es peor. Con 3 altas nuevas, se te fueron 7 de 40 = **17,5% mensual** → 5,7 meses de vida promedio y 10% de supervivencia al año. Antes de cualquier conclusión, separa altas de bajas. El neto miente.

## Qué hay realmente detrás del 114%

Hagamos el número con índice 100 (asumiendo ticket parejo, ajústalo con tus datos reales):

- Base: 40 clientes = 100
- Se van 4 = −10 → quedan 90
- NRR 114 → los 36 que quedaron facturan 114
- **Expansión = +24 sobre una base de 90 = los que se quedaron subieron su gasto ~27%**

Ese es el dato incómodo: tu 114% no viene de que la gente se quede, viene de que **unos pocos pagaron bastante más**. Tu MRR se concentró. Si mañana se va uno de esos que subió de plan, el NRR no baja a 100 — se te va abajo de 90 de un golpe.

Dos verificaciones antes de festejar el 114%:

1. **¿Cuántas cuentas hicieron la expansión?** Si son 2 o 3, no tienes una métrica de retención, tienes un riesgo de concentración disfrazado.
2. **¿Cómo se contabilizó el upgrade?** Si alguien pasó de mensual a anual con descuento, muchos paneles registran el cobro completo en el mes y eso infla la expansión de forma brutal — cuando el efectivo mensual real, prorrateado, puede ser **menor**. Un anual con 41% de descuento sobre el mensual entra como salto de ingreso y es, en tasa mensual, una baja de precio. Revisa si tu panel prorratea.

## El techo que casi nadie ve

La expansión tiene tope. Un cliente puede subir de plan una, dos veces. Después llega al tier más alto y ya no sube más. Cuando eso pasa, **el NRR converge hacia tu retención de clientes**. Con 90% mensual, tu NRR futuro tiende a 90%, no a 114%.

Dicho crudo: el 114% de este mes es un préstamo contra el crecimiento futuro de esas mismas cuentas. No es un motor, es un evento.

## Entonces, ¿churn o adquisición?

Ninguna de las dos como la planteaste. El churn **es** tu problema de adquisición.

Con vida de 10 meses, cada cliente que traes vale 10 meses de ticket. Ese número define cuánto puedes gastar en captar y a qué velocidad puedes crecer. Meter todo a adquisición con la cubeta así te deja pagando dos veces por el mismo cliente: te va a costar más traer al reemplazo que lo que habría costado retener al que se fue.

Además, no puedes atacar el churn si no sabes qué se está yendo. Sospecha lógica dado el patrón: los que se quedan y suben son un perfil, y los que se van son otro — probablemente los que entraron por el canal equivocado o nunca llegaron al momento de valor. Eso se ve segmentando bajas por canal de origen y por antigüedad, no en el número agregado.

## Qué haría yo esta semana

1. **Separa altas de bajas.** Necesitas churn bruto, no el neto 40→36.
2. **Lista las 4 bajas con nombre**: cuánto pagaban, por qué canal entraron, cuántos meses duraron, último día que usaron el producto. Con n=4 no hay estadística, pero sí hay causa.
3. **Mira la curva de supervivencia por cohorte**, no el mes. ¿El churn se concentra en los primeros 30-60 días? Casi siempre sí — y eso es onboarding, no producto.
4. **Reporta las dos métricas juntas, siempre.** NRR sola es la métrica más fácil de usar para engañarte a ti mismo.

Una advertencia honesta en sentido contrario: **un mes no es una tendencia.** Con 40 clientes, 4 bajas tiene un intervalo de confianza que va aproximadamente de 3% a 24%. Puede que tu churn real sea 5% y este mes te fue mal. Por eso el punto 3: la decisión sale de 3-6 meses de cohortes, no del panel de hoy. Lo que sí puedes descartar hoy, con certeza, es la lectura "no se me va nadie". Esa está descartada por definición: 40 menos 36.