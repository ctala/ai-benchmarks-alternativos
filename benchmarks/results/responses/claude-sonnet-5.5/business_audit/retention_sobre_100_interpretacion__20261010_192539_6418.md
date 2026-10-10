# Claude Sonnet 5.5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 7.07 | quality: 8.0
- latency_total: 14.496s | tokens_per_second: 114.6
- input_tokens: 218 | output_tokens: 1662

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, la lectura correcta es bastante menos favorable.

**Qué mide realmente el 114%**

La retención neta de ingresos (NRR) compara los ingresos actuales de la cohorte que ya tenías con los que generaba antes, e incluye upgrades, downgrades y cancelaciones. Un 114% significa que lo que ganas por expansión supera lo que pierdes por churn y contracción. No dice que no se vaya nadie. Y no mide retención de clientes: esa no puede superar el 100%.

**Tu caso**

- Pasaste de 40 a 36 clientes: **10% de churn de clientes en un mes** (asumiendo que no entraron nuevos; si entraron, el churn real es aún mayor).
- Si se mantuviera ese ritmo, perderías más de la mitad de tus clientes en un año.
- El 114% solo te dice que los 36 restantes pagan bastante más que antes. Un ejemplo: si tus 40 clientes pagaban 100 € cada uno (4.000 €), perder 4 son 400 €, y para llegar al 114% (4.560 €) los 36 restantes tendrían que haber aumentado su gasto un ~27% de media.

**Por qué es un riesgo**

1. **La expansión tiene techo.** Un cliente solo puede subir de plan hasta cierto punto. Perder clientes es una fuga permanente; la expansión no es infinita.
2. **Concentración.** Con una base de 36, si el NRR depende de dos o tres cuentas grandes que subieron, una sola salida puede romper la métrica.
3. **Captar sobre un cubo con fugas.** Cada cliente nuevo cuesta CAC; si 1 de cada 10 se va al mes, tu payback se deteriora y gastas mucho para mantenerte en el mismo sitio.
4. **Posible problema de producto o de segmento.** Que unos suban y otros se vayan sugiere que el producto encaja muy bien con un perfil y mal con otro.

**Qué mirar antes de decidir**

- **Retención bruta de ingresos (GRR):** igual que el NRR pero sin expansión. Máximo 100%. Es la métrica que muestra la fuga real.
- **Churn de clientes (logo churn)** por cohorte y por plan.
- **Perfil de los 4 que se fueron:** tamaño, antigüedad, motivo, canal de origen. ¿Son clientes pequeños o recién captados?
- **Distribución de la expansión:** ¿cuántos clientes generan el grueso del upgrade?
- **Periodo del 114%:** ¿es mensual, trimestral o anual? Si es mensual, es excepcional y probablemente poco sostenible; si es anual, la diferencia con el 10% mensual de churn es todavía más llamativa.

**Conclusión:** tienes una buena señal (los clientes que se quedan crecen), pero también una alerta clara en retención de clientes. Yo no desviaría el esfuerzo a adquisición hasta entender por qué se fueron esos 4 y comprobar que el GRR es aceptable. Lo razonable es hacer ambas cosas, con prioridad a diagnosticar el churn.