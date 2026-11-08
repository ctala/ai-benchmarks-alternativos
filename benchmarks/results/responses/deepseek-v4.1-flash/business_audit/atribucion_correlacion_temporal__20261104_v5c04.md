# DeepSeek V4.1 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 52.202s | tokens_per_second: 92.5
- input_tokens: 261 | output_tokens: 4829

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

**Conclusión directa: no se puede saber si la secuencia de emails funcionó.**  
Con los datos que hay, el crecimiento es compatible con que la secuencia haya ayudado, pero también con que no haya hecho nada, o con que el impulso real haya venido de la publicidad y/o de la mención del creador. Decir “funcionó” sería una conclusión cómoda, pero no sostenida por los datos.

### Por qué no se puede atribuir

1. **Hay tres intervenciones solapadas en marzo**  
   - 1 de marzo: secuencia de emails.  
   - 3 de marzo: publicidad pagada.  
   - 12 de marzo: mención de un creador grande.  
   No hay forma de separar el efecto de cada una con estos números agregados.

2. **No hay grupo de control**  
   No sabés qué habría pasado con los usuarios del plan gratuito si no hubieran recibido la secuencia. Sin contrafactual, el +29% de MRR no prueba causalidad.

3. **MRR es una métrica agregada y sucia**  
   El MRR sube o baja por altas, bajas, upgrades, downgrades, cambios de precio, renovaciones, churn, etc. No sabemos cuánto del +$1.200 viene de nuevos pagos, de usuarios que ya existían, o de menor churn.

4. **No sabemos qué pasó con los usuarios del plan gratuito**  
   No tenemos: cuántos free users recibieron la secuencia, cuántos la abrieron, cuántos hicieron clic, cuántos convirtieron a pago, ni en qué fechas. Las 14 altas de marzo pueden venir de ads, del creador, de free users, o de gente que nunca vio la secuencia.

5. **Febrero y marzo no son comparables**  
   Febrero tiene 28 días y marzo 31. Además, marzo tuvo campañas que febrero no. Comparar 9 altas contra 14 mezcla días, estacionalidad y canales nuevos.

### Qué sí se puede decir

- Hubo crecimiento en marzo.
- Es **posible** que la secuencia haya contribuido.
- No hay evidencia suficiente para afirmar que la secuencia causó ese crecimiento.
- Si todas las altas ocurrieron después del 12 de marzo, la mención del creador se vuelve una explicación muy fuerte. Si ocurrieron antes del 3, la secuencia gana plausibilidad. Pero incluso así, faltaría control.

### Qué haría falta para estar seguros

1. **Experimento aleatorio (A/B test)**  
   Dividir a los free users elegibles en dos grupos:
   - Grupo A: recibe la secuencia.
   - Grupo B: no la recibe, o recibe una secuencia placebo/versión anterior.  
   Medir conversión free → pago a 30/60/90 días y MRR incremental.

2. **Datos a nivel usuario**  
   Para cada usuario: fecha de alta free, exposición a cada email, aperturas, clics, fecha de conversión, plan, MRR generado, fuente de adquisición, si vio el video del creador, si vino de publicidad.

3. **Métrica primaria clara**  
   No MRR total. La métrica sería: **tasa de conversión free → pago incremental** y **MRR incremental atribuible a la secuencia**, comparando tratamiento vs control.

4. **Aislar o controlar otros canales**  
   - Holdout para publicidad: un grupo que no vea ads.  
   - UTM/código para la mención del creador.  
   - Si no se puede aislar, usar modelos de diferencia en diferencias o matching, pero son más débiles que un experimento.

5. **Tamaño muestral suficiente**  
   Si la comunidad es chica, un A/B test puede no dar señal clara. En ese caso, la respuesta honesta sigue siendo “no se puede saber” o hay que esperar más datos.

### Si no podés hacer un experimento ahora

Lo mínimo sería un **holdout**: dejar un 10–20% de free users sin recibir la secuencia y comparar su conversión contra los que sí la reciben. Sin algo así, cualquier conclusión fuerte es fe.

**En resumen:** la secuencia *pudo* haber funcionado, pero con estos datos no podés demostrarlo. Para saberlo necesitás asignación aleatoria, grupo control y datos por usuario. Sin eso, lo correcto es decir: “no se puede saber todavía”.