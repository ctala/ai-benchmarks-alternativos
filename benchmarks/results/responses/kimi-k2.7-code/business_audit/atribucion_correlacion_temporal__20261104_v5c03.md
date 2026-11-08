# Kimi K2.7 Code — business_audit/atribucion_correlacion_temporal

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 23.002s | tokens_per_second: 44.0
- input_tokens: 269 | output_tokens: 1011

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

**No se puede saber si la secuencia de emails funcionó con estos datos.** Lo que sí se puede decir es que, en marzo, el negocio creció; pero atribuir ese crecimiento a los emails es una conclusión que los números no sostienen.

## Por qué no se puede concluir

1. **Hay al menos dos intervenciones grandes al mismo tiempo**
   - Publicidad pagada desde el 3 de marzo ($400).
   - Mención de un creador grande el 12 de marzo.
   Cualquiera de esas dos cosas —o ambas— puede explicar el aumento de MRR y de altas.

2. **El aumento del MRR no prueba que los emails hayan convertido usuarios gratuitos**
   - El MRR subió de $4.100 a $5.300 (+29%), pero ese crecimiento puede venir de nuevos usuarios que llegaron por publicidad o por la mención, no necesariamente de gente del plan gratuito que recibió los emails.

3. **Las “altas al plan pago” apenas subieron de 9 a 14**
   - Es una diferencia de solo 5 personas. En muestras tan pequeñas es muy difícil descartar el azar.

4. **No sabemos si los usuarios que pagaron en marzo estaban en la lista de emails gratuitos**
   - Puede que muchas de las 14 altas fueran personas nuevas que nunca estuvieron en el plan gratuito.

5. **No hay grupo de control**
   - Sin un grupo de usuarios gratuitos que no recibiera los emails, comparar es adivinar.

## Qué haría falta para estar seguros

Para medir el impacto real de la secuencia de emails, necesitarías algo como esto:

- **Grupo de control (A/B test):** usuarios del plan gratuito divididos aleatoriamente en dos grupos:
  - Grupo A: recibe los 5 emails.
  - Grupo B: no recibe los emails.
  Luego comparar cuántos de cada grupo pasan al plan pago.

- **Cohorte centrada en usuarios gratuitos existentes:** medir solo conversiones de personas que ya eran usuarias gratuitas antes del 1 de marzo, no incluir a usuarios nuevos que llegaron después.

- **Atribución clara:** preguntar en el checkout o rastrear el origen de cada alta:
  - ¿Llegó por publicidad?
  - ¿Llegó por la mención del creador?
  - ¿Abrió/clickó alguno de los 5 emails antes de pagar?

- **Período más largo o más volumen:** con 9 vs 14 altas, cualquier conclusión será frágil. Necesitas más conversiones para tener confianza estadística.

- **Aislar variables:** lo ideal hubiera sido lanzar los emails en un mes sin publicidad pagada ni menciones grandes, o viceversa.

## Conclusión práctica

**No digas que la secuencia de emails funcionó solo porque MRR y altas subieron.** Pudo haber funcionado, pudo no haber hecho nada, o incluso pudo haber funcionado peor que la publicidad y la mención del creador. Los datos actuales no permiten separar esos efectos.

Si quieres, pásame datos más detallados —por ejemplo, cuántos de esos 14 pagadores estaban en el plan gratuito antes del 1 de marzo, cuántos abrieron los emails, y de dónde venían— y podemos hacer un análisis más certero.