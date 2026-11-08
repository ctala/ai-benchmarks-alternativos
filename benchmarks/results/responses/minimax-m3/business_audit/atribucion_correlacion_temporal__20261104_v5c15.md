# MiniMax M3 — business_audit/atribucion_correlacion_temporal

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 69.052s | tokens_per_second: 58.7
- input_tokens: 382 | output_tokens: 4053

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

## Conclusión: no se puede afirmar que la secuencia funcionó

Los datos muestran que **marzo fue mejor que febrero**, pero no permiten atribuir esa mejora a los emails:

- **MRR:** pasó de $4.100 a $5.300: **+$1.200 (+29,3%)**.
- **Altas al plan pago:** pasaron de 9 a 14: **5 altas más (+56%)**.

Sin embargo, la secuencia coincidió con **dos otras fuentes posibles de clientes**: publicidad desde el 3 de marzo y la mención del creador el 12. Sin un grupo de control, no podemos separar cuánto aportó cada acción.

Tampoco sabemos:

- Cuántos usuarios se habrían convertido **sin** la secuencia.
- Si esas conversiones vinieron de los emails, de los anuncios o de la mención.
- Cuánto MRR es realmente incremental: el MRR también depende de retenciones, cancelaciones, cambios de precio y de los clientes ya existentes.

En particular, **no usaría los $1.200 de incremento para calcular un ROI de los emails** ni lo dividiría por los $400 de publicidad: no hay base para atribuir ese ingreso a ninguna de las dos acciones.

## Qué haría falta para estar seguros

### 1. Un experimento A/B aleatorio
Dividiría a los usuarios elegibles del plan gratuito en dos grupos:

- **Tratamiento:** recibe la secuencia de 5 emails.
- **Control:** no recibe esa secuencia.

Mantendría las mismas ofertas, publicidad y condiciones en ambos grupos. La métrica principal sería la **tasa de conversión por usuario asignado**, comparando ambos grupos durante una ventana predefinida. Reportaría el efecto incremental y su intervalo de confianza.

### 2. Medir el resultado completo, no solo la conversión
Además de altas, mediría:

- MRR neto por usuario.
- Retención y cancelaciones posteriores.
- Reembolsos, si los hay.
- Conversión y MRR en una ventana de 30–60 días, para comprobar que las altas son duraderas.

Las aperturas y los clics sirven para diagnosticar la secuencia, pero no demuestran por sí solos que generaron negocio.

### 3. Si no es posible hacer A/B
Usaría, en orden de Preference:

1. **Lanzamiento escalonado:** una parte recibe los emails primero y otra después, con periodos de comparación.
2. **Comparación entre grupos geográficos o cohortes similares**, verificando que tenían tendencias similares antes de marzo.
3. **Atribución mediante enlaces/códigos por email**, aunque es más débil y no sustituye a un grupo de control.

También necesitaría conocer el **tamaño de la base de usuarios gratuitos**, sus tasas históricas de conversión y el detalle de qué mueve el MRR. Con solo 5 altas de diferencia, la incertidumbre puede ser considerable.

## Mi veredicto

> **Hubo mejora同期 en MRR y altas, pero el efecto causal de la secuencia es indeterminado.**

No la presentaría todavía como un éxito probado. Si tuviera que decidir hoy, mantendría un grupo de control sin esos emails y mediría el incremento atribuible antes de declarar que la secuencia funcionó.