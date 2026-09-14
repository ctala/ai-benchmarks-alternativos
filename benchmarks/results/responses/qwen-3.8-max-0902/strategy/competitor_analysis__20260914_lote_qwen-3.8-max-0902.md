# Qwen 3.8 Max 0902 — strategy/competitor_analysis

- model_id: `qwen/qwen3.8-max-0902`
- success: True  | final: 7.8 | quality: 10.0
- latency_total: 484.87s | tokens_per_second: 39.1
- input_tokens: 221 | output_tokens: 18981

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

Voy a ser directo y transparente:

- No tengo acceso a internet en tiempo real.
- Mi conocimiento llega hasta 2024-06, así que precios y features pueden haber cambiado.
- Conozco razonablemente bien Mailchimp y Brevo por información pública histórica.
- No tengo información fiable sobre “EnviaMas”. Si es una startup local pequeña, es probable que no tenga datos públicos suficientes. En la tabla lo marco como “a validar” y te doy un método para investigarla sin alucinar.

Dicho esto, te dejo una respuesta accionable, específica y orientada a LATAM.

---

## 1. Tabla comparativa

> Nota: los precios son aproximados y deben validarse antes de usarlos en una comparación pública. En LATAM, además, el precio real puede variar por impuestos, tipo de cambio, método de pago y promociones.

| Competidor | Pricing aproximado | Features principales | Mercado target | Fortalezas | Debilidades |
|---|---|---|---|---|---|
| **Mailchimp** | Free: hasta ~500 contactos y envíos limitados. Essentials desde ~US$13/mes. Standard desde ~US$20/mes. Premium desde ~US$350/mes. El precio escala fuerte por contactos y puede tener overages. | Email campaigns, automations, landing pages, formularios, CRM básico, plantillas, integraciones, reportes, AI content, audience management. Transaccional vía Mandrill. SMS/WhatsApp limitado según mercado. | Pymes globales, creadores, e-commerce, agencias, negocios digitales pequeños/medianos. | Marca muy conocida. Onboarding self-serve. Muchas plantillas. Integraciones con muchas herramientas. Buenos reportes básicos. Recursos educativos. | Para pyme LATAM puede volverse caro al crecer. Complejidad para usuarios no técnicos. Soporte y horarios no siempre locales. Facturación/pagos locales pueden ser fricción. Menos nativo para WhatsApp/SMS si se compara con soluciones locales. |
| **Brevo** | Free: contactos ilimitados, ~300 emails/día. Starter alrededor de US$25/mes para ~20k emails. Pro alrededor de US$65/mes para ~20k emails. Planes superiores por volumen. SMS/WhatsApp normalmente aparte o por consumo. | Email marketing, transactional email/API, SMS, WhatsApp campaigns, automation, CRM básico, landing pages, chat, segmentación, reportes. | Pymes y mid-market, especialmente e-commerce, SaaS, equipos técnicos o negocios que necesitan email transaccional + marketing. Fuerte en Europa y con presencia en LATAM. | Contactos ilimitados en free. Precio más ligado a volumen de envío que a contactos. Buen costo inicial para bases grandes. Multicanal: email, SMS, WhatsApp. Transaccional integrado. | Menos marca local que un actor regional. Soporte en español puede ser inconsistente. La UI/automations puede sentirse menos pulida que Mailchimp para usuarios simples. Costos de WhatsApp/SMS pueden confundir. Facturación local y pagos locales pueden ser fricción. |
| **EnviaMas** | **No tengo datos fiables.** Debes validar directamente: pricing público, planes por contactos/envíos, si cobra en moneda local, si tiene free trial, si cobra WhatsApp/SMS aparte. | **No confirmado.** Probablemente email marketing básico, campañas, plantillas, quizás automatizaciones simples. Validar si tiene WhatsApp, SMS, API transaccional, integraciones e-commerce, CRM, reportes de ventas. | Probablemente pymes locales/LATAM hispanohablantes. Validar si es por país, vertical o tamaño de negocio. | Hipótesis a validar: cercanía local, soporte en español, precio más bajo, conocimiento del mercado local, venta más personalizada. | Incertidumbre. Puede tener limitaciones en escala, entregabilidad, integraciones, compliance, infraestructura, producto o funding. Si es un white-label de otra plataforma, su diferenciación real puede ser débil. |

### Qué validar de EnviaMas en los próximos 7 días

No asumas que es fuerte o débil. Haz un teardown real:

1. Entra a su web como si fueras un cliente.
2. Pide demo o prueba gratis.
3. Pregunta explícitamente:
   - ¿Precio mensual para 1,000, 5,000 y 10,000 contactos?
   - ¿Cobran en moneda local?
   - ¿Emiten factura local?
   - ¿Qué métodos de pago aceptan?
   - ¿Tienen WhatsApp oficial API o solo enlaces a WhatsApp?
   - ¿Hacen onboarding humano?
   - ¿Configuran SPF/DKIM/DMARC?
   - ¿Tienen integraciones con Shopify, Tiendanube, WooCommerce, Mercado Libre, POS local?
   - ¿Dónde alojan datos?
   - ¿Cómo manejan consentimiento y baja de suscriptores?
   - ¿Tienen casos de éxito públicos?
4. Pregunta a 10 prospects si conocen EnviaMas, por qué la usarían y por qué no.

---

## 2. Tres gaps de mercado que podrías explotar

No intentes ganar “por features” contra Mailchimp o Brevo. Ellos tienen más recursos. Debes ganar en un segmento específico, con una oferta más local, más simple y más orientada a resultado.

### Gap 1: “Time-to-first-campaign” para pymes LATAM no técnicas

#### El gap

Muchas pymes LATAM no necesitan una plataforma con 200 features. Necesitan enviar su primera campaña bien hecha, sin que caiga en spam, sin entender HTML, sin configurar dominios y sin perderse.

Mailchimp y Brevo son self-serve. Eso funciona para usuarios digitales, pero deja afuera a muchos dueños de pymes que:

- No saben qué es SPF/DKIM/DMARC.
- No saben segmentar.
- No saben importar contactos correctamente.
- Tienen miedo de caer en spam.
- No tienen tiempo para aprender.
- Quieren “que alguien lo haga conmigo”.

#### Cómo explotarlo

Conviértete en la plataforma con onboarding humano local:

- Migración desde Mailchimp/Brevo en 24/48 horas.
- Configuración de dominio y autenticación.
- Importación y limpieza de base.
- Primera campaña lista en 7 días.
- Plantillas por industria.
- Soporte por WhatsApp en español.
- Checklist de entregabilidad.

#### Métrica de validación

- % de clientes que envían su primera campaña en menos de 7 días.
- Tiempo promedio desde registro hasta primer envío.
- Tasa de activación: cuenta creada → dominio verificado → lista importada → campaña enviada.
- Meta inicial: >70% de pilotos activos envían campaña en 7 días.

---

### Gap 2: Pricing, facturación y pagos locales para pymes LATAM

#### El gap

Muchas plataformas globales cobran en USD/EUR, con tarjeta internacional, facturación poco clara para contadores locales y poca adaptación a la realidad de la pyme LATAM.

Para una pyme, esto importa mucho:

- Necesita factura local.
- Quiere pagar con transferencia, OXXO, PIX, PSE, Mercado Pago, tarjeta local o efectivo según país.
- Le preocupa el tipo de cambio.
- Tiene presupuestos más bajos que una pyme de EE.UU. o Europa.
- No quiere sorpresas por overages.

#### Cómo explotarlo

Construye una oferta local clara:

- Precios en moneda local o al menos con referencia local.
- Planes simples por contactos y envíos.
- Sin sorpresas: “esto incluye X envíos; si te pasas, te avisamos antes de cobrar”.
- Facturación local si puedes.
- Pagos con métodos locales.
- Contratos flexibles: mensual, trimestral, anual con descuento.
- Para WhatsApp: costos de conversación separados y visibles.

#### Ejemplo de pricing piloto

No copies el free tier infinito de Brevo. Para una startup pequeña, un free tier amplio puede ser peligroso si atrae usuarios que no pagan y consumen soporte.

Plan piloto sugerido:

| Plan | Precio sugerido | Incluye | Objetivo |
|---|---:|---|---|
| Starter | US$19-29/mes o equivalente local | 1,000 contactos, 5,000 emails, 1 usuario, plantillas básicas, soporte por email/WhatsApp en horario hábil | Entrada |
| Growth | US$49-79/mes | 5,000 contactos, 20,000 emails, WhatsApp Business API o click-to-WhatsApp, 5 automations, soporte prioritario | Plan principal |
| Local Pro | US$99-149/mes | 10,000 contactos, 50,000 emails, onboarding humano, migración, entregabilidad, 2 usuarios | High-touch |

Ajusta por país. Ejemplos aproximados para probar, no los tomes como verdad final:

- México: MXN $399-$1,499/mes.
- Colombia: COP $80,000-$300,000/mes.
- Chile: CLP $18,000-$60,000/mes.
- Perú: PEN $70-$250/mes.
- Argentina: precio local con cuidado por inflación y poder adquisitivo.
- Brasil: solo si tienes portugués, PIX, nota fiscal y LGPD bien resueltos.

#### Métrica de validación

- Conversión de visita a pricing → solicitud de demo/prueba.
- % de prospectos que abandonan por precio o método de pago.
- % de clientes que pagan con método local.
- Churn por precio.
- CAC payback: idealmente menor a 3 meses para SMB.

---

### Gap 3: Email + WhatsApp para recuperar ventas en e-commerce y servicios LATAM

#### El gap

En LATAM, WhatsApp es un canal de venta real. Muchas pymes ya venden por WhatsApp, pero sus herramientas de email marketing suelen estar desconectadas de esa realidad.

Mailchimp y Brevo pueden hacer email, pero la pyme LATAM muchas veces necesita:

- Recuperar carritos abandonados con email + WhatsApp.
- Enviar recordatorios de cita.
- Reactivar clientes inactivos.
- Pedir reseñas.
- Confirmar pedidos.
- Avisar stock.
- Hacer seguimiento postventa.
- Medir ventas atribuidas, no solo opens/clicks.

#### Cómo explotarlo

No vendas “email marketing”. Vende “recuperación de ventas” y “reactivación de clientes”.

Paquetes de automatizaciones listos para LATAM:

1. **Carrito abandonado**
   - Email 1: 1 hora después.
   - Email 2: 24 horas después.
   - WhatsApp: 48 horas después, si hay opt-in.
   - Descuento opcional o envío gratis.

2. **Reactivación de clientes inactivos**
   - Segmento: no compra en 60/90 días.
   - Email: “Te extrañamos + oferta”.
   - WhatsApp: recordatorio con botón de compra.

3. **Postventa / reseña**
   - Email 3 días después de entrega.
   - WhatsApp para pedir calificación.
   - Cupón para segunda compra.

4. **Cumpleaños / aniversario**
   - Email automático.
   - WhatsApp opcional.
   - Cupón con vencimiento corto.

5. **Recordatorio de cita / reserva**
   - Clínicas, salones, talleres, consultores.
   - Email + WhatsApp 24h antes.
   - Reducción de no-shows.

#### Importante con WhatsApp

No hagas spam por WhatsApp. Meta es estricto y el usuario LATAM también se cansa rápido.

Necesitas:

- Opt-in explícito.
- Plantillas aprobadas si usas WhatsApp Business API.
- Segmentación por intención.
- Frecuencia baja y relevante.
- Métricas de clic y conversión.
- Costos de conversación separados del plan.

#### Métrica de validación

- % de clientes que activan al menos una automatización.
- % de clientes con ventas atribuidas en 30 días.
- Ingreso promedio atribuido por cliente.
- Tasa de clic en WhatsApp.
- Tasa de opt-in de WhatsApp.
- Tasa de respuesta en WhatsApp.

---

## 3. Posicionamiento diferenciador para tu startup

No te posiciones como:

> “Somos otra herramienta de email marketing para pymes.”

Eso es commodity. Mailchimp y Brevo ganan ahí.

Posiciónate como:

> “La plataforma de retención y recuperación de ventas para pymes LATAM que convierte tu base de clientes en ingresos usando email + WhatsApp, con soporte humano local y configuración guiada.”

### Posicionamiento recomendado

**Categoría:**  
Retención y recuperación de ventas para pymes LATAM.

**Target inicial:**  
Pymes de e-commerce o servicios en un país específico, con 1,000 a 20,000 contactos, que ya usan WhatsApp para atender o vender, y que no tienen equipo de marketing.

**Promesa:**  
Lanza tu primera campaña rentable en 7 días, sin equipo técnico y sin perderte en una herramienta global.

**Diferenciador:**  
No te dejamos solo con una plataforma. Te acompañamos con onboarding local, plantillas por industria, entregabilidad configurada y automatizaciones listas para vender.

### Mensaje para landing

**H1:**  
Recupera ventas y reactiva clientes con email + WhatsApp en 7 días.

**Subtítulo:**  
Para pymes de [país/nicho] que no tienen equipo de marketing. Configuramos tu dominio, importamos tu base y lanzamos tu primera automatización con soporte humano en español.

**CTA principal:**  
Empezar piloto.

**CTA secundario:**  
Ver cómo migrar desde Mailchimp/Brevo.

**Sección de confianza:**  
- Migración en 24/48 horas.
- Configuración de entregabilidad incluida.
- Plantillas listas para [nicho].
- Soporte local por WhatsApp.
- Precios simples en moneda local.

**Oferta piloto sugerida:**  
“Primeros 20 clientes: setup guiado gratis a cambio de feedback y testimonial.”

O, si quieres ser más agresivo:

“Si en 7 días no envías tu primera campaña, te devolvemos el mes.”

Solo haz esta garantía si tu onboarding realmente puede cumplirlo.

### Ángulo de ataque contra Mailchimp

No digas: “Mailchimp es malo”.

Di:

> “Mailchimp es excelente para equipos que ya saben usarlo. Nosotros ayudamos a pymes que no tienen tiempo: configuramos tu cuenta, limpiamos tu base, autenticamos tu dominio y lanzamos tu primera campaña en 7 días, con soporte local.”

### Ángulo de ataque contra Brevo

No digas: “Brevo no sirve”.

Di:

> “Brevo puede ser muy conveniente por precio, pero muchas pymes se quedan solas configurando. Nosotros te acompañamos con onboarding humano, plantillas por industria y automatizaciones pensadas para vender en LATAM.”

### Ángulo contra EnviaMas

Como no conoces bien a EnviaMas, no ataques directamente. Compite con prueba:

> “No te quedes con promesas. Pide una demo, pregunta por entregabilidad, integraciones, soporte y casos reales. Nosotros te mostramos cómo migrar y lanzar en días.”

---

## 4. Qué hacer en los próximos 90 días

Meta concreta para los próximos 90 días:

> Conseguir 10-20 clientes pagos con alta activación, o demostrar rápido que la oferta/ICP debe cambiar.

No intentes escalar antes de validar:

- Activación.
- Retención.
- Disposición a pagar.
- Costo de adquisición.
- Unit economics básicos.

---

## Supuesto de beachhead

Si todavía no tienes un segmento claro, te propongo uno para probar:

**Beachhead sugerido:**  
Pymes de e-commerce o servicios en México, Colombia, Chile o Perú, con 1,000-20,000 contactos, que venden por WhatsApp y tienen una tienda online simple o catálogo.

Ejemplos:

- Tiendas de moda.
- Belleza/cosmética.
- Accesorios.
- Suplementos.
- Servicios de salud/estética.
- Talleres.
- Academias pequeñas.
- Servicios profesionales con citas.

Evita por ahora:

- Enterprise.
- Negocios sin base de datos.
- Negocios que solo quieren “enviar promos” sin estrategia.
- Brasil, si no tienes portugués, PIX, facturación local y LGPD bien resueltos.
- Todos los países a la vez.

---

## Días 0-10: Elegir foco y validar dolor

### Objetivo

Salir de la ambigüedad: “email marketing para pymes LATAM” es demasiado amplio. Necesitas un nicho concreto.

### Acciones concretas

#### 1. Elige un país y un vertical

Ejemplo:

- País: México.
- Vertical: e-commerce de moda/belleza con 1k-20k contactos.
- Canal: WhatsApp Business.
- Dolor: baja recompra y carritos abandonados.

O:

- País: Colombia.
- Vertical: servicios de salud/estética con citas.
- Dolor: no-shows y reactivación de pacientes.

No elijas cinco. Elige uno.

#### 2. Crea una lista de 100 prospects

Fuentes:

- Instagram Shops.
- Tiendas en Shopify/Tiendanube.
- Mercado Libre.
- Directorios locales.
- Cámaras de comercio.
- Grupos de emprendedores.
- LinkedIn.
- Comunidades de e-commerce.
- Referidos de tu red.

Crea una hoja de cálculo:

| Empresa | País | Vertical | Contacto | Canal | Base estimada | Herramienta actual | WhatsApp | Estado |
|---|---|---|---|---|---|---|---|---|

#### 3. Haz 20 entrevistas

No vendas todavía. Diagnostica.

Preguntas:

1. ¿Qué herramienta de email usas hoy?
2. ¿Cuánto pagas?
3. ¿Cuántos contactos tienes?
4. ¿Cómo conseguiste esos contactos?
5. ¿Tienes consentimiento explícito?
6. ¿Cuándo enviaste la última campaña?
7. ¿Sabes cuántas ventas generó?
8. ¿Qué te frustra más: precio, complejidad, soporte, entregabilidad, plantillas, integraciones?
9. ¿Usas WhatsApp para vender?
10. ¿Tienes WhatsApp Business normal o API?
11. ¿Te gustaría recuperar carritos, reactivar clientes o aumentar recompra?
12. ¿Pagarías US$29-79/mes por una campaña lista en 7 días?
13. ¿Qué te impediría probar una nueva herramienta?

#### 4. Haz teardown de competidores

Crea cuentas gratuitas en Mailchimp y Brevo.

Mide:

- Tiempo desde registro hasta primer envío.
- Facilidad de importar contactos.
- Facilidad de autenticar dominio.
- Calidad del soporte en español.
- Precio para 5,000 contactos y 20,000 envíos.
- Si ofrecen WhatsApp/SMS nativo.
- Si tienen plantillas por industria.
- Si hay fricción de pago para LATAM.

Para EnviaMas:

- Pide demo.
- Graba la llamada.
- Pregunta pricing.
- Pregunta integraciones.
- Pregunta soporte.
- Pregunta casos de éxito.
- Pregunta cómo manejan entregabilidad.

#### 5. Define tu oferta piloto

Ejemplo:

**Piloto “Primera campaña en 7 días”**

Incluye:

- Setup de cuenta.
- Verificación de dominio.
- SPF/DKIM/DMARC.
- Importación de hasta 5,000 contactos.
- Limpieza básica de base.
- Segmentación inicial.
- 3 plantillas listas.
- 1 automatización: carrito abandonado o reactivación.
- Soporte por WhatsApp.
- Precio fundador: US$29/mes durante 3 meses.
- Setup gratis a cambio de testimonial.

### Entregables de esta fase

- ICP definido.
- 20 entrevistas realizadas.
- Top 3 dolores priorizados.
- Comparativa real de Mailchimp/Brevo/EnviaMas.
- Oferta piloto con precio.
- Lista de 100 prospects.

### KPIs

- 20 entrevistas.
- 10 prospectos calificados.
- 3-5 demos agendadas.
- 1 hipótesis de pricing validada.

---

## Días 11-30: Construir la oferta mínima y generar pipeline

### Objetivo

No construir una plataforma completa. Construir la máquina de adquisición y activación.

### Acciones concretas

#### 1. Crea una landing específica

No hagas una landing genérica.

Estructura:

1. H1 con promesa.
2. Subtítulo con ICP.
3. Tres bullets de beneficio.
4. Cómo funciona en 3 pasos.
5. Comparación simple contra Mailchimp/Brevo.
6. Oferta piloto.
7. Testimonios si tienes.
8. FAQ.
9. Calendario para demo.

Ejemplo de copy:

**H1:**  
Recupera carritos y reactiva clientes con email + WhatsApp.

**Sub:**  
Para tiendas y servicios en [país] que no tienen equipo de marketing. Te ayudamos a configurar tu dominio, importar tu base y lanzar tu primera campaña en 7 días.

**CTA:**  
Agendar diagnóstico gratuito.

#### 2. Construye el MVP mínimo

No construyas todo. Prioriza solo lo que desbloquea valor:

Must-have:

- Importación CSV.
- Gestión básica de listas.
- Segmentación simple.
- Editor de plantillas.
- Envío de campañas.
- Unsubscribe visible.
- Registro de consentimiento.
- Autenticación de dominio: SPF/DKIM/DMARC.
- Métricas: envío, apertura, clic, rebote, spam complaints.
- UTM automático para medir tráfico/ventas.
- Integración básica con WhatsApp: click-to-WhatsApp o API si ya la tienes.

Nice-to-have, pero no prioritario:

- CRM completo.
- Editor drag-and-drop perfecto.
- SMS global.
- SSO.
- Roles avanzados.
- Multi-idioma.
- 50 integraciones.
- Marketplace de plantillas.
- AI generativa compleja.

#### 3. Crea 3 automatizaciones empaquetadas

Paquete 1: Carrito abandonado.

- Email 1: 1 hora.
- Email 2: 24 horas.
- WhatsApp: 48 horas.
- Objetivo: recuperar venta.

Paquete 2: Reactivación.

- Segmento: no compra en 60/90 días.
- Email: oferta con urgencia.
- WhatsApp: recordatorio.
- Objetivo: segunda compra.

Paquete 3: Postventa/reseña.

- Email: gracias + cómo usar producto.
- Email: pedir reseña.
- WhatsApp: calificación rápida.
- Objetivo: confianza y recompra.

#### 4. Crea una guía de migración

Título:

> “Migra desde Mailchimp o Brevo en 24 horas sin perder tus contactos.”

Incluye:

- Exportar contactos desde Mailchimp/Brevo.
- Mapeo de campos.
- Limpieza de rebotes.
- Reconfirmación si la lista es vieja.
- Configuración de dominio.
- Prueba de entregabilidad.
- Primera campaña de prueba.

#### 5. Lanza outreach directo

No esperes inbound.

Canal prioritario:

- WhatsApp si tienes contacto directo.
- Email personalizado.
- LinkedIn.
- Instagram DM para tiendas pequeñas.

Script corto:

> Hola [nombre], vi que [empresa] vende por [canal]. Estamos ayudando a pymes de [país/nicho] a recuperar carritos y reactivar clientes con email + WhatsApp, sin depender solo de anuncios.  
>   
> Tenemos un piloto con setup guiado y primera campaña en 7 días. ¿Te interesa ver 3 plantillas listas para [nicho]? Si no te encaja, no te cobro el setup.  
>   
> ¿Tienes 10 minutos esta semana?

Follow-up 1:

> Hola [nombre], te comparto un ejemplo de flujo para [nicho]: carrito abandonado + reactivación + postventa. Si quieres, te lo dejo configurado en una demo de 15 minutos.

Follow-up 2:

> Hola [nombre], ¿tu principal problema hoy es que no tienes tiempo, que la herramienta es cara, o que no sabes por dónde empezar?

#### 6. Habla con 5 posibles partners

No vendas solo directo.

Partners posibles:

- Agencias pequeñas de marketing.
- Consultores de e-commerce.
- Contadores que atienden pymes.
- Proveedores de POS.
- Comunidades de emprendedores.
- Integradores de Shopify/Tiendanube.
- Agencias de WhatsApp Business.

Oferta partner:

- 20% recurring durante el primer año.
- Co-marketing.
- Plantillas co-branded.
- Onboarding prioritario para sus clientes.
- Reporte simple para que el partner muestre ROI.

### Entregables de esta fase

- Landing publicada.
- MVP mínimo usable.
- 3 automatizaciones empaquetadas.
- Guía de migración.
- 100 prospects contactados.
- 5 conversaciones con partners.

### KPIs

- 500+ visitas a landing.
- 30 leads.
- 15 llamadas/demos.
- 5-10 pilotos pagos o comprometidos.
- 3 partners interesados.

---

## Días 31-60: Onboarding de pilotos y primeros casos de éxito

### Objetivo

Que los primeros clientes obtengan resultado rápido. No busques perfección técnica; busca aprendizaje, activación y prueba social.

### Acciones concretas

#### 1. Onboarding en 48 horas

Checklist:

- Cuenta creada.
- Dominio verificado.
- SPF/DKIM/DMARC configurados.
- Base importada.
- Duplicados eliminados.
- Hard bounces suprimidos.
- Unsubscribes previos respetados.
- Segmentos iniciales creados:
  - Clientes activos.
  - Inactivos 60 días.
  - Inactivos 90 días.
  - Carritos abandonados.
  - Leads sin compra.
- Primera plantilla aprobada.
- Primera campaña programada.

#### 2. Lanza la primera campaña en 7 días

Campañas recomendadas para empezar:

**Opción A: Reactivación simple**

Asunto:  
“[Nombre], te dejamos algo para tu próxima compra”

Cuerpo:

- Saludo corto.
- Beneficio claro.
- Cupón con vencimiento.
- Botón de compra.
- Botón de WhatsApp.
- Unsubscribe visible.

**Opción B: Carrito abandonado**

Email 1:  
“¿Olvidaste algo?”

Email 2:  
“Tu carrito sigue disponible”

WhatsApp:  
“Hola [nombre], vimos que dejaste tu carrito. ¿Te ayudamos a completar la compra?”

**Opción C: Postventa**

Asunto:  
“Gracias por tu compra, [nombre]”

Cuerpo:

- Gracias.
- Tips de uso.
- Pedido de reseña.
- Cupón para segunda compra.

#### 3. Mide entregabilidad desde el día 1

Métricas objetivo:

- Bounce rate <2%.
- Spam complaints <0.1%.
- Unsubscribe rate razonable según industria.
- Open rate no como métrica principal, pero útil como señal.
- CTR >1-2% como referencia inicial.
- Clics a WhatsApp medibles.
- Ventas atribuidas con UTM.

Reglas:

- No importar listas compradas.
- No enviar a contactos viejos sin reconfirmación si la lista es riesgosa.
- Suprimir hard bounces automáticamente.
- Respetar bajas inmediatamente.
- Calentar dominio si es nuevo.
- Enviar primero a segmentos más engaged.

#### 4. Instala medición de ventas

Mínimo:

- UTMs en todos los links.
- Integración con Google Analytics 4 si aplica.
- Parámetros:
  - `utm_source=tu_plataforma`
  - `utm_medium=email` o `whatsapp`
  - `utm_campaign=carrito_abandonado`
  - `utm_content=variante_a`
- Si hay e-commerce, medir:
  - Sesiones.
  - Add to cart.
  - Checkout iniciado.
  - Compra.

Si no puedes integrar e-commerce aún, usa:

- Link corto con UTM.
- Código de cupón específico.
- Pregunta en checkout: “¿Cómo nos encontraste?”
- Registro manual de ventas por WhatsApp.

#### 5. Consigue testimonios

Después de la primera campaña:

- ¿Te fue fácil?
- ¿Qué resultado viste?
- ¿Qué era lo que más te preocupaba antes?
- ¿Qué te hizo elegirnos?
- ¿Nos recomendarías?
- ¿Puedo usar tu logo/testimonio?

Pide:

- Captura de ventas.
- Frase corta.
- Video de 30 segundos si es posible.
- Métrica específica: “Recuperamos X ventas en 14 días”.

### Entregables de esta fase

- 10 pilotos activos.
- 8 campañas enviadas.
- 5 automatizaciones activas.
- 3 casos de éxito.
- 2-3 testimonios.
- Dashboard de activación y retención.

### KPIs

- 80% de clientes envían primera campaña en 7 días.
- 50% activan al menos una automatización.
- Bounce <2%.
- Spam complaints <0.1%.
- NPS >40.
- Al menos 3 clientes con ventas atribuidas.

---

## Días 61-90: Decidir si escalar o pivotar

### Objetivo

No es “hacer más marketing”. Es decidir con datos si el negocio tiene una cuña real.

### Acciones concretas

#### 1. Analiza cohortes

Preguntas:

- ¿Cuántos clientes siguen activos después de 30 días?
- ¿Cuántos enviaron más de una campaña?
- ¿Cuántos usan automatizaciones?
- ¿Cuántos ven ventas atribuidas?
- ¿Cuántos pagarían más?
- ¿Cuál fue la objeción más repetida?
- ¿Qué segmento tuvo mejor activación?
- ¿Qué vertical tuvo mejor resultado?
- ¿Qué canal trajo mejores clientes?

#### 2. Define criterios de éxito

Para seguir escalando, idealmente deberías ver:

- Activación: >70% envían primera campaña en 7 días.
- Retención 30 días: >70% de clientes siguen activos.
- Uso recurrente: >50% envían al menos 2 campañas al mes.
- Automatización: >30-50% activan un flujo.
- NPS: >40.
- Churn mensual: <5-8% en pilotos pequeños.
- CAC payback: <3 meses si el ticket es SMB.
- Al menos 3 clientes con ROI visible.

Si no llegas, no escales. Cambia:

- ICP.
- País.
- Vertical.
- Precio.
- Oferta.
- Onboarding.
- Mensaje.

#### 3. Sube precios si validaste valor

Precio piloto no debe ser eterno.

Si tienes resultados:

- Sube de US$29 a US$49.
- O de US$49 a US$79.
- O cobra setup de US$99-199 después de los primeros 10-20 clientes.
- Ofrece anual con descuento para financiar onboarding.

No regales soporte humano. Es caro. Si lo regalas, debe ser a cambio de:

- Testimonio.
- Caso de éxito.
- Pago anual.
- Referido.
- Acceso a datos de performance.

#### 4. Lanza campaña de migración

Campaña específica:

**Nombre:**  
“Migra desde Mailchimp/Brevo en 24 horas.”

Mensaje:

> ¿Pagas Mailchimp o Brevo pero no tienes tiempo para configurarlo bien? Migramos tus contactos, configuramos tu dominio y lanzamos tu primera campaña en 7 días, con soporte local.

Incluye:

- Checklist de migración.
- Comparativa de costo para 5,000 contactos.
- Garantía de onboarding.
- Demo de 15 minutos.

#### 5. Crea un benchmark local

Con datos de tus pilotos, publica algo concreto:

Ejemplo:

> “Pymes de moda en México recuperaron X% de carritos abandonados con email + WhatsApp en 30 días.”

O:

> “Clínicas estéticas en Colombia redujeron no-shows X% con recordatorios por email + WhatsApp.”

No inventes. Usa datos reales, aunque sean pequeños. Di:

> “Resultados de pilotos iniciales con N clientes.”

#### 6. Activa partners

Ofrece:

- 20% recurring el primer año.
- Kit de venta.
- Demo conjunta.
- Onboarding prioritario.
- Reporte mensual simple.
- Plantillas por vertical.

#### 7. Construye una máquina de referidos

Oferta:

- Cliente refiere a otro: 1 mes gratis o descuento.
- Partner refiere: comisión.
- Testimonio a cambio de setup gratis.
- Caso de éxito a cambio de descuento trimestral.

### Entregables de esta fase

- 20 clientes pagos o decisión de pivot.
- 3 casos de éxito.
- Playbook de onboarding.
- Playbook de migración.
- Pricing actualizado.
- Partner program básico.
- Dashboard semanal.

### KPIs finales

- 10-20 clientes pagos.
- MRR inicial: US$500-1,500 dependiendo pricing.
- Active sender rate: >70%.
- Retención 30 días: >70%.
- NPS: >40.
- CAC payback: <3 meses.
- Al menos 5 clientes con automatización activa.
- Al menos 3 clientes con ventas atribuidas.

---

## Lo que no deberías hacer

1. **No lances un free tier ilimitado.**  
   Puede atraer usuarios que nunca pagan y consumen soporte.

2. **No intentes competir con Mailchimp en features.**  
   Perderás por recursos. Gana en tiempo a valor y contexto local.

3. **No vendas a “todas las pymes de LATAM”.**  
   Elige país, vertical y caso de uso.

4. **No construyas 30 integraciones antes de tener 10 clientes.**  
   Primero CSV, plantillas, autenticación, campañas y automations clave.

5. **No prometas entregabilidad sin configurar dominio.**  
   Obliga o guía fuertemente SPF/DKIM/DMARC.

6. **No uses listas compradas.**  
   Arruinarás entregabilidad y reputación.

7. **No metas WhatsApp como canal de spam.**  
   Necesitas opt-in, relevancia y control de frecuencia.

8. **No ignores costos de WhatsApp.**  
   Las conversaciones pueden comer margen si las incluyes sin control.

9. **No escales paid ads antes de validar activación.**  
   Primero onboarding y retención. Luego adquisición.

10. **No copies precios de EE.UU. sin adaptar.**  
   LATAM requiere sensibilidad de precio, moneda y método de pago.

---

## Mi recomendación estratégica concreta

Si tuviera que priorizar una sola apuesta para ti:

> Conviértete en la plataforma de “recuperación de ventas” para pymes LATAM que ya tienen clientes pero no saben cómo hacerlos volver, combinando email + WhatsApp con onboarding humano local.

No vendas email marketing. Vende:

- Recuperar carritos.
- Reactivar clientes inactivos.
- Aumentar recompra.
- Reducir no-shows.
- Generar segunda venta.
- Medir ingresos atribuidos.

Eso es más fácil de vender que “campañas de email”.

### Oferta concreta para ejecutar ya

**Nombre del piloto:**  
“Primera venta recuperada en 7 días.”

**Incluye:**

1. Migración de contactos.
2. Configuración de dominio.
3. Limpieza básica de lista.
4. Segmentación inicial.
5. Plantilla por industria.
6. Automatización de carrito abandonado o reactivación.
7. Botón de WhatsApp con opt-in.
8. Medición con UTM.
9. Soporte por WhatsApp.
10. Precio fundador: US$29-49/mes durante 3 meses.

**Condición:**  
Setup gratis a cambio de feedback semanal y testimonial si hay resultado.

**Meta:**  
Conseguir 10 clientes piloto en 30-45 días.

Si no consigues 10 pilotos con esa oferta, el problema probablemente es uno de estos:

- ICP equivocado.
- País equivocado.
- Precio equivocado.
- Falta de confianza.
- Producto demasiado crudo.
- Mensaje demasiado genérico.

---

## Resumen ejecutivo

1. **Mailchimp** gana en marca, integraciones y self-serve, pero puede ser caro/complejo para pyme LATAM.
2. **Brevo** gana en costo por volumen, contactos ilimitados y multicanal, pero puede dejar solo al usuario no técnico.
3. **EnviaMas** es incógnita. Valídala con teardown directo; no asumas fortalezas ni debilidades.
4. Tu oportunidad no es hacer “otro Mailchimp”.
5. Tu oportunidad es:
   - Onboarding humano local.
   - Entregabilidad resuelta.
   - Precio/pagos locales.
   - Email + WhatsApp orientados a ventas.
   - Plantillas por industria.
   - Tiempo a valor en 7 días.
6. En 90 días, consigue 10-20 clientes pagos con activación alta y casos de éxito.
7. Si la activación y retención no funcionan, pivota ICP/oferta antes de escalar.