# Claude Opus 5.5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 23.555s | tokens_per_second: 88.0
- input_tokens: 366 | output_tokens: 2073

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

# Conclusión: con estos datos no se puede saber si la secuencia funcionó

**Hubo una mejora real en el negocio, pero no hay forma de atribuírsela a los emails.** Cualquier respuesta tipo "sí, funcionó" o "aportó X%" sería inventada.

## Por qué no se puede concluir

**1. Tres cambios a la vez, en la misma ventana**

| Fecha | Cambio |
|---|---|
| 1 de marzo | Secuencia de emails |
| 3 de marzo | Publicidad ($400) |
| 12 de marzo | Mención de un creador con audiencia grande |

Los tres pueden explicar, por sí solos, 5 altas adicionales. La mención de un creador grande en particular puede generar picos fuertes. Con solo el total mensual es imposible separar los efectos.

**2. Los efectos están mezclados entre sí**

Los usuarios que llegaron por la publicidad o el video probablemente se registraron en el plan gratuito y **recibieron la secuencia**. Si después pagaron, no queda claro qué los convenció: el video, el anuncio o el email 3. Incluso con datos de clics, la atribución sería ambigua.

**3. La diferencia es pequeña y sin línea base**

- Pasar de 9 a 14 altas son 5 personas. Sin saber cuánto varían normalmente tus altas mes a mes, no se puede distinguir una mejora real de una fluctuación normal. Si en enero tuviste 13, por ejemplo, febrero sería el mes raro y no marzo.
- Febrero tiene 28 días y marzo 31. Eso solo ya explica alrededor del 10% de diferencia.

**4. El MRR no es lo mismo que las altas**

El +$1.200 de MRR es el resultado neto de altas, bajas, cambios de plan y cancelaciones. Sin esa descomposición, ni siquiera sabemos cuánto del crecimiento viene de las 14 altas.

## Qué puedes averiguar ya, con datos que probablemente tienes

Esto no da certeza, pero puede dar indicios:

1. **Segmentar las 14 altas por fecha de registro en el plan gratuito.**
   - Las personas registradas *antes* del 1 de marzo son la base que existía antes de la publicidad y el video. Si su tasa de conversión en marzo es claramente mayor que la de meses anteriores, hay un indicio a favor de los emails. No es prueba: también pudieron ver el video.
   - Las personas registradas después del 3 o del 12 de marzo probablemente vienen de la publicidad o el video.
2. **Revisar la plataforma de email.** ¿Cuántas de las 14 hicieron clic en un email y pagaron poco después? Ese dato indica que el email participó, no que haya causado el pago.
3. **Mirar la distribución diaria de las altas.** Si se concentran después del 12 de marzo, el video es el principal sospechoso.
4. **Sacar el histórico de altas de 6 a 12 meses** para saber si 14 está fuera de lo normal.
5. **Descomponer el MRR** en nuevo, expansión, contracción y bajas.

## Qué haría falta para estar seguros

**Un grupo de control.** A partir de ahora, separa al azar un 20–30% de los nuevos usuarios gratuitos que *no* reciban la secuencia. Compara la tasa de conversión a pago entre ambos grupos después de 30, 60 y 90 días.

- Como los dos grupos reciben la misma publicidad, el mismo video y la misma estacionalidad, la diferencia entre ellos sí se puede atribuir a los emails.
- Con tus volúmenes, que son bajos, vas a necesitar varios meses de datos acumulados para que la diferencia sea confiable. Ten paciencia y no saques conclusiones con 2 o 3 conversiones de diferencia.
- Complementa con UTMs en todos los links de los emails y de la publicidad, y con una pregunta simple en el checkout: "¿Cómo nos conociste?".

**Resumen para el equipo:** marzo fue un buen mes, pero hoy no sabemos por qué. No hay que apagar la secuencia ni darla por exitosa. Lo que hay que hacer es empezar a medirla bien desde ya.