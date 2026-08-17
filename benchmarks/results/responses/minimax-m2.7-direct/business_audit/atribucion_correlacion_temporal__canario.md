# MiniMax M2.7 (directo) — business_audit/atribucion_correlacion_temporal

- model_id: `MiniMax-M2.7`
- success: True  | final: 7.23 | quality: 8.0
- latency_total: 32.633s | tokens_per_second: 39.8
- input_tokens: 217 | output_tokens: 1299

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

# Análisis: La secuencia de emails y el crecimiento

**Resumen corto:** No se puede saber con estos datos.

---

## Por qué no podemos concluir nada

Tenés tres intervenciones simultáneas:

| Intervención | Inicio |
|---|---|
| Secuencia de 5 emails | 1 de marzo |
| Publicidad pagada ($400) | 3 de marzo |
| Mención de creador con audiencia | 12 de marzo |

El crecimiento que ves ($1.200 MRR, +5 altas) podría ser por cualquiera de las tres, por las tres juntas, o por algo que no estás midiendo (estacionalidad,word-of-mouth, etc.). Sin aislar los efectos, no hay forma de saber cuál contribuyó cuánto —o si alguno contribuyó en absoluto.

---

## Qué necesitarías para estar seguro

1. **Grupo de control (lo más importante)**
   - Tomar una muestra aleatoria de usuarios del plan gratuito que NO reciban los emails.
   - Comparar la tasa de upgrade entre el grupo con emails y el grupo control.
   - Esto te da el efecto causal real.

2. **Datos de engagement**
   - ¿Cuántos abrieron los emails? ¿Cuántos clicks hubo?
   - ¿Los que se upgraded alguna vez abrieron algún email?

3. **Timing de la conversión**
   - ¿Cuándo se upgraded cada usuario nuevo?
   - Si alguien se upgraded el 15 de febrero, no fue por el email del 1 de marzo.
   - Si alguien se upgraded el 5 de marzo, podría ser cualquiera de las tres intervenciones.

4. **Múltiples cohortes**
   - Una secuencia aislada en un mes es un dato puntual. Repetir el experimento en otros períodos te dice si es replicable o fue suerte.

---

## Lo que sí puedo decir

- **El MRR sí creció.** Eso es un hecho.
- **+5 altas en un contexto de 3 intervenciones simultáneas** no te permite distinguir señal de ruido. Con muestras tan pequeñas (9 vs 14), una o dos conversaciones de un cliente representan ~14% del resultado.
- **El influenciador probablemente tuvo un efecto desproporcionado.** "Un creador con audiencia grande" suele mover números rápido.

---

## Recomendación concreta

La próxima vez que lances una secuencia, hazlo con un grupo control. Even un test de 2-3 semanas te da datos干净的. No es caro en esfuerzo, y te salva de tomar decisiones basándote en correlación.

---

*Si me pasás los datos de apertura/click, o el timing de cada upgrade, puedo afinar más. Pero con lo que hay ahora, ser honesto significa decir "no se puede saber".*