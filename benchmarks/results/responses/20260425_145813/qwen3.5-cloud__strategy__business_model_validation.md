# Qwen 3.5 (Ollama Cloud default) — strategy/business_model_validation

- model_id: `qwen3.5:cloud`
- success: True  | final: 7.95 | quality: 9.43
- latency_total: 45.113s | tokens_per_second: 45.4
- input_tokens: 179 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

Siéntate. Deja de sonreír. He visto cien pitches de marketplaces B2B este año y 99 están muertos antes de escribir la primera línea de código. Tu idea suena a "solución buscando un problema" con márgenes que no cuadran.

Aquí tienes la realidad fría, sin el filtro de "empoderamiento emprendedor".

### 1. Los 5 Riesgos Principales (Los que te van a matar)

1.  **Disintermediación (Leakage):** Este es el asesino silencioso. En cuanto el restaurante y el proveedor se conozcan en tu plataforma, intercambiarán WhatsApp en la primera entrega. Al mes siguiente, transaccionan por fuera y tú te quedas con la pantalla vacía. ¿Cómo vas a evitar eso técnicamente? No puedes.
2.  **Márgenes Insostenibles:** Un restaurante pequeño opera con un margen neto del 5% al 10%. Los proveedores de materia prima operan con márgenes brutos ajustados. Querer meter un **15% de comisión** en una cadena de valor de commodities es suicida. O el restaurante quiebra pagándote, o el proveedor te ignora.
3.  **El Problema del Huevo y la Gallina:** Para que un restaurante se registre, necesitas catálogo y disponibilidad real. Para que un proveedor se registre, necesita pedidos. Quemarás tu capital en subsidios para atraer a ambos lados antes de tener liquidez. Tu CAC (Costo de Adquisición de Cliente) se comerá tu LTV (Valor de Vida del Cliente).
4.  **Control de Calidad y Logística:** Si la lechuga llega podrida, ¿quién responde? ¿Tú o el proveedor? Si es el proveedor, el restaurante culpa a tu app. Si eres tú, necesitas logística propia y márgenes del 15% no cubren flota de reparto. Te convertirás en una empresa de logística disfrazada de tech.
5.  **Volatilidad de Precios:** Los ingredientes locales cambian de precio semanalmente (o diario) por clima, estación y oferta. ¿Tu app tendrá actualización de precios en tiempo real? Si el proveedor pone un precio y al momento de cobrar es otro, la confianza se rompe. La fricción operativa es altísima.

### 2. ¿Por qué podría NO funcionar en LATAM específicamente?

*   **La Cultura del "Fiado" (Crédito):** En LATAM, los restaurantes no pagan al contado. Sobreviven con crédito a 30, 60 o 90 días con sus proveedores de confianza. Tu modelo asume transacción inmediata. Si no ofreces financiamiento (y asumes el riesgo de impago), eres irrelevante. Si lo ofreces, necesitas capital de trabajo que no tienes.
*   **Informalidad Fiscal:** Muchos proveedores locales no facturan correctamente. Los restaurantes necesitan factura para deducir impuestos. Si tu plataforma obliga a formalizar, el precio sube y el proveedor se va. Si permites informalidad, te arriesgas legalmente.
*   **WhatsApp es tu Competencia:** En LATAM, WhatsApp es el ERP de la pyme. Pedir por WhatsApp es gratis, rápido y permite negociar. ¿Por qué un dueño de restaurante va a pagar un 15% extra por una app cuando su proveedor le atiende por chat sin comisión?
*   **Relaciones Personales:** El chef no compra "tomates", compra "los tomates de Don José". Confía en la persona, no en la plataforma. Digitalizar la confianza es mucho más difícil que digitalizar la transacción.
*   **Infraestructura de Última Milla:** En muchas ciudades de LATAM, las direcciones son un caos y la seguridad es un problema. Coordinar entregas de perecederos sin una flota propia es una pesadilla operativa.