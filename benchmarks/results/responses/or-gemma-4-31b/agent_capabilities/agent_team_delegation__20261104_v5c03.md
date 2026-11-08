# Gemma 4 31B — agent_capabilities/agent_team_delegation

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 8.86 | quality: 9.52
- latency_total: 5.888s | tokens_per_second: 94.6
- input_tokens: 897 | output_tokens: 557
- judge_score: 4.8 | justificación: 

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres el agente coordinador de un Agent Team. Tienes 5 sub-agentes:
- researcher: busca informacion y datos
- writer: redacta contenido
- coder: genera codigo y automatizaciones
- reviewer: revisa calidad y errores
- designer: crea assets visuales

Reglas:
- Descompone tareas complejas en sub-tareas para cada agente
- Respeta dependencias (el writer necesita los datos del researcher primero)
- Asigna prioridades correctamente
- Explica el plan de ejecucion antes de delegar

**user:**

Necesito crear una landing page para el lanzamiento de nuestro nuevo producto "AutoFlow AI" (herramienta de automatizacion para startups). Incluye:
1. Investigar que hace la competencia (3 competidores)
2. Escribir el copy de la landing (hero, features, pricing, CTA)
3. Generar el codigo HTML/CSS de la pagina
4. Crear las imagenes hero y de features
5. Revisar todo antes de publicar

Coordinalo todo.


## Respuesta completa

Entendido. Como Agente Coordinador, tomaré el mando de este proyecto para el lanzamiento de **AutoFlow AI**. Esta es una tarea multidisciplinaria que requiere un flujo de trabajo secuencial para asegurar que el diseño y el código estén alineados con la estrategia de mercado y el copy.

### 📋 Plan de Ejecución

Para garantizar la calidad, he descompuesto el proyecto en las siguientes fases y dependencias:

**Fase 1: Inteligencia de Mercado (Prioridad: Alta)**
*   **Agente:** `researcher`
*   **Tarea:** Análisis de 3 competidores principales.
*   **Entregable:** Reporte de puntos fuertes, débiles y propuesta de valor comparativa.
*   *Dependencia: El `writer` necesita esto para diferenciar el mensaje.*

**Fase 2: Estrategia de Contenido (Prioridad: Alta)**
*   **Agente:** `writer`
*   **Tarea:** Redacción del copy completo (Hero, Features, Pricing, CTA).
*   **Entregable:** Documento de texto con la estructura de la landing.
*   *Dependencia: El `coder` y el `designer` necesitan el texto final para estructurar la web y crear los assets.*

**Fase 3: Producción Visual y Técnica (Prioridad: Media - Ejecución Paralela)**
*   **Agente:** `designer` $\rightarrow$ Creación de imágenes hero y visuales de funcionalidades.
*   **Agente:** `coder` $\rightarrow$ Desarrollo del código HTML/CSS basado en el copy y los assets.
*   *Dependencia: Ambos trabajan sobre la base del `writer`.*

**Fase 4: Control de Calidad y Cierre (Prioridad: Urgente)**
*   **Agente:** `reviewer`
*   **Tarea:** Auditoría de copy (ortografía y tono), revisión de responsive design en el código y coherencia visual.
*   **Entregable:** Visto bueno final o lista de correcciones.

---

### 🚀 Inicio de Delegación

Voy a comenzar con la primera fase inmediatamente.

<|channel>thought
<channel|>