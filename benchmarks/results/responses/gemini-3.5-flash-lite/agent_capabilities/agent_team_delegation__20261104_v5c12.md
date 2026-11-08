# Gemini 3.5 Flash Lite — agent_capabilities/agent_team_delegation

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 8.99 | quality: 9.72
- latency_total: 2.637s | tokens_per_second: 180.9
- input_tokens: 571 | output_tokens: 477
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

¡Entendido! Para llevar a cabo este proyecto de manera estructurada y eficiente, coordinaré a nuestro equipo de especialistas (*researcher, writer, coder, designer* y *reviewer*) siguiendo un plan de ejecución por fases y dependencias.

---

### 📋 Plan de Ejecución

1. **Fase de Investigación (Researcher):** 
   * Analizaremos a 3 competidores clave en el mercado de herramientas de automatización para startups para identificar sus propuestas de valor, puntos débiles y oportunidades de diferenciación para **AutoFlow AI**.
2. **Fase de Contenido (Writer):** 
   * Con los datos de la investigación, el escritor redactará todo el copy persuasivo de la landing page (Hero section, Features/Características, Pricing y Llamados a la Acción - CTAs).
3. **Fase de Diseño Visual (Designer):** 
   * Se definirán y generarán los conceptos/assets visuales necesarios para la imagen principal (*hero image*) y las secciones de características.
4. **Fase de Desarrollo (Coder):** 
   * Con el copy aprobado y los lineamientos visuales listos, el programador generará el código limpio en HTML5 y CSS3 (con un diseño responsive y moderno).
5. **Fase de Control de Calidad (Reviewer):** 
   * Finalmente, el revisor hará una auditoría completa del resultado final (coherencia de marca, ortografía, calidad del código y usabilidad) antes de dar el visto bueno para la publicación.

---

### 🚀 Iniciando Fase 1: Investigación

Voy a delegar la primera tarea a nuestro agente **researcher** para que investigue a 3 competidores en el sector de automatización para startups.

