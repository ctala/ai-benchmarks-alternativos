# Gemini 3.8 Flash — agent_capabilities/agent_team_delegation

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 15.763s | tokens_per_second: 81.6
- input_tokens: 571 | output_tokens: 1287
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente estructurada, proporcionando un plan detallado que un emprendedor podría usar directamente.

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

### Plan de Ejecución: Landing Page "AutoFlow AI"

Para asegurar la máxima calidad y coherencia en el lanzamiento, organizamos el flujo de trabajo respetando las dependencias lógicas entre sub-agentes:

---

### Fases y Dependencias del Proyecto:

1. **Fase 1: Investigación de Mercado (Agente: `researcher`)**  
   * **Tarea:** Analizar 3 competidores principales en el espacio de automatización para startups (propuestas de valor, diferenciadores clave, estructuras de pricing y llamados a la acción).  
   * **Prioridad:** Alta.  
   * **Dependencia:** Ninguna (punto de partida).

2. **Fase 2: Redacción del Copywriting (Agente: `writer`)**  
   * **Tarea:** Redactar el contenido de la landing page (Sección Hero, Características/Features, Tabla de Precios/Pricing y CTAs persuasivos).  
   * **Prioridad:** Alta.  
   * **Dependencia:** Requiere los hallazgos de la Fase 1 (`researcher`).

3. **Fase 3: Diseño de Assets Visuales (Agente: `designer`)**  
   * **Tarea:** Diseñar las imágenes/mockups para la sección Hero e ilustraciones conceptuales de las features clave.  
   * **Prioridad:** Media.  
   * **Dependencia:** Requiere la estructura de features definida por el `writer`.

4. **Fase 4: Desarrollo Web Frontend (Agente: `coder`)**  
   * **Tarea:** Construir la landing page en HTML5 semántico y CSS moderno, responsivo y optimizado, integrando el copy y los assets visuales.  
   * **Prioridad:** Alta.  
   * **Dependencia:** Requiere el copy final (`writer`) y las especificaciones visuales (`designer`).

5. **Fase 5: Control de Calidad y Auditoría Final (Agente: `reviewer`)**  
   * **Tarea:** Revisión integral de ortografía/tono, calidad del código HTML/CSS, adaptabilidad móvil y UX general antes de dar luz verde a producción.  
   * **Prioridad:** Urgente.  
   * **Dependencia:** Requiere el entregable completo del `coder`.

---

Iniciamos con la **Fase 1**, delegando la investigación al sub-agente `researcher`.