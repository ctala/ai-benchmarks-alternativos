# Gemini 3.7 Flash — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 7.36 | quality: 8.0
- latency_total: 17.506s | tokens_per_second: 116.8
- input_tokens: 154 | output_tokens: 2044

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un fundador experimentado. Sabes que el objetivo de un experimento no es tener razón: es descubrir rápido y barato que estás equivocado. Diseñas tests que pueden FALLAR de forma concluyente.

**user:**

Mi hipótesis: las agencias de marketing pequeñas pagarían $200/mes por una herramienta que les automatice los reportes a clientes.

Estoy a punto de meterme 2 meses a construirla. Antes de eso, diséñame el experimento **más barato y más rápido** que pueda MATAR esta hipótesis.

No quiero validarla. Quiero saber, en el menor tiempo y plata posible, si estoy equivocado. Dime exactamente qué hago, cuánto me cuesta, cuánto tarda, y cuál sería el resultado que me hace abandonar la idea.


## Respuesta completa

Ni una sola línea de código. $200/mes para una agencia pequeña es **caro** (Looker Studio es gratis, AgencyAnalytics empieza en $12/cliente). Si no están sangrando por este problema, jamás pagarán eso.

Aquí tienes el experimento para matar la idea en **5 días** y con **$0**.

---

### El Experimento: "El Concierge Pre-Sale"

No vas a vender software. Vas a vender el **resultado** manualmente haciéndote pasar por una beta cerrada.

#### Paso a Paso (Lunes a Viernes)

1. **Lunes (Prospección - 4 horas):**
   * Ve a LinkedIn o Clutch.co. Busca 50 dueños/directores de agencias de marketing pequeñas (de 2 a 10 empleados).
   * Extrae sus perfiles/emails.

2. **Martes (El Gancho - 4 horas):**
   * Escríbeles un mensaje directo, ultra corto, sin rodeos corporativos:
     > *"Hola [Nombre]. Vi que manejas [Agencia]. Armé una herramienta para automatizar al 100% los reportes mensuales de clientes (Google Ads, Meta, Analytics) en un PDF/Link que los clientes sí entienden. Busco 3 agencias para la beta privada de este mes: nosotros configuramos todo y te ahorramos ~20 horas al mes. Cuesta $200/mes. Si te interesa verlo en 10 min mañana, dime."*

3. **Miércoles y Jueves (Llamadas de Cierre - 15 min c/u):**
   * A los que respondan, hazles una demo con **un PDF ficticio o un Figma de 3 pantallas** (tardas 1 hora en Canva/Figma).
   * Al minuto 10 dices: *"La beta arranca este lunes. El costo es de $200/mes con garantía de devolución si no te ahorra mínimo 15 horas. Para incluirte en el lote de este mes, necesito procesar el primer mes hoy por Stripe (les mandas link de pago de Stripe preconfigurado)."*

4. **Viernes (Análisis y Ejecución o Muerte):**
   * Si pagan: Haces los reportes **a mano** el primer mes usando Make/Zapier/Looker para entender el dolor real antes de programar nada.
   * Si no pagan: Lees las métricas de abajo y matas el proyecto.

---

### Métricas del Experimento

* **Costo:** **$0 USD** (o $15 si pagas LinkedIn Sales Navigator de prueba).
* **Tiempo:** **5 días laborables** (máximo 20 horas de trabajo invertidas).
* **Muestra:** **50 agencias contactadas.**

---

### El Criterio de Muerte (Cuándo ABANDONAR la idea)

Abandona **inmediatamente** y no toques tu editor de código si se cumple **CUALQUIERA** de estas tres condiciones el viernes por la tarde:

1. **Falta de tracción:** De los 50 contactados, **menos de 4 personas** aceptan tener la llamada (Nadie tiene el problema lo suficientemente caliente).
2. **Resistencia letal al precio:** Los que aceptan la llamada te dicen cosas como: *"Uso Looker Studio gratis"*, *"Es muy caro para mi tamaño"*, o *"Avísame cuando esté 100