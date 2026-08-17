# Tencent Hy3 — business_audit/atribucion_correlacion_temporal

- model_id: `tencent/hy3`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 64.708s | tokens_per_second: 39.5
- input_tokens: 273 | output_tokens: 2554

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

Como analista de datos, mi prioridad es proteger al equipo de gastar presupuesto o esfuerzo basándose en ilusiones. Viendo los números que me pasaste, mi conclusión es tajante: **no se puede saber si la secuencia de emails funcionó.** 

Decir que "sí funcionó" porque el MRR subió un 29% sería una respuesta cómoda, pero estadísticamente falsa con la información disponible.

### Por qué no se puede concluir que funcionó
1. **Falta de aislamiento de variables (Ruido en el experimento):** Activaste la secuencia el 1 de marzo, pero el 3 de marzo metiste publicidad paga y el 12 de marzo tuviste un impacto orgánico enorme (el creador con audiencia). El aumento en el MRR y las altas ocurrió en un mes donde al menos *tres* variables de crecimiento estaban activas a la vez. Es imposible saber qué porcentaje de esas 14 altas vino de los emails, de los ads o del video.
2. **Datos agregados, no segmentados:** No me diste cuántos de esos 14 nuevos usuarios de marzo eran usuarios del plan gratuito (que recibieron los emails) frente a usuarios totalmente nuevos (que llegaron por ads o el video). Si los 14 eran todos nuevos de afuera, los emails a los gratuitos no convirtieron ni un peso.
3. **Sin línea base ni grupo de control:** No sabemos cuál era la tasa de conversión histórica de gratuitos a pagos *antes* de los emails, ni si se hizo un test A/B (por ejemplo, enviar los emails solo a la mitad de los gratuitos y a la otra mitad no). Sin grupo de control, cualquier "mejora" es solo una suposición.

### Lo que los datos SÍ dicen (y lo que no)
*   **Sí dicen:** Que marzo fue un mes globalmente mejor que febrero en revenue y altas.
*   **NO dicen:** Que la secuencia de emails sea la causa de esa mejora. Atribuirle el mérito a los emails sin más pruebas nos puede llevar a creer que tenemos una máquina de conversión cuando en realidad solo compramos tráfico o surfeados una oleada de reputación.

### Qué haría falta para estar seguros
Para poder afirmar con datos que la secuencia funciona, necesitamos implementar esto en el futuro (o rastrear lo que queda de datos de marzo):
1. **Atribución y UTM tracking:** Si los anuncios y el video tenían enlaces con parámetros UTM, podemos cruzar las fuentes de tráfico con las conversiones. Si no se hizo, ya perdimos esa visibilidad para marzo y no podemos separar el grano de la paja.
2. **Cohortes de usuarios:** Saber exactamente cuántos usuarios gratuitos recibieron los emails, cuántos los abrieron, y de esos, cuántos se pasaron a paga. Comparar eso con la tasa de conversión de febrero (mes sin emails).
3. **Grupo de control (A/B Test):** Para la próxima vez, no enviar los emails a una porción representativa (ej. 20%) de la base gratuita. Si el grupo que recibe emails convierte a un % significativamente mayor que el grupo que no los recibe, ahí sí podemos decir "la secuencia funciona".
4. **Granularidad temporal:** Si tuviéramos las altas diarias, podríamos ver si hubo un pico de conversiones justo los días posteriores a los emails (1 al 5 de marzo) antes de que entraran en juego los ads y el video. Pero con un número mensual total, eso está ciego.

**Veredicto del equipo de datos:** No celebremslo ni lo usemos como caso de éxito en la presentación del mes. Marzo tuvo demasiado "ruido" publicitario y de terceros como para aislar el efecto del email. Prioricemos montar tracking y grupos de control antes del próximo lanzamiento para no seguir tirando flechas en la niebla.