# Gemini 3.8 Flash — agent_capabilities/agent_team_delegation

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.55 | quality: 9.8
- latency_total: 11.006s | tokens_per_second: 124.8
- input_tokens: 561 | output_tokens: 1374
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundamente útil, con una estructura bien organizada que un emprendedor podría aplicar directamente.

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

### Plan de Ejecución: Landing Page para "AutoFlow AI"

Para asegurar la máxima calidad y coherencia en el lanzamiento, organizaremos el trabajo respetando la cadena de dependencias en 4 fases consecutivas:

---

### Fases y Dependencias

| Fase | Agente | Tarea | Dependencias | Prioridad |
|---|---|---|---|---|
| **Fase 1** | `researcher` | Analizar 3 competidores clave en automatización para startups (features, pricing, propuesta de valor, debilidades). | Ninguna | **Alta** (bloqueante) |
| **Fase 2** | `writer` | Redactar el copy persuasivo estructurado (Hero section, Features diferenciadoras, Pricing y llamadas a la acción/CTA). | Requiere insights de la Fase 1 | **Alta** |
| **Fase 3** *(en paralelo)* | `designer` | Diseñar assets visuales: imagen principal (hero visual) e ilustraciones/iconos de features. | Requiere estructura de copy de la Fase 2 | **Media** |
| **Fase 3** *(en paralelo)* | `coder` | Desarrollar el código HTML5 semántico y CSS moderno/responsive (adaptable a mobile y desktop). | Requiere copy de la Fase 2 | **Alta** |
| **Fase 4** | `reviewer` | Auditoría de calidad integral: ortografía, consistencia del copy, responsive design, accesibilidad web (a11y) y performance. | Requiere entregables de Fases 2 y 3 | **Alta** |

---

Iniciamos con la **Fase 1**, delegando la investigación al sub-agente `researcher`. Una vez completado este informe, activaremos al `writer` con los datos recopilados.