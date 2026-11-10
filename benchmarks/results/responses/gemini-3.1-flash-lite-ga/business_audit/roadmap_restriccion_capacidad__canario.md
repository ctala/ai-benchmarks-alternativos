# Gemini 3.1 Flash Lite (GA) — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.1-flash-lite`
- success: True  | final: 7.82 | quality: 8.0
- latency_total: 4.767s | tokens_per_second: 158.6
- input_tokens: 242 | output_tokens: 756

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

Como jefe de producto de tu empresa, mi trabajo es proteger tu tiempo y asegurar que el trimestre no termine en frustración.

Tienes **160 horas de construcción real** este trimestre (4h/día × 5 días × 8 semanas).

Aquí está el veredicto: **La iniciativa A es una trampa mortal.** Si la empiezas, te comes todo el trimestre, no entregas nada de valor al usuario y sacrificas las otras tres iniciativas. Como empresa de una sola persona, tu ventaja competitiva es la velocidad de iteración, no tener el stack tecnológico perfecto.

### Tu Roadmap para los próximos 2 meses:

| Prioridad | Iniciativa | Duración | Por qué |
| :--- | :--- | :--- | :--- |
| **1** | **B (Flujo de alta)** | 1 semana | Es tu "Quick Win" más rentable. Recuperar ese 60% es ingreso directo sin adquirir nuevos usuarios. |
| **2** | **D (Contenido)** | 2 semanas | Necesitas alimentar el embudo de ventas. 10 videos son activos que trabajan por ti mientras duermes. |
| **3** | **C (Métricas)** | 3 semanas | Aporta valor percibido (retención). *Nota: Como A no se hará, ajusta el alcance de C para que funcione sobre tu stack actual.* |
| **Buffer** | **Imprevistos** | 2 semanas | En una empresa de una persona, el "soporte" suele escalar cuando lanzas cosas nuevas. Este tiempo es tu seguro de vida. |

---

### Análisis estratégico de por qué descartamos A:

1.  **La falacia del constructor:** Reescribir (A) es la forma más rápida de quebrar un negocio en solitario. Estarías 3 meses sin lanzar nada nuevo. Si tu plataforma actual funciona (aunque sea "lenta"), el mercado no te va a pagar más por un framework nuevo; te pagarán por resolver sus problemas.
2.  **Dependencias:** La iniciativa C depende de A. Al matar A, desbloqueas C para que se haga sobre lo que ya tienes. Si tu stack actual no permite hacer C, simplifica el requerimiento de C hasta que sea posible.
3.  **El riesgo del "Burnout":** Tienes 4 horas reales. Si te metes en una reescritura, el soporte te va a comer vivo porque no tendrás tiempo de mejorar la estabilidad del sistema actual mientras construyes el nuevo.

### Plan de acción para el lunes:

1.  **Semana 1:** Implementa el arreglo del flujo de alta (B). Mide obsesivamente. Si el 60% de pérdida baja al 30%, habrás ganado más dinero en una semana que lo que cualquier reescritura te daría en meses.
2.  **Semanas 2-3:** Graba los 10 videos (D). Distribúyelos.
3.  **Semanas 4-6:** Desarrolla el panel de métricas (C) sobre el stack actual.
4.  **Semanas 7-8:** **Buffer de seguridad.** Si todo salió bien, usa este tiempo para optimizar procesos de soporte (para bajar esas 2h diarias) o para empezar a preparar el siguiente trimestre.

**Regla de oro:** Si algo no está roto (o no está perdiendo dinero), no lo reescribas. Tu prioridad es el crecimiento, no la elegancia del código.