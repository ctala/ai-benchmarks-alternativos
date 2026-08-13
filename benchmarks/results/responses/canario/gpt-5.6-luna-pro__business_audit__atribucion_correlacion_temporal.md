# GPT-5.6 Luna Pro — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.85 | quality: 10.0
- latency_total: 14.944s | tokens_per_second: 218.6
- input_tokens: 5127 | output_tokens: 3267

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

## Conclusión

**No se puede saber si la secuencia de emails funcionó a partir de estos datos.**

Lo que sí sabemos es que marzo fue un mes mejor que febrero:

- MRR: de **$4.100 a $5.300**, un aumento de **$1.200 (+29%)**.
- Altas al plan pago: de **9 a 14**, un aumento de **5 altas (+56%)**.

Pero durante marzo ocurrieron al menos tres cambios relevantes:

1. Se activó la secuencia de emails el 1 de marzo.
2. Se empezó a pagar publicidad el 3 de marzo.
3. Un creador con una audiencia grande mencionó la comunidad el 12 de marzo.

Por tanto, el aumento observado **podría deberse a los emails, a la publicidad, a la mención del creador, a una combinación de los tres o a otros factores**. El incremento de MRR tampoco mide exclusivamente las nuevas altas: puede incluir upgrades, bajas, pagos recuperados, cambios de precio o variaciones de otros usuarios.

La afirmación defendible sería:

> “En marzo mejoraron el MRR y las altas, pero no podemos atribuir esa mejora a la secuencia de emails.”

## Qué haría falta para evaluarlo

Como mínimo, analizaría para cada usuario gratuito:

- Si recibió la secuencia, y cuándo.
- Emails entregados, abiertos y clicados.
- Fecha exacta de conversión al plan pago.
- Fuente de adquisición: email, publicidad, creador, orgánico, etc.
- Si había sido expuesto previamente a la publicidad o a la mención.
- Ingresos generados por cada conversión.
- Bajas y retención posterior.

También compararía:

- Tasa de conversión de usuarios expuestos a la secuencia frente a usuarios no expuestos.
- Conversión antes y después del lanzamiento.
- Conversiones ocurridas antes y después del 12 de marzo.
- Coste y conversiones atribuibles a la publicidad.
- Tráfico y altas provenientes del creador.

Aun así, una comparación simple entre “antes” y “después” tendría limitaciones, porque los grupos podrían ser distintos y coincidieron varias campañas.

## La forma más sólida de saberlo

Haría un experimento controlado:

1. Dividir aleatoriamente a los usuarios gratuitos elegibles en dos grupos.
2. Enviar la secuencia a un grupo.
3. Mantener al otro como grupo de control durante un período definido.
4. Medir la conversión a pago, el MRR generado y la retención a 30 o 60 días.

Idealmente, ambos grupos deberían estar igualmente expuestos a la publicidad y a otras comunicaciones. Con solo 9 y 14 altas mensuales, probablemente habría que acumular varios períodos para obtener una señal fiable: cinco conversiones adicionales son una diferencia interesante, pero todavía una base pequeña para sacar conclusiones firmes.

En resumen: **la secuencia puede haber funcionado, pero estos datos no permiten distinguir su efecto del de la publicidad y el creador.**