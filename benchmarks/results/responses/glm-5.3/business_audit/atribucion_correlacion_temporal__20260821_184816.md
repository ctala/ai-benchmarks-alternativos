# GLM 5.3 — business_audit/atribucion_correlacion_temporal

- model_id: `z-ai/glm-5.3`
- success: True  | final: 6.87 | quality: 8.0
- latency_total: 69.878s | tokens_per_second: 70.7
- input_tokens: 235 | output_tokens: 4942

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

**Conclusión: no se puede saber.** Marzo fue un buen mes, pero estos datos son consistentes con que la secuencia funcionó, con que no hizo nada, y con que funcionó poco mientras otras cosas empujaban. Hay tres problemas:

**1. Tres cambios simultáneos.** Emails (1/3), ads (3/3), mención del creador (12/3). Cualquiera de los tres, por sí solo, podría explicar las +5 altas: $400 en publicidad a un CAC razonable dan para varias conversiones, y una mención con audiencia grande suele producir un pico. Cuando hay varias explicaciones suficientes, el total del mes no permite distinguir entre ellas.

**2. Los números son demasiado chicos.** Con conteos así de bajos, saltar de 9 a 14 pasa seguido por puro azar (la variación natural mes a mes a este nivel es de ±3-4). Además, no tengo historia: si los últimos meses fueron 9-10-8-11-9, marzo no se ve excepcional; si fueron 9-9-9-9-9, es otra conversación.

**3. MRR es la métrica equivocada para esta pregunta.** Los +$1.200 incluyen upgrades de usuarios ya pagos, cambios en churn, quizás planes anuales. La secuencia apunta a conversión free→pago, así que la métrica correcta es la *tasa* de conversión, no MRR ni altas en bruto. Y si el video del creador trajo muchos usuarios gratis nuevos, el embudo se agrandó: 14 altas sobre una base mucho mayor puede ser una tasa *peor* que 9 sobre una chica.

### Qué se puede hacer con lo que ya existe (análisis retrospectivo, imperfecto pero útil)

- **Línea de tiempo diaria de altas** con las tres fechas marcadas. Un pico después del 12 apunta al creador. Ojo con dos sesgos: solo tienes 2 días "limpios" (1-2/3) antes de que entren los ads, y el efecto de los emails gotea durante semanas en vez de picar, así que este análisis tiende a favorecer a los ads y al creador por construcción.
- **Atribución por fuente**: UTMs en los links de los emails, conversiones reportadas por la plataforma de ads, referentes del tráfico del video. ¿De dónde vinieron las 14?
- **Métricas del email**: entregas, aperturas, clicks, conversiones desde links del email.
- **Descomposición del MRR**: nuevo vs. expansión vs. churn. Y dime el precio del plan: si cuesta $30/mes, las 14 altas explican ~$420 de los $1.200 — el resto no tendría nada que ver con la secuencia.
- **Comparar cohortes**: usuarios free que existían antes del 1/3 (exposición completa a la secuencia) vs. llegadas después (exposición parcial, mezclada con la audiencia del creador — que también recibió emails, así que hasta eso está entrelazado).

### Qué haría falta para estar seguros (para la próxima)

- **Grupo de control**: excluir aleatoriamente un 15-20% de los usuarios free de la secuencia y comparar tasas de conversión tras 4-6 semanas. Es la única forma limpia de responder esta pregunta. Con tus volúmenes va a requerir paciencia, pero da una respuesta real.
- **No lanzar dos iniciativas la misma semana** si quieres poder leer el efecto de alguna.

Una última cosa para separar del ruido: el +29% de MRR es un resultado real y bueno. El problema no es el resultado — es que hoy no se le puede poner nombre y apellido. Si me pasas las altas diarias con fuente y el desglose de MRR, hago el análisis retrospectivo y al menos acotamos el rango de lo que la secuencia pudo haber aportado.