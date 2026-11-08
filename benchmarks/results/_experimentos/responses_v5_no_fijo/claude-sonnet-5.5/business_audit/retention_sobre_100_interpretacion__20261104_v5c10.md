# Claude Sonnet 5.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 16.146s | tokens_per_second: 108.5
- input_tokens: 218 | output_tokens: 1752

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, no es correcto, y la lectura que haces es justo la peligrosa.

**Qué mide realmente el 114%**

La retención neta de ingresos (NRR) toma los ingresos de los clientes que tenías al inicio del periodo y calcula cuánto facturan ahora, sumando upgrades y restando bajas y downgrades. Un 114% significa que **ese grupo factura un 14% más que antes**, no que no se vaya nadie. Es una métrica de dinero, no de personas.

**Lo que dicen tus datos**

- Pasaste de 40 a 36 clientes: **perdiste al menos 4, un 10% de tus clientes en un mes**. Si captaste alguno nuevo en ese tiempo, las bajas son más de 4.
- La retención de clientes nunca supera el 100%. La tuya es como mucho un 90%.
- Un 10% mensual es un churn muy alto. Si se mantuviera, al cabo de un año conservarías solo ~28% de tus clientes actuales (0,9¹² ≈ 0,28).

El 114% convive con esto porque los upgrades de unos pocos clientes están tapando las bajas. Ilustrativo, suponiendo que todos pagan lo mismo (100 €): empiezas con 4.000 € de MRR, pierdes 400 € por las bajas, y para llegar a 4.560 € los 36 restantes tendrían que aportar ~960 € de expansión, es decir, subir de media ~27%. Eso suele significar pocas cuentas muy expandidas.

**Por qué no deberías volcarte solo en captación**

1. **Cubo con fugas.** Cada cliente nuevo cuesta dinero (CAC) y estás perdiendo clientes a un ritmo que te obliga a reponer constantemente.
2. **La expansión se agota.** Menos clientes significa menos base que pueda subir de plan. El NRR puede caer rápido cuando los que expanden ya estén en el plan máximo.
3. **Riesgo de concentración.** Si tu NRR depende de 3-4 cuentas, que una de ellas se vaya te cambia el número de golpe.
4. **Las bajas pueden ser un síntoma.** Si se van clientes de ciertos segmentos, canales o planes, quizá hay un problema de producto o de encaje con el cliente que los nuevos heredarán.

**Qué mirar antes de decidir**

- **GRR (retención bruta de ingresos):** igual que el NRR pero sin contar expansión, con tope en 100%. Es la métrica que te muestra el churn real en dinero.
- **Churn de logos** por mes, y por cohorte, plan y canal de adquisición.
- **Quién se fue:** ¿clientes pequeños o grandes? ¿recién llegados o antiguos? ¿Motivo?
- **Concentración de la expansión:** qué porcentaje del upgrade viene de los 3 mayores.
- **Periodo del NRR:** confirma si tu panel lo calcula mensual, trimestral o anual, porque un 114% mensual y uno anual son realidades muy distintas.

En resumen: el NRR de 114% es una buena señal sobre el valor que captas de tus clientes que se quedan, pero no te autoriza a ignorar el churn. Con un 10% de bajas en un mes, retención y captación deberían avanzar a la par.