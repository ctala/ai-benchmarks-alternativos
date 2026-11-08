# Gemma 4 31B — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.19 | quality: 10.0
- latency_total: 8.609s | tokens_per_second: 92.9
- input_tokens: 260 | output_tokens: 800

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

Como tu Jefe de Producto, mi trabajo es proteger tu tiempo y asegurar que el negocio sobreviva y crezca. 

Primero, el **baño de realidad**: No tienes 8 semanas. Tienes 4 horas al día. Eso significa que tienes el **50% de la capacidad de un empleado a tiempo completo**. Cualquier estimación de "tiempo completo" debe multiplicarse por 2.

Aquí tienes el análisis y el plan de ejecución:

### 1. El análisis de descarte (The Kill List)

*   **Iniciativa A (Reescritura): ELIMINADA.** 
    Es una trampa mortal para un fundador solo. Estimaste 3 meses a tiempo completo, pero con tu capacidad real, tardarías **6 meses**. Durante ese tiempo, no añadirías ni una sola funcionalidad que traiga dinero. El "impacto futuro" no paga las facturas de hoy. **Se queda en el backlog hasta que tengas un equipo de ingeniería.**
*   **Iniciativa C (Panel de métricas): ELIMINADA.**
    Depende de A. Si A no se hace, C no existe. Además, es impacto medio frente a la hemorragia de usuarios que tienes en el alta.

---

### 2. El Orden de Prioridades (El Roadmap Realista)

Tu prioridad es detener la fuga de dinero y usuarios, y luego alimentar la máquina de adquisición.

#### Prioridad 1: Iniciativa B (Flujo de alta)
*   **Por qué:** Estás perdiendo al 60% de tus prospectos en el paso 2. Es un "cubo perforado". No tiene sentido traer más gente (Marketing) si se van al entrar. Es la victoria más rápida y con mayor ROI.
*   **Esfuerzo real:** 1 semana (tiempo completo) $\rightarrow$ **2 semanas (tu tiempo real).**
*   **Fecha de entrega:** Semana 2.

#### Prioridad 2: Iniciativa D (Videos de contenido)
*   **Por qué:** Una vez que el flujo de alta funcione, necesitas tráfico. El contenido es el combustible. Es un esfuerzo finito que genera activos que trabajan para ti mientras duermes o haces soporte.
*   **Esfuerzo real:** 2 semanas (tiempo completo) $\rightarrow$ **4 semanas (tu tiempo real).**
*   **Fecha de entrega:** Semana 6.

---

### 3. Calendario de Ejecución (8 Semanas)

| Semanas | Foco Principal | Objetivo | Capacidad |
| :--- | :--- | :--- | :--- |
| **1 - 2** | **Iniciativa B** | Arreglar el paso 2 del alta. | 4h/día construcción |
| **3 - 6** | **Iniciativa D** | Grabar y publicar los 10 videos. | 4h/día construcción |
| **7 - 8** | **Buffer / Soporte** | Resolver bugs surgidos de B y optimizar operación. | 4h/día construcción |

### Resumen Final del PO:

1.  **Olvida el framework.** El código "sucio" que funciona es mejor que el código "elegante" que no tiene usuarios.
2.  **Tapa el agujero (B).**
3.  **Trae gente nueva (D).**
4.  **Usa las últimas 2 semanas como colchón.** Como fundador solo, siempre surge un incendio o una tarea de soporte que te roba tiempo. No llenes el calendario al 100% o te quemarás.

**Tu mantra para este trimestre: "Menos arquitectura, más conversión".**