# GLM 5.3 — business_audit/atribucion_correlacion_temporal

- model_id: `z-ai/glm-5.3`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 69.791s | tokens_per_second: 66.0
- input_tokens: 235 | output_tokens: 4606

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

**Conclusión corta: no se puede saber.** Los datos de marzo son compatibles con que la secuencia funcionó, pero también con que no hizo nada y el crecimiento vino de la publicidad o del video. No es una respuesta cómoda, pero es la honesta.

**Por qué no se puede atribuir:**

1. **Tres cambios simultáneos.** Emails (1 de marzo), publicidad (3 de marzo) y mención de un creador grande (12 de marzo), todos dentro de la misma ventana de 11 días, sobre el mismo mes. Con un solo mes de datos agregados no hay forma matemática de separar sus efectos.

2. **El tamaño de muestra no da ni para el mejor de los casos.** Pasar de 9 a 14 altas está dentro de la variación normal cuando manejas ~10 conversiones al mes: diferencias de ±5 entre meses son rutinarias a ese volumen. Aun si no hubieras lanzado nada más en marzo, 9→14 no sería evidencia concluyente. Necesitarías el doble de volumen, o varios meses, para distinguir señal de ruido.

3. **El MRR no cuadra sin más datos.** +$1.200 con 5 altas netas adicionales implica precios altos, upgrades de plan, o menos churn. Sin el churn de marzo y el mix de planes, ni siquiera el +29% se puede descomponer.

**Lo que sí puedo revisar con datos que probablemente ya tienes:**

- **Origen de las 14 altas:** ¿cuántas eran usuarios free que ya existían antes del 1 de marzo (el público de los emails) vs. usuarios que se registraron en marzo (público de ads/video)? Si la mayoría son usuarios nuevos, los emails tienen poco que reclamar. Si la mayoría son antiguos, el crédito se inclina hacia la secuencia. Es el corte más informativo y se puede hacer hoy.
- **Curva diaria de altas:** si se concentran después del 12, el sospechoso principal es el video. Si hay un salto entre el 1 y el 11, apunta más a emails/ads.
- **Engagement de la secuencia:** opens y clicks de quienes convirtieron vs. quienes no. No prueba causalidad, pero si casi nadie abrió los emails, ya tienes la respuesta.
- **Churn de marzo** para reconciliar el MRR.

Ninguno de estos cortes es definitivo por sí solo (el video, por ejemplo, también pudo reactivar usuarios antiguos), pero juntos acotarían bastante la respuesta.

**Lo que haría falta para estar seguros de verdad:**

- **Grupo de control.** La próxima secuencia: excluye aleatoriamente al 15–20% de los usuarios free y compara su conversión contra el resto durante 30–60 días. Es la única forma limpia de medir el efecto. Ojo: a estos volúmenes, incluso el test necesitará paciencia.
- **UTMs** en los anuncios y en el link del video, para que cada alta quede etiquetada por canal desde el inicio.
- **Una baseline más larga.** Con solo febrero como referencia no sé si +29% es excepcional o tu normalidad.

Lo único que los datos sostienen hoy: marzo fue un buen mes en conjunto. Qué palanca lo causó, no lo sostienen.