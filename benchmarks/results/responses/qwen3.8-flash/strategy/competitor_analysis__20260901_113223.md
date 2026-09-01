# Qwen 3.8 Flash — strategy/competitor_analysis

- model_id: `qwen/qwen3.8-flash`
- success: True  | final: 8.38 | quality: 10.0
- latency_total: 248.424s | tokens_per_second: 49.8
- input_tokens: 221 | output_tokens: 12364

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un analista de estrategia para startups. Sé riguroso con los datos y honesto cuando no tengas certeza.

**user:**

Soy fundador de una startup de email marketing para pymes en LATAM. Mis 3 competidores principales son Mailchimp, Brevo (ex-Sendinblue), y una startup local llamada "EnviaMas".

Con la informacion que tengas (si no la tienes, dilo):
1. Genera una tabla comparativa con: pricing, features principales, mercado target, fortalezas, debilidades
2. Identifica 3 gaps de mercado que yo podria explotar
3. Sugiere un posicionamiento diferenciador para mi startup
4. Que deberia hacer en los proximos 90 dias?

Se especifico. No me des consejos genericos.


## Respuesta completa

## Aviso de rigor

Te respondo con lo que puedo sostener con relativa confianza y te marco dónde no tengo certeza:

- **Mailchimp y Brevo**: tengo información pública razonable hasta mi corte de conocimiento (enero 2026). Los precios exactos cambian con frecuencia, así que los uso como **rangos estratégicos**, no como verdad absoluta.
- **EnviaMas**: no tengo información suficientemente fiable y actualizada para afirmar pricing, features o mercado con precisión. No voy a inventar datos. Te dejo una fila con **“no confirmado”** y una hipótesis explícita para que la valides.
- **Asumo**: tu startup está en etapa temprana, probablemente con recursos limitados y compitiendo con plataformas globales. Si ya tienes MRR relevante, el plan de 90 días cambia hacia retención y pricing.

---

# 1. Tabla comparativa

| Competidor | Pricing aproximado / estimado | Features principales | Mercado target | Fortalezas | Debilidades |
|---|---:|---|---|---|---|
| **Mailchimp** | Free: hasta ~500 contactos y límites de envíos. Essentials desde ~USD 13/mes. Standard desde ~USD 20/mes. Premium desde ~USD 95/mes. El costo escala rápido por contactos. | Campañas de email, editor drag-and-drop, plantillas, segmentación básica/avanzada según plan, automatizaciones, landing pages, integraciones e-commerce, reporting, CRM lite, audiencias, journeys. | Pymes, e-commerce, marketers, agencias, startups globales. Fuerte en SMBs y e-commerce. | Marca muy reconocida, ecosistema de integraciones, plantillas, educación de mercado, reporting sólido, confianza para marketers. | Pricing por contactos puede castigar a pymes con listas grandes pero bajo envío. Soporte LATAM limitado. Onboarding en inglés. Automatizaciones avanzadas pueden resultar caras/complejas. No está diseñado alrededor de WhatsApp/realidad LATAM. |
| **Brevo** (ex-Sendinblue) | Free: ~300 emails/día con contactos ilimitados. Starter desde ~USD 9/mes. Business desde ~USD 25/mes. Enterprise custom. SMS/WhatsApp/transactional suelen cobrar por consumo. | Email marketing, automatizaciones, CRM, transactional email, SMS, WhatsApp, landing pages, API, segmentación, campañas multicanal, reporting. | Pymes, startups, e-commerce, equipos técnicos, empresas que quieren email + transactional + SMS/WhatsApp. | Contacto ilimitados, pricing más eficiente por volumen de envíos, multicanal email/SMS/WhatsApp, API, transactional, CRM integrado. | Menos “brand awareness” que Mailchimp en algunos mercados. UX/automatizaciones no siempre tan pulidas. Soporte LATAM y pagos locales limitados. WhatsApp puede volverse costoso si no se gestiona. |
| **EnviaMas** | **No confirmado**. No tengo datos fiables. Hipótesis a validar: planes en moneda local, límites por contactos/envíos, posible add-on de WhatsApp/SMS, pricing competitivo vs. Mailchimp/Brevo. | **No confirmadas**. Hipótesis típica de plataforma local: campañas de email, plantillas, listas, segmentación básica, soporte en español, posible integración con medios de pago locales. | **Hipótesis**: pymes locales en su país o región LATAM. | **Probables fortalezas**: idioma, cercanía cultural, facturación local, soporte más humano, conocimiento de vertical local, integraciones regionales. | **Probables debilidades**: menor escala, menos integraciones, automatizaciones menos maduras, reporting más débil, recursos limitados, marca menos conocida, posible dependencia de un país. |

### Qué necesitas validar de EnviaMas en 48–72 horas

No dejes esta fila como suposición. Haz un **mystery shopping**:

1. Regístrate en su plan gratuito o demo.
2. Captura pricing por contactos, envíos, WhatsApp/SMS, facturación, impuestos.
3. Mide tiempo real de onboarding: ¿cuánto tarda una pyme en enviar su primera campaña?
4. Revisa integraciones: Shopify, Tiendanube, WooCommerce, Mercado Pago, PSE, OXXO, SPEI, WhatsApp Business API.
5. Revisa soporte: ¿responden en español? ¿en cuántas horas? ¿por WhatsApp?
6. Revisa límites de automatización, segmentación, reporting y deliverability.
7. Pide demo a su equipo comercial y grábala si es posible.
8. Busca 10 reseñas en Google, Capterra, GetApp, redes y foros locales.
9. Identifica sus 5 clientes más visibles y qué vertical dominan.
10. Detecta su punto débil real: precio, producto, soporte, integraciones o confianza.

---

# 2. Tres gaps de mercado que podrías explotar

## Gap 1: Pricing y facturación adaptados al comportamiento de pymes LATAM

**Problema concreto:**

- Mailchimp cobra cada vez más fuerte cuando crece la lista, aunque el envío sea bajo.
- Brevo tiene contactos ilimitados, pero sigue siendo pricing global, en USD/euros y con límites por envíos o consumo.
- En LATAM muchas pymes:
  - tienen listas grandes de clientes,
  - envían campañas solo en fechas clave,
  - cobran en moneda local,
  - pagan con OXXO, SPEI, PSE, Mercado Pago, transferencia, tarjeta local,
  - necesitan factura con impuestos locales,
  - no quieren sorpresas en USD.

**Oportunidad:**

Crear un modelo de pricing que no castigue crecer la lista, sino que refleje el valor real:

- Plan base en moneda local.
- Cobro por campañas activas, envíos o conversaciones, no solo por contactos.
- Add-ons transparentes de WhatsApp/SMS.
- Facturación local.
- Opción de prepago o consumo.
- Límites claros para que una pyme no entre en pánico por costos.

**Feature mínima viable:**

Un pricing page que diga, por ejemplo:

> “No pagas por tener contactos. Pagas por campañas, envíos y conversaciones. Facturación local en MXN/COP/CLP/BRL/ARS, según país.”

No necesitas un sistema de billing ultra-complejo desde el día uno. Puedes empezar con Stripe + pasarela local + invoices manuales para pilotos, pero debes diseñar el modelo desde el inicio.

**Riesgo:**

Si copias pricing por contactos, te parecerás a Mailchimp. Si copias pricing por envíos sin límites claros, puedes erosionar márgenes con WhatsApp/SMS.

---

## Gap 2: Email + WhatsApp como un solo journey de ventas para pymes LATAM

**Problema concreto:**

En LATAM, WhatsApp no es un canal secundario. Es el canal de cierre de venta, atención, cobranza y recompra. Pero muchas plataformas lo tratan como un add-on global, caro o mal explicado.

Mailchimp y Brevo tienen capacidad multicanal, pero no están diseñados alrededor del flujo real de una pyme LATAM:

1. Cliente deja email.
2. Recibe campaña.
3. Hace clic.
4. Consulta por WhatsApp.
5. Pide precio.
6. Recibe recordatorio.
7. Cierra compra.
8. Recibe postventa o reseña.

**Oportunidad:**

Posicionarte como la plataforma donde **email y WhatsApp trabajan juntos**, no como dos productos separados.

Casos de uso concretos que deberías priorizar:

- Abandono de carrito con email + WhatsApp.
- Recordatorio de pago por transferencia/OXXO.
- Confirmación de cita con WhatsApp + email.
- Campaña de reposición de stock.
- Reseña postventa.
- Recuperación de cliente inactivo.
- Promoción relámpago con “click to WhatsApp”.

**Feature mínima viable:**

No necesitas inbox completo al inicio. Necesitas:

- Plantillas de WhatsApp aprobadas o listas para enviar.
- Automatizaciones simples: email → WhatsApp si no abrió, WhatsApp → email si no respondió.
- Métricas básicas: entregado, abierto, clic, respuesta, venta.
- Segmentación por comportamiento: compró, cotizó, abandonó, no abrió.
- Botón “Enviar por WhatsApp” dentro de la campaña.
- Costo transparente por mensaje WhatsApp.

**Mensaje fuerte:**

> “Haz que tu campaña de email termine en una venta por WhatsApp.”

---

## Gap 3: Onboarding vertical, soporte local y compliance LATAM

**Problema concreto:**

Mailchimp y Brevo son excelentes para marketers que ya saben usar una plataforma. Pero muchas pymes LATAM no tienen un especialista en email marketing. Necesitan:

- alguien que les diga qué campaña hacer,
- plantillas específicas por industria,
- soporte en español/portugués,
- ayuda con SPF/DKIM/DMARC,
- ayuda con listas y consentimiento,
- ayuda con LGPD, LFPDPPP, habeas data u otras normas locales,
- integraciones con herramientas locales.

**Oportunidad:**

No vendas “email marketing genérico”. Vende un **sistema de comunicación por vertical**.

Ejemplos de verticales:

- Retail y tiendas físicas.
- E-commerce.
- Restaurantes.
- Clínicas y consultorios.
- Inmobiliarias.
- Academias y cursos.
- Servicios profesionales.
- Marcas de belleza/cosmética.

**Feature mínima viable:**

Un setup guiado por vertical:

- “Soy tienda de ropa” → te da 10 plantillas, 5 automatizaciones, 3 campañas recomendadas.
- “Soy restaurante” → reservas, promos, fidelización, reseñas.
- “Soy e-commerce” → carrito abandonado, postcompra, cross-sell, winback.

Además:

- Wizard de entregabilidad: SPF, DKIM, DMARC.
- Consentimiento por país.
- Plantillas de políticas de privacidad.
- Soporte inicial por WhatsApp.
- Onboarding en 20 minutos, no en 2 semanas.

**Mensaje fuerte:**

> “No eres un marketer. Nosotros te damos las campañas, las automatizaciones y el soporte para que vendas más con email y WhatsApp.”

---

# 3. Posicionamiento diferenciador sugerido

## Posicionamiento central

> **La plataforma de email + WhatsApp para pymes LATAM que cobra por uso real, factura en moneda local y viene lista por vertical.**

No intentes ser “el próximo Mailchimp”. Eso es una guerra perdida contra marca, integraciones y presupuesto.

Debes posicionarte como:

> “Herramienta de revenue para pymes LATAM, no solo herramienta de email.”

---

## Propuesta de valor concreta

### Para el founder de la pyme

> “Deja de pagar por contactos y de pelear con plataformas en inglés. Conecta tu tienda, importa tus clientes y lanza campañas de email + WhatsApp en español, con facturación local y soporte real.”

### Para el equipo comercial

> “Cada campaña puede terminar en una conversación de WhatsApp, no solo en un clic.”

### Para el dueño de e-commerce

> “Recupera carritos abandonados con email + WhatsApp, sin pagar USD ni depender de agencias.”

---

## Posicionamiento recomendado por etapas

### Fase 1: Beachhead

Elige **una vertical y dos países**.

Ejemplo:

> “Email + WhatsApp para e-commerce de moda y accesorios en México y Colombia.”

O:

> “Email + WhatsApp para retail local en Chile y Colombia.”

No digas “para todas las pymes de LATAM” al inicio. Eso diluye tu mensaje.

---

### Fase 2: Expansión controlada

Después de dominar una vertical:

> “El sistema de comunicación de revenue para pymes LATAM.”

---

## Pilares de diferenciación

| Pilar | Cómo se ve en producto | Cómo se comunica |
|---|---|---|
| **LATAM-first** | Moneda local, pagos locales, soporte en español/portugués, compliance local. | “Hecho para LATAM, no traducido desde EE.UU.” |
| **Pricing predecible** | Cobro por campañas/envíos/conversaciones, no solo contactos. | “Paga por resultados, no por contactos.” |
| **WhatsApp-native** | Journeys email + WhatsApp, plantillas, métricas, costos claros. | “Tu campaña de email cierra ventas por WhatsApp.” |
| **Vertical onboarding** | Setup por industria, plantillas, automatizaciones recomendadas. | “Listo para tu negocio, no para marketers profesionales.” |
| **Soporte real** | Onboarding asistido, WhatsApp support, help center en español. | “Te acompañamos hasta tu primera campaña.” |

---

# 4. Qué deberías hacer en los próximos 90 días

Te dejo un plan específico, con entregables y métricas. Asumo que tu equipo es pequeño y necesitas validar rápido.

---

## Días 1–15: Teardown competitivo y selección de beachhead

### Objetivo

Dejar de competir contra una idea vaga y empezar contra datos reales.

### Acciones concretas

1. **Haz un teardown completo de Mailchimp, Brevo y EnviaMas.**

   Para cada uno captura:

   - Precios por 500, 1,000, 5,000, 10,000 contactos.
   - Límites de envíos.
   - Costo de WhatsApp/SMS.
   - Plan gratuito.
   - Tiempo para crear campaña.
   - Automatizaciones disponibles.
   - Integraciones.
   - Idioma de soporte.
   - Métodos de pago.
   - Facturación local.
   - Proceso de alta de dominio.
   - Reporting.

2. **Elige una vertical y dos países.**

   No intentes LATAM completo. Elige, por ejemplo:

   - México + Colombia.
   - Chile + Perú.
   - Argentina + Uruguay.
   - Brasil si puedes operar en portugués.

   Criterios:

   - Dolor real con WhatsApp.
   - Acceso a pymes.
   - Facilidad de facturación.
   - Mercado de e-commerce/retail.
   - Tu ventaja de idioma o red.

3. **Entrevista a 20 pymes.**

   No vendas. Pregunta:

   - ¿Cuántos contactos tienes?
   - ¿Cada cuánto envías campañas?
   - ¿Qué herramienta usas?
   - ¿Qué te frustra?
   - ¿Cuánto pagas?
   - ¿Usas WhatsApp para vender?
   - ¿Cómo cobras?
   - ¿Puedes pagar en moneda local?
   - ¿Necesitas factura?
   - ¿Qué campaña te generó más ventas?
   - ¿Qué automatización te daría más dinero?
   - ¿Cuánto pagarías por resolverlo?

4. **Identifica 3 integraciones locales críticas.**

   Ejemplos:

   - Shopify.
   - Tiendanube.
   - WooCommerce.
   - Mercado Pago.
   - OXXO Pay.
   - PSE.
   - SPEI.
   - Bsale.
   - Kyte.
   - Vendty.
   - Facturama.
   - Aspel.
   - WhatsApp Business API.

### Entregables

- Tabla comparativa actualizada con screenshots.
- Lista de 20 entrevistas.
- 1 vertical elegida.
- 2 países elegidos.
- 3 integraciones prioritarias.
- 1 hipótesis de pricing.

### Métrica de éxito

- 100% del teardown hecho.
- 20 entrevistas completadas.
- 1 vertical y 2 países definidos.
- Al menos 8 pymes diciendo: “Esto me interesa” o “pagaría por esto”.

---

## Días 16–30: Definir oferta, pricing y posicionamiento

### Objetivo

Que un cliente potencial entienda tu valor en menos de 60 segundos.

### Acciones concretas

1. **Diseña 3 planes simples.**

   Ejemplo:

   | Plan | Ideal para | Precio local | Incluye |
   |---|---|---:|---|
   | Starter | Pyme que empieza | USD 19 equivalente | Email, plantillas, 3 automatizaciones, soporte básico |
   | Growth | Pyme que vende más | USD 49 equivalente | Email + WhatsApp, 10 automatizaciones, segmentación, reporting |
   | Pro | E-commerce/retail con equipo | USD 99 equivalente | Integraciones, API, soporte prioritario, setup guiado |

   Ajusta moneda local. No uses USD como precio principal si tu target es pyme local.

2. **Define modelo de cobro.**

   Elige una estructura clara:

   - Base mensual + consumo por envíos.
   - Base mensual + consumo por conversaciones WhatsApp.
   - Planes por rangos de contactos, pero con límites suaves.
   - Add-on de WhatsApp con costo transparente.

   Evita pricing opaco.

3. **Crea landing page de validación.**

   Debe tener:

   - Headline: “Email + WhatsApp para pymes LATAM que quieren vender más.”
   - Subheadline: “Campañas, automatizaciones y facturación local en español.”
   - 3 casos de uso:
     - Recuperar carrito.
     - Cobrar por WhatsApp.
     - Enviar promos por vertical.
   - Pricing visible.
   - Botón: “Unirme al piloto” o “Solicitar demo”.
   - Testimonios o avales si tienes.

4. **Haz test de posicionamiento.**

   Prueba 3 mensajes:

   - A: “Email marketing para pymes LATAM.”
   - B: “Email + WhatsApp para vender más.”
   - C: “Plataforma local para campañas de email y WhatsApp.”

   Mide cuál genera más respuestas.

5. **Construye modelo de margen.**

   Calcula:

   - Costo por email.
   - Costo por WhatsApp.
   - Costo de soporte.
   - Costo de integración.
   - Churn esperado.
   - CAC.
   - LTV.
   - Precio mínimo para no perder dinero.

### Entregables

- Pricing final para pilotos.
- Landing page.
- 3 mensajes posicionamiento.
- Modelo financiero simple.
- Lista de 50 prospects.

### Métrica de éxito

- 100+ leads en waitlist.
- 10 demos agendadas.
- 5 cartas de intención o prepagos.
- 1 mensaje de posicionamiento con mejor conversión.

---

## Días 31–60: Construir el MVP del loop de revenue

### Objetivo

Que una pyme pueda enviar una campaña y ver una consecuencia de negocio, no solo un “email abierto”.

### Regla importante

No construyas un editor de email infinito, ni un CRM completo, ni 10 canales. Construye el camino mínimo hacia:

> importación de contactos → campaña → clic/respuesta → venta.

### Features prioritarias

1. **Importación de contactos con consentimiento.**

   - CSV.
   - Campos básicos: nombre, email, teléfono, país, ciudad, categoría.
   - Doble opt-in si es necesario.
   - Unsubscribe visible.

2. **Editor de campañas simple.**

   - Plantillas por vertical.
   - Editor drag-and-drop básico.
   - Preview en móvil.
   - Enviar prueba.

3. **Segmentación básica.**

   - Compradores.
   - No compradores.
   - Abandonaron carrito.
   - Cotizaron.
   - Clientes VIP.
   - Inactivos 90 días.

4. **5 automatizaciones clave.**

   No hagas 50. Haz estas:

   - Bienvenida.
   - Abandono de carrito.
   - Postcompra.
   - Recuperación de cliente inactivo.
   - Reseña/recompra.

5. **WhatsApp integration.**

   Empieza simple:

   - “Click to WhatsApp” en campaña.
   - Plantillas de WhatsApp.
   - Envío de recordatorio por WhatsApp si no abrió email.
   - Métricas básicas.

6. **Integraciones locales.**

   Elige 2, no 10:

   - Shopify o Tiendanube.
   - Mercado Pago, OXXO, PSE, SPEI o WhatsApp Business API.

7. **Deliverability básico.**

   - SPF/DKIM/DMARC wizard.
   - Verificación de dominio.
   - Lista de bloqueos.
   - Monitoreo de rebotes.
   - Warmup manual para cuentas nuevas.

8. **Reporting mínimo.**

   Por campaña:

   - Entregados.
   - Abiertos.
   - Clics.
   - Respuestas WhatsApp.
   - Ventas o conversiones.
   - Revenue estimado.

### No construyas todavía

- CRM completo.
- Inbox multicanal.
- Chatbot complejo.
- App móvil.
- Editor HTML avanzado.
- A/B testing sofisticado.
- Data warehouse.
- SSO enterprise.
- 15 integraciones.
- 20 idiomas.
- Multiusuario avanzado.
- Marketplace de templates.

### Entregables

- MVP funcional.
- 10 plantillas por vertical.
- 5 automatizaciones activas.
- 2 integraciones locales.
- Wizard de dominio.
- Proceso de onboarding manual.

### Métrica de éxito

- 20 pymes onboardadas.
- 50% envía su primera campaña en 7 días.
- 30% usa al menos una automatización.
- 20% registra una conversión o venta.

---

## Días 61–90: Pilotos pagados, GTM y pruebas de pricing

### Objetivo

Convertir validación en ingresos y aprender si tu pricing es sostenible.

### Acciones concretas

1. **Cierra 20 pilotos pagados.**

   No 20 gratis. Haz un piloto pagado con descuento:

   - 3 meses al 50%.
   - Setup fee gratis o bajo.
   - Compromiso de feedback.
   - Caso de estudio al final.

2. **Onboarda manualmente.**

   Para los primeros 20 clientes:

   - Llamada de 30 minutos.
   - Revisión de lista.
   - Configuración de dominio.
   - Plantillas personalizadas.
   - Primera campaña enviada con ellos.
   - Revisión de métricas a los 7 días.

3. **Mide time-to-value.**

   Define una meta:

   > Primera campaña enviada en menos de 3 días.

   Si no lo logras, el problema es onboarding, no features.

4. **Lanza 3 webinars.**

   Temas concretos:

   - “Cómo recuperar carritos abandonados con email + WhatsApp.”
   - “Campañas de email para retail local que venden en 7 días.”
   - “Cómo facturar y cobrar en LATAM sin complicarte con plataformas en USD.”

5. **Cierra 5 partnerships.**

   Busca:

   - Agencias de marketing locales.
   - Tiendas Shopify/Tiendanube.
   - Contadores.
   - Pasarelas de pago.
   - POS locales.
   - Academias de e-commerce.
   - Comunidades de emprendedores.

6. **Crea 3 casos de estudio.**

   Formato:

   - Cliente.
   - Vertical.
   - País.
   - Problema.
   - Herramienta usada.
   - Campaña/automatización.
   - Resultado.
   - Revenue generado o mejora.

7. **Refina pricing.**

   Revisa:

   - ¿Qué plan eligieron?
   - ¿Qué add-ons pidieron?
   - ¿Qué rechazaron?
   - ¿Qué precio fue barrera?
   - ¿Qué costo de WhatsApp te está comiendo margen?
   - ¿Qué feature realmente usaron?

### Entregables

- 20 clientes piloto.
- 3 casos de estudio.
- 5 partnerships.
- 3 webinars.
- Pricing ajustado.
- Roadmap de producto basado en uso real.

### Métricas de éxito

| Métrica | Meta 90 días |
|---|---:|
| Clientes piloto | 20 |
| Activación: primera campaña en 7 días | ≥50% |
| Retención mensual | ≥80% |
| CSAT | ≥4.5/5 |
| Tiempo de respuesta soporte | <4 horas hábiles |
| Entregabilidad | ≥97% |
| Revenue generado por pilotos | ≥USD 5,000–15,000 MRR equivalente |
| Leads de partnerships | ≥100 |
| Costo de adquisición inicial | ≤60% del LTV esperado |

---

# 5. Decisiones estratégicas que deberías tomar

## 1. No compitas con Mailchimp en features

Mailchimp tiene más integraciones, marca y recursos. Si intentas igualarlo, te quedas sin foco.

Compite en:

- LATAM-first.
- WhatsApp.
- soporte.
- facturación local.
- vertical onboarding.
- pricing predecible.

---

## 2. No te vendas como “email marketing barato”

Si compites solo por precio, Mailchimp y Brevo te pueden aplastar.

Tu mensaje debe ser:

> “Te ayudamos a vender más con email y WhatsApp, con soporte local y pricing predecible.”

---

## 3. Elige una vertical antes que un país

Si eliges solo país, puedes quedarte sin foco.

Mejor:

> “Email + WhatsApp para e-commerce de moda en México.”

O:

> “Email + WhatsApp para retail físico en Colombia.”

La vertical te da plantillas, automatizaciones y casos de uso más claros.

---

## 4. WhatsApp debe ser un motor de revenue, no un chat de soporte

No construyas solo un inbox. Construye journeys que generen dinero:

- carrito abandonado,
- recordatorio de pago,
- postventa,
- recompra,
- reserva,
- cotización.

---

## 5. Tu primer moat puede ser servicio, no tecnología

Al inicio, no tengas miedo de hacer:

- onboarding manual,
- campañas hechas por ti,
- templates personalizados,
- setup de dominio,
- revisión de listas,
- acompañamiento por WhatsApp.

Eso no es “poco escalable” si te permite aprender rápido y crear casos de éxito.

---

# 6. Roadmap sugerido de producto para 90 días

## MVP mínimo

- Importar contactos.
- Segmentar por comportamiento.
- Enviar campaña email.
- Plantillas por vertical.
- Automatización de bienvenida.
- Automatización de carrito abandonado.
- Click-to-WhatsApp.
- Métricas básicas.
- Unsubscribe.
- SPF/DKIM wizard.
- Facturación local manual.
- Soporte por WhatsApp.

## V1.5

- Reportes por revenue.
- Más automatizaciones.
- Integración con Shopify/Tiendanube.
- Segmentos avanzados.
- Costos transparentes de WhatsApp.
- Onboarding guiado por vertical.

## V2

- Inbox simple.
- A/B testing.
- API.
- Multiusuario.
- Roles.
- Marketplace de plantillas.
- Más integraciones locales.

---

# 7. Qué deberías priorizar si tu recurso es limitado

Si tienes poco equipo, prioriza esto:

1. **Una vertical.**
2. **Dos países.**
3. **Tres automatizaciones.**
4. **Cinco integraciones locales máximo.**
5. **Un pricing simple.**
6. **Soporte manual.**
7. **Casos de estudio con revenue.**

No priorices:

- editor perfecto,
- CRM completo,
- app móvil,
- multilenguaje,
- enterprise features,
- 10 integraciones,
- branding bonito sin validación.

---

# 8. Mi recomendación de posicionamiento final

Si tuviera que elegir una frase para tu startup:

> **“La plataforma de email + WhatsApp para pymes LATAM que factura local, cobra por uso real y viene lista por vertical.”**

Y una versión más comercial:

> **“Deja de pagar por contactos y de configurar herramientas en inglés. Lanza campañas de email y WhatsApp en español, con soporte local y facturación en moneda local.”**

---

# 9. Lo que necesito de ti para afinar esto

Si me respondes con estos datos, puedo hacer una segunda versión mucho más precisa:

1. País principal donde operas.
2. Si ya tienes producto o estás en pre-MVP.
3. MRR actual, si tienes.
4. Cuántos clientes tienes.
5. Pricing actual.
6. Link o capturas de EnviaMas.
7. Tu equipo: cuántas personas y roles.
8. Tu presupuesto de los próximos 90 días.
9. Si ya tienes integraciones con Shopify, WhatsApp, pasarelas locales o POS.
10. Tu vertical actual o la que crees que más te compra.

Con eso puedo:

- completar la tabla de EnviaMas con datos reales,
- ajustar gaps,
- proponer pricing exacto,
- definir beachhead,
- y hacer un plan de 90 días más específico según tu etapa.