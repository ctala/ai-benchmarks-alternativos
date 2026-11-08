# GPT-6 Astra — business_audit/atribucion_correlacion_temporal

- model_id: `openai/gpt-6-astra`
- success: True  | final: 8.06 | quality: 10.0
- latency_total: 14.759s | tokens_per_second: 37.0
- input_tokens: 224 | output_tokens: 546

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

**Conclusión: no se puede saber con estos datos si la secuencia funcionó.** Marzo mejoró respecto a febrero, pero no podemos atribuir esa mejora a los emails: también arrancó la publicidad y hubo una mención de un creador. Las tres acciones podrían haber contribuido.

### Qué muestran los números
- El MRR subió **$1.200 (+29,3%)**.
- Las altas al plan pago pasaron de **9 a 14: cinco más (+55,6%)**.

Son señales positivas del negocio, **no una prueba del efecto de la secuencia**. Además:
- Sin saber cuántos usuarios gratuitos podían convertirse cada mes, no conocemos la tasa de conversión. Más altas pueden deberse simplemente a más usuarios.
- El MRR también cambia por cancelaciones, ampliaciones o reducciones de plan y cambios de precio; no solo por nuevas altas.
- Dos meses y pocas altas no permiten establecer si el cambio supera la variación habitual.

### Qué haría falta para tener mayor certeza

**1. La prueba más sólida: un grupo de control aleatorio.**  
Dividir a los usuarios gratuitos elegibles entre quienes reciben la secuencia y quienes no la reciben, manteniendo iguales las demás condiciones. Comparar:
- Conversión a pago dentro de una ventana fija, por ejemplo, 30 días desde la asignación.
- Ingreso generado por usuario asignado y permanencia posterior.

La diferencia entre grupos permitiría estimar el efecto incremental de los emails, con su incertidumbre. Con pocas conversiones, probablemente habría que acumular más usuarios o tiempo; el tamaño necesario depende de la conversión habitual y de la mejora que quieras detectar.

**2. Para investigar lo que pasó en marzo:**
- Usuarios gratuitos elegibles y fechas de entrada en la secuencia.
- Fechas de las altas a pago y origen de adquisición: publicidad, creador, orgánico, etc.
- Entregas y clics de los emails, vinculados a las conversiones.
- Desglose del cambio de MRR: nuevas altas, cancelaciones y cambios de plan.
- Varios meses anteriores para conocer la tendencia y la variación habitual.

Esto ayudaría a reconstruir el recorrido, pero **haber recibido o pulsado un email antes de pagar no demuestra que el email causara la compra**. Una persona pudo llegar por el creador y recibir después la secuencia: los efectos pueden combinarse.

**Mi recomendación:** no declarar la secuencia ganadora ni descartarla. Tratar marzo como una mejora de causa aún desconocida y probar la secuencia con un control aleatorio.