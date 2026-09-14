# Fugu Max — business_audit/atribucion_correlacion_temporal

- model_id: `sakana/fugu-max`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 16.752s | tokens_per_second: 83.7
- input_tokens: 297 | output_tokens: 1402

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

**No se puede saber con estos datos si la secuencia de emails funcionó.**

Sí hay una señal positiva:

- MRR: de **$4.100 a $5.300**, un aumento de **$1.200 / 29,3%**.
- Altas al plan pago: de **9 a 14**, un aumento de **55,6%**.

Pero esos resultados ocurrieron al mismo tiempo que:

- Se empezó a invertir **$400 en publicidad** el 3 de marzo.
- Un creador relevante mencionó la comunidad el 12 de marzo.

Por lo tanto, el aumento puede deberse a los emails, a la publicidad, a la mención del creador, a una combinación de los tres o a factores estacionales. La comparación febrero-marzo no permite separar esos efectos.

Además, el MRR no mide solo nuevas altas: también puede cambiar por bajas, upgrades, downgrades, cambios de precio o cobros de usuarios existentes. Incluso las 14 altas de marzo no indican de dónde vino cada usuario.

La conclusión correcta sería:

> **Marzo fue mejor que febrero, pero no hay evidencia suficiente para atribuir la mejora a la secuencia de emails.**

## Qué haría falta para estar seguros

### 1. Un grupo de control

Lo ideal habría sido dividir aleatoriamente a los usuarios gratuitos elegibles el 1 de marzo:

- Grupo tratamiento: recibe la secuencia.
- Grupo control: no recibe emails, o los recibe más tarde.

Después comparar ambos grupos en igualdad de condiciones:

- Conversión a plan pago a 7, 14 y 30 días.
- Ingreso generado por usuario.
- Retención y cancelaciones.
- MRR incremental.

La métrica clave sería algo como:

> Conversión del grupo con emails − conversión del grupo sin emails

Por ejemplo, si el grupo tratado convierte un 6% y el control un 3%, la secuencia habría generado aproximadamente **3 puntos porcentuales de conversión incremental**.

### 2. Información de cada usuario

Necesitaría, como mínimo:

- Fecha en que se registró como usuario gratuito.
- Si recibió, abrió y clicó cada email.
- Fecha exacta de conversión a pago.
- Fuente de adquisición: orgánico, publicidad, creador, email u otra.
- Plan contratado y MRR aportado.
- Cancelaciones, upgrades y downgrades.
- Si estuvo expuesto a la publicidad o a la mención del creador.

Importante: no conviene comparar simplemente “los que abrieron el email” contra “los que no lo abrieron”, porque quienes abren emails probablemente ya sean usuarios más interesados. Eso introduce sesgo. La comparación más fiable es por **asignación aleatoria al envío**, no por apertura posterior.

### 3. Análisis de atribución y cohortes

Como análisis retrospectivo, separaría:

- Usuarios registrados antes del 1 de marzo.
- Usuarios captados por publicidad.
- Usuarios llegados después de la mención del creador.
- Usuarios que recibieron la secuencia y aquellos que no.
- Conversiones ocurridas antes y después del 12 de marzo.

También compararía la conversión de las cohortes de marzo con la de varias cohortes anteriores, controlando por edad del usuario gratuito. Esto puede aportar evidencia, pero no sustituye completamente a un experimento porque la publicidad y la mención siguen siendo factores difíciles de separar.

## Recomendación práctica

Mantendría la secuencia, porque los resultados son compatibles con que haya funcionado, pero lanzaría una nueva prueba con un **holdout del 10–20%** de los usuarios gratuitos. Mantendría constantes, en lo posible, la publicidad y las campañas con creadores, registrando la exposición de cada usuario.

Mediría principalmente:

1. Conversión a pago a 30 días.
2. MRR incremental por usuario elegible.
3. Retención a 60 o 90 días.
4. Coste por conversión incremental.
5. Resultado por cada email de la secuencia.

Hasta tener ese control, la afirmación defendible es: **“los resultados mejoraron durante la campaña”, no “los emails causaron la mejora”.**