# Qwen 3.6 27B base (OpenRouter FP8) — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 47.1s | tokens_per_second: 64.5
- input_tokens: 110 | output_tokens: 3036

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

Tu workflow termina en “success”, pero nada cambió. No es un bug. Es el contrato del motor: n8n marca success cuando el pipeline completa sin lanzar un error no controlado, no cuando la lógica de negocio se cumplió. Un HTTP Request que devuelve 200 con un array vacío, un Code que transforma datos sin validar invariantes, o un IF que nunca entra en la rama activa: todos terminan en success. El ejecutor no conoce tus expectativas.

Para detectarlo, deja de confiar en el estado de ejecución. Implementa validaciones explícitas:

- Verifica longitudes y estructuras con `IF` o `Item Lists` antes de avanzar. `{{ $input.length === 0 }}` es tu primer filtro.
- En Code, lanza errores personalizados con `throw new Error('payload vacío')` si los datos no cumplen condiciones críticas. n8n los capturará y cambiará el estado a `failed`.
- En HTTP Request, no asumas que 200 equivale a trabajo útil. Valida el cuerpo de respuesta en la rama de éxito y desvía a un manejo de error si falta el campo esperado.
- Añade un `Set` al final que etiquete la ejecución con métricas reales (`items_processed`, `rows_updated`). Filtra en la UI o usa la API de ejecuciones para alertar cuando `success` coincida con métricas nulas.
- Usa `Workflow Execution` logs + tags personalizados para correlacionar success con payloads vacíos o rutas no tomadas.

El estado de n8n es técnico, no semántico. Tu responsabilidad es cerrar la brecha entre “no crash” y “trabajo hecho”. Validar, lanzar errores controlados y medir lo que importa. Así dejas de depurar silencios y empiezas a confiar en tus pipelines.