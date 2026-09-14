# GPT-5.6 Luna — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 12.411s | tokens_per_second: 80.7
- input_tokens: 224 | output_tokens: 1002

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

**No se puede saber con estos datos si la secuencia de emails funcionó.**

Sí podemos decir que en marzo hubo una mejora:

- MRR: de **$4.100 a $5.300**, un aumento de **$1.200 (+29%)**.
- Altas al plan pago: de **9 a 14**, un aumento de **5 altas (+56%)**.

Pero esos resultados ocurrieron al mismo tiempo que:

- Comenzaste publicidad el **3 de marzo**, con un gasto de $400.
- Un creador relevante mencionó la comunidad el **12 de marzo**.

Por tanto, el aumento puede deberse a los emails, a la publicidad, a la mención, a una combinación de los tres o incluso a otros factores. Con solo comparar febrero contra marzo, **no es posible atribuir causalidad a la secuencia**.

Además, el MRR puede haber cambiado por bajas, upgrades, cambios de precio o pagos de clientes anteriores, no solo por nuevas altas.

## Qué haría falta para estar más seguros

### 1. Medir conversiones de los usuarios que recibieron los emails

Necesitaría saber:

- Cuántos usuarios gratuitos eran elegibles para recibir la secuencia.
- Cuántos recibieron cada email.
- Cuántos hicieron clic.
- Cuántos pasaron al plan pago.
- En qué fecha se convirtieron.
- Cuánto MRR generó cada conversión.
- Cuántos cancelaron posteriormente.

También sería útil identificar el origen de cada usuario: email, publicidad, mención del creador u otro canal.

### 2. Tener un grupo de control

La evidencia más sólida sería haber dividido aleatoriamente a los usuarios gratuitos elegibles en:

- **Grupo tratamiento:** recibe la secuencia.
- **Grupo control:** no recibe la secuencia.

Después habría que comparar, durante el mismo periodo:

- Tasa de conversión a pago.
- Ingreso o MRR por usuario.
- Retención y cancelaciones.
- Tiempo hasta la conversión.

Por ejemplo, si el 8% del grupo con emails se convierte frente al 4% del grupo control, la diferencia sería evidencia del efecto incremental de la secuencia, suponiendo que la asignación fue realmente aleatoria y que ambos grupos estuvieron expuestos de forma similar a la publicidad y a la mención.

### 3. Separar el impacto de los otros canales

Como mínimo, usaría:

- UTM o enlaces diferenciados para emails, publicidad y creador.
- Fuente de adquisición registrada por usuario.
- Comparación de conversiones entre usuarios expuestos y no expuestos a cada canal.
- Fechas exactas de exposición y conversión.

Esto ayuda a describir la atribución, aunque **los clics o las encuestas de “cómo nos conociste” no demuestran por sí solos causalidad**. El control aleatorio es mucho más fiable.

### 4. Revisar el MRR por cohortes

Separaría el cambio de MRR en:

- Nuevas altas.
- Expansiones o upgrades.
- Cancelaciones.
- Contracciones.
- Cambios de precio.

Y analizaría si los clientes convertidos durante la secuencia siguen activos después de 30, 60 o 90 días. Una secuencia puede generar altas pero no aumentar el MRR sostenible.

## Veredicto

**La secuencia es una hipótesis prometedora, no un resultado demostrado.** Marzo fue mejor que febrero, pero los datos no permiten saber qué parte del crecimiento provino de los emails. Para una conclusión causal, lo principal que falta es un grupo de control comparable o un experimento aleatorio, junto con datos de conversión y retención por usuario.