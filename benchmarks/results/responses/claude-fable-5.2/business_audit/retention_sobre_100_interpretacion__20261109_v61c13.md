# Claude Fable 5.2 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 8.09 | quality: 10.0
- latency_total: 16.215s | tokens_per_second: 83.4
- input_tokens: 218 | output_tokens: 1352

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de SaaS. Explicas métricas con precisión, incluso cuando la lectura correcta es menos halagadora que la intuitiva.

**user:**

Mi panel dice: 'Retención de ingresos: 114%'.

Entiendo entonces que prácticamente no se me va nadie y que la retención de clientes está por encima del 100%. ¿Correcto? ¿Puedo dejar de preocuparme por el churn y meter todo el esfuerzo en captar gente nueva?

Contexto: el mes pasado tenía 40 clientes de pago y este mes tengo 36, pero varios subieron de plan.


## Respuesta completa

No, ninguna de las dos conclusiones es correcta. El 114% mide ingresos, no clientes, y tus propios datos muestran que sí se te va gente.

**Qué dice realmente el 114%**

La retención neta de ingresos compara lo que te pagan hoy los clientes que ya tenías con lo que te pagaban antes. Incluye las subidas de plan, así que puede superar el 100% aunque pierdas clientes. Eso es lo que te pasó: los que subieron de plan compensaron de sobra lo que dejaron de pagar los que se fueron.

**Lo que el 114% oculta**

- **Retención de clientes:** es de 36/40, un 90% como máximo. Nunca puede superar el 100%. Si entre los 36 hay algún cliente nuevo, perdiste más de 4 y la cifra real es peor.
- **Churn de clientes:** ronda el 10% en un mes. Si ese ritmo se mantuviera, en un año conservarías cerca del 28% de tu base actual (0,9^12). Con 40 clientes, un mes es poca muestra y puede ser ruido, pero no es una cifra para ignorar.

**Por qué no puedes olvidarte del churn**

- **La expansión tiene techo:** los clientes no pueden subir de plan indefinidamente, mientras que el churn se repite cada mes.
- **Te concentras:** dependes de menos clientes que pagan más, así que cada baja futura duele más.
- **Captar con fuga es caro:** si pierdes el 10% mensual, buena parte de lo que gastes en captación solo repone bajas.

**Qué haría yo**

1. Añadir al panel la retención bruta de ingresos (la que no cuenta las subidas de plan) y el churn de clientes. Confirma también si el 114% es mensual o de los últimos 12 meses, porque cambia mucho la lectura.
2. Averiguar por qué se fueron esos 4: qué plan tenían, cuánto llevaban y cómo llegaron. Si eran todos del mismo perfil, quizá estés captando clientes que no encajan.
3. Seguir captando, pero no con todo el esfuerzo hasta saber si ese 10% es puntual o una tendencia.

La buena noticia es real: que varios clientes suban de plan indica que quienes se quedan encuentran valor. Pero eso solo describe a los que se quedan.