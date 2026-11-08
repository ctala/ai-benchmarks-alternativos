# Claude Fable 5.1 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.95 | quality: 10.0
- latency_total: 32.591s | tokens_per_second: 69.3
- input_tokens: 297 | output_tokens: 2260

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

No le des. Los tres errores de tu cálculo van todos en la misma dirección, y cuando los corriges el plan deja de cerrar.

## 1. Un cliente no se queda 2 años, se queda 12,5 meses

Con 8% de churn mensual, la vida media es 1/0,08 = **12,5 meses**, no 24. No sé de dónde sale "unos 2 años", pero no sale de ese churn.

Peor aún: la media está inflada por una cola de clientes muy fieles. El cliente **mediano** se va a los 8,3 meses (0,92^8,3 ≈ 0,5). A los 12 meses solo te queda el 37% de la cohorte.

## 2. LTV se calcula sobre margen, no sobre ingreso

Los $35 no son tuyos; $24,50 sí (35 × 0,70). El CAC se paga con margen bruto.

## 3. Los números reales

| | Tu versión | Corregido |
|---|---|---|
| Vida media | 24 meses | 12,5 meses |
| LTV | 35 × 24 = $840 | 35 × 12,5 × 0,70 = **$306** |
| LTV/CAC | 2,9 | **1,06** |
| Payback del CAC | — | 290 / 24,50 = **11,8 meses** |

LTV/CAC de 1,06 significa que ganas $16 por cada $290 que inviertes, y los recuperas a lo largo de más de un año. Y el payback de 11,8 meses cae *después* de que el 63% de los clientes ya se fue: la mayoría de tus clientes nunca te devuelve lo que costó adquirirlos. Los pocos que se quedan dos años subsidian a los demás.

(Nota al margen: 2,9 tampoco está "por encima de 3". Pero es lo de menos.)

## 4. Qué pasa con los $10.000

- $10.000 / $290 ≈ 34 clientes.
- Margen bruto esperado durante toda su vida: 34 × $306 ≈ $10.500.
- Resultado: **+$500 en el mejor caso, cobrados en cuotas durante 12-24 meses**, asumiendo que el CAC de $290 se mantiene al multiplicar el gasto (normalmente no: al subir presupuesto el CAC sube porque agotas las audiencias baratas primero) y sin descontar el valor del dinero en el tiempo.

Estás a un 5% de error en cualquier variable de que la campaña pierda dinero. Eso no es escalar, es apostar a cara o cruz con tu caja.

## 5. Qué tiene que cambiar para que esto funcione

Para LTV/CAC = 3 con tu margen necesitas LTV ≈ $870 de margen, es decir, $1.243 de ingreso por cliente. Caminos:

| Palanca | Qué necesitas | Ratio resultante |
|---|---|---|
| Churn a 5% | vida 20 meses | 1,7 |
| Churn a 4% | vida 25 meses | 2,1 |
| Churn a 3% | vida 33 meses | 2,8 |
| Churn a 2,8% | vida 36 meses | 3,0 |
| CAC a $100 (churn igual) | — | 3,0 |
| Precio a $70 (churn igual) | — | 2,1 |

El churn es la palanca que lo cambia todo, y es la que está rota. 8% mensual en un producto de $35/mes significa que pierdes toda tu base cada ~12 meses: si inviertes en adquisición ahora, estás llenando un balde con un agujero del 8%.

## Recomendación

1. **No gastes los $10.000 en ads este mes.** Gasta una fracción (1-2k) solo para validar que el CAC de $290 es real y estable, no un número de una campaña pequeña.
2. **Pon el dinero y el tiempo en bajar el churn.** Entrevistas de salida, onboarding, cohortes por canal (los clientes de ads suelen churnear más que los orgánicos; si es tu caso, tu LTV real de clientes pagados es aún menor).
3. Vuelve a este cálculo cuando el churn esté por debajo de 4% y el payback por debajo de 6 meses. Ahí sí, mete gasolina.

Ser rentable hoy con crecimiento orgánico y escalar con ads son dos negocios distintos. Con estos unit economics, el segundo todavía no existe.