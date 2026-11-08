# Muse Glimmer 30B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.79 | quality: 10.0
- latency_total: 16.643s | tokens_per_second: 129.1
- input_tokens: 204 | output_tokens: 2148

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

No. Con esos números escalar con $10.000 ahora es quemar caja.

Tu cálculo tiene 3 errores que matan la unidad económica:

**1. La vida media no es 2 años con 8% de churn mensual**
Con churn mensual del 8% la retención es 92%.
Vida media esperada = 1 / churn = 1 / 0.08 = 12.5 meses

La probabilidad de que un cliente sobreviva 24 meses es 0.92^24 = 14%. No se queda 2 años, se queda 1 año.

**2. El LTV se calcula sobre margen bruto, no sobre facturación**
Precio $35/mes
Margen bruto 70% = $35 x 0.70 = $24.5 de contribución por mes

LTV correcto = Contribución mensual / churn mensual
LTV = $24.5 / 0.08 = $306

Si quieres usar tu horizonte de 24 meses:
LTV bruto = $35 x 24 = $840
LTV de margen = $840 x 0.70 = $588

**3. LTV/CAC real**
Con vida media real:
LTV / CAC = $306 / $290 = 1.05

Con tu horizonte de 24 meses optimista:
LTV / CAC = $588 / $290 = 2.03

En ningún caso llegas a 3. Y 2.9 que calculaste es sobre ingresos brutos, no sobre margen. Sobre ingresos el ratio es 840/290 = 2.9, sobre caja es 1.05.

**El problema de cash flow es peor**
Payback = CAC / Contribución mensual = $290 / $24.5 = 11.8 meses

Con 8% de churn mensual, solo el 36% de los clientes sobreviven 12 meses para pagarte el CAC. Estás recuperando el CAC justo cuando la mayoría ya se fue.

Con $10.000 de pauta:
Clientes nuevos ≈ 10.000 / 290 = 34-35 clientes
Contribución total esperada a lo largo de la vida = 35 x $306 = $10.710
CAC total = $10.000
Margen bruto total esperado = $710 antes de gastos fijos, soporte, etc.

Es decir, estás apostando $10.000 para ganar $710 en 12 meses, con cash flow negativo los primeros 11 meses.

**Regla mínima para escalar**
Para LTV/CAC = 3 con tu precio y margen necesitas:
Churn mensual ≤ 2.8%  -> 24.5 / churn = 870
O CAC ≤ $102 con churn 8%
O Precio / margen suficiente para bajar payback < 12 meses

Qué hacer antes de meter $10k:
1. No escales. Haz un test pequeño de $1-1.5k para validar CAC real por canal y cohorte.
2. Baja churn de 8% a <3-4% mensual. Ese es el mayor palanca. Con 4% churn tu LTV pasa a $613 y LTV/CAC a 2.1.
3. Revisa CAC. $290 es caro para $24.5/mes de contribución.
4. Calcula payback real por cohorte, no promedio teórico.

Con 8% de churn mensual tu modelo no soporta crecimiento con paid. Primero arregla retención o precio, después escalas.