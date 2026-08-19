# Sakana Namazu — business_audit/atribucion_correlacion_temporal

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 8.962s | tokens_per_second: 208.7
- input_tokens: 270 | output_tokens: 1870

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

**No se puede saber si la secuencia de emails funcionó.** Con los datos que tienes, afirmar que fue efectiva sería una conclusión cómoda pero falsa. Te explico por qué y qué necesitarías para estar seguro.

### El problema central: tres causas, un efecto

En marzo pasaron tres cosas al mismo tiempo:
1. Tus emails automatizados (1 de marzo).
2. Campaña de publicidad pagada (3 de marzo).
3. Mención de un creador grande (12 de marzo).

El MRR subió 29% y las altas crecieron de 9 a 14. Pero **no tienes forma de separar qué porción del crecimiento corresponde a cada canal**. Especialmente la mención del creador y la publicidad pueden explicar el salvo por sí solas, ya que ambos traen tráfico *nuevo*, mientras que tus emails solo actúan sobre usuarios *ya existentes* del plan gratuito.

Además, hay dos señales que debilitan aún más la hipótesis del email:
- El MRR subió $1,200, pero solo se añadieron 5 altas netas. Eso sugiere que parte del aumento podría venir de usuarios que entraron directo a pagar por la publicidad o la mención (posiblemente en planes de mayor valor), y no necesariamente de la conversión de gratuitos a pagos.
- No tienes un grupo de control: no sabes cuántos de esos gratuitos se habrían convertido de todos modos sin la secuencia.

### ¿Qué haría falta para estar seguros?

Para poder decir "los emails funcionaron" necesitarías alguna de estas evidencias:

1. **Grupo de control**
   - Haber dividido a tus usuarios gratuitos en dos grupos aleatorios: uno que recibió los emails y otro que no. Si el grupo de emails convierte significativamente más, ahí sí hay efecto demostrable.

2. **Atribución directa**
   - Saber cuántas de esas 14 altas de marzo venían de usuarios que ya estaban en el plan gratuito *antes* del 1 de marzo (posibles afectados por el email), versus cuántos llegaron por la publicidad o la mención.
   - Links de tracking (UTM) dentro de los emails para ver conversiones atribuibles directamente a esos clics.

3. **Datos diarios de altas y tráfico**
   - Ver la curva diaria de nuevos pagos. Si hay un pico brusco alrededor del 12 de marzo, es casi seguro que fue la mención del creador. Si los picos coinciden exactamente con el envío de los emails (con un lag de 24-48h), tendrías una pista más sólida.

4. **Cohort analysis**
   - Comparar la tasa de conversión de gratuitos a pagos de los usuarios que abrieron/clickaron los emails vs. los que no interactuaron vs. los que ni siquiera los recibieron.

5. **Costo de adquisición estimado**
   - Con $400 en publicidad, calcula cuántas altas esperabas de eso. Si la publicidad y la mención ya explican razonablemente las 14 altas, no sobra crecimiento para atribuir a los emails.

### Mi recomendación

No gastes confianza en un "sí, funcionó". Lo más honesto ahora es decir: **"los números agregados de marzo son consistentes con un buen mes, pero no permiten aislar el efecto de los emails"**.

Si quieres probar esto bien, la próxima vez:
- Pausa publicidad e influencers durante el experimento, o
- Haz un A/B test donde solo la mitad de tus gratuitos reciba la secuencia.

¿Tienes acceso a datos diarios de altas o a la fuente de origen de esas 14 conversiones de marzo? Con eso podríamos hacer una primera aproximación más informada, aunque seguiría sin ser concluyente.