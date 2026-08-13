# Claude Opus 5 Fast — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.11 | quality: 10.0
- latency_total: 11.584s | tokens_per_second: 176.8
- input_tokens: 364 | output_tokens: 2048

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

## Conclusión corta

**No se puede saber.** Con estos datos no hay forma de atribuirle el crecimiento a la secuencia de emails, ni de descartarlo. No es que falte precisión: es que el diseño no permite separar las causas.

---

## Por qué

**1. Tres intervenciones en la misma ventana.**
Emails (1/3), publicidad (3/3) y mención de un creador (12/3). Los tres empujan en la misma dirección y se solapan en el tiempo. Cualquier número de marzo es la suma de los tres más la variación normal. No hay contrafactual.

Peor: ads y el creador **traen usuarios nuevos al plan gratuito**, que después convierten. O sea que parte del efecto que le atribuirías al email es en realidad "más gente en el embudo", no "el email convierte mejor".

**2. Los números son demasiado chicos para distinguir señal de ruido.**
9 → 14 altas. Con conteos así, la variación aleatoria mes a mes es de ±3 fácil. Si en febrero el proceso subyacente hubiera sido idéntico, ver 14 altas por puro azar tiene una probabilidad de alrededor del 6-7%. No es un resultado que sostenga una decisión.

Además marzo tiene 31 días y febrero 28: un 11% del aumento es puro calendario.

**3. El +29% de MRR es una métrica engañosa acá.**
MRR mezcla altas nuevas, churn, upgrades y cambios de precio. No sabemos precio promedio, ni cuántos usuarios gratuitos había en cada mes (el denominador). Si en marzo entraron 300 usuarios gratuitos por ads y en febrero entraron 80, tu **tasa** de conversión pudo haber *bajado* mientras el número absoluto subía.

---

## Lo que sí podés averiguar hoy, con datos que ya tenés

Hay un experimento natural escondido en tu base. Segmentá las 14 altas de marzo:

- **Grupo A: usuarios que ya estaban en el plan gratuito antes del 1 de marzo.** Estos vieron el email y *no* pudieron venir de ads ni del creador. Es el grupo limpio.
- **