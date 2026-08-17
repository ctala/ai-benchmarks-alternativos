# Claude Opus 5 (suscripción) — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `claude-opus-5`
- success: True  | final: 6.44 | quality: 8.0
- latency_total: 142.803s | tokens_per_second: 55.5
- input_tokens: 2 | output_tokens: 7926

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# El experimento que la mata en 7 días por menos de US$150

Te lo doy en tres capas, de la más barata a la más cara. Cada una puede matar la idea sola. Si sobrevive las tres, recién ahí tiene sentido hablar de código.

---

## Primero: qué estás apostando en realidad

Tu hipótesis parece una sola, pero son seis. Ordenadas por probabilidad de que te maten (mi apuesta, en orden):

| # | Supuesto | Qué tan frágil |
|---|---|---|
| A1 | El reporte es un dolor top-3 de la agencia (no el #7) | Alto |
| A2 | Lo que existe hoy no les alcanza | **Muy alto** |
| A3 | Cambiarían de herramienta a mitad de año, con 15 clientes ya configurados | **Muy alto** |
| A4 | $200/mes cabe en su presupuesto para esta categoría | Alto |
| A5 | Puedes alcanzarlos con un CAC que soporte $200/mes | Medio |
| A6 | Es construible en 2 meses | Bajo pero letal (te explico abajo) |

Fíjate que "¿pagarían $200?" es A4, el cuarto. La mayoría de la gente diseña el test para A4 y se estrella contra A2 y A3 seis meses después. El experimento tiene que atacar A2 y A3 primero, porque son gratis de testear.

---

## Capa 0 — 3 horas, US$0, escritorio

**Qué haces:** abres 12 pestañas. AgencyAnalytics, DashThis, Whatagraph, Databox, Swydo, ReportGarden, Metrics Watch, Porter, Windsor.ai, Looker Studio (gratis), Klipfolio, Oviond. Anotas para cada uno: precio de entrada, precio del plan que un agencia de 10 clientes usaría, cantidad de integraciones, año de fundación, si tienen funding.

Después, 30 minutos en G2/Capterra leyendo **solo las reseñas de 2 y 3 estrellas** de los tres líderes. Ahí está la lista real de lo que no funciona.

**Criterio de muerte (o de reespecificación):**

> Si hay ≥3 productos establecidos haciendo esto por ≤$200/mes con más integraciones que las que tú puedas construir en 2 meses, **y no puedes escribir en una sola frase el wedge que un dueño de agencia repetiría a otro**, la hipótesis en su forma actual está muerta.

Te adelanto lo que casi seguro vas a encontrar: la categoría existe, está poblada y el precio ancla está entre $60 y $180/mes. Eso no significa "no hay mercado" — significa que tu hipótesis "pagarían $200 por reportes automatizados" ya está respondida por el mercado, y la respuesta es "sí, pero le pagan a otro, y a veces menos". Tu pregunta real pasa a ser otra: *qué específico está roto que estos 12 no arreglan*. Esa sí vale un experimento.

**Costo: $0. Tiempo: 3 horas. Probabilidad de que esto solo te ahorre 2 meses: alta.**

---

## Capa 1 — 7 días, ~US$120, el test que de verdad mata

Si sobreviviste a la Capa 0 con un wedge en una frase, corres esto.

**No construyes nada. No haces landing con "join the waitlist". No mandas encuesta.** Las tres cosas producen falsos positivos y son la razón por la que la gente construye 2 meses y no vende.

Haces un **conserje pre-vendido**: ofreces el resultado, hecho a mano por ti, cobrado hoy.

### La oferta exacta

> "Este mes te hago los reportes de tus clientes. Me das los accesos, te los devuelvo en tu formato en 48 horas. US$200 el mes. Si el primero no te sirve, te devuelvo todo y no seguimos."

Eso es todo. Sin producto, sin demo, sin roadmap. Estás testeando si pagan por **el resultado**, que es lo único que tu software vendería. Si no pagan $200 porque se lo entregues tú a mano, no lo van a pagar porque se lo entregue un servidor.

### Segmento (no lo saltes, define el resultado)

- Agencias de **3 a 15 personas**
- **≥5 clientes en retainer**
- Que corran pauta (si no hay pauta, no hay data que reportar)

Excluye freelancers solos (no tienen $200/mes) y agencias de 40+ (tienen analista interno o BI propio). Si mezclas, tu resultado no significa nada.

### Ejecución día por día

| Día | Qué haces |
|---|---|
| 1 | Lista de 100 agencias del segmento. LinkedIn Sales Navigator (trial gratis), Clutch, Sortlist, directorios locales. Nombre + dueño + email/LinkedIn. |
| 1 | Stripe Payment Link de $200. 10 minutos. |
| 2-4 | Outreach. 100 contactos: LinkedIn DM + email. Meta: 10-12 conversaciones reales. |
| 3-7 | Llamadas de 15 min. En cada una: 4 preguntas + el pedido de plata. |
| 7 | Cuentas tarjetas cobradas. Decides. |

### Las 4 preguntas (antes de pedir plata)

Ninguna es "¿pagarías?". Las respuestas a esa pregunta valen cero.

1. "El cierre de mes pasado: ¿quién armó los reportes, cuántas horas fueron, y con qué herramienta?" → **te da el costo real del status quo**
2. "¿Qué pagas hoy por eso, en herramientas y en horas?" → **te da el techo de tu precio**
3. "¿Cuándo fue la última vez que cambiaste de herramienta de reportes y qué te costó cambiar?" → **testea A3, el switching cost**
4. "Si tuvieras 5 horas libres este mes, ¿en qué las meterías?" → **si no dice 'reportes', tu problema no está en el top 3**

Después: el pedido. Link de Stripe en el chat, ahí mismo, en la llamada.

### Criterios de muerte — explícitos, comprométete antes de empezar

Escribe esto en un papel **hoy**, antes de la primera llamada, o vas a mover el poste:

**Mata la idea si ocurre cualquiera de estas:**

- **Plata:** de ≥10 conversaciones calificadas, **0 o 1 tarjeta cobrada**.
- **Precio:** ≥3 dicen que sí pero **te negocian a $80**. El problema puede ser real; tu precio no. Un negocio a $80/mes con este CAC no aguanta.
- **Costo del status quo:** la mediana de las respuestas a P1+P2 da **menos de ~$100/mes** de costo real (ej.: 2 horas de un asistente). No cabes en el presupuesto, punto.
- **Switching:** la mayoría responde a P3 "nunca cambié" o "cambiamos una vez y fue un infierno". Vender contra la inercia con 15 clientes ya configurados te duplica el ciclo de venta.
- **Prioridad:** en P4 nadie menciona reportes. Estás resolviendo el problema #7.

**Zona gris (2 cobros):** no mata, pero **no justifica 2 meses de construcción**. Extiendes 20 conversaciones más antes de decidir. No empieces a codear en zona gris; es la trampa clásica.

**No muere (3+ cobros de 10-12 conversaciones):** sigues — pero sigues **haciendo el conserje otros 60 días**, no construyendo. Cobrando, ves por dentro qué conectores importan de verdad y qué del reporte les cambia la vida. Ese conocimiento vale más que dos meses de código a ciegas.

### Costo real

| Ítem | US$ |
|---|---|
| Sales Navigator / Apollo (trial o free tier) | 0-99 |
| Herramienta de email o envío manual desde Gmail | 0-40 |
| Stripe | 0 |
| Landing (opcional, ni la necesitas) | 0-19 |
| **Total** | **~$0-150** |
| **Tu tiempo** | ~15-18 horas en 7 días |

Y si cobras 3 × $200, el experimento sale **positivo en caja**.

---

## Capa 2 — 1 hora, US$0: el falsificador del plazo, no de la idea

Aparte, en paralelo, una hora de research que casi nadie hace y que mata tu **plan**, no tu hipótesis:

Revisa los requisitos de acceso a las APIs que necesitas. Meta Marketing API (app review), Google Ads API (developer token: solicitud, revisión, requiere producto funcionando), LinkedIn Ads, TikTok Ads, GA4, GSC, HubSpot.

**Criterio:** si el acceso de producción a dos o más de esas requiere revisión con plazos de semanas y producto ya funcionando, **tu estimación de 2 meses está mal por un factor de 2 a 3**. La idea puede seguir viva; el plan con el que estás decidiendo, no. Y estás tomando la decisión de invertir con ese plan.

---

## Las tres trampas que invalidan este test

1. **Aceptar "sí, me interesa mucho" como señal.** No lo es. Solo cuenta tarjeta cobrada. El entusiasmo es gratis y la gente es amable.
2. **Vender el sueño en vez de la oferta.** Si en la llamada dices "estoy construyendo una herramienta que...", contaminaste el test: te van a responder sobre el futuro, que es barato. La oferta es de este mes, a mano, por $200.
3. **Mover el criterio de muerte después de ver el resultado.** Por eso lo escribes antes. Si cobras 1 de 12 y te encuentras pensando "sí, pero es que el segmento estaba mal", esa frase puede ser cierta — y también es exactamente lo que dice alguien que ya decidió construir igual.

Una nota honesta sobre la potencia estadística: con n=12, tres ventas **no validan** nada. Este diseño solo tiene poder para **matar**, no para confirmar. Que es justo lo que pediste, y es lo correcto: para no gastar 2 meses te basta con no encontrar dolor evidente.

---

## Resumen

| Capa | Tiempo | Costo | Resultado que te hace abandonar |
|---|---|---|---|
| 0 · Escritorio | 3 h | $0 | ≥3 incumbentes a ≤$200 y no tienes wedge de una frase |
| 1 · Conserje pre-vendido | 7 días | $0-150 | ≤1 tarjeta cobrada de 10+ conversaciones · o te negocian a $80 · o el status quo les cuesta <$100/mes |
| 2 · APIs | 1 h | $0 | ≥2 APIs con revisión de semanas → tu plazo de 2 meses es ficción |

Empieza hoy por la Capa 0. Son 3 horas y es la que tiene más probabilidad de ahorrarte los 2 meses.

Si al día 8 tienes 3 agencias pagando $200 por reportes que armaste tú a mano, no solo no falsificaste la hipótesis: tienes $600 de ingreso, tres clientes reales y una lista de conectores priorizada por dinero en vez de por intuición. Ese es el mejor escenario posible, y sigue sin ser permiso para codear dos meses — es permiso para hacer conserje otros dos.