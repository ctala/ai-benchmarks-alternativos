# Grok 4.7 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.36 | quality: 10.0
- latency_total: 36.522s | tokens_per_second: 51.6
- input_tokens: 1430 | output_tokens: 1885

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

No. Con esos números la publicidad no escala un negocio rentable: escala un cliente que apenas se paga a sí mismo.

El error está en el lifetime y en usar ingreso bruto en vez de margen.

**Vida esperada.** Con churn mensual del 8%, la permanencia no es 24 meses. Es \(1 / 0{,}08 = 12{,}5\) meses. Churn anual implícito: \(1 - 0{,}92^{12} \approx 63\%\).

**LTV de contribución.** Lo que importa es el margen, no los $35:
- Margen mensual: \(35 \times 0{,}70 = \$24{,}50\)
- LTV: \(24{,}50 / 0{,}08 = \$306\)
- LTV/CAC: \(306 / 290 \approx 1{,}06\), no 2,9

Después de recuperar el CAC quedan unos **$16 de margen bruto en toda la vida del cliente**. Cero para sueldos, herramientas y el resto del opex. Y eso sin descontar el dinero en el tiempo.

**Payback:** \(290 / 24{,}50 \approx 12\) meses, casi igual a la vida media. A los 12 meses solo sigue activo cerca del 37% de la cohorte. Los que se van antes no cubren su CAC; los que se quedan mucho tiempo apenas compensan el promedio.

**Los $10.000:** a $290 de CAC son unos 34 clientes. Margen bruto de por vida ≈ $10.500. Recuperas el gasto en ~12 meses y no te queda nada para operar. Si al subir el presupuesto el CAC sube o el churn no baja, el canal queda en rojo.

Para que el canal aguante un LTV/CAC de 3× haría falta, con precio y margen actuales, un CAC de unos **$100**, o bajar el churn mensual a cerca del **2,8%** (y aun así el payback seguiría largo). Antes de meter presupuesto, el cuello de botella es el 8% de churn, no el alcance.