# GLM 5 — business_audit/atribucion_correlacion_temporal

- model_id: `z-ai/glm-5`
- success: True  | final: 8.63 | quality: 10.0
- latency_total: 33.697s | tokens_per_second: 51.8
- input_tokens: 235 | output_tokens: 1747

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

Mi conclusión directa es: **No se puede saber.** 

Los números muestran que marzo fue un mes excelente para el negocio (el MRR creció un 29% y las altas pagas pasaron de 9 a 14), pero atribuir ese éxito a la secuencia de emails sería una conclusión falsa y peligrosa para el equipo.

**Por qué no podemos concluir que fue la secuencia de emails:**

En marzo lanzaste tres variables distintas casi al mismo tiempo:
1. Secuencia de emails (1 de marzo).
2. Tráfico pagado (3 de marzo).
3. Mención de un creador grande (12 de marzo).

Cualquiera de esas tres cosas (o la combinación de las tres) puede ser la responsable del salto de 9 a 14 altas. Las nuevas altas podrían venir directamente de la publicidad o del video del creador, sin que los usuarios hayan pasado siquiera por la secuencia de emails. Si damos por bueno el sistema de emails y en abril decides pausar la publicidad o el creador deja de dar visibilidad, las altas podrían desplomarse y no entenderías por qué.

**Qué haría falta para estar seguros:**

Para aislar el efecto de la secuencia de emails y dar una conclusión respaldada por datos, necesitaríamos lo siguiente:

1. **Atribución de las 14 altas:** ¿Cuántas de esas 14 altas venían de usuarios que estaban en el plan gratuito y pasaron por la secuencia de emails? Si 12 altas vinieron directamente del anuncio pago o del video del creador (alta directa al plan pago), la secuencia de emails tuvo un impacto nulo.
2. **Tasa de conversión de la cohorte de emails:** ¿Cuántos usuarios gratuitos había al 1 de marzo y cuántos de ellos convirtieron a pago tras recibir los 5 emails? Esa tasa hay que compararla con la tasa de conversión histórica de los usuarios gratuitos en febrero (cuando no había secuencia).
3. **Serie temporal de las altas:** ¿En qué fechas exactas de marzo se dieron las 14 altas? Si la mayoría se concentraron entre el 12 y el 15 de marzo, es altamente probable que el impulsor principal haya sido la mención del creador. Si se dieron de forma paulatina a lo largo del mes, la secuencia de emails podría tener más peso.
4. **Grupo de control (ideal para futuros lanzamientos):** La próxima vez que lances una secuencia, deja a un 10% o 20% de los usuarios gratuitos sin recibir los emails. Así podremos comparar directamente si el grupo que recibe los emails convierte más que el que no los recibe, aislando el efecto de cualquier otra campaña que tengas activa.

En resumen: los datos agregados de final de mes no sirven para evaluar una variable específica cuando hay múltiples factores en juego. Necesitamos desglosar el origen de esas 14 altas y la tasa de conversión específica de quienes recibieron los correos.