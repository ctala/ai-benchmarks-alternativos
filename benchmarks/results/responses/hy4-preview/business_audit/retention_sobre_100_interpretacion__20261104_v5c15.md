# Tencent Hy4 preview — business_audit/retention_sobre_100_interpretacion

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 41.772s | tokens_per_second: 54.2
- input_tokens: 155 | output_tokens: 2263

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

Me temo que no. Como analista, tengo que ser directo contigo: estás mezclando dos métricas completamente distintas y tu conclusión es peligrosa para la salud del negocio a largo plazo.

Vamos a desglosar la realidad de los números que acabas de darme:

**1. Tu Retención de Clientes (o *Logo Retention*) y tu Churn:**
* **Mes pasado:** 40 clientes.
* **Este mes:** 36 clientes.
* **Realidad:** Has perdido 4 clientes. Tu retención de clientes es del **90%**. Por lo tanto, tu tasa de fuga de clientes (*Customer Churn*) es del **10%**. 

Perder al 10% de tus clientes cada mes es muchísimo. Si mantienes ese ritmo, en un año habrás perdido cerca del 70% de tu base de clientes original. Decir que "prácticamente no se va nadie" es la lectura incorrecta. Además, matemáticamente, la retención de clientes **nunca** puede ser superior al 100%.

**2. Lo que significa realmente ese 114% (Net Revenue Retention - NRR):**
* El 114% mide cuánto han crecido los ingresos *dentro* de tu base de clientes existente. 
* **Realidad:** Los 36 clientes que se quedaron (gracias a las subidas de plan que mencionas) están pagando hoy un 14% más de lo que pagaban el mes pasado. Esto es una excelente noticia: significa que tu producto aporta valor y hay *expansión*. Sin embargo, este dato enmascara la fuga de clientes que estás teniendo en la base de tu pirámide.

**¿Puedes dejar de preocuparte por el churn y meter todo en captación?**

No. Definitivamente no. En la industria del SaaS, lo que tienes ahora mismo se conoce como un **"cubo con fugas" (leaky bucket)**. 

Tus clientes que suben de plan están compensando con creces (en euros/dólares) a los que se van, lo cual mantiene tus ingresos creciendo. Pero estás perdiendo volumen de usuarios mes a mes.

**El riesgo de tu estrategia actual:**
Si pones todo tu esfuerzo y presupuesto en captar nuevos clientes para compensar la pérdida de esos 4:
1. Tu Coste de Adquisición (CAC) será altísimo, ya que tendrás que comprar clientes constantemente solo para estar donde estabas el mes pasado.
2. Estás perdiendo el valor a largo plazo (LTV) y el potencial de recomendación (boca a boca) de esos clientes que se fugan.
3. Si en algún momento se frena la captación o se agota el mercado, el negocio se desangrará por ese 10% de churn.

**Conclusión:**
Tienes un motor de *expansión* de ingresos fantástico (114% NRR), pero un motor de *retención* de clientes con problemas (10% de churn). 

No dejes de captar, pero **no ignores el churn**. Si averiguas por qué se están yendo esos 4 clientes y logras retenerlos, la combinación de una alta retención de clientes con tu actual capacidad de subirles el precio hará que tu crecimiento sea exponencial y altamente rentable.