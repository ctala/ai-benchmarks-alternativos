# Claude Fable 5.1 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 8.0 | quality: 10.0
- latency_total: 26.583s | tokens_per_second: 63.2
- input_tokens: 366 | output_tokens: 1679

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

**Conclusión corta: no se puede saber.** Y no es una evasiva: con estos datos no hay forma de atribuir el crecimiento a la secuencia de emails.

## Por qué no se puede concluir

**1. Tres cambios a la vez, sin forma de separarlos.**
En marzo pasaron tres cosas casi simultáneas: emails (día 1), publicidad (día 3) y la mención del creador (día 12). Cualquiera de las tres, o una combinación, puede explicar la subida. El crecimiento es consistente con "los emails funcionaron" y también con "los emails no hicieron nada y todo fue el creador". Los datos no distinguen entre esos dos escenarios.

**2. Los números son pequeños.**
Pasar de 9 a 14 altas son 5 altas de diferencia. Con cifras de ese tamaño, la variación mes a mes por puro azar puede ser fácilmente de ±3 o 4. Sin un historial de varios meses no sabemos si 14 es "mucho" o si entra dentro de lo normal para tu comunidad.

**3. El +29% de MRR no es solo altas nuevas.**
MRR es un neto: altas menos bajas, más cambios de plan. Puede que marzo tuviera menos cancelaciones por cualquier razón ajena a los emails. Sin desglosar nuevo MRR / churn / expansión, el +29% dice poco sobre conversión.

**4. Puede haber efecto en el denominador que no vemos.**
Si la publicidad y el creador trajeron muchos usuarios nuevos al plan gratuito, el pool al que le llega la secuencia creció. Más altas de pago podrían ser simplemente "más gente entrando al embudo", no "mejor conversión". La pregunta relevante es la **tasa** de conversión de gratuito a pago, no el número absoluto.

## Qué sería necesario para saberlo

**Lo mínimo (reconstruible ahora, mirando atrás):**
- Para cada una de las 14 altas de marzo: fecha de alta al plan gratuito, fecha de paso a pago, canal de origen (UTM de anuncios, referral del video, orgánico), y si recibió/abrió/clicó los emails de la secuencia.
- Altas de pago por semana: ¿se concentran después del día 12 (creador) o están repartidas desde el día 1?
- Tasa de conversión gratuito→pago de meses anteriores, para tener una línea base.
- Desglose del MRR de marzo: nuevo, churn, upgrades.

Con esto podrías decir cosas como "de las 14, 8 llegaron por el video y convirtieron en menos de 48 h, antes de recibir el email 2", lo cual ya sería informativo. Pero seguiría siendo correlación, no causa.

**Lo que realmente responde la pregunta:**
Un **grupo de control**. Elegir al azar un porcentaje de los usuarios gratuitos nuevos (por ejemplo, 30-50%) que *no* reciban la secuencia, y comparar la tasa de conversión de ambos grupos durante varias semanas. Es la única forma de aislar el efecto de los emails de todo lo demás que pase ese mes. Con una comunidad pequeña hará falta tiempo para acumular suficientes conversiones, pero es la única respuesta honesta a "¿funcionó?".

## Recomendación práctica

No lances tres cambios a la vez si quieres saber cuál funciona. Si la pregunta importa de verdad (por ejemplo, para decidir si invertir en más emails vs. más publicidad), monta el grupo de control ahora. Si no la vas a usar para decidir nada, acepta que marzo fue un buen mes por una mezcla de causas y sigue adelante, pero sin contar la secuencia como "probada".