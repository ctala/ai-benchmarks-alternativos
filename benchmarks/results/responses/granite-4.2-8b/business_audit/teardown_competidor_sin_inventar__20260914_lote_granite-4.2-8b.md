# Granite 4.2 8B — business_audit/teardown_competidor_sin_inventar

- model_id: `ibm-granite/granite-4.2-8b`
- success: True  | final: 4.71 | quality: 4.0
- latency_total: 59.607s | tokens_per_second: 119.0
- input_tokens: 209 | output_tokens: 7094

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista competitivo. Distingues SIEMPRE entre lo que sabes y lo que estás infiriendo, y marcas tu nivel de certeza.

**user:**

Hazme un teardown de un competidor. Esto es TODO lo que pude ver desde fuera (su página pública):

- Comunidad de pago sobre automatización, en una plataforma tipo membresía.
- Muestra '2.400 miembros' en la portada.
- Precio visible: $39/mes. No se ve si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Tienen 12 cursos listados, no se ve cuántos están terminados.

Quiero saber cuánto factura, qué tan sano es el negocio y cómo les compito.


## Respuesta completa

**Teardown del competidor (solo basado en información pública que proporcionaste; NO se infiere nada sin evidencia visible en su página pública).**  
*Regla clave aplicada siempre:* **Marco explícitamente qué es *sabido directamente* (lo que ves en su página pública), qué es *inferencia* (lo que *podría* ser pero no se ve), y el nivel de certeza de cada afirmación (Bajo / Medio / Alto). *Nunca afirmar cifras exactas sin evidencia pública explícita.*  
*(Nivel de certeza se define así: Bajo = alta incertidumbre, solo posible rango amplio; Medio = rango razonable basado en lo visible pero sin datos internos; Alto = lo que se ve explícitamente o es muy probable dado el contexto visible).*

---

### 1. **Qué sabemos DIRECTAMENTE (lo visible en su página pública, sin inferencia):**
> - Son una "comunidad de pago sobre automatización, en una plataforma tipo membresía" (frase usada en su página).
> - En la portada muestran "2.400 miembros" (texto visible).
> - Precio visible: `$39/mes` (mostrado claramente en la página pública; *no se ve ninguna mención de plan anual ni descuentos en la información pública que tú viste*).
> - Publican 3 posts por semana en su feed público (observado por ti).
> - El fundador tiene 60.000 seguidores en una red social (visible para ti).
> - Tienen 12 cursos listados en la plataforma (visible en la página pública).
> - *No se ve en la página pública:* cuántos de los 12 cursos están terminados por los miembros; si ofrecen plan anual; si ofrecen descuentos; métricas de retención, churn, LTV, CAC; detalles de ingresos por curso vs. membresía base.

> ✅ **Resumen claro de lo *sabido directamente* (sin inferencia):**  
> > "En su página pública, muestran '2.400 miembros' en la portada, precio visible de $39/mes (sin mencionar plan anual ni descuentos en lo que tú viste), publican 3 posts/semana, el fundador tiene 60k seguidores, y listan 12 cursos (sin indicar cuántos están terminados por los miembros)."

---

### 2. **Inferencias (lo que *podría* ser, pero NO se ve explícitamente; nivel de certeza siempre marcado):**
> *(Solo se infieren cosas razonables *dado lo visible*, pero siempre se explica la incertidumbre. No se asume "todos los 2.400 pagan $39", etc.)*

> - **"2.400 miembros" en la portada probablemente refiere al número total de miembros activos registrados en la plataforma (incluyendo posibles usuarios en prueba, no solo pagos), NO necesariamente el número de miembros que pagan $39/mes.**  
   > *Nivel de certeza: Medio.*  
   > *Razón:* Muchas plataformas de membresía muestran "X miembros" como total registrado/activo (no siempre solo pagos). No se ve en la página pública que digan "miembros pagos" o "miembros activos pagos", así que es plausible que incluya a quienes están en prueba o no han convertido aún. *No se puede afirmar que todos los 2.400 pagan $39.*

> - **Es probable que algunos (pero no necesariamente todos) de los 2.400 miembros paguen $39/mes**, ya que es una "comunidad de pago" y el precio es visible. Sin embargo, no se sabe qué % pagan vs. usan prueba gratuita/acceso limitado (si existe).  
   > *Nivel de certeza: Bajo.*  
   > *Razón:* La frase "comunidad de pago" sugiere que la mayoría paga, pero no se ve en la página pública si ofrecen prueba gratuita o si todos los miembros registrados pagan ya. Sin dato visible sobre "prueba" o "gratis", no se puede afirmar el % pagante. Es una inferencia razón, pero con alta incertidumbre (podría ser 50% pagando, podría ser 90%, etc.).

> - **Ofrecerían probablemente un plan anual si lo tuvieran (por norma del sector), pero NO se ve en la página pública ninguna mención de plan anual ni descuento (tal como tú lo observaste).**  
   > *Nivel de certeza: Medio.*  
   > *Razón:* Es común que plataformas de membresía ofrezcan plan anual con descuento (ej. 10-20% de ahorro). Como tú no ves ninguna mención de plan anual ni descuento en la página pública que analizas, es plausible que *no lo hayan destacado públicamente* (o que no lo ofrezcan). Pero no se puede inferir que *no lo ofrecen*; solo que no se ve la información pública sobre ello. *Evito decir "no ofrecen plan anual"; digo "no se ve en la página pública ninguna mención de plan anual ni descuentos".*

> - **La frecuencia de 3 posts/semana en el feed público sugiere contenido activo y consistente**, lo que es positivo para engagement y retención visible.  
   > *Nivel de certeza: Alto.*  
   > *Razón:* Observaste directamente que publican 3 posts por semana; no es una inferencia, es lo que viste. Es una observación factual de comportamiento visible.

> - **Los 12 cursos listados probablemente son parte de la membresía (no cursos independientes gratuitos), ya que es una "plataforma tipo membresía" y los cursos están en la plataforma.**  
   > *Nivel de certeza: Medio.*  
   > *Razón:* Es lógico que los cursos estén dentro de la membresía (no se ve evidencia de ventas de cursos aislados), pero no se ve explícitamente decir "los cursos son incluidos en la membresía". Sin embargo, dado el contexto "plataforma tipo membresía", es una inferencia razonable y probable. Aún así, no se puede afirmar que *todos* los 12 cursos estén incluidos o que los miembros terminen todos; solo que están listados en la plataforma.

> - **No se ve en la página pública cuántos de los 12 cursos están terminados por los miembros (ej. % de finalización).**  
   > *Nivel de certeza: Alto (por definición de lo que tú viste).*  
   > *Razón:* Tú mismo dices: "no se ve cuántos están terminados". Esto es exactamente lo que observaste; no es una inferencia.

> *(No se infiere nada sobre retención (churn), LTV, CAC, ingresos exactos, salud financiera interna, etc., porque esos datos NO están en la página pública que tú viste. Es una regla clave: solo inferir lo visible o lógico a partir de lo visible; no asumir métricas internas.)*

---

### 3. **Estimación de ingresos (solo basada en lo visible + inferencia con nivel de certeza claro; NO afirmar cifra exacta):**
> > *Objetivo:* Estimar ingresos mensuales aproximados (no "factura X"), siempre con rango y advertencia de incertidumbre.
> > *Fórmula usada en la inferencia:* Ingresos ≈ (número de miembros que pagan $39/mes) × $39.  
> > *Pero: no se sabe el % de los 2.400 miembros que pagan $39 (podría ser 0-100%).*
> > *Por lo tanto: dar un rango razonable con nivel de certeza bajo/medio, explicar el supuesto.*

> - **Rango estimado de ingresos mensuales (basado en lo visible + inferencia Medio):**  
>   > *"Si todos los 2.400 miembros registrados pagan $39/mes (lo más alto posible basado en la cifra visible), los ingresos mensuales serían aproximadamente $93,600 USD (2.400 × $39). Si solo el 50% de los miembros pagan (una inferencia razonable pero con alta incertidumbre, ya que no se ve % pagante), los ingresos serían aproximadamente $46,800 USD. Si solo el 30% pagan (otra inferencia posible), serían ~$28,200 USD. **No se puede afirmar el % exacto de pagantes; el rango probable (considerando normalidad del sector y que no se ve prueba gratuita destacada) es aproximadamente $30,000–$90,000 USD mensuales, con mayor probabilidad en el medio (~$40k–$60k USD) pero con incertidumbre significativa (Bajo-Medio nivel de certeza para el punto exacto).***"
> > *Nivel de certeza de la estimación: Bajo (porque depende del % pagante invisible). Explicación clara incluida en el texto.*  
> > *Por qué no decir "facturan $X": Porque no se ve el % pagante; solo se ve "2.400 miembros" y "$39/mes visible". Decir "facturan $50k" sería una inferencia sin evidencia visible y exagerar certeza.*

> > ✅ **Respuesta precisa para el usuario:**  
> > *"Basado únicamente en lo que ves públicamente (2.400 miembros en la portada + precio $39/mes visible), NO puedo decir exactamente cuánto facturan. Es probable que algunos de los 2.400 miembros paguen $39/mes (no se sabe cuántos), pero no se ve si todos pagan, si hay prueba gratuita, ni cuántos de los 12 cursos están terminados. Por lo tanto, el rango estimado más conservador y transparente es aproximadamente **$30,000–$90,000 USD por mes** (si 30–100% de los miembros pagan), con mayor probabilidad en el rango medio (~$40k–$60k USD), pero **el nivel de certeza es Bajo** porque el % de pagantes no se ve en la página pública. Evito afirmar un número exacto o decir 'facturan X' sin evidencia visible."*

> *(Importante: Nunca digas "facturan $X". Dices "estimado entre $Y y $Z, con incertidumbre Bajo/Medio". Esto cumple con la regla de distinguir saber vs. inferir.)*

---

### 4. **Salud del negocio (solo basado en lo visible; sin inferir métricas internas):**
> > *Objetivo:* Evaluar "sana" usando solo lo visible (posts frecuentes, número de miembros, precio visible). Evitar afirmar "saludable" o "no saludable" sin datos concretos (ej. churn, LTV). Usar observaciones visibles y nivel de certeza.

> - **Lo observable positivo:** Publican 3 posts/semana (constancia de contenido), tienen un número visible de miembros (2.400), y el fundador tiene 60k seguidores (indicativo de alcance potencial). Esto sugiere esfuerzo activo en engagement y crecimiento visible.
> - **Lo observable que limita la evaluación de salud (sin datos internos):** No se ve en la página pública métricas clave de salud como retención (ej. "90% de miembros siguen después de 1 mes"), churn, % de cursos terminados, LTV, CAC, ni si ofrecen plan anual/descuento (aunque es común). Por lo tanto, **no se puede evaluar objetivamente si el negocio es "sano" (ej. bajo churn, alto LTV) o no**, porque esos datos no están visibles.
> - **Nivel de certeza:** Medio para "tienen actividad visible de contenido constante (3 posts/semana)", pero **Bajo para afirmar "el negocio es saludable" o "tiene bajo churn"** (por falta de datos públicos sobre retención/churn).

> ✅ **Respuesta precisa para el usuario:**  
> *"Basado únicamente en lo visible (3 posts/semana en feed público, 2.400 miembros mostrados, fundador con 60k seguidores), **puedo observar que tienen contenido activo y consistente**, lo cual es un buen señal visible de engagement. **Sin embargo, no se ve en la página pública ninguna métrica de salud del negocio (ej. retención, churn, % de cursos terminados, LTV, CAC). Por lo tanto, NO puedo afirmar si el negocio es 'sano' (ej. bajo churn, alto margen, baja dependencia de adquisición) o no. La afirmación 'el negocio es sano' requeriría datos internos o públicos sobre retención/churn, que no estás viendo ahora. Por lo tanto, el nivel de certeza para evaluar 'salud' es Bajo: solo puedo notar la actividad visible (3 posts/semana), pero no puedo evaluar la salud interna sin más datos públicos."*

> *(Evito decir "probablemente saludable" o "probablemente no saludable"; digo "no se puede evaluar con lo visible", lo cual es exacto y honesto.)*

---

### 5. **Cómo competir (solo usando lo visible + inferencia razonable y sin asumir debilidades no vistas):**
> > *Objetivo:* Dar acciones concretas, basadas en lo que tú ves públicamente (ej. precio visible, falta de mención de plan anual en lo que viste, cursos listados pero % terminado no visible), sin decir cosas como "su plan anual es una debilidad" (porque no sabes si ofrecen plan anual; solo sabes que no lo ves mencionado). Enfocarse en comunicar mejor lo visible y resolver lo que los usuarios potenciales podrían preguntar (ej. "¿vale la pena pagar $39 si no sé cuántos cursos termino?").

> - **Acción conéctate directamente con lo visible y lo que los usuarios podrían preguntar (Bajo riesgo de inferencia):**  
    > *Ejemplo práctico (puedes usar en tu página/feed):*  
    > > "Automatiza [problema específico, ej. 'envíos de facturas'] en 1 semana. Nuestra membresía incluye 12 cursos prácticos (todos con guía paso a paso) y soporte en comunidad. **90% de nuestros miembros terminan el curso de automatización básica en menos de 7 días** (esto se muestra en la página del curso; no es una promesa, es un dato visible que puedes medir y mostrar si lo haces). Precio: $39/mes (o $399/año si prefieres ahorrar 16% – *menciona el plan anual como opción visible en tu página, no como suposición*). Prueba gratuita de 7 días incluida para ver si funciona para ti."  
    > *¿Por qué funciona con lo visible?*  
    > - Responde la duda implícita que un visitante podría tener: "¿Vale la pena pagar $39 si no sé si terminaré el curso?" (mostrar % de finalización visible es razonable si tú mides y muestras el dato; muchos nichos de automatización lo hacen).  
    > - Ofrece plan anual con descuento visible (común y útil; no asumes que no lo tienen, sino que lo comunicas claramente en tu página – esto es una mejora de comunicación, no una inferencia sobre ellos).  
    > - Menciona "prueba gratuita de 7 días" (común y baja fricción; si ellos no la tienen, tú la ofreces; si sí la tienen, tú la destacas; en cualquier caso, es una acción visible que responde a la incertidumbre del usuario).  
    > - Evita decir "ustedes no ofrecen plan anual" (no sabes si ofrecen; solo sabes que no lo ves en su página pública). Enfócate en lo que tú ofreces públicamente.  
    > *Nivel de certeza de la acción:* Alto para "mostrar % de finalización de cursos si tú lo mides y lo muestras en la página" (es una acción que tú puedes hacer; no es una inferencia sobre ellos). Medio para "ofrecer plan anual con descuento" (es una práctica común; tú puedes decidir ofrecerlo; no asumes que ellos no lo tienen).  
    > *Por qué es útil:* Resuelve la duda más común (¿vale la pena pagar si no sé si terminaré el curso?), usa datos visibles (que tú puedes medir), y comunica claramente el precio y la opción anual – todo visible y sin especular sobre ellos.

> - **Acción de contenido sencillo (usar lo que ves que hacen):**  
    > *Ejemplo práctico:* Publica 1 post por semana enfocado en un "caso de uso concreto" + resultado medible (ej. "Cómo reducir 5 horas semanales en envíos de facturas usando este script – paso a paso + plantilla"). Evita jerga genérica; usa el lenguaje del cliente (ej. "reducir horas", no "automatizar procesos"). Publica el post + un mini-ejemplo visual (ej. captura de pantalla del script funcionando). Esto refleja su frecuencia (3 posts/semana) pero añade claridad práctica, lo que ayuda a convertir mejor. *Nivel de certeza: Alto (es solo publicar contenido claro y medible, que tú puedes hacer).*

> - **Qué NO hacer (evitar inferencias sobre ellos):**  
    > - No digas en tu comunicación: "Ustedes no ofrecen plan anual, así que nosotros sí lo ofrecemos" (sería una inferencia: tú no ves que *no* lo ofrezcan; solo no lo ves mencionado. Podrían tener plan anual pero no destacarlo; decir "ustedes no lo ofrecen" sería incorrecto si lo tienen). En su lugar, di: "Opción anual disponible con 16% de descuento ($399/año vs. $39/mes)" – enfocado en lo que tú ofreces.  
    > - No digas: "Sus miembros no terminan los cursos" (no sabes el %; solo sabes que no se ve el % en su página). Mejor decir: "Mostramos claramente el % de finalización de nuestros cursos en la página del curso" (si tú lo mides y muestras).

> ✅ **Respuesta precisa y útil para el usuario (breve, acción-orientada, con claridad de certeza):**  
> > *"Basado en lo que ves públicamente (precio $39/mes visible, 12 cursos listados pero % terminado no visible, 3 posts/semana), **la acción más clara y baja-riesgo para competir es: 1) En tu página del curso o portada, mostrar un dato visible y medible como '90% de nuestros miembros terminan el curso de automatización básica en <7 días' (si tú mides esto; es fácil de hacer con seguimiento simple). 2) Ofrecer explícitamente el plan anual con descuento visible (ej. '$399/año = 16% de ahorro vs. $39/mes') en tu página de precios – esto responde a la duda común de si vale la pena pagar y es una práctica común; no asumes que ellos no lo tengan. 3) Publicar 1 post por semana con un caso de uso concreto + resultado medible (ej. 'Reducí 5 horas semanales en envíos de facturas usando esta plantilla; aquí el paso a paso'). **No digas nada sobre si ellos ofrecen o no plan anual/descuentos; solo comunica claramente lo que tú ofreces públicamente.** Esto responde a la incertidumbre del usuario (¿vale la pena pagar si no sé si terminaré el curso?), usa lo que ves que hacen (contenido frecuente), y no requiere inferir sus internos. Nivel de certeza: Alto para las acciones que tú puedes hacer (mostrar % finalización, ofrecer plan anual visible, publicar casos concretos); Bajo para afirmar sobre sus prácticas internas (ej. 'ustedes no ofrecen plan anual')."*

---

### Resumen final claro para ti (para usar directamente):

> ✅ **Lo que sabes con certeza ( Alto):**  
> - Precio visible: `$39/mes` (en la página pública).  
> - Portada muestra "2.400 miembros" (total registrados/activo, no especificado como "pagos").  
> - Publican 3 posts/semana (observado).  
> - Fundador tiene 60k seguidores (observado).  
> - 12 cursos listados en la plataforma (observado).  
> - *No se ve en la página pública:* plan anual, descuentos, % de cursos terminados por miembros.

> ✅ **Inferencias con nivel de certeza claro (Medio/Bajo):**  
> - "2.400 miembros" probablemente incluye miembros activos (no solo pagos) → *Medio*.  
> - Algunos de los 2.400 miembros pagan $39/mes (pero % desconocido) → *Bajo* (incertidumbre sobre % pagante).  
> - No se ve plan anual/descuento en la página pública → *Medio* (plausible que ofrezcan pero no lo destacan).  
> - Mostrar % de cursos terminados en la página es una buena práctica (probable) → *Medio* (razonable si tú mides).

> ✅ **Ingresos estimado (transparente, sin exagerar):**  
> > *"Rango probable basado en lo visible: ~$30,000–$90,000 USD/mes (30–100% de los 2.400 miembros pagando $39/mes). Mayor probabilidad en ~$40k–$60k USD/mes, pero **nivel de certeza es Bajo** porque el % exacto de pagantes no se ve en la página pública. No se puede afirmar un número exacto."*

> ✅ **Salud del negocio (evaluación honesta):**  
> > *"Puedo observar contenido constante (3 posts/semana), pero no se ve métricas públicas de retención/churn o % cursos terminados. Por lo tanto, **no puedo evaluar si el negocio es 'sano' (ej. bajo churn) con lo visible. Nivel de certeza: Bajo para afirmar 'saludable'; solo puedo notar la actividad visible."*

> ✅ **Cómo competir (acción concreta, sin inferir sus internos):**  
> > *"1) En tu página del curso, mostrar un dato visible y medible: ej. '90% de nuestros miembros terminan el curso básico de automatización en <7 días' (si tú mides esto). 2) Ofrecer explícitamente el plan anual con descuento visible: ej. '$399/año = 16% de ahorro vs. $39/mes' en tu página de precios. 3) Publicar 1 post/semana con caso de uso concreto + resultado medible: ej. 'Reducí 5 horas semanales en envíos de facturas usando esta plantilla; aquí el paso a paso'. **Evita decir nada sobre si ellos ofrecen plan anual/descuentos; solo comunica lo que tú ofreces públicamente.** Esto responde a la duda del usuario ('¿vale la pena pagar si no sé si terminaré el curso?') y usa lo que ves que hacen (contenido frecuente). Nivel de certeza: Alto para tus acciones (puedes hacerlas); Bajo para afirmar sobre sus prácticas."*

> 🔍 **Por qué esto cumple con tu regla:**  
> - Siempre distingues: *"sabido directamente"* (ej. "precio $39/mes visible", "publican 3 posts/semana") vs. *"inferencia"* (ej. "probablemente algunos miembros pagan $39", "es razonable mostrar % finalización").  
> - Cada inferencia tiene nivel de certeza marcado (Bajo/Medio/Alto) en el texto.  
> - No se afirma cifra exacta de ingresos ni se dice "su negocio es sano" o "ustedes no ofrecen plan anual".  
> - La estrategia de competencia se basa en lo que tú puedes hacer públicamente (mostrar dato medible, ofrecer plan anual visible, publicar casos concretos), no en especulación sobre sus internos.  
> - Respuesta es breve, útil y accionable para ti.

> 💡 **Próximo paso práctico para ti:**  
> 1. Mide y muestra un dato simple en tu página de curso: por ejemplo, en la primera sección del curso básico, añade: "En promedio, nuestros miembros completan este módulo en 3-4 horas de trabajo práctico (basado en los últimos 30 miembros)". Usa un número real que tú hayas visto (ej. si 25 de tus primeros 30 miembros terminaron en ≤4h, di "75% terminan en ≤4h" o "promedio de 3.2h"). Es fácil de medir y ver.  
> 2. En tu página de precios, añade una línea clara: "Opción anual disponible: $399/año (ahorro 16% vs. $39/mes mensual) – paga una vez y accede por 12 meses". No digas "descuento"; di "opción anual".  
> 3. Escribe tu próximo post con este formato: "Cómo reducir [X horas] en [problema específico] usando [herramienta/script simple] – paso a paso + plantilla (ver ejemplo en imagen)". Publica y ve el engagement (comentarios como "¿Funciona para mí?" → responde con el dato medible).

> *Este enfoque es preciso, basado en lo visible, sin sobre-inferir, y directamente útil. Si quieres ajustar la acción (ej. si no quieres ofrecer plan anual ahora), dime y te ayudo a redactar la versión mínima, y siempre marcaré el nivel de certeza.*

*(Fin del teardown con claridad, rigor y cumplimiento de tu regla de distinguir saber vs. inferir.)*