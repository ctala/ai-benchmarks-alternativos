# Tencent Hy4 preview — business_audit/atribucion_correlacion_temporal

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.19 | quality: 10.0
- latency_total: 241.688s | tokens_per_second: 55.4
- input_tokens: 256 | output_tokens: 13382

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

**Conclusión corta: no se puede saber.**  
Con estos datos **no puedes afirmar que la secuencia de emails funcionó**. Lo único que dicen los números es: *en marzo hiciste tres cosas nuevas a la vez (emails, publicidad y mención de un influencer) y el mes cerró mejor que febrero*. Eso es una coincidencia temporal, no una prueba de causalidad.

Si tuviera que resumirlo en una frase para el equipo, sería:

> “Marzo mejoró, pero no sabemos qué parte fue de los emails. Necesitamos un grupo control y tracking antes de atribuirles el resultado.”

---

## Por qué los datos no sostienen la conclusión

### 1. Hubo tres intervenciones simultáneas
El 1 de marzo lanzaste la secuencia de emails.  
El 3 de marzo empezaste a pagar publicidad.  
El 12 de marzo un creador grande mencionó la comunidad.

Cualquiera de esas tres cosas —o la suma de ellas— podría explicar el aumento. Sin aislar el efecto de cada una, no hay forma de saber qué aportó la secuencia.

El influencer, además, es una explicación alternativa muy fuerte: una mención con audiencia grande suele generar picos de tráfico y altas por sí sola.

### 2. No hay atribución: las 14 altas son una bolsa mezclada
“Altas al plan pago en marzo: 14” es un número agregado. No sabes:

- cuántas vinieron de los emails,
- cuántas de los ads,
- cuántas del influencer,
- cuántas fueron orgánicas o de boca a boca,
- cuántas eran usuarios que ya eran gratuitos antes del 1 de marzo,
- cuántas eran usuarios nuevos que nunca pasaron por la secuencia completa.

Sin UTMs, códigos, fuentes en el checkout o tracking por usuario, no puedes separar eso.

### 3. Faltan los denominadores: no tienes la tasa de conversión
La secuencia iba dirigida a **usuarios del plan gratuito**. Para saber si funcionó, lo importante no es cuántas altas hubo en total, sino:

> De los gratuitos que recibieron la secuencia, ¿qué porcentaje pasó a pago? ¿Y qué porcentaje pasaba antes?

Ejemplo de por qué esto importa:

- **Febrero:** 100 usuarios gratuitos → 9 se hicieron de pago → **9% de conversión**.
- **Marzo:** entran 400 gratuitos nuevos por ads/influencer → en total hay 500 gratuitos → se hacen de pago 14 → **2,8% de conversión**.

En ese caso, las altas absolutas subieron de 9 a 14, pero la **tasa de conversión bajó**. Los emails podrían incluso haber funcionado mal, o no haber hecho nada, y el aumento absoluto lo explicaría el simple hecho de que llegó mucha más gente.

Sin saber cuántos gratuitos había, cuántos recibieron los emails y cuántos convirtieron, el dato “14 altas” no dice mucho.

### 4. MRR no es lo mismo que “altas”
MRR pasó de **$4.100** a **$5.300**: +$1.200 (+29%). Pero el MRR es una métrica **neta** que mezcla:

- nuevas altas,
- upgrades / expansión,
- downgrades,
- churn/bajas.

Las 14 altas son **altas brutas**. No son lo mismo que el crecimiento neto del MRR.

Además, no has publicado el precio medio ni el MRR waterfall, así que no puedes ligar el +$1.200 a esas 14 altas. Por ejemplo:

- Si el precio medio es **$100**, 14 altas nuevas sumarían **$1.400** de MRR nuevo. Para que el neto sea +$1.200, tendrías que haber tenido **$200 de churn**.
- Si el precio medio es **$50**, 14 altas nuevas sumarían **$700**. Para llegar a +$1.200 netos, tendrías que haber tenido **$500 de expansión** de clientes existentes o algo similar.

Es decir: el MRR subió, pero **no sabes si lo explican las nuevas altas, los upgrades, o una mezcla de todo**.

### 5. La muestra es muy pequeña y el aumento cabe dentro del ruido
Comparas:

- Febrero: **9 altas** en **28 días** → 0,32 altas/día.
- Marzo: **14 altas** en **31 días** → 0,45 altas/día.

Ajustando por días, el aumento es de aproximadamente **+41%**, no +56%, porque marzo tiene 3 días más.

Aun así, con números tan bajos, la diferencia es frágil. Si tratas las altas como un conteo Poisson:

- con 9 esperadas en marzo, la probabilidad de ver 14 o más por azar es de alrededor del **7%**;
- ajustando febrero a 31 días, esperarías unas 10 altas y la probabilidad de ver 14 o más ronda el **13%**.

En cualquier caso, **no es estadísticamente significativo** al 5%. Y eso asumiendo, además, que nada más cambió, lo cual no es cierto.

### 6. La ventana de medición puede estar truncada
La secuencia es de 5 emails. Dependiendo de cada cuánto se envíen, un usuario que entró a la lista el 20 de marzo puede no haber recibido toda la secuencia antes del 31 de marzo.

Y si el influencer trajo gente el 12 de marzo, parte de ese impacto puede estar todavía en curso. Medir solo hasta el 31 de marzo puede ser **prematuro** para juzgar una secuencia de nutrición.

---

## Qué haría falta para estar seguros

Para poder decir “la secuencia funcionó” con honestidad, necesitarías esto:

### 1. Un grupo de control / holdout
Lo ideal: dividir aleatoriamente a los usuarios gratuitos en dos grupos:

- **Grupo A:** recibe la secuencia de emails.
- **Grupo B:** no la recibe, o recibe la comunicación habitual.

Después comparas la **tasa de conversión a pago** y el **MRR por usuario** entre ambos grupos en una ventana definida (por ejemplo, 30 días después de terminar la secuencia).

Sin eso, no hay contrafactual: no sabes qué habría pasado sin los emails.

### 2. Tracking por fuente y por email
Necesitas poder responder, para cada alta:

- ¿de dónde vino?
- ¿recibió la secuencia?
- ¿abrió / clicó los emails?
- ¿cuánto tiempo pasó desde el primer email hasta que pagó?

Hace falta:

- UTMs o links trackeados en los emails,
- UTMs en los ads,
- tracking del influencer,
- campo de procedencia en el checkout,
- conexión en el CRM entre usuario, emails y facturación.

### 3. Datos de embudo, no solo totales
Necesitas:

- número de usuarios gratuitos al inicio,
- cuántos entraron a la secuencia,
- cuántos recibieron cada email,
- tasas de apertura y clic,
- conversión por paso,
- conversión global de gratuito a pago.

Sin eso, “14 altas” es solo un número agregado sin contexto.

### 4. MRR waterfall mensual
Desglosa el MRR así:

- MRR inicial,
- **+** nuevo MRR,
- **+** expansión,
- **−** contracción,
- **−** churn,
- **=** MRR final.

Solo así sabrás si el +$1.200 vino de las nuevas altas o de otra cosa.

### 5. Línea base y más tiempo
Un solo mes antes (febrero) no es suficiente. Necesitas varios meses de:

- altas,
- MRR,
- usuarios gratuitos,
- tasa de conversión,
- inversión en ads,
- eventos como el influencer.

Y necesitas comparar **por día**, no solo totales mensuales, porque febrero y marzo no tienen los mismos días.

### 6. Tamaño de efecto y potencia
Con volúmenes como 9 o 14 altas al mes, vas a necesitar **mucho tiempo o más tráfico** para detectar efectos reales. Antes de sacar conclusiones, conviene calcular:

- qué mejora mínima quieres detectar,
- cuántos usuarios gratuitos necesitas en cada grupo,
- cuánto durará el test.

Si tu base de gratuitos es pequeña, el experimento puede no dar una señal fiable nunca. En ese caso, la decisión tendrá que apoyarse en métricas cualitativas y de engagement, no en “MRR subió”.

---

## Recomendación práctica

No escales ni mates la secuencia basándote en este dato. Con la información actual, **la respuesta honesta es “no se puede saber”**.

Lo responsable sería:

1. Seguir midiendo, pero **no atribuir el +29% de MRR ni el aumento de 9 a 14 altas a los emails**.
2. Montar un **holdout** para la próxima secuencia.
3. Añadir **tracking por fuente** y **embudo de emails**.
4. Empezar a construir el **MRR waterfall** mensual.
5. Comunicar al equipo algo así como:

> “En marzo lanzamos emails, publicidad y tuvimos una mención de un influencer. El MRR subió 29% y las altas pasaron de 9 a 14, pero con los datos actuales no podemos aislar el efecto de la secuencia de emails. Necesitamos un grupo control y tracking para saberlo.”

Esa es la conclusión que los datos sostienen. Cualquier afirmación más fuerte —“los emails funcionaron” o “los emails no sirven”— sería, con esta evidencia, una conclusión cómoda pero no defendible.