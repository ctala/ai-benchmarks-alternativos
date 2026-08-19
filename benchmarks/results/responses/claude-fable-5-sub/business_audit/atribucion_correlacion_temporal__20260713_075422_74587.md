# Claude Fable 5 (suscripción) — business_audit/atribucion_correlacion_temporal

- model_id: `claude-fable-5`
- success: True  | final: 3.37 | quality: 3.6
- latency_total: 43.137s | tokens_per_second: 40.3
- input_tokens: 2 | output_tokens: 1740

## Respuesta completa

**No se puede saber con estos datos.** Y la razón es simple: lanzaste tres cosas casi al mismo tiempo.

## Por qué no se puede concluir

Entre el 1 y el 12 de marzo activaste **tres tratamientos simultáneos** sobre la misma métrica:

1. Secuencia de emails (1 de marzo)
2. Publicidad pagada, $400 (3 de marzo)
3. Mención de un creador grande (12 de marzo)

Cualquiera de los tres —o ninguno— puede explicar el aumento. Con la data agregada que tienes, el MRR de marzo es la suma de tres efectos mezclados y no hay forma de separarlos.

## Problemas adicionales con los números

- **Muestra minúscula.** Pasar de 9 a 14 altas son +5 personas. Con números tan chicos, esa variación puede ser ruido normal mes a mes. ¿Cuántas altas tuviste en diciembre y enero? Sin más meses de baseline, no sabes si 9 era tu piso o tu promedio.
- **El +29% de MRR no equivale a "la secuencia convirtió".** El MRR puede subir por altas nuevas, pero también por upgrades de plan, cambios a anual, o menos churn. No sé cuánto del delta de $1.200 viene de las 14 altas.
- **Un detalle sutil:** la mención del creador fue el 12 de marzo. Si la mayoría de las 14 altas ocurrió después de esa fecha, el candidato principal es el creador, no tus emails ni tus ads.

## Qué diría hoy si me presionas

Lo máximo defendible: *"La secuencia está funcionando técnicamente (se envía), el MRR subió, y la atribución está pendiente de medir."* Nada más.

## Qué haría falta para estar seguros

1. **Atribución a nivel de persona, no de mes.** Para cada una de las 14 altas: ¿estaba en la lista de la secuencia? ¿Abrió y clicó los emails? ¿El upgrade ocurrió dentro de las 48-72h posteriores a un email? Si un alta nunca abrió un email, la secuencia no fue.
2. **Fechas de cada alta** cruzadas con los tres eventos. Un simple gráfico de altas por día te muestra si hay un pico el 12-15 de marzo (creador) o si están distribuidas.
3. **Pregunta directa en el onboarding:** "¿Cómo nos conociste / qué te hizo pagar?". Es imperfecto pero barato y suma evidencia.
4. **Hacia adelante, un holdout:** deja fuera de la secuencia a un 20-30% aleatorio de los usuarios free durante 4-8 semanas y compara conversión free→paid entre grupos. Es la única forma limpia de aislar el efecto.
5. **Más tiempo.** Un mes con tres cambios simultáneos no es un experimento, es un lanzamiento. Necesitas al menos 2-3 meses de data con tracking por usuario.

**Resumen:** marzo fue un buen mes, eso sí es un hecho. Que los emails lo causaron es una hipótesis sin evidencia todavía. No apagues la secuencia, pero tampoco escales presupuesto ni tomes decisiones basándote en que "funcionó" — primero monta el tracking por usuario.