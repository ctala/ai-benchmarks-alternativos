# Muse Spark 1.3 — business_audit/atribucion_correlacion_temporal

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 22.682s | tokens_per_second: 102.7
- input_tokens: 236 | output_tokens: 2330

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

Con estos datos, mi conclusión es: **no se puede saber si la secuencia funcionó.**

Y es importante que no le digamos al equipo que sí funcionó, porque los números que pasas no lo sostienen.

Te explico por qué:

**1. No tienes comparador.**
Pasaste de 9 altas en febrero a 14 en marzo, y el MRR de $4.100 a $5.300. Eso es un antes-después.

El problema es que un antes-después no responde a la pregunta clave: ¿qué hubiera pasado en marzo *sin* los emails? Sin ese contrafactual, cualquier subida parece un éxito.

Además, con números tan pequeños, pasar de 9 a 14 pueden ser solo 5 personas de diferencia. Eso entra perfectamente en fluctuación normal de mes a mes. No sabemos cuál es tu variabilidad habitual porque no tenemos enero, diciembre, etc. Y ojo: febrero tiene 28 días y marzo 31, o sea que marzo tuvo 11% más días para captar altas.

**2. Tienes dos confusores enormes en el mismo mes.**
- 3 de marzo: empiezas publicidad de pago
- 12 de marzo: un creador grande te menciona

Ambos ocurrieron *después* de activar los emails y *antes* de medir el resultado. Es imposible separar con el total mensual qué altas vinieron por emails, cuáles por ads y cuáles por el video.

Decir que fue por los emails es elegir tu explicación favorita entre tres posibles.

**3. Estás mirando métricas agregadas.**
MRR y altas totales no te dicen nada del mecanismo:
- No sabemos cuántos gratuitos recibieron los 5 emails, cuántos los abrieron, cuántos clickearon y cuántos de esos 14 se convirtieron.
- No sabemos si el aumento de MRR viene de nuevos clientes, de menos cancelaciones en marzo, de upgrades, o de planes anuales.

Sin trazabilidad a nivel de usuario, no puedes conectar emails -> conversión.

### Qué haría falta para estar seguros

No necesitas un experimento perfecto y caro, pero sí esto mínimo:

1. **Grupo control aleatorio.** Para la próxima tanda de usuarios gratuitos: 50% recibe la secuencia, 50% no la recibe. Mides altas a pago en el mismo periodo. Todo lo demás (ads, menciones) les afecta a ambos por igual.

2. **Definir la métrica antes.** Ej: "% de usuarios gratuitos que pasan a pago en 30 días desde que entran a la secuencia". No MRR total, que se mueve por mil cosas.

3. **Atribución por usuario.** Marcar en tu base: recibió email sí/no, abrió/clickeó, fecha de alta, fuente de llegada (UTM de ads, referral del video). Sin eso, seguimos a ciegas.

4. **Aislar el efecto.** Si no puedes hacer A/B, al menos mira la cohorte: de esos 14 de marzo, ¿cuántos habían recibido los emails? ¿cuántos llegaron por ads? ¿cuántos llegaron el 12-15 de marzo justo después del video?

Si quieres, pásame eso si lo tienes:
- enviados / abiertos / clics de la secuencia
- de las 14 altas de marzo, fecha de alta y cómo llegaron
- altas de los meses anteriores para ver variabilidad

Con eso te puedo decir si hay *alguna señal* a favor de los emails, pero con lo que tenemos hoy, lo honesto es decirle al equipo: funcionó el mes, no sabemos por qué.