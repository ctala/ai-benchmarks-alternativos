# Claude Opus 4.7 (suscripción) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `claude-opus-4-7`
- success: True  | final: 6.79 | quality: 8.4
- latency_total: 57.216s | tokens_per_second: 46.0
- input_tokens: 6 | output_tokens: 2632

## Respuesta completa

No. Tus números están mal en tres partes y la aritmética real dice que estás a punto de quemar $10.000 para hacer $500. Vamos por partes.

## Los tres errores del cálculo

**1. La vida del cliente no son 24 meses. Son 12,5.**

Con churn mensual del 8%, la vida promedio del cliente es 1 / 0,08 = **12,5 meses**. Los "2 años" salieron de tu cabeza, no de la matemática. Ese solo error infla el LTV al doble.

**2. El LTV se calcula con margen bruto, no con revenue.**

Los $35 no son tuyos, son del cliente. Tuyo es lo que queda después del 30% de costos.

**3. Con eso corregido:**

```
LTV real = ARPU × margen × vida
LTV real = $35 × 0,70 × 12,5 = $306
```

No $840. **$306.**

## El ratio verdadero

```
LTV / CAC = 306 / 290 = 1,05
```

No 2,9. **1,05.** Estás básicamente empatando. La regla de 3 no está "más o menos", está a un tercio de distancia.

## Payback period (el que te va a matar el cash)

```
Payback = CAC / (ARPU × margen)
Payback = 290 / ($35 × 0,70) = 290 / 24,5 = 11,8 meses
```

Tardas **11,8 meses en recuperar el CAC** de un cliente que vive **12,5 meses**. Recuperas la plata literalmente el mes antes de que se vaya. Cero margen de error.

## Qué pasa si metes los $10.000

- Adquieres: 10.000 / 290 ≈ **34 clientes**
- Gross profit sobre toda su vida: 34 × 306 = **$10.404**
- Utilidad neta: $10.404 − $10.000 = **$404**

Pusiste $10K hoy en cash para hacer $400 repartidos en los próximos 12 meses. Y eso **asumiendo que nada empeora**.

## Sensibilidad (donde se derrumba)

El escalado paid siempre trae leads más fríos que el orgánico. Suposiciones realistas:

| Escenario | Churn | LTV | LTV/CAC | Resultado |
|---|---|---|---|---|
| Optimista | 7% | $350 | 1,21 | Ganas $1.700 |
| Tu escenario actual | 8% | $306 | 1,05 | Ganas $500 |
| Realista al escalar | 10% | $245 | 0,84 | **Pierdes $1.550** |
| CAC sube 20% al escalar | 8% + $348 CAC | $306 | 0,88 | **Pierdes $2.000** |

Basta que suba el churn 2 puntos o el CAC un 20% (ambas cosas normales al pasar de warm a cold traffic) para que estés pagando por perder plata.

## Qué necesitarías para que esto funcione

Para llegar a LTV/CAC = 3 con precio y margen actuales:

- **Bajar CAC a $102** (imposible sin cambiar de canal o creativos), o
- **Bajar churn a 2,8%** (requiere producto, no ads), o
- **Subir precio a $100/mes** manteniendo churn.

El churn es el que más apalanca. Cada punto que bajes vale más que optimizar campañas.

## Veredicto

**No le des.** No es que "esté por encima de 3 más o menos". Está en 1,05 y con el escenario realista de escalar, se va debajo de 1.

Antes de meter $10.000 en ads:

1. **Mide churn real de tus últimas 3 cohortes.** ¿Es 8% parejo o está peor en meses recientes?
2. **Segmenta CAC por canal.** Si tu $290 es el promedio y el orgánico es $50 mientras Meta te cobra $450, el paid puro es aún peor de lo que crees.
3. **Prueba con $1.500-2.000 primero.** Valida CAC y calidad de cohorte antes de escalar 5x.
4. **Ataca el churn.** Bajar de 8% a 5% te lleva el LTV a $490 y el ratio a 1,69. Sigues sin llegar a 3, pero al menos ganas plata mientras iteras precio.

La regla dura: **no escalas paid ads hasta tener LTV/CAC ≥ 3 y payback ≤ 12 meses**. Hoy tienes 1,05 y 11,8. Ninguna de las dos.