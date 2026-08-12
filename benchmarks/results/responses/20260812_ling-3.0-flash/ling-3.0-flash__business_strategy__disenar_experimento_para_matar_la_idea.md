# Ling 3.0 Flash — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 8.0 | quality: 8.0
- latency_total: 7.32s | tokens_per_second: 350.9
- input_tokens: 225 | output_tokens: 2569
- judge_score: 5.0 | justificación: 

## Respuesta completa

# El Experimento: "Cobra antes de construir"

## Qué haces exactamente

**1. Construyes una página de venta, no una landing de "registro".**
Una página que *vende* la herramienta como si ya existiera. No pide email. Pide tarjeta.

- Título claro: *"Reportes automáticos para tus clientes. $200/mes. Sin configuración."*
- 3-4 bullets del valor (lo que ahorran en tiempo, qué ven sus clientes, frecuencia)
- Un botón: **"Empezar prueba de 14 días — $200/mes"**
- Después del checkout: pantalla de "Gracias, en breve te contactamos" (no se le cobra nada todavía, solo se captura la intención con tarjeta)

Herramientas: Carrd ($19/año) + Stripe Checkout (integración de 30 min) + Zapier o Make si quieres notificarte cuando alguien pasa por checkout.

**2. Haces outreach directo a 50 dueños de agencias pequeñas.**
No spam genérico. Donde están:
- Grupos de Facebook de agencias de marketing (LatAm, España, o donde operes)
- LinkedIn: buscas "director de agencia", "dueño agencia marketing", "fundador agencia" en tu mercado objetivo
- Comunidades de Slack/Discord de agencias

Mensaje (adapta):
> *"Estoy construyendo una herramienta que automatiza los reportes mensuales que las agencias envían a sus clientes. Si te interesa, puedo darte acceso anticipado a $200/mes. ¿Te parece bien si te cobro el primer mes solo para reservar lugar? Si no te sirve, me devuelves el dinero y listo."*

**3. No les explicas cómo funciona.**
Si preguntan, dices: *"Es una herramienta que se conecta a las fuentes de datos y genera reportes automáticos para los clientes. La idea es que te ahorre 3-5 horas al mes."* No demos más detalle. Si el dolor es real, lo suficiente.

---

## Cuánto te cuesta

| Item | Costo |
|---|---|
| Carrd Pro (o similar) | ~$19/año |
| Stripe (comisiones solo si cobras) | $0 hasta que haya pagos |
| Tu tiempo de construcción de la página | 4-6 horas |
| Tu tiempo de outreach (50 mensajes) | 2-3 horas |
| **Total** | **~$20 + tu tiempo** |

---

## Cuánto tarda

- **Días 1-2:** Montas la página + el checkout en Stripe.
- **Días 3-4:** Haces los 50 outreachs.
- **Días 5-16:** Esperas respuestas y pagos.
- **Día 17:** Tomas la decisión.

**Total: 2 semanas.**

---

## El resultado que te hace abandonar la idea

🔴 **Umbral de muerte: 0 pagos reales con tarjeta en 14 días.**

Cualquiera de estos también es señal de muerte:
- **Menos de 2 personas** pasan por el checkout (no solo clickean, sino que llegan al formulario de tarjeta).
- **10+ personas** dicen "me interesa" o "envíame info" pero **ninguna** introduce datos de tarjeta → el dolor existe pero no es lo suficientemente fuerte como para pagar $200 por ello.
- **Alguien paga y cancela en los primeros 7 días** → el producto no resuelve lo que crees que resuelve.

🟢 **Lo que te haría seguir:** Si al menos 2-3 agencias pagan el primer mes (o dejan tarjeta comprometida), la hipótesis tiene tracción real y vale la pena construirla.

---

## Por qué este experimento mata la hipótesis y no la valida

- **Exigir dinero real** separa el "me gusta la idea" del "estoy dispuesto a sacrificar $200 por ella". Son dos cosas radicalmente distintas.
- **No construir nada** elimina el sesgo de esfuerzo hundido. Si no funciona sin producto, no va a funcionar con producto.
- **El outreach directo** te da información cualitativa además de cuantitativa: *por qué* no pagan, qué les falta, si el problema es real o si el precio está mal.
- **Es concluyente.** No hay resultado ambiguo. O la gente pone dinero, o no lo pone.

---

## Lo que puede salir mal y cómo manejarlo

| Riesgo | Mitigación |
|---|---|
| Nadie responde al outreach | Ajusta el targeting. Si llevas 3 semanas y 0 respuestas, el problema puede ser tu canal de distribución, no la hipótesis. Prueba otro canal antes de tirar la toalla. |
| Mucho interés, cero pagos | Baja el precio a $50/mes y repite. Si a $50 tampoco hay pagos, el dolor no justifica el costo de ninguna herramienta. |
| Pagos pero de personas equivocadas (no agencias) | Refina tu ICP en el mensaje y repite. |

---

**Regla de oro:** Si no puedes hacer que alguien te dé dinero *antes* de construir, no vas a poder hacerlo *después* de construir. Construir 2 meses para descubrir esto es la forma más cara de validar lo que ya puedes saber en 14 días por $20.