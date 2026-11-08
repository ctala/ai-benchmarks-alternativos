# Kimi K3 — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 7.97 | quality: 10.0
- latency_total: 86.918s | tokens_per_second: 39.9
- input_tokens: 354 | output_tokens: 3469

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

## Conclusión: no se puede saber con estos datos

Los números son **compatibles** con que la secuencia funcionó, pero también con que no haya tenido ningún efecto. En 12 días lanzaste tres cosas que pueden generar conversiones:

- Secuencia de emails → 1 de marzo
- Publicidad pagada → 3 de marzo
- Mención del creador → 12 de marzo

Con los tres efectos mezclados en el mismo mes, atribuir el +29% de MRR o las 14 altas a los emails es adivinar, no analizar.

## Problemas específicos de los datos

1. **No hay grupo de control.** Si todos los usuarios gratuitos recibieron la secuencia, no hay con quién compararlos.
2. **Faltan denominadores.** 14 vs 9 altas no dice nada sin saber sobre cuántos usuarios gratuitos elegibles. Si la base gratuita creció mucho en marzo (por los ads o el video), la *tasa* de conversión pudo incluso bajar aunque suban las altas absolutas.
3. **MRR ≠ altas.** +$1.200 con 14 altas implica ~$86 por alta. ¿Es coherente con tu precio mensual? El MRR neto también incluye upgrades, reactivaciones y churn. Sin ese desglose, ni siquiera sabes de dónde vino el crecimiento.
4. **No sabemos quiénes son las 14 altas.** Si los ads y el video trajeron gente nueva que entró directa al plan pago, esas personas nunca recibieron los emails. La pregunta clave: ¿cuántas de las 14 eran usuarios gratuitos que convirtieron?

## Lo que puedes revisar ya, sin nuevos experimentos

- **Fecha de cada alta en marzo.** Si se concentran después del 12, sospecha del creador. Si caen justo tras cada envío de la secuencia, es un punto a favor de los emails.
- **Trazabilidad de las 14 altas:** ¿eran gratuitos antes? ¿Abrieron o clicaron los emails? ¿Tienes UTMs o un campo de "¿cómo nos conociste?" en el registro?
- **Desglose del MRR:** nuevo vs. expansión vs. churn.
- **Línea base histórica:** ¿cuántas conversiones gratis→pago tenías por mes antes de marzo? Si febrero tuvo 9 *sin* secuencia, el efecto neto de *todo el paquete de marzo* es ~+5 altas, y hay que repartirlo entre tres causas (más estacionalidad, que ni hemos mencionado).

## Para saberlo de verdad la próxima vez

- **Holdout:** deja a un 10-20% de usuarios gratuitos sin recibir la secuencia y compara tasas de conversión.
- **UTMs distintos** por canal: emails, ads, enlace del creador.
- **Escalonar lanzamientos:** no activar tres iniciativas la misma semana.
- **Encuesta post-compra** de una pregunta: "¿cómo descubriste la comunidad?"

## Lo que sí puedes afirmar hoy

"En marzo, con el conjunto de acciones, el MRR subió 29% y hubo 5 altas más que en febrero." Eso es verdad y es útil. Lo que no puedes decir es qué parte corresponde a los emails.

Una nota práctica: si mantener la secuencia activa cuesta poco, probablemente no necesitas certeza total para dejarla corriendo. Pero no la declares la causa del crecimiento, porque con estos datos eso sería una conclusión cómoda, no una conclusión válida.