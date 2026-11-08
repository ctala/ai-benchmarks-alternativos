# Claude Opus 5.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 21.448s | tokens_per_second: 98.8
- input_tokens: 297 | output_tokens: 2119

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

# No le des todavía: los números no cierran

Tu cálculo tiene tres errores, y juntos cambian completamente la conclusión.

## Los tres errores

**1. Con 8% de churn, un cliente no se queda 2 años.**
La vida media es **1 / churn = 1 / 0,08 = 12,5 meses**, no 24. Algunos clientes durarán 2 años o más, pero el promedio es 12,5.

**2. El LTV se calcula sobre margen, no sobre ingreso.**
De cada $35 te quedan $24,50 (70%). El CAC lo pagas con margen, no con facturación.

**3. 2,9 no está "por encima de 3".** Es un detalle menor, pero importa si usas 3 como umbral.

## El recálculo

| Concepto | Tu cálculo | Corregido |
|---|---|---|
| Vida media del cliente | 24 meses | 12,5 meses |
| Valor mensual | $35 (ingreso) | $24,50 (margen) |
| **LTV** | $840 | **$306** |
| **LTV/CAC** | 2,9 | **1,06** |

Con un ratio de 1,06, cada dólar en publicidad te devuelve aproximadamente un dólar a lo largo de toda la vida del cliente. Es casi equilibrio, antes de contar sueldos, herramientas y tu tiempo.

## El problema de caja

Los clientes se van cayendo mes a mes. Si se tiene en cuenta ese churn, una cohorte tarda **unos 35 meses** en devolverte el CAC.

Simulación de tus $10.000:

- **Clientes adquiridos:** 10.000 / 290 ≈ 34 clientes
- **Margen acumulado a 12 meses:** ≈ $6.700, así que **sigues $3.300 abajo**
- **Margen total en toda su vida:** ≈ $10.560, es decir, **unos $560 de ganancia en ~3 años**

Inmovilizas $10.000 durante casi tres años para ganar $560. Eso suponiendo que el CAC se mantiene en $290 al escalar, y casi nunca se mantiene: cuando subes presupuesto, agotas primero a la audiencia más barata.

## Qué tendría que cambiar para que funcione

Para llegar a un LTV/CAC de 3, necesitas **una** de estas cosas, o una combinación:

| Palanca | Valor actual | Valor necesario |
|---|---|---|
| Churn mensual | 8% | **~2,8%** |
| Precio | $35 | **~$99** |
| CAC | $290 | **~$100** |

El churn es la palanca más potente: bajarlo de 8% a 4% duplica el LTV sin tocar nada más.

## Mi recomendación

1. **No metas los $10.000 este mes.**
2. **Trabaja primero el churn.** El 8% mensual es alto para una suscripción. Habla con los clientes que se fueron, revisa el onboarding y considera un plan anual con descuento.
3. **Si quieres probar publicidad, hazlo con $1.000–2.000** y mide dos cosas:
   - El CAC real a ese volumen.
   - El churn específico de los clientes que vienen por publicidad. Suele ser peor que el de los orgánicos, y si es así, el LTV real es aún menor que $306.
4. **Escala cuando el payback simple (CAC / margen mensual) baje de 12 meses.** Hoy está en 11,8 meses, prácticamente igual a la vida media del cliente. Eso significa que recuperas la inversión justo cuando el cliente se va.

Ser rentable hoy es una gran base. Pero esa rentabilidad probablemente viene de clientes que te llegan casi gratis. La publicidad pagada, con estos números, no la amplía: la diluye.