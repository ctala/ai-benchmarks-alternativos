# Claude Opus 5.5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 22.962s | tokens_per_second: 90.3
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

El crecimiento es real (+$1.200 de MRR y 5 altas más que en febrero), pero **no hay forma de atribuirlo a los emails** con la información actual. Que la secuencia haya funcionado es posible, pero no está demostrado.

## Por qué no se puede concluir

**1. Tres cambios en el mismo mes.** En marzo actuaron a la vez:
- La secuencia de emails (1 de marzo)
- La publicidad pagada (3 de marzo)
- La mención del creador (12 de marzo)

Los tres podrían explicar el aumento, total o parcialmente. Con solo dos totales mensuales (febrero y marzo) es imposible separar sus efectos. La mención de un creador grande suele generar picos fuertes, así que es un candidato serio a explicar buena parte del crecimiento.

**2. La diferencia puede ser ruido.** Con números tan chicos, pasar de 9 a 14 altas no es estadísticamente distinguible de la variación normal entre meses. Como referencia aproximada: si tu tasa real fuera de unas 11 o 12 altas por mes, ver 9 un mes y 14 al siguiente sería bastante habitual. Antes de pensar en causas, ni siquiera está claro que la tasa de conversión haya cambiado.

**3. El MRR mezcla varias cosas.** Los +$1.200 son un neto: altas nuevas menos cancelaciones, más o menos cambios de plan. Si en marzo hubo menos bajas de lo habitual, eso también infla el número, y no tiene nada que ver con los emails.

## Qué puedes revisar ya, con datos que probablemente tienes

Esto puede darte una respuesta parcial hoy mismo:

| Pregunta | Qué indicaría |
|---|---|
| De las 14 altas, ¿cuántas eran usuarios gratuitos **registrados antes del 1 de marzo**? | Solo esas personas pudieron recibir la secuencia. Si la mayoría de las altas son usuarios nuevos que llegaron y pagaron directamente, los emails no explican el crecimiento. |
| ¿Esos usuarios abrieron o hicieron clic en algún email antes de pagar? | Si nadie hizo clic, la atribución a los emails es débil. Si pagaron horas después de un clic, es evidencia a favor (aunque no prueba). |
| ¿Cómo se reparten las altas día a día? | Un pico después del 12 de marzo apunta al video. Altas repartidas entre el día 1 y el 11 apuntan más a emails o publicidad. |
| ¿Los enlaces tienen UTM? ¿Qué dice el referrer o la fuente de registro? | Te permite separar el tráfico de la publicidad, del video y de los emails. |
| ¿Cuál es la tasa de conversión de gratuito a pago de los usuarios antiguos, en febrero frente a marzo? | Es la métrica correcta para evaluar la secuencia, no el MRR total. |
| ¿Cuántas cancelaciones hubo en febrero y en marzo? | Para entender qué parte del MRR viene de altas y qué parte de retención. |

## Qué haría falta para estar seguros

**Un grupo de control.** Es la única forma limpia de medirlo:
- A partir de ahora, envía la secuencia a una parte aleatoria de los nuevos usuarios gratuitos (por ejemplo, 50%) y deja al resto sin ella.
- Compara la tasa de conversión a pago entre ambos grupos durante 30 a 60 días.
- Como ambos grupos están expuestos por igual a la publicidad y a cualquier mención, la diferencia sí se puede atribuir a los emails.

**Aviso sobre el volumen:** con pocas decenas de conversiones al mes, el experimento necesitará varios meses, o bastantes usuarios gratuitos, para detectar un efecto que no sea enorme. Si tu base gratuita es pequeña, es mejor saberlo de antemano que sacar conclusiones de un resultado de 7 contra 5.

## Resumen para el equipo

> "Marzo creció, pero coincidieron tres acciones y los números son demasiado chicos para separar sus efectos. No sabemos si la secuencia funcionó. Vamos a revisar de dónde vinieron las 14 altas y, a partir de ahora, medir la secuencia con un grupo de control."

Si me pasas el detalle de las 14 altas (fecha de registro, fecha de pago y si interactuaron con los emails), puedo decirte bastante más.