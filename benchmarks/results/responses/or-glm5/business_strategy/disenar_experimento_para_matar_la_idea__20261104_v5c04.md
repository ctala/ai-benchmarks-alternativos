# GLM 5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `z-ai/glm-5`
- success: True  | final: 7.01 | quality: 8.0
- latency_total: 62.785s | tokens_per_second: 40.9
- input_tokens: 194 | output_tokens: 2566

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Frena. No escribas ni una línea de código. Si te metes dos meses a construir esto, estás apostando $200/mes de ingresos futuros contra dos meses de tu vida que no vas a recuperar. 

Tu objetivo ahora mismo es encontrar al idiota que dice "no" para poder irte a hacer otra cosa.

Aquí tienes el experimento exacto. Se llama **"El Concierge de Pago Adelantado"**.

### El Experimento: Vender el humo (con maqueta)

Vas a vender el producto como si ya estuviera hecho, pero por detrás lo vas a hacer a mano. Si nadie te paga por adelantado, la hipótesis está muerta.

#### Paso 1: La maqueta (2 horas)
No construyas software. Ve a Canva o Figma. Diseña cómo se vería un reporte automatizado para una agencia. Que se vea bonito, profesional, con métricas (SEO, Ads, Social) y un logo de la agencia en la cabecera. Crea también una landing page de una sola pantalla (con Carrd o Notion, gratis) que diga: *"Reportes automatizados para tu agencia en 1 clic. $200/mes. Cancela cuando quieras."* Pon un botón de "Comenzar" que lleve a un checkout de Stripe.

#### Paso 2: La lista de prospectos (3 horas)
Busca 50 agencias de marketing pequeñas (de 2 a 10 empleados). 
- Búscalas en LinkedIn, directorios o Google Maps.
- El perfil exacto: Hacen trabajo decente, pero seguro pierden horas cada fin de mes pegando screenshots en un PDF para mandárselo a sus clientes.
- Encuentra el correo del fundador o del director de operaciones.

#### Paso 3: El ataque (2 días)
Mándales un correo corto y directo. No les pidas feedback. No les ofrezcas una demo gratuita. Ofréceles el producto.

**Asunto:** Reportes de clientes en 1 clic (te ahorramos el fin de semana)
**Cuerpo:** 
*"Hola [Nombre], veo que gestionan campañas para [Cliente de la agencia]. Sé que a fin de mes pierden como 10 horas armando reportes en PDF para clientes. Acabamos de lanzar una herramienta que automatiza todo ese proceso, conecta con tus plataformas y envía el reporte branded directamente a tu cliente. Cuesta $200/mes. Si quieres ser uno de nuestros 10 primeros clientes con acceso inmediato, puedes suscribirte aquí: [Link de Stripe]. ¿Te lo muestro en una llamada de 10 minutos?"*

#### Paso 4: El truco (si alguien paga)
Si alguien mete su tarjeta en Stripe y paga los $200, **no construyas el software todavía**. Escríbele ese mismo día:
*"¡Gracias por tu confianza! Como somos de los primeros usuarios, quiero asegurarme de que el reporte quede perfecto. Dame acceso a tus cuentas de Google Analytics/Ads y yo mismo te configuraré y te enviaré el primer reporte esta semana."*

Lo haces a mano (o con plantillas de Looker Studio/Excel). Tardas 2 horas. Le das el reporte. Si está feliz, mantienes su suscripción y ya tienes tu primer cliente pagando $200/mes. Si te pide devolución del dinero, se la das y aprendes por qué no le convenció.

---

### Métricas del Experimento
- **Costo:** $0 a $20 (dominio + Carrd + Stripe, que no cobra si no hay venta).
- **Tiempo:** 5 días máximo (2 días de preparación, 3 días de envío y espera de respuesta).

### ¿Cuál es el resultado que MATA la hipótesis? (El "Criterio de Asesinato")

Abandonas la idea si se cumple **CUALQUIERA** de estas condiciones:

1. **El silencio absoluto:** Envías 50 correos y no obtienes ni una sola respuesta. *(Significa: El problema no duele lo suficiente como para que abran un correo).*
2. **El sí gratis:** Te responden 10 agencias diciendo "¡Me encanta! Pásame una prueba gratuita de 14 días para ver cómo funciona". Pero nadie mete la tarjeta. *(Significa: Hay interés curioso, pero cero voluntad de pago. Tu producto sería un pasatiempo, no una herramienta de negocio).*
3. **La regateada:** Te responden algunos dispuestos a pagar, pero te dicen "¿Tienes un plan de $20/mes?" o "¿Me haces un descuento?". *(Significa: $200 está fuera de rango para el valor que perciben. Tu modelo de precios no encaja con tu público).*
4. **El reembolso masivo:** Logras que 2 o 3 paguen los $200 por adelantado, pero cuando ven el resultado (o se dan cuenta de que tienes que hacerlo a mano), te piden el reembolso antes de que pase el primer mes. *(Significa: El problema existe, pero tu solución no es la adecuada).*

Si después de 50 correos a los clientes perfectos no logras que **al menos 3** metan su tarjeta de crédito por $200 antes de ver el software funcionar, la hipótesis está muerta. 

Ve a matarla. Nos vemos en 5 días. ¿Qué vas a hacer si resulta que estabas equivocado?