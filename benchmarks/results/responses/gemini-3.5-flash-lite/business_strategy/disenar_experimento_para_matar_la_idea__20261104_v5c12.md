# Gemini 3.5 Flash Lite — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 7.49 | quality: 8.0
- latency_total: 5.463s | tokens_per_second: 206.7
- input_tokens: 154 | output_tokens: 1129

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Para matar esta hipótesis en **menos de 48 horas y gastando menos de $20**, vamos a usar una técnica de validación B2B clásica: **La Venta Fantasma (The Fake Door) combinada con Outbound frío.**

No vas a escribir una sola línea de código. No vas a diseñar el logo. Vamos a averiguar si $200/mes es un dolor real o una ilusión tuya.

Aquí tienes el plan de ataque exacto.

---

### El Experimento: El "Email de Acceso Anticipado"

Vas a actuar como si la herramienta ya existiera (o estuviera en su última fase de desarrollo). Tu objetivo es conseguir que un dueño de agencia saque su tarjeta de crédito o te agende una llamada de compromiso.

#### Paso 1: Arma la "Falsa Puerta" (2 horas - Costo: $0)
*   Crea una página de aterrizaje ultra simple (Usa Carrd.co, Framer o Notion).
*   **Título:** "Automatiza los reportes de tus clientes en piloto automático".
*   **Subtítulo:** "Conecta tus fuentes de datos y genera reportes de marketing profesionales en 2 minutos. Diseñado para agencias."
*   **El Gancho:** Pon un botón que diga: *"Obtener acceso anticipado (Cupos limitados para el piloto de $200/mes)"*.
*   **La Trampa (El checkout):** Al hacer clic, el botón abre un formulario de Typeform o Tally que dice: *"El acceso al piloto cierra este viernes. Déjanos tus datos y te activamos la cuenta"*. Al final, los mandas a una pasarela de Stripe con un cobro real de $200 (puedes ponerlo en modo de prueba o cobro real, pero el punto es ver si intentan pagar).

#### Paso 2: Sal a la calle digital a buscar agencias (3 horas - Costo: $0)
*   Ve a LinkedIn o Google Maps. Busca dueños de agencias de marketing pequeñas (de 2 a 10 empleados) en tu país o hispanoamérica.
*   Extrae 50 emails de fundadores o directores de operaciones.

#### Paso 3: Lanza el misil (1 hora - Costo: $0)
Envía un correo ultra corto, conversacional y directo. Nada de marketing corporativo.

> **Asunto:** ¿Sigues perdiendo los viernes haciendo reportes, [Nombre]?
>
> Hola [Nombre],
>
> Sé que los viernes en las agencias pequeñas se van enteros armando reportes manuales en PDF/Looker Studio para los clientes.
>
> Estoy terminando de construir una herramienta que automatiza esto 100% y se ve tan pro que tus clientes pensarán que gastaste miles de dólares. 
>
> Estamos abriendo un grupo de fundador ultra reducido este mes por **$200/mes** (precio congelado para siempre). 
>
> Si te interesa ver un demo de 5 minutos de cómo funciona y entrar al early access, míralo aquí y aparta tu lugar: [Link a tu Landing Page]
>
> Un saludo,
> [Tu Nombre]

---

### Cuánto cuesta
*   **Plata:** $0 (puedes usar la versión gratuita de Carrd y Tally). Si quieres gastar $15 en un dominio .com para que se vea profesional, adelante. Total: **$0 - $15**.
*   **Tiempo:** **6 horas repartidas en 2 días**.

---

### La sentencia de muerte (Cuándo matas la idea)

El objetivo de esto es **matar** tu proyecto antes de que pierdas 2 meses de tu vida. Abandona la idea inmediatamente si ocurre **cualquiera** de estas situaciones en los próximos 3 días:

1.  **Silencio radioactivo:** Envías 50 correos y **nadie** hace clic en el link. *(Diagnóstico: El dolor del reporte no es lo suficientemente agudo como para abrir el correo).*
2.  **El fantasma del "Avísame cuando esté listo":** Consigues 10 o 15 llamadas, hablas con ellos, les encanta la idea, asienten con la cabeza, dicen *"¡Uf, qué falta hace eso!"*, **pero ninguno está dispuesto a pagar por adelantado** o comprometer una tarjeta para el piloto. *(Diagnóstico: Es una "vitamina", no un "analgésico". Les molesta, pero no lo suficiente como para sacar la billetera).*
3.  **El rechazo al precio:** Te dicen abiertamente: *"Está buenísimo, pero por $200 prefiero seguir pagándole a mi becario/hacerlo yo mismo"*. *(Diagnóstico: Tu hipótesis de precio está totalmente rota para el segmento).*

### ¿Qué pasa si por milagro alguien paga o mete su tarjeta?
Felicidades. Acabas de validar que vale la pena arriesgarse a construir un MVP de 2 semanas (no de 2 meses) para entregarles lo que prometiste. Pero ve primero a buscar el "No". Es mucho más barato.