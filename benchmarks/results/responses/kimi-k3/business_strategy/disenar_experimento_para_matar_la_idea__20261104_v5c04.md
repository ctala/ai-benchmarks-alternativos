# Kimi K3 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `moonshotai/kimi-k3`
- success: True  | final: 6.5 | quality: 8.0
- latency_total: 105.522s | tokens_per_second: 47.6
- input_tokens: 307 | output_tokens: 5023

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Tu hipótesis tiene tres partes: (1) las agencias pequeñas sufren con los reportes, (2) sufren *lo suficiente* para pagar, (3) pagarían **$200/mes**. La parte más frágil es la 3. El experimento tiene que atacar ahí.

## La lógica del test de muerte

Para matar una hipótesis de forma concluyente, el test debe ser **fácil de pasar**: precio rebajado, prospectos elegidos a dedo, oferta agresiva. Si la versión fácil falla, la versión real ($200/mes, mercado frío) está muerta con certeza. Si haces el test difícil y falla, no aprendiste nada: nunca sabrás si fue la idea o tu ejecución.

Y la única señal falsable es **dinero que cambia de manos**. "Suena interesante", "avísame cuando salga", un like en LinkedIn: nada de eso puede matar tu hipótesis porque no cuesta nada decirlo.

## El experimento: preventa de algo que no existe

**Fase 0 — Muerte gratis en 48 horas (costo: $0)**

Antes de cualquier pitch, habla con 5-8 dueños de agencias pequeñas (2-15 personas) y haz solo preguntas sobre comportamiento pasado, no opiniones:

- "Cuéntame cómo hiciste el último reporte de un cliente, paso a paso."
- "¿Cuántas horas al mes se van en eso? ¿Quién las hace?"
- "¿Qué herramientas pagas hoy para esto?"

Tu hipótesis predice algo observable hoy: si alguien pagaría $200/mes, hoy está *perdiendo* más de $200/mes en horas o pagando herramientas. **Si la mayoría dedica <3-4 horas/mes y paga $0 (Looker Studio gratis + un junior copiando datos), tu precio es indefendible. Muerta en 48 horas, sin gastar un peso.**

**Fase 1 — Preventa real (días 3-10, costo: ~$50)**

Si sobrevive la Fase 0:

1. **Día 3:** Lista de 50-80 agencias pequeñas (Clutch.co, Google Maps, LinkedIn). Emails con Apollo/Hunter (plan gratis). Un mock: video Loom de 2 minutos o PDF de una página mostrando cómo se vería. Un link de pago de Stripe. Nada funcional.
2. **Días 4-10:** 10-15 emails/DMs personalizados al día. Algo como: *"Vi que manejan campañas para [cliente/rubro]. Estoy lanzando reportes automáticos de cliente para agencias — conectas las fuentes y el cliente recibe su PDF/dashboard brandeado cada mes, sin tocar nada. Precio fundador: $100/mes de por vida (precio normal $200). Solo 5 cupos, arranco el [fecha]. ¿15 min esta semana?"*
3. **En la llamada:** 5 min sobre su proceso actual, 5 min mostrando el mock, y luego el cierre literal: *"Estoy tomando 5 clientes fundadores a $100/mes, el primer pago reserva el cupo y empezamos el [fecha]. ¿Entras?"*

Con 50-80 contactos bien elegidos esperas 8-12 conversaciones reales.

## Costo y tiempo

| Ítem | Costo |
|---|---|
| Herramientas de email (free tier) | $0 |
| Mock (Figma/Canva/Loom) | $0-15 |
| Stripe link | $0 (comisión solo si vendes — buen problema) |
| **Total** | **$0-65** |
| Tiempo | 10 días hábiles, 2-3 h/día |

## Criterios de muerte (escríbelos ANTES de empezar)

- **0 ventas pagadas de 8-10 pitches reales → muerta.** Si no pagan $100/mes rebajado y de por vida, jamás pagarán $200/mes. Sin ambigüedad.
- **"Lo usaría, pero no a ese precio" repetido 5+ veces → muerta en esa forma.** El problema existe, tu precio/segmento no. Ojo: este es el desenlace más probable. Las agencias pequeñas son brutalmente sensibles al precio y su stack actual es gratis.
- **"Ya uso AgencyAnalytics/Looker Studio y me funciona" dominante → muerta.** Mercado servido. (AgencyAnalytics cobra ~$60/mes; tu $200 necesita justificar 3x.)
- **1-2 ventas con mucha fricción** (regateo fuerte, "déjame pensarlo" eterno, exigen features que no puedes hacer) → yo también la mataría. Define esto hoy, porque en el momento vas a querer racionalizarlo como éxito.

**Sobrevive solo si: 3+ agencias pagaron de verdad en 10 días.** Y aun así no escribas código: entrégales los reportes *a mano* durante un mes (concierge). Si no puedes vender/entregar el servicio manual, no puedes vender el software.

Última cosa: gasta 1 hora el día 0 leyendo reviews de 2 y 3 estrellas de AgencyAnalytics, DashThis y Whatagraph en G2. Ahí está escrito exactamente qué odian las agencias pequeñas y cuánto están dispuestas a pagar. Puede que la idea muera ahí mismo, gratis, antes del almuerzo. Ese sería el mejor resultado posible.