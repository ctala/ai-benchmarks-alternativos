# DeepSeek V3 — business_audit/atribucion_correlacion_temporal

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.94 | quality: 10.0
- latency_total: 18.725s | tokens_per_second: 36.5
- input_tokens: 235 | output_tokens: 684

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

**Conclusión: No podemos atribuir el crecimiento de marzo a la secuencia de emails con la información actual.**

**Explicación detallada:**

1. **Tienes tres intervenciones simultáneas en marzo:**
   - Secuencia de emails (lanzada el 1 de marzo)
   - Campaña de publicidad (comenzó el 3 de marzo, $400 invertidos)
   - Mencion orgánica de un creador (ocurrió el 12 de marzo)

2. **Los datos muestran mejoras, pero sin aislamiento:**
   - Aumento del MRR: $1.200 (+29%)
   - Aumento en altas: de 9 a 14 (+56%)
   - **No podemos saber** qué porcentaje de estas altas vinieron de:
     - La secuencia de emails
     - La publicidad pagada
     - La mención viral
     - Fuentes orgánicas existentes

3. **Problemas metodológicos:**
   - No hay grupo de control (usuarios gratuitos que NO recibieron la secuencia)
   - No hay tracking de qué altas específicas vinieron de cada fuente
   - La secuencia comenzó casi al mismo tiempo que otras intervenciones

**Para estar seguros, necesitarías:**

1. **Diseño experimental limpio:**
   - Dividir aleatoriamente tu base gratuita en dos grupos:
     - Grupo A: Recibe la secuencia de emails
     - Grupo B: No la recibe (grupo de control)
   - Medir conversión a pago en ambos grupos durante el mismo período

2. **Datos de atribución:**
   - Implementar UTM parameters o tracking específico en los emails
   - Preguntar en el onboarding "¿Cómo te enteraste?" con opciones específicas
   - Cruzar datos de altas con aperturas/clics de la secuencia

3. **Métricas adicionales necesarias:**
   - Tasa de apertura y clics de la secuencia
   - Churn rate (¿se cancelaron más suscripciones?)
   - MRR de las altas específicas de la secuencia vs otras fuentes
   - ROI de cada canal ($400 en ads vs retorno de esas altas específicas)

**Recomendación inmediata:**
Si vas a hacer otra secuencia en el futuro, implementa un test A/B desde el día 1. Mientras tanto, podrías:
- Revisar analytics para ver si hubo un pico de visitas/registros alrededor del 12 de marzo (por la mención del creador)
- Calcular si las 5 altas adicionales justifican los $400 en ads (¿cada alta vale más de $80 en LTV?)
- Enviar una encuesta a las altas de marzo preguntando qué los motivó a unirse

**Conclusión final:** Es probable que la combinación de los tres factores (emails + ads + mención viral) causara el crecimiento, pero sin mejor tracking, no puedes atribuir el éxito específicamente a la secuencia de emails.