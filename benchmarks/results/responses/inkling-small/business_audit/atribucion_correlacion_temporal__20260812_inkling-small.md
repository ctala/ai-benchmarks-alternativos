# Inkling Small — business_audit/atribucion_correlacion_temporal

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.97 | quality: 10.0
- latency_total: 9.412s | tokens_per_second: 166.6
- input_tokens: 232 | output_tokens: 1568
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis exhaustivo y práctico de la situación.

## Respuesta completa

**Conclusión: no se puede saber si la secuencia de emails funcionó.**

Los números subieron, pero hay al menos tres fuerzas simultáneas que explican igual o mejor el resultado: la publicidad ($400), el video del creador (mención masiva) y la variabilidad natural de un mes a otro con muestras pequeñas (9 → 14 altas). Sin aislarlas, atribuir el +29 % de MRR o las 5 altas extra a los 5 emails es una conclusión cómoda, no una conclusión de datos.

**Por qué no sostiene la causalidad:**

- **Sin atribución:** No sabes cuántos de esos 14 nuevos pagaron *por* la secuencia. Podrían venir de los ads, del video o de tráfico orgánico que entró por la mención.
- **Sin grupo de control:** No tienes una cohorte de usuarios del plan gratuito que *no* recibiera los emails para comparar tasas de conversión.
- **Confounders fuertes:** El 3 de marzo arrancaste ads y el 12 de marzo un creador te mencionó. Esas dos acciones suelen mover MRR y altas de forma inmediata y desproporcionada respecto a un email automatizado.
- **MRR ≠ altas:** Subió $1.200, pero no sabes si es por nuevas altas, upgrades de existentes, menor churn o cambios de precio. Las altas pasaron de 9 a 14 (+55 %), pero con números tan pequeños una diferencia de 5 puede ser ruido.
- **Sin métricas de la secuencia:** No tienes tasas de apertura, clics ni conversiones directas de los emails. No sabes si los usuarios los leyeron.

**Qué haría falta para estar seguros:**

1. **Atribución de la fuente:** ¿De dónde vienen los 14 nuevos? (Encuesta al registrarse, UTM en links del email, tracking de tráfico de la publicidad y del video).
2. **Datos internos de la secuencia:** Cuántos usuarios del plan gratuito la recibieron, cuántos abrieron, cuántos clicaron y cuántos convirtieron *directamente* desde el email (no solo “en el mismo mes”).
3. **Grupo de control:** La próxima vez, deja a una parte del plan gratuito sin recibir la secuencia y compara tasas de conversión entre grupos.
4. **Datos de cohorte/retención:** Cuántos de los nuevos permanecen al mes 2 y 3. Si el MRR subió por una oleada de bajas que luego se van, el “éxito” es temporal.
5. **Aislar variables:** Si lanzas publicidad o te mencionan, intenta medir el impacto de cada canal por separado (ej. pausar ads una semana o usar códigos de descuento distintos).

**Mi recomendación práctica:** No digas al equipo que “funcionó” ni que “no funcionó”. Di que hay una correlación temporal positiva, pero que el experimento no está controlado. Para la próxima secuencia, implementa al menos un enlace con UTM exclusivo y compara con una cohorte que no reciba los mails. Si no puedes hacer el grupo de control ahora, al menos mide cuántas conversiones vienen de los links de los emails; sin eso, cualquier conclusión es una suposición.