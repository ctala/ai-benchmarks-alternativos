# Claude Opus 5.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.67 | quality: 8.0
- latency_total: 35.287s | tokens_per_second: 85.8
- input_tokens: 291 | output_tokens: 3027

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# Experimento para matar la hipótesis en 10 días por menos de $50

## Primero, descompón la hipótesis

Tu frase contiene **cuatro supuestos**, y cualquiera puede matarla:

1. **Dolor:** las agencias pequeñas pierden tiempo o plata relevante haciendo reportes.
2. **Hueco:** las herramientas actuales no lo resuelven. Ya existen AgencyAnalytics, DashThis, Whatagraph, Swydo y Looker Studio, que es gratis.
3. **Precio:** pagarían **$200/mes**, no $30.
4. **Acceso:** puedes llegar a ellas de forma barata.

El supuesto más peligroso suele ser el **#2**, no el #1. El dolor de los reportes es real y conocido, y por eso ya hay competidores. Tu experimento tiene que atacar primero lo que más probablemente sea falso.

---

## Fase 0: matar desde el escritorio (2 horas, $0)

Antes de hablar con nadie:

- Revisa precios y reviews de 3 estrellas en G2 y Capterra de AgencyAnalytics, DashThis y Whatagraph. Ahí la gente dice qué le falta.
- Busca en r/agency, r/PPC y grupos de Facebook de agencias quejas sobre reportes.

**Criterio de muerte:** si no encuentras **ninguna queja recurrente y específica** que los competidores no resuelvan, ya tienes una señal fuerte en contra. Sigue igual a la Fase 1, pero ahora con una pregunta concreta: *¿qué tendría que ser distinto para que alguien cambie?*

Antes de seguir, define "agencia pequeña" por escrito. Por ejemplo: 2 a 15 personas, 5 a 30 clientes con retainer mensual. Si no lo defines, después vas a reinterpretar los resultados.

---

## Fase 1: outreach directo (días 1 a 4, $0)

**Qué haces:** escribe a **60 dueños de agencias pequeñas** por LinkedIn o email. Puedes sacar los contactos de Clutch.co, Google Maps ("agencia de marketing" + ciudad) o el free tier de Apollo.

**Mensaje (sin pitch):**
> "Hola [nombre], estoy investigando cómo las agencias de [X] personas manejan los reportes mensuales a clientes. ¿Me darías 15 minutos esta semana? No vendo nada, solo quiero entender el proceso."

**Métrica:** tasa de respuesta y de llamadas agendadas.

---

## Fase 2: las llamadas (días 3 a 8, $0)

Usa preguntas tipo *The Mom Test*, sobre el pasado y en concreto. Nada de hipotéticos:

- "¿Cuántas horas le dedicó tu equipo a reportes **el mes pasado**?"
- "¿Qué herramienta usan hoy? ¿Cuánto pagan?"
- "¿Cuándo fue la última vez que intentaste solucionar esto? ¿Qué probaste?"
- "¿Alguna vez perdiste un cliente o tuviste un problema por un reporte?"

**Prohibido preguntar** "¿pagarías por...?" o "¿te interesaría...?". Las respuestas a eso no valen nada.

**Al final de cada llamada en que detectes dolor, haz la pregunta que realmente prueba la hipótesis:**

> "Estoy armando algo para esto. Busco 5 agencias fundadoras: **$200 el primer mes, pagado hoy**, y yo personalmente te dejo los reportes de todos tus clientes automatizados en 2 semanas. Si no te sirve, te devuelvo la plata."

Mándale un **link de pago de Stripe**, que es gratis de crear. Si hay resistencia, ofrece una alternativa: **depósito de $100 reembolsable** para reservar el cupo.

Esto es un *concierge MVP*: si alguien paga, haces el trabajo a mano o con Looker Studio, Zapier y plantillas. Así aprendes exactamente qué construir y no gastas 2 meses a ciegas.

---

## Criterios de muerte (escríbelos antes de empezar y no los toques)

| Etapa | Resultado que te hace **abandonar** | Qué mata |
|---|---|---|
| Outreach | < 8 llamadas de 60 contactos | El dolor no es urgente, o no puedes acceder al segmento |
| Llamadas | < 50% gasta **más de 5 h/mes** en reportes | El dolor no existe a esta escala |
| Llamadas | La mayoría ya usa una herramienta **y está conforme** | No hay hueco: el mercado ya lo resolvió |
| Pago | **0 o 1 pagos** tras ~12 llamadas | La disposición a pagar $200 es falsa |
| Pago | Pagan solo si bajas a ~$50 | El negocio a $200 está muerto (quizás no la idea) |

**Señal para seguir:** **3 o más agencias pagan** $200 o dejan un depósito. Y no solo "me encantaría".

---

## Resumen

| | |
|---|---|
| **Costo** | $0 a $50 (Stripe, Calendly y Apollo tienen versión gratis) |
| **Tiempo** | 8 a 10 días, unas 15 a 20 horas tuyas |
| **Ahorro potencial** | 2 meses de desarrollo |

## Trampas que invalidan el experimento

- **Contar el entusiasmo como dato.** "Qué buena idea, avísame cuando esté" equivale a un **no**.
- **Entrevistar a amigos o conocidos.** Te van a mentir por cariño.
- **Mover la vara al final.** Si obtienes 1 pago y piensas "bueno, pero fue muy buena la conversación...", ya perdiste la disciplina. El criterio quedó escrito.
- **Confundir qué murió.** Un "no" puede matar el *precio*, el *segmento* (quizás las agencias de 20 a 50 personas sí pagarían) o la *idea*. Anota cuál de los tres en cada caso.

Si al día 10 no tienes 3 pagos, la respuesta probablemente no es "construir para convencerlos". Ese resultado es el experimento haciendo su trabajo.