# Gemini 3.7 Flash — agent_capabilities/agent_team_delegation

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.77 | quality: 9.72
- latency_total: 8.905s | tokens_per_second: 104.2
- input_tokens: 561 | output_tokens: 928
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

### Plan de Ejecución del Equipo de Agentes

Para el lanzamiento de la landing page de **"AutoFlow AI"**, he estructurado el flujo de trabajo en 4 fases respetando las dependencias técnicas y de contenido:

1. **Fase 1: Investigación (Bloqueante inicial)**
   - **Agente:** `researcher`
   - **Tarea:** Analizar a 3 competidores clave en automatización para startups (propuestas de valor, estructura de landing pages, pricing y CTAs).
   - **Prioridad:** Alta.

2. **Fase 2: Copywriting y Diseño Visual (En paralelo tras Fase 1)**
   - **Agente:** `writer` → Redactar el copy completo (Hero, Features, Pricing, CTA) basado en los insights de la competencia.
   - **Agente:** `designer` → Generar los assets visuales (imagen hero conceptual, iconos y mockups de features).
   - **Prioridad:** Alta.

3. **Fase 3: Desarrollo Web (Tras Fase 2)**
   - **Agente:** `coder` → Implementar la estructura HTML5 semántica, estilos CSS responsivos y modernos, integrando el copy y las imágenes generadas.
   - **Prioridad:** Media.

4. **Fase 4: Control de Calidad y Revisión Final (Fase de cierre)**
   - **Agente:** `reviewer` → Auditar accesibilidad, responsive design, consistencia del copy, enlaces/CTAs y performance general.
   - **Prioridad:** Alta.

---

Iniciamos con la **Fase 1** delegando la investigación al agente `researcher`.