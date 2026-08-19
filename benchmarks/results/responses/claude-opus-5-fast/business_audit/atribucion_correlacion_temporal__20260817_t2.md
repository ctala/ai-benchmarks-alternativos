# Claude Opus 5 Fast — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.02 | quality: 10.0
- latency_total: 18.704s | tokens_per_second: 180.0
- input_tokens: 364 | output_tokens: 3367

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

**No se puede saber.** Con estos datos no hay forma de separar el efecto de la secuencia de emails del de la publicidad y el del video. No es que "probablemente funcionó pero falta confirmar": es que los datos son literalmente compatibles con que la secuencia no haya aportado nada.

Y hay un detalle peor: los números tampoco alcanzan para afirmar que *algo* funcionó.

---

## Por qué

**1. Tres cambios simultáneos, un solo mes de observación.**
Emails (1/3), ads (3/3), creador (12/3). Tres causas candidatas, un único resultado agregado. Cualquier reparto del crédito que haga ahora sería inventado.

**2. El salto de 9 → 14 es más chico de lo que parece.**

- Marzo tiene 31 días y febrero 28. A la misma tasa diaria, febrero "equivale" a ~10 altas en marzo. Así que la comparación real es **14 vs ~10**, no 14 vs 9.
- Con volúmenes tan bajos, la variación aleatoria mes a mes es grande. Si tu tasa real fuera de ~10 altas/mes, ver 14 o más por puro azar pasa aproximadamente 1 de cada 7-8 meses. Eso no es una señal, es ruido normal.

Traducción: si en enero hubieras tenido 13 altas sin hacer nada, marzo no tendría nada de especial. **Necesito ver tus altas mensuales de los últimos 6-12 meses antes de decir que 14 es un número alto.** Es el dato más importante que falta y probablemente ya lo tenés.

**3. El +29% de MRR y el +56% de altas no cuadran.**
Las altas subieron 55% pero el MRR solo 29%. Eso significa que pasó alguna de estas cosas: hubo churn que se comió parte del crecimiento, las altas de marzo entraron a precios más bajos, o el MRR de febrero incluía algo que no se repitió. **No celebres el +29% hasta saber cuál.** El número bruto de MRR mezcla altas, bajas, upgrades y downgrades; sin desglosarlo no dice nada sobre la secuencia.

**4. Confusión de poblaciones.**
La secuencia apunta al *stock* de usuarios gratuitos que ya tenías. Los ads y el creador traen usuarios gratuitos *nuevos*, que además entran a la secuencia. O sea que los tres canales están enredados por diseño: parte del efecto "email" puede ser en realidad tráfico pago que convirtió bien.

---

## Qué haría falta

**Cosas que probablemente ya tenés y respondería mucho hoy mismo:**

1. **Altas mensuales de los últimos 6-12 meses.** Para saber cuál es tu variación normal. Sin esto no hay línea base.
2. **Fecha exacta de cada una de las 14 altas.** Si 8 cayeron entre el 12 y el 16 de marzo, fue el creador y no hay más que discutir. Si están repartidas parejo, la hipótesis del creador se debilita.
3. **Fecha de registro de cada una de las 14.** Distingue lo esencial: quienes ya eran usuarios gratuitos antes del 1/3 (candidatos legítimos al efecto email) vs. quienes se registraron en marzo (llegados por ads/creador).
4. **Fuente/UTM de cada alta**, si tenés tracking.
5. **Churn de febrero y marzo por separado**, para poder leer el MRR.
6. **Cuántos usuarios gratuitos entraron a la secuencia y cuántos de ellos convirtieron.** Eso te da una tasa de conversión de la cohorte email, comparable contra la tasa histórica de conversión free→pago.

Con los puntos 1, 3 y 6 ya podrías tener una respuesta razonable, aunque no definitiva.

**Lo que hace falta para estar realmente seguros:**

Un experimento. Retené entre el 20% y el 30% de los usuarios gratuitos nuevos como grupo de control que no recibe la secuencia, asignados al azar, y dejalo correr. Comparás tasa de conversión entre grupos. Es la única forma de aislar el efecto.

Aviso honesto sobre esto: con ~14 altas al mes, un test así tarda **varios meses** en dar una señal confiable. Si la secuencia mejora la conversión un 30%, vas a necesitar del orden de cientos de usuarios por rama para detectarlo. No es un test de dos semanas. Si eso no es viable, la alternativa es aceptar que vas a decidir con evidencia débil, y decidirlo conscientemente.

**Y algo que no medí porque no puedo:**

Con $400 de ads no puedo decirte si fueron rentables. Necesito cuántas altas vinieron de ads y cuál es tu retención promedio. Si el ticket ronda los $85/mes y los ads trajeron 5 altas, el primer mes ya casi se paga solo — pero eso depende enteramente de si esos usuarios se quedan, y de eso no tengo ni un dato.

---

## Recomendación práctica

No apagues la secuencia: cuesta poco y es plausible que ayude. Pero **no la declares ganadora ni la uses como base para decidir dónde poner más esfuerzo.**

Lo accionable de este mes es otra cosa: el video del creador es el único evento con una fecha lo bastante puntual como para verse en los datos diarios. Mirá esa curva primero. Si ahí está la mayor parte del salto, ya sabés dónde invertir, y de paso te ahorrás atribuirle a los emails un mérito que no tuvieron.