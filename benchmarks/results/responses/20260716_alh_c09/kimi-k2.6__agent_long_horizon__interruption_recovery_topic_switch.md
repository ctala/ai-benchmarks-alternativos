# Kimi K2.6 — agent_long_horizon/interruption_recovery_topic_switch

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 7.47 | quality: 9.0
- latency_total: 234.652s | tokens_per_second: 122.3
- input_tokens: 21481 | output_tokens: 18260

## Respuesta completa

El usuario quiere retomar el hilo principal: el plan de lanzamiento. Específicamente pide:
1. La tabla completa con los hitos de las 4 semanas previas (la que armamos al principio).
2. Agregar el detalle día por día de la semana 4 (la semana -1, la más cercana al lanzamiento, que ya habíamos detallado).
3. Agregar también el detalle de la semana 3 (la semana -2 en mi numeración anterior, la de calentamiento y lista de espera).

Necesito reconstruir y unificar todo en una tabla o estructura clara. El usuario pide "la tabla completa", pero las semanas 1 y 2 (semanas -4 y -3) no las tengo desglosadas día por día, solo por hitos semanales. La semana -2 (que el usuario llama "semana 3" probablemente, ya que semana 4 es la última) tampoco la había desglosado día por día aún. Pero el usuario pide "agregar también el detalle de la semana 3". Espera, revisemos:

En la conversación:
- Primera respuesta: 4 semanas previas. Semana -4 (14-20 abril), Semana -3 (21-27 abril), Semana -2 (28 abr-4 may), Semana -1 (5-13 may).
- Segunda respuesta: el usuario pidió detallar la semana 4 (más cercana al lanzamiento). Yo detallé semana -1 (del 8 al 14 si 15 es lunes).
- Ahora el usuario pide: "la tabla completa con los hitos de las 4 semanas que armamos al principio, ahora con las tareas día por día de la semana 4 que ya empezaste, y agregar también el detalle de la semana 3".

Interpretación:
- "Semana 4": la última semana (semana -1, del 8 al 14 de mayo aprox, que ya detallé día por día).
- "Semana 3": la antepenúltima semana? No, espera. Contando hacia atrás desde el lanzamiento:
  - Semana 4 (previa): es la semana -1 (más cercana). Ya la tengo.
  - Semana 3 (previa): sería la semana -2 (del 28 abr al 4 may). El usuario pide detalle de esta semana también.
  
Pero el usuario dice "agregar también el detalle de la semana 3". Eso implica que quiere el desglose día por día de la semana -2 (la de aceleración y prueba social / pre-venta).

Sin embargo, debo verificar si tengo sentido. El usuario dice: "la tabla completa con los hitos de las 4 semanas que armamos al principio". Es decir, quiere una vista unificada. Pero solo semana 4 y semana 3 con detalle día por día. Las semanas 1 y 2 pueden quedar en formato semanal (hitos clave) como al principio, o puedo intentar dar un híbrido. Lo más práctico es:

- Presentar las 4 semanas en formato tabla o estructura clara.
- Semanas -4 y -3: resumen de hitos semanales (como al principio).
- Semana -2 (que el usuario llama semana 3): detalle día por día (nuevo).
- Semana -1 (que el usuario llama semana 4): detalle día por día (ya existente).

Pero espera, la semana -3 (21-27 abril) era "Calentamiento y Lista de Espera". El usuario pide "detalle de la semana 3". Si contamos:
- Semana 1: -4 (14-20 abr)
- Semana 2: -3 (21-27 abr)
- Semana 3: -2 (28 abr-4 may)
- Semana 4: -1 (5-13 may)

Sí, semana 3 es la -2. Necesito inventar el día a día de la semana -2 basándome en la estrategia que ya había definido (Aceleración y Prueba Social / Preventa).

Veamos la semana -2 (28 abril - 4 mayo):
Objetivo: generar evento, demostrar autoridad y abrir la preventa.
Hitos que ya había puesto:
- Masterclass/Webinar
- Prueba social (testimonios, BTS)
- Secuencia de lanzamiento (emails cada 48h)
- Redes: backstage, FAQs, encuestas
- Ventas: early bird para asistentes, seguimiento

Necesito convertir esto en 7 días. Asumamos que el 15 es lunes, entonces:
- Semana -2: Lunes 28 abril al Domingo 4 mayo.
- Semana -1: Lunes 5 al Domingo 12 (espera, antes puse 5-13, pero si 15 es lunes, entonces -1 es 8-14. Corrijo: si 15 es lunes, las semanas son:
  - -4: 14-20 abr (lunes-domingo)
  - -3: 21-27 abr (lunes-domingo)
  - -2: 28 abr - 4 may (lunes-domingo)
  - -1: 5-11 may? No, 15 es lunes, entonces 7 días antes sería lunes 8. Pero la primera respuesta puse 5-13. Eso fue un error de cálculo o asumiendo que 15 podría ser miércoles. Mejor no atarme a fechas exactas de día de la semana, sino usar "Día -14", "Día -13", etc. o directamente fechas relativas.

El usuario no especificó en qué día de la semana cae el 15 de mayo. En 2024, 15 de mayo es miércoles. En 2025, 15 de mayo es jueves. No importa el año, el usuario dijo "Lanzo el 15 de mayo". Debería mantener las fechas relativas o las fechas exactas asumiendo un año? Mejor usar las fechas exactas basadas en el calendario real. Veamos: si hoy es 2024? No importa. Puedo usar las fechas que ya usé al principio y ajustar.

Al principio usé:
- Semana -4: 14-20 de abril
- Semana -3: 21-27 de abril
- Semana -2: 28 abril - 4 mayo
- Semana -1: 5-13 de mayo

Eso asumiría que el 15 es miércoles (porque 5-13 son 9 días? No, 5 al 13 es raro. 5,6,7,8,9,10,11,12,13 = 9 días. Eso no es una semana. Claramente usé "5-13" como aproximación o porque conté mal. Mejor corregir a semanas exactas de 7 días.

Si 15 de mayo es el lanzamiento:
- Semana -1: 8 al 14 de mayo (7 días).
- Semana -2: 1 al 7 de mayo? No, 8-14 es semana -1, entonces 1-7 sería semana -2? Pero antes puse 28 abr - 4 may. Eso sería si 15 es miércoles:
  - Mié 15
  - Semana -1: Jue 9? No, para que sea 7 días: Mié 8 al Martes 14. O Lun 6 al Dom 12? Depende.

Para evitar confusiones, usaré las fechas exactas que ya establecí en la primera respuesta, aunque no sean 7 días perfectos, o mejor aún, usaré el formato "Semana -4", "Semana -3", etc., con las fechas aproximadas que ya di, y aclarar que son ajustables.

Pero el usuario pide una tabla. Puedo hacer una tabla larga o una estructura por semanas. Una tabla con 4 filas (semanas) y columnas: Semana, Fechas, Hitos/Diario. Pero si semana 3 y 4 son día por día, no caben bien en celdas pequeñas. Mejor hacer una tabla para las semanas 1-2 con hitos semanales, y luego secciones detalladas para semana 3 y 4, o una tabla mixta donde las celdas de semana 3 y 4 tengan listas día por día.

Voy a optar por:
1. Una tabla resumen de las 4 semanas con fechas y objetivo general.
2. Debajo, el detalle día por día de la Semana 3 (semana -2: 28 abr - 4 may) que debo crear.
3. Debajo, el detalle día por día de la Semana 4 (semana -1: 5-13 may? No, usaré las fechas correctas: si 15 es lanzamiento, y semana -1 es la inmediata anterior, usaré 8-14 de mayo como los 7 días previos. Sin embargo, en mi respuesta anterior usé 8-14 asumiendo que 15 era lunes. Pero el usuario no corrigió. Voy a mantener el desglose relativo (Día -7 a Día -1) y asignar fechas flexibles, o simplemente poner las fechas que fluyan de la primera respuesta. 

Espera, la primera respuesta usé:
- Semana -4: 14-20 abril
- Semana -3: 21-27 abril
- Semana -2: 28 abril - 4 mayo
- Semana -1: 5-13 mayo (esto es 9 días, está mal). 

Debería corregirlo sutilmente o usar el formato Día -7, etc. Sin embargo, el usuario pidió específicamente "la tabla completa con los hitos de las 4 semanas que armamos al principio". Así que debo mantener los hitos semanales de las 4 semanas como los definí inicialmente, pero ajustando las fechas de la semana -1 para que sean 7 días exactos antes del 15.

Si 15 de mayo es el lanzamiento, y quiero 4 semanas previas exactas:
- Semana -4: 17-23 de abril? No, 15 menos 28 días = 17 de abril. Pero al principio puse 14-20. No importa tanto la fecha exacta del inicio de la semana, lo importante es la secuencia. Pero para ser consistente, usaré:
  - Semana -4: 14-20 de abril (hitos semanales)
  - Semana -3: 21-27 de abril (hitos semanales)
  - Semana -2: 28 abril - 4 de mayo (Ahora desglosada día por día)
  - Semana -1: 5-11 de mayo (Ahora desglosada día por día, 7 días exactos)

Pero en mi respuesta anterior de semana -1 usé 8-14. Eso fue inconsistente. Voy a usar 8-14 para semana -1 si asumo que 15 es miércoles (15 mayo 2024 es miércoles). Entonces:
- Miércoles 15 mayo: lanzamiento.
- Semana -1: Miércoles 8 al Martes 14 de mayo.
- Semana -2: Miércoles 1 al Martes 7 de mayo.
- Semana -3: Miércoles 24 al Martes 30 de abril.
- Semana -4: Miércoles 17 al Martes 23 de abril.

Pero al principio puse:
- -4: 14-20 abril (domingo a sábado? o lunes a domingo?)
- -3: 21-27 abril
- -2: 28 abr - 4 mayo
- -1: 5-13 mayo

Si quiero mantenerme fiel a lo que ya dije al principio, debería respetar esas fechas aproximadas y solo ajustar la semana -1 a 7 días exactos: 8-14 de mayo en lugar de 5-13. O simplemente presentar las semanas como bloques de 7 días terminando el 14 de mayo.

Creo que lo mejor es presentar la tabla con las fechas ajustadas para que sean coherentes, y no me preocupo por la primera respuesta porque el usuario quiere la tabla completa ahora. Puedo poner una nota diciendo "fechas ajustadas a calendario exacto".

Veamos el calendario 2025 (asumiendo que estamos planeando para el futuro cercano):
- 15 mayo 2025 = jueves.
Entonces:
- Semana -1: Jueves 8 al Miércoles 14 de mayo.
- Semana -2: Jueves 1 al Miércoles 7 de mayo.
- Semana -3: Jueves 24 abril al Miércoles 30 abril.
- Semana -4: Jueves 17 al Miércoles 23 abril.

En 2024:
- 15 mayo = miércoles.
- Semana -1: Mié 8 al Martes 14.

Como no sé el año, usaré fechas relativas o aproximadas pero consistentes. O simplemente usaré las fechas que puse al principio para las 4 semanas y aclararé. Pero el usuario no va a preocuparse por un desfase de 1-2 días. Lo importante es la secuencia lógica.

Estructura de la respuesta:

**Tabla resumen de las 4 semanas previas al 15 de mayo**

| Semana | Fechas | Objetivo | Hito clave / Entregable |
|---|---|---|---|
| Semana -4 (Cimientos) | 14-20 abr | Producto, oferta y máquina lista | Curso estructurado, página de espera, copy base, checkout probado |
| Semana -3 (Calentamiento) | 21-27 abr | Calificar interés y lista de espera | Masterclass anunciada, emails de valor, contenido diario |
| Semana -2 (Aceleración) | 28 abr - 4 may | Evento, autoridad y early bird | Webinar, prueba social, preventa, emails cada 48h |
| Semana -1 (Pre-apertura) | 8-14 may* | Urgencia, objeciones y apertura técnica | Bonus fast-action, demo de valor, testeo final, cuenta regresiva |

*Ajusté la semana -1 a los 7 días exactos previos.

Luego, detalle día por día de la Semana -2 (28 abr - 4 may):

Día -14 (Lunes 28/04): Anuncio del evento + primer email de secuencia
Día -13 (Martes 29/04): Contenido de autoridad + invitación directa a la masterclass
Día -12 (Miércoles 30/04): Prueba social temprana + FAQ en historias
Día -11 (Jueves 01/05): Masterclass/Webinar gratuito + early bird al final
Día -10 (Viernes 02/05): Seguimiento a asistentes + post de "lo que aprendimos ayer"
Día -9 (Sábado 03/05): Descanso estratégico / Contenido humano + respuesta a DMs
Día -8 (Domingo 04/05): Cierre de early bird + transición a "faltan 7 días"

Espera, necesito que sea coherente con lo que ya dije en la primera respuesta para semana -2:
- Masterclass/Webinar: ejecutar el evento gratuito de calentamiento.
- Prueba social: publicar testimonios.
- Secuencia de lanzamiento: activar emails cada 48h.
- Redes: backstage, FAQs, encuestas.
- Ventas: early bird exclusivo para asistentes.

Así que el desglose podría ser:

**Semana -2 (28 abril – 4 mayo): Aceleración y Prueba Social**

- **Lunes (Día -14):** Email a lista anunciando la masterclass gratuita del jueves. Tema: "Te enseño el sistema en vivo". Post en redes con CTA a registro.
- **Martes (Día -13):** Contenido de autoridad: "El error #1 de productividad que cometen los emprendedores". Historias con encuesta: "¿Cuál es tu mayor distracción?"
- **Miércoles (Día -12):** Último recordatorio de masterclass. Email con mini-lección (video o texto) y link de registro. Prueba social: testimonio o screenshot de resultados previos.
- **Jueves (Día -11):** **MASTERCLASS/WEBINAR**. Ejecutar el evento en vivo. Al final, ofrecer el curso en early bird (precio especial o bonus extra) por 48h.
- **Viernes (Día -10):** Email de seguimiento solo para asistentes: link de compra early bird + bonus. Post en redes: "Ayer en la masterclass hablamos de X". Responder dudas en DMs intensivamente.
- **Sábado (Día -9):** Contenido humano / Behind the scenes del curso. Último día del early bird. Historias recordando que cierra la oferta especial a la medianoche.
- **Domingo (Día -8):** Cierre de early bird. Email a toda la lista: "Se cerró el precio especial, pero el 15 abro oficialmente". Contenido en redes: cuenta regresiva de 7 días.

Esto funciona bien. Ahora, para la Semana -1, ya tengo el detalle anterior. Lo reproduciré con las fechas ajustadas (8-14 mayo si 15 es miércoles/jueves, pero usaré fechas relativas o exactas según convenga). En mi respuesta anterior usé "Día -7 al Día -1". Puedo mantener ese formato o usar fechas. Como el usuario pidió "la tabla completa", quizás sea mejor usar fechas exactas coherentes.

Asumiendo que 15 de mayo es el lanzamiento (miércoles en 2024, jueves en 2025), usaré el formato Día -X y las fechas genéricas o exactas del calendario 2025. Pero para no complicar, usaré las fechas como: "8 al 14 de mayo (ajustá según el día de la semana)". O simplemente usaré el desglose Día -7 a Día -1 que ya está perfecto.

Voy a presentar:

1. Tabla resumen de 4 semanas (columnas: Etapa, Fechas, Objetivo, Hito Central).
2. Debajo, bloque detallado: **Semana -2 (28 abr – 4 may): Día por día**.
3. Debajo, bloque detallado: **Semana -1 (8 – 14 may): Día por día** (reproduciendo lo ya dicho).

Debo asegurarme de no perder el hilo de la conversación y no agregar información de Notion/Obsidian/SEO. El usuario quiere retomar el plan.

Veamos si necesito ajustar algo de la semana -1. En mi respuesta previa, la semana -1 tenía:
- Día -7: Testeo + Autoridad
- Día -6: Objeción #1 (Tiempo)
- Día -5: Demo de Valor
- Día -4: Escasez y Urgencia
- Día -3: Prueba Social Máxima
- Día -2: Descanso Estratégico
- Día -1: Último Recordatorio

Esto está perfecto. Lo mantengo.

Ahora, para la tabla, necesito que sea legible. Si pongo el detalle día por día dentro de la tabla, las celdas serán enormes. Mejor la tabla resumen para las 4 semanas, y luego fuera de la tabla los desgloses.

O hacer una tabla de 4 filas donde la última columna sea "Plan detallado" y para semanas 3 y 4 ponga "Ver desglose abajo". Pero el usuario pidió explícitamente la tabla completa con las tareas día por día de la semana 4 y agregar el detalle de la semana 3. Podría interpretarse que quiere todo en la tabla. Sin embargo, una tabla con celdas enormes es ilegible. Optaré por:

- Tabla resumen de 4 semanas (formato compacto, fiel a la primera respuesta).
- Desglose día por día de Semana -2 (Semana 3).
- Desglose día por día de Semana -1 (Semana 4).

Y aclarar que las semanas -4 y -3 permanecen en hitos semanales como se acordó al principio, ya que el usuario solo pidió el detalle de la semana 3 y 4.

Espera, la frase: "¿Puedes darme la tabla completa con los hitos de las 4 semanas que armamos al principio, ahora con las tareas día por día de la semana 4 que ya empezaste, y agregar también el detalle de la semana 3?"

Esto significa:
- Tabla completa con hitos de 4 semanas (como al principio).
- PERO ahora con las tareas día por día de la semana 4 (incorporadas).
- Y agregar el detalle de la semana 3.

Podría ser una tabla grande donde:
- Fila Semana -4: hitos semanales.
- Fila Semana -3: hitos semanales.
- Fila Semana -2: desglose día por día.
- Fila Semana -1: desglose día por día.

Si formateo bien con saltos de línea y viñetas dentro de las celdas, se puede leer. Markdown permite listas dentro de tablas usando `<br>` o simplemente saltos de línea si el renderizado lo permite. Aunque en algunos renderizadores de Markdown las tablas no permiten saltos de línea fáciles, se pueden usar `<br>` HTML.

Voy a intentar hacer una tabla única. Estructura:

| Semana | Fechas | Objetivo | Tareas / Hitos |
|---|---|---|---|
| **Semana -4** Cimientos | 14 – 20 abr | Producto, oferta y máquina lista | • Producto: Módulo 1 listo y estructura definida<br>• Oferta: Precio, bonuses, garantía<br>• Técnica: Página de espera, checkout, plataforma<br>• Copy: Borrador de 5 emails + 10 piezas redes<br>• Audiencia: Contenido de valor puro (sin vender) |
| **Semana -3** Calentamiento | 21 – 27 abr | Calificar interés y lista de espera | • Email + post anunciando lanzamiento 15/05 y lista de espera<br>• Contenido diario (1 pieza/día) productividad = resultados<br>• 2-3 emails de valor educando el problema<br>• Anunciar masterclass gratuita para la semana que viene<br>• DMs activos detectando objeciones |
| **Semana -2** Aceleración | 28 abr – 4 may | Evento, autoridad y early bird | **Lun 28:** Email + post anunciando masterclass del jueves<br>**Mar 29:** Contenido autoridad + encuesta en historias<br>**Mié 30:** Último recordatorio masterclass + prueba social<br>**Jue 1:** MASTERCLASS EN VIVO + oferta early bird exclusiva<br>**Vie 2:** Seguimiento asistentes + post de valor + responder DMs<br>**Sáb 3:** Behind the scenes + cierre early bird (últimas horas)<br>**Dom 4:** Email "Se cerró early bird" + cuenta regresiva oficial al 15 |
| **Semana -1** Pre-apertura | 8 – 14 may | Urgencia, objeciones y apertura técnica | **Lun 8 (D-7):** Testeo de compra real + email caso de estudio + tour del curso en redes<br>**Mar 9 (D-6):** Email objeción tiempo + historias FAQ + post error común<br>**Mié 10 (D-5):** Email mini-lección gratis + redes antes/después + bonus visible<br>**Jue 11 (D-4):** Email bonus fast-action + post precio vs valor + encuesta lista<br>**Vie 12 (D-3):** Email testimonio con cifras + screenshots reales + countdown "7 días"<br>**Sáb 13 (D-2):** Descanso estratégico + revisión técnica final + plantillas respuesta<br>**Dom 14 (D-1):** Email corto recordatorio + post checklist + serie historias (7) + programar apertura |

Necesito verificar que las fechas de la semana -1 sean coherentes con las de la semana -2. Si semana -2 termina el 4 de mayo (domingo), semana -1 debería empezar el 5 de mayo (lunes) y terminar el 11 (domingo). Pero entonces el lanzamiento sería el lunes 12, no el 15. Aquí está el problema.

Veamos: 4 semanas exactas antes del 15 de mayo:
- 15 mayo menos 7 días = 8 mayo.
- Entonces semana -1: 8 al 14 de mayo (termina un día antes del 15).
- Semana -2: 1 al 7 de mayo.
- Semana -3: 24 al 30 de abril.
- Semana -4: 17 al 23 de abril.

Pero al principio puse:
- 14-20 abr
- 21-27 abr
- 28 abr - 4 may
- 5-13 may

Eso son 4 bloques de 7 días? 14-20 (7 días), 21-27 (7 días), 28 abr-4 may (7 días), 5-13 may (9 días). Y el lanzamiento estaría el 14? No, el usuario dijo 15.

Debo corregir las fechas para que sean exactas y consistentes. Es mejor decir:

"Acá va la versión corregida a fechas exactas (asumiendo lanzamiento 15 de mayo):"

Y poner:
- Semana -4: 17 – 23 de abril
- Semana -3: 24 – 30 de abril
- Semana -2: 1 – 7 de mayo
- Semana -1: 8 – 14 de mayo

Pero esto cambia lo que ya habíamos dicho. Sin embargo, es necesario para la coherencia. El usuario no va a reprochar 3 días de diferencia en la semana -4, especialmente porque no hay nada sagrado en esas fechas exactas. Lo importante es que sean 4 semanas de 7 días.

Alternativa: mantener las fechas originales y ajustar solo la última semana. Pero eso deja huecos.

Creo que lo más profesional es presentar la tabla con las fechas corregidas a bloques perfectos de 7 días y una nota: *(Fechas ajustadas a calendario exacto de 7 días; mové 1-2 días si el 15 cae feriado en tu país)*.

Pero si uso 8-14 para semana -1, y quiero que la tabla sea "completa", debería poner:
- Semana -4: 17-23 abr
- Semana -3: 24-30 abr
- Semana -2: 1-7 may
- Semana -1: 8-14 may

Esto es matemáticamente perfecto.

¿Y si el usuario nota que cambié las fechas de la primera respuesta? Puedo poner una nota breve: "Ajusté las fechas a bloques exactos de 7 días para que sea más fácil de ejecutar".

Ahora, para el contenido de la semana -2 (1-7 mayo):
- Lunes 1: Email + post anunciando masterclass del jueves (o del día del evento). Si el evento es jueves 4, el lunes 1 es anuncio.
- Martes 2: Contenido autoridad + encuesta.
- Miércoles 3: Último recordatorio + prueba social.
- Jueves 4: MASTERCLASS + early bird.
- Viernes 5: Seguimiento asistentes + post valor + DMs.
- Sábado 6: Behind the scenes + cierre early bird.
- Domingo 7: Email cierre early bird + cuenta regresiva.

Esto encaja perfecto.

Para la semana -1 (8-14 mayo):
- Lunes 8 (D-7): Testeo + email caso de estudio.
- Martes 9 (D-6): Objeción tiempo.
- Miércoles 10 (D-5): Demo valor.
- Jueves 11 (D-4): Escasez/urgencia.
- Viernes 12 (D-3): Prueba social máxima.
- Sábado 13 (D-2): Descanso estratégico.
- Domingo 14 (D-1): Último recordatorio.

Esto es coherente.

Ahora, para las semanas -4 y -3, debo usar las fechas ajustadas:
- Semana -4: 17-23 abr (Cimientos)
- Semana -3: 24-30 abr (Calentamiento)

Hitos que ya tenía:
Semana -4:
- Producto: Finalizar módulo 1 y estructura.
- Oferta: Precio, bonuses, garantía, duración apertura.
- Técnica: Página de ventas, checkout, plataforma, lista de espera.
- Copy: Borrador secuencia emails y banco de 10 piezas redes.
- Audiencia: Contenido valor puro.

Semana -3:
- Anuncio oficial (email + post) con lista de espera.
- Contenido diario (1 pieza/día) sobre productividad = resultados.
- 2-3 emails de valor educando el problema.
- Anunciar y promover masterclass gratuita para semana siguiente.
- DMs activos.

Todo esto cabe bien en la tabla.

Formato final:
- Intro corta diciendo que ajusté fechas a bloques exactos de 7 días.
- Tabla Markdown con HTML <br> para saltos de línea dentro de celdas (para que se vea bien).
- Nota final con checklist del 15 de mayo.

Debo asegurarme de que la tabla no sea demasiado ancha. Usaré viñetas breves.

Veamos cómo se vería la celda de Semana -2 en Markdown:

| **Semana -2** Aceleración | 1 – 7 may | Evento, autoridad y early bird | **Lun 1:** Email/post anunciando masterclass del Jue 4<br>**Mar 2:** Contenido autoridad + encuesta historias<br>**Mié 3:** Último recordatorio + prueba social temprana<br>**Jue 4:** **MASTERCLASS EN VIVO** + oferta early bird (48h)<br>**Vie 5:** Seguimiento asistentes + post valor + DMs<br>**Sáb 6:** Behind the scenes curso + cierre early bird<br>**Dom 7:** Email cierre early bird + cuenta regresiva al 15 |

Esto funciona.

Celda de Semana -1:

| **Semana -1** Pre-apertura | 8 – 14 may | Urgencia, objeciones y técnica | **Lun 8 (D-7):** Testeo compra real + email caso de estudio + tour curso<br>**Mar 9 (D-6):** Email objeción tiempo + historias FAQ + post error común<br>**Mié 10 (D-5):** Email mini-lección + post antes/después + mostrar bonus<br>**Jue 11 (D-4):** Email bonus fast-action + post valor vs precio + encuesta<br>**Vie 12 (D-3):** Email testimonio + screenshots reales + countdown 7 días<br>**Sáb 13 (D-2):** Descanso estratégico + revisión técnica final + plantillas<br>**Dom 14 (D-1):** Email recordatorio hora apertura + post checklist + serie historias |

Perfecto.

Ahora, para las semanas -4 y -3, las celdas de hitos:

Semana -4:
• Producto: Módulo 1 listo y estructura definida<br>• Oferta: Precio, bonuses, garantía y duración apertura<br>• Técnica: Lista de espera activa, checkout probado, aula configurada<br>• Copy: Borrador 5 emails + banco 10 piezas redes<br>• Audiencia: Contenido valor puro (sin venta) sobre el dolor principal

Semana -3:
• Anuncio oficial: Email + post lanzamiento 15/05 + lista de espera<br>• Contenido diario: 1 pieza/día conectando productividad y resultados<br>• Emails valor: 2-3 educando el problema (sin vender)<br>• Evento: Anunciar masterclass gratuita para la semana siguiente<br>• Comunidad: DMs activos detectando objeciones

Esto es claro y conciso.

Un detalle: en la primera respuesta, semana -3 decía "Anunciar y anunciar una masterclass/webinar gratuito para la semana que viene". En este calendario ajustado, la masterclass cae el Jueves 4 de mayo, que está en la semana -2. Y la