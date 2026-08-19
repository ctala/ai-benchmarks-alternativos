# Claude Sonnet 5 (suscripción) — business_audit/retention_sobre_100_interpretacion

- model_id: `claude-sonnet-5`
- success: True  | final: 8.19 | quality: 10.0
- latency_total: 50.817s | tokens_per_second: 64.4
- input_tokens: 2 | output_tokens: 3271

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No. Tu lectura tiene dos errores, y el segundo es el que te puede costar caro.

## Qué mide realmente el 114%

NRR (Net Revenue Retention) es un cálculo de **ingresos**, no de **clientes**, y solo mira la cohorte que ya existía al inicio del período — nunca incluye clientes nuevos.

```
NRR = (MRR inicial + expansión − contracción − MRR de churn) / MRR inicial
```

114% significa: de cada $100 que facturabas al inicio del mes con tus clientes existentes, terminaste el mes con $114 de esa misma cohorte, contando ya la pérdida de los que se fueron. La expansión (los que subieron de plan) no solo compensó lo perdido, lo superó.

No dice nada sobre cuántos clientes se quedaron. Puedes perder la mitad de tu base y tener NRR sobre 100% si los que quedan gastan mucho más.

## Aplicando tus números

40 → 36 clientes de pago = **perdiste el 10% de tu base de clientes en un mes** (logo churn = 10%).

Eso no es ruido. Si esa tasa se sostiene, tu retención de clientes a 12 meses es 0.9^12 ≈ 28%. Es decir, de cada 100 clientes que tienes hoy, en un año te quedarían ~28 si nada cambia — el resto lo reemplazarías con adquisición nueva, a costo creciente.

El 114% en tu panel es compatible, matemáticamente, con esa fuga. Los "varios que subieron de plan" están **tapando** la salida de los otros 4, no anulándola.

## El riesgo que el número esconde

Hay algo más incómodo: los clientes que quedaron y subieron de plan probablemente no son una muestra aleatoria — son los de mayor intención de compra o mayor dependencia del producto. Eso concentra tu ingreso en menos cuentas. Si el mes que viene se te va uno de esos que expandieron, el NRR puede caer de 114% a bajo 100% de un mes a otro, porque tu colchón son pocas cuentas grandes, no una base ancha.

## Qué hacer

No puedes moverte a "solo captar" con este dato. Al revés:

1. **Investiga a los 4 que se fueron** — mismo plan, mismo perfil, mismo motivo. Si son un patrón (mismo onboarding fallido, mismo caso de uso, mismo momento de churn en su ciclo de vida), tienes un problema de producto o de fit, no de suerte.
2. **Reporta ambas métricas juntas siempre**: NRR *y* logo retention (o su inverso, logo churn). Un dashboard que solo muestra NRR es un dashboard que oculta la fuga de clientes por diseño.
3. **No metas presupuesto de adquisición sin resolver la fuga**. Adquirir para reemplazar el 10% mensual es cargar agua en un balde con hoyo — funciona hasta que el balde no da abasto o el CAC sube porque ya agotaste el canal barato.

En una palabra: el 114% te dice que el motor de expansión de tus mejores clientes está sano. No te dice nada bueno sobre retención de clientes — y con un 10% mensual de logo churn, ahí sí deberías estar preocupado.