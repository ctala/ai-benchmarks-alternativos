# Qwen 3.7 Max — business_strategy/disenar_experimento_para_matar_la_idea

- model_id: `qwen/qwen3.7-max`
- success: True  | final: 6.7 | quality: 8.0
- latency_total: 64.558s | tokens_per_second: 49.3
- input_tokens: 179 | output_tokens: 3185
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan detallado y práctico para probar la hipótesis de manera efectiva.

## Respuesta completa

Bienvenido al club. Me encanta tu actitud. El 90% de los fundadores primerizos se enamoran de su solución y gastan 6 meses programando para luego descubrir que a nadie le importa. Tú quieres que te rompan la hipótesis en la cara antes de abrir tu IDE. Eso es pensar como un verdadero fundador.

Para un SaaS B2B de **$200/mes** (un ticket alto para una agencia pequeña), la gente no saca la tarjeta de crédito por un anuncio en Facebook ni por un botón en una Landing Page. Hay una barrera de confianza enorme: **les estás pidiendo que te den acceso a los datos de sus clientes** (APIs de Meta, Google Analytics, etc.). 

Tu mayor riesgo no es si puedes construirlo. Tu mayor riesgo es **la fricción de integración y la percepción de valor**.

Aquí tienes el experimento para matar tu hipótesis en **10 días y con menos de $50 dólares**.

---

### El Experimento: "La Preventa de Humo y la Guillotina de la API"

No vas a vender "software". Vas a vender el **resultado**: reportes perfectos entregados en la bandeja de entrada de sus clientes todos los lunes a las 8 AM, sin que ellos muevan un dedo.

#### Paso 1: Reclutamiento (Días 1-2)
*   **Acción:** Busca 30 dueños/fundadores de agencias de marketing pequeñas (de 3 a 15 empleados) en LinkedIn o usando Apollo.io.
*   **El Mensaje (Frío y al pie):** *"Hola [Nombre], veo que lideras [Agencia]. Sé que armar reportes de fin de mes para los clientes es un cuello de botella que te roba horas de margen. Estoy cerrando un grupo beta de 5 agencias para automatizar esto al 100%. ¿Tienes 10 minutos el jueves para mostrarte cómo funciona?"*

#### Paso 2: La Demo Falsa (Días 3-5)
*   **Acción:** No tires ni una línea de código. Abre **Figma** y diseña 3 pantallas: 
    1. El dashboard de conexión de APIs.
    2. La plantilla del reporte automático (que se vea increíble, mejor que lo que ellos hacen en Data Studio o Canva).
    3. La pantalla de "Configurar envío automático al cliente".
*   **Preparación:** Graba un video de Loom de 3 minutos haciendo "clic" en tu Figma como si fuera real, o haz la demo en vivo por Zoom.

#### Paso 3: La Guillotina (Días 6-10)
En las llamadas con los dueños de las agencias, después de mostrarles la magia, haces **La Pregunta de los $200**:
> *"Esto cuesta $200 al mes. El grupo beta empieza el próximo lunes y solo me quedan 2 lugares. Si me dejas tu tarjeta hoy, el lunes a primera hora conectamos tus primeras 3 cuentas y tu cliente recibe el reporte sin que tú hagas nada. ¿Lo hacemos?"*

---

### 📊 Los Números del Experimento

*   **Tiempo total:** 7 a 10 días.
*   **Costo:** $0 (si lo haces manual) o ~$49 (un mes de Apollo/LinkedIn Sales Nav para extraer los contactos).
*   **Muestra:** 30 outreach -> ~10 llamadas de demostración.

---

### 💀 Cuándo MATAR la idea (Tus criterios de fracaso)

Debes abandonar la idea y no escribir una sola línea de código si ocurre **CUALQUIERA** de estos 3 escenarios:

#### 1. El Síndrome de la Vitamina ("Avísame cuando esté lista")
Si de las 10 llamadas, **menos de 2 personas** te dan su tarjeta de crédito en esa misma llamada (o firman un LOI / acuerdo de preventa vinculante), **MATA LA IDEA**.
*   *Por qué:* Si te dicen "se ve genial, me avisas cuando esté construida para probarla", significa que tu herramienta es una *vitamina*, no un *analgésico*. Las agencias solo pagan por cosas que les están haciendo sangrar dinero *hoy*. Si no te pagan por adelantado, no te pagarán cuando esté lista.

#### 2. El Muro de la Confianza (La trampa de la API)
Si te dicen: *"Me encanta, pero no puedo darte acceso a las cuentas publicitarias de mis clientes porque es un riesgo de seguridad / mis clientes no me dejan compartir credenciales con terceros"*.
*   *Por qué:* Acabas de descubrir una barrera de entrada insuperable para una agencia pequeña. Si el software requiere que el dueño de la agencia le pida a su cliente que autorice a una startup desconocida (tú) para leer sus datos, el ciclo de venta se alargará meses. **MATA LA IDEA.**

#### 3. La Objeción del Margen
Si te dicen: *"Es muy caro, yo le pago a un freelancer en Latam/Asia $150 al mes para que me arme los reportes en Canva/Sheets"*.
*   *Por qué:* Tu hipótesis de precio de $200/mes se rompe contra la realidad de la externalización barata. Si tu software no puede reemplazar a una persona que cobra menos que tu software, no tienes negocio. **MATA LA IDEA.**

---

### ¿Qué pasa si sobrevives al experimento?

Si logras que **3 agencias te den su tarjeta de crédito por adelantado** (o te pagan el primer mes por Stripe antes de que el software exista), entonces, y solo entonces, tienes permiso para empezar a programar. 

En ese caso, tu primer MVP no será un SaaS multi-tenant complejo. Será un script de Python corriendo en tu servidor que extrae los datos, los escupe en un PDF bonito y lo manda por email. **Eso es todo.** 

Ahora ve, habla con 10 dueños de agencias y deja que el mercado te diga si estás equivocado. Cuéntame cómo te fue en la llamada #3.