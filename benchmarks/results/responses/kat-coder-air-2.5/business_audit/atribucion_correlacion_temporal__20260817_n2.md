# KAT Coder Air v2.5 — business_audit/atribucion_correlacion_temporal

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.13 | quality: 10.0
- latency_total: 7.207s | tokens_per_second: 189.7
- input_tokens: 245 | output_tokens: 1367

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



### Conclusión: No se puede saber.

Los datos que me pasas muestran una correlación temporal, pero **no permiten atribuir el aumento a la secuencia de emails**. Hay al menos dos factores de confusión críticos que operaron en el mismo periodo y que pueden explicar (total o parcialmente) los resultados:

1.  **Publicidad pagada:** Iniciada el 3 de marzo ($400). El tráfico pagado suele tener tasas de conversión más altas y puede haber traído nuevos suscriptores que aumentaron el MRR.
2.  **Mención de un creador:** El 12 de marzo un creador con audiencia grande habló de la comunidad. Esto genera un pico de visibilidad orgánica que es muy difícil de separar de cualquier otra campaña lanzada esa misma semana.

Además, los números que me das son agregados y no desglosados:

- **MRR pasó de $4.100 a $5.300 (+$1.200).** No sabemos cuánto vino de *nuevos suscriptores* (que pueden venir de la publicidad o la mención) vs. *upgrades de usuarios gratuitos* (lo que sí podría atribuirse a los emails).
- **Altas al plan pago:** 9 en febrero vs. 14 en marzo. Eso es un aumento de 5, pero sin saber cuántos usuarios gratuitos había en total, no podemos calcular tasas de conversión. Si la comunidad creció un 50% en marzo por la publicidad, 14 altas podrían ser incluso una *menor* tasa de conversión.

### Qué haría falta para estar seguros

Para responder con rigor, necesitaríamos:

1.  **Un grupo de control:** La única forma válida de probar la secuencia de emails es dividendo a los usuarios gratuitos en dos grupos al azar: uno que recibe los emails y otro que no (o que recibe un email de control sin el CTA de conversión). Si el grupo de emails convierte significativamente más, ahí sí podemos atribuir el efecto.
2.  **Desglose de fuentes de conversión:** Un sistema de tracking que permita saber, para cada alta al plan pago, si vino de:
   - Email de la secuencia (con UTM/parámetros)
   - Publicidad pagada
   - Mención orgánica/redes
   - Tráfico directo o recomendado
3.  **Métricas de exposición:** Cuántos usuarios gratuitos recibieron efectivamente los emails (tasa de apertura/delivery) vs. cuántos no fueron expuestos. Sin esto, no sabemos el denominador de la conversión.
4.  **Análisis de cohortes:** Seguir a los usuarios que recibieron los emails en marzo y comparar su tasa de conversión a lo largo del tiempo con una cohorte similar de febrero (antes de la campaña) o con usuarios que no la recibieron, controlando por estacionalidad.

### Mi recomendación práctica

Dado que ya lanzaste la campaña y no tuviste un diseño experimental previo:

- **No declares la secuencia como "exitosa"** basándote solo en estos números. Cualquier conclusión sería especulativa.
- **Implementa tracking inmediato** para la próxima campaña: usaUTM parameters en todos los enlaces de los emails, y asegúrate de que tu plataforma de pagos/análisis registre la fuente de cada conversión.
- **Para la próxima vez, diseña un A/B test antes de lanzar.** Es el único método que aísla el efecto de una intervención específica de otros factores externos.

Los datos muestran que marzo fue un mes mejor, pero la causa sigue siendo una incógnita. **Decir que "funcionó" sería una afirmación no sostenida por la evidencia disponible.**