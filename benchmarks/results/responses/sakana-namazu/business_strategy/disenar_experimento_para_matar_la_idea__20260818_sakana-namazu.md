# Sakana Namazu — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `sakana/sakana-namazu`
- success: True  | final: 7.21 | quality: 8.0
- latency_total: 10.782s | tokens_per_second: 190.0
- input_tokens: 223 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

El usuario quiere un experimento para matar su hipótesis: "Las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes."

Principios clave:
- No quiere validar, quiere invalidar rápido y barato.
- No debe construir nada durante 2 meses todavía.
- Necesita procedimiento exacto, costo, tiempo, y criterio de abandono.

La hipótesis tiene varios riesgos/ componentes:
1. Existe el dolor real (hacen reportes manualmente y les molesta).
2. Valoran la automatización lo suficiente como para pagar.
3. Pagan específicamente $200/mes.
4. Las agencias PEQUEÑAS tienen capacidad de pago.
5. Quieren una herramienta externa, no hacerlo internamente o con templates.
6. El proceso actual es lo suficientemente complejo como para justificar el gasto pero no tanto como para requerir soluciones enterprise.

Experimento ideal: Test de ventas con pre-venta o letter of intent ANTES de construir. Pero más brutal aún: ¿Podemos simular que la herramienta existe y ver si compran? O mejor aún: forzar el "skin in the game" inmediato.

El experimento más barato y rápido para matar una hipótesis de B2B con precio es el **"Fake Door + Pre-venta con depósito"** o **"Landing + llamada de ventas con intento de cierre por adelantado"**.

Pero el más barato y rápido es:
1. Crear una landing page muy simple (con Carrd o similar) que describa el producto. ~$20/año.
2. Hacer una lista de 20-30 agencias pequeñas (menos de 10 empleados, ingresos <X).
3. Contactarlas directamente (LinkedIn/correo/frío) o mejor: ir a comunidades donde están (Facebook groups, Slack communities, Reddit r/agency, etc.) y también outreach directo.
4. No mostrar demo (porque no existe). Mostrar "early access" o "beta cerrada".
5. Intentar cerrar la venta CON PAGO ADELANTADO o depósito simbólico ($20-$50) que se devuelve si no se entrega, o que se convierte en crédito. O aún más duro: intentar que paguen los $200 del primer mes para entrar a la lista beta.

Pero hay un problema: si no hay producto, el "fake door" puede quemar reputación. En B2B es complicado. Alternativa: **interview de ventas con cierre forzado**.

Mejor experimento específico para este caso:

**El Test del Cierre Forzoso en Frío (Forced Sale Smoke Test)**

Pasos exactos:
1. Definir ICP muy estrecho: Agencias de marketing digital con 2-10 empleados, que trabajen con pymes, y que hagan reportes mensuales a clientes (SEO, ads, social media).
2. Armar un mensaje de outreach frío (email/LinkedIn/ WhatsApp si es posible) que presente la solución hipotética en 2 semanas.
3. No armar landing pública. Usar un Google Doc o Notion como "memoria de producto" si alguien pide más info, o un Calendly para "demo".
4. Hacer outreach a 50 agencias.
5. Llamar/ reunión zoom de 15 min con las que contesten.
6. En la llamada, describir la herramienta técnica (automatiza reportes de FB Ads, Google Ads, GA4, TikTok en un PDF/marca blanca o dashboard). Preguntar: "Si la tuviera lista la próxima semana, ¿la contratarías hoy por $200/mes?"
7. Si dicen que sí, pasar a la parte de pago: "Perfecto, estamos tomando a 5 agencias beta. El requisito para entrar es pagar el primer mes de $200 ahora, te lo cuidamos como crédito y si en 30 días no te encanta, te devolvemos el dinero." O aún más duro: "Te envío el link de pago ahora mismo".

Esto es barato (solo tiempo) y rápido (1 semana de outreach, 1 semana de calls). Pero quizás 50 agencias son muchas para empezar.

Aún más barato: **El Test del Mockup en Llamada + Pre-pago**
Pero quizás el usuario no quiere hacer llamadas. Sin embargo, para B2B, las llamadas matan la incertidumbre más rápido que las métricas de landing.

Diseñemos el experimento más brutal:

**Experimento: "Beta Cerrada con Compromiso de Pago Inmediato"**

- Tiempo total: 5 días de trabajo efectivo (espaciados en 7-8 días calendario).
- Costo: ~$0-$30 (herramientas de email finding, Calendly, Google Docs).
- Esfuerzo: 20-30 outreach personalizados.

Pero necesitamos un criterio claro de abandono. ¿Qué tan malo es suficientemente malo?

Componentes hipótesis a deconstruir:
- H1: Las agencias pequeñas tienen un dolor significativo con los reportes.
- H2: Están dispuestas a pagar por solución ($200 es aceptable).
- H3: Pagarán SIN ver el producto terminado (demanda real vs. nice-to-have).

Criterio de abandono: Si de 20 conversaciones calificadas (gentes que actualmente hacen reportes manualmente), menos de 25% (5 agencias) están dispuestas a pagar $200 hoy como depósito para una solución que llega en 2 semanas, la hipótesis está muerta.

¿Por qué 25%? En B2B pre-producto, si no cierras al menos 1 de 4 o 1 de 5 calificados, no hay producto de dolor agudo. Nota: el usuario dice "agencias pequeñas". En agencias pequeñas $200 es dinero real. Si no pagan un depósito reembolsable, no hay dolor.

Podemos hacerlo aún más barato: **El "Fake Door" por Email sin Producto.**

Pero quizás lo más inteligente es combinar:
1. Un día para definir lista y contactos (LinkedIn Sales Navigator gratuito por mes, o scraping básico).
2. Un día para crear un "micro-demo" falso: 3 slides en PDF o un video de Loom de 2 min mostrando "así se vería tu reporte automatizado". Esto lo hacemos con Figma gratis (mockup) o incluso con Google Slides y screenshots editadas.
3. Outreach frío ofreciendo "acceso prioritario a la beta cerrada por $200/mes, primer mes cobrado al entrar".
4. Intentar que paguen.

No obstante, el "experimento más barato y rápido" puede ser simplemente intentar cobrar a 10 agencias. Pero definamos exactamente los pasos.

**Propuesta de Experimentos ( elegiré el más agresivo ):**

Nombre: **"Pre-venta a ciegas con mockup estático en 7 días"**

**Paso 1: Define el blanco (1 día)**
- 30 agencias de marketing pequeñas (2-15 personas) en tu país/mercado objetivo.
- Criterio: Que ofrezcan servicios de PPC, SEO o Social y tengan >5 clientes (para que reportes sean tediosos).
- Encuéntralas en Clutch.co, Google Maps, o grupos de Facebook de agencias. O mejor: en comunidades donde ya hay algo de confianza.

**Paso 2: Crea el anzuelo visual (2-3 horas, $0)**
- Usa Google Slides o Canva para diseñar 1 "reporte automático" fake: logo de la agencia, métricas de FB Ads y Google Ads, todo bonito. Exporta como PDF.
- Escribe un copy de 3 líneas: "Automatizo tus reportes mensuales de cliente. 0 minutos de trabajo. $200/mes."

**Paso 3: Outreach masivo personalizado (2 días)**
- Envía 30 mensajes directos por email o LinkedIn.
- Texto clave: "Estoy armando una herramienta