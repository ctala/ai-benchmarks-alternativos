# Llama 4 Scout 17B (Groq preview) — agent_capabilities/agent_team_delegation

- model_id: `meta-llama/llama-4-scout-17b-16e-instruct`
- success: True  | final: 7.61 | quality: 9.16
- latency_total: 2.449s | tokens_per_second: 376.4
- input_tokens: 1375 | output_tokens: 922
- judge_score: 4.4 | justificación: 

## Respuesta completa

Para coordinar la creación de la landing page para el lanzamiento de "AutoFlow AI", descompondré la tarea en sub-tareas específicas para cada agente especializado y explicaré el plan de ejecución.

### 1. Investigar la Competencia

- **Agente:** researcher
- **Tarea:** Investigar 3 competidores directos de "AutoFlow AI" en el mercado de herramientas de automatización para startups.
- **Prioridad:** Alta
- **Contexto:** Información sobre los competidores, incluyendo características, precios y propuestas de valor.

### 2. Escribir el Copy de la Landing

- **Agente:** writer
- **Tarea:** Redactar el contenido (copy) para la landing page basado en la investigación de los competidores y los objetivos de "AutoFlow AI".
  - **Secciones:**
    - Hero
    - Features
    - Pricing
    - CTA (Llamada a la acción)
- **Prioridad:** Alta
- **Dependencia:** La tarea del researcher debe completarse primero para informar el contenido.

### 3. Generar el Código HTML/CSS de la Página

- **Agente:** coder
- **Tarea:** Crear el código HTML/CSS para la landing page según el diseño y contenido aprobados.
- **Prioridad:** Alta
- **Dependencia:** El contenido del writer y los assets visuales del designer deben estar disponibles.

### 4. Crear las Imágenes Hero y de Features

- **Agente:** designer
- **Tarea:** Diseñar las imágenes necesarias para la landing page, incluyendo:
  - Imagen hero
  - Imágenes para destacar las features
- **Prioridad:** Media
- **Dependencia:** Ninguna específica, pero debe coordinar con el progreso general.

### 5. Revisar Todo antes de Publicar

- **Agente:** reviewer
- **Tarea:** Revisar la calidad del contenido, diseño y código de la landing page para asegurar que todo esté correcto y funcional.
- **Prioridad:** Alta
- **Dependencia:** Todas las tareas anteriores deben estar completadas.

### Plan de Ejecución

1. **Investigación de la Competencia (researcher):** Día 1
2. **Redacción del Contenido (writer):** Día 2-3 (depende de la entrega del researcher)
3. **Creación de Assets Visuales (designer):** Día 2-3
4. **Generación de Código (coder):** Día 4 (depende de la entrega del writer y designer)
5. **Revisión (reviewer):** Día 5
6. **Publicación:** Día 5 o 6, después de las revisiones finales.

### Delegación de Tareas

```
