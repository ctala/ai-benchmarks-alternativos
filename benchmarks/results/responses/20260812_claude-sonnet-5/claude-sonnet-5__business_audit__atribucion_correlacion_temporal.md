# Claude Sonnet 5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.4 | quality: 10.0
- latency_total: 15.931s | tokens_per_second: 65.6
- input_tokens: 364 | output_tokens: 1045

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

# Conclusión: no se puede saber con estos datos

Con lo que me pasás no puedo atribuir el aumento de MRR (ni las 14 altas) a la secuencia de emails. Hay al menos **tres cosas pasando al mismo tiempo** en marzo:

1. Secuencia de emails (desde el 1/3)
2. Publicidad paga (desde el 3/3, $400)
3. Mención de un creador grande (12/3)

Cualquiera de las tres —o una combinación— pudo causar el salto de 9 a 14 altas. No hay forma de separar el efecto de cada una solo mirando el agregado mensual.

## Problemas específicos con la lectura actual

- **La mención del creador es la sospechosa más fuerte.** Una mención con audiencia grande puede generar un pico de tráfico y conversiones que fácilmente explique 5 altas extra, sin que los emails hayan tocado nada.
- **El MRR no es lo mismo que "la secuencia convirtió gente".** MRR sube también por upgrades de planes existentes, o baja menos por menor churn. No sabés si el +$1.200 viene de altas nuevas, de upgrades, o de menos cancelaciones.
- **9 vs 14 es una muestra chica.** Con números tan bajos, la varianza mes a mes puede ser simplemente ruido (estacionalidad, día de la semana en que caen los pagos, etc.), sin que haga falta ninguna causa especial.

## Qué haría falta para saber

1. **Fecha de conversión de cada uno de los 14 usuarios nuevos**, cruzada con:
   - ¿Abrió/clickeó los emails de la secuencia antes de convertir?
   - ¿Llegó por el link/UTM del video del creador?
   - ¿Vino de un anuncio pago (UTM de la campaña)?
2. **Separar altas por canal de origen** (idealmente ya deberías tener UTMs o al menos preguntar "¿cómo nos conociste?" en el signup).
3. **Idealmente, un grupo de control**: mandar la secuencia solo a una parte de los usuarios gratuitos y comparar tasas de conversión entre quienes la recibieron y quienes no. Esto es lo único que te da atribución causal real.
4. **Ver el timing exacto de las 14 conversiones dentro de marzo.** Si la mayoría cayó justo después del 12/3 (mención del creador), es mala señal para atribuirle el mérito a los emails. Si se distribuyeron parejo desde el día 1-5 (cuando corrió la secuencia), es mejor señal — aunque igual no aísla la publicidad.

**Mi recomendación concreta**: antes de gastar más tiempo en optimizar la secuencia, mirá el timing de las 14 altas y si tenés UTMs, revisá el origen. Si no tenés tracking de origen, empezá a implementarlo ya — sin eso, vas a seguir sin poder responder esta pregunta cada vez que lancés algo nuevo.