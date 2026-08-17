# Claude Sonnet 5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 7.0 | quality: 8.0
- latency_total: 15.679s | tokens_per_second: 68.5
- input_tokens: 216 | output_tokens: 1074

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, esa interpretación es incorrecta y puede llevarte a decisiones peligrosas.

## Qué mide realmente el 114%

Ese número es **Net Revenue Retention (NRR)**, y mide *dinero*, no *clientes*. La fórmula típica:

$$NRR = \frac{\text{Ingresos de la cohorte inicial este mes (con upgrades, downgrades y cancelaciones)}}{\text{Ingresos de esa misma cohorte el mes pasado}}$$

Un 114% significa que **los clientes que se quedaron gastan, en conjunto, un 14% más que antes**. Nada más. No dice nada directo sobre cuántos clientes conservaste.

## Tu caso concreto

- Mes pasado: 40 clientes de pago
- Este mes: 36 clientes
- **Perdiste 4 clientes, un 10% de churn logo (customer churn)**

Lo que pasó es que los que se quedaron subieron de plan lo suficiente para que el ingreso total no solo compensara la pérdida de esos 4 clientes, sino que creciera un 14% neto. Es decir, tu **expansion revenue** está tapando tu **customer churn**.

## Por qué esto importa (y no es solo semántica)

1. **Son dos problemas distintos con causas distintas.** Perder 1 de cada 10 clientes cada mes es una tasa altísima (proyectado a churn anualizado, es brutal). El NRR alto no arregla eso, solo lo disfraza en el P&L de corto plazo.

2. **El NRR bueno no es sostenible si sigue erosionándose la base.** Si cada mes pierdes 10% de logos y dependes de que los que quedan paguen más, en algún momento se te acaba la gente que pueda o quiera pagar más. Es una base cada vez más pequeña y concentrada = más riesgo.

3. **Un cliente que se va no puede expandirse nunca.** Estás optimizando el LTV de los que quedan mientras el "grifo" de arriba (adquisición) tiene que trabajar cada vez más duro solo para mantener el número de clientes plano.

4. **Preguntas que deberías hacerte ya:** ¿por qué se fueron esos 4? ¿Es un segmento específico (plan bajo, cierto tipo de uso, cierta antigüedad)? Si es un patrón, ese churn se va a comer también a los que hoy están expandiéndose.

## Conclusión

No puedes "dejar de preocuparte por el churn" — de hecho es lo primero que deberías investigar. Tu situación real es: **buen upsell/expansion, mal churn de logos**. Meter todo el esfuerzo en adquisición sin arreglar la fuga de clientes es llenar una cubeta con un agujero cada vez más grande, usando NRR como métrica que hace ver la cubeta llena.

Mira en paralelo: **Gross Revenue Retention (GRR)** — el mismo cálculo pero sin contar expansión (topando en 100%). Ese número te va a mostrar el daño real del churn sin que la expansión lo maquille.