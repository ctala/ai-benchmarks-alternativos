# DeepSeek V4.1 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 25.368s | tokens_per_second: 139.7
- input_tokens: 165 | output_tokens: 3544

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Esa lectura no es correcta. “Retención de ingresos: 114%” es **NRR / Net Revenue Retention**, no retención de clientes. Significa que los ingresos recurrentes del grupo de clientes que ya tenías crecieron un 14% neto, gracias a subidas de plan, upsells o cross-sells, **después de restar bajas y downgrades**. Puede pasar del 100% aunque estés perdiendo clientes.

Con tus datos:

- Mes pasado: 40 clientes de pago.
- Este mes: 36 clientes de pago.
- Varios subieron de plan.

Si no hubo clientes nuevos, tu retención de clientes es:

**36 / 40 = 90%**

Y tu churn de clientes es:

**10%**

Si además hubo clientes nuevos, el churn de la base original es peor: perdiste más de 4 clientes y algunos nuevos taparon parcialmente la caída.

La diferencia clave:

- **Retención de ingresos / NRR:** puede ser >100%.  
  Fórmula aproximada:  
  `(MRR inicial + expansión - contracción - churn) / MRR inicial`

- **Retención de clientes / logo retention:** normalmente no puede superar el 100%.  
  `clientes retenidos / clientes iniciales`

Así que puedes tener **NRR 114%** y a la vez **churn de clientes 10%**. Lo que ocurre es que las subidas de plan están compensando en ingresos la pérdida de clientes. Pero has perdido 4 logos. Si ese 10% fuese mensual y se repitiese, anualizarías un churn de logos cercano al 72%: `1 - 0,9^12`. Eso no es “prácticamente no se me va nadie”.

¿Puedes dejar de preocuparte por el churn y meter todo a captación? **No.** Puedes aumentar captación si tu NRR es alto y tu economía unitaria aguanta, pero no deberías abandonar retención. Un NRR alto puede ser frágil si viene de pocos clientes que subieron de plan. Revisa también:

- **GRR** o retención bruta de ingresos: ingresos retenidos sin contar expansión. Si es baja, la expansión está tapando fuga.
- **Churn de logos** y motivos de baja.
- **Churn por segmento**: no es lo mismo perder clientes pequeños que grandes.
- **Concentración de la expansión**: si 2 clientes explican el +14%, tienes riesgo.
- **Sostenibilidad de los upgrades**: ¿son recurrentes o puntuales?

Resumen: el panel dice que **tus ingresos de clientes existentes aguantan o crecen**, no que **tus clientes se queden**. Has perdido un 10% de clientes en el mes. Puedes priorizar más captación, pero no dejar de gestionar churn.