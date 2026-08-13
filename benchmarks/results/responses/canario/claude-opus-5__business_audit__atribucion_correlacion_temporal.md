# Claude Opus 5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.12 | quality: 10.0
- latency_total: 31.432s | tokens_per_second: 59.0
- input_tokens: 364 | output_tokens: 1855

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

# Conclusión corta

**No se puede saber.** Con estos números no hay forma de atribuirle el crecimiento a la secuencia de emails, ni de descartar que haya funcionado. Tienes tres intervenciones solapadas en el mismo mes y un solo mes de comparación.

# Por qué los datos no alcanzan

**1. Tres causas candidatas, un solo resultado**
En marzo pasaron tres cosas: la secuencia (1/3), la publicidad (3/3) y la mención del creador (12/3). Las tres apuntan en la dirección de más altas. No hay nada en los datos que permita separar sus efectos. Esto es un problema de diseño, no de análisis: ningún método arregla un experimento donde todo cambió a la vez.

**2. El delta es demasiado pequeño para ser señal**
9 → 14 altas es +5 conversiones. En ese rango, la variación normal mes a mes puede explicar el movimiento sin que haya pasado nada. Si en enero tuviste 13 y en diciembre 8, esos "+29%" son ruido. **No me diste los meses anteriores, así que ni siquiera sé cuál es tu rango habitual.** Ese es el dato que más falta.

**3. El MRR y las altas cuentan historias que no verifiqué que encajen**
+$1.200 de MRR con 14 altas implica ~$86 por alta. Si tu plan cuesta menos que eso, parte del crecimiento vino de otra parte: upgrades de usuarios existentes, cambio de precios, menos cancelaciones, anualidades cobradas de golpe. Y si vino de ahí, la secuencia (que apunta a usuarios del plan gratuito) no es la explicación. Tampoco sé cuántas bajas hubo: +$1.200 neto podría ser +$1.600 en altas y -$400 en churn, o cualquier otra combinación.

**4. Falta el denominador**
14 altas sobre cuántos usuarios gratuitos? Si la publicidad te trajo tráfico nuevo, tu base de free users creció en marzo. Más altas con una base más grande puede significar la misma tasa de conversión o incluso peor. La cifra absoluta no distingue entre "convierto mejor" y "tengo más gente a la que convertir".

**5. El timing del creador es verificable y no lo miré**
La mención fue el 12 de marzo. Si las altas se concentran alrededor de esa fecha, tienes una pista fuerte de que no fue el email. Si están repartidas parejo, otra. Este es el chequeo más barato que puedes hacer hoy mismo con datos que ya tienes.

# Qué haría falta

**Ahora, con lo que ya tienes registrado:**

- **Altas por día de marzo y febrero.** Busca el pico alrededor del 12.
- **Altas segmentadas por origen:** ¿el usuario entró por la publicidad, por el video, o ya estaba en tu base antes del 1 de marzo? Solo los que ya estaban antes del 1/3 pudieron ser afectados por la secuencia sin contaminación de los otros dos canales. Ese subgrupo es tu mejor aproximación disponible.
- **Descomposición del MRR:** altas nuevas, upgrades, cancelaciones, cambios de precio. Necesito saber de dónde vinieron los $1.200.
- **Usuarios gratuitos activos al inicio de cada mes**, para calcular tasa de conversión en lugar de conteo.
- **Métricas de la secuencia:** aperturas, clics, y cuántos de los que convirtieron habían abierto al menos un email. Si convirtieron gente que nunca abrió un email, ya sabes algo.
- **Altas de los 6-12 meses previos.** Sin esto no puedes distinguir señal de ruido, ni descartar estacionalidad.

**Para tener una respuesta real, no una pista:**

- **Prueba con grupo de control.** Divide a los usuarios gratuitos nuevos: mitad recibe la secuencia, mitad no. Compara tasa de conversión a 30 días. Es la única forma de aislar el efecto.
- **Advertencia sobre el tamaño:** con tu volumen actual (~10-15 altas/mes), un test así tarda meses en dar algo concluyente. Detectar una mejora modesta requiere cientos de usuarios por rama. Conviene decidir de antemano cuánto tiempo lo vas a correr y qué diferencia mínima te haría cambiar de decisión, para no mirar los números cada semana y detenerte cuando se vean bien.
- **No cambies tres cosas a la vez otra vez.** Si necesitas moverte rápido, al menos espacia las intervenciones dos o tres semanas.

# Lo honesto

La secuencia puede haber funcionado perfectamente. También puede no haber hecho nada y el crecimiento ser del video, o de la publicidad, o azar. Estos datos son compatibles con las tres historias.

Lo que sí puedes concluir hoy: **marzo fue mejor que febrero.** Eso es todo. Y si mañana apagas la secuencia y las altas caen, tampoco sabrás si fue por eso o porque se agotó el efecto del video.

Empieza por el desglose de altas por día y por origen. Con eso mañana ya tienes una idea mucho mejor, y es gratis.