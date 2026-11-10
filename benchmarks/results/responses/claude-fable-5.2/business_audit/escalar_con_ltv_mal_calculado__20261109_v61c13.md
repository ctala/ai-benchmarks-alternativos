# Claude Fable 5.2 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 8.0 | quality: 10.0
- latency_total: 24.292s | tokens_per_second: 88.2
- input_tokens: 297 | output_tokens: 2142

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

**No le des. Con tus propios números, el LTV/CAC real es de alrededor de 1,06, no 2,9.**

## Dónde falla tu cálculo

1. **La vida del cliente no es 24 meses.** Con churn de 8% mensual, la vida media es 1 / 0,08 = **12,5 meses**. Para que un cliente dure 2 años necesitarías un churn cercano al 4,2%.
2. **Usaste ingresos, no margen.** El LTV se calcula sobre el margen bruto, porque el 30% restante se va en infraestructura y procesador de pagos.
3. **2,9 no está por encima de 3.** Incluso con tu propio número, no pasabas el umbral.

## Los números recalculados

| Métrica | Tu cálculo | Real |
|---|---|---|
| Vida media del cliente | 24 meses | 12,5 meses |
| Margen bruto por cliente al mes | no aplicado | $35 × 0,70 = $24,50 |
| LTV | $840 | $24,50 × 12,5 = **$306,25** |
| LTV/CAC | 2,9 | $306,25 / $290 = **1,06** |

## Qué pasa si metes los $10.000

- Compras unos 34 clientes ($10.000 / $290).
- El margen bruto total que dejarán en toda su vida es de unos $10.560.
- Ganas unos $560 sobre $10.000, antes de costos fijos, soporte y tu tiempo.
- A los 12 meses habrás recuperado solo unos $6.700. Como los clientes se van yendo, recuperar el CAC completo tarda unos **35 meses**.

Además, el CAC casi siempre sube al escalar la inversión, porque las primeras audiencias son las más baratas. Con un margen de 6%, cualquier subida te deja en negativo.

## Qué tendría que cambiar para llegar a 3:1

Cualquiera de estas, por separado:

- **CAC:** bajarlo a unos $100.
- **Churn:** bajarlo a alrededor de 2,8% mensual.
- **Precio:** subirlo a unos $99/mes, sin que empeore el churn.

Lo más realista es una combinación. Por ejemplo, con churn de 4% y CAC de $200, el LTV sube a $612 y el ratio queda en 3,06.

## Mi recomendación

No escales la publicidad todavía. Tu problema es la retención: con 8% de churn mensual pierdes más de la mitad de cada cohorte en 9 meses. Ataca eso primero, porque cada punto de churn que bajes mejora el LTV de todos tus clientes, no solo de los pagados.

Si quieres seguir aprendiendo del canal, haz una prueba chica de $1.000 a $2.000 para buscar segmentos con CAC más bajo. Hoy los $10.000 serían gastar para quedar casi en el mismo lugar tres años después.