# Kimi K2.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 6.66 | quality: 8.0
- latency_total: 225.414s | tokens_per_second: 26.6
- input_tokens: 223 | output_tokens: 5997

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

**Experimento: "El Piloto Manual de 48h" (Wizard of Oz)**

No construyas nada. Si no pagan $200 por el resultado **una sola vez**, hecho a mano y entregado en 24h, no pagarán $200/mes por un software que ellos deben configurar.

---

### EXACTAMENTE QUÉ HACES

**Paso 1: Caza (2 horas)**
Busca **20 dueños/directores de agencias de 2-10 personas** que tengan al menos 3 clientes en retainer (mensualidad). Dónde:
- LinkedIn: Filtro "CEO/Founder/Director" + empresa 1-10 empleados + industria "Marketing publicitario".
- Facebook/Slack/Discord: Grupos de agencias de marketing digital (busca "Agencias de marketing [país]", "Media Buyers", etc.).
- Instagram: Perfiles de agencias pequeñas que publiquen resultados de clientes.

**Filtro de calidad:** Si no tienen clientes mensuales, no necesitan reportes recurrentes. Sáltalos.

**Paso 2: Mensaje directo (15 min)**
Envía este mensaje exacto (adapta el nombre):

> *"Hola [Nombre]. Vi que trabajan con clientes mensuales. Pregunta rápida: ¿cuántas horas pierden armando reportes de resultados este mes?*
>
> *Estoy probando un piloto: te armo el reporte de marzo por **$200**, entregado mañana en PDF/dashboard listo para enviar al cliente. Sin que toques Excel.*
>
> *Si te funciona, después lo automatizo a $200/mes. ¿Te interesa que lo haga con tus datos?"*

**Paso 3: Entrega manual (solo si pagan)**
Si te responden "sí":
- Pídeles acceso de lectura a Analytics / Ads Manager / capturas de pantalla.
- Ármales el reporte en **Looker Studio, Google Slides o Canva** (lo que ya sepas usar). Máximo 2 horas de tu tiempo. Que se vea profesional.
- Entrégalo. Diles: *"Aquí está. Te paso el link de pago por los $200."* Usa Stripe, PayPal o transferencia. Cobro real.

**Paso 4: El cuchillo (solo si compraron el piloto)**
Si pagan los $200, al día siguiente les dices:
> *"Si quieres que esto se genere automático cada mes sin que hagas nada, la herramienta queda a $200/mes. ¿Te la configuro este fin de semana?"*

---

### CUÁNTO CUESTA

**$0.** Cero pesos en ads, cero código, cero Figma, cero landing. Solo tu tiempo:
- 2h para buscar los 20 contactos.
- 30 min para enviar mensajes.
- 2h para armar el reporte (solo si alguien paga).

---

### CUÁNTO TARDA

**48 a 72 horas.**
- Día 1: Enviar los 20 mensajes por la mañana. Seguir por la tarde a los que no respondan.
- Día 2: Si alguien paga, entregas el reporte y cobras. Preguntas por la mensualidad.

---

### EL RESULTADO QUE TE HACE ABANDONAR (MATA LA HIPÓTESIS)

Cierra la idea si pasa **cualquiera** de esto:

1. **0 de 20 pagan los $200 del piloto manual.**  
   *(Si no compran un reporte hecho y entregado, no comprarán una herramienta abstracta.)*

2. **Alguien paga el piloto, pero 0 de 3 aceptan la mensualidad de $200.**  
   *(El dolor es puntual, no recurrente. O prefieren pagar por servicio, no por software.)*

3. **Más del 50% de las respuestas son "está interesante, contáctame en 2-3 meses".**  
   *(No es un problema urgente. No hay "dolor de cabeza" suficiente para pagar ahora.)*

4. **Te dicen "ya usamos Looker/Data Studio/una plantilla" y no ven valor en $200.**  
   *(El precio está fuera de lo que consideran razonable para esta categoría.)*

---

### POR QUÉ ESTO MATA TU HIPÓTESIS SIN SESGOS

La mayoría de fundadores se equivocan porque confunden **"me interesa"** con **"pagaré"**. Este experimento elimina ese ruido:

- **Elimina el "me encanta la idea":** No vendes una herramienta. Vendes un resultado concreto (un reporte en su inbox mañana).
- **Elimina excusas de la landing:** No hay botón de "Saber más", no hay funnel que optimizar. Es una conversación humana directa a la decisión de compra.
- **Elimina el "cuando esté listo":** Les ofreces valor HOY. Si no pagan hoy, no pagarán en 2 meses cuando tu app esté en beta.
- **Prueba el precio real:** $200 no es un número que dijiste en una encuesta. Es una transferencia que deben autorizar.

**Si este experimento falla, ahorraste 2 meses de desarrollo y $0.** Si sobrevive (2+ agencias te pagan la mensualidad), entonces sí construyes, pero ya con clientes que esperan tu herramienta.

Ahora ve y trata de que te digan que no.