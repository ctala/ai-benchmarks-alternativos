# Claude Opus 5 (suscripción) — business_audit/atribucion_correlacion_temporal

- model_id: `claude-opus-5`
- success: True  | final: 5.08 | quality: 6.0
- latency_total: 111.683s | tokens_per_second: 58.8
- input_tokens: 2 | output_tokens: 6569

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

## Conclusión corta

No se puede saber. Y no es que falten datos para afinar el número: falta el diseño para responder la pregunta.

Lanzaste tres cosas en la misma ventana de 30 días (secuencia el 1, ads el 3, mención del creador el 12) y mediste un solo resultado agregado. No hay forma matemática de repartir ese +29% entre las tres. Cualquiera que te dé un porcentaje de atribución con estos datos te lo está inventando.

Peor: aunque los emails hubieran sido la única variable, el movimiento que muestras no alcanza para afirmar que pasó algo.

## Los números no aguantan el peso que les estás poniendo

**9 vs 14 altas está dentro del ruido.** Con conteos tan chicos, si el ritmo real fuera constante (~11,5/mes), ver 14 en un mes es bastante común. Test de Poisson condicional: p ≈ 0,20 a una cola. Y marzo tiene 31 días contra 28 de febrero: al mismo ritmo diario esperarías ~10 altas sin hacer nada. Ajustando por eso, p ≈ 0,28.

Traducido: aproximadamente 1 de cada 4 meses te daría una diferencia así por pura variación mensual, con la secuencia apagada.

**El MRR y las altas no cuadran entre sí.** +$1.200 de MRR con 14 altas implica ~$86 promedio por alta nueva, y eso asumiendo churn cero. Si tu plan cuesta menos que eso, la mayor parte del crecimiento de MRR **no viene de las altas nuevas** sino de otra cosa: upgrades, un plan anual contado mal, un cambio de precio, o menos bajas que en febrero. Si cuesta más que eso, entonces perdiste MRR por churn y no lo estás viendo.

Antes de discutir emails, necesitas partir el MRR en cuatro: nuevo, expansión, contracción, churn. Un mes con menos cancelaciones sube el MRR sin que la secuencia haya convertido a nadie.

## El sesgo que casi nadie mira

Si la secuencia se envió al **stock acumulado** de usuarios gratis (todos los que ya tenías), marzo tuvo un evento irrepetible: vaciaste la bodega. Los que llevaban seis meses tibios recibieron un empujón que solo podían recibir una vez.

Eso puede ser una alta legítima, pero no es una tasa. Si proyectas "+5 altas/mes por la secuencia" sobre un flush de stock, tu forecast de abril en adelante va a fallar. Distinto es si solo entraron los registros nuevos desde el 1 de marzo: ahí sí es una tasa, pero entonces el volumen expuesto fue mucho menor y el efecto tendría que haber sido enorme para mover 5 altas.

## Qué haría hoy, en una hora

Son 14 personas. No las analices como estadística, míralas una por una. Para cada una:

| Dato | Para qué |
|---|---|
| Fecha de alta gratis y fecha de pago | Días de tenure antes de convertir |
| ¿Recibió la secuencia? ¿Abrió? ¿Hizo clic? ¿Cuál email? | Evidencia de mecanismo, no de correlación |
| Fuente / UTM de la entrada al plan gratis | Separar ads, creador, orgánico |
| Fecha exacta de la conversión | Detectar el pico del 12-14 de marzo |

Con eso ya sabes bastante:

- Alguien que entró gratis el 12, pagó el 13 y nunca abrió un email: eso es el creador, no la secuencia.
- Alguien que llevaba tres meses gratis, abrió los emails 3 y 4 y pagó al día siguiente: eso es evidencia razonable a favor. No es prueba, pero es mucho más que el agregado.
- Si las conversiones se agrupan el 12-15 de marzo, tu +5 se explica solo con el video.

Ojo con la atribución de último toque de tu plataforma. Si alguien llegó por el video, entró gratis, y tres semanas después convirtió tras el email 4, el reporte te va a decir una sola cosa y las dos participaron. Por eso importa la secuencia de eventos por persona, no la etiqueta de fuente.

**Chequeo de plausibilidad temporal:** si tus 5 emails se despliegan en dos o tres semanas, quien pagó el 4 de marzo alcanzó a recibir uno. No le atribuyas a la secuencia completa una conversión que ocurrió antes de que la secuencia terminara.

## Qué haría falta para estar seguros

Lo único que da causalidad es un **holdout**: un 20-30% de los usuarios gratis nuevos, elegidos al azar, que no reciben la secuencia. Comparas tasa de conversión free→paid entre los dos grupos, con la misma ventana de observación.

Pero te tengo que decir la parte incómoda antes de que lo montes.

Con tus volúmenes, un holdout probablemente **nunca llegue a significancia estadística** para un efecto moderado. Cálculo rápido: si tu conversión base free→paid es ~2,5% y quieres detectar una mejora a 3,75% (un lift del 50%, que ya sería excelente), necesitas alrededor de 3.000 usuarios gratis **por brazo**. Unos 6.000 en total. Si entran unos cientos al mes, eso son años.

Para detectar un lift del 100% (2,5% → 5%) bastan ~900 por brazo, unos 1.800 en total. Eso sí puede ser alcanzable en unos meses, y define bien el terreno: **con tu tamaño solo vas a poder distinguir un efecto grande de nada.** Los efectos medianos van a quedar permanentemente en zona gris.

Así que el plan realista es:

1. **Corre el holdout igual**, con 20-30%, y déjalo correr sin mirar cada semana. Lo revisas cuando acumules ~1.500-2.000 usuarios gratis en total, no antes. Mirar resultados parciales y parar cuando se ve bonito es la forma más común de engañarse.
2. **No repitas el error de marzo:** si vas a evaluar la secuencia, no cambies los ads ni el copy ni el pricing en la misma ventana. Un cambio a la vez.
3. **Mientras tanto, decide con evidencia de mecanismo,** no con el MRR: tasa de apertura, clics, y qué porcentaje de los que pagaron habían tocado los emails antes. Es sesgado (los más interesados abren más), pero es honesto sobre lo que es.
4. **Mide el costo.** Los $400 de ads sí tienen un CAC calculable si trazas la fuente. Los emails son casi gratis en marginal, lo que baja mucho el listón: si no te cuestan tiempo recurrente y no molestan a nadie, la decisión de mantenerlos no requiere probar causalidad. La decisión de *invertir más* en ellos, sí.

## La prueba barata que llega sola

Abril te va a decir bastante gratis. La mención del creador es un evento único y no se repite; la secuencia sigue corriendo.

- Si abril vuelve a 9-10 altas con la secuencia activa: el bump de marzo fue el creador.
- Si abril se mantiene en 13-15: hay algo estructural nuevo, aunque todavía no sabrás si son los emails o los ads.
- Si sube más: probablemente los ads, que en marzo solo corrieron 28 días y con aprendizaje inicial.

Nada de eso es prueba. Pero dos o tres meses de la serie diaria de altas, con los eventos marcados en la línea de tiempo, valen más que cualquier análisis que pueda hacerte con dos puntos.

## Resumen en una línea

Tienes un mes bueno con tres explicaciones posibles y una diferencia (9 → 14) que ni siquiera se distingue del azar. El estado correcto de la secuencia hoy es **"funcionando técnicamente, ROI sin medir"**. Registra eso así en tus notas, porque en tres meses vas a recordar "los emails subieron el MRR 29%" y vas a tomar decisiones de presupuesto sobre una afirmación que nunca verificaste.