# GLM-5.1 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `z-ai/glm-5.1`
- success: True  | final: 6.94 | quality: 8.0
- latency_total: 57.342s | tokens_per_second: 38.1
- input_tokens: 187 | output_tokens: 2186
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando un experimento bien estructurado y práctico para evaluar la hipótesis.

## Respuesta completa

Bienvenido al lado oscuro (y real) del emprendimiento. Si vas a meterte 2 meses a construir algo sin saber si te van a pagar, no estás fundando una empresa, estás haciendo un hobby caro.

Tu mayor riesgo no es técnico, es de "dolor dispuesto a pagar". Las agencias odian hacer reportes, sí. Pero ¿odian hacerlo *tanto* como para sacrificar $200 al mes de su margen?

Aquí tienes el experimento para destrozar tu hipótesis. Se llama el **"Cobro Fantasma" (Painted Door via Outreach)**. No hay código, no hay landing page bonita, solo ventas directas a una puerta que no existe.

### Qué hacer exactamente

1. **Crea la ilusión (1 hora):** Diseña 1 o 2 pantallas en Figma de cómo se vería el dashboard o el reporte automatizado. Que se vea profesional, pero no perfecto. 
2. **Arma la puerta falsa (30 mins):** Crea un link de pago en Stripe (o tu procesador favorito) para una suscripción de $200/mes. Cuando lleguen a la pasarela, verán que es real. *No vas a cobrar el dinero si lo intentan*, pero el botón de "Pagar" debe estar ahí. (Puedes poner un modo de prueba y anotar los datos, o usar un checkout real y devolver el dinero/reembolsar al instante si alguien paga).
3. **La prospección fría (4 horas):** Busca en LinkedIn, agencias de marketing de 2 a 10 personas. Necesitas contactar a los fundadores o directores (los que aprueban el gasto). Busca 100 agencias. 
4. **El mensaje (El gancho):** Envíales un DM o correo corto y directo. Cero humo, cero "te cambio la vida". Habla en su idioma:
   > *"Hola [Nombre], vi que dirigen [Agencia]. Sé que armar reportes para clientes cada mes quita horas. Estoy lanzando una herramienta que automatiza todo el proceso en 5 minutos y se envía directo al cliente. Sería de $200/mes. Tengo 5 plazas beta con un 50% de descuento el primer mes. ¿Te interesa echarle un vistazo a cómo se ve?"*
5. **La estocada:** Si dicen que sí, les mandas el link a tu Figma + el link de pago de Stripe. Diles: *"Te adjunto cómo se ve. Para reservar tu plaza y configurar tus cuentas, puedes completar el checkout aquí [Link de Stripe]."*

### Cuánto cuesta
**$0.** Figma es gratis, Stripe es gratis (solo cobran si hay transacción), LinkedIn cuesta $0 mandar DMs si lo haces manualmente. Tu único costo son unas horas de tu tiempo.

### Cuánto tarda
**72 horas.** Hoy diseñas, mañana sales a la calle, pasado mañana tienes los resultados. 

---

### El resultado que MATA tu hipótesis (y te hace abandonar)

Como fundador, vas a querer engañarte. Vas a escuchar un *"¡Qué guay! Avísame cuando esté lista"* y vas a querer ponerlo en tu Excel como una "venta potencial". **No lo hagas.** Las palabras son baratas; la tarjeta de crédito no miente.

**Tu hipótesis está MUERTA y debes abandonar la idea si:**
De esas 100 agencias contactadas, menos de 3 intentan pagar en Stripe.

**Escenarios de fracaso disfrazados de éxito (NO construyas si escuchas esto):**
* *"Me encanta la idea, pero ahora mismo no tengo presupuesto."* -> No hay dolor suficiente por $200.
* *"¿Tienen plan gratuito?"* -> Quieren el resultado, pero no lo valoran en $200/mes.
* *"Pásame un demo cuando esté listo."* -> Cortesía de empresario. No es intención de compra real.

**El único resultado que te da luz verde para codear:**
Alguien hace clic en el botón de pago de Stripe, mete sus datos de la tarjeta e intenta pagar los $200. (En ese momento, le devuelves el dinero, le dices la verdad: *"Soy el fundador, estoy validando esto, me acabo de dar cuenta de que hay dolor real. Te doy los primeros 3 meses gratis cuando lance en 8 semanas"*).

Si no hay gente metiendo la tarjeta, no hay producto. Te ahorras 2 meses de tu vida. Ve a buscar otro problema.