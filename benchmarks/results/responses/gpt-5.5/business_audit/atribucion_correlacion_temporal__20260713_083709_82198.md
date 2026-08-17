# GPT-5.5 — business_audit/atribucion_correlacion_temporal

- model_id: `gpt-5.5`
- success: True  | final: 5.17 | quality: 5.74
- latency_total: 23.657s | tokens_per_second: 55.6
- input_tokens: 224 | output_tokens: 1316

## Respuesta completa

Conclusión: **no se puede afirmar que la secuencia de emails funcionó** con estos datos.

Lo que sí podemos decir es:

- En marzo mejoraron las métricas:
  - MRR: de **$4.100 a $5.300**, +$1.200 / +29%
  - Altas al plan pago: de **9 a 14**, +5 altas / +56%
- Pero en marzo pasaron **tres cosas a la vez**:
  1. Lanzaste la secuencia de emails el 1 de marzo.
  2. Empezaste publicidad paga el 3 de marzo.
  3. Un creador grande mencionó la comunidad el 12 de marzo.

Por lo tanto, el aumento podría venir de los emails, de la publicidad, del creador, de una combinación de los tres, o incluso de variación normal por tener números pequeños.

Mi lectura sería:

> Hay una mejora en marzo, pero no hay evidencia suficiente para atribuirla a la secuencia de emails. La secuencia pudo haber ayudado, pero los datos actuales no permiten saber cuánto, ni siquiera si fue el factor principal.

Además, las altas pasaron de 9 a 14. Es una mejora, pero estamos hablando de **solo 5 altas adicionales**. Con volúmenes tan pequeños, una mención externa o unos pocos usuarios muy motivados pueden mover bastante el resultado.

## Qué haría falta para estar seguros

### 1. Un grupo de control

La forma más limpia sería hacer un experimento:

- Tomar usuarios del plan gratuito.
- Dividirlos aleatoriamente en dos grupos:
  - Grupo A: recibe la secuencia de emails.
  - Grupo B: no recibe la secuencia, o recibe la comunicación habitual.
- Comparar la conversión a pago entre ambos grupos.

Ejemplo:

| Grupo | Usuarios gratis | Conversiones a pago | Tasa de conversión |
|---|---:|---:|---:|
| Recibieron emails | 1.000 | 40 | 4,0% |
| No recibieron emails | 1.000 | 25 | 2,5% |

Ahí sí podrías estimar el efecto incremental de la secuencia.

### 2. Medir conversiones por fuente

Necesitarías saber de dónde vinieron las altas de marzo:

- Usuarios que hicieron clic desde emails.
- Usuarios que vinieron de publicidad.
- Usuarios que vinieron por la mención del creador.
- Usuarios orgánicos/directos.
- Usuarios que ya estaban en el plan gratuito antes de marzo versus nuevos usuarios registrados en marzo.

Si 10 de las 14 altas vinieron de enlaces con UTM del email, sería una señal fuerte. Si 9 vinieron desde el video del creador, la historia cambia bastante.

### 3. Mirar cohortes de usuarios gratuitos

La pregunta correcta no es solo “¿subieron las altas?”, sino:

> De los usuarios gratuitos que ya existían antes del 1 de marzo, ¿convirtieron más después de recibir la secuencia?

Por ejemplo:

- Usuarios gratuitos activos al 28 de febrero.
- Cuántos recibieron la secuencia.
- Cuántos abrieron/clicaron.
- Cuántos pasaron a pago.
- En qué momento convirtieron respecto al email recibido.

Esto ayuda a separar el efecto sobre la base existente del efecto de nuevos usuarios traídos por publicidad o por el creador.

### 4. Comparar con meses anteriores

Febrero solo puede ser un mes atípico. Sería mejor ver:

- Altas en diciembre.
- Altas en enero.
- Altas en febrero.
- Altas en marzo.

Si venías con 8, 9, 9 y pasaste a 14, hay una mejora. Si venías con 13, 15, 9 y luego 14, marzo no parece tan especial.

### 5. Ver el timing de las altas

Sería útil saber qué días ocurrieron las 14 altas de marzo.

- Si muchas ocurrieron justo después de los emails, eso apoya la hipótesis de que la secuencia ayudó.
- Si muchas ocurrieron después del 12 de marzo, puede haber sido la mención del creador.
- Si vienen después de campañas pagas concretas, puede ser la publicidad.

Una línea diaria de conversiones ayudaría mucho.

## Mi recomendación

Yo no diría “la secuencia funcionó”. Diría algo más prudente:

> “Marzo fue mejor que febrero en MRR y altas a pago, pero como al mismo tiempo se lanzaron publicidad y hubo una mención importante de un creador, no podemos atribuir la mejora a la secuencia de emails. Hay señales positivas, pero falta medición causal.”

Para estar seguros, haría un test con grupo de control durante abril o mayo, usando UTMs, tracking de cohortes y conversión por fuente. Ahí podrías medir el impacto real de la secuencia en altas y MRR incremental.