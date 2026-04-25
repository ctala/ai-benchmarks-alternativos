# Devstral Medium — agent_capabilities/agent_team_delegation

- model_id: `mistralai/devstral-medium`
- success: True  | final: 7.21 | quality: 9.16
- latency_total: 5.957s | tokens_per_second: 121.5
- input_tokens: 970 | output_tokens: 724
- judge_score: 4.4 | justificación: 

## Respuesta completa

Para coordinar la creación de la landing page para "AutoFlow AI", descompondré la tarea en sub-tareas y asignaré cada una a los sub-agentes correspondientes, respetando las dependencias y prioridades.

### Plan de Ejecución

1. **Investigación de la Competencia**
   - **Agente**: researcher
   - **Tarea**: Investigar qué hace la competencia (3 competidores).
   - **Prioridad**: Alta
   - **Dependencia**: Ninguna

2. **Escribir el Copy de la Landing**
   - **Agente**: writer
   - **Tarea**: Escribir el copy de la landing (hero, features, pricing, CTA).
   - **Prioridad**: Alta
   - **Dependencia**: Necesita la información de la competencia del researcher.

3. **Generar el Código HTML/CSS de la Página**
   - **Agente**: coder
   - **Tarea**: Generar el código HTML/CSS de la página.
   - **Prioridad**: Alta
   - **Dependencia**: Necesita el copy del writer.

4. **Crear las Imágenes Hero y de Features**
   - **Agente**: designer
   - **Tarea**: Crear las imágenes hero y de features.
   - **Prioridad**: Alta
   - **Dependencia**: Necesita el copy del writer para asegurarse de que las imágenes coincidan con el contenido.

5. **Revisar Todo Antes de Publicar**
   - **Agente**: reviewer
   - **Tarea**: Revisar todo antes de publicar.
   - **Prioridad**: Urgente
   - **Dependencia**: Necesita el código HTML/CSS del coder y las imágenes del designer.

### Delegación de Tareas

1. **Delegar a researcher**
   - **Tarea**: Investigar qué hace la competencia (3 competidores).
   - **Prioridad**: Alta

2. **Delegar a writer**
   - **Tarea**: Escribir el copy de la landing (hero, features, pricing, CTA).
   - **Prioridad**: Alta
   - **Dependencia**: Información de la competencia del researcher.

3. **Delegar a coder**
   - **Tarea**: Generar el código HTML/CSS de la página.
   - **Prioridad**: Alta
   - **Dependencia**: Copy del writer.

4. **Delegar a designer**
   - **Tarea**: Crear las imágenes hero y de features.
   - **Prioridad**: Alta
   - **Dependencia**: Copy del writer.

5. **Delegar a reviewer**
   - **Tarea**: Revisar todo antes de publicar.
   - **Prioridad**: Urgente
   - **Dependencia**: Código HTML/CSS del coder y imágenes del designer.

### Ejecución

Ahora procederé a delegar las tareas a los sub-agentes correspondientes.