# Claude Opus 5.5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.12 | quality: 10.0
- latency_total: 25.074s | tokens_per_second: 92.8
- input_tokens: 366 | output_tokens: 2328

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

# Conclusión: con estos datos no se puede saber si la secuencia funcionó

No digo que no haya funcionado. Digo que **estos números no permiten distinguir su efecto del de otras causas**. Hay tres problemas.

## 1. Tres cambios a la vez

En marzo ocurrieron tres cosas que podrían haber subido las altas:

| Fecha | Cambio |
|---|---|
| 1 de marzo | Secuencia de emails |
| 3 de marzo | Publicidad pagada ($400) |
| 12 de marzo | Mención de un creador con audiencia grande |

El +29% de MRR y las 5 altas extra podrían venir de cualquiera de las tres, de una combinación, o de ninguna. Con un solo número agregado por mes no hay forma de separarlas. Atribuirle el resultado a los emails sería elegir la explicación que más te gusta, no la que demuestran los datos.

## 2. La diferencia podría ser ruido

Pasar de 9 a 14 altas suena a +55%, pero con números tan chicos la variación natural entre meses es grande. Como referencia aproximada, un conteo de ~10 eventos puede oscilar ±3 o ±4 de un mes a otro sin que cambie nada. Una diferencia de 5 está en el límite de lo que el azar produce solo.

**Ni siquiera está claro que marzo haya sido realmente mejor que febrero**, más allá de por qué.

## 3. El MRR mezcla más cosas que las altas

Los +$1.200 de MRR son altas, menos bajas, más upgrades o downgrades, más cambios de precio. Sin desglose no sabemos cuánto viene de nuevas altas. Por ejemplo, si en marzo hubo menos cancelaciones de lo normal, eso no tiene nada que ver con los emails.

## Qué puedes averiguar ya, con datos que probablemente tienes

Toma las **14 altas de marzo** y para cada una anota:

1. **Fecha de registro en el plan gratuito.** ¿Era usuario gratuito antes del 1 de marzo, o se registró en marzo, posiblemente por los anuncios o el video?
2. **¿Recibió la secuencia?** ¿Abrió o hizo clic en algún email?
3. **¿Llegó al checkout desde un link de email?** Si los links tenían UTM o tu plataforma registra el origen, esto es oro.
4. **Fecha de conversión.** ¿Se concentran después del 12 de marzo? Eso apuntaría al creador.

Cómo leerlo:
- **Si casi ninguno de los 14 interactuó con los emails**, es una señal fuerte de que la secuencia no explica el aumento.
- **Si varios hicieron clic en un email y luego pagaron**, es una señal a favor, pero no prueba causalidad. Quizás iban a pagar igual y el email solo fue el último clic.

**Una comparación más fuerte:** calcula la tasa de conversión de los usuarios gratuitos que ya existían antes del 1 de marzo, en marzo versus en meses anteriores. Ese grupo está menos expuesto a los anuncios y al video, que traen gente nueva, así que se acerca más a aislar el efecto de los emails. No es perfecto: alguien antiguo también pudo ver el video.

## Qué haría falta para estar seguros

**Un grupo de control.** De ahora en adelante:

- Divide al azar a los nuevos usuarios gratuitos: 50% recibe la secuencia y 50% no.
- Compara la **tasa de conversión a pago** entre ambos grupos después de 30 a 60 días.
- Como tus volúmenes son bajos, probablemente necesites **varios meses** para acumular suficientes conversiones y ver una diferencia clara. Si la secuencia mejora poco la conversión, quizás nunca lo puedas detectar con certeza a tu escala, y eso también es información útil.

Mientras tanto:
- Pon **UTMs en todos los links** de emails y anuncios.
- Pregunta en el checkout: *"¿Cómo nos conociste?"*. Es imperfecto, pero barato.
- **Desglosa el MRR mensual** en altas, bajas y cambios de plan.

## Resumen

| Pregunta | Respuesta |
|---|---|
| ¿Marzo fue mejor que febrero? | Probablemente, pero la diferencia en altas es pequeña y podría ser variación normal. |
| ¿Fue gracias a los emails? | No se puede saber. Hay tres causas posibles mezcladas. |
| ¿Hay que apagar la secuencia? | No hay evidencia para apagarla ni para darla por exitosa. |
| ¿Qué hacer? | Revisar el origen de las 14 altas ahora y montar un grupo de control para los próximos meses. |

Si me pasas el detalle de esas 14 altas (fecha de registro, fecha de pago, si abrieron o hicieron clic en emails), te ayudo a ver qué se puede concluir y qué no.