# Grok 4.7 — business_audit/churn_mezcla_free_y_pago

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.24 | quality: 10.0
- latency_total: 30.957s | tokens_per_second: 49.3
- input_tokens: 1404 | output_tokens: 1527

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

El 31% es real, pero no mide lo que creías. Es el churn de toda la base, y casi todo el número lo ponen los gratuitos.

**Qué población está midiendo el panel**

62 / 200 = 31%. El cálculo es correcto si el denominador es “usuarios al inicio del mes”, gratis y de pago juntos. No es un error de fórmula. Es una métrica mezclada.

| Población | Base | Bajas | Churn |
|---|---:|---:|---:|
| Todos | 200 | 62 | 31% |
| Gratuitos | 178 | 60 | 33,7% |
| De pago | 22 | 2 | 9,1% |

El 97% de las bajas (60 de 62) son del plan gratuito. Los de pago son el 11% de la base y solo 2 bajas.

**Qué tan grave es**

- Como emergencia de ingresos, no. El 31% no es tu churn de pago.
- Como churn de pago, sí hay que mirarlo, pero con la muestra que tienes no puedes concluir que “pasaste de 5% a 9%”. Con 22 cuentas, 2 bajas dan un intervalo muy ancho: 9% es compatible con ruido. Una baja de más o de menos mueve el porcentaje varios puntos.
- El problema estable y grande está en gratuitos: ~34% en un mes. Eso importa si el gratis es tu canal de adquisición, no si solo miras facturación.
- No compares el 31% con el 5% hasta reconstruir el 5% con la misma definición (¿solo pago?, ¿logo o revenue?, ¿misma ventana?). Lo más probable es que el 5% fuera otra población.

Sin MRR, motivo de baja y antigüedad no se puede decir si esas 2 cuentas de pago duelen o no.

**Plan**

1. Hoy: no actúes sobre el 31% (no descuentos masivos, no cambio de pricing, no “todos se están yendo”).
2. Separa el panel en tres números fijos: churn de pago, churn gratuito y, cuando tengas importes, churn de ingresos. El de “todos” puede existir, pero no como KPI de retención.
3. Abre las 2 bajas de pago: plan, MRR, antigüedad, motivo, si cancelaron o solo dejaron de pagar, y si hubo ticket previo. Con n=22, el trabajo es caso a caso, no una campaña.
4. Reconstruye la serie del “5%” con el mismo corte (solo pago, inicio de mes, misma regla de baja). Si el histórico de pago sigue cerca del 5%, no hubo deterioro; hubo un cambio de definición en el panel.
5. En gratuitos, no trates el 34% como churn de clientes. Mide activación: % que llega al hábito en los primeros 7–14 días y % que pasa a pago. Ahí está la palanca, no en “retener” cuentas que nunca pagaron.
6. Documenta la definición en el panel: población, momento del corte y qué cuenta como baja. Si no, el mes que viene vuelves a comparar peras con manzanas.

Prioridad: las 2 cuentas de pago y alinear la definición. El 31% explica el susto; no explica el negocio.