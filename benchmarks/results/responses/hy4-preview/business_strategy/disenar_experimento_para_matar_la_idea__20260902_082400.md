# Tencent Hy4 preview — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `tencent/hy4-preview`
- success: True  | final: 6.95 | quality: 8.0
- latency_total: 99.65s | tokens_per_second: 58.8
- input_tokens: 213 | output_tokens: 5864

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Me alegra que pienses así. El cementerio de las startups está lleno de fundadores que se enamoraron de su solución, pasaron meses programando en la oscuridad, y al salir al mercado descubrieron que nadie quería pagar por ella.

Para matar esta idea rápido y barato, tenemos que atacar el supuesto más riesgoso: **¿Realmente van a sacar la billetera y pagar $200/mes por esto?**

Un error fatal sería enviar una encuesta preguntando "¿Te gustaría pagar por esto?". La gente miente para ser amable o para no desilusionarte. La única métrica real para validar o matar una idea de negocio es el *swipe* de la tarjeta de crédito.

El experimento se llama **Preventa de Humo (Pre-Sell)**. Vas a vender un producto que no existe para ver si el mercado muerde el anzuelo.

Aquí tienes el plan exacto para intentar destruir tu hipótesis:

### 1. Exactamente qué hacer
*   **Día 1: Crea el "Activo".** Haz una página web de una sola pantalla (usa Carrd, Notion o Typedream).
    *   **Titular:** "Deja de perder tiempo armando reportes manuales para tus clientes".
    *   **Descripción:** Conecta Google Ads, Meta y GA4. Genera reportes PDF automáticos y con la marca de tu agencia en minutos.
    *   **Botón de compra:** "Pre-ordenar: $200/mes (Precio de Fundador)". Este botón debe llevar a una pasarela de pago real (Stripe o PayPal).
*   **Día 2: Consigue la "Municipión".** Extrae una lista de **100 agencias de marketing pequeñas** (de 2 a 15 empleados). Usa LinkedIn Sales Navigator, Apollo.io (tiene plan gratuito) o Clutch.co. Consigue el contacto directo del dueño, fundador o director.
*   **Día 3: Dispara.** Envíales un correo frío o un mensaje directo por LinkedIn. Ve directo al grano, sin rodeos:
    > "Hola [Nombre], veo que diriges una agencia de marketing. Estoy lanzando un software que automatiza el 100% de los reportes a clientes (jala datos de Meta/Google y arma el PDF solo). Lanzo en 8 semanas. Estoy buscando 5 agencias fundadoras para pre-ordenar a $200/mes (precio bloqueado para siempre). Si entras hoy, personalmente te configuro las plantillas. Mira cómo funciona aquí: [Link a tu landing page]"

### 2. Cuánto te cuesta
*   Dominio + Herramienta de Landing Page: **~$30 USD** (máximo).
*   Extracción de leads (Apollo Free o búsqueda manual en LinkedIn): **$0 USD**.
*   **Costo total: $30 USD.** (Cero código, cero diseñadores, cero anuncios pagados).

### 3. Cuánto tarda
*   Construir la página y conseguir los 100 contactos: 2 días.
*   Enviar los mensajes personalizados: 1 día.
*   Esperar a ver si alguien paga: 4 días.
*   **Tiempo total: 1 semana.** (En el peor de los casos, perdiste 1 semana y te ahorraste 2 meses de programación inútil).

### 4. El Resultado que MATA la Hipótesis (Kill Criteria)
Abandonas la idea (o pivotas drásticamente el precio/mercado) si al final de la semana obtienes **MENOS DE 3 VENTAS PAGADAS** de esas 100 agencias contactadas.

*   **¿Por qué 3?** 1 o 2 ventas pueden ser falsos positivos (un amigo, un conocido, o alguien que ni siquiera leyó bien y compró por error). **3 desconocidos pagando $200 por un software que literalmente no existe** es la prueba irrefutable de que el dolor es real, el precio es correcto y el canal de ventas funciona.
*   Si tienes 0, 1 o 2 ventas: **MATA LA IDEA HOY.** El problema no es lo suficientemente grave como para que paguen $200 al mes por ello, el precio está mal, o te estás dirigiendo al cliente equivocado.

**El único "efecto secundario" de este experimento:**
Si fallas en matar la idea y logras 3 o más ventas, tendrás que entregar el producto. No entres en pánico: durante esos 2 meses, haz los reportes **manualmente** (tú mismo entra a las cuentas de tus clientes, saca los datos y arma el PDF en Canva o Looker Studio). Esto se llama un *Concierge MVP* (MVP Conserje) y te enseñará más sobre lo que tus clientes realmente quieren ver en ese reporte que cualquier línea de código que pudieras escribir a ciegas.

No escribas una sola línea de código hasta que escuches la caja registradora. Ve a intentar matar tu idea.