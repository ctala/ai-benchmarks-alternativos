# Claude Fable 5.1 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 6.51 | quality: 8.0
- latency_total: 47.991s | tokens_per_second: 57.6
- input_tokens: 291 | output_tokens: 2764

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Antes del experimento, una corrección: tu hipótesis no es una, son tres apiladas. Cualquiera de las tres te mata.

1. Las agencias pequeñas **sienten** el reporting como un dolor que quieren resolver (no como una molestia que ya toleran).
2. Están dispuestas a **pagar** por quitárselo (y no a resolverlo con Looker Studio gratis o con un junior).
3. Pagan **$200/mes** (no $49, que es donde ya vive AgencyAnalytics/DashThis).

Las landing pages y las encuestas no matan ninguna de las tres. Solo el dinero las mata.

---

## El experimento: pre-venta de un servicio que no existe

Vendes el resultado (el reporte entregado), no el software. Cobras antes de construir nada. Si venden, los reportes los haces tú a mano el primer mes.

### Qué haces, exactamente

**Días 1-2 — Lista y canal (4 horas)**
- Arma una lista de 40 agencias de 3-15 personas. Fuentes: LinkedIn (filtro "marketing agency" + tamaño), directorios de partners de Google/Meta, grupos de Facebook/Slack de agencias, Clutch filtrando por tamaño.
- El contacto debe ser el dueño o el account manager que hoy arma los reportes. No un vendedor.

**Días 2-6 — Outreach (1 hora/día)**
Mensaje corto, sin pitch de software:

> "Hablo con dueños de agencias pequeñas sobre cómo arman los reportes mensuales a clientes. ¿Cuántas horas al mes te lleva eso hoy y cómo lo haces? 15 minutos, no vendo nada todavía."

Objetivo: 15 conversaciones de 15 minutos. Si de 40 mensajes no sacas 15 llamadas, ya tienes una señal (ver abajo).

**En la llamada — pregunta en este orden**
1. ¿Cómo haces los reportes hoy? ¿Quién, cuánto tarda, qué herramientas?
2. ¿Cuánto pagas hoy por eso (herramienta + horas)?
3. ¿Qué intentaste para resolverlo y por qué no funcionó?
4. **Solo si** las respuestas anteriores muestran dolor real: *"Te lo saco de encima. $200/mes, me das accesos, te entrego los reportes de todos tus clientes el día 1 de cada mes, con tu marca. ¿Lo empezamos con el ciclo que viene? Te paso el link de pago ahora."*

El link de pago es un Stripe Payment Link. Lo mandas en la llamada, no después.

**Días 7-10 — Cierre**
Seguimiento único a los que dijeron "déjame pensarlo". Una vez. Si no pagan, es un no.

### Cuánto cuesta y cuánto tarda

| | |
|---|---|
| Dinero | $0 – $60 (Stripe gratis, Calendly gratis, LinkedIn Sales Nav en trial, opcional un dominio) |
| Tu tiempo | ~25 horas repartidas en 10 días |
| Calendario | 10 días hábiles |

Contra 2 meses de construcción, es el 8% del tiempo.

---

## Criterio de muerte (defínelo ahora, antes de empezar)

**La idea está muerta si, de 15 conversaciones reales, menos de 3 pagan $200.**

Esto no es un número optimista. Si has filtrado bien (dueños de agencias pequeñas, hablaste con 15) y la propuesta es "te resuelvo el problema desde ya, sin esperar software", un 20% es el **mínimo** para que un negocio sin marca ni producto tenga alguna oportunidad. Si con el pitch más fácil posible (humano haciéndolo por ti, resultado inmediato) no cierran 3 de 15, el software automático no lo va a arreglar.

**Señales de muerte anticipada**, antes incluso de pedir dinero:
- De 40 mensajes, menos de 8 responden → el tema no les importa lo suficiente para una llamada gratis de 15 minutos. Muerto.
- En la mayoría de llamadas dicen "nos lleva 2-3 horas al mes, lo hace el junior con Looker Studio" → el dolor es pequeño y ya está resuelto por $0. Muerto.
- Más de la mitad ya paga AgencyAnalytics/Whatagraph/DashThis y está conforme → competir con eso a $200 es cuesta arriba. Muerto o pivota a otro segmento.
- Dicen que sí pero piden que sea $50-80 → la hipótesis de precio murió, el problema puede vivir. Decide si el negocio a $60 te interesa.

**Lo que NO cuenta como señal de vida:**
- "Qué buena idea, avísame cuando esté listo"
- Emails en una waitlist
- "Sí, pagaría" sin tarjeta
- Alguien que paga porque es tu amigo o conocido

---

## Si pasa el test (3+ pagan)

No construyas todavía. Haz los reportes a mano un mes para esos 3-5 clientes. Vas a descubrir qué piden realmente, qué fuentes de datos importan, y qué es lo que les hace renovar. Eso es tu spec. Construyes recién en el mes 2, con ingresos y con clientes que ya te pagan.

---

## Un último punto honesto

El riesgo real de tu hipótesis no es "las agencias no quieren reportes automáticos". Lo quieren. El riesgo es que **el mercado ya lo resolvió a $49-$99** y tú entras a $200 sin diferenciación. Las llamadas te van a decir en 48 horas si eso es así. Escucha lo que usan hoy antes de enamorarte de lo que vas a construir.