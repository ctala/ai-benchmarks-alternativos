# Claude Fable 5.2 — strategy/pricing_strategy

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 4.34 | quality: 5.0
- latency_total: 53.189s | tokens_per_second: 92.7
- input_tokens: 290 | output_tokens: 4930

## Entrada exacta (lo que recibió el modelo)

**user:**

Mi SaaS de gestion de inventario tiene estos datos:
- CAC actual: $120
- LTV promedio: $840 (14 meses * $60/mes)
- Churn mensual: 7%
- 200 clientes actuales
- Competidores cobran entre $29 y $149/mes
- Mi costo por usuario es ~$8/mes

Estoy considerando subir el precio de $60 a $89/mes.
Analiza:
1. Calcula el LTV/CAC ratio actual y como cambiaria
2. Estima el impacto en churn (usa benchmarks de la industria SaaS)
3. Modela 3 escenarios: optimista, realista, pesimista
4. Dame tu recomendacion con numeros concretos
5. Sugiere una estrategia de implementacion (grandfather, gradual, etc)


## Respuesta completa

**Conclusión: sube el precio, pero empieza solo con clientes nuevos.** El riesgo no está en los clientes que se van al anunciar la subida, sino en que suban el churn permanente y el CAC.

## 1. LTV/CAC actual y con el nuevo precio

| | $60/mes | $89/mes (mismo churn) |
|---|---|---|
| LTV por ingresos | $840 | $1,271 |
| LTV por margen (precio − $8, dividido por churn) | $743 | $1,157 |
| LTV/CAC por margen | 6.2x | 9.6x |
| Payback del CAC | 2.3 meses | 1.5 meses |

Tu ratio ya es muy sano (el benchmark es 3x o más). Tu punto débil es el churn del 7% mensual, que está en el extremo alto del rango típico de SaaS para pymes (3-7%).

## 2. Impacto en churn

No hay un benchmark exacto para una subida del 48%, así que estos rangos son supuestos razonables y no datos duros. Hay tres efectos distintos:

- **Fuga puntual de clientes actuales:** las subidas del 20-50% bien comunicadas suelen provocar entre 5% y 15% de bajas extra en los 2-3 meses siguientes. La tuya está en la parte alta, así que puede llegar al 25%.
- **Churn recurrente:** puede subir 1-3 puntos por mayor sensibilidad al precio.
- **Conversión de nuevos:** si cae, tu CAC sube.

Tus puntos de equilibrio dan bastante colchón:

- Puedes perder hasta **65 clientes (32.6%)** y mantener el mismo MRR.
- El churn mensual puede subir hasta **10.9%** antes de que el LTV por margen empeore.
- La conversión puede caer hasta **36%** antes de que cada dólar de marketing rinda menos que hoy.

## 3. Escenarios

Aplico la subida a toda la base. Para el largo plazo supongo que hoy captas unos 14 clientes al mes (lo necesario para mantener 200 con 7% de churn) y que el presupuesto de marketing no cambia.

| | Optimista | Realista | Pesimista |
|---|---|---|---|
| Fuga puntual | 5% (10) | 12% (24) | 25% (50) |
| Churn mensual | 7% | 8% | 10% |
| CAC | $120 | $150 | $190 |
| MRR inmediato | $16,910 (+41%) | $15,664 (+31%) | $13,350 (+11%) |
| LTV/CAC por margen | 9.6x | 6.8x | 4.3x |
| MRR de equilibrio a largo plazo | $17,800 | $12,460 | $7,870 |

A corto plazo ganas en los tres escenarios. A largo plazo, el realista apenas supera tus $12,000 actuales y el pesimista te deja peor, porque el churn y el CAC más altos encogen la base con el tiempo.

## 4. Recomendación

1. **Clientes nuevos: $89 desde ya.** Estás a mitad del rango de mercado ($29-149), así que el precio es defendible.
2. **Clientes actuales: $79 en vez de $89** (+32%). Con una fuga del 10% quedarían 180 clientes a $79, es decir, $14,220 de MRR (+18.5%). El equilibrio está en perder el 24%.
3. **Ataca el churn en paralelo.** Bajarlo del 7% al 5% sube el LTV por margen un 40% incluso sin tocar el precio. Con las dos cosas llegarías a $1,620, más del doble que hoy.

## 5. Implementación

1. **Semanas 1-6:** cobra $89 solo a nuevos y mide conversión y churn temprano. Si la conversión cae menos del 20-25%, sigue adelante. Si cae más del 36%, prueba $79.
2. **Semana 6:** anuncia la subida a los clientes actuales con 60 días de aviso, acompañada de mejoras concretas del producto.
3. **Oferta de plan anual:** ofréceles mantener $60/mes si pagan el año por adelantado ($720). Si 40 clientes aceptan, recibes $28,800 de caja y esos clientes no pueden irse en 12 meses.
4. **Día 60:** los demás pasan a $79. Prepara una oferta de retención (por ejemplo, 3 meses más a $60) para quien pida cancelar.
5. **Seguimiento:** revisa churn y conversión cada mes durante dos trimestres.

Si me das tu número real de altas mensuales y tu tasa de conversión, puedo ajustar los escenarios a tu caso.