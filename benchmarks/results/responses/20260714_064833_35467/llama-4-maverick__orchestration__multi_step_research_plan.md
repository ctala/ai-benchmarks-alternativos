# Llama 4 Maverick — orchestration/multi_step_research_plan

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 7.61 | quality: 8.32
- latency_total: 9.432s | tokens_per_second: 38.9
- input_tokens: 1449 | output_tokens: 367
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para preparar el reporte solicitado, se deben realizar varias tareas de investigación y análisis de datos. A continuación, se presentan los pasos necesarios para completar el reporte:

### Plan de Acción

1. **Buscar las 5 principales startups de IA en Chile con su funding**:
   - Utilizar la función `search_web` para encontrar información sobre startups de IA en Chile y su financiamiento.

2. **Comparar con el mercado de IA en Colombia y México**:
   - Utilizar la función `search_web` para obtener información sobre el estado del mercado de IA en Colombia y México.

3. **Obtener datos de inversión VC en tecnología en Chile para 2025-2026**:
   - Utilizar la función `search_web` o `query_database` (si se tiene acceso a una base de datos relevante) para encontrar datos sobre inversión de capital de riesgo (VC) en tecnología en Chile para los años 2025 y 2026.

4. **Crear un resumen ejecutivo de 1 página**:
   - Una vez recopilada la información, se analizarán los datos y se redactará un resumen ejecutivo.

### Dependencias entre Pasos

- Los pasos 1, 2 y 3 se pueden ejecutar en paralelo ya que son tareas de investigación independientes.
- El paso 4 depende de la finalización de los pasos 1, 2 y 3, ya que requiere la información recopilada y analizada en esos pasos.

### Ejecución del Primer Paso

Se iniciará con el paso 1: Buscar las 5 principales startups de IA en Chile con su funding.

```json
[search_web(query="top 5 AI startups in Chile with funding")]
```

Ejecutaré la función:
```
[search_web(query="top 5 AI startups in Chile with funding")]
```