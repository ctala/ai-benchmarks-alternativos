# GLM 5.3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.27 | quality: 10.0
- latency_total: 64.292s | tokens_per_second: 78.6
- input_tokens: 206 | output_tokens: 5052

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

No le des. El plan muere en la aritmética, y en tres lugares distintos.

## Los tres errores

**1. El lifetime no es 24 meses.** Con 8% de churn mensual, el lifetime promedio es 1/0.08 = **12.5 meses**. La curva de retención es brutal:
- Mes 12: solo 0.92¹² ≈ **37%** de tus clientes siguen ahí
- Mes 24: 0.92²⁴ ≈ **13%**

Los "2 años" no salen de tu churn; salen de ningún lado. Dos tercios de tus clientes se van antes del año.

**2. Calculaste el LTV sobre ingresos, no sobre margen.** Lo que hay que comparar contra el CAC es ganancia bruta. Cada cliente aporta $35 × 0.70 = **$24.50/mes**, no $35.

**3. Menor, pero: 2.9 no está "por encima de 3".** Está debajo. Aunque da igual, porque el número real es otro.

## El recálculo

| | Tu cálculo | Real |
|---|---|---|
| Lifetime | 24 meses | 12.5 meses |
| Aporte mensual | $35 | $24.50 |
| LTV | $840 | **$306** |
| LTV/CAC | 2.9 | **1.06** |

No es 2.9. Es **1.06**. Y el payback lo confirma: $290 / $24.50 = **11.8 meses** para recuperar el CAC, contra un lifetime de 12.5 meses. Recuperas tu dinero 0.7 meses antes de que el cliente se vaya. Cero margen de error.

## Qué pasa con los $10,000

- Compras ~34 clientes ($10,000 / $290)
- Esos clientes generarán ~34 × $306 ≈ $10,560 de ganancia bruta... **a lo largo de más de un año**
- Beneficio neto del experimento: ~$560, antes de costos fijos, con el dinero saliendo hoy y volviendo en 12 meses

Y eso asumiendo lo mejor: que el CAC se mantiene en $290 (al escalar, sube — primero agotas las audiencias baratas) y que las cohortes de pago churnean igual que tus clientes actuales (suelen churnear peor). Si descuentas por valor temporal del dinero, el LTV cae a ~$260 y la relación baja de 1: pasas de break-even a destruir valor.

## Qué tendría que cambiar para que sí

Para llegar a LTV/CAC ≥ 3 necesitarías alguna de estas (o una combinación):

- **CAC de ~$100** (un 65% menos)
- **Churn de ~2.8%** (menos de la mitad del actual)
- **Precio de ~$100/mes** con el mismo churn y CAC
- Margen de 85% solo te lleva a 1.28 — el margen solo no te salva

Ninguna ocurre de un mes para otro.

## Lo que sí haría

Tu rentabilidad actual probablemente viene de adquisición orgánica o barata. Escalar con publicidad a estas cifras no acelera ese negocio — lo diluye.

Si quieres aprender del canal de pago, invierte **$2,000, no $10,000**, y mide retención por cohorte y por canal/creativo. La pregunta útil no es "¿consigo clientes a $290?" (ya sabemos que sí, y que no valen la pena), sino "¿existe algún segmento donde el CAC baje de $150 o el churn sea claramente menor?" Esa respuesta vale más que 34 clientes que no te dejan nada.

La intuición de comparar LTV contra CAC era correcta. Los insumos, no.