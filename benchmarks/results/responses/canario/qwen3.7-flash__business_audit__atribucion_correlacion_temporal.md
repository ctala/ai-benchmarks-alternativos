# Qwen 3.7 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.16 | quality: 10.0
- latency_total: 19.48s | tokens_per_second: 89.8
- input_tokens: 245 | output_tokens: 1750

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

**No se puede saber.** 

Lo que tienes son datos agregados de un mes donde coincidió activar tres fuentes de tráfico/conversión diferentes. Eso rompe cualquier intento de atribución causal con la información actual:

1. **Superposición temporal exacta:** Emails (1 mar), publicidad ($400 desde el 3 mar) y mención del creador (12 mar). Cualquiera de los tres, o su combinación, pudo impulsar tanto el MRR como las 14 altas de marzo.
2. **MRR ≠ conversiones de la secuencia:** El salto de $4.100 a $5.300 incluye nuevos suscriptores pagados por cualquier canal, no solo usuarios gratuitos que subieron de nivel gracias a los emails.
3. **Ausencia de línea base y grupo de control:** Un solo mes de comparación no descarta estacionalidad, crecimiento orgánico natural o efectos de red. Tampoco sabes cómo se comportó un segmento equivalente que no estuvo expuesto a la secuencia.
4. **Falta de métricas intermedias:** No tienes aperturas, clics, retención en la secuencia ni tasa de conversión específica por email. Sin eso, no puedes rastrear el comportamiento real de los receptores.

### Qué haría falta para estar seguros:
- **Tracking por origen:** UTM, códigos de referido o segmentación nativa que distinga cuántas de esas 14 altas vinieron de usuarios que recibieron los emails vs. los que llegaron por ads, el video o tráfico orgánico.
- **Métricas de la secuencia:** % de entregables, aperturas, clics en CTAs y conversión gratuita→pago exclusiva para quienes la completaron (o al menos la abrieron).
- **Prueba controlada o A/B:** Comparar la evolución de un cohorte similar que no reciba la secuencia (o la reciba con retraso) contra el expuesto, manteniendo ads y menciones constantes si es posible.
- **Desagregación financiera:** Separar el ingreso marginal atribuible a cada canal, calculando CAC/ROAS de los $400 de publicidad y evaluando el pico post-video. Restar ese impacto deja solo la porción atribuible a los emails.
- **Ventana histórica más amplia:** Mínimo 3-6 meses previos para establecer tendencia natural y detectar patrones estacionales.

Hasta que no aíles la variable “secuencia de emails” con métricas de conversión directa, controles adecuados y trazabilidad por canal, la conclusión válida sigue siendo **no se puede saber**. Si quieres, puedo ayudarte a montar un experimento ligero (A/B por cohorte + tracking básico) que te dé una respuesta accionable sin frenar tus otras campañas.