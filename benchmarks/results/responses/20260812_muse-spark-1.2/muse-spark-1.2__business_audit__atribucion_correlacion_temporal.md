# Muse Spark 1.2 — business_audit/atribucion_correlacion_temporal

- model_id: `meta/muse-spark-1.2`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 18.278s | tokens_per_second: 117.2
- input_tokens: 221 | output_tokens: 2142

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

Conclusión directa: **No se puede saber si la secuencia de emails funcionó con estos datos.**

Y es importante no concluir que sí funcionó, porque los datos no lo sostienen y tomar esa conclusión como cierta es peligroso para las decisiones del equipo.

Te explico por qué:

### 1. Tienes 3 cambios a la vez, no uno
Activaste la secuencia el 1 de marzo, pero:
* El 3 de marzo empezaste a pagar publicidad
* El 12 de marzo te mencionó un creador grande

Pasaste de $4.100 a $5.300 de MRR y de 9 a 14 altas, pero es imposible saber qué parte de ese +$1.200 y de esas 5 altas extra viene de los emails, de los ads o del video. Cualquiera de los tres, o la combinación, podría explicar todo el crecimiento. Esto se llama factor de confusión. Sin aislarlos, cualquier atribución es especulación.

### 2. El aumento es muy pequeño para sacar conclusiones
Pasar de 9 a 14 altas suena a +55%, pero en números absolutos son solo 5 personas más. Con volúmenes tan bajos, esa variación puede ser puro azar de un mes a otro. No podemos descartar que en abril vuelvas a 9 altas aunque no cambies nada.

Tampoco sabemos la composición de ese MRR: ¿es por altas nuevas, por usuarios que pagaban más, por menos churn? Sin ese desglose no podemos atribuirlo a la conversión de gratuitos a pago, que es lo que atacaba el email.

### 3. No tienes el contrafactual
Para saber si funcionó necesitaríamos responder: ¿Qué hubiera pasado en marzo *sin* los emails? Como todos los usuarios gratuitos recibieron la secuencia, no tenemos con qué comparar.

Incluso si me dijeras "5 de las 14 altas hicieron clic en el email antes de pagar", tampoco sería prueba. Esas personas quizá hubieran pagado igual sin el email, empujadas por el anuncio o el video.

> Correlación no es causalidad. Que dos cosas pasen a la vez -lancé emails y subió el MRR- no demuestra que una causó la otra.

### Qué haría falta para estar seguros

Para poder decir "la secuencia generó X altas extra" necesitaríamos un experimento controlado, no solo mirar el total de marzo:

**1. Un grupo de control aleatorio:**
La próxima vez, divide a los usuarios gratuitos al azar en dos grupos al inicio del mes:
* Grupo A: recibe la secuencia de 5 emails
* Grupo B: no recibe nada

Si el Grupo A convierte significativamente más que el Grupo B, entonces sí puedes atribuir la diferencia a los emails.

**2. Medir incrementabilidad, no solo atribución:**
No basta con poner un link con UTM en el email. Necesitas comparar la tasa de conversión del Grupo A vs Grupo B. La diferencia es el efecto real e incremental del email.

**3. Aislar variables en el tiempo:**
No lances 3 iniciativas grandes el mismo mes si quieres medir cada una. Si tienes que hacerlo, al menos el experimento A/B te permite aislar el efecto del email del ruido de los ads y el video.

**4. Métricas intermedias de la secuencia:**
Para diagnosticar, necesitaríamos: ¿a cuántos se les envió?, ¿tasa de apertura?, ¿tasa de clic?, ¿tasa de conversión a pago de los que clicaron vs los que no? Sin eso, ni siquiera sabemos si los emails se leyeron.

**Mi recomendación ahora:** No escales ni descartes la secuencia todavía. Déjala como "hipótesis no probada". Si quieres saber si vale la pena mantenerla y mejorarla, monta el A/B con grupo de control el próximo mes. Hasta entonces, la respuesta honesta es que no lo sabemos.