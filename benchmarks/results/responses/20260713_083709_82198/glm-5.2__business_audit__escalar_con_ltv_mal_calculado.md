# GLM 5.2 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `z-ai/glm-5.2`
- success: True  | final: 7.23 | quality: 8.14
- latency_total: 31.534s | tokens_per_second: 59.2
- input_tokens: 206 | output_tokens: 1868

## Respuesta completa

No le doy luz verde. Detén el plan. Tu modelo no sobrevive el escrutinio de la aritmética. 

Tienes dos errores fundamentales en tu cálculo que hacen que un negocio que parece rentable sea en realidad un sumidero de efectivo si lo escalas con publicidad pagada.

Aquí están tus números reales:

**1. Tu error con el Churn (La vida útil del cliente)**
Asumiste que un cliente se queda 2 años (24 meses) porque "es lo que parece". Pero tienes un churn mensual del 8%. La matemática real de la vida útil es 1 / Churn mensual.
- Vida útil real = 1 / 0.08 = **12.5 meses** (no 24).

**2. Tu error con el Margen Bruto (LTV sobre Ingresos vs. Utilidad)**
Calculaste el LTV sobre los ingresos brutos ($35), ignorando tu propio margen bruto del 70%. El LTV debe calcularse sobre la utilidad bruta, no sobre el precio de la suscripción, porque de esos $35 ya se te van $10.50 en infraestructura y pasarela de pagos. 
- Utilidad bruta mensual = $35 × 70% = **$24.50/mes**

**Tus números reales de Unit Economics:**
- **LTV real** = $24.50 (utilidad mensual) × 12.5 (meses de vida) = **$306.25**
- **CAC** = **$290**
- **Ratio LTV:CAC real** = 306.25 / 290 = **1.05x** (No es 2.9x. Está muy lejos del mínimo saludable de 3x).

**El problema del Payback Period (Recuperación de la inversión)**
Para recuperar tus $290 de CAC, a $24.50 de margen al mes, te toma **11.8 meses** recuperar a ese cliente. 
Como tu cliente se va a los 12.5 meses, apenas vas a recuperar tu inversión de publicidad un mes antes de que el cliente haga churn. Cualquier mínima variación (que el CAC suba a $300 o que el churn suba a 9%) te hace perder dinero en cada adquisición.

**¿Qué pasa si metes los $10,000 en publicidad hoy?**
A $290 de CAC, comprarás unos 34 clientes. Esos 34 clientes te generarán, a lo largo de toda su vida (un año), unos $10,615 de utilidad bruta. Es decir, inmovilizas $10,000 hoy para ganar $615 en un año. El costo de oportunidad y el riesgo de flujo de caja es altísimo.

**Veredicto:**
No metas los $10,000 todavía. Eres rentable orgánicamente, lo cual es genial, pero la publicidad pagada te va a asfixiar el flujo de caja. Antes de escalar con ads, necesitas lograr una de estas dos cosas (o ambas):

1. **Bajar el CAC pagado:** Necesitas que esté por debajo de $100 para que el negocio respire y el payback period baje a 4 meses.
2. **Reducir el Churn drásticamente:** Un churn del 8% mensual es crítico para un SaaS de $35/mes. Si bajas el churn al 4%, tu vida útil sube a 25 meses, tu LTV sube a $612, y ahí sí tendrías un ratio LTV:CAC de 2.1x (aún no óptimo, pero ya jugable).

Arregla la retención o el costo de los ads. La aritmética no perdona.