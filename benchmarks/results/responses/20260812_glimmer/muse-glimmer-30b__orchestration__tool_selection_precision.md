# Muse Glimmer 30B — orchestration/tool_selection_precision

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 3.92 | quality: 2.5
- latency_total: 4.715s | tokens_per_second: 145.3
- input_tokens: 1293 | output_tokens: 685
- judge_score: 4.8 | justificación: 

## Respuesta completa

Para cada tarea la herramienta más adecuada sería:

**Tarea 1: Verificar si el servidor de producción está respondiendo**
* Herramienta: `http_request`
* Por qué: Necesitas hacer una petición HTTP real a `https://api.example.com/health` y comprobar el código de estado / cuerpo de respuesta. `http_request` es la única herramienta diseñada para interactuar con APIs web. `search_web` buscaría información indexada, no haría un health-check en vivo.

**Tarea 2: Obtener el conteo de usuarios activos del último mes**
* Herramienta: `query_database`
* Por qué: El conteo de usuarios activos es un dato interno de tu sistema. Se obtiene con una consulta SQL a la base de datos de usuarios. `search_web` o `http_request` no accederían a tus datos internos.

**Tarea 3: Calcular el promedio de 3 números: 45, 67, 89**
* Herramienta: `run_script`
* Por qué: Es un cálculo determinista rápido. `run_script` con Python permite ejecutar la operación de forma reproducible. No requiere acceso a web, archivo o base de datos.

**Tarea 4: Encontrar artículos recientes sobre competidores**
* Herramienta: `search_web`
* Por qué: Necesitas información pública y actualizada de la web. `search_web` está pensado para búsquedas en internet. `query_database` solo consulta datos internos.

Ahora ejecuto la Tarea 1:
