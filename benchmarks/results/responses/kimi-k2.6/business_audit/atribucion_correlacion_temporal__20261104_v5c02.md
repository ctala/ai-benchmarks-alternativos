# Kimi K2.6 — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.43 | quality: 10.0
- latency_total: 42.06s | tokens_per_second: 57.8
- input_tokens: 270 | output_tokens: 2431

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

 **No se puede saber.** Y es importante que no te diga lo contrario.

El crecimiento de marzo es real, pero con los datos que tienes **es imposible atribuirlo a la secuencia de emails**. De hecho, si tuviera que apostar, diría que la mención del creador grande (12 de marzo) o la publicidad pagada (3 de marzo) probablemente explican una parte más grande de esas 5 altas extras que los emails, pero incluso eso es una especulación, no una conclusión de datos.

### ¿Por qué no se puede saber?

1. **Tres variables cambiaron al mismo tiempo.** Lanzaste emails, pagaste ads y recibiste una mención de influencer todo en la misma ventana. Los datos que tienes no permiten separar el efecto de cada uno. Es como cambiar la dieta, el entrenamiento y los suplementos el mismo día y luego preguntarse cuál funcionó.

2. **No hay grupo de control.** Necesitas una cohorte de usuarios gratuitos que *no* recibiera los emails para comparar su tasa de conversión. Sin eso, no sabes si esos usuarios se habrían convertido de todos modos.

3. **La muestra es demasiado pequeña.** Pasaste de 9 a 14 altas. Una diferencia de solo 5 personas. En números tan bajos, una sola conversión "de suerte" o por el influencer mueve la aguja un 20%. Eso es ruido, no señal.

4. **No sabes de dónde vinieron esas 14 altas.** ¿Eran usuarios gratuitos previos que recibieron tus emails? ¿O eran personas nuevas que llegaron por el anuncio o el video del creador? El MRR creció, pero podría ser puramente por tráfico nuevo, no por conversión de la base gratuita.

5. **El corte de fechas esconde un sesgo.** Comparaste 28 días de febrero contra 31 días de marzo. Eso ya te da ~10% más de "tiempo de venta" en marzo antes de mirar ninguna otra variable.

### ¿Qué haría falta para estar seguros?

Para poder decir "la secuencia funcionó" necesitarías, como mínimo, una combinación de esto:

- **Experimento con control:** La próxima vez, divide tu base gratuita en dos grupos aleatorios (A y B). Solo el grupo A recibe la secuencia. Comparas tasas de conversión. Eso es el estándar mínimo.
- **Atribución directa en el checkout:** Pregunta en el momento de pago "¿cómo te enteraste?" o usa URLs con `utm_source=email_automation` en todos los botones de la secuencia para rastreo exacto.
- **Desglose temporal:** ¿Cuánde se dieron de alta esas 14 personas en marzo? ¿Fueron antes o después del 12 de marzo (la mención del creador)? ¿Hubo picos justo después de enviar alguno de los 5 emails?
- **Baseline histórico:** ¿Cuántas altas tenías en enero, diciembre, noviembre? Si históricamente fluctúas entre 8 y 11 y de pronto saltas a 14 en el mes con influencer, la historia se cuenta sola.
- **Métricas intermedias de los emails:** ¿Cuántos abrieron, clickearon e iniciaron checkout desde esos correos? Si nadie clickeó, no fueron los emails.
- **Análisis de cohorte:** De las 14 altas de marzo, ¿cuántas eran cuentas creadas antes del 1 de marzo (usuarios gratuitos existentes)? Si solo 2 o 3 eran antiguos, los emails no fueron el motor.

### Mi recomendación operativa

**No declares victoria de los emails todavía.** Usa el crecimiento de marzo como evidencia de que *el negocio está creciendo*, pero invierte los próximos 30 días en instalar atribución básica (UTMs en emails, pregunta en checkout, grupo de control en la siguiente secuencia).

Si necesitas justificar el trabajo hecho, puedes decir: *"Marzo creció, pero hubo tres iniciativas simultáneas. Vamos a aislar la secuencia de emails en abril para medir su impacto real antes de escalarla."* Eso protege tu credibilidad y la del equipo.

¿Tienes acceso a alguno de esos datos adicionales (fechas exactas de las 14 altas, aperturas de emails, o de dónde viene el tráfico de pago)? Con eso podríamos al menos hacer una hipótesis más informada, aunque seguiría sin ser una certeza.