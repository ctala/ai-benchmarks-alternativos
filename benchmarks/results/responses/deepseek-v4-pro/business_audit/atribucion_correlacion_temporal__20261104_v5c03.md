# DeepSeek V4 Pro — business_audit/atribucion_correlacion_temporal

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 16.28s | tokens_per_second: 67.1
- input_tokens: 235 | output_tokens: 1093

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

**Conclusión directa:**  
Con los datos que compartes **no se puede afirmar que la secuencia de emails funcionara**, aunque tampoco se puede descartar. El crecimiento en MRR (+29 %) y en altas pagas (+56 %) es real, pero ocurrió al mismo tiempo que otras dos acciones con alto potencial de impacto: la inversión en publicidad y la mención de un creador con audiencia. Los tres factores se solapan, por lo que atribuir el resultado a uno solo es una especulación.

**Por qué no podemos estar seguros:**

- **Publicidad ($400 desde el 3 de marzo):** pudo atraer tráfico nuevo que se convirtió directamente a planes pagos o a gratuitos que luego convirtieron sin haber recibido la secuencia completa.
- **Mención del creador (12 de marzo):** un pico de visibilidad puntual que pudo traer tanto altas gratuitas como de pago, distorsionando el efecto de los emails.
- **Falta de trazabilidad:** no sabemos cuántos de los 14 nuevos pagos de marzo provienen de usuarios que estaban en el plan gratuito, recibieron los emails y luego convirtieron. Tampoco conocemos la evolución del MRR por tipo de cliente (nuevos vs. existentes, upgrades vs. altas) ni la tasa de cancelación en el período.
- **Estacionalidad o efecto inercia:** sin datos de meses anteriores (tendencia natural de crecimiento), no podemos aislar el incremento orgánico que hubiera ocurrido sin intervenciones.

**Qué haría falta para estar seguros:**

1. **Atribución directa del email:**  
   - Tracking de clics en los emails con UTM o enlaces únicos.  
   - Comparar la tasa de conversión a pago del grupo que recibió y abrió los emails vs. un grupo de control (holdout) de usuarios gratuitos que no los recibió. Sin grupo de control, todo es correlación.

2. **Cohortes por fuente de adquisición:**  
   - Separar las altas pagas de marzo según su origen (email, publicidad, tráfico directo/referido tras el video).  
   - Ver cuántos venían de la base gratuita previa a marzo y cuántos eran nuevos usuarios atraídos por publicidad o el creador.

3. **Ventana temporal limpia:**  
   - Analizar el comportamiento antes, durante y después de la secuencia, idealmente con semanas sin otras campañas concurrentes. Si es posible, repetir la secuencia en otro momento sin publicidad ni menciones externas.

4. **Datos de engagement granular:**  
   - Tasa de apertura, clics y conversión por email de la secuencia.  
   - Tiempo medio desde la recepción hasta la conversión, para ver si el ritmo de altas se acelera justo tras cada envío.

**Recomendación inmediata:**  
Para la próxima prueba, aísla las variables. Por ejemplo, lanza la secuencia a un subconjunto aleatorio de usuarios gratuitos y compara con el resto. Mientras tanto, la respuesta honesta es: **no sabemos si la secuencia de emails aportó, y asumir que fue la causa sería un error de atribución.**