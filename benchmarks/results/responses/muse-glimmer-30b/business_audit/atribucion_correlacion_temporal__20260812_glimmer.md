# Muse Glimmer 30B — business_audit/atribucion_correlacion_temporal

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 16.801s | tokens_per_second: 84.2
- input_tokens: 237 | output_tokens: 1414
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis detallado y práctico para evaluar la efectividad de la secuencia de correos electrónicos.

## Respuesta completa

No se puede saber si la secuencia de emails funcionó con los datos que tienes.

Tienes un resultado positivo, pero también tienes al menos 3 intervenciones solapadas en el mismo periodo y no tienes un contrafactual. MRR al 31 de marzo $5.300 vs $4.100 al 28 de febrero y 14 altas vs 9 en febrero son señales, no prueba de causalidad.

Confusores que no puedes descartar ahora:

* **Publicidad desde el 3 de marzo.** $400 en el mes. No sabes cuántos de los 5 nuevos pagos extra vienen de ese tráfico.
* **Mención del creador el 12 de marzo.** Es un evento puntual de awareness que normalmente genera un pico de altas en los días siguientes. No sabes su tamaño ni su contribución.
* **No sabes de dónde vienen las altas.** El MRR puede subir por nuevas altas, upgrades de usuarios existentes, o reducción de churn. La secuencia iba a usuarios gratuitos, pero las altas totales de pago pueden venir de usuarios que llegaron por ads o por el creador.
* **Base y tasa.** 9 a 14 altas es un cambio de +55% pero con números muy pequeños. Con 9 vs 14 la variabilidad aleatoria ya explica gran parte del cambio. Sin saber cuántos usuarios gratuitos había el 1 de marzo y cuántos recibieron la secuencia, no puedes calcular una tasa de conversión.

Para poder decir si la secuencia funcionó necesitarías aislar su efecto:

**1. Grupo control**
Randomiza a los usuarios gratuitos al inicio de marzo en 2 grupos iguales:
* Grupo A recibe la secuencia de 5 emails
* Grupo B no recibe nada, o recibe un email de control
Mide tasa de conversión a pago en 30 días: conversiones / usuarios gratuitos expuestos. Si A > B de forma estadísticamente significativa, ahí tienes evidencia.

**2. Métricas de funnel de la secuencia**
* Tamaño de la base gratuita el 1 de marzo
* Entregados / abiertos / clics por email
* Cuántos clics llegaron a la página de pago y cuántos convirtieron, con UTM específico de la secuencia
* Tiempo entre último email y conversión

**3. Aislar el resto**
* Etiqueta el origen de cada alta: email secuencia, publicidad, referido creador, orgánico...
* Mira la curva diaria de altas. Un pico el 13-15 de marzo apunta más al creador que a la secuencia que empezó el 1.
* Compara marzo vs un periodo previo similar sin intervenciones, y si puedes, haz un pre-post dentro del mismo grupo con un holdout.

Con lo que tienes ahora la conclusión honesta es: hubo crecimiento en marzo, pero no puedes atribuirlo a la secuencia de emails. Es igual de plausible que venga de la publicidad y/o la mención del creador, o una combinación.

Si quieres validar rápido, pausa la publicidad una semana y mantén la secuencia con un holdout, o viceversa. Sin un experimento controlado, cualquier atribución sería una conclusión cómoda pero falsa.