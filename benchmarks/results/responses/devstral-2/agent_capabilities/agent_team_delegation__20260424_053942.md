# Devstral 2 (Dic 2025) — agent_capabilities/agent_team_delegation

- model_id: `mistralai/devstral-2512`
- success: True  | final: 7.0 | quality: 8.86
- latency_total: 6.886s | tokens_per_second: 69.9
- input_tokens: 970 | output_tokens: 481
- judge_score: 4.4 | justificación: 

## Respuesta completa

### Plan de Ejecución:

1. **Investigación de la Competencia (researcher)**:
   - El agente `researcher` investigará a 3 competidores directos de "AutoFlow AI" para identificar sus características principales, precios, mensajes clave y estrategias de marketing.
   - **Prioridad**: Alta (esta información es crítica para el copy y el diseño).

2. **Redacción del Copy (writer)**:
   - Una vez que el `researcher` proporcione los datos, el agente `writer` redactará el contenido de la landing page, incluyendo:
     - Sección hero (título, subtítulo, descripción).
     - Sección de características (features).
     - Sección de precios (pricing).
     - Llamado a la acción (CTA).
   - **Prioridad**: Alta (depende de la investigación).

3. **Generación de Código HTML/CSS (coder)**:
   - El agente `coder` generará el código para la landing page basado en el copy proporcionado por el `writer`.
   - **Prioridad**: Media (depende del copy).

4. **Creación de Imágenes (designer)**:
   - El agente `designer` creará las imágenes para la sección hero y las imágenes de las características.
   - **Prioridad**: Media (puede trabajarse en paralelo con el código).

5. **Revisión Final (reviewer)**:
   - El agente `reviewer` revisará todo el contenido, el código y las imágenes para asegurar que no haya errores y que todo cumpla con los estándares de calidad.
   - **Prioridad**: Urgente (último paso antes de la publicación).

### Delegación de Tareas:

1. **Investigación de la Competencia**:
   - Delegar al `researcher` para investigar a 3 competidores de "AutoFlow AI".