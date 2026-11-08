# GLM 5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `z-ai/glm-5`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 40.828s | tokens_per_second: 58.7
- input_tokens: 206 | output_tokens: 2396

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

No le des. Detén la transferencia. Tu plan acaba de morir en la aritmética.

Has cometido dos errores clásicos de fundador: has calculado el LTV sobre ingresos brutos ignorando tu margen, y has inventado un "lifetime" de 2 años que contradice tu propio churn.

Vamos a hacer la autopsia de tus números reales:

**1. El Lifetime real**
Dices que un cliente se queda 2 años (24 meses). Pero tu churn mensual es del 8%. La fórmula del lifetime es 1 / Churn.
1 / 0.08 = **12.5 meses**.
Tus clientes no se quedan 24 meses, se van a los 12.5. Estás sobreestimando la retención por un 92%.

**2. El LTV real (sobre margen, no sobre ingresos)**
El LTV no se calcula sobre el precio de venta, se calcula sobre el margen bruto, porque es el dinero que realmente te queda para pagar el CAC y los gastos operativos.
- Ingreso mensual: $35
- Margen bruto (70%): $24.50
- LTV = $24.50 × 12.5 meses = **$306.25**

**3. La ratio real LTV/CAC**
- LTV real: $306.25
- CAC: $290
- Ratio: $306.25 / $290 = **1.05**

No tienes un ratio de 2.9. Tienes un ratio de 1.05. Por cada dólar que metes en Facebook/Google Ads, recuperas $1.05 de margen bruto. Te quedan 5 centavos para pagar tu sueldo, el alquiler, el equipo, los impuestos y el software. Esto es una quema de dinero disfrazada de crecimiento.

**4. El verdadero asesino: el Payback Period**
Incluso si ignoráramos la ratio, miremos cuánto tardas en recuperar tu inversión en publicidad.
- CAC: $290
- Margen bruto mensual: $24.50
- Payback period = 290 / 24.50 = **11.8 meses.**

Tardas casi un año en recuperar el dinero de adquirir a un cliente. Y como tu cliente promedio se va a los 12.5 meses, estás prestando dinero a la plataforma de publicidad durante 11 meses sin intereses para, literalmente, ganar 15 días de margen bruto antes de que se vaya. Tu flujo de caja se va a asfixiar inmediatamente. 

**Veredicto:**
No metas los $10,000. Si los metes hoy, dentro de 30 días tendrás $10,000 menos en el banco, una factura de infraestructura más alta por los nuevos usuarios, y no habrás recuperado ni el 20% de lo invertido.

**Qué hacer antes de escalar:**
Tienes dos palancas que mover antes de volver a hablar de publicidad pagada:
1. **Reducir el Churn:** Si bajas el churn del 8% al 4% mensual, tu lifetime pasa a 25 meses. Tu LTV sube a $612. Con tu CAC actual de $290, tu ratio sube a 2.1 y tu payback baja a 11 meses. Sigue siendo ajustado, pero ya es un negocio.
2. **Subir el ARPU o bajar el CAC:** Con un margen de $24.50 al mes, un CAC de $290 es insostenible. Necesitas que el CAC baje a $80 (ratio de 3.8), o subir tu precio a $100/mes (lo que daría $70 de margen, manteniendo el CAC en $290 daría una ratio de 3).

Arregla la retención o el precio. Cuando tu ratio pase de 3 y tu payback period baje a menos de 6 meses, me llamas y autorizamos los $10,000.