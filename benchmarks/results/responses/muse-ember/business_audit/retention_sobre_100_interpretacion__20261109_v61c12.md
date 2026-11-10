# Muse Ember — business_audit/retention_sobre_100_interpretacion

- model_id: `meta/muse-ember`
- success: True  | final: 9.0 | quality: 10.0
- latency_total: 8.828s | tokens_per_second: 368.6
- input_tokens: 144 | output_tokens: 3254

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, es justo lo contrario de lo que sugiere el 114%. Y esa es la lectura importante aquí.

**La retención de clientes nunca puede ser superior al 100%.** Si empiezas con 40, como máximo puedes retener al 100% (40). No puedes retener al 114% (45,6 clientes).

La que puede superar el 100% es la **retención de ingresos**, y no significa que no se te vaya nadie. Significa otra cosa.

### Qué mide ese 114%

Casi seguro tu panel muestra *Net Revenue Retention* (NRR), no retención bruta.

La fórmula es:

**NRR = (Ingresos iniciales + Expansión - Contracción - Churn) / Ingresos iniciales**

Expansión = subidas de plan de los que se quedan
Contracción = bajadas de plan
Churn = ingresos de los que se van

Si el resultado es 114%, solo te dice que en esa cohorte, **la expansión superó a la contracción + churn en un 14%**. No te dice que el churn sea bajo. De hecho, lo está escondiendo.

La métrica que sí mide churn sin maquillaje es la **Gross Revenue Retention (GRR)**, que excluye la expansión:

**GRR = (Ingresos iniciales - Contracción - Churn) / Ingresos iniciales**

La GRR nunca puede pasar del 100%.

### Con tus números

Pasaste de 40 a 36 clientes de pago. Asumiendo que esos 36 son solo supervivientes de los 40 (si entre los 36 hay clientes nuevos, la retención es aún peor):

**Retención de logos = 36 / 40 = 90%**
**Churn de logos mensual = 10%**

Te se fue 1 de cada 10 clientes en un mes. Eso no es "prácticamente nadie". Con un churn mensual del 10%, la vida media de un cliente es de unos 10 meses, y en 12 meses solo sobreviviría el 28% de la base inicial (0,9^12).

Un ejemplo para que se vea el 114%:

Cohorte inicial: 40 clientes = 4.000€ MRR
- Se van 4 clientes: -400€
- Los 36 restantes suben de plan: +960€
- Total de la cohorte este mes: 4.560€

NRR = 4.560 / 4.000 = **114%**
GRR = (4.000 - 400) / 4.000 = **90%**
Retención de logos = **90%**

¿Ves el truco? El 114% solo es posible porque los que se quedaron expandieron un +24% sobre la base inicial. Sin esa expansión brutal, tu retención de ingresos sería del 90%.

### Por qué no debes dejar de preocuparte por el churn

1. **La expansión no es infinita.** Una vez que un cliente llega al plan más alto, ya no puede compensar la pérdida del siguiente cliente que se va. El mes que viene, ese +24% probablemente no se repita y el NRR caerá por debajo del 100% de golpe.

2. **Estás en la cinta de correr.** Si pierdes el 10% mensual, para mantenerte en 40 clientes tienes que captar 4 nuevos cada mes solo para empatar. Captación es mucho más cara que retención.

3. **Concentración de riesgo.** Ese 114% probablemente depende de muy pocos clientes que subieron mucho de plan. Si uno de esos se va, el efecto es doble: pierdes churn + pierdes la expansión que te estaba salvando.

En SaaS, un NRR >100% es bueno *cuando va acompañado de una GRR alta* (p. ej. 95%+). Un NRR alto con una GRR baja es una señal de alerta, no de salud: es crecimiento por upselling sobre una base que se está desangrando.

No metas todo el esfuerzo en captar. Primero desglosa ese 114% en tu panel: ¿cuánto es expansión, cuánto es contracción y cuánto es churn de ingresos? Y mira la GRR y la retención de logos de esa misma cohorte.

Que el panel ponga un número verde no significa que el problema no exista. En tu caso, el problema es precisamente el churn.