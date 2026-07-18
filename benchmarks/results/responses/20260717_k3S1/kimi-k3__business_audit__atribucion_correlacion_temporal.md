# Kimi K3 — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.94 | quality: 10.0
- latency_total: 111.665s | tokens_per_second: 32.5
- input_tokens: 354 | output_tokens: 3627
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis exhaustivo y práctico para evaluar la efectividad de la secuencia de correos electrónicos.

## Respuesta completa

## Conclusión: no se puede saber con estos datos

Marzo fue un buen mes y eso es real. Pero **atribuir el crecimiento a la secuencia de emails es imposible** con lo que me pasas, porque lanzaste tres cosas casi a la vez:

- Secuencia de emails (1 de marzo)
- Publicidad pagada (3 de marzo)
- Mención de un creador grande (12 de marzo)

Cualquiera de las tres, sola o combinada, puede explicar +5 altas. Los datos son *compatibles* con que la secuencia funcionó, pero igual de compatibles con que no haya hecho nada y todo venga del video del creador.

## Otros problemas con la comparación

- **Sin línea base:** solo tienes un mes previo. No sabes si 9 altas era lo normal o un mes bajo, ni si la comunidad ya venía creciendo sola.
- **Meses de distinta duración:** febrero tuvo 28 días (0,32 altas/día) vs. 31 en marzo (0,45/día). Sigue habiendo subida, pero menor que el 9→14 crudo.
- **Números pequeños:** con conteos así, 9 vs. 14 puede ser en parte fluctuación aleatoria, no señal.
- **Falta el denominador:** ¿a cuántos usuarios gratuitos les llegó la secuencia? 5 altas extra sobre 100 usuarios gratis es enorme; sobre 5.000 es ruido.
- **El MRR no cuadra solo con las altas:** +$1.200 con +5 altas incrementales sugiere que hay algo más (menos churn, upgrades, planes anuales, reactivaciones). Sin churn ni precio por usuario, no puedes reconciliarlo.

## Lo que sí puedes intentar con datos que probablemente ya tienes

1. **Mira quiénes son los 14.** ¿Eran usuarios gratuitos desde antes del 1 de marzo, o gente nueva que llegó por los anuncios o el video? Esto es lo más barato y revelador.
2. **Curva diaria de altas.** ¿Se concentran después del día 12 (video)? ¿Después de qué email caen, si es que caen después de alguno?
3. **Métricas del email:** aperturas, clics y, sobre todo, ¿los que convirtieron abrieron/clicaron la secuencia?
4. **Datos de la plataforma de ads:** ¿cuántas conversiones reclama?

Ojo: incluso esto no lo resuelve del todo. Un usuario gratuito pudo ver el video del creador *y* recibir tus emails — convertiría "dentro" de la secuencia sin que el email fuera la causa.

## Para estar seguros la próxima vez

- **Grupo de control:** deja a un 10–20% aleatorio de usuarios gratuitos sin recibir la secuencia y compara tasas de conversión. Es la única forma limpia.
- **No solapes campañas:** lanza una cosa a la vez, o escalona con semanas de separación.
- **UTM en los enlaces** de cada email para rastrear la conversión hasta el pago.
- **Define el éxito antes de lanzar:** "queremos que X% de los gratuitos que reciben la secuencia conviertan en 30 días", no mirar el MRR total después.
- **Acumula 3–6 meses de base** de altas y MRR para saber qué es variación normal.

**Resumen:** algo funcionó en marzo, y la secuencia no fracasó visiblemente. Pero decir "la secuencia funcionó" sería una conclusión que estos datos no sostienen. Si me pasas el desglose de quiénes convirtieron y la curva diaria, te puedo dar una respuesta menos incómoda.