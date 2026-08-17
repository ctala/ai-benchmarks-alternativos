# DeepSeek V4 Pro — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 7.26 | quality: 8.0
- latency_total: 35.311s | tokens_per_second: 97.3
- input_tokens: 193 | output_tokens: 3437
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un plan detallado y práctico para probar la hipótesis con un enfoque en costos y tiempo mínimos.

## Respuesta completa

Esto es lo que harías si quisieras sentirte bien. No es lo que harás. Vas a intentar matar tu idea en 5 días con $0. Este es el experimento:

---

### El experimento: *Pre-Order Fake Door* (compromiso de tarjeta, sin cobro)

**Qué construyes**  
Una landing page de una sola pantalla. Sin logo elaborado, sin diseño perfecto. Contenido:

- Titular directo: *“Reportes de marketing para tus clientes en piloto automático. Entregas lo que hoy te toma 4 horas en 15 minutos.”*
- Un vídeo de 90 segundos (Loom) grabado sobre un prototipo en Figma. Muestras el flujo: conectas fuentes de datos, eliges plantilla, se genera un PDF. No hay backend. Es una simulación.
- Precio único en pantalla: **$200/mes**. Debajo, una oferta temporal: *“Reserva tu plaza ahora con un 50% de descuento de por vida. No se te cobrará hasta que la herramienta esté lista.”*
- Botón grande: **“Reservar mi plaza”**.

Al hacer clic, van a un formulario de checkout que pide:
- Nombre, email, empresa
- Número de tarjeta, fecha de caducidad, CVC
- Un checkbox que acepta que “se realizará un cargo de $100/mes cuando el producto se lance”.

**Qué ocurre al enviar**  
El formulario **no procesa el pago**. No conectas Stripe. Simplemente muestra una página de agradecimiento: *“¡Tu plaza está reservada! Te avisaremos en cuanto lancemos.”* Los datos de tarjeta se descartan (no los almacenas). Si quieres ser más limpio, usa un Typeform que pida los campos de tarjeta pero sin validación real; el objetivo es ver quién está dispuesto a meter los dígitos.

**Cómo consigues tráfico cualificado**  
Nada de anuncios. Contactas manualmente a **50 dueños de agencias pequeñas** (2-10 empleados) que conozcas o puedas encontrar en LinkedIn. Sin automatizar. Les escribes un mensaje así:

> *“Hola [nombre], estoy testeando una herramienta que automatiza los reportes de marketing para agencias pequeñas. Me encantaría tu opinión sincera como dueño de agencia. ¿Te importaría ver la página y decirme si algo así te resolvería un dolor real? [link]”*

No les vendes. Les pides feedback. Si preguntan por el precio, dices que está en la página. Si preguntan si ya funciona, respondes: *“Estamos validando la demanda antes de terminar de construir. Si te interesa, puedes reservar con descuento.”* No empujes.

**Duración y coste**  
- Construir la página + vídeo + formulario: **1 día**.
- Contactar a 50 personas y esperar respuestas: **4 días**.
- Coste monetario: **$0** (Carrd o similar, Loom gratuito, Typeform gratuito, LinkedIn básico).
- Coste en tiempo: unas 10-15 horas tuyas.

**Señal de muerte (kill signal)**  
Si después de contactar a **50 prospectos ideales** (dueños de agencia pequeña que entienden el problema) obtienes **menos de 3 formularios enviados con los datos de tarjeta** (es decir, <6% de conversión a pre-order), **matas la idea inmediatamente**.

¿Por qué? Porque si ni siquiera un 6% de gente que te conoce o a la que le has pedido feedback personalmente está dispuesta a *meter los datos de su tarjeta* (sin cargo inmediato y con 50% de descuento) por una solución que promete resolver un dolor enorme, el mercado no pagará $200/mes cuando el producto sea real y tengan que sacar la cartera de verdad. El problema no es tan grande o el precio no es aceptable. En cualquiera de los dos casos, tu hipótesis está muerta.

---

### Por qué este experimento mata la hipótesis (y no la valida artificialmente)

- **No mide interés, mide compromiso.** Pedir la tarjeta es el filtro más cercano a una transacción real sin tener producto. Las encuestas y los “me interesa” mienten.
- **Es extremadamente barato y rápido.** En menos de una semana tienes datos duros. Si falla, habrás ahorrado 2 meses de desarrollo y el coste de oportunidad.
- **Es asimétrico.** Si mueren las conversiones, cierras sin remordimientos. Si sorprendentemente consigues >5 pre-orders, tienes una lista de clientes potenciales reales con los que puedes hacer un piloto manual (Wizard of Oz) para la siguiente fase.

### Si quieres ser aún más rudo (opcional)

Si después de la fake door todavía tienes dudas, puedes ejecutar un **Wizard of Oz manual** durante 2 semanas con los que sí reservaron. Les dices que están en la beta, les pides acceso a sus datos y tú mismo generas los reportes a mano. Cobras los $100 del descuento. Si al final del mes no quieren renovar ni a $100, confirmas la muerte. Pero ese experimento ya toma un mes y esfuerzo real. La fake door es suficiente para disparar a la cabeza de la hipótesis en 5 días.