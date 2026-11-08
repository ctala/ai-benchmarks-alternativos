# Kimi K3.1 Pro — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 7.86 | quality: 10.0
- latency_total: 161.413s | tokens_per_second: 23.6
- input_tokens: 354 | output_tokens: 3806

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

**No se puede saber con estos datos si la secuencia funcionó.** Lo que sí podemos afirmar es que marzo fue mejor en agregado, pero **no que los emails causaran esa mejora**.

- El MRR aumentó **$1.200**, un **29,3%**.
- Las altas pasaron de 9 a 14: **5 más**, un **55,6%**.
- Pero la secuencia coincidió con otras dos intervenciones capaces de aumentar las altas: la publicidad y la mención del creador.

Además, faltan datos esenciales:

- **No hay denominadores:** necesitamos saber cuántos usuarios gratuitos eran elegibles cada mes. Si la base gratuita creció mucho por la publicidad o el video, podría haber más altas con una tasa de conversión igual o incluso menor.
- **No sabemos el origen de las 14 altas:** algunas podrían ser compras directas de personas nuevas, sin haber pasado por la secuencia.
- **El MRR total no mide únicamente conversiones:** también puede cambiar por churn, reactivaciones, expansiones, descuentos o cambios de plan.
- **No hay grupo de comparación ni tendencia histórica:** un solo mes antes y otro después no permite separar el efecto de los emails del resto de factores.

En teoría, los datos son compatibles con que los emails ayudaran, no tuvieran efecto o incluso perjudicaran ligeramente mientras las otras acciones impulsaban el resultado.

## Qué haría falta para tener evidencia sólida

La mejor opción sería un **experimento con grupo de control aleatorio**:

1. Entre los usuarios gratuitos elegibles, asignar aleatoriamente quién recibe la secuencia y quién continúa sin ella, manteniendo el resto de comunicaciones habituales.
2. No hace falta detener la publicidad: ambos grupos deben vivir las mismas condiciones externas, de modo que publicidad, menciones y estacionalidad queden equilibradas por la aleatorización.
3. Definir previamente una ventana común, por ejemplo, conversión dentro de los **30 días posteriores a la asignación**.
4. Comparar:
   - **Conversión:** altas al plan pago ÷ usuarios elegibles asignados a cada grupo.
   - **MRR nuevo por usuario elegible**, en una ventana fija.
   - Idealmente, bajas, desuscripciones y quejas como métricas de seguridad.
5. Analizar a todos los asignados, no solamente a quienes abrieron los emails: quienes abren suelen tener más interés desde el principio. Aperturas y clics sirven para diagnosticar el funcionamiento, pero **no demuestran ventas incrementales**.
6. Calcular previamente el tamaño de muestra. Con sólo 9–14 altas mensuales, podría hacer falta acumular varios meses para detectar algo distinto de un efecto grande.

Mientras tanto, revisaría los datos a nivel de usuario —fecha de elegibilidad, recepción de emails, fecha del alta, plan y MRR, fuente de adquisición— y descompondría el MRR en nuevo, expansión, contracción, churn y reactivación. Eso puede aportar indicios, pero no sustituye al control.

**En resumen: marzo arroja un resultado agregado favorable, pero la secuencia no está validada. No le atribuiría los $1.200 adicionales ni las cinco altas extra con la evidencia actual.**