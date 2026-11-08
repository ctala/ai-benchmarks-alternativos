# GLM 5.2 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `z-ai/glm-5.2`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 12.958s | tokens_per_second: 90.7
- input_tokens: 206 | output_tokens: 1175

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

No le des. Tu plan acaba de morir en la aritmética. 

Vamos a recalcular tus números paso a paso, porque tienes tres errores graves en tu cálculo:

**1. El cálculo de la retención (Lifetime)**
Asumiste que un cliente se queda 2 años (24 meses) porque "parece razonable". Pero tu churn mensual es del 8%. En SaaS, la vida media de un cliente se calcula como 1 / Churn.
- Vida media = 1 / 0.08 = **12.5 meses**, no 24.
*Con un churn del 8%, a los 8 meses ya se te ha ido la mitad de los clientes.*

**2. El Margen Bruto**
Calculaste el LTV sobre el precio ($35), pero el LTV debe calcularse sobre el dinero que realmente te queda en el bolsillo, es decir, tu margen bruto.
- Ingreso neto por mes = $35 × 70% = **$24.50/mes**

**3. El cálculo real del LTV**
La fórmula correcta es: (ARPU × Margen Bruto) / Churn
- LTV = ($35 × 0.70) / 0.08
- LTV = $24.50 / 0.08
- **LTV real = $306.25**

**La realidad de tu ratio LTV/CAC**
- LTV / CAC = $306.25 / $290 = **1.05**

Un ratio de 1.05 no es cercano a 3; es un desastre. Significa que por cada dólar que inviertes en publicidad, recuperas ese dólar y 5 centavos para cubrir el costo del producto. No te queda nada para pagar sueldos, alquiler, herramientas, ni para generar ganancias. Estás comprando clientes para perder dinero.

**El problema del Payback Period (Período de recuperación)**
Tardas **11.8 meses** en recuperar los $290 de CAC (290 / 24.50). Dado que tu cliente promedio se va a los 12.5 meses, el cliente apenas te da 2 meses de "ganancia" antes de churnear. Esto ahogará tu flujo de caja (cash flow) inmediatamente.

**Veredicto:**
No metas los $10,000 en publicidad todavía. Tienes dos opciones antes de escalar:
1. **Bajar el CAC:** $290 es altísimo para un producto de $35/mes. Necesitas bajarlo a menos de $80 para tener un LTV/CAC saludable de 3.8.
2. **Bajar el Churn:** Si bajas tu churn al 4% mensual (vida media de 25 meses), tu LTV sube a $612, y tu ratio sube a 2.1. Aún no llega a 3, pero ya empieza a tener sentido.

Arregla una de las dos variables (o ambas) y vuelve a mi mesa. Hasta entonces, guarda esos $10,000.