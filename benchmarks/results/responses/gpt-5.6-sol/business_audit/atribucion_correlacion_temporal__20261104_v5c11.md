# GPT-5.6 Sol — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.54 | quality: 10.0
- latency_total: 8.486s | tokens_per_second: 92.3
- input_tokens: 224 | output_tokens: 783

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

**No se puede saber si la secuencia de emails causó la mejora.**

Sí podemos afirmar que marzo fue mejor:

- MRR: de **$4.100 a $5.300**, un aumento de **$1.200 (+29%)**.
- Altas al plan pago: de **9 a 14**, un aumento de **5 (+56%)**.

Pero en marzo ocurrieron al menos tres cambios simultáneos:

1. Se activó la secuencia de emails.
2. Comenzó la publicidad.
3. Un creador mencionó la comunidad.

Además, comparar solo febrero con marzo no permite descartar variación normal, estacionalidad u otros factores. El MRR tampoco mide únicamente nuevas conversiones: puede cambiar por bajas, upgrades, downgrades o variaciones de precio.

Por tanto, los datos son **compatibles con que los emails hayan ayudado**, pero no permiten atribuirles el aumento. Incluso podrían haber convertido usuarios captados por la publicidad o el creador, en cuyo caso habría un efecto combinado.

## Qué haría falta para estar seguros

La mejor opción sería un **experimento con grupo de control**:

- Dividir aleatoriamente a los usuarios gratuitos elegibles en dos grupos comparables.
- Un grupo recibe la secuencia y el otro no, o recibe la comunicación habitual.
- Medir durante el mismo periodo:
  - porcentaje que pasa a pago;
  - MRR incremental;
  - tiempo hasta la conversión;
  - bajas o cancelaciones posteriores.
- Definir de antemano una ventana de conversión, por ejemplo 30 días.
- Mantener el grupo de control suficientemente grande para detectar una diferencia real.

La atribución por enlaces, aperturas o clics ayudaría a entender el recorrido, pero **no demostraría causalidad**: quien hace clic puede ser alguien que ya tenía más intención de comprar.

Si ahora no puedes hacer un experimento, como aproximación convendría analizar:

- fecha exacta de cada alta;
- fuente de adquisición de cada usuario;
- qué usuarios recibieron, abrieron y pulsaron los emails;
- antigüedad en el plan gratuito;
- conversiones antes y después por cohortes equivalentes;
- varios meses históricos, no solo febrero;
- nuevas altas, bajas, upgrades y downgrades que explican el cambio de MRR.

Eso permitiría estimar mejor el efecto, pero seguiría siendo menos concluyente que un grupo de control aleatorio. Con los datos actuales, la conclusión correcta es: **marzo mejoró, pero no sabemos cuánto —si algo— se debió a la secuencia de emails**.