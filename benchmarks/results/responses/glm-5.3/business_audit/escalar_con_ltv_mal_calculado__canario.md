# GLM 5.3 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.19 | quality: 10.0
- latency_total: 81.316s | tokens_per_second: 91.1
- input_tokens: 206 | output_tokens: 7411

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

# No le doy. Y no es por prudencia: tu LTV está inflado casi 3x.

Hay tres errores en tu cálculo, y cada uno solo empeora las cosas.

## Error 1: La vida del cliente no son 24 meses

Con churn mensual del 8%, la vida esperada es **1/churn = 12,5 meses**, no 24. Los "2 años" no salen de tus números. Con 8% mensual, al mes 12 solo queda el 0,92¹² ≈ **37%** de una cohorte. El cliente *mediano* se va a los ~8,3 meses.

## Error 2: El LTV se calcula sobre margen, no sobre facturación

De los $35 no te quedan $35: te quedan **$24,50**. El resto se lo llevan infraestructura y el procesador.

**LTV correcto = 35 × 0,70 × 12,5 = $306.** (Descontando flujos futuros a ~1% mensual: ~$272.)

## Error 3: Menor, pero sintomático

2,9 no está "por encima de 3". Está por debajo. Pero da igual, porque el número real es otro:

$$LTV/CAC = 306 / 290 ≈ 1,05$$

No estás en 3x. Estás en **1x**: cada dólar en ads devuelve aproximadamente un dólar de margen… en más de un año. Antes de descontar, antes de costos de soporte, antes de que el CAC suba al escalar presupuesto.

## Los números que deberían frenarte

- **Payback:** 290 / 24,5 = **11,8 meses**
- **Vida mediana del cliente:** **8,3 meses**
- Traducción: el cliente típico genera ~$204 de margen contra $290 de CAC. **El cliente mediano pierde ~$86.** Solo ~1 de cada 3 clientes que compres sobrevive lo suficiente para pagarse. Toda la economía depende de la cola de los que se quedan años.

## Tu plan de $10.000, recalculado

~34 clientes. Margen esperado: ~$10.400 sin descontar, ~$9.250 descontado. Inmovilizas $10.000 hoy para recuperar, *con suerte*, lo mismo en 12–18 meses. Y con dos supuestos generosos:

- El churn del 8% probablemente es *blended* con tráfico orgánico. El tráfico pagado suele retener peor. Si esa cohorte churnea al 10–12%, el LTV cae a $204–245 y pasas a pérdida neta por cliente.
- El CAC de $290 rara vez está *fully loaded* (creativos, herramientas, tiempo tuyo) y rara vez se mantiene al escalar.

## Qué tendría que cambiar para dártelo

| Palanca | Hoy | Necesitas para 3x |
|---|---|---|
| Churn mensual | 8% | ~2,8% |
| CAC | $290 | ~$102 |
| ARPU | $35 | ~$99 |

Cualquiera de las tres es un proyecto. Pero nota cuál es la más barata: **cada punto de churn que bajas vale ~$44 de LTV (+14%)**. Ir de 8% a 5% lleva el LTV a $490 sin tocar CAC ni precio.

## Mi recomendación

1. **No metas $10.000.** Mete $1.500–2.000 como prueba, con tracking de churn por cohorte (pagada vs. orgánica) durante 90 días. Ese dato vale más que el gasto completo.
2. Mientras tanto, trabaja retención: onboarding, activación, plan anual. Es la palanca con más apalancamiento que tienes.
3. Una pregunta incómoda: dices que ya eres rentable. ¿Con clientes orgánicos baratos? La rentabilidad de tu base actual no dice nada sobre la economía marginal del tráfico pagado. Son dos negocios distintos.

Tu plan no muere por asumir "2 años". Muere porque con 8% de churn mensual estás comprando clientes que, en promedio, apenas se pagan. Y la mitad ni eso.