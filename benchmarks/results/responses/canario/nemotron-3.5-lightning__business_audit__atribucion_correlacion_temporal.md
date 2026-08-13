# Nemotron 3.5 Lightning — business_audit/atribucion_correlacion_temporal

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.43 | quality: 10.0
- latency_total: 3.699s | tokens_per_second: 415.2
- input_tokens: 243 | output_tokens: 1536

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

Conclusión directa: **Con los datos que compartiste, no puedo decirte si la secuencia de emails funcionó.** Lo que ves es una correlación (las altas subieron y el MRR creció un 29%), pero la causalidad está completamente confundida por dos factores que ocurrieron al mismo tiempo y que son mucho más visibles:

1. **Publicidad pagada:** Empezaste el 3 de marzo con $400 en gasto. Eso solo ya puede haber traído varios suscriptores nuevos.
2. **Mención de un creador grande:** El 12 de marzo alguien con audiencia grande habló de la comunidad en un video. Eso suele generar un pico de tráfico y conversiones mucho mayor que una secuencia de 5 emails.

Las altas al plan pago pasaron de 9 en febrero a 14 en marzo (+5). Dependiendo del precio de tu plan, eso podría representar una fracción pequeña o grande del crecimiento de $1.200 en MRR, pero no sabemos cuántas de esas 5 altas nuevas provinieron de los emails, cuántas de los anuncios y cuántas de la mención del creador.

**Qué haría falta para estar seguros:**
- Un **grupo de control**: usuarios del plan gratuito que no recibieron los emails y comparar su tasa de conversión con la que sí los recibió.
- **Atribución por fuente**: registrar de dónde vino cada alta (anuncio, búsqueda, recomendación, email, redes orgánicas, etc.).
- **Métricas de engagement de los emails**: tasas de apertura, de clics y de conversión por cada uno de los 5 emails.
- **Precio promedio por usuario (ARPU)**: para saber exactamente cuánto de ese +$1.200 en MRR viene de los 5 nuevos suscriptores netos.
- **Seguimiento temporal**: ver si las conversiones se agrupan alrededor de los envíos de email, o alrededor del 12 de marzo (fecha de la mención).

Sin esos datos, cualquier afirmación de "los emails funcionaron" sería una suposición cómoda, no una conclusión basada en evidencia. Si quieres aislar el efecto de la secuencia, lo próximo sería diseñar un test A/B o pausar los anuncios y la mención del creador durante un mes completo y ver qué pasa con la curva de conversión.