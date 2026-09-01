# GLM 5.3 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 140.626s | tokens_per_second: 38.4
- input_tokens: 206 | output_tokens: 5404

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

**No te lo apruebo.** El problema no es tu regla del 3x, es que la aritmética está inflada ~2.7x. Vamos al recálculo.

## Tres errores en tu LTV

**1. El tiempo de vida no son 24 meses.** Con churn de 8% mensual, la vida esperada es 1/0.08 = **12.5 meses**, no 2 años. Para promediar 24 meses necesitarías churn de ~4.2%. Si tienes datos de cohortes que digan otra cosa, muéstramelos; si no, manda la tasa.

**2. El LTV se calcula sobre margen bruto, no sobre revenue.** El 30% se lo llevan infraestructura y el procesador. Nunca lo vas a usar para pagar publicidad.

```
LTV real = $35 × 0.70 × 12.5 = $306
```

**3. Y 2.9 no está "por encima de 3".** Pero ya no importa, porque el ratio real es:

```
$306 / $290 = 1.06
```

## Lo que compra tu $10,000

- ~34 clientes nuevos
- Que generan ~$835/mes de margen bruto, decayendo 8% mensual
- Margen bruto total de la cohorte durante toda su vida: **~$10,400**

Es decir: recuperas tu dinero en ~3 años, sin ganancia, sin contar costos fijos ni tu tiempo. Con 8% de churn, solo el **37% de los clientes sigue vivo al mes 12** — la mayoría nunca paga su CAC completo. Tu CAC se recupera, en esperanza, hacia el mes **~35**, cuando la mediana del cliente ya lleva ~27 meses muerto.

Además: al escalar gasto el CAC casi siempre sube (saturación de subastas). $290 es probablemente tu mejor caso.

## El problema de fondo

8% mensual = **~63% de churn anual**. Estás pensando enmeter gasolina a un tanque que pierde dos tercios por año. La publicidad no es tu palanca ahora; la retención sí.

## Qué necesito ver para aprobarte

Cualquiera de estas dos:

| Palanca | Valor necesario |
|---|---|
| Churn ≤ **2.8%** mensual (con CAC de $290) | LTV ≈ $870, ratio ≈ 3.0 |
| CAC ≤ **$102** (con churn de 8%) | Ratio ≈ 3.0 con LTV actual |

Subir precio solo no alcanza: a $50/mes tu ratio sería 1.5. Sigues corto.

## Mi recomendación

1. **Fija la retención primero**: onboarding, planes anuales, medición de cohortes separando churn nuevo vs. antiguo.
2. Si aun así quieres probar paid, mete **$1,500–2,000, no $10,000**, y midéelo por cohorte: margen bruto cobrado vs. CAC, mes a mes.
3. Escala solo cuando cumplas las dos condiciones: LTV(margen)/CAC ≥ 3 **y** payback ≤ 12 meses.

Hoy el plan no pierde dinero en papel — pero tampoco lo gana, y te deja sin caja ni colchón para arreglar el churn, que es el verdadero problema.