# Grok 4.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `x-ai/grok-4.5`
- success: True  | final: 6.9 | quality: 8.0
- latency_total: 36.159s | tokens_per_second: 86.2
- input_tokens: 373 | output_tokens: 3116
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, proporcionando un plan detallado y práctico para probar la hipótesis de manera efectiva.

## Respuesta completa

**El experimento: pre-venta fría de un producto que no existe (fake door + commitment de dinero real).**

Este es el más barato, rápido y letal que conozco para matar “pagarían $200/mes”. No mides “interés”, “likes” ni “suena genial”. Mides **si sacan la tarjeta o se comprometen por escrito a pagar**. Si no lo hacen, la hipótesis muere. 0 validación positiva permitida.

### Exactamente qué haces (paso a paso)

1. **Define el target con precisión (30 min)**  
   Agencias de marketing pequeñas: 1-15 personas, facturan menos de ~$50-100k/mes, hacen reportes recurrentes a clientes (performance, SEO, ads, social). Dueños o heads of client success.  
   Fuentes gratuitas: LinkedIn (búsqueda “dueño agencia marketing”, “founder marketing agency”, “agencia de marketing” + filtro por tamaño/ubicación), directorios locales, grupos de Facebook/LinkedIn de agencias, o Google “agencia de marketing [ciudad]” + scrapea 50-80 contactos. Prioriza españoles/latam o el mercado que quieras. Lista de 50-80 names + LinkedIn/email.

2. **Crea el “producto” en 2-4 horas (cero código)**  
   - Una página simple (Carrd.co, Notion público, Framer free o incluso un Google Doc limpio). Título: “Reportes de clientes automatizados en 5 minutos para agencias”.  
   - Descripción del dolor (reportes manuales que tardan 4-10h/semana, errores, clientes quejándose).  
   - Solución: “subes datos o conectas Google Analytics/Ads/Meta → genera PDF/dashboard branded listo para enviar”.  
   - 3-4 mockups fake (Figma, Canva o screenshots de Looker/Data Studio + Photoshop rápido).  
   - Precio claro: **$200/mes** (o “$150 founding rate primeros 20”).  
   - Botón principal: “Reservar acceso anticipado – pagar primer mes ahora” → link de Stripe Payment Link o PayPal (crea en 10 min, modo test o live). Alternativa: “Agendar demo de 15 min y pagar al final de la llamada”.  
   - Video Loom de 90 segundos: tú “demostrando” el flujo con los mockups.  
   Opcional ultra-barato: no hagas landing. Solo one-pager PDF + Loom + link de pago.

3. **Outreach frío (el core del test)**  
   Mensaje corto y directo (LinkedIn first, email second). Ejemplo:  
   “Hola [Nombre], vi que tienes [agencia]. ¿Cuántas horas/semana te/le gastáis en reportes a clientes?  
   Lancé una herramienta que lo automatiza (conecta Ads/Analytics → PDF branded listo). Precio $200/mes.  
   Aquí demo de 90s: [Loom].  
   ¿Te interesa el founding rate y reservar el primer mes ahora? Link: [pago o Calendly]. Si no es dolor real, dímelo y cierro el tema.”  
   Personaliza 1 línea (menciona un cliente o servicio suyo). Manda a 50. No más de 3-4 follow-ups.  
   En las respuestas o calls de 10-15 min: enseña mockups, pregunta cuánto tiempo pierden hoy, y **pide el pago o compromiso firmado** (“¿te cargo el primer mes y te doy acceso la próxima semana?”). Si dicen “suena bien pero…”, empuja: “¿Qué tendría que tener para que pagues hoy $200?”.

4. **Tracking brutal**  
   Spreadsheet: contactado / respondió / dijo que tiene el dolor / click en demo / agendó call / **pagó o firmó LOI con fecha de pago**. Nada más cuenta.

### Cuánto cuesta y cuánto tarda
- **Costo total: $0-30**. Carrd/Notion free, Stripe free, LinkedIn free, Canva free, dominio opcional ($10). Cero ads.
- **Tiempo total: 3-5 días calendario** (setup 4-6 horas un día; outreach + respuestas + 5-10 calls en los siguientes 2-4 días). Puedes matarlo en 48-72 horas si las primeras 20-30 respuestas son frías.

### Resultado que te hace ABANDONAR la idea (criterio de muerte concluyente)
Mata la hipótesis si se cumple **cualquiera** de estos:
- Después de contactar 50 dueños/calificados, **menos de 3 personas pagan o se comprometen por escrito a pagar $150-200/mes** (con fecha o tarjeta).
- Tasa de respuesta positiva seria (dolor + “quiero pagar o ver cómo pagar”) < 8-10%.
- En las conversaciones, el dolor de reportes es “molestia menor” o ya lo resuelven con templates/freelance/barato (<$50-100) y nadie ve $200 como justificado.
- Te dicen variaciones de: “lo haría si fuera $49”, “prefiero Excel + VA”, “mis clientes no pagan tanto premium”, o “no es prioridad”.

Si obtienes 0 pagos y solo “suena interesante, avísame cuando esté listo” → está muerta. Eso es el clásico falso positivo. No construyas.

### Por qué este test mata de verdad
- Fuerza el dinero o el compromiso real (no opiniones).
- Es más barato y rápido que cualquier MVP o landing + ads.
- Si sobrevive (3+ pre-pagos o LOIs serios), entonces sí tienes señal para el siguiente experimento más caro. Si muere, te ahorraste 2 meses.
- Bonus: en las calls descubres el dolor real, el precio real y el messaging que funciona (o no).

Hazlo esta semana. El día 5 miras el spreadsheet y decides: enterrar o iterar. La mayoría de hipótesis de “pagarían $X” mueren aquí. Eso es exactamente lo que quieres.