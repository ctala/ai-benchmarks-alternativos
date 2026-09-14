# Gemini 3.8 Flash — business_audit/retention_sobre_100_interpretacion

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 7.24 | quality: 8.0
- latency_total: 18.945s | tokens_per_second: 100.2
- input_tokens: 126 | output_tokens: 1899

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No, tu conclusión es incorrecta y asumir eso es uno de los errores más peligrosos en SaaS.**

Una métrica te está cegando sobre la otra. Estás confundiendo la **Retención Neta de Ingresos (NRR)** con la **Retención de Clientes (Logo Retention)**. 

Aquí está el desglose frío de lo que realmente está pasando en tu negocio:

---

### 1. La retención de clientes NUNCA puede superar el 100%
Físicamente es imposible retener más del 100% de tus clientes: o se quedan (100%) o se van (menos del 100%).

Tus datos reales de clientes este mes:
* Tenías 40 clientes.
* Ahora tienes 36.
* **Perdiste 4 clientes en un solo mes.**
* Tu retención de clientes es del **90%** (o lo que es lo mismo: un **Logo Churn mensual del 10%**).

Un churn mensual de clientes del 10% es una **emergencia crítica**. Si mantienes ese ritmo de fuga, a final de año habrás perdido a más del **70%** de los clientes que tienes hoy debido al efecto compuesto.

### 2. ¿Qué significa realmente ese 114% de NRR?
Significa que el dinero de los clientes que sobrevivieron creció lo suficiente mediante *upgrades* (expansión) como para tapar el agujero de los 4 clientes que cancelaron, y además sumar un 14% extra de facturación sobre la base original.

Fórmula aplicada: 
$$\text{NRR} = \frac{\text{MRR inicial} - \text{MRR perdido por bajas} + \text{MRR por expansión}}{\text{MRR inicial}} = 114\%$$

Es una métrica excelente de forma aislada (significa que tu producto aporta valor a quien se queda), pero **en tu caso está enmascarando un problema estructural de producto o fit de mercado.**

### 3. Los riesgos de ignorar esto y centrarte solo en captar

Si abres el grifo de la captación ahora mismo, te vas a estrellar por tres motivos:

1. **El cubo agujereado:** Meter más clientes en un sistema que pierde el 10% mensual destruirá tu economía unitaria. Quemarás caja en marketing/ventas (CAC) para clientes que se van antes de amortizar su adquisición.
2. **Riesgo extremo de concentración:** Al perder volumen de clientes pero aumentar ingresos con unos pocos, te estás volviendo rehén de un puñado de cuentas grandes. Si el mes que viene se te va *uno* de los que subió de plan, tu NRR se desplomará y el golpe a la facturación será devastador.
3. **Límite de expansión:** La base que subió de plan este mes no va a seguir subiendo de plan todos los meses hasta el infinito. La expansión tiene techo; el churn, si no se frena, se lo come todo.

### Conclusión y plan de acción

**No dejes de preocuparte por el churn.** De hecho, debería ser tu prioridad número uno esta semana:

* Llama a los 4 clientes que cancelaron y averigua exactamente por qué se fueron (¿precio, falta de uso, onboarding deficiente, prometiste algo que el software no hace?).
* Analiza a los que subieron de plan: ¿qué tienen en común? Ese es tu *Ideal Customer Profile* (ICP). 
* Si vas a captar clientes nuevos, asegúrate de que sean clones de los que subieron de plan, no de los 4 que cancelaron.