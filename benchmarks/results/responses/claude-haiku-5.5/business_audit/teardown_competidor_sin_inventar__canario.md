# Claude Haiku 5.5 — business_audit/teardown_competidor_sin_inventar

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 4.72 | quality: 4.0
- latency_total: 17.962s | tokens_per_second: 182.9
- input_tokens: 288 | output_tokens: 3286

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

# Teardown: comunidad de pago de automatización

## 1. Lo que sabes (hechos observados)

- Es una comunidad de pago sobre automatización, en formato membresía.
- La portada muestra "2.400 miembros".
- Precio visible: $39/mes. No sabes si hay plan anual ni descuentos.
- Publican 3 posts por semana en el feed público.
- El fundador tiene 60.000 seguidores en una red social.
- Hay 12 cursos listados. No sabes cuántos están terminados.

## 2. Lo que infieres (con nivel de certeza)

| Inferencia | Certeza | Por qué |
|---|---|---|
| El producto principal es la membresía, y los cursos son un complemento | Media-alta | Los cursos aparecen listados, pero el precio y el formato de comunidad sugieren que la suscripción es el núcleo |
| El fundador es el principal motor de adquisición | Alta | 60k seguidores y contenido publicado sugieren que el canal propio es central |
| La operación es activa y tiene cadencia de contenido sostenida | Media | 3 posts/semana indica consistencia, pero no dice nada sobre el uso real de la comunidad |
| Dependen mucho del fundador | Media | Es habitual en negocios de creador, pero no lo puedes verificar desde fuera |
| Tienen más de un canal de adquisición | Baja | No tienes datos de tráfico ni de fuentes |

## 3. Facturación estimada

**No hay forma de saber cuánto factura desde fuera.** Lo que puedes hacer es un rango con supuestos explícitos.

**Techo teórico:** 2.400 × $39 = **$93.600 MRR** (≈ $1,12M ARR). Esto solo se cumple si:
- Los 2.400 pagan activamente,
- Todos pagan el precio completo mensual,
- Nadie tiene descuento, prueba gratuita ni cuenta inactiva.

Es improbable. Hay varios factores que lo reducen:
- **"Miembros" puede significar acumulados históricos**, no activos. Muchas comunidades muestran el total histórico.
- **Pruebas gratuitas, becas o cuentas de equipo** inflan el contador sin generar ingreso.
- **Churn**: en comunidades de suscripción mensual es común perder una fracción relevante cada mes.
- **Planes anuales con descuento** reducen el ingreso por miembro.

**Escenarios (certeza baja, son supuestos):**

| Escenario | % de miembros pagando | MRR aprox. | ARR aprox. |
|---|---|---|---|
| Bajo | 30% | ~$28k | ~$340k |
| Medio | 60–80% | ~$45k–75k | ~$550k–900k |
| Techo | 100% | ~$94k | ~$1,1M |

Mi estimación más razonable está en el **escenario medio (ARR de $0,5M–0,9M)**, con certeza baja. Si quieres afinar, la señal más útil sería conocer el número de miembros activos, no el publicado.

## 4. Salud del negocio

**Señales positivas (indirectas):**
- Cadencia de publicación constante, lo que sugiere operación activa y foco.
- Catálogo de 12 cursos, que indica inversión en contenido.
- Activo de distribución propio (60k seguidores), que reduce el coste de adquisición.
- Margen probablemente alto: el producto es digital y los costes marginales son bajos. Esto es una inferencia general sobre el modelo, no sobre ellos.

**Señales de riesgo o incertidumbre:**
- **Dependencia del fundador**: si el contenido y la marca están en una persona, es un riesgo de continuidad.
- **Retención desconocida**: el número de miembros no dice si la gente se queda. Es el dato más importante para la salud del negocio y no lo ves.
- **Cursos sin completar visibles**: 12 cursos listados no equivale a 12 cursos útiles o terminados.
- **Contador de portada**: suele ser un dato de marketing, no contable.

**Conclusión:** la salud es **indeterminable desde fuera**. Parece un negocio con tracción y operación activa, pero la retención y los ingresos reales son la gran incógnita.

## 5. Cómo les compites

Tu estrategia depende de lo que tú vendes, que no me has dicho. Dicho esto, estas son las palancas típicas:

1. **Nicho más estrecho**: ellos son "automatización" en general. Un nicho concreto (automatización para e-commerce, para agencias, para una herramienta específica) te permite ser la opción obvia para alguien.
2. **Diferenciación por resultado, no por contenido**: si ellos venden acceso a conocimiento, tú puedes vender implementación, plantillas probadas, revisiones de proyectos o acompañamiento.
3. **Precio**: $39/mes es un precio de entrada. Puedes competir con un tier más alto (más práctico, más personalizado) o uno más bajo para captar a quien aún no paga.
4. **Comunidad real**: si su "comunidad" es sobre todo acceso a contenido, una comunidad con actividad real (respuestas del fundador, retos, revisiones) es una ventaja tangible.
5. **Distribución propia**: no compitas con su audiencia de 60k en su terreno. Busca canales donde ellos no estén o donde su fundador no sea la voz principal.

## 6. Qué verificar para afinar el análisis

Estas fuentes te darían datos mucho más fiables que la portada:

- **Tráfico estimado** (Similarweb, Semrush): aproxima el alcance de la web.
- **Histórico de la web** (Wayback Machine): cómo ha cambiado el contador de miembros y el precio en el tiempo. Un contador que sube de forma lineal y constante es distinto de uno estancado.
- **Reseñas y menciones** (Reddit, Trustpilot, grupos de Facebook/Discord, YouTube): busca quejas sobre renovaciones, cancelaciones o calidad de cursos.
- **Empleo** (LinkedIn, portales de empleo): si contratan, indica ingresos suficientes o inversión.
- **Prueba de compra o trial**: si pueden ofrecer una prueba, revisa si hay plan anual, qué incluye y cuánta actividad hay dentro (número de posts, respuestas del fundador, fechas de último mensaje).
- **Engagement del fundador**: 60k seguidores con poca interacción en sus posts sugiere audiencia menos activa de lo que parece.

---

**Siguiente paso:** dime qué vendes tú (precio, nicho, formato) y qué datos tienes sobre tu propio negocio. Con eso puedo comparar posicionamiento, precio y oportunidades de diferenciación de forma concreta.