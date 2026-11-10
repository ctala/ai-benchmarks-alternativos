# Muse Ember — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `meta/muse-ember`
- success: True  | final: 7.39 | quality: 8.0
- latency_total: 17.435s | tokens_per_second: 370.5
- input_tokens: 180 | output_tokens: 6460

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

No hagas landing, no hagas encuesta, no hagas “mándame info”. Eso no puede matar tu hipótesis, solo te va a dar falsos “sí, me interesa”.

El test que mata es brutalmente simple: **intentar venderle el resultado por $200 por adelantado, entregado manualmente por ti, a 60 agencias reales.** Si no te pagan por el resultado, no te van a pagar por el software.

### 1. Escribe hoy tu criterio de muerte

Antes de contactar a nadie, deja esto por escrito. Si se cumple, abandonas la idea tal como está formulada. No bajas a $99, no agregas una feature, no “probemos una landing más”.

**ABANDONAS si después de 60 contactos calificados pasa cualquiera de estas 3:**

1. **<10 llamadas** con el decisor (dueño, socio, director de cuentas)
2. **De esas 10 llamadas, <3 pagan $200**
3. **De los que pagan, <2 entregan datos y mandan el reporte a su cliente en 7 días**

“Me interesa”, “pásame info”, “lo pienso” = **No**. Solo cuenta dinero transferido y uso real.

Si no llegas a 10 llamadas o a 40 mensajes efectivamente entregados, el test es inconcluso por mala ejecución, no por hipótesis muerta. Repites una vez corrigiendo copy/canal.

### 2. El experimento: 7 días, $0, ~12 horas

**Día 0 (3 horas, sin esto no empiezas):**
- ICP: agencia de 3-12 personas, servicios de Paid Media / Social Media, mínimo 3 clientes activos visibles en web/Instagram, con decisor identificable. Prioriza señales de dolor: contratan “analista de reportes”, publican resultados de Meta/Google, tienen muchos clientes y equipo chico.
- Crea el link de pago: Stripe, PayPal o Wise por **$200 USD por adelantado, reembolsable si no sirve**. Pruébalo tú mismo. Sin link que funcione, no hay test.
- Crea 1 ejemplo de 1 página + Loom de 2 min con datos públicos. Nada más.
- Lista de 60. Columnas: Agencia | Decisor | WhatsApp/LinkedIn/Email | Cliente visible | Fecha contacto | Respuesta | Llamada | Pagó | Entregó datos | Lo envió al cliente

**Día 1-4: Outreach 15/día, personalizado en 2 min**
Mensaje inicial (WhatsApp/LinkedIn, incluye precio para filtrar curiosos):

> Hola [Nombre], vi que en [Agencia] gestionan [Cliente/Sector] y publican resultados de Meta Ads. Estoy cerrando una beta para 5 agencias chicas: les automatizo el reporte mensual y en 48h les entrego el reporte listo para enviar al cliente, sin Excel manual. Es beta cerrada, la entrega la hago yo asistida mientras lo automatizo. Son $200/mes, primer mes por adelantado, reembolsable. ¿Te mando un ejemplo de 1 página en un Loom de 2 min para que juzgues?

Follow-up día 3: pegas el Loom.
Follow-up día 6: “Cierro los 5 lugares mañana, ¿te dejo fuera?”

No mandes a freelancers solos, ni a juniors, ni a agencias enterprise.

**Día 4-7: Llamadas de 15 min. Solo decisores.**
No pitchees features. Pregunta: ¿cómo hacen el reporte hoy? ¿cuánto tardan? ¿qué pasa cuando el cliente pide cambios?
Cierra así:

> Tengo un lugar en la beta. Son $200 hoy por este link, te entrego el jueves con tus datos. ¿Lo hacemos?

Si duda, pide tiempo, o pide descuento = No. Anótalo y sigue.

Si paga, en la misma llamada pide acceso/datos y fecha de entrega. Entrega en 48h manualmente (Looker Studio / Sheets). A los 7 días pregunta: ¿se lo mandaste al cliente?

### 3. Costo y tiempo

- **Plata: $0.** LinkedIn/WhatsApp/email gratis. No pagues ads, dominio, ni Apollo para este test.
- **Tiempo: 7 días corridos, 2-3h/día.** 60 investigaciones cortas + 15 envíos/día + llamadas.

### 4. Cómo leer el resultado

**Te mató:** 60 contactos -> 4 llamadas -> 0 pagos. No es problema de código. Es que el dolor no vale $200, o prefieren su Excel gratis, o no confían en dar acceso. Construir 2 meses no arregla eso.

**Te mató también:** 12 llamadas, todos dicen “buenísimo” pero 0 pagan $200. Eso es exactamente para lo que sirve el test: interés verbal = $0.

**Sobrevive (no que valides, que no murió):** 10+ llamadas, 3+ pagan $200, 2+ lo usan con su cliente. Ahí **tampoco** construyas 2 meses. Sirve a esos 3 manualmente 1 mes, cobra el segundo, y recién automatiza lo que se repitió.

Si tu hipótesis era “pagarían $200/mes”, y solo pagan $50 o piden prueba gratis eterna, tu hipótesis murió. Puedes pivotar a otro precio/segmento, pero no cuentes eso como acierto.

Haz el Día 0 hoy.