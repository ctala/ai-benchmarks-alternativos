# Muse Spark 1.3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 19.719s | tokens_per_second: 148.7
- input_tokens: 202 | output_tokens: 2932

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

No le des. Tu plan muere en la aritmética.

No tienes un LTV/CAC de 2,9. Tienes uno de **1,06**. Y 2,9 tampoco estaría "por encima de 3 más o menos".

Vamos a recalcular:

### 1. Tu cálculo vs. el real

**Tu cálculo:**
Vida = 24 meses (?) -> LTV = 35 x 24 = $840 -> 840 / 290 = 2,9

Dos errores:

**Error 1: La vida no es 2 años.**
Con churn mensual de 8%, la vida esperada es:

Vida = 1 / churn = 1 / 0,08 = **12,5 meses**

No 24. Con 8% mensual, después de 24 meses solo te queda el 13,5% de la cohorte: `0,92^24 = 13,5%`. No es que el cliente promedio se quede 2 años.

**Error 2: Te comiste el margen bruto.**
LTV no es Precio x Vida. Es Margen x Vida:

LTV = ARPU x Margen Bruto / Churn
LTV = 35 x 0,70 / 0,08 = 24,5 / 0,08 = **$306,25**

Tu LTV de $840 asume 100% de margen y el doble de vida.

Realidad:
LTV = $306,25
CAC = $290
**LTV/CAC = 306,25 / 290 = 1,06**

Para escalar con paid necesitas >3. Tú estás en 1. Apenas empatas, antes de sueldos, soporte, y todo lo demás.

### 2. El otro killer: el payback

¿Cuántos meses tardas en recuperar esos $290?

Payback = CAC / (ARPU x Margen) = 290 / (35 x 0,70) = 290 / 24,5 = **11,8 meses**

Tardas 11,8 meses en recuperar un cliente que en promedio dura 12,5 meses. Recuperas la inversión justo cuando se está yendo.

Si metes $10.000 este mes:
$10.000 / $290 = ~34 clientes nuevos
+ $1.190 de MRR, pero solo + ~$845/mes de margen bruto.

Vas a quemar $10.000 de caja hoy para recuperarlo gota a gota durante un año, ganando ~$560 en total en toda la vida de esa cohorte. Y si el churn del canal paid es peor que tu promedio (casi siempre lo es), pierdes dinero directamente.

Ser rentable hoy no importa. Esa es tu rentabilidad *actual*. La decisión marginal de paid es perdedora.

### 3. ¿Qué necesitarías para que sí funcione?

Para justificar un CAC de $290 con LTV/CAC = 3, necesitarías un LTV de $870.

Con tu precio de $35 y margen de 70%, eso es imposible solo con margen. Necesitarías:

CAC máximo viable = LTV / 3 = 306,25 / 3 = **~$102**

Tu CAC actual es casi 3x más caro de lo que aguantas. O:

Churn necesario = 24,5 / 870 = **2,8% mensual** (vs tu 8% actual)
O precio necesario = ~$100/mes (vs tus $35 actuales)

### Veredicto: NO

No metas los $10.000. Lo que sí haz:

1.  Test pequeño de $500-$1.000 y mide CAC y churn *de esa cohorte*, no tu promedio.
2.  Baja churn de 8% primero. 8% mensual es altísimo para escalar con paid. Necesitas <4-5%.
3.  Baja CAC a <$100 o sube ARPU con planes anuales, upsells, aumento de precio.

Escalar fuerte con estos números no te hace crecer, te hace comprar ingresos a pérdida.