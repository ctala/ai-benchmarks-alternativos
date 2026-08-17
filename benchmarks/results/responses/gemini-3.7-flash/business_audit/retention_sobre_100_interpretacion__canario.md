# Gemini 3.7 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 7.22 | quality: 8.0
- latency_total: 21.563s | tokens_per_second: 90.9
- input_tokens: 126 | output_tokens: 1960

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No, tu interpretación es incorrecta y asumir eso es uno de los errores más peligrosos en SaaS.** 

Tienes un problema grave de churn de clientes que tus métricas de ingresos están **enmascarando**.

Aquí tienes el desglose analítico de lo que realmente está pasando en tu negocio:

---

### 1. Estás confundiendo dos métricas distintas

* **Retención Neta de Ingresos (NRR = 114%):** Mide el dinero. Significa que, de la cohorte que tenías el mes pasado, hoy estás generando un 14% más de ingresos a pesar de las bajas, gracias a los *upgrades* (expansión).
* **Retención de Clientes (*Logo Retention* = 90%):** Mide cuentas/logos. Empezaste con 40 y perdiste 4. **Tu retención de clientes jamás puede superar el 100%**. 

Tu retención de clientes este mes fue del **90%**, lo que equivale a un **10% de Logo Churn mensual**.

---

### 2. La gravedad de un 10% de Logo Churn mensual

Perder 4 de 40 clientes en un solo mes es una señal de alarma crítica:

* Un 10% de churn mensual compuesto significa que **en un año habrás perdido aproximadamente el 71% de tu base de clientes actual**.
* Tus ingresos subieron porque los clientes que se quedaron aumentaron su gasto más rápido de lo que restaron los que se fueron. 

La expansión de unos pocos te está salvando la foto financiera del mes, pero el modelo tiene una fuga estructural.

---

### 3. Por qué NO debes ignorar el churn para centrarte solo en captar

Si metes todo el esfuerzo en captación ahora mismo, estarás **echando agua en un cubo agujereado**:

1. **Riesgo de concentración:** Tu negocio depende cada vez de menos clientes que pagan más. Si el mes que viene se te va uno de los clientes que subió de plan, tu NRR se desplomará en picado.
2. **La expansión tiene un techo:** Tus clientes actuales no van a duplicar su plan todos los meses de forma infinita. Cuando se estabilicen, el 10% de churn mensual destruirá tus ingresos.
3. **CAC desperdiciado:** Si captas 10 clientes nuevos el próximo mes pero sigues perdiendo el 10%, estarás quemando dinero en adquisición (CAC) para quedarte prácticamente en el mismo sitio.

---

### 4. Qué deberías hacer ahora

En lugar de volcarte a ciegas en captación:

1. **Entrevista a los 4 que se fueron:** Necesitas saber con urgencia por qué cancelaron (¿mala incorporación/onboarding, producto incompleto, precio, no vieron valor?).
2. **Identifica tu ICP (*Ideal Customer Profile*):** Analiza qué diferencia a los que subieron de plan de los 4 que se fueron. Es muy probable que estés vendiendo a dos tipos de clientes distintos: uno para el que tu producto es imprescindible (los que expanden) y otro al que no le sirve (los que se van).
3. **Optimiza antes de escalar:** Ajusta tu captación para traer *únicamente* al perfil de cliente que se expande y retén el esfuerzo de gasto masivo en marketing hasta que tu churn mensual de logos baje a niveles sostenibles (idealmente <1-2% mensual en B2B).