# Claude Fable 5.2 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 6.63 | quality: 8.0
- latency_total: 22.078s | tokens_per_second: 83.2
- input_tokens: 264 | output_tokens: 1837

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de retención. Antes de interpretar una métrica, verificas qué población está midiendo realmente.

**user:**

Estoy en pánico. Mi plataforma reporta un churn del 31% este mes y pensé que estaba en 5%. ¿Qué hago?

Datos que me da el panel:
- Usuarios totales que se dieron de baja este mes: 62
- Usuarios totales a inicio de mes: 200
- Churn reportado: 31%

Detalle que encontré exportando la tabla:
- De los 200 usuarios, 178 están en el plan gratuito y 22 son de pago.
- De las 62 bajas, 60 eran del plan gratuito y 2 eran de pago.

¿Qué tan grave es? Dame un plan.


## Respuesta completa

**Tu 31% es casi todo plan gratuito. El churn de pago, que es el que afecta a tus ingresos, es del 9,1%.**

| Segmento | Bajas | Base | Churn |
|---|---|---|---|
| Gratuito | 60 | 178 | 33,7% |
| De pago | 2 | 22 | **9,1%** |
| Mezclado (lo que reporta el panel) | 62 | 200 | 31% |

El panel mezcla dos poblaciones muy distintas, y como el 89% de tu base es gratuita, el número agregado refleja básicamente su comportamiento.

## Qué tan grave es

**En pago, no puedes saberlo todavía.** El 9,1% es más que el 5% que esperabas, pero con 22 clientes cada baja pesa 4,5 puntos: una baja sería 4,5% y dos son 9,1%. La diferencia entre lo esperado y una mala señal es literalmente un cliente. Un 9% mensual sostenido sí sería preocupante, porque perderías cerca de dos tercios de la base al año, pero un solo mes con esta muestra no lo demuestra.

**En gratuito, depende de qué signifique "baja".** Un 33,7% parece alto, pero en planes gratuitos es habitual que mucha gente se registre, pruebe y se vaya. Solo importa si esos usuarios eran candidatos reales a convertirse a pago.

## Qué verificar primero

1. **De dónde salía tu 5%.** Si antes mirabas solo clientes de pago, u otro periodo, puede que nada haya empeorado y solo estés viendo otra métrica.
2. **Cómo define el panel "baja" en gratuito.** No es lo mismo una cuenta eliminada por el usuario que una marcada por inactividad o una purga automática.
3. **Si pasó algo puntual este mes.** Por ejemplo, una limpieza de cuentas inactivas, el fin de una promoción, un cambio en el plan gratuito o registros basura de una campaña.
4. **El historial de bajas de pago de los últimos 6 a 12 meses.** Si sueles tener 0 o 1 al mes, 2 es ruido. Si vienes de 0 sostenido, vale la pena mirar.

## Plan

**Esta semana**
- Habla con los 2 clientes de pago que se fueron. Con 22 clientes, puedes saber exactamente por qué se fue cada uno.
- Calcula el churn en ingresos (MRR perdido sobre MRR inicial). Si los dos tenían el plan más barato, el impacto es menor que el 9%. Si uno era tu cuenta más grande, es mayor.
- Resuelve los cuatro puntos de verificación.

**Este mes**
- Separa el reporte por plan y no vuelvas a usar el churn mezclado para decidir.
- Para pago, usa una ventana móvil de 3 meses, porque con 22 clientes el dato mensual salta demasiado.
- Para gratuito, revisa si las 60 bajas llegaron a usar el producto. Si nunca se activaron, el problema es de activación u onboarding, no de retención.

**Cuándo preocuparte de verdad**
- Si el churn de pago se mantiene en 2 o más bajas al mes durante 2 o 3 meses seguidos.
- Si las dos bajas comparten causa (precio, una función que falta, un competidor).
- Si la conversión de gratuito a pago está cayendo a la vez.

Si me pasas el historial mensual de bajas de pago y la definición de "baja" que usa el panel, te ayudo a afinar el diagnóstico.