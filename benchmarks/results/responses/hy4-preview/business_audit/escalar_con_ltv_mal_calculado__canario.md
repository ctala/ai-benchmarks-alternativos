# Tencent Hy4 preview — business_audit/escalar_con_ltv_mal_calculado

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 62.739s | tokens_per_second: 58.2
- input_tokens: 228 | output_tokens: 3651

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

**Veredicto: No. Frena el motor. No gastes esos $10.000.**

Como analista de unit economics, veo dos errores de bulto en tu aritmética que, como bien dices, matan este plan de crecimiento antes de empezar. Vamos a recalcular.

**Error 1: El tiempo de vida del cliente (Lifetime)**
Dices que un cliente se queda unos 2 años (24 meses). Matemáticamente, eso es incorrecto. Si pierdes el 8% de tus clientes *cada mes*, la vida media de un cliente es de **12,5 meses** (1 dividido por 0,08), no 24. Si fueran 24 meses, tu churn mensual tendría que ser del 4%.

**Error 2: Usaste Ingresos en lugar de Margen Bruto**
El LTV (Lifetime Value) nunca se calcula sobre el precio de venta (Revenue), sino sobre el margen bruto (Gross Profit). Tú no te quedas con $35 al mes, te quedas con el 70%. Es decir, **$24,50 al mes** de ganancia bruta por cliente.

**Los números reales:**
Vamos a hacer la matemática correcta para un negocio de suscripción:

*   **Margen Bruto Mensual:** $35 * 70% = $24,50
*   **Vida media del cliente:** 1 / 0,08 = 12,5 meses
*   **LTV Real:** $24,50 * 12,5 meses = **$306,25**

**Ahora veamos tu ratio LTV/CAC:**
*   **LTV:** $306,25
*   **CAC:** $290
*   **Ratio Real:** **1,05** (¡Muy, muy lejos del 3,0 que buscabas!)

**La estocada final: El Payback Period (Recuperación del CAC)**
Lo más grave de este plan es el tiempo que tardas en recuperar lo que inviertes para adquirir un cliente:
*   $290 (CAC) / $24,50 (Margen mensual) = **11,8 meses**.

**¿Te das cuenta del problema?**
Tardas **11,8 meses** en recuperar la inversión de traer a un cliente. Pero ese cliente, de media, se te va a los **12,5 meses**. 
Prácticamente, el cliente se va justo cuando empiezas a ganar dinero con él. Estás trabajando gratis para la plataforma de publicidad (Meta, Google, TikTok) y asumiendo todo el riesgo del flujo de caja.

**Qué pasaría si metes los $10.000 hoy:**
Con $10.000 a un CAC de $290, traerías 34 clientes nuevos. 
La ganancia bruta total que te dejarían esos 34 clientes durante *toda* su vida (12,5 meses) sería de apenas **$412 dólares** ($10.412 de LTV total - $10.000 de inversión). Eso sin contar tus costos fijos (sueldos, herramientas, etc.). 

**Qué necesitas hacer antes de escalar:**
No enciendas la manguera de la publicidad todavía. Tienes que arreglar la fontanería:
1.  **Bajar el Churn:** Si logras bajar el churn del 8% al 4%, duplicas el LTV a $612,5 y tu ratio LTV/CAC sube a 2,1.
2.  **Subir el Precio / Cobrar Anualidades:** Un precio más alto o cobrar por adelantado el año inyecta caja inmediata y mejora dramáticamente tu payback.
3.  **Bajar el CAC:** Necesitas optimizar tus campañas o encontrar un canal donde el CAC esté por debajo de los $100. 

Regla de oro: Si tu LTV/CAC no es mayor a 3, y tu CAC Payback no es menor a 12 meses (idealmente 6), estás comprando clientes a pérdida. Escalar eso solo hará que pierdas dinero más rápido.