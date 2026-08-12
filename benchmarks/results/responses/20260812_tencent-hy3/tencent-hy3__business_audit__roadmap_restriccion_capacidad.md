# Tencent Hy3 — business_audit/roadmap_restriccion_capacidad

- model_id: `tencent/hy3`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 63.621s | tokens_per_second: 71.6
- input_tokens: 302 | output_tokens: 4556

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

Hola. Como tu Jefe de Producto (y sabiendo que el equipo de ingeniería, ventas y soporte eres tú mismo), mi trabajo es ser brutalmente honesto con la capacidad real y no dejarte caer en la trampa del founder solitario: querer reescribir todo mientras el negocio se queda sin clientes.

Aquí está el cálculo de la realidad y el orden del trimestre.

### 1. La matemática de tu capacidad real
No tienes 8 semanas de trabajo completo. Tienes:
*   8 semanas x 5 días x 4 horas reales = **160 horas de construcción** este trimestre (si trabajas 6 días, serán 192h; el resultado no cambia).

Evaluemos las iniciativas contra esas horas:
*   **A (Reescribir):** 3 meses a tiempo completo = ~480 horas. Te llevaría **24 semanas**. 🛑 *No cabe. Es físicamente imposible.*
*   **C (Dashboard):** Depende de A. Si A no se hace, C no se hace. 🛑 *No cabe.*
*   **B (Arreglar alta):** ~1 semana full-time (40h) = **2 semanas reales** para ti.
*   **D (Videos):** ~2 semanas full-time (80h) = **4 semanas reales** para ti.

**Total a ejecutar (B + D): 6 semanas reales.** Te regala 2 semanas de colchón para cuando el soporte de 2h diarias se desborde (que lo hará).

---

### 2. El Roadmap del Trimestre (Ordenado)

**Semanas 1 a 2: Iniciativa B (Arreglar el flujo de alta)**
*   **Por qué primero:** Tienes una hemorragia. Perder al 60% en el paso 2 es matar tu tasa de conversión todos los días. Es alto impacto y bajo esfuerzo relativo. Como PM, esto es un P0 (Prioridad Cero). No construyes nada más hasta tapar este agujero.

**Semanas 3 a 6: Iniciativa D (Grabar 10 videos de contenido)**
*   **Por qué segundo:** Impacto medio, pero necesario para alimentar el embudo (top-of-funnel). En 4 semanas reales a 4h/día es perfectamente factible. Sin clientes nuevos entrando, arreglar el paso 2 (B) no sirve de nada.

**Semanas 7 a 8: Colchón de Seguridad (Buffer)**
*   **Qué hacer:** Mantenimiento, resolver bugs imprevistos del soporte, o descansar. Al ser un equipo de 1, el riesgo de agotamiento (burnout) es altísimo; este margen de 2 semanas es sagrado y no negociable.

---

### 3. Por qué descartamos A y C (La charla de PM)
*   **Sobre A (La trampa de la reescritura):** Cambiar de framework es el clásico procrastinar disfrazado de mejora técnica. El impacto de A es "velocidad futura", pero hoy tu problema no es la velocidad del código, es que la gente no se registra (B) y no sabes atraer tráfico (D). No demoles la casa para ponerle cimientos nuevos mientras se te escapan los inquilinos por la puerta rota.
*   **Sobre C:** Queda oficialmente pospuesto al próximo trimestre. Como PM, te sugiero cuestionar la dependencia: ¿de verdad el panel de métricas *no* se puede hacer con el framework actual y hay que esperar a A? Si es estrictamente así, se hace después de A en Q2.

**Resumen para el fundador:** Este trimestre construyes B y D. Dejas de perder clientes y generas tracción. A y C esperan a que tengas más capacidad o decidas contratar/deslegar soporte.