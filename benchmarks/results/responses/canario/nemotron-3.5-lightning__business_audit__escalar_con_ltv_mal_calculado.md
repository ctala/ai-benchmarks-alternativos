# Nemotron 3.5 Lightning — business_audit/escalar_con_ltv_mal_calculado

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.15 | quality: 10.0
- latency_total: 6.217s | tokens_per_second: 478.1
- input_tokens: 223 | output_tokens: 2972

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

No, no me aprobarías aún. Lo que tienes es un **error de cálculo clásico** que, si se ejecuta, convertiría tu rentabilidad actual en pérdida neta.

Aquí el desglose técnico de por qué, y los números corregidos:

### 1. El lifetime (vida del cliente) no son 24 meses
Con un **churn mensual del 8%**, el lifetime promedio se calcula como:
```
Lifetime (meses) = 1 / churn = 1 / 0.08 = 12.5 meses
```
(El cálculo de "24 meses" asume que la tasa de churn cae a la mitad o que hay un contrato mínimo, pero con 8% fijo cada mes, la expectativa de vida es de 12.5 meses.)

### 2. LTV debe incluir el margen bruto
El LTV en dólares puros (`precio × meses`) no es lo que importa para los ads; importa el **beneficio** que te deja cada cliente.

- Ingreso mensual: $35
- Margen bruto: 70% → **Margen por cliente/mes = $35 × 0.70 = $24.50**
- **LTV (beneficio total) = $24.50 × 12.5 = $306.25**

También existe la fórmula estándar SaaS: `LTV = (ARPU × Margen) / Churn = (35 × 0.70) / 0.08 = $306.25`. ✅

### 3. LTV/CAC real
- LTV (beneficio) = $306.25
- CAC = $290
- **LTV/CAC = 306.25 / 290 ≈ 1.06**

Eso está **por debajo del mínimo saludable de 3** y cercano al punto de equilibrio. Significa que cada cliente que traigas con publicidad apenas te devuelve el costo de adquisición en margen, y recién a los ~12 meses empiezas a ganar dinero real con ellos.

### 4. ¿Qué pasa si inviertes $10,000 este mes?
- Nuevos clientes: $10,000 / $290 ≈ **34 clientes**
- Margen mensual inmediato: 34 × $24.50 = **$833**
- Tiempo para recuperar el CAC: $290 / $24.50 ≈ **11.8 meses**
- Considerando que cada mes el 8% se va, el flujo de margen acumulado se desploma rápidamente. Después de 12 meses, habrías recuperado el costo, pero el efectivo estuvo parado y expuesto a riesgo de churn o variaciones de CAC.

### Recomendación
**No aprobar el gasto de $10k** con estos números. La unidad económica está justa apenas, y cualquier aumento de churn, un CAC un poco más alto o una ligera caída de conversión te dejaría en números rojos.

#### Para que sí funcione, necesitas uno de estos cambios:
| Opción | Qué cambiar | Nuevo LTV/CAC objetivo |
|--------|-------------|------------------------|
| **Bajar CAC** | Negociar mejores costos de ads o usar canales orgánicos/referidos | CAC ≤ $100 para LTV/CAC ≥ 3 |
| **Aumentar margen** | Subir precio a $45–$50 o reducir costos de infra/pago | LTV sube proporcionalmente |
| **Reducir churn** | Mejorar onboarding, soporte o producto para bajar al 3–4% mensual | Lifetime sube a 25–33 meses, LTV/CAC ~2.5–3 |
| **Aumentar precio** | Pasar a $45/mes manteniendo churn | Margen por mes = $31.5, LTV = $393, LTV/CAC = 1.35 (aún justo) |

Si insistes en escalar con ads, haz un **test piloto de $2,000–$3,000**, mide el CAC real y el churn real en las primeras 60–90 días, y solo entonces escala si el LTV/CAC se mantiene > 2.5 de forma consistente.

¿Tienes flexibilidad para ajustar alguno de los números (precio, churn objetivo o costo de ads) antes de soltar el presupuesto grande?