# Claude Fable 5 (suscripción) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `claude-fable-5`
- success: True  | final: 6.74 | quality: 8.4
- latency_total: 35.986s | tokens_per_second: 45.6
- input_tokens: 2 | output_tokens: 1640

## Respuesta completa

No le des todavía. Tu cálculo tiene dos errores y ambos van en tu contra.

## Error 1: la vida del cliente no son 24 meses

Con churn mensual de 8%, la vida promedio es 1/churn:

- 1 / 0,08 = **12,5 meses**, no 24.

Si un cliente se quedara 2 años, tu churn sería ~4%. Con 8%, la mitad de tu cohorte se fue antes del mes 9.

## Error 2: LTV se calcula sobre margen, no sobre ingreso

Los $35 no son tuyos; el 30% se va en infra y pagos.

- Margen mensual por cliente: 35 × 0,70 = **$24,50**
- LTV real: 24,50 × 12,5 = **$306**

## El número real

- LTV/CAC = 306 / 290 = **1,06**

No es 2,9. Estás en breakeven sobre margen bruto. Después de tu tiempo, herramientas y cualquier otro gasto operativo, **pierdes dinero con cada cliente pagado**.

## Payback: el otro problema

- CAC 290 / margen mensual 24,50 = **11,8 meses para recuperar**
- Vida promedio del cliente: 12,5 meses.

Recuperas la inversión justo cuando el cliente promedio se va. Cero colchón.

## Qué pasa si metes los $10.000

- 10.000 / 290 ≈ **34 clientes**
- Margen total que te devuelven en toda su vida: 34 × 306 ≈ **$10.400**, repartidos en más de un año.

Pones $10.000 hoy para recuperar $10.400 en 12+ meses. Antes de opex. Eso no es escalar, es prestarle plata a Meta sin interés.

## Qué tendría que cambiar antes de escalar (uno de estos tres)

1. **Churn a ~3%**: con vida de ~33 meses, LTV sube a ~$870 y ahí sí LTV/CAC ≈ 3. Es la palanca más potente.
2. **CAC bajo $100**: con tu churn actual, ese es el CAC que soporta un 3x.
3. **Precio/mix**: subir precio o empujar plan anual pagado por adelantado (arregla el problema de caja del payback aunque no arregle el churn).

Mi recomendación concreta: no metas $10.000. Mete $500-1.000/mes como presupuesto de aprendizaje mientras atacas el churn, y mide payback real por cohorte, no LTV proyectado. Cuando el churn baje de 5% y el payback quede bajo 6 meses, ahí sí le das con todo.