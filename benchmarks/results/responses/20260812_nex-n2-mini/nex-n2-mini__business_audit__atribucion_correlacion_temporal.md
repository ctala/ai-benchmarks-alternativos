# Nex-N2-Mini — business_audit/atribucion_correlacion_temporal

- model_id: `nex-agi/nex-n2-mini`
- success: True  | final: 9.28 | quality: 10.0
- latency_total: 16.03s | tokens_per_second: 165.1
- input_tokens: 244 | output_tokens: 2647

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

**Conclusión: no se puede saber con estos datos.**  
La secuencia **pudo haber ayudado**, pero los números no permiten atribuir el aumento de MRR ni las nuevas altas pagadas principalmente a los emails.

### Por qué no puedo decir que funcionó

1. **Hay confusores importantes justo en la misma ventana**
   - Publicidad pagada desde el 3 de marzo.
   - Mención en video desde el 12 de marzo.
   - Ambos eventos pueden haber aumentado tráfico, registros gratuitos y conversiones a pago.

2. **El MRR no se explica solo por nuevas altas pagadas**
   El MRR pasó de $4.100 a $5.300, un aumento de $1.200. Pero eso puede venir de:
   - Nuevas altas pagadas.
   - Menos bajas.
   - Upgrades de usuarios existentes.
   - Renovaciones.
   - Cambios de plan.
   
   La secuencia iba dirigida a usuarios gratuitos, así que no explica por sí sola todo ese aumento.

3. **Las altas pagadas subieron, pero el dato es débil**
   - Febrero: 9 altas pagadas.
   - Marzo: 14 altas pagadas.
   
   Eso es +5 usuarios. Considerando que marzo tiene más días, sería aproximadamente:
   - Febrero: 9 / 28 = 0,32 altas por día.
   - Marzo: 14 / 31 = 0,45 altas por día.
   
   Eso sugiere una mejora diaria de alrededor de 41%, pero todavía no prueba causalidad.

4. **Faltan datos clave**
   Para saber si los emails funcionaron necesitaría ver:
   - Cuántos usuarios gratuitos recibieron los emails.
   - Cuántos los abrieron o hicieron clic.
   - Cuántos usuarios gratuitos se convirtieron a pago antes y después.
   - Qué cohortes se activaron cada día.
   - Si los nuevos pagados vinieron de tráfico orgánico, publicidad, video, referrals, etc.
   - Cuánto MRR vino de nuevas altas vs. upgrades vs. reducción de churn.

### Mi conclusión práctica

Diría esto:

> “La secuencia de emails probablemente contribuyó al crecimiento, pero no puedo afirmar que fue la causa del aumento de MRR ni de las nuevas altas pagadas. Los cambios en publicidad y la mención del creador hacen que la atribución sea demasiado incierta.”

### Qué haría falta para estar más seguros

Lo ideal sería hacer una prueba controlada:

1. **Crear un grupo de control**
   - 80% de usuarios gratuitos recibe la secuencia.
   - 20% no la recibe o la recibe con retraso.
   - Comparar conversión a pago entre ambos grupos.

2. **Medir conversión por cohorte**
   Por ejemplo:
   - Usuarios gratuitos activos antes del 1 de marzo.
   - Usuarios gratuitos activos después del 1 de marzo.
   - Usuarios expuestos vs. no expuestos al email.
   - Conversión a pago en 7, 14 y 30 días.

3. **Separar el impacto del MRR**
   Hacer un puente de MRR:
   - MRR inicial.
   - Nuevas altas pagadas.
   - Upgrades.
   - Downgrades.
   - Cancelaciones.
   - MRR final.

4. **Controlar o registrar fuentes de adquisición**
   Usar UTM, códigos, formularios de origen, etc., para saber si las altas pagadas vienen de:
   - Email.
   - Publicidad.
   - Video del creador.
   - Tráfico directo.
   - Referidos.

5. **Hacer un A/B test antes de escalar**
   Si el grupo expuesto a emails convierte significativamente más que el grupo control, entonces sí podríamos decir que la secuencia funcionó.

En resumen: **hay una señal positiva, pero no suficiente para decir que la secuencia funcionó de forma causal.**