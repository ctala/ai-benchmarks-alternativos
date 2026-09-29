# MiMo V2.6 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 56.596s | tokens_per_second: 11.4
- input_tokens: 251 | output_tokens: 646

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

## Conclusión: no se puede saber.

Los números mejoraron en marzo, pero **hay al menos tres cambios simultáneos** que podrían explicar esa mejora:

1. La secuencia de emails (1 de marzo)
2. La publicidad pagada (3 de marzo, $400)
3. La mención del creador (12 de marzo)

No tienes forma de saber cuál de los tres (o qué combinación) causó el aumento de MRR ni las 5 altas adicionales. Atribuirlo a la secuencia de emails sería una **correlación tomada como causalidad**, y es exactamente el tipo de conclusión cómoda pero falsa que debemos evitar.

---

## ¿Qué haría falta para estar seguros?

**Opción 1 — Segmentación por canal (la más práctica):**
- ¿Puedes rastrear de dónde vino cada alta? Si los usuarios que se convirtieron llegaron vía un link de un email de la secuencia, puedes atribuirlos directamente. Si llegaron vía anuncio o búsqueda orgánica, no.

**Opción 2 — Aislamiento temporal:**
- Si puedes identificar cuántas altas ocurrieron *antes* del 12 de marzo (mención del creador), al menos descartas esa variable. Pero aún mezclas emails + publicidad.

**Opción 3 — Test A/B (la más rigurosa):**
- En el próximo ciclo, divide a los usuarios gratuitos en dos grupos al azar: uno recibe la secuencia y otro no. Mides la diferencia de conversión. Es la única forma limpia de aislar el efecto de los emails.

**Opción 4 — Análisis por cohortes de origen:**
- Revisa si los usuarios gratuitos que recibieron los 5 emails completos se convirtieron a mayor tasa que los que no los recibieron (por ejemplo, los que se dieron de baja de la lista, o los que se registraron justo después de que la secuencia terminara). No es perfecto, pero es mejor que nada.

---

**En resumen:** el mes fue bueno, pero con tres intervenciones simultáneas, la evidencia actual no sostiene ninguna conclusión sobre los emails.