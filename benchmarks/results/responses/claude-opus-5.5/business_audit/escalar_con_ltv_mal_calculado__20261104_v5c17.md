# Claude Opus 5.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.15 | quality: 10.0
- latency_total: 21.398s | tokens_per_second: 94.2
- input_tokens: 297 | output_tokens: 2015

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

# No le des todavía: con estos números el plan apenas sale tablas

Hay tres errores en el cálculo, y juntos cambian la conclusión.

## 1. La vida del cliente no es 24 meses

Con churn mensual del 8%, la vida media es:

**1 / 0,08 = 12,5 meses**, no 24.

## 2. El LTV se calcula sobre margen, no sobre ingreso

El 30% de cada pago se va en infraestructura y procesador. Lo que te queda para recuperar el CAC es el margen bruto:

- Margen bruto mensual por cliente: $35 × 0,70 = **$24,50**
- LTV = $24,50 × 12,5 = **$306**

## 3. El ratio real es 1,06, no 2,9

**LTV/CAC = $306 / $290 ≈ 1,06**

Además, 2,9 no está por encima de 3. Pero aun aceptando tu cifra, el número correcto está muy lejos de ese umbral.

## Qué pasa con los $10.000

- Clientes adquiridos: $10.000 / $290 ≈ **34**
- Margen bruto que generarán en toda su vida: 34 × $306 ≈ **$10.560**
- Ganancia neta: **unos $560**, sin descontar el valor del dinero en el tiempo ni contar soporte, onboarding o reembolsos.

El problema de caja es aún peor. Pagas los $10.000 hoy, y como los clientes se van yendo al 8% mensual, recuperarlos tarda mucho:

- A los 12 meses cada cliente te ha dejado unos $194 de margen, menos que los $290 que costó.
- Recuperar el CAC completo toma **unos 35 meses**.

Siendo realistas, estarías inmovilizando caja casi 3 años para ganar casi nada. Si el CAC sube al escalar, que es lo habitual cuando agotas las audiencias baratas, pierdes dinero.

## Qué tendría que cambiar para que tenga sentido

Para llegar a LTV/CAC = 3 necesitas un LTV de unos $870. Cualquiera de estas palancas, o una combinación, te acerca:

| Palanca | Valor necesario (moviendo solo esa) |
|---|---|
| Churn | Bajar de 8% a **~2,8%** mensual |
| CAC | Bajar de $290 a **~$100** |
| Precio | Subir a **~$100/mes** (con churn y margen iguales) |

El churn es la palanca más potente. Bajarlo al 4% ya duplica el LTV, a unos $612, y deja el ratio en ~2,1.

## Recomendación

1. **No metas los $10.000 este mes.** Si quieres aprender, prueba con $1.000–2.000 y mide el CAC real por canal y el churn de *esa cohorte*. Los clientes de publicidad suelen tener más churn que los orgánicos.
2. **Ataca el churn primero.** Averigua por qué se va el 8% cada mes: entrevistas de salida, análisis de en qué mes se van, activación del onboarding.
3. **Ofrece un plan anual con descuento.** Por ejemplo, 2 meses gratis cobrados por adelantado. Cobras el CAC de inmediato y reduces el churn de esos clientes.
4. **Revisa el precio.** A $35/mes con churn alto, el espacio para pagar adquisición es muy estrecho.

Que ya seas rentable es buena señal, pero tu rentabilidad actual probablemente viene de canales con CAC casi cero. La publicidad pagada es otro negocio, y hoy los números no lo sostienen.