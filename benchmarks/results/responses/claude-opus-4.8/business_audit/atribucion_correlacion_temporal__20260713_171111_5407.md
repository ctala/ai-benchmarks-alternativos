# Claude Opus 4.8 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-opus-4.8`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 20.784s | tokens_per_second: 57.2
- input_tokens: 364 | output_tokens: 1189
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación exhaustiva de la situación y recomendaciones prácticas.

## Respuesta completa

No se puede saber si la secuencia de emails funcionó. Te explico por qué, sin adornos.

## El problema central

En marzo pasaron **tres cosas a la vez**:
1. La secuencia de emails (1 de marzo)
2. Publicidad pagada (3 de marzo, $400)
3. La mención de un creador grande (12 de marzo)

Tu MRR subió $1.200 y las altas pasaron de 9 a 14. Pero **no hay forma, con estos datos, de atribuir ese aumento a ninguna de las tres causas en particular**. Es el problema clásico de variables confundidas: cuando cambias tres cosas a la vez, el resultado no te dice cuál funcionó.

Es perfectamente posible que:
- Los emails no hicieran nada y todo viniera del creador.
- Los emails funcionaran y la publicidad fuera dinero tirado.
- Cualquier combinación intermedia.

Los números que me diste son compatibles con todas esas historias.

## Un par de cautelas sobre las cifras

- **5 altas más (9 → 14)** es un número muy pequeño. Con muestras así, la variación mes a mez puede ser puro ruido. ¿Cuánto variaron las altas en enero, diciembre, noviembre? Si oscilaban entre 7 y 15 sin campañas, marzo no tiene nada de especial.
- El **+29% de MRR** puede venir de altas nuevas, de que subiste precios, de que alguien pasó a un plan anual, o de menos bajas. No sabemos la composición.

## Qué haría falta para estar seguros

Para aislar el efecto de los emails necesitarías datos de atribución, no solo totales:

1. **De las 14 altas de marzo, ¿cuántas venían del plan gratuito y habían recibido la secuencia?** Las altas que llegaron por publicidad o por el creador probablemente ni pasaron por tu secuencia. Sepáralas.
2. **Métricas propias de la secuencia**: tasa de apertura, clics, y sobre todo **cuántos de los que recibieron los emails convirtieron**, comparado con usuarios gratuitos equivalentes que NO los recibieron.
3. **Fechas de las altas**: si hay un pico claro alrededor del 12 de marzo, huele a creador, no a emails.
4. **Línea base histórica**: altas de los 3-6 meses previos para saber qué es "normal".

## Cómo saberlo de verdad la próxima vez

- **Grupo de control**: manda la secuencia solo a la mitad de los usuarios gratuitos (al azar) y compara conversión entre los dos grupos. Es la única forma limpia.
- **No lances tres iniciativas la misma semana** si quieres medir alguna. O las separas en el tiempo, o usas grupos de control.
- **UTMs y atribución por fuente** para separar publicidad, creador y email.

## Conclusión

La secuencia **pudo** haber funcionado, pero los datos actuales no lo demuestran ni lo descartan. Si alguien en el equipo dice "los emails nos subieron el MRR un 29%", eso es una afirmación que hoy no puedes respaldar. Lo honesto es: *"probamos tres cosas, el mes fue mejor, y aún no sabemos qué lo movió."*

Si me pasas el desglose de las 14 altas por fuente y fecha, te puedo dar algo bastante más concreto.