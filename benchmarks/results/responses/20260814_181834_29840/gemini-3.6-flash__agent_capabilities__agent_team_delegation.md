# Gemini 3.6 Flash — agent_capabilities/agent_team_delegation

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.15 | quality: 9.16
- latency_total: 9.452s | tokens_per_second: 166.4
- input_tokens: 561 | output_tokens: 1573
- judge_score: 4.4 | justificación: 

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

¡Excelente! Voy a coordinar todo el proceso para el lanzamiento de la landing page de **AutoFlow AI**. 

A continuación detallo el **Plan de Ejecución y Dependencias**:

---

### 📋 Plan de Ejecución

1. **Fase 1: Investigación de Mercado y Competencia**
   - **Agente:** `researcher` (Prioridad: Alta)
   - **Tarea:** Investigar a 3 competidores clave en herramientas de automatización para startups (ej. Zapier, Make, n8n/Bardeen) para identificar sus propuestas de valor, precios y puntos fuertes/débiles.

2. **Fase 2: Redacción de Copywriting (Landing Page)**
   - **Agente:** `writer` (Prioridad: Alta) — *Depende de Fase 1*
   - **Tarea:** Redactar la propuesta de valor, sección Hero, Features clave, tabla/opciones de Pricing y Calls to Action (CTA) orientados a startups.

3. **Fase 3: Diseño Visual y Assets**
   - **Agente:** `designer` (Prioridad: Media) — *Depende de Fase 2*
   - **Tarea:** Definir el estilo visual y generar los conceptos/assets para la imagen principal del Hero y los íconos/gráficos de Features.

4. **Fase 4: Desarrollo Web (HTML/CSS)**
   - **Agente:** `coder` (Prioridad: Alta) — *Depende de Fases 2 y 3*
   - **Tarea:** Crear el código HTML y CSS responsive, optimizado y moderno para la landing page.

5. **Fase 5: Revisión y Control de Calidad**
   - **Agente:** `reviewer` (Prioridad: Alta) — *Depende de Fases 2, 3 y 4*
   - **Tarea:** Auditar la calidad del copy, la usabilidad, el código y la experiencia general antes de su publicación.

---

Comenzamos de inmediato con la **Fase 1**. Delegando la investigación al agente `researcher`...