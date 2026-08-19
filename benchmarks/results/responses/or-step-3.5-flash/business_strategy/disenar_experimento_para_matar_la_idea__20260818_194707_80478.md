# Step 3.5 Flash — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 7.56 | quality: 8.0
- latency_total: 25.041s | tokens_per_second: 81.8
- input_tokens: 205 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Vamos a diseñar un experimento que pueda matar la hipótesis de manera rápida y barata. La hipótesis es: "las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes."

El objetivo es encontrar evidencia de que esto es falso, no validarlo. Queremos un test que pueda fallar de manera concluyente, es decir, que si el test falla, podamos decir "la hipótesis está muerta".

**Concepto clave:** Para matar la hipótesis, necesitamos encontrar que las agencias pequeñas NO están dispuestas a pagar $200/mes por esta herramienta, incluso si se la ofrecemos en condiciones ideales. Pero no queremos construirla primero. Entonces, debemos simular la oferta sin construir el producto.

**Enfoque:** El experimento más barato y rápido es un "test de humo" o "smoke test". Consiste en crear una página de aterrizaje (landing page) que presente la solución como si ya existiera, con un call-to-action que permita a los interesados reservarla o preordenarla (o al menos dejar su email para ser notificados). Pero en lugar de eso, podemos ir un paso más allá: intentar venderla realmente, pero sin tener el producto. Si logramos que alguien pague, entonces la hipótesis tiene potencial. Si no, y especialmente si encontramos resistencia, la hipótesis podría estar muerta.

Sin embargo, para matarla de manera concluyente, necesitamos una señal fuerte. Pagar $200/mes es un compromiso. Podríamos ofrecer un descuento por ser early adopter, pero queremos probar el precio de $200. Entonces, el experimento debe medir la intención de pago a ese precio.

**Diseño del experimento:**

1. **Crear una landing page simple** que describa el producto: "Herramienta de automatización de reportes para agencias de marketing". Incluir benefits, precio ($200/mes), y un botón de "Comprar ahora" o "Reservar" que lleve a un formulario de pago (pero no cobraremos realmente). O mejor: un botón que diga "Quiero probarlo" y luego en el formulario preguntar si están dispuestos a pagar $200/mes. Pero para medir intención real, debemos simular el proceso de compra.

   Idea: Usar un botón que diga "Comprar por $200/mes" y al hacer clic, mostrar un formulario que pida datos de tarjeta de crédito, pero con un mensaje claro: "Este es un test. No se cobrará nada. Solo queremos saber si pagarías $200/mes por esto". Luego, al completar el formulario, agradecer y decir que el producto estará listo en X meses. Esto nos dará una medida de intención de pago real (necesitan estar dispuestos a dar los datos de tarjeta).

   Pero eso puede ser demasiado para un test rápido. Alternativa: ofrecer un "pre-order" con descuento, pero a $200/mes no es un precio de pre-order típico. Mejor: "Reserva tu lugar por $1" (para comprometerse) y luego si el producto se lanza, pagarán $200/mes. Pero eso no prueba el precio de $200.

   Necesitamos probar el precio de $200/mes. Entonces, el test debe preguntar directamente: "¿Pagarías $200/mes por una herramienta que automatice tus reportes a clientes?" Pero eso es solo una encuesta, y la gente dice que sí pero luego no paga.

   Para matar la hipótesis, debemos encontrar que incluso cuando se les da la oportunidad de comprar (con un proceso de pago simulado), no lo hacen. O que el costo de adquisición sería demasiado alto.

2. **Cómo conseguir tráfico:** Necesitamos llegar a agencias de marketing pequeñas. Podemos:

   - Usar redes sociales (LinkedIn, Facebook) para segmentar dueños de agencias pequeñas.
   - Foros y grupos de marketing.
   - Contacto directo por email (buscar agencias pequeñas y enviar un email personalizado).
   - Publicar en sitios como Reddit (r/marketing, r/agency, etc.).
   - Usar Google Ads con palabras clave relacionadas (pero eso cuesta dinero).

   Queremos el experimento más barato, así que evitamos pagar por tráfico si es posible. Podemos hacer outreach manual: encontrar 100 agencias pequeñas (por ejemplo, en Google Maps, directorios) y enviarles un email o llamarlas.

   Pero eso es lento. Mejor: crear un post en un grupo de Facebook de agencias de marketing, o en LinkedIn. O usar Twitter.

   Sin embargo, para que sea rápido, podemos pagar un poco de publicidad para obtener respuestas rápidas. Pero queremos barato.

   **Propuesta:** Hacer outreach manual a 50 agencias pequeñas. Enviar un email personalizado (usando un template) que diga:

   "Hola [nombre], soy [tu nombre]. Estoy evaluando si construir una herramienta para automatizar reportes a clientes para agencias como la tuya. Si existiera, ¿pagarías $200/mes por ella? Responde a este email con 'Sí' o 'No'."

   Eso es muy simple, pero no es un test de pago real. La gente podría decir que sí por amabilidad. Para matar la hipótesis, necesitamos una señal más fuerte: que estén dispuestos a dar dinero.

   **Mejor:** Ofrecer un acceso temprano con un precio especial de $200/mes (precio normal sería $300, por ejemplo). Y pedir un depósito reembolsable de $50 para reservar el lugar. Eso prueba que están dispuestos a pagar algo. Si nadie paga $50 para reservar, entonces probablemente no pagarán $200/mes.

   Pero el depósito de $50 no es lo mismo que $200/mes. Podría ser que sí paguen $200 una vez que el producto exista, pero no quieren reservar sin verlo.

   **Alternativa:** Construir una landing page con Stripe (o similar) para aceptar pagos, pero en realidad no cobrar. Poner un botón de "Comprar ahora por $200/mes" que lleve a un checkout donde piden tarjeta. Al intentar pagar, mostrar un mensaje: "Este es un test de demanda. No se realizará ningún cargo. Si hubieras completado la compra, habrías obtenido acceso prioritario cuando lancemos." Y luego agradecer. Eso mediría cuánta gente está dispuesta a pasar por el proceso de dar los datos de tarjeta para un producto que no existe.

   Este es un "fake door test" o "smoke test" con intención de pago.

3. **Costos:**

   - Landing page: Usar Carrd, Webflow, o incluso un Google Sites gratis. No necesitamos nada fancy. Unos $0-$20.
   - Dominio: $10-15/año, pero podemos usar un subdominio gratis.
   - Stripe (o similar) para el checkout simulado: Stripe tiene fees, pero si no cobramos, no hay fees. Solo configurar el checkout. Gratis.
   - Tiempo de diseño: 2-4 horas para una página simple.
   - Tiempo de outreach: Para conseguir tráfico, podemos:
        Opción A: Pagar $50 en Facebook/Instagram Ads dirigidos a dueños de agencias pequeñas (posiblemente en LinkedIn también, pero más caro). Eso nos dará clicks.
        Opción B: Hacer outreach manual en LinkedIn (mandar mensajes a 100 dueños de agencias). Gratis pero tiempo: 2-3 horas.
        Opción C: Publicar en grupos relevantes (gratis, pero puede no llegar a suficiente gente).

   Para ser rápido, pagar un poco de publicidad es mejor. Pero queremos barato. Supongamos que gastamos $50 en ads y logramos 500 visitas. Con una tasa de conversión a "intención de pago" (completar el checkout) del 1%, tendríamos 5 personas. Pero si la hipótesis es falsa, la tasa será cercana a 0.

   Si hacemos outreach manual, podemos contactar 100 agencias y quizás 10 respondan. Pero el proceso de pago requiere que vayan a la página.

   **Decisión:** Crear la landing page y luego enviar el enlace a 100 agencias pequeñas por email/LinkedIn. Y también publicar en 2-3 grupos de Facebook/LinkedIn relevantes. Sin pagar ads. Costo: $0 (excepto tiempo).

   Tiempo total: 
   - Diseño landing page: 4 horas.
   - B