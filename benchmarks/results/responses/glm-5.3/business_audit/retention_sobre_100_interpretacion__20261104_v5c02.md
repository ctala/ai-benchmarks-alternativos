# GLM 5.3 — business_audit/retention_sobre_100_interpretacion

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 70.09s | tokens_per_second: 64.4
- input_tokens: 138 | output_tokens: 4513

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, ambas lecturas son incorrectas, y una de ellas es conceptualmente imposible. Vamos por partes.

## Qué mide realmente ese 114%

La retención de ingresos (NRR) es una métrica de **dinero sobre una cohorte**, no de clientes:

> NRR = (MRR inicial + expansión − contracción − churn de MRR) / MRR inicial

No puedes retener al 114% de tus clientes —el máximo es 100%— pero sí puedes facturarle el 114% a los que quedan. Eso es exactamente lo que te está pasando: **la expansión de unos está compensando (y superando) la fuga de otros**. El panel te muestra el neto; las dos fuerzas opuestas quedan invisibles.

## Lo que dicen tus números

Bajaste de 40 a 36 clientes. En el mejor escenario (ninguno de los 36 es nuevo), perdiste **4 de 40 = 10% de churn mensual de logos**. Si alguno de los 36 entró este mes, el churn real es mayor —revisa cuántos son altas nuevas—.

Ilustración con números redondos (40 clientes × 100 € de media = 4.000 € MRR):

| Concepto | Valor |
|---|---|
| MRR inicio | 4.000 € |
| Churn (4 clientes × 100 €) | −400 € (−10%) |
| Subidas de plan | +960 € (+24%) |
| MRR fin de cohorte | 4.560 € → **114%** |

El "114%" esconde un −10% y un +24%. Uno de cada diez clientes se fue este mes; a ese ritmo, en un año conservas solo ~28% de tu base (el 0,9¹²). El churn no ha desaparecido: está **subvencionado** por las subidas de plan.

## Por qué "todo a captación" es la conclusión equivocada

- **Cubo agujereado**: si los que se van son del tier de entrada (donde suelen aterrizar los clientes nuevos), parte de tu inversión en captación se drena cada mes.
- **La expansión tiene techo**: los clientes que suben de plan tienen un límite. A medida que la base se encoge, se encoge también el activo que financia tu NRR.
- **Riesgo de concentración**: si el crecimiento depende de pocos cuentas que expanden mucho, perder una de ellas duele el doble.
- **Caso legítimo pero distinto**: hay negocios que aceptan deliberadamente churn alto en un segmento y expansión fuerte en otro. Si es tu caso, debe ser una decisión con datos, no un supuesto sacado de un número neto.

## Lo que sí es cierto

114% de NRR es objetivamente buena señal: tus clientes supervivientes valoran el producto y pagan más. Varios inversores consideran >110% excelente. El error no es la métrica; es la inferencia "NRR alto ⇒ nadie se va".

## Qué hacer esta semana

1. **Separa los componentes**: pide a tu panel el GRR (retención bruta) y el churn de logos. Si solo muestra el NRR, es porque es el número que más favorece.
2. **Cuenta las altas nuevas** dentro de los 36 para calcular el churn real de logos.
3. **Segmenta**: ¿qué plan tenían los que se fueron vs. los que subieron? Si son perfiles distintos, tienes dos mercados con problemas distintos.
4. **Entrevistas de salida** con los 4 (o más) que se fueron.

En resumen: no, no puedes dejar de preocuparte por el churn. El 114% no dice que nadie se va; dice que los que se quedan pagan lo suficiente para que no lo notes. Todavía.