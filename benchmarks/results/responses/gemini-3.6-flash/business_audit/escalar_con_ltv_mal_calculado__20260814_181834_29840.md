# Gemini 3.6 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 11.574s | tokens_per_second: 176.6
- input_tokens: 194 | output_tokens: 2044

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

**No. Pon la mano en el freno de mano inmediatamente.** 

Si metes $10.000 en publicidad hoy con estas métricas, vas a incinerar el dinero. Tu plan no muere en la ejecución, muere en la calculadora.

Has cometido dos errores matemáticos fatales en tu cálculo de LTV. Vamos a destriparlos:

---

### Error 1: Te inventaste la vida media del cliente
Dices que un cliente se queda "unos 2 años" (24 meses). 
Con un **Churn mensual del 8%**, la fórmula real de vida media (*Customer Lifespan*) es $1 / \text{Churn}$.

$$1 / 0,08 = 12,5 \text{ meses}$$

Tus clientes no se quedan 24 meses; se quedan **12,5 meses en promedio**. Tu premisa de partida ya estaba inflada al doble.

---

### Error 2: Confundiste Ingresos con Margen Bruto
El LTV **nunca** se calcula sobre la facturación bruta, sino sobre el **Beneficio Bruto**. No puedes usar el dinero que se va en servidores y comisiones de Stripe para recuperar tu CAC.

* **LTV de Ingresos (incorrecto):** $35 \times 12,5 = \$437,50$
* **LTV Real (Margen Bruto del 70%):** $\$437,50 \times 0,70 = \mathbf{\$306,25}$

---

### La Realidad de tus Números

Alineemos tu CAC real contra tu LTV real:

* **LTV Real:** $306,25
* **CAC:** $290,00
* **Ratio LTV/CAC Real:** **1,05x** (No 2,9x como calculaste).

**¿Qué significa un ratio de 1,05x?**
Significa que por cada cliente que compras a $290, ganas $16,25 a lo largo de *un año y medio*. Pero no hemos contado tus costes fijos, nóminas, ni el coste del capital. **Con un LTV/CAC de 1,05x estás perdiendo dinero netamente en cada venta.**

---

### La Trampilla de la Muerte: El Payback Period

Calculemos cuánto tardas en recuperar los $290 que te cuesta cada cliente:
* Ganancia bruta mensual por cliente: $\$35 \times 0