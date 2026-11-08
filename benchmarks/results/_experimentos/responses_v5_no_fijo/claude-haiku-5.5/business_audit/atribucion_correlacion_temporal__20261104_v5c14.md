# Claude Haiku 5.5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.05 | quality: 10.0
- latency_total: 10.412s | tokens_per_second: 164.9
- input_tokens: 366 | output_tokens: 1717

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

**Conclusión: con estos datos no se puede saber si la secuencia de emails funcionó.** Hay demasiadas cosas que cambiaron al mismo tiempo, y los números son pequeños.

**Por qué no se puede atribuir el crecimiento a los emails**

- **Tres cambios simultáneos.** Los emails empezaron el 1 de marzo, la publicidad el 3 y el creador mencionó la comunidad el 12. Los tres pueden explicar el aumento, y el video del creador es el candidato más fuerte por el alcance que suele tener una mención así.
- **No hay grupo de control.** Sin un grupo comparable que no recibió los emails, no sabes qué habría pasado sin ellos.
- **Muestra pequeña.** 9 frente a 14 altas es una diferencia de 5 personas. Con números tan bajos, esa diferencia puede ser ruido. Si repitieras el mes de febrero, podrías ver 14 altas sin ningún cambio real.
- **El MRR no es solo altas.** El +$1.200 mezcla nuevas altas, cancelaciones, cambios de precio o de plan y posibles pagos anuales. Con 5 altas adicionales no sabemos cuánto de ese aumento viene de ellas.
- **Desfase temporal.** Una secuencia de 5 emails puede tardar semanas en mostrar su efecto completo, así que marzo puede no reflejar todo lo que causaron.

**Qué haría falta para estar seguros**

1. **Un grupo de control aleatorio.** Divide a los usuarios gratuitos en dos grupos al azar: uno recibe la secuencia y el otro no. Esta es la única forma limpia de aislar el efecto de los emails. Si no quieres dejar a nadie fuera, puedes comparar grupos con distinto ritmo de activación.
2. **Atribución por origen.** Separa las altas por canal (anuncio, mención del creador, orgánico, email) usando UTMs, códigos de referido o una pregunta en el registro. Así verás qué parte viene de cada fuente.
3. **Comparar con una línea base.** Revisa la tasa de conversión free→pago de enero, febrero y marzo, y de meses anteriores sin campañas. Si la tasa mensual típica es de 2 a 3 %, cambios de 9 a 14 altas pueden quedar dentro de lo normal.
4. **Seguir la cohorte de email.** Mide cuántos de los usuarios que recibieron la secuencia abrieron, hicieron clic y se convirtieron, comparado con los que no abrieron. Ojo: quien abre emails ya está más interesado, así que esta comparación también tiene sesgo.
5. **Esperar más datos.** Revisa abril y mayo, cuando el efecto de la mención del creador ya se haya diluido y los emails tengan más tiempo para actuar.
6. **Calcular el tamaño de muestra.** Antes de concluir, define cuántas conversiones necesitas para detectar un cambio que te importe (por ejemplo, +30 %). Con 9 a 14 altas por mes, probablemente necesites varios meses o un experimento más grande.

**Mi recomendación práctica:** no tomes decisiones grandes (como escalar o descartar la secuencia) con este mes. Lo más útil ahora es implementar el grupo de control para la secuencia, o al menos etiquetar el origen de cada alta a partir de hoy. Así en dos o tres meses tendrás una respuesta que sí se pueda defender.