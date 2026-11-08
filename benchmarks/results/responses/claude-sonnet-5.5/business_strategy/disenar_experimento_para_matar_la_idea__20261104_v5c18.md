# Claude Sonnet 5.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 6.93 | quality: 8.0
- latency_total: 32.196s | tokens_per_second: 106.5
- input_tokens: 291 | output_tokens: 3430

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# Experimento: preventa concierge en 10 días

## Antes de empezar: dónde está el riesgo real

"¿Pagarían por automatizar reportes?" probablemente sea **cierto**, porque ya hay AgencyAnalytics, DashThis, Whatagraph, Swydo y Databox. El riesgo está en otras tres cosas:

1. **Precio:** esos competidores cobran entre $30 y $150. ¿Pagan $200 *a ti*?
2. **Switching:** si ya usan algo "suficientemente bueno", no cambian.
3. **Dolor:** puede que el reporte sea una molestia, no un dolor que justifique $200/mes.

El experimento ataca esos tres, no el "me interesa".

## Qué haces

**Días 1-2: lista y outreach (costo ~$0-50)**
- Arma una lista de 150 dueños o directores de agencias de 2-15 personas (Clutch, LinkedIn, Google Maps, comunidades de Slack/Facebook de agencias).
- Mensaje de 3 líneas, sin pitch: *"Estoy investigando cómo las agencias arman reportes a clientes. ¿15 min para contarme tu proceso? No vendo nada."*
- Meta: 20 conversaciones con gente calificada (que hoy manda reportes mensuales a 5 o más clientes). Si no consigues 20 en 7 días, eso ya es dato sobre qué tan alcanzable es el segmento.

**Días 3-9: llamadas de 20 min**

Cada llamada tiene dos partes.

*Parte 1, conducta pasada (no opiniones):*
- "Muéstrame/cuéntame el último reporte que armaste. ¿Cuánto tardó?"
- "¿Qué herramienta usas? ¿Cuánto pagas? ¿Qué probaste y dejaste? ¿Por qué?"
- "¿Cuándo fue la última vez que buscaste una solución?"

*Parte 2, la oferta que puede fallar:*
> "Estoy armando esto. Te propongo: pagas **$200 hoy** (reembolsable 100% en 30 días) y durante el primer mes yo te genero los reportes de tus clientes, a mano si hace falta. Después queda automatizado a $200/mes."

Sin descuento ni ancla baja. Si dudan del precio, pregunta: "¿a qué precio sería una obviedad? ¿y a cuál dirías que no, ni regalado?"

**Qué cuenta como compromiso real (de más a menos fuerte):**
1. Pagan con tarjeta.
2. Te dan acceso a sus cuentas (GA, Meta Ads, etc.) y firman que pagan si el reporte sale bien.
3. Nada más. "Mándame info" y "suena genial" valen cero.

## Costo y tiempo

| Concepto | Costo |
|---|---|
| Lista y herramientas de outreach | $0-50 |
| Stripe link / Calendly | $0 |
| Tu tiempo | ~25-30 horas en 10 días |
| **Total en plata** | **<$100** |

Si quieres una segunda señal en paralelo: landing con precio visible y botón de pago, más $150 en ads. Opcional; el outreach directo es más informativo.

## Criterios de muerte (escríbelos hoy)

Sobre 20 conversaciones calificadas:

| Resultado | Decisión |
|---|---|
| **0-1 pagan** a $200 | **Hipótesis muerta.** No construyas. |
| **2-3 pagan** | Zona gris. Mira *quiénes* pagaron: si comparten perfil (nicho, tamaño, herramienta actual), reformula para ese segmento y repite. Si son dispersos, mátala. |
| **4+ pagan** | Sobrevivió al primer test. Construye el MVP mínimo, solo para esos clientes. |

**Señales de muerte adicionales, aunque alguien pague:**
- Menos de 40% dedica más de 3 horas al mes por cliente a reportes: no hay dolor.
- Más de 60% usa una herramienta actual con la que dice estar "bien": no hay hueco.
- El precio que dicen "obvio" está sistemáticamente en $50-80: tu hipótesis de $200 está muerta, y un negocio a $60 es otro negocio (otro CAC, otra escala).
- No logras 20 llamadas en 7 días con 150 contactos: el canal de adquisición es un problema serio.

## Cómo no engañarte

- **No cuentan:** amigos, conocidos, gente que "quiere ayudarte", ni elogios.
- **Sesgo de selección:** quien acepta una llamada ya tiene más dolor que el promedio. Si incluso ellos no pagan, la evidencia es contundente.
- **Sesgo de cortesía:** por eso exiges dinero o acceso a datos, no opiniones.
- **Límite del test:** con n=20 puedes *matar* la hipótesis con confianza, pero no *confirmarla*. Pasar el test solo te autoriza el siguiente experimento: entregar el servicio a mano durante 2-3 meses y ver si renuevan.

## Costo de equivocarte

Test: ~$100 y 10 días. Construir: 2 meses de tu vida. Aunque el test tenga solo 70% de capacidad de detectar una mala idea, sigue siendo muy buena apuesta.

Si de los 20 nadie paga, habrás ahorrado 2 meses. Si 4 o más pagan, ya tienes tus primeros clientes y sabes exactamente qué construir.