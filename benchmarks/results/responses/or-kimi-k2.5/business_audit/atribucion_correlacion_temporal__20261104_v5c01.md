# Kimi K2.5 — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.23 | quality: 10.0
- latency_total: 84.36s | tokens_per_second: 29.8
- input_tokens: 270 | output_tokens: 2515

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

**Conclusión: No se puede saber.** Y afirmar lo contrario —ya sea que funcionó o que no— sería una conjetura, no un análisis.

Con los datos que tienes, es imposible atribuir el crecimiento de marzo (o parte de él) a la secuencia de emails. Te explico por qué, y luego qué necesitarías para poder responder con certeza.

---

### Por qué no se puede saber

**1. Tienes tres tratamientos simultáneos y una sola variable de resultado**
En marzo ocurrieron al menos tres cambios importantes en menos de dos semanas:
- 1/03: Secuencia de emails a gratuitos.
- 3/03: Inicio de publicidad pagada ($400).
- 12/03: Mención masiva de un creador.

Cuando varias cosas cambian al mismo tiempo y solo miras el resultado global, no puedes desenredar qué causó qué. Es el problema clásico de las **variables de confusión**.

**2. No sabes quién generó las altas**
Las 14 altas de marzo podrían ser:
- Usuarios gratuitos antiguos que convirtieron gracias a tus emails.
- Usuarios nuevos que llegaron por los anuncios y pagaron directamente.
- Seguidores del creador que entraron en caliente y pagaron de inmediato.
- Una combinación de las tres.

Si las altas vinieron principalmente de tráfico nuevo (ads + influencer), los emails no tuvieron nada que ver. Si vinieron de tu base antigua, podrían haber influido. Pero no tienes esa segmentación.

**3. Faltan datos de referencia (baseline)**
- ¿Cuál era la tasa de conversión mensual habitual de tu plan gratuito antes de marzo? Si históricamente convertías 12-15 usuarios al mes con cero emails, entonces 14 altas sería normal, no un éxito. Si convertías 2-3, sería extraordinario. Sin esa línea base, el número 14 no significa nada.
- ¿Cuántos usuarios gratuitos tenías al 1 de marzo? Si tenías 5,000, 14 conversiones es una tasa baja. Si tenías 100, es altísima.

**4. Los números son demasiado pequeños para diferenciar señal de ruido**
La diferencia entre febrero y marzo es solo **5 altas adicionales** (14 vs. 9). Con muestras tan pequeñas, una sola conversión extra por el influencer o por un tweet aleatorio cambia todo el porcentaje. El margen de error es enorme.

**5. El MRR no ayuda a atribuir**
El salto de $4,100 a $5,300 (+$1,200) es consistente con 5 altas nuevas si tu ARPU es ~$240, pero también podría deberse a:
- Upgrades de usuarios existentes a un plan más caro.
- Nuevos usuarios del influencer que eligieron un plan anual (reconocen más MRR de golpe).
- Menos cancelaciones de lo habitual (retención, no adquisición).

---

### Qué haría falta para estar seguros

Para poder decir "la secuencia de emails funcionó" necesitarías algo de lo siguiente:

| Lo que necesitas | Por qué |
|---|---|
| **Grupo de control** | Dividir tu base gratuita el 1 de marzo en dos: 50% recibe los emails, 50% no. Si la tasa de conversión del grupo expuesto es significativamente mayor (y el timing de las conversiones coincide con los envíos), tienes evidencia. |
| **Atribución por fuente** | Saber, de cada una de las 14 altas, de dónde venía el usuario: lista gratuita antigua, campaña de ads, tráfico del influencer, orgánico, etc. |
| **Fecha exacta de cada alta** | Si las 14 altas se concentraron entre el 12 y 20 de marzo, el influencer es el principal sospechoso. Si se concentraron justo después de cada email (con 24-48h de delay), apuntaría a los emails. |
| **Tasa de conversión histórica de gratuitos** | Comparar marzo no con febrero (que puede tener estacionalidad diferente), sino con el promedio de conversión de tu lista gratuita en los últimos 3-6 meses. |
| **Datos de engagement de los emails** | Aperturas, clics y, lo más importante, cuántos de los que clickearon terminaron pagando. Si nadie que abrió el email pagó, es una prueba fuerte de que no funcionaron (aunque no definitiva). |
| **Aislar variables** | Si vas a hacer otro experimento, no lances ads ni busques menciones al mismo tiempo. O, si no puedes evitarlo, al menos haz un análisis de cohortes excluyendo a todo usuario que se registró después del 1 de marzo. |

---

### Mi recomendación práctica

No le digas al equipo que "la secuencia funcionó porque crecimos 29%". Eso es una **narrativa conveniente pero insostenible**. Diles esto:

> "En marzo crecimos, pero tenemos al menos tres factores grandes ocurriendo al mismo tiempo y no tenemos forma de saber cuánto le corresponde a cada uno. Para la próxima secuencia, hagamos un envío con grupo de control o, como mínimo, etiquetemos a los usuientes que entran por ads/influencer para no mezclarlos con la base antigua."

Si quieres, puedo ayudarte a diseñar un experimento simple para la próxima campaña que sí te dé una respuesta clara.