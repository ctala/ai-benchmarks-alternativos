# Kimi K3 — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 8.08 | quality: 10.0
- latency_total: 56.859s | tokens_per_second: 31.2
- input_tokens: 354 | output_tokens: 1773
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un análisis exhaustivo y recomendaciones prácticas para el emprendedor.

## Respuesta completa

## Conclusión: no se puede saber con estos datos

El resultado es **consistente** con que la secuencia funcionó, pero también con que no haya hecho nada. Tres cosas cambiaron casi a la vez (emails el día 1, ads el día 3, mención del creador el día 12), y con estos números es imposible separar el efecto de cada una.

## Por qué no alcanza

- **Tres intervenciones simultáneas, cero atribución.** De las 14 altas de marzo, ¿cuántas clicaron un email? ¿Cuántas vinieron del video? ¿De los ads? Sin esa trazabilidad, cualquier reparto del "crédito" es inventado.
- **La muestra es chica.** Pasar de 9 a 14 altas parece mucho (+56%), pero con números así de bajos, una diferencia de 5 entra perfectamente en la variación normal mes a mes. Ni siquiera está claro que haya un efecto real que atribuir.
- **Falta el denominador.** 14 altas sobre ¿cuántos usuarios gratuitos? Si los ads y el video trajeron muchos registros gratuitos nuevos, la *tasa* de conversión pudo incluso bajar mientras el número absoluto subía.
- **MRR ≠ altas.** Los +$1.200 mezclan altas nuevas, bajas, upgrades y downgrades. Sin descomponerlo, no sabés cuánto vino de conversión de gratuitos.
- Marzo tiene 31 días vs. 28 de febrero. Detalle menor, pero empuja en la misma dirección del supuesto efecto.

## Qué haría falta para estar seguros

**Con lo que ya tenés (análisis retrospectivo, hacelo esta semana):**
1. **Signups por día** en marzo. Si el pico es post-12 de marzo, el creador es el sospechoso principal.
2. **Fuente de cada alta**: UTM en los links de los emails, datos de la plataforma de ads, y una pregunta "¿cómo nos conociste?" en el registro (agregala ya si no existe).
3. **Métricas del email**: tasa de apertura, clics en el CTA de upgrade y, sobre todo, conversiones directas desde esos clics.
4. **Descomposición del MRR**: MRR nuevo vs. churn vs. expansión, en febrero y marzo.

**Para la próxima (diseño correcto):**
5. **Grupo de control (holdout)**: dejá a un 15-20% aleatorio de usuarios gratuitos *sin* recibir la secuencia. Si el grupo con emails convierte al 6% y el control al 2%, ahí sí tenés evidencia. Es barato y es el estándar.
6. **Espaciar los lanzamientos**: no actives tres cosas en 11 días si después querés saber cuál funcionó.

## Mi recomendación honesta

Decile al equipo: "Marzo fue un buen mes, pero no sabemos por qué." Hacé el análisis retrospectivo de los puntos 1-4 — quizás ahí la señal sea clara (ej: 8 de 14 altas con clic en email = buena evidencia). Y montá el holdout antes de la próxima campaña, así la siguiente respuesta no depende de adivinar.