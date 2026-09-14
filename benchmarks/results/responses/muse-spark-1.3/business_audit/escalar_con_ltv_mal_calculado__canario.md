# Muse Spark 1.3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 18.651s | tokens_per_second: 155.6
- input_tokens: 202 | output_tokens: 2902

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

No le des. Este plan muere en la aritmética.

Tienes 3 errores encadenados y cuando los corregimos el caso se invierte por completo.

### 1. Tu cálculo vs. el cálculo real

**Tu cálculo:**
Vida útil = ~24 meses (¿de dónde sale?)
LTV = 35 x 24 = $840
LTV/CAC = 840 / 290 = 2.9, que dices que es "por encima de 3 más o menos"

De hecho 2.9 ya está *por debajo* de 3, pero ese es el menor de los problemas.

**El cálculo correcto:**

1.  **Vida útil no es 2 años.** Con churn mensual, la vida promedio esperada es:
  `1 / Churn = 1 / 0.08 = 12.5 meses`
  No 24. Con 8% mensual pierdes el 63% de tus clientes cada año: `1 - (0.92^12) = 63.2%`

2.  **Te olvidaste del margen bruto.** LTV no es facturación, es beneficio bruto.
  Contribución mensual = 35 x 70% = **$24.5 / mes**
  No $35.

3.  **LTV real:**
  `LTV = Contribución mensual / Churn = 24.5 / 0.08 = $306.25`
  O lo mismo: `35 x 0.7 x 12.5 = $306.25`
  No $840. Te dio casi 3x más alto por olvidar el margen y duplicar la vida útil.

**Ratio real:**
`LTV / CAC = 306.25 / 290 = 1.06`

No es 2.9, es **1.06**. La regla de SaaS rentable es >3 para poder pagar equipo, producto, soporte, etc. Tú estás en 1.

### 2. El otro killer: el payback

¿Cuántos meses tardas en recuperar esos $290?

`Payback = CAC / Contribución mensual = 290 / 24.5 = 11.8 meses`

Tardas 11.8 meses en recuperar la inversión en un cliente que en promedio solo dura 12.5 meses. Lo recuperas justo antes de que se vaya.

### 3. Qué pasa si metes los $10,000 este mes

$10,000 / $290 = **~34 clientes nuevos**

Mes 1 te generan: 34 x $24.5 = ~$845 de margen bruto.

Si los sigues en el tiempo con ese churn del 8%, toda esa cohorte te va a generar en TODA su vida:
34.5 x $306.25 = **$10,560**

Gastaste $10,000 upfront para ganar $10,560 en bruto durante los próximos 1-2 años. Beneficio bruto de $560, antes de sueldos, herramientas, soporte para esos 34 clientes, y sin contar el valor del dinero en el tiempo.

Eres rentable ahora, pero escalar así te hace no rentable y te crea un bache de caja de casi un año.

### Para que SÍ pudieras escalar necesitarías:

Para LTV/CAC = 3, con tu LTV de $306, tu CAC máximo sería:
`306.25 / 3 = $102`

Tu CAC de $290 es casi 3x más caro de lo permitido.

O al revés, para soportar un CAC de $290 a ratio 3, necesitarías un LTV de $870. Eso implicaría, por ejemplo:
* Bajar churn de 8% a **~2.8% mensual**, o
* Subir precio de $35 a **~$99** con mismo churn y margen

No escales paid. Primero arregla churn o CAC. Con $35/mes y 8% de churn, este negocio no se escala con CAC de $290.

¿Quieres que modelemos qué churn + CAC necesitarías para que esos $10k sí tengan sentido?