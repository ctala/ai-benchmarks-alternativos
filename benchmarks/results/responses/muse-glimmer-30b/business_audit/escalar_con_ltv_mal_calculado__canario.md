# Muse Glimmer 30B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.65 | quality: 10.0
- latency_total: 33.162s | tokens_per_second: 62.3
- input_tokens: 204 | output_tokens: 2065

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

No. Con esos números escalar con $10.000 te va a quemar caja.

Tu cálculo de LTV está inflado en 2 ejes: usas ingresos brutos y asumes 24 meses de vida.

**La vida real con 8% de churn mensual**

Retención mensual = 1 - 0,08 = 0,92
Vida media = 1 / churn = 1 / 0,08 = 12,5 meses

No son 24 meses. Con 8% mensual el churn anual es 1 - 0,92^12 = 63,3%.

**LTV correcto**

Ingresos brutos por mes = $35
Margen de contribución por mes = $35 x 70% = $24,5

LTV de contribución = Margen mensual / churn = $24,5 / 0,08 = $306,25

LTV de ingresos brutos = $35 / 0,08 = $437,5

Con tu CAC de $290:

* LTV contribución / CAC = 306 / 290 = **1,06**
* LTV ingresos / CAC = 438 / 290 = **1,51**

Ni de lejos el 2,9 que calculaste. Y mucho menos el 3x que se pide para escalar.

**Payback y riesgo de caja**

Payback nominal = CAC / margen mensual = 290 / 24,5 = 11,8 meses

Con 8% de churn mensual la probabilidad de que un cliente sobreviva 12 meses es 0,92^12 = 36,7%. Solo ~37% llegan a pagar el CAC.

Con $10.000 de pauta a $290 CAC compras ~34 clientes.
Margen mensual esperado = 34 x $24,5 = $833
Necesitas ~12 meses para recuperar el cash, y en ese tiempo perderás ~63% de ellos.

El modelo es casi break-even en valor presente y negativo en cash flow.

**Para que sí valga escalar necesitas:**

* LTV/CAC >=3 con margen: CAC máximo = $306 / 3 = **$102**
* O bajar churn a ~3% mensual:  $24,5 / 0,03 = $817 LTV -> CAC viable de ~$272
* O subir precio/margen. Con churn 8% necesitas margen mensual de $290 x 0,08 x 3 = $69,6 -> precio ~ $99 con 70% de margen.

No metas los $10k ahora. Primero valida CAC real < $100 o churn < 4% mensual. Si no, estás comprando clientes que se van antes de pagarse.