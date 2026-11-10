# Claude Fable 5.2 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-fable-5.2`
- success: True  | final: 6.56 | quality: 8.0
- latency_total: 33.857s | tokens_per_second: 78.3
- input_tokens: 291 | output_tokens: 2650

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

## Primero: tu hipótesis está mal planteada

Que las agencias pagan por automatizar reportes ya está probado: existen AgencyAnalytics, DashThis, Whatagraph, Swydo y Looker Studio (gratis). Varias cuestan bastante menos de $200; verifica los precios actuales, es una hora de trabajo.

La hipótesis que puede matarte es otra: **"una agencia pequeña me pagaría $200/mes a mí, hoy, existiendo esas alternativas."** Esa es la que hay que testear.

## El experimento: preventa con plata real

**Duración:** 10 días. **Costo:** $0–100 y unas 20–25 horas tuyas.

**Día 0 (2 horas)**
- Escribe los criterios de abandono de abajo y mándaselos a alguien que te los haga cumplir, antes de hablar con nadie.
- Crea un link de pago en Stripe: $200, primer mes, 100% reembolsable.
- Arma a mano un reporte de ejemplo (PDF o Loom de 2 minutos). Sin código.

**Días 1–7: contacto**
- Escribe a 50 dueños de agencias de 2 a 15 personas por LinkedIn, email frío y tu red. Tienen que ser dueños, no empleados: el que no decide el gasto no sirve.
- Meta: 15 llamadas de 20 minutos.

**En cada llamada**
1. Pregunta cómo hacen los reportes hoy, cuántas horas les toma, qué herramienta usan y cuánto pagan. No menciones tu idea todavía.
2. Muestra el ejemplo.
3. Cierra: *"Cuesta $200/mes. Todavía no está construida: las primeras semanas te hago los reportes yo a mano. Si pagas hoy entras como cliente fundador y te devuelvo todo si no te sirve. ¿Te mando el link?"*
4. Si dice que no, pregunta por qué y anota la respuesta textual.

## Criterios de abandono

| Resultado | Decisión |
|---|---|
| Menos de 8 de 50 aceptan la llamada | El problema no duele lo suficiente para darte 20 minutos. Mala señal. |
| **0–1 pagos de 15 llamadas** | **Hipótesis muerta. No construyas.** |
| 2 pagos | Zona gris. Haz 10 llamadas más antes de escribir código. |
| 3 o más pagos | Sigue viva. Entrégales a mano y construye solo lo que ya estás haciendo manualmente. |

Señal de muerte adicional: si más de la mitad ya usa una herramienta y está conforme, el mercado está servido. Abandona o cambia de ángulo.

## Qué no cuenta como señal

- "Qué buena idea."
- "Avísame cuando esté lista."
- Inscripciones a una lista de espera.
- "Lo pagaría seguro."

Solo cuenta la plata en Stripe. Las opiniones de gente amable son el dato más engañoso que existe.

## Lo que el test no te dice

- **Falso negativo:** un "no" puede ser culpa de tu pitch o de tu canal, no de la idea. Por eso anotas las objeciones textuales. Si 10 de 15 dicen "ya uso X y me basta", es la idea. Si dicen "no entendí qué hace", es el pitch.
- **Retención:** pagar el primer mes no garantiza el mes 6. Eso lo descubres en la fase manual, que también cuesta mucho menos que 2 meses de desarrollo.

En el peor caso pierdes 10 días y $100 en vez de 2 meses. Si alguien paga y decides no seguir, le devuelves la plata y listo.