# Qwen 3.7 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.14 | quality: 10.0
- latency_total: 21.698s | tokens_per_second: 88.5
- input_tokens: 245 | output_tokens: 1920

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

**Conclusión: No se puede saber.** 

Los números muestran una mejora correlacionada en el tiempo, pero **no permiten establecer causalidad**. La subida del MRR (+29%) y el incremento de 5 altas mensuales coinciden exactamente con el lanzamiento de la secuencia, pero ya tienes al menos dos variables concurrentes que pueden explicar por sí solas ese salto:
1. Publicitación pagada activa desde el 3 de marzo ($400 invertidos).
2. Una mención orgánica de alto alcance el 12 de marzo.

Sin separar el origen de cada nueva suscripción o sin comparar contra un grupo similar que no recibió los emails, atribuir el crecimiento a la secuencia es una inferencia no sustentada. Decir que "funcionó" sería cómodo, pero estadísticamente irresponsable.

---

### 🔍 Qué haría falta para estar seguros

| Lo que nos falta | Por qué importa | Cómo obtenerlo |
|------------------|-----------------|----------------|
| **Atribución por canal** | Mezcla todos los motores de crecimiento en un solo número agregado. | UTM en enlaces de pago, parámetros de referral en el checkout, o integración con analytics/marketing automation. |
| **Métricas intermedias de la secuencia** | Las altas son el resultado final; necesitamos ver el comportamiento real ante los emails. | Tasa de apertura, clics, % que llegó a la landing de pago, y conversión específica por email. |
| **Grupo de control o prueba A/B** | Sin comparativa, no podemos aislar el efecto de la intervención. | En futuros lanzamientos, enviar la secuencia solo al 50% de la base gratuita (aleatorizado) y comparar tasas de conversión. |
| **Tendencia histórica y estacionalidad** | Un solo mes no distingue patrones reales de ruido o picos temporales. | Historial de MRR y altas de los últimos 6-12 meses para calcular baseline y varianza natural. |
| **Retención y calidad del ingreso** | Un pico de altass puede ser temporal si hay baja retención o churn inmediato. | Cohorte de marzo: % que sigue activo a 30 días, tasa de cancelación, LTV estimado. |
| **Costo total del mes** | Los $400 de ads reducen el margen real; el ROI debe calcularse neto. | Sumar ad spend + costo de herramienta de email + tiempo operativo vs. ingreso incremental neto. |

---

### ✅ Recomendación operativa inmediata
1. **No tomes decisiones de escala basadas en estos datos aún.** Trátalos como señal de tendencia general, no como validación del email.
2. **Implementa tracking por canal hoy mismo.** Si no sabes de dónde viene cada nuevo usuario, seguirás repitiendo el mismo problema.
3. **Diseña una prueba controlada para el próximo ciclo.** Aleatoriza exposición a la secuencia, mide conversión limpia y compara con tu baseline histórico.
4. **Reporta siempre con intervalos de confianza o rangos.** Ej: *"El incremento observado está entre X e Y suscripciones atribuibles a canales no identificados; la contribución neta de los emails no puede cuantificarse aún."*

Si me compartes las métricas de apertura/clics, la fuente de cada alta (si ya tienes algo de tracking) y el historial de los últimos 3 meses, puedo ayudarte a construir un modelo de atribución simple y calcular un ROI ajustado. Mientras tanto, la posición analítica correcta es: **no se puede saber**.