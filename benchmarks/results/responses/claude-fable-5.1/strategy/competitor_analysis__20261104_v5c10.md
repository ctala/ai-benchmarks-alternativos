# Claude Fable 5.1 — strategy/competitor_analysis

- model_id: `anthropic/claude-fable-5.1`
- success: True  | final: 7.7 | quality: 10.0
- latency_total: 123.096s | tokens_per_second: 65.4
- input_tokens: 276 | output_tokens: 8056

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

Antes de empezar, dos advertencias honestas:

- **Sobre "EnviaMas": no tengo información confiable.** No la reconozco con certeza como un jugador identificable; puede ser muy pequeña, muy nueva, o tener otro nombre comercial. No voy a inventar su pricing. Lo que sí puedo hacer es usar como proxy a los competidores locales que sí conozco (Doppler y Perfit en Argentina/LATAM, SendPulse con fuerte presencia regional, Acumbamail/Mailrelay desde España) porque "EnviaMas" casi seguro compite con el mismo playbook. Si me pegás su página de pricing y features, la agrego a la tabla.
- **Los precios de Mailchimp y Brevo cambian seguido** (Mailchimp subió precios en 2023 y 2024). Los números que doy son referenciales de mi último conocimiento; verificá las páginas de pricing hoy mismo antes de usar esto en un deck.

---

## 1. Tabla comparativa

| | **Mailchimp** (Intuit) | **Brevo** (ex-Sendinblue) | **"EnviaMas"** (sin datos) / proxy: jugador local tipo Doppler-Perfit |
|---|---|---|---|
| **Modelo de pricing** | Por **contactos** (y límite de envíos = ~10x contactos). Free: 500 contactos / 1.000 envíos mes, con branding. Essentials desde ~US$13/mes (500 contactos). Standard desde ~US$20/mes. Premium desde ~US$350/mes. A 10k contactos, Standard ronda los US$100/mes. Facturado en USD. | Por **volumen de envío**, contactos ilimitados. Free: 300 emails/día. Starter desde ~US$9/mes (5k emails). Business desde ~US$18/mes (automatización completa, A/B, multiusuario). Quitar logo es add-on. WhatsApp y SMS se cobran aparte (pass-through de Meta + margen). USD/EUR. | **No lo sé.** Patrón típico del local: plan gratis limitado, planes desde ~US$10–30 equivalentes, a veces facturación en moneda local y con factura fiscal. Si EnviaMas no factura en moneda local, no es realmente "local" en lo que importa. |
| **Features principales** | Editor drag-and-drop muy pulido, biblioteca de templates grande, Customer Journey Builder, segmentación, landing pages, formularios, reportes, integración QuickBooks, integraciones con casi todo (Shopify, WooCommerce, Zapier). Sin WhatsApp nativo. | Email + **SMS + WhatsApp** + chat + CRM de ventas + **email transaccional (SMTP/API)** en una sola cuenta. Automatización decente, landing pages. | Patrón típico: email + automatizaciones básicas, integración con **Tiendanube/Nuvemshop** y a veces VTEX/Mercado Libre (esto es lo que hace Perfit bien), soporte en español. |
| **Mercado target** | Pymes globales, muy US-centric. Creadores, e-commerce Shopify, "solopreneurs". | Pymes europeas sensibles a precio, empresas que necesitan transaccional + marketing juntos. | Pymes de 1–3 países LATAM, muchas veces un vertical (e-commerce o agencias). |
| **Fortalezas** | Marca (es el "Kleenex" de la categoría), onboarding muy fácil, ecosistema de integraciones, templates. | Pricing que no castiga el crecimiento de lista, multicanal real, transaccional incluido, UI en español y portugués, cumplimiento GDPR. | Soporte humano en español en horario local, cobro en moneda local (a veces), integraciones con tiendas locales, conocimiento del contexto (Hotmail/Outlook muy usado en México, dominios sin autenticar, etc.). |
| **Debilidades** | Precio en USD y subiendo; te cobra por contactos aunque no les envíes; soporte en español limitado (chat/email, no teléfono salvo Premium); sin medios de pago locales; sin WhatsApp; requiere dominio autenticado (desde feb 2024 por reglas de Google/Yahoo) y el wizard está pensado para usuarios US. | Marca débil en LATAM; editor y templates menos pulidos; percepción de deliverability mediocre en planes bajos (IPs compartidas); WhatsApp caro y con fricción de verificación Meta; soporte en español mejorable; sin facturación local. | Típicamente: producto menos pulido, menos integraciones, menos inversión en deliverability, dependencia de 1–2 países, marca desconocida fuera de su nicho. **Esto es lo que tenés que confirmar sobre EnviaMas: ¿en qué país factura, con qué tienda se integra, y cuántos clientes tiene?** |

---

## 2. Tres gaps de mercado que podrías explotar

Aclaración importante: "ser local" **no es un gap**, Doppler, Perfit y SendPulse ya lo hacen. El gap está en combinaciones específicas que nadie cubre bien.

### Gap 1: Cobro en moneda local + factura fiscal válida + medios de pago locales, en más de un país
- Mailchimp y Brevo cobran en USD con tarjeta internacional. En Argentina eso significa impuesto PAIS/percepciones y tarjetas bloqueadas; en Brasil, muchas pymes no tienen tarjeta internacional y quieren boleto/Pix y Nota Fiscal; en Colombia y México, la pyme quiere factura deducible (CFDI en México).
- Los locales resuelven esto **en un solo país**. Nadie lo hace bien en los 4–5 mercados grandes a la vez.
- Qué implica construir: Mercado Pago + Pix/boleto + PSE + OXXO/SPEI, y emisión de factura fiscal en cada jurisdicción (podés usar un proveedor tipo Facturante/Alegra/Nubimetrics según país, no lo construyas vos).
- Es aburrido, es trabajo de plomería, y por eso nadie lo hace. Eso es exactamente lo que lo hace defendible.

### Gap 2: Email + WhatsApp orquestados en un mismo journey, con pricing predecible para pymes
- En LATAM WhatsApp es el canal #1 de la pyme. Brevo tiene WhatsApp pero: (a) la verificación de Meta Business es una pesadilla para una pyme sin equipo, (b) el pricing por conversación de Meta es opaco y cambia, (c) Brevo no te ayuda con el onboarding de Meta.
- Mailchimp directamente no lo tiene.
- El gap no es "tener WhatsApp" (eso lo da cualquier BSP), es **"te hacemos el onboarding de Meta Business y te vendemos un paquete de X emails + Y conversaciones de WhatsApp a precio fijo mensual"**. La pyme no quiere entender el pricing de Meta, quiere un número.
- Cuidado: los márgenes en WhatsApp son finos porque Meta se lleva la mayor parte. Usalo como gancho de adquisición, no como motor de margen.

### Gap 3: Onboarding de deliverability para pymes sin infraestructura (el problema del "mando desde Gmail")
- Desde febrero 2024, Google y Yahoo exigen SPF/DKIM/DMARC para remitentes masivos. Una enorme porción de pymes LATAM: no tiene dominio propio, o lo tiene pero no sabe entrar al DNS, o lo compró en un registrador local sin documentación en español.
- Mailchimp y Brevo te muestran un wizard en inglés y te dicen "pegá estos registros en tu DNS". La pyme se cae ahí y culpa a la herramienta.
- Oportunidad concreta: (a) flujo de autenticación guiado en español con instrucciones por registrador (GoDaddy, Hostinger, DonWeb, NIC.ar, Registro.br, Hostgator MX), (b) opción de **subdominio provisto por vos** (`pyme.tudominio.com`) con reputación cuidada para quien no tiene dominio, (c) warm-up automático.
- Esto además mejora tu deliverability agregada, que es el activo más difícil de copiar en este negocio.

(Gap honorable: cumplimiento de **LGPD/Ley 1581/LFPDPPP/Ley 25.326** con templates de consentimiento y footer legal por país. Es menor como diferenciador de venta pero importante para cerrar pymes más formales.)

---

## 3. Posicionamiento sugerido

**No te posiciones como "el Mailchimp barato de LATAM".** Es la trampa de todos los locales: competir en precio contra alguien que puede bajar precio cuando quiera, y en producto contra alguien con 10x tu equipo.

Posicionamiento propuesto (formato clásico):

> Para **pymes que venden online en [país inicial]** (dueños que gestionan solos el marketing, 500–20.000 contactos), **[tu marca]** es la plataforma de email + WhatsApp que **se conecta a tu tienda [Tiendanube/VTEX/Mercado Libre], se cobra en [moneda local] con factura, y te deja enviando con dominio autenticado en 15 minutos**, a diferencia de Mailchimp y Brevo, que cobran en dólares, no entienden tu tienda y te abandonan en el paso del DNS.

Puntos clave de este posicionamiento:
1. **Un país primero.** Hacer bien gap 1 en cinco países al día uno es imposible. Elegí por tamaño de mercado e-commerce + dolor de pago en USD. Mi recomendación: **Brasil** (mayor mercado, Pix, Nuvemshop enorme, barrera idiomática protege de Mailchimp) o **Argentina** (dolor de USD máximo, Tiendanube nació ahí, pero mercado chico e inestable). México es más grande pero la pyme mexicana tiene menos fricción con USD y Mailchimp está más instalado. Si tu equipo no habla portugués, Argentina para validar y Brasil como expansión #1.
2. **Un vertical de entrada: e-commerce.** Es donde el ROI del email es medible (carrito abandonado, post-compra, recompra), lo que te permite vender resultados en vez de features. Perfit ya hace esto en Argentina; tenés que ser mejor en WhatsApp + deliverability + facturación multi-país, o elegir otra plataforma de tienda donde Perfit sea débil.
3. **Pricing por envíos, no por contactos** (modelo Brevo). Es el argumento de venta más simple contra Mailchimp y la pyme lo entiende en 5 segundos: "no te cobramos por la gente a la que no le escribís".

---

## 4. Qué hacer en los próximos 90 días

Asumo que ya tenés un producto mínimo que envía emails. Si no, el plan cambia (decime).

### Días 1–15: Inteligencia y decisión de país
- **Auditar EnviaMas en serio**: crear cuenta, pagar el plan más bajo, ver en qué moneda cobra, qué factura emite, qué integraciones tiene, y mandar un ticket de soporte a las 20hs un viernes para medir respuesta. Hacé lo mismo con Doppler y Perfit. 3 horas, te ahorra meses.
- **20 entrevistas con pymes** (no encuesta: llamadas). Mitad que usan Mailchimp/Brevo, mitad que usan un local o nada. Preguntas que importan: ¿cómo pagás hoy y cuánto te cuesta realmente en moneda local con impuestos? ¿Tenés dominio propio? ¿Quién configuró tu DNS? ¿Usás WhatsApp para vender? ¿Qué tienda usás?
- **Decidir el país y la plataforma de tienda** con esos datos. Escribirlo en una página y no volver a discutirlo por 90 días.

### Días 15–45: Construir las tres cosas que te diferencian
- **Billing local**: integrar Mercado Pago (o Pix/boleto si Brasil) + emisión de factura fiscal vía proveedor tercero. No lo construyas desde cero.
- **Wizard de autenticación de dominio en español** con instrucciones por registrador, detección automática de registrador por NS, y chequeo en vivo de SPF/DKIM/DMARC. Esto es 1–2 semanas de un dev y es el feature que más retención te va a dar.
- **Integración con la tienda elegida** (Tiendanube tiene API pública y app store; VTEX también). Mínimo viable: sincronizar clientes y pedidos, un flujo de carrito abandonado y uno post-compra pre-armados.
- **Infraestructura de envío**: no armes tu propio MTA. Amazon SES, SparkPost o Postmark como backend, con IPs dedicadas cuando superes ~100k envíos/mes. Tu diferencial no es el MTA, es el onboarding.
- WhatsApp: **todavía no.** Validá primero que la gente paga por lo anterior.

### Días 45–75: Primeros clientes pagos
- Objetivo concreto: **15 clientes pagando** en moneda local. No "usuarios", pagando.
- Canal 1: la app store de la plataforma de tienda elegida (Tiendanube App Store, etc.). Es distribución gratis y filtrada.
- Canal 2: **3 agencias de marketing locales** que hoy revenden Mailchimp. Ofreceles 30% recurrente de por vida y un panel multi-cuenta. Las agencias odian explicarle a sus clientes el cobro en USD.
- Canal 3: una pieza de contenido específica, no genérica: *"Cómo autenticar tu dominio de [registrador local] para que Gmail no te mande a spam"* en español/portugués, por registrador. Es búsqueda de alta intención y nadie la cubre bien.
- Ofrecer **migración gratuita desde Mailchimp** (listas, templates, automatizaciones básicas). Hacelo a mano si hace falta. El costo de cambio es tu enemigo #1.

### Días 75–90: Medir y decidir
Métricas que importan a los 90 días:
- % de cuentas nuevas con dominio autenticado en las primeras 24 hs (meta: >70%; Mailchimp probablemente está muy por debajo de eso en LATAM, aunque no tengo el dato).
- Tasa de entrega e inbox placement en Gmail y Outlook/Hotmail (usá GlockApps o Mail-tester por cliente).
- Clientes pagos y churn del mes 1 (si churn >10% mensual, el problema es producto, no marketing).
- Cuántos clientes vinieron de la app store de la tienda vs. agencias vs. orgánico.
- **Decisión al día 90**: si tenés ≥15 pagos y churn <8%, arrancás WhatsApp (gap 2) y segundo país. Si no, el problema no es la falta de features: volvé a las entrevistas.

### Qué NO hacer en estos 90 días
- No construir landing pages, formularios bonitos ni "CRM". Mailchimp y Brevo ya ganaron ahí.
- No lanzar en 3 países a la vez.
- No competir con plan gratis generoso: atrae a quienes nunca van a pagar y destruye tu reputación de IP.
- No gastar en ads de marca. Nadie busca tu nombre todavía.

---

Si me pasás la página de pricing de EnviaMas, el país donde estás y qué plataforma de tienda usan tus primeros usuarios, afino la tabla y el plan con datos reales en vez de proxies.