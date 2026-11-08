# Gemini 4 Argon — agent_capabilities/agent_team_delegation

- model_id: `google/gemini-4-argon`
- success: True  | final: 8.25 | quality: 9.72
- latency_total: 13.75s | tokens_per_second: 50.9
- input_tokens: 954 | output_tokens: 700
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

Para llevar a cabo la creación de la landing page de **AutoFlow AI**, he estructurado el siguiente **Plan de Ejecución por Fases**, respetando las dependencias entre cada sub-agente y asignando las prioridades correspondientes:

### 📋 Plan de Ejecución

1. **Fase 1: Investigación y Diseño Base (En paralelo)**
   * **Researcher (Prioridad: Alta):** Investigará a 3 competidores directos en el sector de automatización con IA para startups (analizando su propuesta de valor, estructura de precios, puntos fuertes/débiles y llamados a la acción). *Esta tarea es bloqueante para la redacción del copy.*
   * **Designer (Prioridad: Media):** Creará los assets visuales (imagen principal para la sección Hero e ilustraciones/iconos para la sección de Features) alineados con la identidad tecnológica de "AutoFlow AI".

2. **Fase 2: Redacción de Contenidos (Secuencial - Depende de Fase 1)**
   * **Writer (Prioridad: Alta):** Una vez obtenidos los hallazgos del *researcher*, redactará el copy persuasivo de la landing page (Hero, Features diferenciadoras, tabla de Pricing competitiva y CTAs).

3. **Fase 3: Desarrollo e Integración (Secuencial - Depende de Fases 1 y 2)**
   * **Coder (Prioridad: Media):** Tomará el copy final del *writer* y los assets visuales del *designer* para maquetar y generar el código HTML/CSS responsivo de la landing page.

4. **Fase 4: Control de Calidad / QA (Secuencial - Depende de Fase 3)**
   * **Reviewer (Prioridad: Alta):** Realizará una auditoría completa del producto final (ortografía y persuasión del copy, consistencia visual y validación del código HTML/CSS) antes de dar luz verde para publicar.

---

### 🚀 Iniciando Fase 1

Comenzaré delegando las tareas que no tienen dependencias previas (**Investigación de competencia** y **Diseño de assets visuales**):