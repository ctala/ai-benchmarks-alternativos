# Muse Spark 1.3 — business_audit/atribucion_correlacion_temporal

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.42 | quality: 10.0
- latency_total: 23.831s | tokens_per_second: 96.0
- input_tokens: 235 | output_tokens: 2288

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

Con estos datos: **no se puede saber si la secuencia funcionó.**

Y es importante no decir que sí, porque el +29% suena muy convincente y puede llevar al equipo a una decisión equivocada.

Te explico por qué:

### 1. Pasaron 3 cosas a la vez, no una
El 1 de marzo lanzaste los emails, pero:
- el 3 de marzo empezaste publicidad pagada
- el 12 de marzo un creador grande te mencionó

Tienes un aumento de 9 a 14 altas al plan pago (+5 personas) y de $4.100 a $5.300 de MRR (+$1.200). Con este diseño es imposible repartir ese mérito entre emails, ads e influencer. Es correlación, no causalidad.

No tenemos contrafactual: ¿qué habría pasado en marzo *sin* emails?

### 2. Los números son demasiado pequeños para concluir
Pasar de 9 a 14 son solo 5 personas más en todo un mes.

Con volúmenes tan bajos, esa diferencia puede ser puro ruido, suerte, o que febrero tiene menos días que marzo. Febrero: 9 altas / 28 días = 0,32 por día. Marzo: 14 / 31 = 0,45 por día. No es una evidencia sólida.

No puedes atribuir un +29% de MRR a 5 altas extra sin más información.

### 3. Te falta el denominador más importante
Me das altas absolutas, pero no tasas de conversión.

¿Cuántos usuarios gratuitos había en febrero vs marzo?

La publicidad y el video probablemente trajeron muchos más usuarios gratuitos en marzo. Si la base creció mucho, pasar de 9 a 14 podría significar que la **tasa** de conversión en realidad bajó.

Sin saber: altas / total de gratuitos elegibles, no sabes nada.

### 4. El MRR no mide los emails
El MRR del 28 de febrero vs 31 de marzo incluye muchas cosas que no son los emails:
retención, churn, upgrades, downgrades, cambios de precio, gente que venía del mes anterior.

No sabemos cuánto de esos +$1.200 viene de las 14 altas nuevas y cuánto de clientes antiguos que no cancelaron.

### Qué haría falta para estar seguros

Para una empresa pequeña no necesitas estadística perfecta, pero sí esto como mínimo:

1. **Atribución a nivel usuario:** De esos 14 que se pasaron a pago en marzo, ¿cuántos recibieron/abrieron/clickearon los emails? ¿cuántos vienen de UTM de ads? ¿cuántos llegaron el 12-14 de marzo tras el video?
Mira las altas por día. Si hay un pico justo después del video, ya tienes una pista.

2. **Grupo control:** La única forma de aislar el efecto. Por ejemplo, al 50% aleatorio de gratuitos les mandas la secuencia y al otro 50% no, y comparas conversión a pago a 30 días. Con tu volumen necesitarías correrlo 2-3 meses.

3. **Desglose del MRR:** No solo MRR total. Necesitas: MRR por altas nuevas vs. expansión vs. churn evitado en feb vs mar.

4. **Pregunta directa:** Añade "¿cómo nos conociste?" en el checkout. Es imperfecto, pero barato y te separa influencer/ads de emails.

Mi recomendación: no presentes marzo como "los emails funcionaron" y no escales inversión basándote en eso. Lo honesto para el equipo es: *tuvimos un buen marzo con 3 iniciativas superpuestas, no sabemos cuál lo causó.*

Si quieres, pásame las altas por día y el origen si lo tienes, y te ayudo a ver si hay al menos una señal que apunte a una causa u otra.