# Kimi K3 — integridad_idioma/jerga_tecnica_densa

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 2.18 | quality: 2.0
- latency_total: 166.133s | tokens_per_second: 49.3
- input_tokens: 297 | output_tokens: 8192

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un periodista que escribe para un medio digital latinoamericano.
Escribes para lectores hispanohablantes de México, Chile, Argentina, Colombia y España.
Tu trabajo es tomar material de origen y redactar en español neutro, claro y directo.

**user:**

Explica en 400-500 palabras, para un fundador sin
formación técnica, qué significa este cambio y por qué le importa:

"Speculative decoding with a 1B draft model cuts time-to-first-token by 40% on 70B
targets, but only when the acceptance rate stays above 0.7. Below that, the verification
overhead dominates and you end up slower than greedy decoding. Batch size interacts
badly: at batch 32+ the draft model contends for the same KV cache bandwidth."

No uses viñetas, escribe en párrafos.


## Respuesta completa

The task: explain in 400-500 words, for a non-technical founder, what this change means and why it matters. The source material is about speculative decoding with a 1B draft model cutting time-to-first-token by 40% on 70B targets, conditional on acceptance rate above 0.7, verification overhead, batch size interactions, KV cache bandwidth contention.

I need to write in neutral, clear, direct Spanish for Latin American and Spanish readers (Mexico, Chile, Argentina, Colombia, Spain). No bullet points, paragraphs only. 400-500 words.

I should explain:
- What speculative decoding is in plain terms: a small "assistant" model that guesses ahead, and the big model verifies.
- Time-to-first-token: the delay before the user sees the first word of the response — latency perceived.
- 1B draft model vs 70B target: small model vs big model (parameters as a measure of size/capability).
- 40% reduction in time-to-first-token: meaningful UX improvement.
- Acceptance rate above 0.7: the small model's guesses need to be right at least 70% of the time; otherwise the big model wastes time checking wrong guesses and it's slower than just doing it normally (greedy decoding).
- Batch size: serving many users at once. At 32+ simultaneous requests, the small model competes for the same memory bandwidth (KV cache), so the trick degrades.
- Why a founder cares: cost, user experience, infrastructure decisions, when this optimization applies and when it doesn't, vendor claims, capacity planning.

Use analogies: like an assistant drafting a document that the expert reviews; if the assistant is right most of the time, you save time; if not, reviewing wastes more time than doing it yourself. Restaurant analogy? Editor and junior writer.

KV cache bandwidth: explain as shared working memory / counter space in a kitchen. Keep it accessible.

Neutral Spanish: avoid regionalisms. Use "computadora" or "ordenador"? Neutral Spanish often uses "computadora" but for Spain "ordenador". Maybe avoid the word or use "servidor" since we're talking about servers/GPUs. Use "memoria" fine. "Latencia" is fine. "Tiempo de respuesta" good.

Word count: 400-500 words. Let me draft and count.

Draft:

Title? Probably no title needed, but could include one. The task says "Explica en 400-500 palabras". I'll write paragraphs only, no bullets. Maybe a short headline is okay but safer to just write the explanation. I'll include a brief headline perhaps — the persona is a journalist for a digital medium. A headline would be natural. But instructions say no bullets, paragraphs; a headline isn't a bullet. I'll add a short headline to fit the journalistic style, then 4-5 paragraphs.

Let me write:

---

**Un truco para que la IA responda más rápido (y cuándo deja de funcionar)**

Imagina que contratas a un asistente junior para ayudar a un experto muy lento pero muy bueno. El asistente redacta borradores rápidos y el experto solo los revisa: si el borrador está bien, lo aprueba en segundos; si está mal, tiene que rehacerlo. Eso es, en esencia, la "decodificación especulativa": un modelo de lenguaje pequeño (de 1.000 millones de parámetros, o 1B) que adivina lo que diría el modelo grande (de 70.000 millones, 70B), y el grande que solo verifica. Cuando funciona, el resultado es idéntico al del modelo grande, pero llega antes.

El dato concreto es este: ese esquema reduce en 40% el "tiempo hasta la primera palabra", es decir, la espera entre que un usuario envía su pregunta y ve aparecer la respuesta en pantalla. Para un producto de IA conversacional, ese número es oro: es la diferencia entre una experiencia que se siente instantánea y una que se siente lenta, y afecta directamente la retención de usuarios.

Pero hay una condición crítica. El truco solo funciona si el modelo pequeño acierta sus predicciones al menos el 70% de las veces (la "tasa de aceptación" de 0,7). Por debajo de ese umbral, el modelo grande pasa más tiempo revisando borradores equivocados que el que le tomaría escribir la respuesta por sí mismo, y el sistema termina siendo más lento que el método tradicional. En la analogía: si tu asistente junior se equivoca la mitad de las veces, corregirlo cuesta más que hacer el trabajo tú mismo. La tasa de aciertos depende del tipo de tarea —textos predecibles como código o respuestas formulares se adivinan fácil; contenido creativo o muy especializado, menos— así que no es un número garantizado: hay que medirlo con tu caso de uso real.

El segundo problema es de escala. Cuando atiendes a muchos usuarios simultáneos (lotes de 32 o más peticiones a la vez), el modelo pequeño empieza a competir con el grande por el mismo recurso: el ancho de banda de la memoria de trabajo donde se guarda el contexto de cada conversación (la "caché KV"). Es como dos cocineros compartiendo una mesa de trabajo demasiado estrecha: se estorban. En la práctica, esto significa que la mejora del 40% puede desvanecerse justo cuando más la necesitas: en horas pico, con muchos usuarios conectados.

¿Por qué debería importarte como fundador? Tres razones. Primero, si tu producto depende de modelos grandes, esta técnica puede mejorar la experiencia sin cambiar de modelo ni pagar hardware más caro. Segundo, los beneficios no son automáticos: exigen monitorear la tasa de aceptación y probar con carga real, no con demos de un solo usuario. Tercero, si un proveedor te promete "40% más rápido", ahora sabes qué preguntar: ¿con qué tasa de aceptación?, ¿con cuántos usuarios simultáneos?, ¿medido en mi tipo de contenido? Las optimizaciones de infraestructura de IA rara vez son gratis; son apuestas condicionales. Entender las condiciones es lo que separa una buena decisión de ingeniería de una sorpresa en la factura del servidor.

---

Let me count words roughly. I'll count paragraph by paragraph.

Paragraph 1: "Imagina que contratas a un asistente junior para ayudar a un experto muy lento pero muy bueno." (15) "El asistente redacta borradores rápidos y el experto solo los revisa: si el borrador está bien, lo aprueba en segundos; si está mal, tiene que rehacerlo." (~26) "Eso es, en esencia, la decodificación especulativa: un modelo de lenguaje pequeño (de 1.000 millones de parámetros, o 1B) que adivina lo que diría el modelo grande (de 70.000 millones, 70B), y el grande que solo verifica." (~35) "Cuando funciona, el resultado es idéntico al del modelo grande, pero llega antes." (14). Total ~90.

Paragraph 2: ~60 words.

Paragraph 3: ~110 words.

Paragraph 4: ~75 words.

Paragraph 5: ~110 words.

Total ≈ 445. Good, within 400-500. Let me actually count more carefully to be safe.

Paragraph 1 word count:
"Imagina(1) que(2) contratas(3) a(4) un(5) asistente(6) junior(7) para(8) ayudar(9) a(10) un(11) experto(12) muy(13) lento(14) pero(15) muy(16) bueno(17)." = 17
"El(1) asistente(2) redacta(3) borradores(4) rápidos(5) y(6) el(7) experto(8) solo(9) los(10) revisa(11): si(12) el(13) borrador(14) está(15) bien(16), lo(17) aprueba(18) en(19) segundos(20); si(21) está(22) mal(23), tiene(24) que(25) rehacerlo(26)." = 26
"Eso(1) es(2), en(3) esencia(4), la(5) decodificación(6) especulativa(7): un(8) modelo(9) de(10) lenguaje(11) pequeño(12) (de(13) 1.000(14) millones(15) de(16) parámetros(17), o(18) 1B(19)) que(20) adivina(21) lo(22) que(23) diría(24) el(25) modelo(26) grande(27) (de(28) 70.000(29) millones(30), 70B(31)), y(32) el(33) grande(34) que(35) solo(36) verifica(37)." = 37
"Cuando(1) funciona(2), el(3) resultado(4) es(5) idéntico(6) al(7) del(8) modelo(9) grande(10), pero(11) llega(12) antes(13)." = 13
P1 = 17+26+37+13 = 93

Paragraph 2:
"El(1) dato(2) concreto(3) es(4) este(5): ese(6) esquema(7) reduce(8) en(9) 40%(10) el(11) tiempo(12) hasta(13) la(14) primera(15) palabra(16), es(17) decir(18), la(19) espera(20) entre(21) que(22) un(23) usuario(24) envía(25) su(26) pregunta(27) y(28) ve(29) aparecer(30) la(31) respuesta(32) en(33) pantalla(34)." = 34
"Para(1) un(2) producto(3) de(4) IA(5) conversacional(6), ese(7) número(8) es(9) oro(10): es(11) la(12) diferencia(13) entre(14) una(15) experiencia(16) que(17) se(18) siente(19) instantánea(20) y(21) una(22) que(23) se(24) siente(25) lenta(26), y(27) afecta(28) directamente(29) la(30) retención(31) de(32) usuarios(33)." = 33
P2 = 67

Paragraph 3:
"Pero(1) hay(2) una(3) condición(4) crítica(5)." = 5
"El(1) truco(2) solo(3) funciona(4) si(5) el(6) modelo(7) pequeño(8) acierta(9) sus(10) predicciones(11) al(12) menos(13) el(14) 70%(15) de(16) las(17) veces(18) (la(19) tasa(20) de(21) aceptación(22) de(23) 0,7(24))." = 24
"Por(1) debajo(2) de(3) ese(4) umbral(5), el(6) modelo(7) grande(8) pasa(9) más(10) tiempo(11) revisando(12) borradores(13) equivocados(14) que(15) el(16) que(17) le(18) tomaría(19) escribir(20) la(21) respuesta(22) por(23) sí(24) mismo(25), y(26) el(27) sistema(28) termina(29) siendo(30) más(31) lento(32) que(33) el(34) método(35) tradicional(36)." = 36
"En(1) la(2) analogía(3): si(4) tu(5) asistente(6) junior(7) se(8) equivoca(9) la(10) mitad(11) de(12) las(13) veces(14), corregirlo(15) cuesta(16) más(17) que(18) hacer(19) el(20) trabajo(21) tú(22) mismo(23)." = 23
"La(1) tasa(2) de(3) aciertos(4) depende(5) del(6) tipo(7) de(8) tarea(9) —textos(10) predecibles(11) como(12) código(13) o(14) respuestas(15) formulares(16) se(17) adivinan(18) fácil(19); contenido(20) creativo(21) o(22) muy(23) especializado(24), menos(25)— así(26) que(27) no(28) es(29) un(30) número(31) garantizado(32): hay(33) que(34) medirlo(35) con(36) tu(37) caso(38) de(39) uso(40) real(41)." = 41
P3 = 5+24+36+23+41 = 129

Paragraph 4:
"El(1) segundo(2) problema(3) es(4) de(5) escala(6)." = 6
"Cuando(1) atiendes(2) a(3) muchos(4) usuarios(5) simultáneos(6) (lotes(7) de(8) 32(9) o(10) más(11) peticiones(12) a(13) la(14) vez(15)), el(16) modelo(17) pequeño(18) empieza(19) a(20) competir(21) con(22) el(23) grande(24) por(25) el(26) mismo(27) recurso(28): el(29) ancho(30) de(31) banda(32) de(33) la(34) memoria(35) de(36) trabajo(37) donde(38) se(39) guarda(40) el(41) contexto(42) de(43) cada(44) conversación(45) (la(46) caché(47) KV(48))." = 48
"Es(1) como(2) dos(3) cocineros(4) compartiendo(5) una(6) mesa(7) de(8) trabajo(9) demasiado(10) estrecha(11): se(12) estorban(13)." = 13
"En(1) la(2) práctica(3), esto(4) significa(5) que(6) la(7) mejora(8) del(9) 40%(10) puede(11) desvanecerse(12) justo(13) cuando(14) más(15) la(16) necesitas(17): en(18) horas(19) pico(20), con(21) muchos(22) usuarios(23) conectados(24)." = 24
P4 = 6+48+13+24 = 91

Paragraph 5:
"¿Por(1) qué(2) debería(3) importarte(4) como(5) fundador(6)? Tres(7) razones(8)." = 8
"Primero(1), si(2) tu(3) producto(4) depende(5) de(6) modelos(7) grandes(8), esta(9) técnica(10) puede(11) mejorar(12) la(13) experiencia(14) sin(15) cambiar(16) de(17) modelo(18) ni(19) pagar(20) hardware(21) más(22) caro(23)." = 23
"Segundo(1), los(2) beneficios(3) no(4) son(5) automáticos(6): exigen(7) monitorear(8) la(9) tasa(10) de(11) aceptación(12) y(13) probar(14) con(15) carga(16) real(17), no(18) con(19) demos(20) de(21) un(22) solo(23) usuario(24)." = 24
"Tercero(1), si(2) un(3) proveedor(4) te(5) promete(6) 40%(7) más(8) rápido(9), ahora(10) sabes(11) qué(12) preguntar(13): ¿con(14) qué(15) tasa(16) de(17) aceptación(18)?, ¿con(19) cuántos(20) usuarios(21) simultáneos(22)?, ¿medido(23) en(24) mi(25) tipo(26) de(27) contenido(28)?" = 28
"Las(1) optimizaciones(2) de(3) infraestructura(4) de(5) IA(6) rara(7) vez(8) son(9) gratis(10); son(11) apuestas(12) condicionales(13)." = 13
"Entender(1) las(2) condiciones(3) es(4) lo(5) que(6) separa(7) una(8) buena(9) decisión(10) de(11) ingeniería(12) de(13) una(14) sorpresa(15) en(16) la(17) factura(18) del(19) servidor(20)." = 20
P5 = 8+23+24+28+13+20 = 116

Total: 93+67+129+91+116 = 496. Close to 500. Good, within range but near the top. Maybe trim slightly to be safe, around 460-480. Let me trim a bit.

Trim: in P3, "respuestas formulares" — maybe "respuestas formulísticas" is better Spanish. "formulares" isn't a word; I meant "formulaic". Use "respuestas repetitivas o fórmulas conocidas". Let me adjust: "textos predecibles, como código o respuestas repetitivas, se adivinan fácil; el contenido creativo o muy especializado, menos".

Also "monitorear" — fine in neutral Spanish (used widely in LatAm; Spain uses "supervisar" but "monitorear" is understood). Could use "vigilar" or "medir de forma continua". Keep "monitorear" — it's common in tech journalism across regions.

"hardware" — commonly used; fine. Could say "servidores más potentes". "sin cambiar de modelo ni pagar servidores más caros" — better neutral.

Also "lotes de 32 o más peticiones" — "peticiones" fine; "solicitudes" also fine. Use "solicitudes" maybe more neutral. Either works. Keep "peticiones" — used in Spain and LatAm.

Should I include a headline? It adds words. The count 496 includes no headline. If I add a headline, I exceed. The instruction says 400-500 words for the explanation. A headline might not count, but safer to keep total near 480 or just skip the headline. I'll include a short headline since it's a journalistic piece, and trim body to ~460 so even with headline it's under 500. Actually, to be safe, let me trim body to ~455 and add a headline of ~10 words → ~465 total. 

Trim options:
- P1: "Eso es, en esencia, la decodificación especulativa:" keep. Maybe drop "Cuando funciona, el resultado es idéntico al del modelo grande, pero llega antes." → keep, it's important (output identical). Keep.
- P3: shorten analogy sentence: "En la analogía: si tu asistente se equivoca la mitad de las veces, corregirlo cuesta más que hacer el trabajo tú mismo." (drop "junior") saves 1.
- P5: fine.

Actually 496 is within 400-500. Adding a headline would push over only if headline counts. Headline of 10 words → 506. Slightly over. Options: no headline, or trim ~15 words. Let me trim ~20 words and include headline, landing ~485 total.

Trims:
- P2: "El dato concreto es este: ese esquema reduce en 40% el tiempo hasta la primera palabra" → "El dato concreto: este esquema reduce en 40% el tiempo hasta la primera palabra" (saves 3).
- P2: "y afecta directamente la retención de usuarios" keep.
- P3: "La tasa de aciertos depende del tipo de tarea —textos predecibles, como código o respuestas repetitivas, se adivinan fácil; el contenido creativo o muy especializado, menos— así que no es un número garantizado: hay que medirlo con tu caso de uso real." Recount: roughly same. Maybe shorten to "La tasa de aciertos depende del tipo de tarea: el código o las respuestas repetitivas se adivinan fácil; el contenido creativo, menos. No es un número garantizado: hay que medirlo con tu caso de uso real." Let me count: La(1) tasa(2) de(3) aciertos(4) depende(5) del(6) tipo(7) de(8) tarea(9): el(10) código(11) o(12) las(13) respuestas(14) repetitivas(15) se(16) adivinan(17) fácil(18); el(19) contenido(20) creativo(21), menos(22). No(23) es(24) un(25) número(26) garantizado(27): hay(28) que(29) medirlo(30) con(31) tu(32) caso(33) de(34) uso(35) real(36). = 36 (was 41, saves 5).
- P4: "Es como dos cocineros compartiendo una mesa de trabajo demasiado estrecha: se estorban." keep — vivid.
- P5: "¿Por qué debería importarte como fundador? Tres razones." keep.

Savings: 3 + 5 + a few = ~10. New body ≈ 486. Headline 10 words → 496. Cutting it close. Trim a bit more:

- P1: "Imagina que contratas a un asistente junior para ayudar a un experto muy lento pero muy bueno." → "Imagina que contratas a un asistente junior para ayudar a un experto brillante pero lento." = Imagina(1) que(2) contratas(3) a(4) un(5) asistente(6) junior(7) para(8) ayudar(9) a(10) un(11) experto(12) brillante(13) pero(14) lento(15). = 15 (saves 2).
- P5: "Las optimizaciones de infraestructura de IA rara vez son gratis; son apuestas condicionales." → "En IA, estas optimizaciones rara vez son gratis: son apuestas condicionales." = En(1) IA(2), estas(3) optimizaciones(4) rara(5) vez(6) son(7) gratis(8): son(9) apuestas(10) condicionales(11). = 11 (saves 2).
- P5: "sin cambiar de modelo ni pagar hardware más caro" → "sin cambiar de modelo ni pagar servidores más caros" same count.

Total savings ~14 → body ≈ 482, headline ~10 → 492. Hmm still near limit. It's fine: "400-500 palabras" — 490 is within. But counting variations (hyphenated words, "40%" as one word, "1.000" as one) could shift things. My count treats "40%" as one word. If a counter treats numbers differently, could vary ±few. 480-490 is safe.

Alternatively skip the headline entirely and land ~482. The instruction didn't ask for a headline. Journalist persona suggests one could be nice, but not required. I'll include a short headline — it fits the medium — and keep body tight. Actually, risk: if evaluator counts headline words, fine (~490). If not, 482. Both within range. Good.

Let me also double check neutral Spanish choices:
- "computadora/ordenador" — avoided; used "servidor", "hardware"→ changed to "servidores".
- "pantalla" — neutral.
- "petición" — neutral in tech contexts; "solicitud" also fine. Keep "peticiones".
- "horas pico" — neutral (Spain: "horas punta"). Hmm. "Horas pico" is used in LatAm; Spain says "hora punta". Neutral alternative: "en los momentos de mayor demanda". Use that to be safe: "justo cuando más la necesitas: en los momentos de mayor demanda, con muchos usuarios conectados." Adds a couple words but more neutral.
- "monitorear" — widely used in LatAm tech; Spain increasingly uses it, but "supervisar" is safer neutral. Use "medir y supervisar"? Just "supervisar la tasa de aceptación". Or "exige medir la tasa de aceptación de forma continua". I'll say "exigen supervisar la tasa de aceptación y probar con carga real".
- "junior" — anglicism common everywhere; fine.
- "caché KV" — keep the term, explained.
- "lote" for batch — fine, or "tandas". "lotes de 32 o más peticiones" ok.
- "tú" form — neutral, appropriate for founder audience. Fine.

Also check: "respuestas formulares" removed. Good.

One more check on accuracy: speculative decoding — draft model proposes tokens, target verifies in parallel; if accepted, you get multiple tokens per step; TTFT reduction claim as given. Acceptance rate 0.7 threshold as given. Greedy decoding comparison as given. Batch 32+ KV cache bandwidth contention as given. My explanation stays faithful: I say "reduce 40% el tiempo hasta la primera palabra" per source. Note: technically speculative decoding usually helps throughput/per-token latency more than TTFT, but the source says TTFT, so I report the source. Fine — I'm rewriting the source, not fact-checking it.

Also "el resultado es idéntico al del modelo grande" — speculative decoding with proper verification preserves the target model's output distribution; greedy gives identical outputs. Acceptable simplification.

Final structure: headline + 5 paragraphs. Let me finalize text.

Final:

**Un truco para que la IA responda más rápido, y cuándo deja de funcionar**

(11 words)

P1: Imagina que contratas a un asistente junior para ayudar a un experto brillante pero lento. El asistente redacta borradores rápidos y el experto solo los revisa: si el borrador está bien, lo aprueba en segundos; si está mal, tiene que rehacerlo. Eso es, en esencia, la decodificación especulativa: un modelo de lenguaje pequeño (de 1.000 millones de parámetros, o 1B) que adivina lo que diría el modelo grande (de 70.000 millones, 70B), y el grande que solo verifica. Cuando funciona, el resultado es idéntico al del modelo grande, pero llega antes.

P2: El dato concreto: este esquema reduce en 40% el tiempo hasta la primera palabra, es decir, la espera entre que un usuario envía su pregunta y ve aparecer la respuesta en pantalla. Para un producto de IA conversacional, ese número es oro: es la diferencia entre una experiencia que se siente instantánea y una que se siente lenta, y afecta directamente la retención de usuarios.

P3: Pero hay una condición crítica. El truco solo funciona si el modelo pequeño acierta sus predicciones al menos el 70% de las veces (la "tasa de aceptación" de 0,7). Por debajo de ese umbral, el modelo grande pasa más tiempo revisando borradores equivocados que el que le tomaría escribir la respuesta por sí mismo, y el sistema termina siendo más lento que el método tradicional. En la analogía: si tu asistente se equivoca la mitad de las veces, corregirlo cuesta más que hacer el trabajo tú mismo. La tasa de aciertos depende del tipo de tarea: el código o las respuestas repetitivas se adivinan fácil; el contenido creativo o muy especializado, menos. No es un número garantizado: hay que medirlo con tu caso de uso real.

P4: El segundo problema es de escala. Cuando atiendes a muchos usuarios simultáneos (lotes de 32 o más peticiones a la vez), el modelo pequeño empieza a competir con el grande por el mismo recurso: el ancho de banda de la memoria de trabajo donde se guarda el contexto de cada conversación (la "caché KV"). Es como dos cocineros compartiendo una mesa de trabajo demasiado estrecha: se estorban. En la práctica, esto significa que la mejora del 40% puede desvanecerse justo cuando más la necesitas: en los momentos de mayor demanda, con muchos usuarios conectados.

P5: ¿Por qué debería importarte como fundador? Tres razones. Primero, si tu producto depende de modelos grandes, esta técnica puede mejorar la experiencia sin cambiar de modelo ni pagar servidores más caros. Segundo, los beneficios no son automáticos: exigen supervisar la tasa de aceptación y probar con carga real, no con demos de un solo usuario. Tercero, si un proveedor te promete "40% más rápido", ahora sabes qué preguntar: ¿con qué tasa de aceptación?, ¿con cuántos usuarios simultáneos?, ¿medido en mi tipo de contenido? En IA, estas optimizaciones rara vez son gratis: son apuestas condicionales. Entender las condiciones es lo que separa una buena decisión de ingeniería de una sorpresa en la factura del servidor.

Recount roughly: P1 = 15+26+37+13 = 91. P2 = 31+33 = 64. P3 = 5+24+36+22+22+14 = let me recount P3 sentences:
- "Pero hay una condición crítica." 5
- "El truco solo funciona si el modelo pequeño acierta sus predicciones al menos el 70% de las veces (la tasa de aceptación de 0,7)." 24
- "Por debajo de ese umbral, el modelo grande pasa más tiempo revisando borradores equivocados que el que le tomaría escribir la respuesta por sí mismo, y el sistema termina siendo más lento que el método tradicional." 36
- "En la analogía: si tu asistente se equivoca la mitad de las veces, corregirlo cuesta más que hacer el trabajo tú mismo." 22
- "La tasa de aciertos depende del tipo de tarea: el código o las respuestas repetitivas se adivinan fácil; el contenido creativo o muy especializado, menos." La(1) tasa(2) de(3) aciertos(4) depende(5) del(6) tipo(7) de(8) tarea(9): el(10) código(11) o(12) las(13) respuestas(14) repetitivas(15) se(16) adivinan(17) fácil(18); el(19) contenido(20) creativo(21) o(22) muy(23) especializado(24), menos(25). = 25
- "No es un número garantizado: hay que medirlo con tu caso de uso real." 14
P3 = 5+24+36+22+25+14 = 126

P4 = 6+48+13+? Last sentence: "En(1) la(2) práctica(3), esto(4) significa(5) que(6) la(7) mejora(8) del(9) 40%(10) puede(11) desvanecerse(12) justo(13) cuando(14) más(15) la(16) necesitas(17): en(18) los(19) momentos(20) de(21) mayor(22) demanda(23), con(24) muchos(25) usuarios(26) conectados(27)." = 27
P4 = 6+48+13+27 = 94

P5: 8 + "Primero...caros." Primero(1), si(2) tu(3) producto(4) depende(5) de(6) modelos(7) grandes(8), esta(9) técnica(10) puede(11) mejorar(12) la(13) experiencia(14) sin(15) cambiar(16) de(17) modelo(18) ni(19) pagar(20) servidores(21) más(22) caros(23). = 23
"Segundo...usuario." Segundo(1), los(2) beneficios(3) no(4) son(5) automáticos(6): exigen(7) supervisar(8) la(9) tasa(10) de(11) aceptación(12) y(13) probar(14) con(15) carga(16) real(17), no(18) con(19) demos(20) de(21) un(22) solo(23) usuario(24). = 24
"Tercero...contenido?" Tercero(1), si(2) un(3) proveedor(4) te(5) promete(6) 40%(7) más(8) rápido(9), ahora(10) sabes(11) qué(12) preguntar(13): ¿con(14) qué(15) tasa(16) de(17) aceptación(18)?, ¿con(19) cuántos(20) usuarios(21) simultáneos(22)?, ¿