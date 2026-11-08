# Claude Sonnet 5.5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.42 | quality: 10.0
- latency_total: 19.099s | tokens_per_second: 112.0
- input_tokens: 366 | output_tokens: 2140

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

**Con estos datos no se puede saber si la secuencia funcionó.** Es plausible que haya ayudado, pero los números son igual de compatibles con que no haya hecho nada.

## Por qué no se sostiene la conclusión

**1. Tres cosas cambiaron a la vez.** El 1 de marzo la secuencia, el 3 la publicidad y el 12 el video del creador. Todas empujan en la misma dirección (más altas y más MRR) y ninguna está aislada. Además, no son independientes entre sí: la publicidad y el video traen usuarios gratuitos nuevos, y esos usuarios también entran en la secuencia. Si convierten, no sabes a qué atribuirlo.

**2. La diferencia de altas es pequeña.** Pasar de 9 a 14 son 5 altas. Con conteos tan bajos, la variación aleatoria mes a mes es grande: la desviación típica esperable en cada cifra es de unas 3 altas, así que 9 vs. 14 no se distingue con claridad del ruido. Tampoco sé cómo fueron diciembre, enero o los meses previos, así que no tengo línea base.

**3. El MRR mezcla varias cosas.** El cambio neto de $1.200 es altas nuevas, menos bajas, más cambios de plan o precio. Sin saber el precio del plan ni las bajas de marzo, no puedo separar cuánto viene de altas nuevas. Además, el MRR de un solo mes no dice nada sobre retención: puede haber altas "de impulso" que se caigan en abril.

**4. No hay grupo de comparación.** Un antes/después solo muestra que algo cambió, no qué lo causó.

## Qué haría falta para estar seguros

**Con datos que probablemente ya tienes:**
- **Origen de cada una de las 14 altas de marzo.** Fecha de registro gratuito, UTM o fuente, y si hizo clic en algún email antes de pagar.
- **Conversión de la base gratuita previa al 1 de marzo.** Es la comparación más limpia que tienes: esos usuarios no vinieron de la publicidad ni del video. Compara cuántos de ellos pasaron a pago en marzo contra su tasa mensual histórica (ene, feb, etc.). Si subió claramente, es una señal a favor de la secuencia. Aun así sería débil, porque el video pudo reactivar a gente existente.
- **Tiempos.** ¿Las altas ocurrieron poco después de recibir un email de la secuencia, o se concentraron tras el 12 de marzo?
- **Histórico de 6 a 12 meses** de altas y MRR, para ver cuánto varía normalmente.
- **Bajas de marzo** y si hubo cambios de precio o promociones.

**Para tener una respuesta real hacia adelante:**
- **Grupo de control.** Elige al azar un 20–50% de los nuevos registros gratuitos para que **no** reciban la secuencia, y compara la conversión entre ambos grupos durante 4–8 semanas. Esto es lo único que aísla el efecto de los emails, porque la publicidad y los videos llegan por igual a los dos grupos.
- **Ten en cuenta el tamaño muestral.** Si tu conversión es baja, necesitarás cientos de registros por grupo para detectar un efecto moderado. Conviene calcularlo antes de empezar para no concluir con muy pocos datos.

## Qué sí puedes decir hoy

"Marzo fue un buen mes, y la secuencia, la publicidad y el video del creador son candidatos a explicarlo. No sé cuánto aportó cada uno." Es una conclusión menos satisfactoria, pero es la que los datos sostienen. Mantener la secuencia activa mientras tanto es razonable, porque tiene bajo costo. Solo evita atribuirle el crecimiento ni basar decisiones de inversión en eso todavía.