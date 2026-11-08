# Mercury 2.5 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `inception/mercury-2.5`
- success: True  | final: 7.92 | quality: 8.0
- latency_total: 5.768s | tokens_per_second: 365.1
- input_tokens: 185 | output_tokens: 2106

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa



Entendido. Quieres un test destructivo, no validación. Aquí está el plan para fallar rápido:

1. **Acción:**
   - Crea una landing page simple (1 hora) con un video Loom de 2 minutos mostrando cómo se vería la herramienta (puede ser un mockup).
   - Pon el precio explícito: **$200/mes**.
   - El botón de "Comprar" o "Empezar" debe pedir tarjeta de crédito o un depósito previo.

2. **Tráfico:**
   - Envía 50 mensajes directos (LinkedIn, Twitter, Email) a dueños de agencias pequeñas.
   - El mensaje: *"Estoy construyendo una herramienta para automatizar reportes. Ya no hay lista de espera. Si te interesa, puedo activarte el acceso hoy a $200/mes. ¿Te interesa?"*

3. **Costo:**
   - ~$50 (dominio + hosting + herramientas).
   - Tu tiempo: 2 días.

4. **Tiempo:**
   - 5 días máximo.

5. **Resultado que te hace abandonar (Kill Switch):**
   - Si **0 de 50** muestran intención real de pagar (agendar llamada seria, responder con objeciones de precio, o pre-pagar), la hipótesis está muerta. No construyas nada.