# Gemini 3.5 Flash Lite — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 7.72 | quality: 8.0
- latency_total: 4.009s | tokens_per_second: 190.3
- input_tokens: 242 | output_tokens: 763

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

Hola. Como jefe de producto de esta empresa (tú y yo), te voy a hablar claro y sin piedad corporativa. 

Hagamos números reales antes de tocar nada:
* Tienes 4 horas/día de desarrollo. 
* En una semana de 5 días, son 20 horas.
* En 8 semanas de trimestre, tienes **160 horas reales** de desarrollo. Punto. No hay más.

Evaluemos tus iniciativas con esa realidad en la mano:

* **A) Reescribir la plataforma:** Requiere ~3 meses a tiempo completo (unas 480-500 horas). Como solo tienes 160 horas, **es físicamente imposible**. Además, tu regla dice que C depende de A, así que te cargas dos de un plumazo. **Descartada rotundamente para este trimestre.**
* **C) Panel de métricas:** Depende de A. Como A no se hace, C tampoco se hace. **Descartada.**
* **B) Arreglar el flujo de alta:** Pierdes el 60% (¡una barbaridad!). Esfuerzo: ~1 semana (20 horas). **Es oro puro.** Es la definición de "bajo esfuerzo, alto impacto".
* **D) Grabar 10 videos:** Esfuerzo: ~2 semanas (40 horas). Impacto medio para captación/retención. 

---

### Tu plan para las próximas 8 semanas

Te quedan 160 horas. Vamos a gastar solo 60 y dejar un colchón gigante de 100 horas para imprevistos, soporte que se alargue, o salud mental (que siendo solo, lo vas a agradecer).

#### **Semanas 1 y 2 (40 horas): El embudo de conversión (Iniciativa B)**
* **Objetivo:** Arreglar el Paso 2 del alta.
* **Por qué:** Estás tirando a la basura al 60% de la campa de adquisición actual. De nada sirve traer más tráfico (videos) ni retener mejor (métricas) si la puerta de entrada tiene un boquete. Arreglar esto es lo único que va a mover la aguja de ingresos este trimestre.

#### **Semanas 3 y 4 (40 horas): Contenido (Iniciativa D)**
* **Objetivo:** Grabar los 10 vídeos.
* **Por qué:** Ahora que el alta ya no es una vía de agua, tiene sentido empezar a atraer miradas con un poco más de fuelle. 

#### **Semanas 5 a 8 (80 horas restantes): El Colchón de Supervivencia + Iteración**
* **¿Qué hacemos con estas 4 semanas libres?** NADA de inventar nuevas iniciativas. 
* Las vas a usar para:
  1. Absorber los días en que el soporte diario te coma más de 2 horas.
  2. Vigilar de cerca el nuevo flujo de alta (medir si el 60% de caída baja al 20%, por ejemplo).
  3. Corregir bugs urgentes que salgan de los usuarios nuevos.

### Resumen del trimestre:
Haces **B y D**. Metes un gol operativo brutal arreglando el alta, creas algo de contenido, y sobrevives al trimestre sin quemarte intentando hacer una migración suicida (A) que te mataría la empresa por inacción.

¿Nos ponemos con el Paso 2 del alta este lunes?