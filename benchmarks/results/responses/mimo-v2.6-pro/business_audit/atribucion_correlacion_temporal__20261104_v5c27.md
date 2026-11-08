# MiMo V2.6 Pro — business_audit/atribucion_correlacion_temporal

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 28.911s | tokens_per_second: 46.1
- input_tokens: 251 | output_tokens: 1333

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

# No se puede saber con estos datos

Y digo esto con toda la seriedad del caso, porque es la respuesta correcta aquí.

## Por qué no se puede atribuir el crecimiento a la secuencia de emails

En marzo ocurrieron **tres cosas simultáneamente**:

| Intervención | Fecha | Posible efecto en conversiones |
|---|---|---|
| Secuencia de emails | 1 de marzo | Directo sobre usuarios del plan gratuito |
| Publicidad pagada ($400) | 3 de marzo | Trae tráfico nuevo que puede convertirse |
| Mención de creador con audiencia grande | 12 de marzo | Pico de visibilidad externa |

El salto de 9 a 14 altas (+5) y de $4.100 a $5.300 de MRR pueden venir de **cualquier combinación de las tres**. Decir que "los emails funcionaron" porque marzo fue mejor que febrero es atribuir causalidad donde solo hay correlación temporal.

## Lo que tampoco sabemos (y sería clave)

1. **¿De dónde vinieron las 14 altas?** Si no tienes atribución (UTM, pregunta "¿cómo nos conociste?", tracking de clics en emails), no puedes separar el efecto de cada canal.

2. **¿Cuántos de los que se suscribieron eran usuarios del plan gratuito que recibieron los emails?** Es el grupo objetivo. Si las 14 altas son mayoritariamente usuarios nuevos (vía ads o el creador), la secuencia pudo no haber convertido a nadie.

3. **¿Tasas de apertura y clic?** Si el 95% de destinatarios ni abrió los emails, la secuencia difícilmente fue el motor. Si hubo clicks y conversiones rastreadas, eso es señal útil (aunque no definitiva).

4. **N es pequeño.** Pasar de 9 a 14 son 5 conversiones más. Con muestras tan reducidas, la variación aleatoria mensual puede explicar buena parte del cambio sin ninguna intervención.

---

## Qué haría falta para estar seguros

**Lo más rápido (ya, con los datos existentes):**

- Extraer el **origen de cada una de las 14 altas de marzo** (email / ads / directo / referido / creador). Aunque sea retroactivo con Google Analytics, Stripe metadata, o un formulario de "¿cómo nos conociste?".
- Revisar los **analytics de la secuencia de emails**: tasa de apertura, tasa de clic, y cuántos de esos clics llegaron a la página de pago.

**Lo riguroso (para el futuro):**

- **Test A/B o grupo de control:** enviar la secuencia al 50% de los usuarios gratuitos y no enviarla al otro 50%. Comparar la tasa de conversión entre ambos grupos. Es la única forma limpia de aislar el efecto.
- **UTMs distintas por canal** para que cada alta se pueda trazar a su origen.
- **Algunos meses de datos base** antes de lanzar la secuencia (con Feb solo tienes 1 punto de referencia, insuficiente para distinguir tendencia de ruido).

---

## En resumen

> **Los datos muestran que marzo fue mejor que febrero. No muestran que los emails lo causaron.** Tres intervenciones simultáneas + muestra pequeña + sin atribución = imposible aislar el efecto. Podría haber funcionado, podría no haberlo hecho, podría haber funcionado parcialmente. Lo honesto es decir: **no se puede saber todavía**.

Lo que sí puedes hacer hoy: ir a buscar la fuente de esas 14 altas. Eso te dará la primera pista real.