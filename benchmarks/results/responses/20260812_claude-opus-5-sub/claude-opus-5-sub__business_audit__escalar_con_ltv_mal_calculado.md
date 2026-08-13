# Claude Opus 5 (suscripción) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `claude-opus-5`
- success: True  | final: 7.95 | quality: 10.0
- latency_total: 76.228s | tokens_per_second: 58.8
- input_tokens: 2 | output_tokens: 4482

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

## No. Y no es marginal: es 1,06, no 2,9.

Hay dos errores en tu cálculo y los dos empujan en la misma dirección — a favor de gastar.

### Error 1: la vida del cliente no la elegís, la fija el churn

Con 8% de churn mensual, la vida promedio es `1 / 0.08 = 12,5 meses`. No 24.

A los 24 meses te queda el `0,92^24 = 13,7%` de la cohorte. La mediana de vida es 8,3 meses — la mitad de tus clientes se va antes del mes 9. Los "2 años" son la cola larga de una minoría, no el cliente típico.

### Error 2: el LTV se calcula con margen, no con precio

Vos no te llevás $35. Te llevás $24,50. El resto es infraestructura y Stripe.

| | Tu cálculo | Real |
|---|---|---|
| Vida del cliente | 24 meses | **12,5 meses** |
| Ingreso mensual | $35 | $35 |
| Margen mensual | (ignorado) | **$24,50** |
| LTV | $840 | **$306** |
| CAC | $290 | $290 |
| **LTV/CAC** | **2,9** | **1,06** |

`LTV = 35 × 0,70 / 0,08 = $306,25`

Con 1,06 estás comprando dólares a 94 centavos, antes de contar tu tiempo, tu equipo, soporte, y cualquier costo fijo. Y ojo: 2,9 tampoco está "por encima de 3". Está por debajo.

### El número que realmente te frena: payback de 11,8 meses

`290 / 24,50 = 11,8 meses` para recuperar el CAC.

La vida promedio de tu cliente es 12,5 meses. Recuperás lo que gastaste en adquirirlo **tres semanas antes de que se vaya**. No hay negocio ahí, hay un ciclo de lavado de caja.

### Qué compra tu $10.000

34 clientes ($10.000 / $290). Eso es $845/mes de margen bruto que se va erosionando 8% mensual.

- **A 12 meses:** recuperaste ~$6.700. Seguís $3.300 abajo.
- **A vida completa de la cohorte (~3 años):** $10.565. Ganaste **$565** sobre $10.000, repartidos en tres años.

Eso no es escalar. Es prestarle $10.000 a tu propio negocio a una tasa peor que un depósito a plazo.

### Y el CAC de $290 no sobrevive el salto

Ese $290 lo mediste al nivel de gasto actual, con tus mejores audiencias. Multiplicar el gasto por un orden de magnitud significa: reinicio de aprendizaje, saturación de audiencia, y bajar a públicos más fríos. Lo normal es que el CAC suba 20-40% en el camino. A $380 de CAC tu ratio cae a 0,80 — perdés plata en cada cliente nuevo, con certeza matemática.

---

## Antes de tocar nada: resolvé la contradicción

Dijiste 8% de churn **y** 2 años de vida. Esos dos números no pueden ser ciertos a la vez. Uno lo mediste y el otro lo asumiste — averiguá cuál es cuál, porque cambia todo:

- Si el churn real es 8% → todo lo de arriba aplica.
- Si de verdad medís 24 meses de vida en cohortes cerradas → tu churn es ~4%, y el LTV es $612, ratio 2,1. Mejor, pero **sigue por debajo de 3**.

En ninguno de los dos escenarios el plan pasa.

## Dónde está la palanca real

Corrí la sensibilidad. El precio solo no te salva:

| Cambio | LTV/CAC |
|---|---|
| Hoy | 1,06 |
| Precio $35 → $49 | 1,48 |
| Churn 8% → 4% | 2,10 |
| Churn 8% → 4% + CAC $290 → $150 | **4,08** |
| Solo CAC $290 → $100 | **3,06** |

**Bajar el churn a la mitad duplica el LTV.** Ninguna optimización de creativos te da ese retorno. Y es más barato: onboarding, activación en la primera semana, entender por qué se van los que se van.

## El plan anual es tu mejor arma y no lo estás usando en el cálculo

Tenés $249/año en la mesa. Un cliente anual te deja `249 × 0,70 = $174` de margen **el día uno**. Eso convierte un payback de 11,8 meses en recuperar el 60% del CAC de inmediato, más 12 meses de retención estructural.

Si el mix de nuevos clientes por publicidad fuera mayoritariamente anual, la conversación cambia por completo. Medí qué porcentaje de tus altas pagadas hoy toman anual. Si es bajo, ese es el experimento antes que el gasto.

## Qué haría yo este mes

1. **Verificá el CAC.** ¿Es gasto en ads dividido por clientes **pagadores atribuibles**, o dividido por todas las altas incluyendo orgánicas y free? El segundo cálculo infla el resultado sistemáticamente. Si tenés tier gratis, casi seguro tu CAC a pagador real es mayor a $290.
2. **Ataca el churn.** Objetivo 8% → 5%. Es la única palanca que mejora todo lo demás sin gastar en medios.
3. **Empujá el anual** en el checkout y en el primer mes de vida del cliente.
4. **Escalá en escalera, no de un salto.** Duplicá el presupuesto, esperá 3-4 semanas, medí el CAC **de esa cohorte** y su retención al día 30. Recién ahí volvés a duplicar. Fijá el umbral de corte antes de empezar: si el CAC a pagador supera $180, se apaga.

Con $10.000 en el mes no vas a comprar crecimiento. Vas a comprar la respuesta a una pregunta que podés responder con $1.000 y cuatro semanas.