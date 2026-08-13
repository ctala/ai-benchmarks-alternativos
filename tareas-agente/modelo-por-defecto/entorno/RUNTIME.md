# Estado del runtime

Este archivo lo escribe el supervisor al arrancar. Refleja lo que está corriendo AHORA.

| | |
|---|---|
| Motor | Ollama |
| Puerto | 11434 |
| Modelo cargado | `nemotron3-nano-omni-30b-a3b-reasoning` |
| Formato del nombre en LiteLLM | los modelos de Ollama se declaran como `ollama/<nombre>` |

> El gateway (`config.yaml`) apunta hoy a un vLLM en el puerto 8000 que **ya no está
> corriendo**. Las entradas que apunten ahí no responden.
