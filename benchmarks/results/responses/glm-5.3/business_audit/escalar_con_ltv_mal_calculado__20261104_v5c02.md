# GLM 5.3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 87.725s | tokens_per_second: 75.5
- input_tokens: 206 | output_tokens: 6619

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

No le des todavía. El plan no muere, pero queda herido en la aritmética. Tienes tres errores apilados, y cada uno va en tu contra.

**Error 1: la vida del cliente.**
Con churn mensual de 8%, la vida esperada es 1/0,08 = **12,5 meses**, no 24. Tu churn y tus "2 años" son mutuamente excluyentes: una vida de 24 meses implica churn de ~4,2%. Además, con 8% mensual, a los 24 meses solo queda (0,92)²⁴ ≈ 13% de la cohorte original. Sospecho que tus "2 años" vienen de mirar a tus clientes actuales — los que sobrevivieron — o del tenure promedio a la fecha, que subestima el churn porque muchos todavía no se han ido. Sesgo de supervivencia clásico.

**Error 2: el margen.**
El LTV se calcula sobre ganancia bruta, no sobre ingreso. Tu cliente aporta $35 × 70% = **$24,50/mes**, no $35.

**Error 3 (menor): 2,9 no está "por encima de 3".**
Está debajo. Y la regla del 3:1 ya se aplica al LTV de margen bruto, así que la vara correcta es más exigente que la que usaste.

**Números corregidos:**

| | Tu cálculo | Corregido |
|---|---|---|
| Vida del cliente | 24 meses | 12,5 meses |
| Aporte mensual | $35 | $24,50 |
| LTV | $840 | **$306** |
| LTV/CAC | 2,9 | **1,05** |

La fórmula compacta: **LTV = (precio × margen bruto) / churn**.

**Qué significa esto:**
- Payback del CAC = 290 / 24,50 ≈ **11,8 meses**... contra una vida esperada de 12,5. Recuperas tu dinero justo cuando el cliente promedio ya se está yendo.
- El cliente *mediano* vive ~8,3 meses: se va casi 4 meses antes de pagarte.
- Solo ~37% de los clientes que compres llegarán alguna vez a cubrir su propio costo. Todo tu "profit" depende de la cola.

**Qué compra realmente el gasto de $10.000:**
~34 clientes × $306 = ~$10.400 de ganancia bruta *total*, goteando a lo largo de 1-2 años y decayendo 8% al mes. Gastas $10.000 hoy para recuperar ~$10.400 en margen bruto durante años — antes de costos fijos, antes de que el CAC suba al escalar presupuesto (y sube), y antes de considerar que el tráfico pagado suele churnear más rápido que el orgánico. Eso no es un motor de crecimiento; es capital congelado a retorno ~0%. Y con cualquier tasa de descarto razonable, el ratio cae bajo 1: pagarías más de lo que vale el cliente.

**Y ojo — incluso en tu escenario optimista falla:**
Si te concedo los 24 meses (churn ~4,2%), el LTV corregido por margen es $24,50 × 24 = $588. Ratio: 2,0. Todavía bajo 3. El plan solo pasa si corrijo *ambos* errores a tu favor... y además el churn baja a ~2,8%.

**Antes de darle:**
1. **Mide churn por cohorte y por canal de adquisición.** Si la fuente pagada churnea peor que la orgánica, tu CAC efectivo es aún más alto de lo que crees.
2. **Ataca el churn — es tu palanca más grande.** De 8% a 4% duplica el LTV a $612 (ratio 2,1). De 8% a ~2,8% te lleva a 3:1 con el mismo CAC.
3. **O ataca el CAC:** para 3:1 con churn actual necesitas CAC ≈ $100. Revisa canales, creativos, audiencias.
4. **Plan anual prepago:** no cambia el unit economics, pero adelanta el cash y suele bajar churn — invierte la curva de payback.
5. Si igual quieres probar paid, hazlo con un piloto de $1.500-2.000 con tracking por cohorte, y escala solo si el payback *observado* te sorprende para bien.

Que ya seas rentable probablemente se debe a clientes orgánicos con CAC casi cero. Ese es tu activo real. La publicidad pagada tiene que sostenerse sola, y con estos números no se sostiene.