# Claude Opus 5.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.82 | quality: 8.0
- latency_total: 14.92s | tokens_per_second: 93.6
- input_tokens: 218 | output_tokens: 1397

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

**No, no es correcto.** Ese 114% mide dinero, no clientes, y tus propios datos muestran una pérdida de clientes considerable.

## Qué significa ese 114%

Lo más probable es que tu panel muestre la **Retención Neta de Ingresos (NRR)**:

> NRR = (Ingresos iniciales de los clientes existentes − bajas − downgrades + upgrades) ÷ Ingresos iniciales de esos mismos clientes

Indica que **los clientes que ya tenías** generan hoy un 14% más de ingresos que antes. Las subidas de plan han compensado con creces el dinero perdido por quienes se fueron. Pero no dice nada de cuántas personas se quedaron.

## Tu retención de clientes real

| Métrica | Cálculo | Resultado |
|---|---|---|
| Retención de clientes (logos) | 36 ÷ 40 | **90%** |
| Churn de clientes mensual | 4 ÷ 40 | **10%** |

**La retención de clientes nunca puede superar el 100%**, porque no puedes conservar más clientes de los que tenías. Además, si este mes tienes 36, cualquier cliente nuevo que hayas captado significa que se fueron *más* de 4 de los 40 originales.

Un 10% de churn mensual es alto. Si se mantiene, al cabo de un año solo te quedaría alrededor del **28% de tus clientes actuales** (0,9¹² ≈ 0,28).

## Por qué no deberías dejar de preocuparte por el churn

1. **La expansión tiene techo.** Los upgrades no se repiten indefinidamente: un cliente que ya está en el plan más alto no puede subir más. El churn, en cambio, sigue actuando cada mes.
2. **Dependes de pocos clientes.** Si tus ingresos se concentran en los que subieron de plan, perder a uno o dos de ellos puede hundir la NRR de golpe.
3. **Captar es caro si el cubo está agujereado.** Con un 10% de churn mensual, buena parte de lo que gastes en adquisición se perderá en pocos meses. Tu coste de adquisición tarda en amortizarse y quizá no llegue a hacerlo.
4. **Las bajas son información.** Que se vayan clientes mientras otros suben de plan sugiere que tu producto encaja muy bien con un tipo de cliente y mal con otro. Conviene saber cuál es cuál.

## Qué revisaría

- **Que la NRR esté bien calculada.** Debe excluir los ingresos de clientes nuevos. Si los incluye, el 114% está inflado.
- **El periodo de la cifra.** Un 114% *mensual* sería excepcional y probablemente puntual. Un 114% *anual* es bueno, pero no se compara directamente con tu churn mensual del 10%.
- **Quién se fue y por qué.** Tamaño, plan, antigüedad y motivo de las bajas. Una breve encuesta o llamada de salida aporta mucho.
- **Quién subió de plan y qué tienen en común.** Ese es tu cliente ideal y debería orientar tu captación.

## Conclusión

Tu NRR del 114% es una buena señal: los clientes que se quedan valoran el producto y pagan más. Pero **pierdes 1 de cada 10 clientes al mes**, y eso es un problema serio. No elegiría entre retención y captación. Entendería primero por qué se van y usaría el perfil de los que suben de plan para captar mejor, no solo más.