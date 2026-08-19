# Claude Fable 5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-fable-5`
- success: True  | final: 7.93 | quality: 10.0
- latency_total: 25.211s | tokens_per_second: 43.6
- input_tokens: 364 | output_tokens: 1098
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando una evaluación exhaustiva de la situación y recomendaciones prácticas.

## Respuesta completa

# Conclusión: no se puede saber con estos datos

Y te explico por qué no es una respuesta evasiva, sino la única honesta.

## El problema: tres intervenciones simultáneas

En marzo cambiaste **tres cosas a la vez**:

1. Secuencia de emails (1 de marzo)
2. Publicidad de pago (3 de marzo)
3. Mención de un creador grande (12 de marzo) — que además no controlaste tú

El +29% de MRR y las 5 altas extra podrían venir de cualquiera de las tres, de una combinación, o incluso de estacionalidad normal (con 9-14 altas mensuales, la variación aleatoria mes a mes puede ser enorme).

## El problema del tamaño de muestra

Pasar de 9 a 14 altas son **5 personas**. Con números tan pequeños, ese salto puede ocurrir sin que hayas cambiado nada. Si en enero tuviste 7 y en febrero 9, ya venías creciendo. No me pasaste esos datos, y los necesitaría.

## Qué haría falta para saber si la secuencia funcionó

**Con los datos que probablemente ya tienes:**

- **Atribución directa:** ¿cuántas de las 14 altas eran usuarios gratuitos que recibieron la secuencia? ¿Cuántos hicieron clic en el email antes de pagar? Tu plataforma de email debería mostrar esto.
- **Timing:** ¿cuándo ocurrieron las altas? Si 10 de las 14 llegaron después del 12 de marzo, el sospechoso principal es el video del creador, no tus emails.
- **UTMs en la publicidad:** ¿cuántas altas vienen rastreadas desde los anuncios?
- **Origen de los nuevos pagos:** ¿eran usuarios gratuitos antiguos (audiencia de la secuencia) o gente nueva que llegó y pagó directo (audiencia del video/ads)?

**Para el futuro, si quieres una respuesta sólida:**

- **Grupo de control:** deja fuera de la secuencia a un 20-30% aleatorio de usuarios gratuitos durante 2-3 meses. Compara tasas de conversión entre grupos. Es la única forma de aislar el efecto.
- **No lances varias cosas la misma semana** si quieres poder medirlas.

## Lo que sí puedo decirte

- El mes fue bueno en términos absolutos. Eso es real.
- Pero atribuirlo a la secuencia sería contarte una historia cómoda. Y si la secuencia en realidad no convierte, seguirías invirtiendo en algo que no funciona mientras crees que sí.

Pásame el desglose de fechas de las altas y los datos de clics de la secuencia, y afinamos.