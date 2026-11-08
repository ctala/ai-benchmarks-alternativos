# Muse Spark 1.3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.53 | quality: 10.0
- latency_total: 20.961s | tokens_per_second: 137.6
- input_tokens: 203 | output_tokens: 2884

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

Eres rentable ahora porque tu CAC actual debe ser bajo. Con este CAC pagado de $290, escalar te destruye. Tienes 3 errores encadenados:

### 1. Tu vida útil no es 2 años

Con churn mensual de 8%, la vida promedio es:

**Vida = 1 / churn = 1 / 0.08 = 12.5 meses**

No 24 meses. 24 meses implicaría un churn de ~4.2% mensual, casi la mitad del tuyo.

Para que lo veas: con 8% mensual, después de 12 meses solo te queda el (0.92)^12 = **36.8%** de la cohorte. Después de 24 meses, solo el 13.5%.

### 2. Tu LTV olvidó el margen bruto

Calculaste: 35 x 24 = $840

La fórmula correcta es:

**LTV = ARPU x Margen Bruto x Vida**

LTV correcto = 35 x 0.70 x 12.5 = **$306.25**

Tu cálculo:
- usó el doble de vida útil
- usó $35 de ingreso en vez de $24.5 de margen ($35 x 70%). Infraestructura y Stripe también se pagan.

Tu LTV real es casi 1/3 del que crees. Y sin descontar a valor presente, así que $306 ya es el caso optimista.

### 3. 2.9 no es "por encima de 3 más o menos"

840 / 290 = 2.90. Eso está *por debajo* de 3.

Pero con los números corregidos es peor:

**LTV/CAC real = 306.25 / 290 = 1.06**

No tienes 2.9x. Tienes 1.06x.

Regla: necesitas >3 para cubrir salarios, overhead, fallos, y ganar dinero. Con 1.06, por cada $290 que metes, recuperas $306 en margen bruto en *toda* la vida del cliente. Te quedan $16 para todo lo demás.

Y el payback lo confirma:

**Payback CAC = CAC / margen mensual = 290 / (35 x 0.70) = 290 / 24.5 = 11.8 meses**

Tardas casi 12 meses en recuperar lo que pagaste por el cliente, pero tu cliente promedio solo vive 12.5 meses. La mayoría se va antes de que los recuperes.

### Qué pasa si metes los $10,000 este mes

$10,000 / $290 = ~34.5 clientes

Margen bruto esperado en toda su vida: 34.5 x $306.25 = ~$10,560

Gastas $10,000 hoy en cash para recuperar $10,560 a cuentagotas durante el próximo año. Ganancia bruta de ~$560 antes de sueldos y gastos. Es una trampa de caja.

**Veredicto: NO.**

### Qué necesitarías para que SÍ funcione con ese CAC

Para LTV/CAC = 3 con tu LTV de $306:

**CAC objetivo máximo = 306.25 / 3 = ~$102**

Estás pagando casi 3x de más.

O, manteniendo CAC de $290, necesitarías:

Churn objetivo: 24.5 / (290 x 3) = **2.8% mensual**, no 8%.
Precio objetivo: **~$99/mes**, no $35.

Tienes 3 palancas: bajar CAC, bajar churn, subir precio/margen. Con 8% de churn mensual, paid a $290 no es escalable.

No escales. Prueba con $500-$1,000, mide CAC real y churn de cohorte pagada (suele ser peor), y ataca retención primero.