# Claude Sonnet 5.5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 8.44 | quality: 10.0
- latency_total: 17.322s | tokens_per_second: 112.6
- input_tokens: 366 | output_tokens: 1950

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

**Conclusión: con estos datos no se puede saber si la secuencia funcionó.** Es plausible que ayudara, pero los números no lo demuestran ni permiten estimar cuánto aportó.

## Por qué no se puede concluir

1. **Tres cambios simultáneos.** En marzo coinciden la secuencia (1 mar), la publicidad (3 mar, $400) y el video del creador (12 mar). Los tres empujan hacia el mismo resultado, y con una sola serie mensual no hay forma de separarlos.

2. **El video y los anuncios traen usuarios nuevos.** Más tráfico significa más registros gratuitos y más altas, con o sin emails. Si esos usuarios además entran a la secuencia, el efecto del email queda mezclado con el del tráfico.

3. **La diferencia es pequeña para sacar conclusiones.** Pasar de 9 a 14 altas son 5 altas más. Con conteos tan bajos, una variación así puede darse por azar de un mes a otro. No sé cuál era tu variabilidad habitual, pero con un solo mes previo no hay línea base.

4. **No sabemos la tendencia previa.** Si el MRR ya venía creciendo, parte del +29% podría haber ocurrido igual. Un mes anterior no basta para saberlo.

5. **El MRR neto mezcla cosas.** El +$1.200 incluye altas, bajas (churn) y posibles cambios de plan. Además, por mi cuenta: 14 altas explicando +$1.200 netos implica unos $86 o más por alta incluso sin ninguna baja. Si tu plan cuesta bastante menos, algo no cuadra (upgrades, planes anuales, otros ingresos), y conviene revisarlo antes de atribuir nada.

## Qué haría falta para estar seguros

**Con datos que probablemente ya tienes:**
- **Origen de cada una de las 14 altas:** ¿eran usuarios gratuitos que ya existían antes del 1 de marzo, o registros nuevos de marzo? Solo los primeros son un caso razonable para atribuir al email.
- **Fuente de adquisición (UTM, referrer):** cuántos vienen de anuncios, del video o de orgánico.
- **Métricas de la secuencia:** aperturas, clics y altas de quienes hicieron clic en el enlace de upgrade. Si pocas altas pasaron por los emails, el efecto es pequeño.
- **Timing:** ¿las altas ocurren días después de cada email, o se concentran tras el 12 de marzo (video) y el 3 de marzo (anuncios)?
- **Historial de 6 a 12 meses** de altas y MRR, para ver tu rango normal.
- **Churn de marzo** frente a meses anteriores.

**Para saberlo con rigor hacia adelante:**
- **Grupo de control (holdout):** deja un 10–20% de los usuarios gratuitos sin recibir la secuencia y compara la conversión entre ambos grupos en el mismo período. Es la única forma limpia de aislar el efecto del email, porque anuncios y video afectan a ambos grupos por igual.
- Si no quieres un holdout, al menos no lances varias iniciativas a la vez.

## Lo que sí puedes decir hoy

"Marzo fue un buen mes y la secuencia pudo contribuir, pero también hubo anuncios y un video con audiencia grande, así que no puedo atribuirle el crecimiento." Si revisas el origen de las altas, probablemente tengas una respuesta parcial en un par de horas. Pásame esos datos y lo afinamos.