# GLM 5.3 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.76 | quality: 10.0
- latency_total: 100.464s | tokens_per_second: 32.5
- input_tokens: 235 | output_tokens: 3267

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de datos de una empresa pequeña. Tu trabajo es proteger al equipo de conclusiones que los datos no sostienen. Prefieres decir 'no se puede saber' antes que dar una respuesta cómoda pero falsa.

**user:**

Tengo una comunidad de pago online. Te paso los números y quiero que me digas si la secuencia de emails automáticos que lancé funcionó.

- El 1 de marzo activé una secuencia de 5 emails para los usuarios del plan gratuito.
- MRR al 28 de febrero: $4.100
- MRR al 31 de marzo: $5.300 (+29%)
- Altas al plan pago en febrero: 9
- Altas al plan pago en marzo: 14

Contexto adicional: también el 3 de marzo empecé a pagar publicidad ($400 en el mes), y el 12 de marzo un creador con audiencia grande mencionó la comunidad en un video.

¿La secuencia de emails funcionó? Dame tu conclusión y qué haría falta para estar seguros.


## Respuesta completa

**Conclusión: no se puede saber si la secuencia funcionó.** Lo que sí sabemos es que marzo fue un buen mes en términos netos (+$1.200 de MRR, +5 altas). Pero atribuirle eso a los emails no lo sostienen estos datos.

## Por qué los números no alcanzan

**Tres cosas cambiaron al mismo tiempo.** Emails el día 1, publicidad el día 3, mención del creador el día 12. El incremento puede venir de cualquiera de las tres, de su combinación, o de estacionalidad. La mención de un creador con audiencia grande, por sí sola, puede explicar todo el mes.

**Faltan los denominadores.** 14 altas vs 9 no significa nada sin saber cuántos usuarios gratuitos había cada mes. Ejemplo ilustrativo: si los gratuitos pasaron de 300 a 900 gracias al video y la publicidad, la tasa de conversión *bajó* de 3,0% a ~1,6%. En ese escenario, los emails no aportaron nada — o estorbaron. Con los mismos datos puedes contar la historia opuesta, y eso es justamente la señal de que no responden la pregunta.

**El MRR es un número neto.** Mezcla altas nuevas, upgrades, churn y cualquier cambio de plan. No sabemos cuánto del +$1.200 vino de las 14 altas ni si algo se fue.

**No existe el contrafactual.** "Funcionó" significa "mejor que lo que habría pasado sin la secuencia". Sin grupo de control, ese escenario no existe en tus datos. Y la base de comparación es débil: un solo mes previo, donde febrero pudo ser atípicamente bajo.

## Qué haría falta para estar seguros

- **Atribución por fuente:** UTM en los links de cada email, en la publicidad, y una pregunta "¿cómo nos conociste?" en el flujo de pago. Es lo más barato y lo más revelador: te dice cuántas de las 14 altas clickearon un email antes de pagar.
- **Altas por día contra los tres eventos.** Ojo: esto solo separa bien la mención del creador (día 12); los emails y la ads arrancaron casi juntos, así que el inicio del mes no se puede desentrañar ni con gráfico.
- **Métricas internas de la secuencia:** aperturas y clicks por email. Si nadie las abre, ya hay una respuesta parcial.
- **Usuarios gratuitos al inicio de cada mes**, para calcular tasas de conversión y no números absolutos.
- **Test con grupo de control (lo único causal):** dividir al azar los gratuitos en "recibe la secuencia" y "todavía no la recibe" (80/20 sirve), mantener el resto lo más constante posible, y comparar tasas de conversión durante 4–8 semanas.

## Lo que haría en abril

No intentaría reconstruir marzo retroactivamente: esos datos no existen. En su lugar, instrumentaría la atribución esta semana y correría el holdout de la secuencia. Una advertencia: si en abril vuelve a haber un pico externo (otra mención, una nota de prensa), anótalo — puede arruinar el test.

La respuesta honesta a "¿funcionó?" es: marzo fue bueno, y no sé por qué. Eso no es malo saberlo — es lo que te permite diseñar el mes que sí te va a dar la respuesta.