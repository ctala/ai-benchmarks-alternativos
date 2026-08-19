# Claude Sonnet 5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 7.01 | quality: 8.0
- latency_total: 14.397s | tokens_per_second: 69.4
- input_tokens: 364 | output_tokens: 999

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

Y te digo por qué, porque no es solo una formalidad: tenés **tres intervenciones simultáneas** en el mismo mes (secuencia de emails, publicidad paga, mención de un creador) y **una sola métrica agregada** (MRR, altas totales). No hay forma de separar el efecto de cada una.

## El problema concreto

El crecimiento de altas (9 → 14) y de MRR (+29%) puede explicarse por:

- La secuencia de emails
- Los $400 en ads (activados el 3 de marzo)
- La mención del creador (12 de marzo, potencialmente el mayor driver si tuvo alcance grande)
- Una combinación de las tres, en proporciones que hoy no conocés

Si la mención del creador generó un pico de tráfico nuevo, ese tráfico también pudo:
- Entrar directo al plan pago (sin pasar por la secuencia)
- Entrar al plan gratuito y luego sí recibir la secuencia
- Confundirse con las altas atribuibles a ads

**No tenés cómo distinguir esto con los números que me pasaste.**

## Qué preguntaría antes de sacar conclusiones

1. **¿De dónde vinieron las 14 altas de marzo?** Si tu plataforma tiene tracking de fuente/UTM, esto es lo primero que miraría.
2. **¿Cuántos usuarios del plan gratuito completaron la secuencia de 5 emails, y de esos, cuántos convirtieron a pago?** Esta es la métrica que realmente te dice si la secuencia funciona: tasa de conversión de quienes *recibieron* la secuencia vs. quienes no.
3. **¿Cuándo fue el pico de altas dentro de marzo?** Si se concentraron entre el 12 y el 15, sospecho fuerte del creador. Si se distribuyeron parejo o coincidieron con los envíos de cada email de la secuencia, ahí hay señal a favor de la secuencia.
4. **¿Cuánto tráfico/altas al plan gratuito generó el video del creador?** Si generó 50 nuevos usuarios gratis y de esos 8 convirtieron, la secuencia sí importa (fue el mecanismo de conversión). Si generó 5 altas *directas* a pago sin pasar por gratis, la secuencia no tuvo nada que ver con esas 5.

## Lo que sí te puedo decir

El +29% de MRR es un dato positivo para el negocio, pero como evidencia de que "la secuencia de emails funcionó" es prácticamente inútil aislado del resto. Atribuírselo a los emails sin más análisis sería una conclusión cómoda pero no sostenida por los datos.

Si me pasás la conversión gratuito→pago segmentada por quienes recibieron la secuencia completa, ahí sí podemos hablar con más confianza.