# Solar Pro 4 — agent_capabilities/agent_team_delegation

- model_id: `upstage/solar-pro4`
- success: True  | final: 8.57 | quality: 9.52
- latency_total: 18.306s | tokens_per_second: 46.5
- input_tokens: 1108 | output_tokens: 851
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

¡Perfecto! Vamos a crear una landing page completa para **AutoFlow AI**. Esta es una tarea compleja que requiere coordinación entre todos los sub-agentes. Voy a desglosar el plan de ejecución:

## 📋 Plan de Ejecución

### Fase 1: Investigación (Researcher)
- Buscar 3 competidores de herramientas de automatización para startups
- Analizar sus features, positioning y pricing
- Identificar gaps de mercado que AutoFlow AI pueda aprovechar

### Fase 2: Copywriting (Writer)
- Elaborar hero section con value proposition fuerte
- Redactar sección de features destacando diferenciadores
- Crear pricing tables y CTA persuasivos
- *Dependencia: necesita datos del researcher*

### Fase 3: Assets Visuales (Designer)
- Crear imagen hero que comunique automatización + IA
- Diseñar iconos/ilustraciones para las features
- *Puede empezar en paralelo con el copy*

### Fase 4: Desarrollo (Coder)
- Generar HTML/CSS responsive
- Implementar el copy y los assets visuales
- *Dependencia: necesita copy y assets*

### Fase 5: Revisión (Reviewer)
- Revisar calidad del código, copy y diseño
- Verificar consistencia de messaging
- Bug check y mejoras antes de publicar

---

Voy a iniciar delegando las tareas en paralelo donde sea posible. Primero, el researcher y el designer pueden trabajar simultáneamente: