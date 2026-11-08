# GLM 5.3 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 8.73 | quality: 10.0
- latency_total: 60.591s | tokens_per_second: 67.4
- input_tokens: 235 | output_tokens: 4084

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

## Conclusión: no se puede saber

Marzo fue un buen mes. Eso es lo único que estos datos permiten afirmar. No se puede atribuir el crecimiento a la secuencia de emails, y ninguna presentación de estos números cambiaría eso.

## Por qué

**Tres cambios a la vez.** El 1/3 activaste la secuencia, el 3/3 la pauta, el 12/3 salió el video. Cualquiera de los tres, la combinación, o simple estacionalidad podría explicar el aumento. Sin separarlos, el crédito no se puede repartir.

**Cero atribución.** Los 14 registros no tienen fuente. No sabés cuántos vinieron de clics en email, de anuncios, del video, o de boca a boca preexistente.

**Febrero es más corto.** 9 altas en 28 días = 0,32/día. A ese ritmo, marzo "esperado" era ~10 altas. El exceso real es ~4, no 5. Y con números tan chicos, 4 altas de diferencia entre meses es perfectamente compatible con azar, incluso sin ningún cambio.

**El MRR no cierra solo con las altas.** +$1.200 con 14 altas implica precio promedio de ~$86 sin ninguna baja. Si tu plan cuesta menos, parte del crecimiento no viene de las altas contadas (¿upgrades de usuarios existentes? ¿anuales? ¿bajas que no estás midiendo?). Eso hay que verificarlo antes de cualquier análisis.

**No hay línea base.** ¿Cuánto crecía la comunidad en un mes típico sin cambios? Si ene→feb fue +5%, el +29% destaca; si fue +20%, mucho menos.

## Qué haría falta para estar seguros

**El estándar de oro:** dividir al azar los usuarios free — ~80-90% recibe la secuencia, el resto no, durante 4-8 semanas — y comparar tasas de conversión. Ojo: con tan pocas conversiones mensuales, probablemente necesites 2-3 meses para detectar incluso efectos grandes.

**Lo barato, aplicable ya en abril:**
- Links con UTM distintos por canal y un link/código exclusivo para el creador
- Pregunta "¿cómo nos conociste?" en el formulario de alta
- Altas por día en un gráfico, con los tres eventos marcados (un pico post-12/3 apuntaría al creador; sugerente, no conclusivo)
- Clasificar a los convertidos: ¿eran free antiguos (la audiencia de la secuencia) o altas nuevas del mes? Son preguntas distintas con respuestas distintas
- Tasa de conversión free→paid de enero y febrero como baseline

## Qué sí se puede decir

El conjunto de cambios coincidió con crecimiento. Punto. Y hay un riesgo operativo real: si concluís "la secuencia funcionó" y dejás de mirar, podés terminar escalando lo que no funciona y recortando lo que sí — por ejemplo, el video del creador, que a priori es el candidato más probable a explicar el pico.

La respuesta honesta es "no se puede saber". La buena noticia: las herramientas para saberlo son baratas y la mayoría se pueden implementar este mes.