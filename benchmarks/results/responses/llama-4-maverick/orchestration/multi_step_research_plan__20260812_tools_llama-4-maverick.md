# Llama 4 Maverick — orchestration/multi_step_research_plan

- model_id: `meta-llama/llama-4-maverick`
- success: True  | final: 7.94 | quality: 7.92
- latency_total: 2.287s | tokens_per_second: 130.3
- input_tokens: 1321 | output_tokens: 298
- judge_score: 3.8 | justificación: 

## Respuesta completa

Para preparar el reporte solicitado, se deben realizar varias tareas de investigación y análisis de datos. A continuación, se presentan los pasos necesarios para completar el reporte:

**Paso 1: Buscar información sobre las 5 principales startups de IA en Chile y su funding**
- Utilizar la función `search_web` para encontrar esta información.

**Paso 2: Comparar el mercado de IA en Chile con el de Colombia y México**
- Utilizar la función `search_web` para recopilar información sobre el mercado de IA en Colombia y México.

**Paso 3: Obtener datos de inversión VC en tecnología en Chile para 2025-2026**
- Utilizar la función `search_web` o `query_database` (si se tiene acceso a una base de datos relevante) para encontrar estos datos.

**Paso 4: Redactar el resumen ejecutivo de 1 página**
- Requiere la información recopilada en los pasos anteriores.

**Dependencias:**
- El Paso 4 depende de los resultados de los Pasos 1, 2 y 3.

**Paralelismo:**
- Los Pasos 1, 2 y 3 se pueden ejecutar en paralelo ya que son tareas de investigación independientes.

El primer paso es buscar información sobre las 5 principales startups de IA en Chile y su funding. Se ejecutará la función `search_web` con la consulta adecuada.

[search_web(query="Top 5 AI startups in Chile funding")]