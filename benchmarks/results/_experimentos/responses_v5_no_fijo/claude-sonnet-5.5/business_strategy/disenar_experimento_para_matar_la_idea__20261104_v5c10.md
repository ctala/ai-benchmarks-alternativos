# Claude Sonnet 5.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 6.92 | quality: 8.0
- latency_total: 34.802s | tokens_per_second: 106.8
- input_tokens: 291 | output_tokens: 3716

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# Experimento: preventa de un servicio "concierge" a $200/mes

**Idea central:** no midas si les gusta la idea, mide si **pagan** por ella antes de que exista. Lo que cuenta es dinero, no opiniones. Los "suena genial" no cuentan.

## Qué estás testeando realmente

Tu hipótesis tiene tres apuestas que pueden morir por separado:

1. **Dolor:** hacer reportes les cuesta tiempo o dinero real.
2. **Alternativas:** las herramientas actuales (Looker Studio gratis, AgencyAnalytics, DashThis, Whatagraph, Swydo) no lo resuelven.
3. **Precio:** $200/mes es alto frente a esas alternativas, que suelen costar $40-$150. Este es probablemente tu punto más débil.

## Paso 0: Prueba de 2 horas (día 1, costo $0)

Mira los precios y reviews de 5 competidores y busca en Reddit, G2 y Capterra qué se quejan de ellos.

**Mata la idea si:** no puedes articular en una frase por qué alguien pagaría 2-4 veces más que por DashThis o AgencyAnalytics. Si tu única respuesta es "es más fácil", todavía no tienes una hipótesis, tienes una preferencia.

## El experimento (10 días, ~25 horas tuyas)

### Días 1-2: Preparación
- Arma una lista de **150 agencias pequeñas** (2-15 personas, que atiendan 5 o más clientes recurrentes). Fuentes: LinkedIn, Clutch, Google Maps, grupos de Facebook de agencias.
- Crea una página simple (Carrd, $19/año) con la oferta y un **link de pago de Stripe**.
- **Oferta:** *"Programa piloto: yo me encargo de que tus reportes mensuales a clientes salgan automáticos. $200/mes, primer mes con garantía de devolución total. Cupos limitados: 5."*

### Días 3-6: Outreach
Mensaje a los dueños, por email o LinkedIn:

> "Hola [nombre], estoy buscando 5 agencias para un piloto en el que me encargo de automatizar los reportes mensuales a sus clientes (GA4, Meta, Google Ads → PDF/dashboard con su marca). $200/mes, con devolución completa si no les ahorra tiempo. ¿Te hago 2 preguntas rápidas para ver si encajas?"

### Días 4-8: Llamadas de 15 minutos
Haz todas las que consigas. Pregunta por **comportamiento pasado**, no por futuro:

- ¿Cuándo fue la última vez que hiciste reportes? ¿Cuánto tardaste en total?
- ¿Qué herramienta usas hoy y cuánto pagas?
- ¿Qué pasó la última vez que buscaste una alternativa?
- ¿Quién paga ese tiempo hoy: tú, un junior, el cliente?

Luego haz **el cierre**: *"Si te lo dejo funcionando en 7 días, ¿lo activamos hoy?"* y manda el link de pago.

### Días 8-10: Entrega mínima
A quien pague, entrégale el servicio **a mano** (Looker Studio + Sheets + Zapier + tu tiempo). No escribas código todavía.

## Costo

| Concepto | Costo |
|---|---|
| Carrd + dominio | ~$30 |
| Stripe | $0 hasta cobrar |
| Herramientas de outreach (planes gratis) | $0-$50 |
| **Total** | **$30-$80** |

## Criterios de abandono (escríbelos hoy, antes de empezar)

Un "calificado" es una agencia con 5 o más clientes recurrentes que hace reportes mensuales.

| Resultado (sobre ~15 llamadas calificadas) | Decisión |
|---|---|
| **0 pagos** | **Abandona.** Si la tasa real fuera 20%, ver 0 de 15 tiene ~3% de probabilidad. |
| 1-2 pagos, y las objeciones son de precio | Repite el test a $79-99. Si sigues sin pagos, abandona. |
| 1-2 pagos, y las objeciones son "ya uso X" | Probablemente el nicho está saturado. Abandona o cambia de segmento. |
| **3 o más pagos** | Sigue. Construye solo lo que hiciste a mano. |

**Señales de muerte temprana** (para parar antes de las 15 llamadas):
- En las primeras 8 llamadas, 6 o más dicen que su solución actual "ya funciona".
- Los reportes les toman menos de 5 horas/mes en total. A $200/mes, el ahorro no justifica el cambio.
- Nadie puede nombrar la última vez que buscó una alternativa. Eso significa que el dolor no es activo.
- Con menos de 3% de respuesta tras 150 mensajes, el canal o el mensaje están mal. Prueba otro antes de concluir que no hay demanda.

## Reglas para que el test pueda fallar de verdad

1. **Solo cuenta el dinero.** "Me interesa", "mándame info" y "suena bien" son un cero.
2. **Nada de amigos ni conocidos.** Inflan los resultados.
3. **No cambies la oferta a mitad del test** si no es para resetearlo. Si ajustas el precio, empieza otra ronda.
4. **Si no pagan, pide un compromiso más barato:** acceso a sus datos reales o 30 minutos de onboarding con sus clientes. Si ni eso, el interés es cortesía.
5. **Fija tu número hoy.** Si después de ver los resultados te encuentras justificando por qué 1 pago "es una buena señal", estás racionalizando.

## Qué no te dice este test

No valida que puedas construirlo a escala ni que retengan después del mes 3. Pero si no pasa esta prueba, esas preguntas ya no importan. Cuesta $50 y 10 días, contra 2 meses de tu vida.