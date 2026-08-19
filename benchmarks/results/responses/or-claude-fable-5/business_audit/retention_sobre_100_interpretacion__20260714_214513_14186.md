# Claude Fable 5 — business_audit/retention_sobre_100_interpretacion

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.94 | quality: 10.0
- latency_total: 21.475s | tokens_per_second: 49.8
- input_tokens: 216 | output_tokens: 1070
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una interpretación completa y práctica de la retención de ingresos por encima del 100%.

## Respuesta completa

No, y de hecho tus propios números demuestran lo contrario. Vamos por partes.

## Qué mide realmente ese 114%

Ese dato es **retención neta de ingresos (NRR)**: compara los ingresos que generan hoy los clientes que ya tenías, frente a lo que generaban antes. Puede superar el 100% porque las **expansiones** (upgrades, más asientos, add-ons) compensan —y en tu caso, superan— lo perdido por bajas y downgrades.

No mide cuánta gente se queda. Para eso está la **retención de clientes (logo retention)**.

## Tu retención de clientes real

- Mes pasado: 40 clientes
- Este mes: 36 clientes
- **Retención de logos: 90% → churn del 10% mensual**

Un 10% de churn *mensual* es muy alto. Anualizado de forma simple, si mantuvieras ese ritmo, perderías más de dos tercios de tu base en un año (0,90¹² ≈ 28% de retención anual). El 114% de NRR no te está diciendo que no se va nadie: te está diciendo que **los que se quedan gastan bastante más, y eso tapa el agujero**.

## Por qué esto es un riesgo, no una tranquilidad

1. **Concentración**: tus ingresos dependen cada vez más de menos clientes. Si uno de los que hizo upgrade se va el mes que viene, el golpe es doble.
2. **La expansión tiene techo**: los clientes no suben de plan indefinidamente. El churn de logos, en cambio, sí puede sostenerse mes tras mes.
3. **Coste de adquisición**: con 10% de churn mensual, cada cliente nuevo que captes tiene una vida media corta. Estás llenando un cubo con agujeros; captar más solo acelera el desgaste del CAC.
4. **Muestra pequeña**: con 40 clientes, un solo upgrade grande puede inflar el NRR. Ese 114% es un dato frágil, no una tendencia consolidada.

## Qué haría yo

- **Sigue ambos números por separado**: NRR y retención de logos. Nunca uno como proxy del otro.
- **Investiga las 4 bajas**: ¿fueron cuentas pequeñas que no encajaban (churn "sano") o clientes que se frustraron? La respuesta cambia todo.
- **Segmenta el NRR**: ¿la expansión viene de 1-2 cuentas o está distribuida?
- **No abandones la captación**, pero el churn del 10% mensual es tu problema prioritario, no algo resuelto.

En resumen: el 114% es una buena noticia sobre *monetización* de tu base, pero tu *retención de clientes* está en 90% mensual y eso, sin corregirse, se come cualquier esfuerzo de captación.