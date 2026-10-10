# Claude Opus 5.5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.12 | quality: 10.0
- latency_total: 26.1s | tokens_per_second: 87.3
- input_tokens: 366 | output_tokens: 2279

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

# Conclusión: con estos datos no se puede saber si la secuencia funcionó

Esto no significa que no haya funcionado. Significa que los números no permiten distinguir su efecto del de las otras dos cosas que pasaron ese mes, ni siquiera del azar.

## Por qué no se puede atribuir

**1. Tres intervenciones en el mismo mes.**
Los emails (1 de marzo), la publicidad (3 de marzo) y la mención del creador (12 de marzo) empezaron casi juntos. Cualquiera de las tres, o cualquier combinación, explica la subida igual de bien. El video de un creador grande, en particular, puede mover mucho más que una secuencia de emails.

**2. La subida de altas no es distinguible del ruido.**
- 9 contra 14 son números muy chicos. Si la tasa real de altas no hubiera cambiado, una diferencia así o mayor aparecería alrededor del 20% de las veces por pura variación (test binomial condicional, p ≈ 0,20 a una cola).
- Febrero tiene 28 días y marzo 31. Ajustado por días, febrero equivale a unas 10 altas, así que la diferencia real es de 10 a 14.
- Es decir, antes de preguntar *qué* causó la subida, ni siquiera está claro que haya una subida real en la tasa de conversión.

**3. El MRR no mide solo altas.**
Los +$1.200 mezclan altas nuevas, bajas (churn), cambios de plan y posibles cambios de precio. Sin separar esos componentes, el +29% no dice nada específico sobre los emails.

**4. Hay contaminación entre canales.**
Si la gente que llegó por la publicidad o el video entró primero al plan gratuito, también recibió los emails. Una alta así no es "de los emails" ni "del video": es de ambos, y no se puede repartir el crédito a ojo.

## Qué haría falta para estar seguros

**Con datos que probablemente ya tenés (análisis retroactivo):**

1. **Origen de cada una de las 14 altas.** ¿Era usuario gratuito antes del 1 de marzo? ¿Llegó con UTM de publicidad? ¿Se registró después del 12 de marzo?
2. **Cohorte limpia.** Tomá solo a los usuarios gratuitos que ya existían antes del 1 de marzo, que no fueron expuestos a la publicidad ni al video. Compará su tasa de conversión en marzo con la de esa misma base en meses anteriores. Es la mejor aproximación al efecto aislado de los emails.
3. **Clics en los emails.** ¿Cuántas de las 14 altas hicieron clic en un email de la secuencia antes de pagar, y cuánto tiempo pasó entre el clic y el pago? Esto no prueba causalidad (quien iba a pagar igual también hace clic), pero si casi nadie hizo clic, es una señal fuerte en contra.
4. **Más historia.** Altas y MRR de 6 a 12 meses atrás, para ver si 14 está fuera del rango normal o si ya hubo meses así.
5. **Desglose del MRR.** Nuevo, expansión, churn y contracción por separado.

**Para tener una respuesta sólida (de acá en adelante):**

6. **Grupo de control.** Asigná al azar una parte de los nuevos usuarios gratuitos (por ejemplo, entre un 30% y un 50%) a *no* recibir la secuencia, y compará la tasa de conversión entre ambos grupos. Es la única forma de aislar el efecto de verdad.
   - Con tu volumen, esto va a llevar varios meses para tener suficientes conversiones. Con 10 a 15 altas por mes, solo vas a poder detectar efectos grandes. Es mejor saberlo de antemano que sacar conclusiones con 3 o 4 casos por grupo.
7. **No lanzar varias cosas a la vez** cuando quieras medir algo puntual, o al menos etiquetar bien cada canal (UTMs, códigos de descuento distintos, la pregunta "¿cómo nos conociste?" al registrarse).

## En una frase

Marzo fue un buen mes, pero no hay forma de saber cuánto del crecimiento vino de los emails. Si querés una respuesta aproximada ya, el punto 2 (la cohorte de usuarios gratuitos previos) es lo más útil. Si querés una respuesta confiable, necesitás un grupo de control.