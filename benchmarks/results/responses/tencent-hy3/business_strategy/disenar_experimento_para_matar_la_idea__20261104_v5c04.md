# Tencent Hy3 — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `tencent/hy3`
- success: True  | final: 7.23 | quality: 8.0
- latency_total: 116.281s | tokens_per_second: 56.7
- input_tokens: 221 | output_tokens: 6592

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Excelente instinto. La mayoría de los fundadores escribe código para sentirse productivos, no para resolver un problema real. Vamos a diseñar un experimento para matar tu bebé en 72 horas con $0 de inversión.

**El Experimento: El "Fake Door" de Pre-venta Directa (Smoke Test)**
No vas a construir el software. Vas a vender el software que no existe y ver si alguien saca la tarjeta de crédito por un dolor que ni siquiera has aliviado.

### 1. Qué haces (Exacto, paso a paso)
*   **Paso A (15 mins):** Entra a Stripe (o Mercado Pago) y crea un *Payment Link* para cobrar $200 (puede ser el primer mes). No necesitas web, solo el link de pago.
*   **Paso B (1 hora):** Consigue una lista de 50 dueños de agencias de marketing pequeñas (de 2 a 15 empleados) en LinkedIn, directorios locales o grupos de Facebook.
*   **Paso C (1 hora):** Mándales un mensaje directo (Email o LinkedIn DM) personalizado pero escalable. Usa este guion:
    > *"Hola [Nombre], vi que diriges [Agencia]. Muchas agencias pequeñas pierden horas semanales haciendo reportes manuales a clientes. Estoy lanzando una herramienta que los automatiza y manda PDFs con tu marca por $200/mes. Solo abro 10 plazas fundadoras. Paga el primer mes aquí para entrar: [Link Stripe]"*
*   **Paso D (Si hay respuestas negativas):** Si alguien te responde "no", pregúntales: *"¿Es por el precio o porque no sienten ese dolor?"*. Anota las respuestas.

### 2. Cuánto cuesta
*   **Stripe:** $0 (solo cobra comisión si alguien paga; si paga, le devuelves el dinero al instante diciendo que fue un error del sistema para no tener que cumplir el servicio manualmente).
*   **Outreach:** $0 (usando Gmail/LinkedIn).
*   **Costo total:** **$0.** (Quizás $10 si compras un dominio nuevo para que tus correos no vayan a spam, pero no es estrictamente necesario).

### 3. Cuánto tarda
*   Preparación y envío: 1 tarde (2-3 horas).
*   Espera de respuestas: 48 a 72 horas.
*   **Tiempo total:** **3 días.**

### 4. El Resultado que te hace ABANDONAR la idea (Kill Criteria)
La hipótesis está **MUERTA** y quema los puentes si se cumple **cualquiera** de estas dos condiciones en esos 3 días:
*   **A) El vacío monetario:** De los 50 dueños contactados, **0 personas** hacen clic en el link de Stripe y **0 personas** meten los datos de su tarjeta para pagar los $200. (Si 1 o 2 pagan, tienes un indicio; si 0 pagan de 50, nadie quiere eso a ese precio).
*   **B) La fricción cualitativa:** Si al menos 10-15 de los 50 te responden un "no" y las razones principales son: *"Ya uso Google Data Studio/Excel y es gratis"*, *"Mis clientes no piden reportes"*, o *"No tengo $200/mes para eso"*. Si el mercado no siente el dolor o no tiene el dinero, tu hipótesis de $200/mes está falsada.

Si después de 50 mensajes directos y un link de pago no consigues ni un solo "cha-ching" en tu Stripe, te acabas de ahorrar 2 meses de tu vida y miles de dólares en costo de oportunidad. A disparar el cohete.