# Claude Opus 5 Fast — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.12 | quality: 10.0
- latency_total: 11.906s | tokens_per_second: 172.0
- input_tokens: 216 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

## Respuesta corta: no, y de hecho el dato dice justo lo contrario de lo que estás leyendo.

Estás mezclando dos métricas distintas:

- **Retención de ingresos (NRR)**: cuánto dinero te sigue dando *la cohorte de clientes que ya tenías*, incluyendo subidas de plan. Puede superar el 100%.
- **Retención de clientes (logo retention)**: cuántos de esos clientes siguen contigo. **Nunca puede superar el 100%.**

Tus propios números: 40 → 36 clientes. Eso es **90% de retención de logos, 10% de churn mensual**. No está por encima del 100%; está bastante mal.

## Qué está pasando realmente

Con cifras redondas, para que se vea:

| | |
|---|---|
| 40 clientes × 100 € | 4.000 € |
| Se van 4 | −400 € |
| Base superviviente | 3.600 € |
| Expansión necesaria para llegar a 114% | **+960 €** |
| Total | 4.560 € |

Los que se quedaron tuvieron que subir su gasto **un 27%** para que tú vieras un +14%. Casi dos tercios de todo tu esfuerzo de expansión se fue en tapar el agujero. El 114% no es "no se va nadie": es "se va gente y unos pocos están pagando la factura".

## Por qué esto no es sostenible

1. **La expansión tiene techo, el churn no.** Un cliente puede subir de plan tres o cuatro veces; después se acaba. Irse solo se hace una vez, y es definitivo. Si repites este mes, ¿de dónde sale el siguiente 27%?
2. **Riesgo de concentración.** Si ese +960 € viene de dos o tres cuentas, tu NRR depende de que no se vayan. El día que una se marche, pasas de 114% a 80% sin cambiar nada más.
3. **Compuesto anual.** 10% mensual sostenido = 0,90^12 ≈ **28% de tus clientes vivos al cabo de un año**. Vida media ~10 meses. Eso pone un techo durísimo al LTV y, por tanto, a cuánto puedes gastar en captación.
4. **Captar sobre un cubo agujereado es caro.** Cada cliente nuevo tiene que amortizar su CAC en 10 meses antes de irse. Ese es el cálculo que deberías hacer antes de meter todo el presupuesto en adquisición.

## Tres cosas que comprobaría hoy

**1. Cómo define tu panel ese 114%.** Muchos dashboards etiquetan como "retención de ingresos" lo que en realidad es crecimiento neto de MRR *incluyendo clientes nuevos*. Si tus 36 clientes incluyen altas de este mes, perdiste más de 4 y el churn real es peor.

**2. Tu GRR (gross revenue retention).** Es el mismo cálculo pero **sin contar expansiones**: solo bajas y downgrades. Tope 100%. Es la métrica honesta de si el producto retiene. Si tu GRR está en 85-88%, tienes una fuga estructural que la expansión te está ocultando