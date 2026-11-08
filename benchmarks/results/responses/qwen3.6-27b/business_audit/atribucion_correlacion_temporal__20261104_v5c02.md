# Qwen 3.6 27B base (OpenRouter FP8) — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 43.409s | tokens_per_second: 50.4
- input_tokens: 245 | output_tokens: 2187

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
No se puede saber con los datos actuales. No hay evidencia suficiente para atribuir el crecimiento del MRR o las nuevas altas a la secuencia de emails.

**Por qué no se puede afirmar que funcionó:**
1. **Múltiples variables cambiaron a la vez:** La secuencia (1 mar), la publicidad paga (3 mar) y la mención del creador (12 mar) se solaparon en el mismo periodo. Sin aislamiento experimental, cualquier crecimiento es correlación, no causalidad.
2. **Falta de atribución:** No sabemos cuántas de las 14 altas vinieron de los emails, de los anuncios o del video. Sin parámetros de tracking (UTMs, landing pages diferenciadas, códigos únicos o datos de conversión por canal), asignar el mérito a un solo canal es una suposición.
3. **Muestra pequeña y alta variabilidad natural:** Pasar de 9 a 14 altas (+5 usuarios) en un mes con base tan reducida está dentro del rango de ruido operativo normal. No hay desviación estándar ni histórico de variación mensual para determinar si ese salto es estadísticamente significativo.
4. **El MRR y las altas no se mueven al mismo ritmo:** El MRR subió un 29%, pero las altas un ~55%. Esto indica que parte del crecimiento puede venir de cambios en el mix de planes, precios o retención, no exclusivamente de nuevas conversiones por la secuencia.

**Qué haría falta para estar seguros:**
- **Atribución técnica:** Implementar tracking por canal. Cada email debe llevar enlaces con UTM o códigos de descuento únicos para cruzar clics → registro pago.
- **Test A/B o grupo de control:** Enviar la secuencia solo al 50% de los usuarios gratuitos y comparar la tasa de conversión con el 50% que no la recibe, manteniendo el resto de variables iguales.
- **Métricas de funnel por email:** No solo aperturas/clics, sino conversión real por etapa (¿cuántos usuarios que hicieron clic en el email 3 se pagaron?).
- **Análisis de cohortes:** Seguir a los usuarios expuestos a la secuencia vs. los no expuestos durante 30-60 días para ver si el efecto se sostiene o es un pico temporal.
- **Desglose de MRR por plan:** Separar el crecimiento por tipo de suscripción para saber si el aumento viene de más cabezas o de usuarios que migraron a planes más caros.

**Recomendación operativa:**  
Mientras se implementa el tracking y un diseño experimental básico, no tomes decisiones de inversión o escalado basadas en esta correlación. Si quieres validar la secuencia en el próximo ciclo, congela o reduce temporalmente uno de los otros canales (ej. ads) y mide el delta, o haz el test A/B mencionado. 

Con los números actuales, la conclusión rigurosa es: **crecimiento sí, atribución no.**