# Claude Opus 5 — business_audit/atribucion_correlacion_temporal

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 5.3 | quality: 6.0
- latency_total: 33.673s | tokens_per_second: 60.8
- input_tokens: 364 | output_tokens: 2048

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

## Conclusión corta

**No se puede saber.** Con estos datos no hay forma de separar el efecto de la secuencia de emails del de los $400 de publicidad y de la mención del creador. Los tres empezaron en la misma ventana de 12 días. Cualquier número que te dé de "la secuencia aportó X" sería inventado.

Y hay un segundo problema, más incómodo: **incluso si la secuencia hubiera sido la única cosa que cambió, 9 → 14 altas no alcanza para concluir que algo funcionó.**

## Por qué el "+56% de altas" es más débil de lo que parece

- **Febrero tiene 28 días, marzo 31.** En tasa diaria es 0,32 → 0,45 altas/día, o sea +41%, no +56%.
- **Con números tan chicos, la variación aleatoria explica esto sin problema.** Si tu tasa real fuera constante en 9 altas/mes, ver 14 o más en un mes cualquiera pasa aproximadamente 1 de cada 13 o 14 meses solo por azar. No es raro. No tenés un mes anterior con 14 solo porque no me mostraste los meses anteriores — ¿los tenés?
- **Un solo mes de comparación no es una línea base.** Necesito 6–12 meses para saber si 9 era un mes flojo, si venías creciendo igual desde antes, y si hay estacionalidad (enero/febrero suelen ser distintos).

## Por qué el MRR tampoco ayuda

+$1.200 con 14 altas implica ~$86 por alta. Eso no cuadra con casi ningún plan de comunidad mensual, así que hay algo más ahí: planes anuales contados como MRR, upgrades de usuarios existentes, un cambio de precio, o churn muy bajo. **El MRR es una cifra neta** (altas − bajas − downgrades + expansión) y me la estás dando sin sus componentes. Ahora mismo el +29% podría ser en buena parte una venta anual grande, y no tendría nada que ver con la secuencia.

Antes de discutir atribución, necesito el MRR descompuesto: nuevo, expansión, contracción, churn.

## Lo que haría falta para tener una respuesta

**Nivel 1 — lo que probablemente ya tenés y respondería mucho (esta semana):**

1. **Origen de cada una de las 14 altas.** ¿Cuántas venían de UTMs de publicidad? ¿Cuántas se registraron entre el 12 y el 20 de marzo (ventana del creador)?
2. **La pregunta clave: ¿cuántos de los 14 eran us