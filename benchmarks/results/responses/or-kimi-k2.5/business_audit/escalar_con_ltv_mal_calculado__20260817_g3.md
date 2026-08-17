# Kimi K2.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.23 | quality: 10.0
- latency_total: 87.003s | tokens_per_second: 23.5
- input_tokens: 231 | output_tokens: 2048

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

 **Stop.** No le metas esos $10,000. Tu plan muere en la aritmética.

Has cometido dos errores fatales que convierten tu "ratio 2.9" en un agujero negro de efectivo. Aquí está la autopsia:

---

### Error #1: La vida promedio no son 24 meses
Con un **churn del 8% mensual**, la vida promedio de un cliente es:
$$ \text{Vida promedio} = \frac{1}{\text{Churn}} = \frac{1}{0.08} = \mathbf{12.5\ meses} $$

No 24 meses. Estás calculando como si retuvieras al 100% de los clientes durante 2 años, pero pierdes al 8% de tu base *cada mes*. Es una curva exponencial, no lineal.

Con 8% de churn mensual:
- A los 6 meses ya perdiste al 40% de la cohorte.
- A los 12 meses, sobrevive solo el 36%.
- Tu "promedio" es 12.5 meses, no 24.

### Error #2: El LTV se calcula sobre el margen, no sobre el precio
El valor de vida útil (LTV) es el **beneficio** que te deja el cliente, no el ingreso bruto.

$$ \text{LTV} = \frac{\text{ARPU} \times \text{Margen\ bruto}}{\text{Churn}} = \frac{\$35 \times 0.70}{0.08} = \mathbf{\$306} $$

Tu cálculo real de LTV/CAC:
$$ \frac{\$306}{\$290} = \mathbf{1.05} $$

**Estás perdiendo plata.** Por cada cliente que compras a $290, solo recuperas $306 en valor presente (y eso asumiendo que el churn no empeora al escalar).

---

### El problema del Cash (más letal que el LTV)
Incluso si el LTV fuera positivo, mira tu **Payback Period**:

$$ \frac{\$290}{\$35 \times 0.70} = \frac{290}{24.5} = \mathbf{11.8\ meses} $$

Tardas casi un año en recuperar tu inversión. Pero con 8% de churn mensual, la probabilidad de que un cliente te dure 12 meses es solo **36%**. Es decir: **pagas $290 hoy por una "apuesta" donde el 64% de las veces el cliente se va antes de devolverte ni siquiera el costo de adquisición.**

Esto es quemar efectivo.

---

### La receta antes de escalar
Para que este modelo funcione, necesitas mover *al menos* dos de estas tres palancas:

