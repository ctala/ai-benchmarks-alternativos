# Gemini 3.5 Flash Lite — business_audit/retention_sobre_100_interpretacion

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.12 | quality: 10.0
- latency_total: 4.399s | tokens_per_second: 170.9
- input_tokens: 126 | output_tokens: 752

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

Hola. Como analista de SaaS, tengo una mala y una buena noticia para ti. Empecemos por la que no te va a gustar: **estás interpretando mal la métrica y tu conclusión sobre el *churn* es peligrosamente incorrecta.** No, no puedes dejar de preocuparte por el *churn*.

Desglosemos exactamente qué está pasando en tu negocio con los datos que me das:

### 1. La ilusión óptica del 114% de NRR (Net Revenue Retention)
Ese 114% significa que, de los ingresos que tenías el mes pasado, hoy conservas un 14% más, **gracias a que los clientes que se quedaron te pagaron más dinero** (lo que llamamos *Expansion MRR*). 

Matemáticamente es posible tener una Retención Neta de Ingresos superior al 100% mientras el negocio se encoge en número de clientes. Tus pocos clientes restantes compensaron con creces (en dinero) a los que se fueron. 

### 2. La realidad operativa: estás perdiendo un 10% de tu cartera
Me dices que pasaste de **40 a 36 clientes de pago**. 
Eso significa que **perdiste 4 clientes en un solo mes**. En términos de clientes (lo que llamamos *Logo Churn*), tu tasa de cancelación mensual es del **10%** (4 de 40). 

Para ponerlo en perspectiva en el mundo SaaS: un *churn* de clientes del 10% mensual es una hemorragia severa. Significa que estás reemplazando toda tu base de clientes cada 10 meses. Tu negocio actual es una cubeta con agujeros muy grandes; la única razón por la que no se vacía del todo es porque estás echando agua con una manguera de alta presión (las subidas de plan).

### 3. ¿Por qué deberías preocuparte (y mucho)?
Apuntar todos tus esfuerzos a captar gente nueva con un *churn* de clientes del 10% es como intentar llenar una piscina sin tapar el desagüe. Te saldrá carísimo en costos de adquisición (CAC) y eventualmente te quedarás sin suficiente base para hacer *upselling*.

Además, hay un riesgo de concentración: si dependes de que 36 clientes (o menos) suban de plan constantemente para mantener los ingresos a flote, estás a merced de que uno o dos de esos "ballenas" decidan irse el mes próximo. Si eso pasa, ese 114% se desplomará de golpe.

### El veredicto del analista:
*   **¿Se te va poca gente?** Falso. Se te está yendo el 10% de tus clientes cada mes.
*   **¿La retención de clientes está por encima del 100%?** Confundes ingresos con clientes. Tu NRR es del 114%, pero tu retención de clientes (*Logo Retention*) es del 90%.
*   **¿Puedes dejar de preocuparte por el churn?** Ni se te ocurra. 

**Mi recomendación:** Antes de gastar un dólar más en captación, dedica las próximas semanas a averiguar **por qué** se te fue ese 10% de clientes el mes pasado. Si detienes esa fuga y mantienes las ganas de tus clientes actuales de subir de plan, ese 114% se disparará y entonces sí tendrás un SaaS saludable.