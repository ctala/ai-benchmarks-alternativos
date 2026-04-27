# Llama 3.1 8B Instant (Groq) — agent_capabilities/agent_team_delegation

- model_id: `llama-3.1-8b-instant`
- success: True  | final: 7.17 | quality: 7.62
- latency_total: 1.353s | tokens_per_second: 628.1
- input_tokens: 1046 | output_tokens: 850
- judge_score: 3.8 | justificación: 

## Respuesta completa

Lo primero que debemos hacer es descomponer la tarea en sub-tareas para cada agente:

1. Investigar que hace la competencia (3 competidores):
 * researcher: busca informacion y datos sobre las 3 competidoras
 * coder: genera una matriz de comparacion de caracteristicas y precios
 * reviewer: revisa la calidad y relevancia de la informacion
 * designer: crea un diagrama de fuerzas competitivas

2. Escribir el copy de la landing (hero, features, pricing, CTA):
 * writer: redacta el contenido de la landing
 * designer: crea un plano de contenido visual

3. Generar el codigo HTML/CSS de la pagina:
 * coder: crea el codigo HTML/CSS de la pagina

4. Crear las imagenes hero y de features:
 * designer: crea las imagenes hero y de features

5. Revisar todo antes de publicar:
 * reviewer: revisa la calidad y errores de la landing
 * researcher: revisa la informacion de la landing
 * writer: revisa el contenido de la landing
 * coder: revisa el codigo HTML/CSS de la pagina
 * designer: revisa las imagenes y el plano de contenido visual

Ahora, podemos delegar las tareas a los sub-agentes de la siguiente manera:

