# Qwen 3.5 397B — business_audit/roadmap_restriccion_capacidad

- model_id: `qwen/qwen3.5-397b-a17b`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 54.199s | tokens_per_second: 61.6
- input_tokens: 255 | output_tokens: 3337

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

Hola. Como Head of Product que ha visto quemarse a muchos fundadores solitarios, voy a ser brutalmente honesto contigo: **tu capacidad real es de 160 horas para este trimestre** (8 semanas × 5 días × 4 horas).

Si intentas hacer lo que "debería" hacerse en una empresa ideal, vas a fallar en todo. Vamos a priorizar basándonos en **supervivencia y flujo de caja**, no en perfección técnica.

Aquí tienes tu plan de batalla.

### 1. El Veredicto de las Iniciativas

*   **🔴 A) Reescribir la plataforma (NO HACER):**
    *   **Decisión:** **Cancelar para este trimestre.**
    *   **Por qué:** Es una trampa mortal. 3 meses a tiempo completo son ~480 horas. Tú tienes 160 horas *totales* disponibles. Si intentas esto, no entregarás valor visible al mercado en 8 semanas. Además, bloquea la iniciativa C. El "deuda técnica" no mata startups, la falta de tracción sí.
*   **🟢 B) Arreglar el flujo de alta (PRIORIDAD 1):**
    *   **Decisión:** **Hacer YA.**
    *   **Por qué:** Estás perdiendo al 60% de tu potencial ingreso. Es el agujero en el cubo. Arreglar esto tiene un ROI inmediato. Es esfuerzo bajo (1 semana) e impacto alto.
*   **🔴 C) Panel de métricas (CANCELAR / POSTERGAR):**
    *   **Decisión:** **Bloqueado.**
    *   **Por qué:** Depende de A (que no vamos a hacer). No empieces A solo para habilitar C. Tus clientes prefieren que el producto funcione bien (B) a tener un panel bonito que no pueden usar porque el onboarding falla.
*   **🟡 D) Videos de contenido (PRIORIDAD 2):**
    *   **Decisión:** **Hacer, pero con alcance reducido.**
    *   **Por qué:** Necesitas alimentar el embudo para que el arreglo del onboarding (B) valga la pena. 2 semanas de esfuerzo es viable, pero debemos dejar colchón para imprevistos.

---

### 2. Tu Plan Trimestral (8 Semanas)

Tu capacidad es de **4 horas diarias de "construcción"**. Todo lo demás es ops/soporte. No llenes esas 4 horas al 100%, deja un 20% de buffer porque el soporte siempre se come tiempo de desarrollo.

**Objetivo del trimestre:** Maximizar conversión (B) y alimentar tráfico (D).

#### **Fase 1: Tapa el agujero (Semanas 1 y 2)**
*   **Foco:** Iniciativa B (Onboarding).
*   **Tiempo asignado:** 40 horas (2 semanas × 5 días × 4 horas).
*   **Meta:** Reducir el drop-off del paso 2 del 60% al menos al 30%.
*   **Regla:** No toques nada más. Si sale un bug crítico en producción, atiéndelo, pero no empieces D todavía.
*   **Por qué:** No sirve de nada grabar videos (D) para traer gente a un producto que no saben usar (B).

#### **Fase 2: Motor de crecimiento (Semanas 3 a 6)**
*   **Foco:** Iniciativa D (Videos).
*   **Tiempo asignado:** 64 horas (4 semanas × 4 horas/día).
*   **Ajuste:** El esfuerzo estimado era 2 semanas full-time (~80 horas). Tienes 64 horas reales.
    *   *Opción A:* Grabar 8 videos en vez de 10.
    *   *Opción B:* Grabar 10 pero con producción más simple (menos edición).
*   **Meta:** Tener contenido publicado para empezar a atraer tráfico hacia el onboarding ya arreglado.

#### **Fase 3: Buffer y Iteración (Semanas 7 y 8)**
*   **Foco:** Medición y Ops.
*   **Tiempo asignado:** 40 horas (Buffer).
*   **Actividad:**
    1.  Medir si el arreglo de B funcionó. Si no, usar estas 2 semanas para iterar sobre B.
    2.  Absorber el exceso de soporte (siempre pasa).
    3.  Planificar el siguiente trimestre.
*   **Nota:** Aquí es donde evalúas si la iniciativa A (Rewrite) sigue siendo necesaria. Spoiler: Probablemente descubras que con B y D funcionando, A sigue siendo menos prioritaria.

---

### 3. Reglas de Oro para ti (Fundador Solo)

1.  **La Iniciativa A es un "No" rotundo:** Como PM, mi trabajo es protegerte de ti mismo. Reescribir por "velocidad futura" es una excusa para no vender hoy. Solo reescribe si la plataforma actual impide cobrar dinero *hoy*. Si solo es "más lento", aguanta.
2.  **La Iniciativa C muere con A:** No busques atajos para hacer C sin A. Es una distracción. Tus clientes quieren resultados, no paneles.
3.  **Protege las 4 horas:** Si el soporte se come 3 horas un día, no recuperes esas horas trabajando hasta la noche. Recorta el alcance de D. El burnout es el único riesgo real de muerte para tu empresa ahora mismo.
4.  **Métrica de éxito del trimestre:** No es "código entregado". Es **% de conversión en onboarding** y **nuevos usuarios activos** gracias a los videos.

**Resumen:**
1.  **Semana 1-2:** Arreglar Onboarding (B).
2.  **Semana 3-6:** Grabar Videos (D) (ajustando alcance a tu tiempo real).
3.  **Semana 7-8:** Buffer, medir resultados y soporte.
4.  **A y C:** Fuera del backlog trimestral.

¿Te comprometes a no tocar la iniciativa A hasta que el ingreso mensual se haya duplicado gracias a B y D?