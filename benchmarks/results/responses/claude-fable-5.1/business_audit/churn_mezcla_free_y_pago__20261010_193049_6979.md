# Claude Fable 5.1 — business_audit/churn_mezcla_free_y_pago

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 24.315s | tokens_per_second: 62.2
- input_tokens: 264 | output_tokens: 1512

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

Respira. Antes de hacer nada, mira qué está midiendo ese 31%: mezcla dos poblaciones que se comportan de forma completamente distinta.

**Desglose real**

| Segmento | Usuarios inicio | Bajas | Churn |
|---|---|---|---|
| Gratuito | 178 | 60 | 33,7% |
| Pago | 22 | 2 | 9,1% |
| **Total (lo que ves)** | 200 | 62 | 31,0% |

El 31% es matemáticamente correcto pero casi todo es churn gratuito. El 89% de tu base es free, así que el promedio ponderado te cuenta la historia de los usuarios gratuitos, no la de tu negocio.

**Qué tan grave es, por partes**

1. **Churn de pago: 9,1%, no 5%.** Esto sí merece atención, pero con matices. Con 22 clientes, cada baja mueve el número 4,5 puntos. Un mes con 1 baja = 4,5%; con 2 bajas = 9,1%. La diferencia entre "lo que pensabas" y "lo que es" es literalmente **una persona**. No puedes distinguir señal de ruido con una muestra así en un solo mes.

2. **Churn gratuito: 33,7%.** Normal en freemium. Muchos usuarios free se registran, prueban una vez y desaparecen. No es "pérdida de clientes", es parte del embudo. Lo que importa de este segmento es otra cosa: ¿cuántos convierten a pago antes de irse?

**Plan**

*Esta semana:*
- Separa el dashboard en dos métricas: churn de pago y churn/inactividad de free. Nunca más mires el agregado.
- Habla con los 2 clientes de pago que se fueron. Con n=2, una llamada te dice más que cualquier gráfica. Averigua: ¿fallo de cobro, falta de uso, cambio a competidor, cierre de empresa?
- Calcula churn de ingresos (MRR perdido / MRR inicial), no solo de cuentas. Si los 2 eran planes básicos, el impacto es menor que el 9,1% sugiere; si eran los más grandes, es peor.

*Este mes:*
- Reconstruye el churn de pago de los últimos 6–12 meses. Si históricamente ronda 1 baja/mes y este mes fueron 2, es ruido. Si venía en 0–1 y la tendencia sube, es señal.
- Define qué significa "baja" en free: ¿canceló cuenta o simplemente no entró en 30 días? Son cosas distintas y la segunda suele inflar el número.
- Mide la tasa free→pago. Si de 178 free convirtieron 3–4 este mes, los 60 que se fueron son el costo normal de ese embudo.

*Umbral de alarma:* si el churn de pago supera ~5–7% sostenido durante 3 meses consecutivos, ahí sí hay un problema de producto o de ajuste al mercado. Un mes aislado al 9% con 2 personas no lo es.

**Resumen:** no tienes un problema de churn del 31%. Tienes una métrica mal construida y un mes de churn de pago ligeramente alto que necesita dos llamadas y seis meses de contexto para interpretarse.