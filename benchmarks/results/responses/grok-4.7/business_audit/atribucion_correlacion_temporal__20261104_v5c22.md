# Grok 4.7 — business_audit/atribucion_correlacion_temporal

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 21.005s | tokens_per_second: 50.5
- input_tokens: 1458 | output_tokens: 1060

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

**No se puede saber si la secuencia funcionó.** Los números subieron, pero no aíslan el efecto de los emails.

En marzo cambiaste tres cosas a la vez: la secuencia (1 de marzo), publicidad de pago (desde el 3, $400) y una mención de un creador con audiencia grande (12 de marzo). El MRR pasó de $4.100 a $5.300 y las altas de 9 a 14. Eso es compatible con que hayan funcionado los emails, los anuncios, la mención, una mezcla, o variación normal. Con este diseño no hay forma de separarlas.

Además, el MRR no es solo “altas nuevas”. +$1.200 puede venir de altas, de menos bajas, de upgrades o de cambios de precio. No tienes ese desglose, así que ni siquiera el salto de ingresos se puede atribuir a las 5 altas extra (14 frente a 9). Con muestras tan chicas, esa diferencia también puede ser ruido.

**Para estar seguros haría falta algo que separe el efecto de los emails del resto:**

1. Un grupo de control: usuarios del plan gratuito que no reciban la secuencia (idealmente al azar), y comparar su tasa de paso a pago con la de quienes sí la reciben, en la misma ventana.
2. Atribución mínima: clics y conversiones con origen (email vs anuncio vs mención/orgánico), no solo el total del mes.
3. Desglose del MRR: nuevas altas, expansión, contracción y churn, para no leer el +29% como “la secuencia convirtió”.
4. Una línea de base más larga (varios meses antes) para ver si marzo ya venía subiendo.

Hasta tener al menos el punto 1, o una atribución clara del 2, la conclusión correcta es: **no se puede saber**. Decir que “funcionó” porque el mes cerró mejor sería una respuesta cómoda y falsa.