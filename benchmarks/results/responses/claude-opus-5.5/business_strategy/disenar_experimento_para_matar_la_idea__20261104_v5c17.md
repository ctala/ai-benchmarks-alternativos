# Claude Opus 5.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.62 | quality: 8.0
- latency_total: 45.253s | tokens_per_second: 86.3
- input_tokens: 291 | output_tokens: 3906

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# Experimento para matar la hipótesis: preventa con dinero real

**Costo:** $0–60. **Duración:** 10 días hábiles (~25 horas tuyas). **Criterio de muerte:** menos de 2 pagos reales de 100 agencias contactadas.

## Primero: qué parte de la hipótesis puede matarte

Tu hipótesis tiene tres afirmaciones:

1. **A las agencias pequeñas les duele hacer reportes.** Probablemente cierto. Por eso no vale la pena testearlo.
2. **Pagarían por automatizarlo.** También probablemente cierto: AgencyAnalytics, DashThis, Whatagraph y Swydo existen y facturan.
3. **Te pagarían $200/mes a ti, existiendo esas opciones y Looker Studio gratis.** Esta es la que puede matarte.

Así que el experimento no pregunta "¿te duele?". Pregunta: **"¿me das $200 hoy?"**

## Paso 0: investigación de escritorio (2 horas, $0)

Antes de hablar con nadie:

- Anota precios y planes de 4 o 5 competidores.
- Lee reseñas de 1 a 3 estrellas en G2 y Capterra. Ahí está lo que la gente odia de lo que ya existe.
- Escribe en una frase por qué alguien te elegiría a ti.

**Señal de muerte temprana:** si no puedes escribir esa frase, tu hipótesis real es "quiero clonar AgencyAnalytics". Eso ya es información.

## Paso 1: escribe y compromete los criterios de muerte (30 min, día 1)

Escríbelos **antes** de hablar con nadie. Mándaselos a un amigo con la instrucción "si no cumplo esto y sigo igual, recuérdamelo". Esto es lo más importante del experimento. Sin esto, vas a reinterpretar los resultados a tu favor.

| Etapa | Muere si... |
|---|---|
| Respuestas positivas al outreach | Menos de 5 de 100 (<5%) |
| En las llamadas: dolor actual | Más del 70% dice que ya está conforme con su herramienta o gasta menos de 1 h por cliente al mes en reportes |
| **Pagos reales a $200** | **0 o 1 pago** |
| Zona ambigua | 2 pagos: repites con otros 50 contactos, sin cambiar precio ni oferta |
| Sigue adelante | 3 o más pagos, y aun así empiezas en modo concierge, no con 2 meses de código |

**Definición de "pago":** dinero en tu Stripe. No es "me interesa", no es "avísame cuando esté", no es una carta de intención. Solo cuenta el dinero.

## Paso 2: arma la lista (días 1–2, $0)

- **100 dueños o directores de agencias** de 2 a 15 personas, con clientes en retainer mensual. Si no tienen retainer, no hay reportes recurrentes.
- **Fuentes:** Clutch.co, Google Maps ("agencia de marketing" + ciudad), LinkedIn (la prueba gratis de Sales Navigator sirve) y grupos de dueños de agencias.
- **Excluye** amigos, conocidos y cualquiera que te deba un favor. Contaminan el resultado.

## Paso 3: vende algo que no existe (días 2–5)

No ofrezcas una entrevista: ofrece el servicio directamente. Mensaje corto, por LinkedIn o email:

> Hola [nombre], estoy armando un servicio para agencias como [agencia]: te entrego los reportes mensuales de tus clientes listos para enviar, sin que tu equipo toque una planilla.
>
> Estoy tomando 5 agencias fundadoras a $200/mes. ¿Te sirve una llamada de 15 min esta semana para ver si encaja?

Herramientas: Gmail, LinkedIn y una landing en Carrd ($19) si quieres algo que linkear. Opcional. **Costo total: $0–60.**

## Paso 4: la llamada de 15–20 minutos (días 3–8)

**Primeros 10 minutos: comportamiento pasado, no opiniones** (método *The Mom Test*):

- "¿Cómo hiciste los reportes del mes pasado? Muéstrame."
- "¿Cuántas horas te tomó? ¿Quién lo hizo?"
- "¿Qué herramientas has probado? ¿Por qué dejaste las que dejaste?"
- "¿Cuánto pagas hoy por esto?"

**Últimos 5 minutos: el cierre.**

> "Te propongo esto: el primer mes son $200, yo me encargo de los reportes de 3 de tus clientes y te los entrego el día X. Si no te sirven, te devuelvo la plata. ¿Te mando el link de pago ahora?"

Mándalo en la llamada. "Lo pienso y te aviso" cuenta como un no.

**Si alguien paga, haces los reportes a mano** (Looker Studio, Zapier, tu tiempo). Eso es el concierge MVP: validas sin escribir una línea de código y aprendes qué hay que automatizar de verdad.

## Paso 5: seguimiento y conteo (días 6–10)

Un solo follow-up a quienes no respondieron. El día 10 cuentas contra la tabla del Paso 1 y ejecutas lo que dice. Sin negociar contigo mismo.

## Trampas que vas a querer cometer

1. **Contar halagos como datos.** "¡Qué buena idea!" vale $0.
2. **Bajar el precio en el momento.** Si te dicen "a $50 sí", no validaste nada. Es otra hipótesis con otra matemática: necesitas 4 veces más clientes para el mismo ingreso, con el mismo costo de adquirirlos.
3. **Culpar al mensaje.** Si la respuesta está bajo el 5%, puedes reescribir el copy **una sola vez** y mandarlo a otros 50. Si vuelve a fallar, el problema no es el copy.
4. **"Es que necesitan ver el producto."** Las agencias le compran servicios a gente que no conocen todo el tiempo. Si nadie paga por el resultado entregado a mano, el software no lo va a arreglar.

## Lo que este experimento no te dice

No mide **retención**: si te pagan el mes 1 pero cancelan el mes 3 porque Looker Studio "ya es suficiente". Si pasas el test, mantén a esos 3 o más clientes en concierge 2 o 3 meses mientras construyes. Si cancelan, tienes tu segunda señal de muerte, y la descubriste antes de invertir los 2 meses completos.

**En resumen:** 10 días y menos de $60 para saber si vale la pena invertir 2 meses. Y si alguien paga, ya tienes tus primeros clientes.