# Muse Spark 1.2 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 18.42s | tokens_per_second: 163.0
- input_tokens: 188 | output_tokens: 3003

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

No le des. Con esos números escalar te hace perder dinero. Tu cálculo tiene 2 errores que te duplican el LTV.

Así mueren la mayoría de los planes de paid: en la aritmética.

### Tu cálculo vs. cálculo correcto

| Concepto | Tu cálculo | Cálculo correcto |
| :--- | :--- | :--- |
| **Vida promedio del cliente** | 24 meses [asumido] | **12.5 meses** = 1 / Churn = 1 / 0.08 |
| **LTV que usaste** | $840 = $35 x 24 | **$306.25** = $35 x 70% / 8% |
| **LTV/CAC** | 2.9 = 840 / 290 | **1.06** = 306.25 / 290 |

**Error 1: La vida del cliente no es 24 meses.**
Con un churn de 8% mensual, no se quedan 2 años en promedio. La fórmula es `Vida = 1 / churn`.

1 / 0.08 = 12.5 meses.

Para que se quedaran 24 meses, tu churn tendría que ser de 4.1%. Con 8% mensual, al mes 24 solo te queda el 13.5% de la cohorte inicial `0.92^24`.

**Error 2: El LTV no es sobre facturación, es sobre margen bruto.**
Tú cobras $35, pero no te quedan $35. Después de infra y pagos te quedan $24.50 `35 x 70%`. El LTV para comparar contra CAC siempre es sobre margen bruto.

LTV correcto = $24.50 / 0.08 = **$306.25**

> Incluso si usaras facturación, tu LTV sería $437.5 `35/0.08`, no $840. Y tu ratio de 2.9 ni siquiera es >3, es <3.

### El diagnóstico real:

**1. LTV/CAC = 1.06. Estás en zona de quiebra, no de escala.**
El estándar sano para SaaS es >3. Con 1.06, por cada $290 que metes, recuperas $306 en TODA la vida del cliente. Te quedan $16 de margen para pagar todo lo demás: salarios, soporte, impuestos, herramientas. Pierdes dinero.

Para que tu CAC de $290 fuera sano necesitarías:
* Un LTV de $870 `290 x 3` -> Eso exige un churn de **2.8%** mensual, no 8%.
* O bajar tu CAC a **$102** `306.25 / 3`.

**2. Payback de 11.8 meses. Te vas a quedar sin caja.**
`Payback = CAC / Margen mensual = 290 / 24.50 = 11.8 meses`

Tardas casi 12 meses en recuperar lo que pagaste por el cliente, y su vida promedio es de 12.5 meses. Estás financiando a tus clientes durante un año.

Si metes $10,000 hoy:
* Consigues ~34 clientes `10,000 / 290`
* Sumas +$1,190 de MRR, pero -$10,000 de caja el mes 1
* Necesitas 12 meses para recuperar esos $10,000. Y en esos 12 meses ya se te habrá ido la mitad de esos 34 clientes por el churn.

Ganancia total de esa cohorte en toda su vida: 34 x $306.25 = $10,412. Ganancia neta después de un año: **$412**. Un imprevisto y quedas en negativo.

### Veredicto: NO escales.

No metas $10,000.

**Qué hacer antes de escalar:**

1.  **No escales paid con 8% de churn mensual.** Es altísimo. 8% mensual = 64% anual. Primero obsesiónate con retención. Tienes que bajarlo a <5% mensual para que el modelo respire.
2.  **Baja el CAC o sube el precio.** Con tu margen actual, tu CAC máximo para un ratio de 3 es $102. Testea creativos, audiencias, landing, oferta anual prepago. O testea subir precio a $45-$49.
3.  **Si quieres testear, testea pequeño.** Máximo $1,000-$1,500 para validar si puedes bajar el CAC a ~$100. No $10,000 a ciegas.

Escalar con un LTV/CAC de 1.06 no es escalar, es acelerar la quema de caja.

¿Quieres que modelemos juntos qué churn o qué precio necesitarías para que ese CAC de $290 sí sea rentable?