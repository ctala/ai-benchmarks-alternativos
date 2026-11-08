# MiMo V2.6 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 7.43 | quality: 8.0
- latency_total: 31.142s | tokens_per_second: 26.4
- input_tokens: 251 | output_tokens: 821

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

## No se puede saber con estos datos

La conclusión directa es que **la secuencia de emails podría haber funcionado, pero estos números no lo demuestran ni lo descartan**. Tienes al menos tres variables cambiando en el mismo período:

1. **Secuencia de emails** (1 de marzo)
2. **Publicidad pagada** (3 de marzo, $400)
3. **Mención de un creador** (12 de marzo)

El subidón de MRR (+$1.200) y el de altas (9 → 14) son reales, pero **atribuirlo a los emails sería un error**. Cualquiera de las tres causas —o una combinación— podría explicar el aumento, y no tienes forma de separarlas con lo que has compartido.

---

### Lo que haría falta para estar seguros

**Nivel mínimo (datos que ya tienes):**
- **Tasas de apertura y clic por email** de la secuencia (open rate, CTR, especialmente en los emails con enlace a la página de pago)
- **Conversión directa**: cuántas de las 14 altas en marzo llegaron a la página de pago desde un link de la secuencia (utm, enlaces rastreables)
- **Timing**: cuántas altas ocurrieron antes del 3 (antes de la publicidad) y antes del 12 (antes de la mención). Si varias altas son del 1-2 de marzo, es evidencia a favor de los emails

**Nivel recomendado:**
- **Descompón las altas por fecha** y marca cuándo entra cada variable. Un gráfico con la línea de tiempo de altas vs. las fechas de activación de cada canal ya te da una pista razonable
- **Separa los canales de tráfico** en Google Analytics o tu herramienta: tráfico orgánico, directo, desde emails, desde publicidad

**Nivel ideal (si quieres rigor):**
- Un **A/B test** en próximos envíos: a la mitad de la lista le mandas la secuencia, a la otra mitad no, y comparas conversión a los 30 días
- **Retrospectivamente**: puedes mirar si las altas de marzo tienen un pico los días que se envió cada email de la secuencia (días 1, 3, 5, 7... según tu frecuencia)

---

### Lo que diría con los datos de hoy

> *"El MRR subió un 29% en marzo, pero lanzamos tres iniciativas simultáneamente. No puedo decir que los emails sean la causa. Lo que sí puedo decir es que cualquiera de las tres está funcionando, o todas juntas. Para saber cuánto aporta cada una, necesito rastrear las fuentes."*

Antes de repetir el experimento en abril, **implementa el tracking**. De lo contrario vas a seguir en la misma situación: un número bonito sin saber de dónde viene.