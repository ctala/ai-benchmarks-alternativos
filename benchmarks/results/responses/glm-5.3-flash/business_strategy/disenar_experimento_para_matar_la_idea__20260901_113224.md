# GLM 5.3 Flash — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `z-ai/glm-5.3-flash`
- success: True  | final: 7.49 | quality: 8.0
- latency_total: 62.071s | tokens_per_second: 130.6
- input_tokens: 194 | output_tokens: 8105

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

# El experimento: véndelo antes de que exista, pidiendo dinero real

Primero, el principio de diseño: las encuestas y los "¿pagarías $200/mes?" **no pueden matar tu hipótesis**, porque la gente miente sobre hipotéticos (casi siempre por amabilidad, sin darse cuenta). Los clicks en una landing tampoco: un click no cuesta nada. Lo único que mata concluyentemente es pedirle dinero a desconocidos. Si no te lo dan, tienes tu respuesta.

---

## Qué haces, exactamente

**Días 1-2: arma la oferta (~$50)**
- Landing de 1 página (Carrd $19/año + dominio $12): qué hace, para quién, **precio de $200/mes visible**, botón "Reservar precio fundador".
- Link de Stripe para un **depósito reembolsable de $50** que congela $200/mes de por vida + primer mes gratis al lanzar. Siendo transparente: "producto en desarrollo, lanzamiento en [fecha], depósito 100% reembolsable".
- Mockup en Figma o un PDF de reporte de ejemplo. Máximo 3 horas. Nada más.

**Días 2-3: lista de 150 agencias ICP**
- ICP estricto: 3-20 empleados, manejan paid media/SEO para 5+ clientes, ya envían reportes mensuales.
- Apollo ($49, un mes) o LinkedIn + Hunter.
- **Cero amigos o conocidos en la lista.** Solo desconocidos.

**Días 3-14: outreach (1-2 h/día)**
- 15-20 contactos/día, personalizados, email + LinkedIn, 2 seguimientos.
- Apertura: *"Vi que [agencia] lleva cuentas de [canal]. ¿Cómo generan hoy los reportes mensuales de sus clientes? Estamos armando algo que automatiza eso completo."*

**Días 8-18: llamadas de 15 min**
- 5 min: cómo lo hacen hoy (horas/mes, quién lo hace, qué herramientas, **cuánto pagan hoy**).
- 5 min: muestras el mockup.
- 5 min: cierre con dinero: *"¿Te reservo el precio fundador con el depósito de $50?"*

**Día 18-21: decisión.** Escribe los criterios de abajo **antes de empezar** y mándatelos por email. A mitad de experimento tu yo motivado va a querer mover la meta. No dejes que lo haga.

---

## Criterios de muerte (acordados antes de ver un solo dato)

| Métrica | Mata la hipótesis si... |
|---|---|
| Respuestas (de 150, con 2 follow-ups) | <5 incluso tras iterar el pitch **una sola vez** |
| Llamadas held con ICP | <3 → no puedes concluir; una iteración más de canal/oferta |
| Aceptación del precio | 0 de ≥6 llamadas held aceptan $200 ("con $50-80 sí") |
| **Dinero real** | **0 depósitos tras ≥6 llamadas held → MUERTA. Regla principal.** |

- *"Me interesa, avísame cuando salga"* cuenta como **NO**. Solo el dinero cuenta.
- **Pasa si:** ≥2 depósitos de ≤150 contactos. Y aun así no construyas software: dales el servicio **manual** un mes a $200 y automatiza únicamente lo que ya estés haciendo a mano.

---

## Costo y tiempo

- **Plata:** ~$100. (Opcional: +$200 en ads solo si al día 10 el outreach no da respuestas.)
- **Tiempo:** 2-3 semanas, 1-2 h/día. vs. tus 2 meses de build.
- **Si muere:** te quedas con la lista, el pitch y todas las respuestas de discovery — la materia prima de tu siguiente hipótesis. No pierdes nada.

---

## Las 2 trampas que van a intentar engañarte

1. **El sí verbal.** Van a escuchar "suena genial" varias veces. No es dato. Si aceptas cualquier cosa que no sea dinero, este experimento no puede matar nada.
2. **Reescribir la hipótesis para no perderla.** Tendrás 6 llamadas buenas, 0 depósitos, y pensarás "es que el depósito asusta, con prueba gratis sí". Eso ya no es tu hipótesis — es otra. La tuya dice **$200/mes**. Si $200 no se vende, está muerta (aunque exista otro negocio a $79, y eso es otra conversación).

---

## La pregunta que probablemente te mate (y está bien que lo haga)

En cada llamada: *"¿Qué usas hoy para esto y cuánto te cuesta?"* Ya existen AgencyAnalytics, Whatagraph, DashThis y Swydo a $49-150, y Looker Studio gratis. Si el 60%+ ya lo resuelve por menos de $100 y no logras articular en el momento por qué pagarían el doble, morirás por falta de diferenciación, no de dolor. Descubrirlo ahora te cuesta $100; descubrirlo en 2 meses te cuesta los 2 meses.