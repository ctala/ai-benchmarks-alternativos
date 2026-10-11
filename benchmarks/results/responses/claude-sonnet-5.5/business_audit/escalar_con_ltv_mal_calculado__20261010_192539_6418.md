# Claude Sonnet 5.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 15.524s | tokens_per_second: 118.1
- input_tokens: 297 | output_tokens: 1833

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

# No le des todavía

Hay dos errores en tu cálculo, y juntos cambian la respuesta.

## 1. La vida del cliente está mal calculada
Con 8% de churn mensual, la vida media es 1 / 0,08 = **12,5 meses**, no 24. Para que un cliente dure 24 meses, el churn tendría que ser ~4,2%.

## 2. LTV debe calcularse sobre margen, no sobre ingresos
- Ingresos por cliente: $35 × 12,5 = $437,50
- **LTV (margen bruto 70%): $306**

## Tu LTV/CAC real
$306 / $290 = **1,06x**

(Y aunque tu cifra fuera 2,9, está por debajo de 3, no por encima.)

## Payback
- Margen bruto mensual por cliente: $24,50
- Cálculo ingenuo: 290 / 24,50 ≈ 12 meses, ignorando el churn
- Con churn, la cohorte recupera el CAC en **~35 meses**. Pierdes clientes más rápido de lo que recuperas lo invertido.

## Qué compran tus $10.000
- ~34 clientes
- Margen bruto total esperado a lo largo de su vida: ~$10.500
- Ganancia: **~$500 en ~3 años**, antes de soporte, desarrollo y costos fijos. Dejas tu caja inmovilizada para quedar prácticamente en cero, o en pérdida si el churn de los clientes pagados es peor que el de tus orgánicos.

## Qué necesitas para que escale sano (LTV/CAC ≥ 3, payback < 12 meses)
Con el CAC actual de $290 necesitarías un LTV de ~$870. Opciones:
- **Bajar el CAC a ~$100** con los mismos precio y churn.
- **Bajar el churn a 4%** (vida de 25 meses, LTV ≈ $612, 2,1x). Mejora, pero no basta solo.
- **Subir el precio a $50 con churn de 5%:** LTV ≈ $700 (2,4x). Con un CAC de ~$230 llegarías a 3x.
- **Planes anuales prepagados**, que recuperan el CAC desde el día 1 y reducen el churn.

## Qué haría yo
1. No gastes los $10.000. Con este LTV/CAC, más gasto solo acelera la pérdida de caja.
2. Revisa si tu "ya soy rentable" depende de clientes orgánicos. El CAC pagado es otro negocio.
3. Arregla churn y precio primero. Cada punto de churn que bajes mueve tu LTV más que cualquier optimización de anuncios.
4. Haz un test de $1.000–2.000 para medir el CAC real y, sobre todo, el churn de la cohorte pagada a 60–90 días.
5. Escala cuando LTV/CAC supere 3x o el payback baje de ~12 meses.

Si me pasas el desglose de churn (primer mes vs. meses posteriores) y el CAC por canal, te ayudo a ver dónde está la palanca más barata.