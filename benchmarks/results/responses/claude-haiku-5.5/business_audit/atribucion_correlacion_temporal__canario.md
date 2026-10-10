# Claude Haiku 5.5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.04 | quality: 10.0
- latency_total: 10.178s | tokens_per_second: 171.1
- input_tokens: 366 | output_tokens: 1741

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

**Conclusión: con estos datos no se puede saber si la secuencia de emails funcionó.** Es posible que haya contribuido, pero los números no permiten atribuirle el crecimiento.

**Por qué no se puede concluir**

- **Hay dos cambios al mismo tiempo.** El 3 de marzo empezaste a pagar publicidad y el 12 de marzo un creador mencionó la comunidad. Cualquiera de los dos pudo traer usuarios nuevos que se convirtieron al plan pago, con o sin emails.
- **No hay grupo de control.** No sabes cuál habría sido el crecimiento sin la secuencia. Comparar febrero con marzo mezcla el efecto de todo lo que cambió.
- **La muestra es muy pequeña.** Pasar de 9 a 14 altas son 5 personas. Esa diferencia puede ser ruido. Con números así, variaciones de este tamaño ocurren por azar con frecuencia.
- **El MRR no es lo mismo que las altas.** El MRR neto también depende de cancelaciones, cambios de plan y precios. No sabemos cuánto de los +$1.200 viene de las 5 altas adicionales ni cuánto de otra cosa.
- **Las altas no tienen origen identificado.** No sabemos qué usuarios recibieron los emails, cuáles llegaron por publicidad o por el creador, ni cuáles abrieron los emails.

**Qué haría falta para estar seguros**

1. **Grupo de control aleatorio.** Antes de enviar la secuencia, separa al azar un 10–20% de los usuarios gratuitos que no la reciban. Compara la tasa de conversión entre ambos grupos durante el mismo período. Es la única forma limpia de medir el efecto.
2. **Segmentar las altas por origen.** Usa UTMs o un campo de "cómo nos conociste" para saber si cada alta vino de publicidad, del creador, de orgánico o de la secuencia.
3. **Revisar la publicidad y el video por separado.** Compara el coste por alta de los $400 de anuncios y mira cuántos usuarios llegaron por el enlace del creador (si lo tienes, con un código o una URL específica).
4. **Mirar cohortes y no solo totales mensuales.** Compara la conversión a 30 días de los usuarios que se registraron antes y después del 1 de marzo, separando por origen.
5. **Medir retención y churn.** Un aumento de altas que se cancelan pronto no es un éxito real. Revisa también el MRR neto por cohorte.
6. **Esperar más datos.** Con 9 y 14 altas, cualquier conclusión será frágil. Varios meses de datos, o un test con grupo de control, dará una respuesta más sólida.

**Lo que sí puedes hacer ya:** mirar cuántos de las 14 altas de marzo recibieron la secuencia, cuántos vinieron del creador y cuántos de publicidad. Con eso puedes formular una hipótesis, pero no confirmarla.

Si me pasas los datos de origen de las altas o el número de usuarios que recibieron la secuencia, puedo ayudarte a hacer ese desglose.