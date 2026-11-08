# Kimi K2 — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 19.436s | tokens_per_second: 36.8
- input_tokens: 271 | output_tokens: 715

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

## Conclusión directa: **No se puede saber**

Los datos que tienes **no permiten atribuir** el crecimiento a la secuencia de emails. De hecho, hay señales que sugieren que probablemente **no fue el factor principal**.

---

## Por qué no se puede saber

| Problema | Explicación |
|----------|-------------|
| **Múltiples intervenciones simultáneas** | Tres cosas cambiaron casi al mismo tiempo: emails (1 mar), publicidad (3 mar) y mención de influencer (12 mar) |
| **El timing no cuadra** | La mayoría del crecimiento de MRR (+$1,200) ocurrió cuando la publicidad y el influencer ya estaban activos, no en los primeros días de marzo |
| **Sin grupo de control** | No sabes qué hubiera pasado sin los emails |
| **Métrica débil** | "Altas al plan pago" no dice de dónde vienen (¿orgánico? ¿publicidad? ¿referido del influencer?) |

---

## Lo que sí podemos razonar

La subida de **9 a 14 altas (+56% en volumen)** con un crecimiento de MRR del **29%** sugiere que las nuevas altas fueron en planes **más baratos** que las de febrero, o que hubo bajas que compensaron parte del crecimiento. Esto es consistente con tráfico de publicidad o influencer (que suele convertir en planes iniciales) más que con nurturance de usuarios gratuitos existentes (que tienden a convertir en planes más altos si ya conocen el valor).

---

## Qué necesitarías para estar seguros

| Dato | Por qué importa |
|------|---------------|
| **Fuente de cada alta** | Tracking de UTM o pregunta en checkout: "¿cómo nos conociste?" |
| **Conversión del funnel de emails** | Tasa de apertura, clic, y conversión a pago **solo de quienes recibieron la secuencia** |
| **Grupo de control** | Usuarios gratuitos que NO recibieron los emails en el mismo período |
| **Cohortes diarias/semanales** | ¿Hubo pico de conversiones el 1-5 de marzo (emails) o el 12-15 (influencer)? |
| **Costo de adquisición por canal** | Si gastaste $400 en ads, ¿cuántas altas atribuibles generó? |

---

## Hipótesis provisional (con baja confianza)

La secuencia de emails probablemente **contribuyó marginalmente**, pero el crecimiento de marzo se explica mejor por la combinación de publicidad + mención del influencer. 

**Si quieres validar los emails:** pausa publicidad e influencer por 2-4 semanas y mide conversión orgánica con y sin la secuencia activa.

¿Tienes acceso a datos de fuentes de tráfico o atribución de las altas de marzo?