# MiMo V2.6 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 92.038s | tokens_per_second: 23.4
- input_tokens: 149 | output_tokens: 2150

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

## Respuesta corta

**A medias.** El 114% es un buen número, pero la lectura que haces de él es incorrecta en dos puntos importantes: no mide clientes que se quedan, y no te libra del churn.

## Qué mide el 114%

Tu panel muestra **Net Revenue Retention (NRR)**: cuánto ingreso generan *los mismos clientes de mes a mes*, incluyendo subidas de plan (+), bajadas de plan (−) y churn (−), pero **excluyendo clientes nuevos**.

| Métrica | Qué responde | Tu caso |
|---|---|---|
| **NRR: 114%** | ¿Los clientes viejos pagan más que hace un mes? | Sí, +14% neto |
| **Retención de clientes (logo)** | ¿Cuántos clientes siguen? | 36/40 = **90%**, o peor si hay clientes nuevos entre esos 36 |
| **GRR** (no lo tienes) | ¿Cuántos ingresos quedan *sin contar* expansiones? | Falta calcularlo |

**"Retención de clientes por encima del 100%" no existe como concepto**: un cliente no se queda 1,5 veces. El >100% solo aplica a ingresos, y solo porque las subidas de plan de los que se quedaron compensaron lo que se fueron.

## La aritmética de tu caso

Perdiste **4 de 40 clientes (10% de churn)**. Eso es real y ya ocurrió. El 114% dice que las subidas de plan de los supervivientes aportaron más ingresos de los que esos 4 clientes se llevaron.

Eso es **buena señal de expansión**, no señal de ausencia de churn.

## Por qué no puedes dejar de preocuparte

1. **El churn está enmascarado, no eliminado.** Si las subidas de plan se detienen (son eventos puntuales, no recurrentes), el 114% se desploma de golpe y aparece el churn que siempre estuvo ahí. Pasa de 114% a 90% en un mes sin que nada empeore en retención.

2. **El churn es permanente; la expansión no.** Un cliente perdido se lleva su ingreso para siempre. Una subida de plan puede revertirse.

3. **40 clientes es una muestra diminuta.** Un solo cliente que se va = 2,5% de tu base. El 114% probablemente lo provocaron 2 o 3 upgrades. Es una métrica volátil, no una tendencia establecida.

4. **El churn temprano se paga dos veces**: además de perder el ingreso, ya gastaste en captarlo. Que hoy la expansión lo cubra no cancela ese costo.

## Qué hacer en su lugar

- **Calcula tu GRR**: ingresos de tus clientes del mes pasado, excluyendo clientes nuevos, sin sumar upgrades. Es el "suelo" real de tu retención. Si el GRR es 90%, ese es tu churn de ingresos puro.
- **Mantén el logo retention en el panel** junto al NRR, para que la expansión no tape la fuga.
- **No redirijas todo el esfuerzo a captación.** Con 10% de churn mensual, cada mes sales a buscar más de lo que ya perdiste. Bajar churn suele ser más barato que reemplazarlo.

**Lo correcto con tu dato**: celebrar el 114% como señal de que tus clientes que se quedan ven más valor (buen indicador de producto/precio), y seguir atacando el churn de fondo —porque hoy la expansión lo oculta, no lo resuelve.