# DeepSeek V4 Flash 0731 — business_audit/atribucion_correlacion_temporal

- model_id: `deepseek/deepseek-v4-flash-0731`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 5.953s | tokens_per_second: 205.1
- input_tokens: 315 | output_tokens: 1221

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

Con los datos que me das, mi respuesta honesta es: **no se puede saber si la secuencia de emails funcionó**.

Te explico por qué y qué necesitaríamos para poder responderlo con rigor.

---

## Lo que dicen los números (y lo que no dicen)

| Métrica | Febrero | Marzo | Cambio |
|---|---|---|---|
| MRR | $4.100 | $5.300 | +29% |
| Altas a plan pago | 9 | 14 | +56% |

A simple vista, marzo fue mejor que febrero. El problema es que en marzo pasaron **tres cosas distintas** al mismo tiempo:

1. Activaste la secuencia de 5 emails (1 de marzo).
2. Empezaste a pagar publicidad (3 de marzo, $400).
3. Un creador grande mencionó la comunidad (12 de marzo).

Cualquiera de esas tres (o las tres combinadas) puede explicar el aumento. Con solo un dato agregado mensual, no hay manera de separar el efecto de cada una.

Además, hay otras preguntas que estos números no responden:

- ¿Cuántos usuarios del plan gratuito recibieron realmente la secuencia?
- ¿Cuántos de esos 14 nuevos clientes venían del email, de la publicidad, del creador o de otras fuentes?
- ¿Cuánto pagaba cada nuevo cliente? Si en marzo entraron clientes de mayor ticket, el MRR sube aunque la secuencia no haya convertido a nadie.
- ¿Cuántos usuarios se dieron de baja (churn) en esos meses? Si en marzo se fueron clientes caros y entraron muchos baratos, el MRR puede subir o bajar de forma engañosa.
- ¿En qué fechas exactas se produjeron las altas? Si las 14 altas ocurrieron todas después del 12 de marzo, apuntaría más al creador que a los emails.

---

## Conclusión

**No hay evidencia suficiente para afirmar que la secuencia de emails funcionó.** Tampoco para decir que no funcionó. Lo único que sabemos es que marzo fue mejor que febrero, pero no por qué.

---

## Qué haría falta para estar seguros

Para atribuir causalidad, necesitarías al menos una de estas cosas:

1. **Grupo de control**: dividir a los usuarios del plan gratuito en dos grupos aleatorios: uno recibe la secuencia y otro no (o la recibe después). Comparar tasas de conversión entre ambos. Esto es lo más limpio y no requiere dejar de mandar emails para siempre: puedes hacer un experimento con una parte de la audiencia.

2. **Datos de atribución**: saber de qué fuente viene cada alta (email, anuncio, mención, orgánico). Con un UTM en los enlaces de los emails y en los anuncios, y preguntando a los nuevos clientes cómo te conocieron, puedes asignar cada alta a su origen.

3. **Análisis temporal fino**: si no puedes hacer experimento, necesitas al menos datos diarios de altas y saber cuándo se envió cada email. Si ves picos de conversión en las 24-48 horas después de cada envío, y esos picos no coinciden con los anuncios ni con la mención, tendrías una pista fuerte (aunque no prueba definitiva).

4. **Histórico más largo**: saber cómo se comportaban las altas en meses anteriores (enero, diciembre, etc.) para entender la estacionalidad. Si febrero fue anormalmente bajo, marzo pudo ser simplemente una vuelta a la media.

---

Mi recomendación: no tires más dinero ni tiempo en optimizar la secuencia basándote en estos datos. Primero monta un sistema mínimo de atribución (UTMs + seguimiento de eventos) o un test A/B controlado. Es más aburrido, pero es la única forma de saber qué está funcionando de verdad.

Si me pasas datos diarios de altas, el detalle de envíos de la secuencia y las fechas de la publicidad y la mención, puedo ayudarte a hacer un análisis más fino. Pero con lo que hay ahora, la respuesta correcta es: **no se puede saber**.