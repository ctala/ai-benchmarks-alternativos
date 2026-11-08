# Grok 4.7 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `x-ai/grok-4.7`
- success: True  | final: 6.7 | quality: 8.0
- latency_total: 84.473s | tokens_per_second: 43.2
- input_tokens: 1409 | output_tokens: 3653

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

La hipótesis muere si nadie te paga. No si “les interesa”.

**Test:** preventa reembolsable del producto real, a $200/mes, sin construirlo.  
**Costo:** $0–30. **Tiempo:** 7 días, ~15 horas. **Qué mata la idea:** 0 pagos de 15 agencias calificadas.

Si no pagan por el resultado con reembolso total, no van a pagar por un software que todavía no existe. No construyas para descubrir eso.

### A quién le escribís
Una sola playa: agencias de 2–20 personas, en un país y un idioma, que ya mandan reportes mensuales a clientes. No freelancers sueltos, no consultoras grandes, no amigos.

Califica solo si las tres son sí:
- Manda reportes recurrentes a **≥3 clientes**.
- Hoy lo hace a mano (Slides, Sheets, screenshots, PDF, Looker exportado).
- Habla el que decide pagar.

“Interesante” de alguien que no tiene ese dolor no cuenta. Tampoco un no de alguien que no califica.

### Qué ofrecés (el mismo día 1)
Un Google Doc o 4 capturas hechas en Slides, más un reporte de ejemplo con datos inventados. Nada de código.

Texto de la oferta, fijo:

> Reporte mensual de performance para tus clientes, con tu marca, listo para enviar. $200/mes por la agencia, hasta 10 clientes. Pagás hoy para reservar uno de 5 cupos. Si en 14 días no te entrego el primer reporte o no te sirve, te devuelvo el 100%. Sin contrato.

Precio inamovible. Si ofrecen $50, es un **no** a esta hipótesis. No negocies: anotá el número y seguí.

Cuenta como sí solo esto: plata cobrada, o tarjeta cargada con fecha de cobro escrita y aceptada.  
“Avisame cuando esté”, “pasame propuesta” y “sí, después te pago” son **no**.

### Qué hacés, día por día
**Día 1 (6 h, $0).** Armá el one-pager, el reporte de ejemplo y un link de pago (Stripe, Mercado Pago o transferencia). Lista de 50 agencias: dueño o director, LinkedIn, web, Instagram o mail público. Google y Clutch alcanzan.

**Días 2–5 (8 h).** 50 mensajes, uno por uno, no campaña. Precio y reembolso en el primer mensaje. Pedí una llamada de 15 minutos solo para cobrar, no para “entender el problema”. En la llamada: repetí la oferta y mandá el link antes de colgar. Una pregunta de calificación y después el cierre. Nada de demo de features que no existen.

Mensaje:

> Vi que [agencia] le reporta performance a sus clientes. Estoy armando una herramienta que genera ese reporte mensual, con su marca, listo para enviar. $200/mes, hasta 10 clientes. Tengo 5 cupos: se paga hoy y en 14 días está el primero. Si no sirve, devolución total. ¿Lo ves 15 minutos esta semana o te mando el link y lo cerramos por acá?

**Días 6–7 (2 h).** Un solo follow-up a quien no respondió. Cerrá el conteo. No alargues “para ver si aparece alguno más”.

### Regla de abandono (escribilá antes de mandar el primer mensaje)
Después de **50 contactos** y **15 conversaciones con calificados**:

- **0 pagos → abandoná.** No bajes el precio, no agregues features, no empieces el build de 2 meses.
- 1 pago → no construyas todavía. Es ruido, no un mercado.
- Recién 3+ pagos de calificados justifican un segundo test (y ese segundo test sigue sin ser 2 meses de producto).

También abandoná si en 15 calificados la plata que ofrecen no llega a $200 en ninguno. La hipótesis era $200, no “algo de interés”.

### Qué no hacer
No encuesta. No landing con emails. No ads. No “¿cuánto pagarías?”. No MVP. Un clic o un “me copa” no puede matar ni salvar esto. La plata sí.