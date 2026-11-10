# Claude Fable 5.2 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 8.05 | quality: 10.0
- latency_total: 19.525s | tokens_per_second: 83.5
- input_tokens: 366 | output_tokens: 1630

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

**Conclusión: con estos datos no se puede saber si la secuencia funcionó.** Marzo fue un mes mejor, pero no hay forma de atribuir la mejora a los emails.

**Por qué no se puede saber**

1. **Hay tres causas mezcladas.** Los emails (1 de marzo), la publicidad (3 de marzo) y la mención del creador (12 de marzo) coinciden en el mismo mes. Cualquiera de las tres, o una combinación, puede explicar el aumento.
2. **La muestra es muy chica.** Pasar de 9 a 14 altas son 5 más, y con números así esa diferencia entra dentro de la variación normal entre meses, incluso sin haber hecho nada. Además, marzo tiene 3 días más que febrero.
3. **El MRR no mide la secuencia.** Es un número neto que incluye bajas, cambios de plan y altas que nunca pasaron por el plan gratuito. El +29% dice que el negocio creció, no por qué.
4. **No hay grupo de comparación.** Todos los usuarios gratuitos recibieron la secuencia, así que no sabemos qué habría pasado sin ella.

**Qué se puede revisar ya con datos existentes**

Esto no dará certeza, pero sí indicios:

- **Origen de las 14 altas:** cuántas eran usuarios gratuitos que recibieron la secuencia y cuántas entraron directo a pago o llegaron por anuncio o video. Si solo 3 de las 14 pasaron por la secuencia, su efecto máximo posible es 3.
- **Fecha de las altas:** si se concentran después del 12 de marzo, apunta al video.
- **Tasa de conversión de gratuito a pago**, comparando marzo con los meses anteriores. Importa la tasa, no el número absoluto de altas.
- **Interacción con los emails:** si quienes pagaron los abrieron, hicieron clic y pagaron poco después. Es evidencia débil, porque los más interesados abren más emails de todos modos.

Hay una complicación: quienes llegaron por el anuncio o el video y entraron al plan gratuito también recibieron la secuencia. En esos casos los efectos no se pueden separar.

**Qué haría falta para estar seguros**

Un grupo de control. De aquí en adelante, asigna al azar una parte de los nuevos usuarios gratuitos (por ejemplo, la mitad) a no recibir la secuencia y compara la tasa de conversión entre ambos grupos. Es la única forma de aislar el efecto de los emails de todo lo demás.

Con tu volumen, probablemente necesites varios meses para ver una diferencia confiable, salvo que el efecto sea muy grande.

Si me pasas el detalle de las 14 altas (fecha, origen y si recibieron la secuencia), puedo decirte cuál es el efecto máximo que podría tener la secuencia.