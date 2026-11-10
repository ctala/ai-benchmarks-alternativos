# GLM 5.3 — business_audit/atribucion_correlacion_temporal

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 89.43s | tokens_per_second: 52.8
- input_tokens: 235 | output_tokens: 4722

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

## Conclusión: no se puede saber

Marzo fue mejor que febrero, eso es real. Pero **los datos no permiten separar el efecto de los emails del de la publicidad y del video del creador**. Decir "la secuencia funcionó" sería inventar una respuesta cómoda.

## Lo que los datos sí sostienen

- MRR neto: +$1.200 (+29%) entre el 28/2 y el 31/3.
- 14 altas contra 9 en febrero (+55%... aunque con muestras tan pequeñas, esa diferencia está dentro del rango normal de variación de un mes a otro).

Eso es todo. Nada de esto apunta a los emails *específicamente*.

## Por qué no puedo atribuirlo a la secuencia

1. **Tres intervenciones simultáneas.** Emails (1/3), anuncios (3/3), mención del creador (12/3). Sin atribución, culpar o premiar a cualquiera de las tres es apostar. La mención del creador es candidata especialmente fuerte: una audiencia grande a mitad de mes puede generar tanto altas directas como nuevos usuarios gratuitos.

2. **No sé de dónde vienen las 14 altas.** ¿Cuántas eran usuarios gratuitos existentes (el público objetivo de los emails) y cuántas llegaron directo al plan pago desde el anuncio o el video? Si la mayoría son altas directas, la secuencia no tuvo nada que ver.

3. **El MRR es neto, no bruto.** Incluye bajas y cambios de plan. Con precio promedio desconocido, ni siquiera sé si 14 altas alcanzan aritméticamente para explicar +$1.200, o si hubo upgrades o menos churn contribuyendo. Y no tengo el churn de cada mes.

4. **Línea base de un solo mes.** Sin enero ni diciembre no sé si la comunidad ya venía creciendo por su cuenta. Tampoco sé el tamaño de la base gratuita (el denominador de cualquier tasa de conversión), ni si creció con el video.

5. **Ni siquiera sé si los emails se abrieron.** Sin aperturas y clics, "funcionó" no tiene ni evidencia intermedia.

## Qué haría falta

**Con los datos que ya existen (análisis parcial):**
- Fuente/UTM de cada una de las 14 altas: ¿free→paid o alta directa?
- Serie **diaria** de altas de marzo, cruzada con las fechas de envío de cada email, el inicio de ads (3/3) y el video (12/3). Si las altas se concentran después del 12, el candidato principal es el video.
- Métricas de la secuencia: entregas, aperturas, clics.
- Churn de febrero y marzo, y precio promedio de planes, para descomponer el MRR.
- Enero (o más) como línea base.
- Tamaño de la base gratuita al 1/3 y al 31/3, y aclarar si los emails solo los recibieron los usuarios gratuitos del 1/3 o también quienes entraron después.

**Para estar seguros de verdad (la próxima vez):**
- **Grupo de control aleatorio.** Antes de activar la siguiente secuencia: 80% de usuarios gratuitos la reciben, 20% queda en holdout. Comparar conversión free→paid a 30-60 días. Es la única forma limpia de causalidad y no cuesta nada.
- Advertencia honesta: con ~14 altas/mes, un holdout necesitará varias semanas para detectar un efecto. Mejor esperar ese tiempo que quedarnos con una conclusión falsa.

## Cierre

No diría "funcionó", pero tampoco diría "no funcionó". La secuencia está **sin medir**, no refutada. Con un holdout en el próximo lanzamiento, en un par de meses tendrías la respuesta de verdad.