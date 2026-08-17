# Claude Sonnet 5 (suscripción) — business_audit/atribucion_correlacion_temporal

- model_id: `claude-sonnet-5`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 28.52s | tokens_per_second: 46.5
- input_tokens: 2 | output_tokens: 1325

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

# Corto: no se puede saber con estos datos

Con lo que tienes, no hay forma de aislar el efecto de la secuencia de emails. Y te lo digo así de directo porque la tentación natural acá es agarrar el +29% de MRR y atribuírselo a los emails, y eso sería una conclusión que los datos no sostienen.

## Por qué no se puede saber

En marzo activaste **tres cosas distintas casi al mismo tiempo**:

| Fecha | Evento |
|---|---|
| 1 marzo | Secuencia de 5 emails (free → paid) |
| 3 marzo | Empezaste a pagar ads ($400) |
| 12 marzo | Mención de un creador con audiencia grande |

Las 14 altas de marzo (vs. 9 en febrero) pueden venir de cualquier combinación de las tres — o de ninguna en particular, si marzo tenía estacionalidad propia. No tienes manera de separar "esta alta vino del email 3 de la secuencia" de "esta alta vino porque vio el video del creador y se registró gratis, y de casualidad le llegó un email esa semana".

Además, ojo con esto: **9 → 14 altas es una muestra chica.** Con volúmenes así, la diferencia entre "funcionó" y "ruido normal mes a mes" puede ser perfectamente ese rango. No es una tendencia robusta, es un mes.

Y el MRR total (+29%) mezcla altas nuevas con lo que ya tenías — no aísla si ese crecimiento es directamente atribuible a la secuencia sin saber cuánto de esos $1.200 extra vino de upgrades de gente que ya estaba, no de conversión free→paid.

## Qué haría falta para saber de verdad

1. **Separar por fuente/cohorte.** De las 14 altas de marzo: ¿cuántas eran usuarios free que recibieron la secuencia completa vs. gente nueva que llegó por el creador o por ads y nunca vio los 5 emails? Sin esto no hay atribución posible.

2. **Grupo de control o al menos un "antes" más largo.** Comparar solo feb vs. marzo es un solo punto de datos. Necesitas ver la tendencia de altas de al menos 3-4 meses previos para saber si 9→14 es un salto real o variación normal.

3. **Trackear clics/aperturas de la secuencia y cruzarlos con conversión.** Si tienes esos datos: ¿de los que abrieron/clickearon el email 3, cuántos convirtieron vs. los que no interactuaron con la secuencia? Eso sí empieza a dar señal causal.

4. **Idealmente, un A/B.** Mitad de los free reciben la secuencia, mitad no, mismo mes, mismas condiciones externas. Es la única forma limpia de aislar el efecto sin que ads o menciones externas contaminen el resultado.

5. **Separar el efecto del creador.** Un pico de tráfico del 12 de marzo probablemente tiene una ventana de conversión visible en tus altas de los días siguientes. Si tienes fecha de registro por usuario, mira si hay un cluster de altas pegado al 12-15 de marzo — eso te dice cuánto "roba" esa mención al resto de la historia.

## Mi recomendación concreta

No declares la secuencia "exitosa" ni la "descartes" todavía. Lo que sí puedes decir hoy, honestamente: *"marzo fue mejor que febrero, pero no sabemos por qué."* Si quieres saber si vale la pena seguir invirtiendo tiempo en la secuencia, el próximo mes corta las otras dos variables (pausa ads, no hay mención esperada) y mide un mes "limpio" solo con la secuencia corriendo. Ahí sí vas a tener una lectura que puedas defender.