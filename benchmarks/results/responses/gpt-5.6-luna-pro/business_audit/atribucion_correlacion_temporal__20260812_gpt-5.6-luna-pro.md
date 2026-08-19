# GPT-5.6 Luna Pro — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.93 | quality: 10.0
- latency_total: 18.816s | tokens_per_second: 65.2
- input_tokens: 215 | output_tokens: 1226

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

**No se puede saber si la secuencia de emails funcionó a partir de estos datos.**

Sí se observa que marzo fue mejor que febrero:

- MRR: $4.100 → $5.300, un aumento de $1.200, aproximadamente **+29%**.
- Altas al plan pago: 9 → 14, un aumento de **5 altas**, aproximadamente **+56%**.

Pero durante marzo ocurrieron al menos dos acciones adicionales que pueden explicar parte o todo ese crecimiento:

1. Se invirtieron $400 en publicidad desde el 3 de marzo.
2. Un creador relevante mencionó la comunidad el 12 de marzo.

Por tanto, comparar febrero contra marzo mezcla el efecto de los emails con publicidad, exposición orgánica, estacionalidad y cualquier otro cambio del negocio. La conclusión defendible es:

> **El negocio creció en marzo, pero estos datos no permiten atribuir ese crecimiento a la secuencia de emails.**

Además, las altas no bastan para explicar el MRR: habría que considerar el precio de los planes, upgrades, bajas, reactivaciones y cuándo se produjeron las altas.

## Qué haría falta para estar más seguros

### 1. Un grupo de control

La mejor opción sería haber dividido aleatoriamente a los usuarios gratuitos elegibles:

- **Grupo tratamiento:** recibe la secuencia.
- **Grupo control:** no recibe la secuencia o recibe la comunicación habitual.

Después comparar, durante un período definido:

- Tasa de conversión a pago.
- MRR incremental por usuario.
- Tiempo hasta la conversión.
- Bajas o reembolsos.
- Ingresos netos, descontando costes relevantes.

La comparación clave sería:

\[
\text{Efecto estimado} =
\text{Conversión del grupo email}
-
\text{Conversión del grupo control}
\]

No simplemente “marzo versus febrero”.

### 2. El denominador de cada grupo

Saber que hubo 14 altas no alcanza. Necesitaría, entre otros datos:

- Cuántos usuarios gratuitos había al inicio de cada mes.
- Cuántos eran elegibles para recibir la secuencia.
- Cuántos recibieron realmente cada email.
- Entregas, aperturas, clics y conversiones.
- Fecha exacta de cada conversión.
- Plan contratado y MRR generado por cada usuario.
- Fuente de adquisición: email, publicidad, creador u otra.

Por ejemplo, 14 altas sobre 1.000 usuarios sería muy distinto de 14 sobre 100.

### 3. Separar las fuentes de adquisición

Conviene etiquetar los enlaces y usuarios con parámetros de seguimiento para distinguir:

- Usuarios provenientes de publicidad.
- Usuarios provenientes del video del creador.
- Usuarios que ya estaban en la base y recibieron emails.
- Usuarios que llegaron por otros canales.

Aun así, si un usuario recibió tanto publicidad como emails, la atribución puede seguir siendo ambigua. Por eso el control aleatorio es más fiable.

### 4. Si el experimento ya terminó

Se podría hacer un análisis retrospectivo comparando:

- Usuarios elegibles que recibieron la secuencia.
- Usuarios elegibles que no la recibieron o que la recibieron de forma incompleta.
- Cohortes según fecha de alta.
- Conversión antes y después de cada email.

Pero hay una advertencia importante: los usuarios que recibieron emails y los que no pueden ser diferentes de entrada. Esa comparación puede mostrar una asociación, **no necesariamente causalidad**.

También analizaría si las conversiones se concentraron:

- Antes o después del 12 de marzo.
- Entre usuarios expuestos al creador.
- Entre usuarios impactados por publicidad.
- Dentro de los días posteriores a cada email.

## Recomendación práctica

Para la próxima campaña, mantendría un **grupo de control del 10–20%**, asignado aleatoriamente y excluido de la secuencia. Definiría de antemano:

- Métrica principal: conversión a pago en, por ejemplo, 30 días.
- Métrica económica: MRR incremental por usuario.
- Ventana de medición.
- Tratamiento de bajas y reembolsos.
- Tamaño mínimo de muestra.

Con los números actuales —9 altas frente a 14— hay además muy pocas conversiones para sacar una conclusión sólida. El resultado es compatible con que los emails hayan ayudado, con que no hayan tenido efecto, o con que la mayor parte del crecimiento provenga de la publicidad y la mención del creador.