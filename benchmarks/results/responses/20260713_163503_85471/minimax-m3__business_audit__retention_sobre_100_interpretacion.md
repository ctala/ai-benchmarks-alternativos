# MiniMax M3 — business_audit/retention_sobre_100_interpretacion

- model_id: `minimax/minimax-m3`
- success: True  | final: 6.91 | quality: 7.2
- latency_total: 15.114s | tokens_per_second: 115.9
- input_tokens: 284 | output_tokens: 1752
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una comprensión completa de la métrica NRR y sus implicaciones para la estrategia empresarial.

## Respuesta completa

# 114% de NRR: muy buena métrica, conclusión peligrosa

Voy a desmontar el malentendido porque la diferencia importa mucho para dónde pones el esfuerzo.

## Qué mide realmente ese 114%

Lo que ves en el panel es **Net Revenue Retention (NRR)**, no retención de clientes. La fórmula es:

> (MRR inicial + expansión − churn − downgrades) / MRR inicial

Un 114% significa que **los ingresos que generan hoy los clientes que ya tenías** son un 14% mayores que el mes pasado, **a pesar de las bajas**. Es decir: la expansión (upgrades) compensó de sobra las pérdidas.

Eso es métrica de élite para SaaS B2B (por encima del 100% ya es muy buena). Pero **no dice nada sobre cuántos clientes se te fueron**.

## Lo que dicen tus números de verdad

| Métrica | Valor | Lectura |
|---|---|---|
| Clientes inicio de mes | 40 | — |
| Clientes fin de mes | 36 | — |
| **Logo churn mensual** | **−10%** | **Alto** |
| NRR | 114% | Expansión compensando |

Si anualizas ese 10% mensual de forma compuesta te queda una retención de clientes anual cercana al 28%. Eso es **malo**, aunque el NRR tape la hemorragia.

Lo que está pasando es que tus 36 clientes que se quedan pagan, en promedio, **~26% más** que antes. Eso tapa que perdiste a 4 de cada 40.

## Por qué no deberías despreocuparte del churn

1. **La expansión tiene un techo.** Cada cliente solo puede subir de plan hasta donde llega tu catálogo. El churn no tiene ese límite natural.
2. **Con 40 clientes, cada baja es ~2,5% de tu base.** En una empresa con 5.000 clientes, 4 bajas son ruido. En la tuya, son señal.
3. **El NRR es una métrica agregada.** Si pierdes a tus clientes pequeños y los grandes hacen upgrade, el NRR sube mientras tu base se concentra y se vuelve más frágil.
4. **El NRR puede colapsar de un mes a otro.** Si la expansión se ralentiza un trimestre y el churn se mantiene, pasas de 114% a 95% sin haber hecho nada "peor".

## Qué deberías mirar además

- **Gross Revenue Retention (GRR):** ingresos retenidos sin contar expansión. Probablemente la tienes en 75–85%. **Esa es tu realidad de retención pura.**
- **Logo churn por cohortes:** ¿se te van los nuevos, los antiguos, los de cierto plan?
- **Razón de la baja:** voluntaria, impago, encaje con producto… cada una requiere acción distinta.

## La distribución de esfuerzo correcta

NRR 114% no te dice "ignora el churn". Te dice:

> "Tu motor de expansión es sano, **no lo dejes compensar un motor de retención roto**."

El reparto razonable para una empresa en tu etapa sería algo así:
- **Captación:** sigue creciendo, sí.
- **Expansión:** protégela, es lo que te da el 114%.
- **Retención:** **invierte aquí precisamente porque la métrica agregada la está tapando.** Es tu mayor riesgo oculto.

En resumen: el 114% es una buena noticia *y* una trampa cognitiva. Te está diciendo la verdad sobre tus ingresos, pero no la que crees estar leyendo.