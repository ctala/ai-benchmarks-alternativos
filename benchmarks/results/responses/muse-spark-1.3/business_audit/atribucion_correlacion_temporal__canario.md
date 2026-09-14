# Muse Spark 1.3 — business_audit/atribucion_correlacion_temporal

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 19.629s | tokens_per_second: 135.3
- input_tokens: 235 | output_tokens: 2655

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

Conclusión corta: **No se puede saber con estos datos si la secuencia funcionó.**

Prefiero decirte eso que darte un "sí, +29% de MRR" que suene bien pero que los datos no sostienen.

Esto es lo que tienes en realidad:

Pasaste de 9 altas en febrero a 14 en marzo, y de $4.100 a $5.300 de MRR. Eso es un antes-después. Y en el medio pasaron 3 cosas a la vez:

1. Secuencia de emails el 1 de marzo
2. Publicidad de pago desde el 3 de marzo
3. Mención de un creador grande el 12 de marzo

Con ese diseño es imposible aislar el efecto de los emails. Todo el aumento podría ser por los ads, por el video, por variación normal, o por una mezcla. Atribuirlo a los emails sería adivinar.

Tres problemas concretos:

**1. No tienes contrafactual.**
¿Qué hubiera pasado en marzo *sin* emails? No lo sabes porque todos los gratuitos los recibieron. Sin un grupo que no reciba la secuencia, no hay comparación válida.

**2. Tienes dos confusores enormes.**
Ads y mención de creador traen usuarios nuevos que no estaban en tu lista gratuita. Si esos convierten, suben las altas y el MRR de marzo aunque los emails no hagan nada. Y no me pasas el desglose por fuente, así que no podemos separar.

**3. Los números son muy pequeños y muy agregados.**
9 vs 14 son +5 altas. Con volúmenes así, subir o bajar 5 de un mes a otro entra dentro de la variación normal. Necesitarías varios meses de base para saber qué es ruido.

Y el MRR peor aún: el MRR sube por altas, pero también por menos churn, menos downgrades, upgrades, cambios de precio. No sabemos si en marzo se fueron menos clientes o si las 14 altas pagaron más que las 9 de febrero. El MRR agregado no te dice *quién* convirtió ni *por qué*.

### Qué haría falta para estar seguros

No más totales mensuales. Necesitas datos a nivel de usuario y un experimento:

1. **Define la población:** usuarios gratuitos existentes al 1 de marzo, por ejemplo.
2. **Aleatoriza:** 50% recibe la secuencia de 5 emails, 50% no la recibe (holdout). Es lo único que te da causalidad limpia. Tu herramienta de email seguro permite un A/B o split.
3. **Pre-define una métrica y una ventana:** ej. "% de gratuitos que pasan a pago en 30 días". No mires después 10 métricas hasta encontrar una que suba.
4. **No lances nada más a la vez.** Si durante el test metes ads o colaboraciones, que afecten por igual a ambos grupos gracias a la aleatorización.
5. **Mide exposición y fuente:** quién recibió, abrió, clickeó, y de dónde vino cada alta (UTM, encuesta de "¿cómo nos conociste?", fecha de registro como gratuito). Esto no prueba nada solo, pero ayuda a interpretar.

Lo que **sí** puedes hacer ahora como pista, no como prueba:
- Separar las 14 altas de marzo: ¿cuántas ya eran gratuitas antes del 1 de marzo y recibieron la secuencia completa, vs cuántas llegaron nuevas después del 3 y del 12?
- Ver fechas: ¿las altas se concentran después del video del día 12?
- Ver funnel de email: enviados > abiertos > clics > pago.

Si los que convirtieron ni siquiera abrieron los emails, es una señal fuerte en contra. Si coinciden todos con el video, también. Pero ni siquiera eso probaría que los emails causaron la conversión.

Recomendación práctica: no tomes decisiones caras basadas en este marzo - como subir el gasto en ads asumiendo que "los emails convierten solos", o dejar de mejorar la oferta. Lo único que puedes decir al equipo es: marzo fue buen mes, no sabemos por qué.