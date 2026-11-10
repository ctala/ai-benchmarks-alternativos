# Muse Ember — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meta/muse-ember`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 7.46s | tokens_per_second: 388.1
- input_tokens: 203 | output_tokens: 2895

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

No le des. Con tus propios números, ese plan pierde dinero — o gana tan poco que cualquier variación te deja en negativo.

Tu cálculo tiene 3 errores que se multiplican:

### 1. La vida útil no es 24 meses

Con un churn mensual del 8%, la vida media esperada es:

**1 / 0,08 = 12,5 meses**

No 24. De hecho, después de 12 meses solo te queda el 36,8% de los clientes (0,92^12), y después de 24 meses solo el 13,5%.

24 meses de vida implicarían un churn de ~4,2%, la mitad del tuyo.

### 2. El LTV no es ingresos, es margen

Un cliente no te deja $35/mes, te deja $35 x 70% = **$24,50/mes** después de infraestructura y pagos. Todavía falta soporte, salarios, impuestos, etc.

**LTV correcto = Precio x Margen x Vida útil**
**LTV = 35 x 0,70 x 12,5 = $306,25**

No $840. Tu cálculo usó ingresos brutos y una vida útil duplicada.

### 3. 2,9 no está "por encima de 3"

840 / 290 = 2,89. Está por debajo, y con el cálculo correcto ni siquiera llega a eso.

### El número real

**LTV / CAC = 306 / 290 = 1,06**

Por cada $1 que metes en publicidad, esperas recuperar $1,06 en margen bruto *durante los próximos 12,5 meses*. Antes de pagar sueldos, oficinas y todo lo que no está en ese 70%.

Y el payback es brutal:

**CAC / Margen mensual = 290 / 24,50 = 11,8 meses**

Tardas casi toda la vida del cliente en recuperar lo que invertiste en adquirirlo.

### Qué significa meter $10.000 este mes

10.000 / 290 = **34 clientes**

Margen bruto esperado de esa cohorte: 34 x 306 = **$10.560**
Beneficio esperado: **~$560 en 12 meses**, si todo sale perfecto.

Si el CAC sube un 10% al escalar (lo normal), a $319, ya pierdes dinero. Si el churn es 10% en vez de 8% un mes malo, LTV cae a $245 y también pierdes.

No es un negocio de escala, es una ruleta con margen de seguridad cero.

### Qué necesitarías para escalar con publicidad pagada

Para un LTV/CAC = 3 con tu CAC de $290, necesitarías una de estas tres cosas:

1.  **CAC de $102 o menos** (306 / 3). Tu canal actual está a casi 3x de eso.
2.  **Churn de 2,8% mensual** (en vez de 8%). A 4% tu LTV sería $612 y el ratio 2,1, todavía corto.
3.  **Precio de ~$99/mes** (en vez de $35) manteniendo churn y CAC.

Ninguna es un ajuste menor.

**Veredicto:** No metas $10.000. Si hoy eres rentable, es probablemente porque tu adquisición orgánica es barata. La publicidad pagada a $290 te destruye la rentabilidad.

Primero ataca churn o consigue un canal con CAC < $100. Escalar un ratio de 1,06 solo acelera la velocidad a la que te quedas sin caja.