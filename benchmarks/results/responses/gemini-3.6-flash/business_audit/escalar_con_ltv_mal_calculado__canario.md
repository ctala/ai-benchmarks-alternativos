# Gemini 3.6 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 9.125s | tokens_per_second: 224.0
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

**Frena. No pongas un solo dólar en publicidad todavía.** 

Tu plan no solo no va a generar retornos, sino que si metes $10.000 este mes, vas a incinerar caja y podrías matar tu rentabilidad actual. 

Aquí está el desglose de dónde se rompió tu aritmética:

---

### 1. El error de la vida media (Lifespan)
Dijiste que un cliente se queda unos 2 años (24 meses) con un churn del 8%. 
La fórmula matemática de la vida media de un cliente es $1 / Churn$.

$$\text{Vida media} = \frac{1}{0,08} = \mathbf{12,5\text{ meses}}$$

No son 24 meses; es **casi la mitad**. Con un 8% de churn mensual, pierdes al ~64% de tu cohorte en el primer año.

### 2. El error del LTV (Olvidaste el Margen Bruto)
El LTV (Lifetime Value) no se calcula sobre la facturación bruta, sino sobre el **beneficio bruto**. No puedes usar dinero que se va en infraestructura y pasarelas de pago para recuperar tu CAC.

* Facturación total por cliente: $35 \times 12,5 \text{ meses} = \$437,50$
* Margen bruto (70%): $\$437,50 \times 0,70 = \mathbf{\$306,25}$

**Tu LTV real es de $306,25, no de $840.**

### 3. La realidad del LTV/CAC
Con un LTV real de $306,25 y un CAC de $290:

$$\text{LTV/CAC} = \frac{\$306,25}{\$290} = \mathbf{1,05x}$$

Un LTV/CAC de 1,05x significa que ganas $16,25 por cliente **en un periodo de un año y medio**, antes de pagar salarios, impuestos, software interno o alquiler. Estás operando en punto de equilibrio teórico, pero en pérdida en el mundo real.

---

### 4. La trampa mortal: El Payback Period (Tiempo de recuperación)
Cada mes, un cliente te deja en beneficio bruto:
$$\$35 \times 0,70 = \mathbf{\$24,50\text{/mes}}$$

Para recuperar los $290 que gastaste en adquirirlo:
$$\text{Payback Period} = \frac{\$290}{\$24,50} = \mathbf{11,8\text{ meses}}$$

Tardas **casi 12 meses** solo en recuperar el dinero de la publicidad. Pero recuerda: tu churn es del 8% mensual. Para cuando llegues al mes 12, **más del 60% de los clientes que pagaste a $290 ya se habrán ido antes de haber devuelto su costo de adquisición.**

---

### ¿Qué pasa si metes los $10.000 hoy?

1. Adquieres ~34 clientes ($10.