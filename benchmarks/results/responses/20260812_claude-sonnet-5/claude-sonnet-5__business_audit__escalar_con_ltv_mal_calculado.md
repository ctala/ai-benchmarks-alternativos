# Claude Sonnet 5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.34 | quality: 10.0
- latency_total: 19.486s | tokens_per_second: 76.2
- input_tokens: 295 | output_tokens: 1485

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

# Alto ahí. Hay dos errores en el cálculo que cambian todo el resultado.

## Error 1: La vida útil del cliente

Con **churn mensual del 8%**, la vida útil promedio NO es "unos 2 años". Se calcula así:

```
Vida útil = 1 / churn mensual = 1 / 0.08 = 12.5 meses
```

No 24 meses. Confundiste "algunos clientes duran 2 años" con el promedio real de la cohorte. El 8% mensual es un churn agresivo — implica que casi la mitad de tus clientes se van en el primer año.

## Error 2: LTV con revenue, no con margen

El LTV se calcula sobre lo que **realmente te queda**, no sobre el precio de venta. Con 70% de margen bruto:

```
LTV = (Precio × Margen bruto) / Churn mensual
LTV = (35 × 0.70) / 0.08
LTV = 24.5 / 0.08
LTV = $306.25
```

## El número real

```
LTV/CAC = 306.25 / 290 = 1.06
```

No 2.9. **1.06.** Estás casi en punto de equilibrio, no en una zona segura para escalar.

## Lo que esto significa en la práctica

**Payback period real:**
```
CAC / (Precio × Margen) = 290 / 24.5 = 11.8 meses
```

Recuperas el CAC casi en el mes 12... y la vida útil promedio del cliente es 12.5 meses. Es decir: **el cliente promedio apenas te deja margen antes de irse.** Cualquier variación negativa (churn real más alto que el histórico, aumento de CAC por saturar el canal, un mes malo de retención) te pone en números rojos.

## Si metes los $10,000

A $290 de CAC, conseguís ~34 clientes. Con LTV/CAC de 1.06, **no estás comprando crecimiento rentable, estás comprando casi al costo** — y sin margen de error para imprevistos operativos, reembolsos, o soporte.

## Antes de meter un peso, arreglá alguna de estas tres cosas:

1. **Bajar el CAC** — necesitarías ~$100-120 para tener un LTV/CAC saludable (>3x)
2. **Bajar el churn** — si lo llevás a 4-5% mensual, la vida útil sube a 20-25 meses y el LTV se dispara
3. **Subir el precio o el margen** — cada punto de margen bruto pesa directamente en el LTV

**¿Cuál de las tres palancas es más realista de mover en el corto plazo?** Ese es el verdadero punto de partida antes de hablar de presupuesto de ads.