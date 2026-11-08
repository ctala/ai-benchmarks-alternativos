# Tencent Hy4 preview — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `tencent/hy4-preview`
- success: True  | final: 6.98 | quality: 8.0
- latency_total: 90.58s | tokens_per_second: 54.7
- input_tokens: 213 | output_tokens: 4958

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Me alegra que preguntes antes de picar código. Meterte 2 meses a programar es el error clásico del primerizo: enamorarse de la *solución* antes de validar si el *dolor* es real y si hay *disposición a pagar* (WTP).

Para matar esta hipótesis en días y con $0, no vamos a construir una landing page ni invertir en anuncios. Vamos a hacer una **Preventa Manual (Concierge MVP o Wizard of Oz)**. 

Básicamente: **vendes la herramienta, pero la entregas a mano.** Tú eres el software.

Aquí tienes el experimento diseñado específicamente para fallar rápido:

### Exactamente qué vas a hacer (Paso a Paso)

**1. Consigue 20 prospectos (Día 1):**
Busca en LinkedIn, Apollo.io o Google Maps a 20 dueños o fundadores de agencias de marketing pequeñas (de 2 a 15 empleados). Nada de corporativos, agencias pequeñas que hagan reporting manual.

**2. El Pitch - Pide dinero, no opiniones (Día 2):**
Mándales un DM o un Email frío. Sé directo y saca tu lado vendedor.
> *El guion:* "Hola [Nombre], estoy lanzando un software que automatiza los reportes a clientes (conecta Meta/Google Ads y manda reportes automáticos). Estoy seleccionando 3 agencias fundadoras. El precio de lista será de $300/mes, pero lo voy a bloquear en $200/mes de por vida para los primeros. Para agendar tu setup y reservar el cupo, necesito el primer mes por adelantado. ¿Te paso el link de pago?"

*Si te piden un demo o preguntan cómo funciona:* "Justo por ser agencia fundadora, el primer reporte lo configuramos a mano juntos para calibrar tus KPIs exactos, y a partir de ahí el motor lo automatiza".

**3. La Entrega - Tú eres la máquina (Día 5):**
Si te pagan los $200, **no escribas una línea de código**. Pídeles acceso a sus métricas (o que te pasen capturas de pantalla/CSV). Tú, manualmente, ármales un reporte hermoso en Looker Studio, Canva o Google Slides y envíaselo. 

**4. La Autopsia (Días 3 al 5):**
A los que te digan que no, diles: *"Entendido, ¿me ayudas a entender qué te detiene para no quitarte más tiempo?"*. Toma nota de cada excusa. Ahí estará tu respuesta real.

---

### Cuánto te cuesta
**$0.** 
Usas LinkedIn o las búsquedas gratuitas de Apollo para prospectar, Stripe o PayPal para cobrar, y herramientas gratuitas (Looker Studio/Canva) para hacer el reporte a mano. Solo cuesta tu tiempo y tu ego.

### Cuánto tarda
**3 a 5 días.**
*   Día 1: Armar la lista de 20 agencias y escribir el mensaje.
*   Día 2: Enviar los 20 mensajes.
*   Días 3 y 4: Hacer seguimiento y cerrar a los interesados.
*   Día 5: Hacer el reporte manual para los valientes que te pagaron.

---

### El Resultado que MATA la hipótesis (Kill Criteria)
Aquí es donde separamos a los founders de los soñadores. Tienes que ser brutalmente honesto contigo mismo al definir el fracaso.

**Si de esas 20 agencias contactadas, MENOS DE 2 pagan los $200 por adelantado, tu hipótesis está MUERTA.**

Presta mucha atención a esto: "Me encanta la idea", "Avísame cuando esté listo", "Déjame lo platico con mi socio" o "Mándame más info" **SON UN NO**. 
Si no sacan la tarjeta de crédito hoy, significa que el dolor de hacer reportes no es lo suficientemente agudo como para pagar $200 al mes, o no confían en una herramienta nueva para algo tan crítico. 

### Por qué este experimento es a prueba de balas:
*   **Si nadie paga:** Te acabas de ahorrar 2 meses de código. Descubriste que el precio está mal, el dolor no es real, o tu mensaje de ventas apesta. Idea descartada, a por la siguiente.
*   **Si 2 o más agencias pagan:** Acabas de generar tracción en 5 días, validaste el mercado, el precio y el dolor... y encima tienes el dinero (y el tiempo) para empezar a construir la herramienta real con clientes pagándote desde el día 1.

No busques validación. Busca el rechazo. Si te rechazan rápido, ganaste. Ve y ejecuta esto hoy mismo.