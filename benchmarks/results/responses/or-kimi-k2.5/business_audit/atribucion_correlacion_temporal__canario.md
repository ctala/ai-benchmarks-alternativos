# Kimi K2.5 — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 44.384s | tokens_per_second: 38.5
- input_tokens: 270 | output_tokens: 1709

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

**Conclusión: No se puede saber.** Con los datos actuales, atribuir el crecimiento a la secuencia de emails sería una conjetura, no un análisis.

## Por qué no podemos afirmar que funcionó

Tienes **tres variables cambiando simultáneamente** en un período de 31 días:

1. **Emails automáticos** (1 marzo)
2. **Publicidad pagada** ($400 desde 3 marzo) 
3. **Mención de influencer** (12 marzo)

Las 14 altas de marzo podrían desglosarse así:
- 0 de emails + 14 del influencer
- 14 de emails + 0 del influencer  
- 5 de emails + 5 de ads + 4 del influencer
- **Cualquier combinación posible**

Además, careces de:
- **Grupo de control**: Usuarios del plan gratuito que NO recibieron los emails para comparar tasas de conversión
- **Atribución**: No sabes cuántos nuevos pagados venían de cada canal (¿preguntaste "¿cómo nos conociste?" en el checkout?)
- **Contexto histórico**: ¿Cuántas altas tenías en enero? ¿noviembre? El crecimiento podría ser simplemente tendencia natural

## Qué haría falta para estar seguros

**Para una respuesta definitiva:**
1. **Test A/B** (o cohorte de control): Hubieras necesitado dividir tu base de usuarios gratuitos en dos grupos iguales aleatoriamente, mandarle emails solo a uno, y comparar tasas de conversión al mes
2. **Tracking por UTM**: Que cada email tuviera links con parámetros únicos para rastrar conversiones atribuibles específicamente a esa secuencia
3. **Datos desagregados**: Saber exactamente qué día se produjo cada alta en marzo (¿fueron 10 altas el 13 de marzo post-influencer? Eso cambiaría todo)
4. **Tasa de conversión base**: Saber cuántos usuarios gratuitos tenías el 1 de marzo (si tenías 100, 14 conversiones es brutal; si tenías 2,000, es mediocre y probablemente no fueron los emails)

**Para una respuesta probable (más realista):**
- Comparar el **porcentaje de conversión** de usuarios que abrieron los emails vs. los que no (aunque esto tiene sesgo de auto-selección)
- Analizar los **clicks** en los CTAs de los emails y ver cuántos llevaron a upgrades en las 48h siguientes
- Comparar marzo no con febrero, sino con el **mismo mes del año pasado** (ajustando por estacionalidad)

## Mi recomendación práctica

**No tomes decisiones sobre la secuencia de emails basándote en estos números.** Podrías estar manteniendo algo que no funciona o, peor, descartando algo que sí funciona pero fue opacado por el influencer.

**Próximo paso:** Si aún tienes usuarios gratuitos sin exponer a la secuencia actual, pausa temporalmente los emails para ese grupo (como control) o implementa atribución "self-reported" preguntando en el proceso de pago: *"¿Qué te impulsó a unirte hoy?"* con opciones: "Email recibido", "Publicidad", "Recomendación de [nombre del influencer]", "Otro".

Sin eso, estás volando a ciegas.