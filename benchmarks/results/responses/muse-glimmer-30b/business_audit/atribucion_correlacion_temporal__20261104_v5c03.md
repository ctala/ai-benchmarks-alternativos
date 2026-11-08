# Muse Glimmer 30B — business_audit/atribucion_correlacion_temporal

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.71 | quality: 10.0
- latency_total: 15.378s | tokens_per_second: 96.4
- input_tokens: 237 | output_tokens: 1483

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

No se puede saber si la secuencia de emails funcionó con los números que me pasaste. Tienes un resultado positivo, pero no puedes atribuirlo a los emails.

Tienes 3 intervenciones solapadas en el mismo mes y sin grupo de control:

* 1 de marzo: secuencia de 5 emails a usuarios free
* 3 de marzo: inicio de publicidad pagada $400/mes
* 12 de marzo: mención de un creador con audiencia grande

Con eso el aumento de MRR de $4.100 a $5.300 +29% y las altas de 9 a 14 +55% son correlación, no causalidad. No sabes cuánto viene de emails, cuánto de ads y cuánto del creator, y cuánto sería haber ocurrido igual sin hacer nada.

Hay además inconsistencias que ya indican que no es solo altas nuevas: 5 altas extra no explican un +$1.200 de MRR a menos que el ARPU medio sea ~$240 y no haya churn. Necesitarías ver MRR por cohorte, churn y upgrades.

Para poder decir si la secuencia funcionó necesitarías al menos:

**1. Aislar la exposición**
* ¿Cuántos usuarios free estaban en el flujo el 1 de marzo y lo recibieron completo?
* Tasa de apertura, click y conversión de ese grupo vs. un grupo control que no recibió emails.
* Ideal: experimento randomizado 50/50 con holdout que nunca recibe la secuencia. Sin holdout no hay contrafactual.

**2. Atribución por canal**
* Fuente de cada alta a pago en marzo: email, ads con UTM, referral del creador, orgánico.
* Nuevos registros de usuarios free en marzo por canal. Si el creador trajo un pico de free el 12-13, esas conversiones no son de la secuencia.

**3. Métricas de conversión limpias**
* Tasa de conversión free -> pago en febrero como baseline.
* Tasa de conversión free -> pago en marzo solo para usuarios expuestos a emails y para los no expuestos.
* Tiempo de conversión: la secuencia de 5 emails puede tener efecto con lag >31 de marzo.

**4. Salud del MRR**
* Churn de marzo, upgrades/downgrades y ARPU medio por plan.
* MRR neto = nuevas altas - churn + expansión. Sin eso el MRR puede subir por retención y no por emails.

Con lo que tienes ahora la conclusión responsable es: **No hay evidencia suficiente para atribuir el crecimiento a la secuencia de emails.** 

Lo más prudente es no escalar la secuencia como ganador y montar un test controlado el próximo mes con holdout, tracking por UTM y ventana de atribución clara. Si quieres, te armo el diseño del experimento y el dashboard mínimo para medirlo.