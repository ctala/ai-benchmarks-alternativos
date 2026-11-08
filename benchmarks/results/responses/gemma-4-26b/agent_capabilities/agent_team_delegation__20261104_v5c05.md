# Gemma 4 26B MoE (3.8B activos) — agent_capabilities/agent_team_delegation

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 8.71 | quality: 9.8
- latency_total: 21.957s | tokens_per_second: 25.3
- input_tokens: 898 | output_tokens: 555
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

Entendido. Para el lanzamiento de **AutoFlow AI**, he diseñado un plan de ejecución estructurado por fases para asegurar que la calidad del producto final sea óptima y que el flujo de trabajo respete las dependencias técnicas.

### Plan de Ejecución: Lanzamiento "AutoFlow AI"

**Fase 1: Inteligencia de Mercado (Investigación)**
*   **Agente:** `researcher`
*   **Objetivo:** Analizar a 3 competidores directos en el sector de automatización para startups, identificando sus puntos fuertes, debilidades y modelos de precios. Esto servirá de base para que el copy sea diferenciador.

**Fase 2: Estrategia de Contenido (Copywriting)**
*   **Agente:** `writer` (Depende de la Fase 1)
*   **Objetivo:** Redactar el contenido persuasivo de la landing page (Hero, Features, Pricing, CTAs) utilizando los insights de la investigación para posicionar a AutoFlow AI como la solución superior.

**Fase 3: Diseño y Activos Visuales**
*   **Agente:** `designer` (Depende de la Fase 2)
*   **Objetivo:** Crear la imagen "Hero" y los iconos/imágenes de las funcionalidades basándose en el tono de voz y el concepto definido por el `writer`.

**Fase 4: Desarrollo Técnico**
*   **Agente:** `coder` (Depende de las Fases 2 y 3)
*   **Objetivo:** Escribir el código HTML y CSS limpio y responsivo que integre el copy y los assets visuales creados.

**Fase 5: Control de Calidad (QA)**
*   **Agente:** `reviewer` (Depende de la Fase 4)
*   **Objetivo:** Realizar una auditoría integral: revisar ortografía/gramática en el copy, verificar la coherencia visual y asegurar que el código sea funcional y libre de errores.

---

Comenzaré ahora mismo con la primera fase.

