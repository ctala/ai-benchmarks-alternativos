# Gemini 3.6 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 10.157s | tokens_per_second: 201.2
- input_tokens: 242 | output_tokens: 2044

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

Como tu Jefe de Producto, mi trabajo es proteger tu tiempo y asegurar que cada hora invertida mueva la aguja del negocio. 

Primero, bajemos esto a **números reales**:
*   **Tu capacidad real:** 4 horas/día × 5 días/semana = **20 horas a la semana**.
*   **Tu ventana de tiempo:** 8 semanas restantes = **160 horas en total para el trimestre**.

Con 160 horas de capacidad total, así es como ordenamos tu trimestre.

---

### La Matriz de la Realidad (Qué se hace y qué se descarta)

*   **INICIATIVA A (Reescribir plataforma): DESCARTADA.** 
    *   *Por qué:* 3 meses a tiempo completo (40h/sem) son 480 horas. Tu trimestre entero tiene 160 horas. Si empiezas esto, terminarás el trimestre con un producto a medias, roto, sin métricas y perdiendo el 60% de los usuarios. La reescritura es la trampa mortal del solo-founder.
*   **INICIATIVA C (Panel de métricas): REFORMULADA.** 
    *   *Por qué:* Si depende de A, está bloqueada. Pero como eliminamos A, tienes que construir una versión "sucia" pero funcional (MVP) de este panel sobre tu código actual.

---

### El Plan de Ejecución (Semana a Semana)

#### **Semana 1: Fuego Primario — Iniciativa B (Arreglar el flujo de alta)**
*   **Esfuerzo:** 1 semana (20h).
*   **Por qué va primero:** Estás tirando a la basura al 60% de la gente en el paso 2. No tiene sentido hacer marketing (videos) ni retención (métricas) si la puerta de entrada está rota.
*   **Objetivo:** Reducir esa fuga al menos a la mitad. Con la misma gente que entra hoy, duplicas tus conversiones en 7 días.

#### **Semanas 2 y 3: Atraer Trafico — Iniciativa D (10 Videos de contenido)**
*   **Esfuerzo:** 2 semanas (40h).
*   **Por qué va segundo:** Ahora que la puerta de entrada (flujo de alta) ya no pierde al 60% de la gente, tiene sentido meter más usuarios por el embudo.
*   **Consejo de PM:** No los edites en exceso. Graba, corta lo obvio y publica. 4 horas al día son suficientes si batcheas la producción.

#### **Semanas 4, 5 y 6: Retención — Iniciativa C (Panel de métricas MVP)**
*   **Esfuerzo:** 3 semanas (60h).
*   **Por qué va tercero:** Ya mejoraste la conversión y metiste tráfico con los videos. Ahora das valor a los usuarios existentes para que no se vayan.
