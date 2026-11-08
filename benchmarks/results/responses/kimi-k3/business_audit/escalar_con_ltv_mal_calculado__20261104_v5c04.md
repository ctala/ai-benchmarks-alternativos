# Kimi K3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.95 | quality: 10.0
- latency_total: 78.836s | tokens_per_second: 49.5
- input_tokens: 315 | output_tokens: 3904

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

**No le des. Tu aritmética tiene dos errores que te llevan de "casi 3x" a "apenas 1x".**

## Error 1: la vida del cliente no es 24 meses

Con 8% de churn mensual, la vida esperada es **1 / 0.08 = 12,5 meses**, no 24. Verifícalo: a los 12 meses te queda el 0,92¹² = **37%** de la cohorte; a los 24 meses, el **13,5%**. Tu churn anual real es 63%. Eso no es "se quedan unos 2 años".

## Error 2: el LTV se calcula sobre margen, no sobre revenue

Cada cliente te deja 35 × 0,70 = **$24,5/mes** de margen bruto. Eso es lo que tienes para recuperar el CAC.

## Los números corregidos

| Métrica | Tu cálculo | El cálculo correcto |
|---|---|---|
| Vida media | 24 meses | 12,5 meses |
| LTV | $840 | **$306** (24,5 × 12,5) |
| LTV/CAC | 2,9 | **1,06** |
| Payback | — | ~11,8 meses, y solo el 37% de los clientes llega |

Detalle adicional: incluso con tu matemática, 2,9 es *menos* que 3, no "por encima de 3 más o menos".

## Qué compran tus $10.000

- 10.000 / 290 = ~34 clientes.
- Retorno esperado: 34 × $306 = **~$10.400** distribuidos en más de un año.
- Es decir: inmovilizas $10k un año para ganar ~$400 esperados, antes de sueldos, soporte y cualquier costo fijo. Y asumiendo que el CAC se mantiene en $290 al escalar, cosa que casi nunca pasa.

Peor aún: el cliente mediano dura 8,3 meses y genera ~$203. **El 63% de los clientes que compres no recuperará su CAC.** El promedio se salva solo por la cola larga de los pocos que se quedan.

Y la sensibilidad es brutal: si el churn se te mueve de 8% a 9%, el LTV cae a $272 < CAC $290. Pierdes plata en cada cliente.

## El problema no es el CAC, es el churn

Tu CAC de $290 es razonable. Lo que mata el modelo es perder 8% de la base cada mes. Mira los caminos al 3x:

- **Bajar churn a ~2,8%/mes** → vida de 35,5 meses → LTV $870 → ratio 3,0 ✅ (palanca principal)
- Bajar CAC a ~$100 con el churn actual → improbable
- Subir ARPU de $35 a ~$99 → improbable sin cambiar de segmento

## Recomendación

1. **No escales ads ahora.** A ratio 1,06, "crecer fuerte" = comprar revenue sin margen y con caja atada un año.
2. Dedica los próximos 1-2 meses a retención: ¿por qué se van? ¿Onboarding, falta de hábito, segmento equivocado? Cada punto de churn que recortes vale más que cualquier optimización de campañas.
3. Cuando el churn baje de ~4-5%, rehaz los números. Si quieres validar mientras tanto, haz un test de $1.500-2.000 midiendo CAC real por cohorte, no una apuesta de $10k.

¿Tienes datos de por qué churnan, o curva de retención por mes de cohorte? Con eso te digo si el problema es de activación temprana o de valor a largo plazo — se arreglan distinto.