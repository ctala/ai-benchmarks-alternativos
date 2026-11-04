# GLM 5.2 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 23.629s | tokens_per_second: 89.1
- input_tokens: 206 | output_tokens: 2106

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

No le des. Guarda esos $10.000 en el banco. Tu plan de crecimiento acaba de morir en la aritmética.

Vamos a diseccionar tus números, porque has cometido los tres pecados capitales del análisis de Unit Economics en SaaS:

**1. La ilusión de la retención (El error del Lifetime)**
Asumes que un cliente se queda 2 años (24 meses) porque "más o menos se queda". La matemática no se hace con intuiciones, se hace con la tasa de churn. 
Si tu churn mensual es del 8%, tu Lifetime real es **1 / 0.08 = 12.5 meses**. 
Acabas de perder más de la mitad del tiempo de vida que asumiste. No son 24 meses, son 12.5.

**2. Ingresos vs. Margen Bruto (El error del LTV)**
Calculaste el LTV sobre los ingresos brutos ($35 x 24 = $840). Pero la publicidad no se paga con ingresos brutos, se paga con margen bruto. Tú mismo dices que tu margen es del 70%. 
El valor real que genera un cliente para tu negocio cada mes no son $35, son **$24.50** ($35 x 0.70).

**3. El ratio real (El error del LTV/CAC)**
Vamos a hacer las cuentas como dios manda:
*   **Margen bruto mensual:** $24.50
*   **Lifetime esperado:** 12.5 meses
*   **LTV real:** $24.50 x 12.5 = **$306.25**

Tu LTV real no es $840. Es $306.25. 
Ahora dividamos eso entre tu CAC de $290:
**$306.25 / $290 = 1.05**

Tu ratio LTV/CAC es de **1.05**, no de 2.9 ni de 3. Por cada dólar que metes en Facebook/Google, te estás recuperando 1.05 dólares a lo largo del ciclo de vida de ese cliente. 

**El análisis del Payback Period (el clavo final en el ataúd)**
Veamos cuánto tardas en recuperar tu inversión en publicidad:
*   CAC: $290
*   Margen bruto mensual: $24.50
*   **Payback period:** $290 / $24.50 = **11.8 meses.**

Tardas casi 12 meses en recuperar lo que te costó traer a ese cliente. Y, según tu churn, el cliente promedio se va a los 12.5 meses. Básicamente, estás trabajando casi un año gratis por cada cliente para ganar $16.25 de margen bruto antes de que se vaya. Si el CAC sube un 5% o el churn sube un 1%, estás quemando dinero en cada adquisición.

**Veredicto:**
Si metes esos $10.000 hoy, vas a comprar clientes que te atarán capital durante un año para devolverte $10.500 en el mejor de los casos, asumiendo que tu CAC se mantiene estable (lo cual no ocurre cuando escalas). El costo de oportunidad y el riesgo de flujo de caja te ahogarán.

**Qué hacer antes de pensar en escalar:**
1.  **Baja el churn:** 8% mensual es altísimo para un producto de $35. Es un desangramiento. Necesitas bajarlo al 3-4%.
2.  **Mejora el CAC:** $290 para un ticket de $35/mes es carísimo. ¿Tienes funeles orgánicos, referidos, o SEO?
3.  **Sube el precio o el ARPU:** ¿Hay upsells? ¿Puedes cobrar anualmente con descuento para mejorar tu flujo de caja y reducir el churn?

Arregla el producto y la retención primero. Cuando tu LTV/CAC (calculado sobre margen) pase de 3 de verdad, vuelves y hablamos de los $10.000.