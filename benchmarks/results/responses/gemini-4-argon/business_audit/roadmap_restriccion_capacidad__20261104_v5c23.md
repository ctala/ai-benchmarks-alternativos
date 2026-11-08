# Gemini 4 Argon — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-4-argon`
- success: True  | final: 8.27 | quality: 10.0
- latency_total: 19.467s | tokens_per_second: 49.5
- input_tokens: 270 | output_tokens: 964

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres jefe de producto de una empresa de una sola persona. Priorizas con la capacidad real del equipo, no con la ideal.

**user:**

Soy fundador solo. Tengo 6 horas al día de trabajo enfocado y ya gasto 2 de esas 6 en soporte y operación diaria que no puedo delegar todavía. Me quedan ~4h/día reales para construir. Quedan 8 semanas hasta el cierre del trimestre.

Tengo cuatro iniciativas y quiero saber qué hago:

A) Reescribir la plataforma en otro framework. Impacto estimado: alto (velocidad y todo lo futuro). Esfuerzo: ~3 meses a tiempo completo.
B) Arreglar el flujo de alta, que hoy pierde al 60% de la gente en el paso 2. Impacto: alto. Esfuerzo: ~1 semana.
C) Añadir un panel de métricas para mis clientes. Impacto: medio. Esfuerzo: ~3 semanas. Depende de que A esté terminado.
D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas.

Ordename el trimestre.


## Respuesta completa

Vamos a poner los pies en la tierra y hacer matemáticas de verdad, no de fantasía.

Dices que tienes 8 semanas y 4 horas al día. Asumiendo que tus estimaciones de esfuerzo ("1 semana", "3 meses") están pensadas en jornadas estándar de 8 horas, **tu capacidad real está a la mitad**. Una semana de trabajo de alcance para ti son 2 semanas de calendario. 

En estas 8 semanas tienes exactamente **160 horas para construir**. Si le restamos un 20% por imprevistos, bugs urgentes o días malos, te quedan unas **130 horas reales**. 

Con esa capacidad, aquí tienes tu plan para el trimestre, ordenado sin piedad:

### 1. Lo que vas a hacer (En este orden estricto)

**Paso 1: Iniciativa B (Arreglar el flujo de alta)**
*   **Por qué primero:** Estás tirando a la basura el 60% de tu tráfico. Es una hemorragia crítica. No tiene sentido traer más gente ni mejorar el producto si la puerta de entrada está rota. Es el mayor retorno de inversión (Alto impacto / Bajo esfuerzo).
*   **Tiempo real:** Estimaste 1 semana (~40h). A 4h/día, te tomará **2 semanas de calendario**. 
*   **Estado del trimestre:** Te quedan 6 semanas.

**Paso 2: Iniciativa D (Grabar 10 videos de contenido)**
*   **Por qué segundo:** Ahora que el flujo de alta convierte bien (gracias a B), necesitas meter gente a ese embudo para validar que el arreglo funciona y generar ingresos. 
*   **Tiempo real:** Estimaste 2 semanas (~80h). A tu ritmo, te tomará **4 semanas de calendario**. *(Nota de Product Manager: Graba 5 videos, publícalos, mide si traen tráfico y luego decides si grabas los otros 5).*
*   **Estado del trimestre:** Te quedan 2 semanas.

**Paso 3: Construir una versión "hackeada" de C (Panel de métricas) + Colchón**
*   **Por qué tercero:** Te sobran 2 semanas (40 horas). No te da para hacer C completo (y dijiste que dependía de A), pero tus clientes necesitan ver valor. No reescribas nada; usa las últimas 2 semanas para escupir esos datos como puedas: un reporte automático por email, un CSV descargable o incrustar una gráfica fea en el código viejo. 

---

### 2. Lo que NO vas a tocar este trimestre (El cementerio de ideas)

**Iniciativa A (Reescribir la plataforma): CANCELADA.**
*   **La realidad:** Estimaste 3 meses a tiempo completo (unas 480 horas). Con tus 4 horas al día, esto te tomará **6 meses**. Si empiezas esto hoy, terminarás el trimestre con cero mejoras para tus usuarios, el flujo de alta seguirá perdiendo al 60% de la gente, no habrás hecho marketing y tendrás un código a medio escribir que no sirve para nada. El síndrome de "reescribir todo" es el asesino número uno de fundadores solos. Tu código actual funciona; exprímelo hasta que duela.

**Iniciativa C (Tal como la pensaste): BLOQUEADA.**
*   **La realidad:** Al depender de A, queda automáticamente fuera. Además, a tu ritmo te tomaría 6 semanas completas. Por eso haremos la versión "hackeada" en el Paso 3 sobre la plataforma vieja.

---

### Resumen de tu Trimestre (Calendario Real)

*   **Semanas 1 y 2:** Arreglar el onboarding (B). 
*   **Semanas 3, 4, 5 y 6:** Crear contenido y traer tráfico al nuevo onboarding (D).
*   **Semanas 7 y 8:** Colchón para imprevistos (que los tendrás) y ver cómo entregar las métricas a los clientes (C) sin tocar el framework actual.

**Un consejo extra de gestión:** Esas 2 horas diarias de soporte te están comiendo el 33% de tu energía. Cuando termines el trimestre, tu prioridad para el siguiente no será reescribir el código (A), será automatizar procesos para bajar ese soporte a 30 minutos al día. Ahí es donde realmente ganarás velocidad.