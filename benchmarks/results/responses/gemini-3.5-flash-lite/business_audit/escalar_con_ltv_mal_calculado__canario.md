# Gemini 3.5 Flash Lite — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 9.09 | quality: 10.0
- latency_total: 4.438s | tokens_per_second: 201.9
- input_tokens: 194 | output_tokens: 896

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

Alto ahí. Baja el dedo del botón de los $10,000. 

Tu plan no está muriendo en la aritmética; **ya está muerto**. Te estás metiendo una falacia mental clásica de fundador optimista. Vamos a desarmar tus números con la frialdad que requiere tu dinero.

### El error 1: El LTV de fantasía (El cementerio del 8% de Churn)
Crees que tus clientes se quedan "unos 2 años" (24 meses). La matemática dice otra cosa muy distinta. 

Con un churn mensual del **8%**, la retención real no es lineal. Usa la fórmula correcta para calcular la vida promedio del cliente ($1 / \text{Churn}$):

*   $1 / 0.08 = \mathbf{12.5\text{ meses}}$ (poco más de 1 año, no 2).

Ahora calculemos el **LTV real** usando tu margen bruto (70%):
*   Ingreso mensual por usuario: $35
*   Margen bruto mensual: $35 \times 0.70 = \mathbf{\$24.50}$ por mes.
*   LTV Real = $24.50 \times 12.5\text{ meses} = \mathbf{\$306.25}$.

*Tu LTV real no es $840. Es $306.25.*

### El error 2: El ratio LTV/CAC
Si recalculamos con tu CAC de $290:
*   $\text{LTV / CAC} = \$306.25 / \$290 = \mathbf{1.05}$.

Un ratio de 1.05 significa que **apenas recuperas lo que gastas** en adquirir al cliente, sin contar tus costos fijos, sueldos, marketing general, impuestos ni el costo de operación. Estás cambiando dólares por dólares, pero con estrés operativo.

### El error 3: El ciclo de caja (La trampa de mortalidad)
Incluso si el LTV fuera de $306 y el CAC de $290 (un margen finísimo), mira cómo recuperas esos $290:
*   El cliente te paga $35 al mes ($24.50 de margen bruto).
*   Para recuperar los $290 de CAC, necesitas que ese cliente se quede **12 meses exactos** solo para *empatar* la inversión publicitaria. 
*   Pero con un churn del 8%, una parte masiva de esos clientes se te va a ir en el mes 2, 4 o 6. **Perderás dinero en cada cliente que no llegue al año.**

Si metes $10,000 hoy en pauta con estos números, vas a quemar caja a una velocidad ridícula y tu "rentabilidad actual" va a desaparecer en semanas porque el flujo de caja no va a aguantar el desfase entre pagar el CAC hoy y cobrarlo en cuotas chiquitas durante 12 meses.

### Mi veredicto como analista:
**NO LE DIES.**

Si escalas hoy con un CAC de $290 y un churn de 8%, vas a acelerar tu propia quiebra. 

### ¿Qué tendrías que arreglar antes de gastar un solo dólar?
1.  **Bajar el Churn:** Si reduces ese 8% mensual a un 3% o 4%, tu vida promedio se duplica y el LTV despega.
2.  **Bajar el CAC:** Necesitas optimizar canales para que esos $290 bajen drásticamente (al menos a menos de $100 con estos precios).
3.  **Subir el precio:** A $35/mes, adquirir clientes vía publicidad pagada es un deporte extremo casi imposible de ganar, a menos que tengas retención casi perfecta (SaaS enterprise). 

Guarda esos $10,000 en el banco. Arregla la cubeta antes de seguir abriéndole la llave al agua.