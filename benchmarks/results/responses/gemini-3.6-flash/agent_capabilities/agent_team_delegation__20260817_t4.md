# Gemini 3.6 Flash — agent_capabilities/agent_team_delegation

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.74 | quality: 10.0
- latency_total: 8.039s | tokens_per_second: 195.9
- input_tokens: 561 | output_tokens: 1575
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando un plan detallado y estructurado para la coordinación del proyecto.

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

¡Excelente! Asumo la coordinación completa del proyecto para el lanzamiento de la landing page de **AutoFlow AI**. 

A continuación detallo el **Plan de Ejecución por Fases**, respetando el flujo de dependencias entre los especialistas del equipo:

---

### 📋 Plan de Ejecución del Equipo

1. **Fase 1: Investigación de Mercado y Competencia** *(Prioridad: Alta)*
   * **Agente:** `researcher`
   * **Tarea:** Analizar a 3 competidores clave (ej. Zapier, Make, Bardeen/Relay) enfocados en automatización para startups. Identificar propuestas de valor, estructuras de landing, pricing y llamadas a la acción (CTA).
   * **Dependencia:** Ninguna (Fase inicial).

2. **Fase 2: Redacción del Copy de la Landing** *(Prioridad: Alta)*
   * **Agente:** `writer`
   * **Tarea:** Redactar la propuesta del copy completo: Hero Section, Features principales, Tabla de Pricing y CTAs persuasivos enfocados en startups.
   * **Dependencia:** Requiere el informe de la Fase 1 (`researcher`).

3. **Fase 3: Desarrollo Visual y Código (En Paralelo)** *(Prioridad: Media-Alta)*
   * **Agente:** `designer`
     * **Tarea:** Generar/diseñar los assets visuales (imagen del Hero y gráficos/iconos ilustrativos de las features).
   * **Agente:** `coder`
     * **Tarea:** Crear el código HTML/CSS responsivo y moderno incorporando la estructura y el copy definidos.
   * **Dependencia:** Requieren el copy finalizado de la Fase 2 (`writer`).

4. **Fase 4: Control de Calidad y Revisión Final** *(Prioridad: Alta)*
   * **Agente:** `reviewer`
   * **Tarea:** Auditoría integral del código, copy, diseño visual, coherencia de marca, accesibilidad y preparación para publicación.
   * **Dependencia:** Requiere entregables de las Fases 3a y 3b (`designer` y `coder`).

---

Damos inicio con la **Fase 1** delegando la investigación al agente `researcher`.