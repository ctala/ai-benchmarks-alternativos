# MiniMax M3.1 Flash — business_audit/atribucion_correlacion_temporal

- model_id: `minimax/minimax-m3.1-flash`
- success: True  | final: 9.01 | quality: 10.0
- latency_total: 24.901s | tokens_per_second: 139.5
- input_tokens: 399 | output_tokens: 3474

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

## Conclusión

**No se puede saber si la secuencia de emails funcionó.** Tampoco sería correcto decir que no funcionó; los datos no permiten atribuirle el resultado.

Lo que sí se observa es que marzo mejoró en los indicadores agregados:

- **MRR:** de $4.100 a $5.300, un aumento de **$1.200 (+29,3%)**.
- **Altas al plan pago:** de 9 a 14, es decir, **5 altas más (+55,6%)**.

Pero esto demuestra una mejora general de marzo, **no que la secuencia la haya causado**.

### Por qué no se puede atribuir

1. **Hubo otras intervenciones simultáneas:** publicidad desde el 3 de marzo y una mención de un creador con gran audiencia el 12 de marzo. Ambas pudieron generar altas.
2. **No existe un grupo de control:** no sabemos cuántos usuarios_free se habrían convertido sin la secuencia.
3. **NoKnown el denominador:** falta saber cuántos usuarios elegibles había al inicio de marzo y cuántos recibieron realmente los emails.
4. **No hay atribución por usuario:** no sabemos si los 14 upgrades vinieron de emails, publicidad, creación o de forma orgánica.
5. **El MRR no equivale únicamente a nuevas altas:** también puede haberoviido de.expansiones de usuarios existentes, planes升级, cancelaciones o diferencias de recognize.
6. **La muestra es pequeña:** con solo 14 altas, unas pocas conversiones cambian porcentajes y no permiten una conclusión robusta.

Además, que alguien haya_convertido después de hacer clic en un email probaría **atribución**, pero no necesariamente **incrementalidad**: quizá esa persona se habría convertido igualmente sin recibirlo.

## Qué haría falta para estar seguros

### Opción más sólida: una prueba con grupo de control

Entre los usuarios elegibles del plan gratuito:

- Asignar aleatoriamente al 50% a la secuencia.
- Dejar al otro 50% sin la secuencia durante el periodo de prueba.
- Medir en una ventana fija, por ejemplo 30 días:
  - **Métrica principal:** tasa de conversión a plan pago.
  - **Métricas secundarias:** MRR incremental por usuario, retención y valor neto.

La secuencia debería probarse contra una alternativa real —por ejemplo, otro flujo o ninguna comunicación— y el resultado analizarse con intervalos de confianza.

### Si ya no se puede hacer un test aleatorio

Las siguientes opciones son útiles, aunque menos concluyentes:

- **Despliegue escalonado:** que distintos usuarios reciban la secuencia en fechas diferentes y comparar momentos de activación.
- **Comparación con cohortes similares:** usuarios no expuestos con Characteristics parecidas, usando varios meses previos y posteriores.
- **Análisis de Difference-in-Differences**, si se dispone de suficiente histórico.
- Revisar la **distribución temporal de las altas**: las occurring antes del 3 y del 12 de marzo están menos contaminadas por las otras campañas, pero siguen sin demostrar causalidad.

## Datos adicionales necesarios

- Número de usuarios gratuitos elegibles al 1 de marzo.
- Emails enviados, entregados, abiertos y clicados.
- Identificador de usuario y fuente de cada alta: email, publicidad, creador, orgánico.
- Altas, downsells, cancelaciones y cambios de plan de los usuarios existentes.
- Histórico de MRR y conversiones de varios meses anteriores y posteriores.
- Coste total de la secuencia para evaluar retorno, no solo conversión.
- Datos de impresiones, clics y conversiones de la publicidad y de la referencia del creador.

### Mi decisión analítica

Con la información actual, diría:

> **“Hubo una mejora descriptiva en marzo, pero no se puede determinar si la secuencia de emails la produjo ni qué parte del resultado le corresponde.”**

Para afirmar que “funcionó” con confianza, necesitaría al menos una **comparación aleatoria con un grupo de control**, junto con trazabilidad por usuario y una reconciliación completa del MRR.