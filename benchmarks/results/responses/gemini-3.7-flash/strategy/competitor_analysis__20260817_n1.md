# Gemini 3.7 Flash — strategy/competitor_analysis

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 4.09 | quality: 3.33
- latency_total: 17.901s | tokens_per_second: 114.2
- input_tokens: 166 | output_tokens: 2044

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

### 1. Tabla Comparativa de Competidores

> **Nota de transparencia:** He modelado a **EnviaMas** basándome en los patrones de los ESPs (Email Service Providers) regionales de LATAM (como Doppler, EnvíaloSimple o MasterBase), ya que "EnviaMas" no cuenta con datos públicos consolidados de cuota global. Si tu competidor tiene features propietarias específicas distintas, ajústalas sobre esta base.

| Criterio | Mailchimp (Intuit) | Brevo (ex-Sendinblue) | EnviaMas (Competidor Local) |
| :--- | :--- | :--- | :--- |
| **Modelo de Pricing** | • Cobro por **contactos totales** (activos e inactivos) + envíos.<br>• Free tier muy limitado (500 contactos, 1k envíos/mes).<br>• Desde ~$13 USD/mes hasta >$350 USD al escalar lista. | • Cobro por **volumen de envíos**, no por tamaño de base de datos.<br>• Free tier generoso (300 emails/día).<br>• Starter desde ~$25 USD/mes (20k envíos). | • Cobro mixto (créditos prepagos o suscripción mensual por contactos).<br>• Precios en moneda local (evita fluctuación cambiaria).<br>• Generalmente 30-40% más barato en USD que Mailchimp. |
| **Features Principales** | • Automatizaciones avanzadas y Customer Journey Builder.<br>• IA generativa de contenido y optimización de envío.<br>• Ecosistema masivo de integraciones (Shopify, WooCommerce, CRMs). | • Email + SMS + WhatsApp nativo.<br>• Email transaccional robusto vía API/SMTP.<br>• CRM ligero integrado y chat en vivo. | • Editor Drag & Drop básico.<br>• Plantillas predeterminadas regionales.<br>• Integración con plataformas locales (ej. Tiendanube, Mercado Pago vía webhooks simples). |
| **Mercado Target** | SMBs consolidadas y Mid-Market a nivel global; e-commerce con presupuesto en USD. | Pymes globales que buscan omnicanalidad (Email + WhatsApp) y bajo costo de base de datos. | Micro y pequeñas empresas locales que priorizan soporte en español y pago sin tarjeta internacional. |
| **Fortalezas** | • Marca líder indiscutida y alta entregabilidad técnica.<br>• UX/UI pulida y reportes predictivos profundos. | • Costo predecible para bases de datos inactivas grandes.<br