# Qwen 3.8 27B — business_audit/atribucion_correlacion_temporal

- model_id: `qwen/qwen3.8-27b`
- success: True  | final: 8.35 | quality: 10.0
- latency_total: 46.473s | tokens_per_second: 44.1
- input_tokens: 283 | output_tokens: 2048

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



**Conclusión corta: no se puede saber con los datos que me has dado.**  
No puedo decir que la secuencia de emails “funcionó” de forma causal. Los números son positivos, pero hay al menos dos eventos externos importantes en el mismo período que también podrían explicar el crecimiento: la publicidad y la mención del creador.

## Qué dicen los datos

- MRR pasó de **$4.100** a **$5.300**, un aumento de **$1.200** o **+29%**.
- Las altas al plan pago pasaron de **9 en febrero** a **14 en marzo**, es decir, **+5 altas**.
- La secuencia de emails empezó el **1 de marzo**.
- La publicidad empezó el **3 de marzo**.
- El creador mencionó la comunidad el **12 de marzo**.

Entonces, el crecimiento se produce en un mes donde ocurren **tres posibles causas simultáneas**:

1. Secuencia de emails.
2. Publicidad de pago.
3. Mención de un creador con audiencia grande.

Con eso no puedo separar cuánto vino de cada una.

## Por qué no puedo afirmar que la secuencia funcionó

El problema es que los datos muestran **correlación temporal**, no **causalidad**.

Es plausible que la secuencia de emails haya ayudado, pero también es plausible que el crecimiento venga sobre todo de la publicidad o del creador. Incluso puede ser una combinación:

- 2 altas por emails, 2 por publicidad, 1 por creador.
- 0 por emails, 3 por publicidad, 2 por creador.
- 5 por emails, 0 por publicidad, 0 por creador.

Con lo que me has dado, no hay forma de distinguir entre esas opciones.

Además, el MRR no solo depende de las nuevas altas. También depende de:

- Cancelaciones.
- Downgrades.
- Upgrades.
- Cambios de plan.
- Precios.
- Usuarios que pagan más o menos que antes.

Por ejemplo, un aumento de MRR puede venir de más altas, pero también de menos cancelaciones o de usuarios que pasaron a un plan más caro. No podemos saberlo solo con el MRR total.

## Lo que sí puedo decir

Lo que sí puedo decir es esto:

> Hubo un crecimiento relevante en marzo, pero no hay evidencia suficiente para atribuirlo específicamente a la secuencia de emails.

Eso no significa que la secuencia no sirvió. Significa que **no podemos demostrarlo** con estos datos.

## Qué haría falta para estar seguros

Lo ideal sería poder medir la secuencia de forma experimental.

### 1. Hacer un test A/B o holdout

Lo más limpio sería dividir aleatoriamente a los usuarios gratuitos en dos grupos:

- **Grupo A:** recibe la secuencia de 5 emails.
- **Grupo B:** no recibe la secuencia, o recibe una versión neutra/placebo.

Luego medir durante varias semanas:

- Tasa de conversión a plan pago.
- MRR generado por cada grupo.
- Altas totales.
- Ingresos por usuario.
- Cancelaciones.
- Tiempo hasta conversión.

Si el grupo con emails convierte significativamente más que el grupo sin emails, entonces sí tendríamos una base razonable para decir que la secuencia funcionó.

### 2. Medir por cohortes

Habría que ver qué pasa con los usuarios que entraron en distintos momentos:

- Usuarios que recibieron el email 1.
- Usuarios que recibieron el email 2.
- Usuarios que recibieron el email 3.
- Usuarios que recibieron el email 4.
- Usuarios que recibieron el email 5.

Y luego ver:

- ¿Cuántos abrieron?
- ¿Cuántos hicieron clic?
- ¿Cuántos convirtieron después de cada email?
- ¿Cuántos convirtieron en 7, 14 o 30 días?
- ¿Cuál fue su MRR posterior?

Eso ayudaría a entender si la secuencia tiene efecto, pero aún así no sería perfecto si no hay grupo control.

### 3. Aislar el efecto de la publicidad y del creador

Para no mezclar las causas, habría que registrar ventanas temporales y segmentos:

- ¿Cuántas altas vinieron antes de la publicidad?
- ¿Cuántas altas vinieron después de la mención del creador?
- ¿Las altas llegaron desde campañas pagadas?
- ¿Las altas llegaron desde el enlace del creador?
- ¿