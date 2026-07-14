# Qwen3 Coder — content_verificable/audiencia_que_ya_sabe

- model_id: `qwen/qwen3-coder`
- success: True  | final: 8.72 | quality: 10.0
- latency_total: 21.4s | tokens_per_second: 14.6
- input_tokens: 109 | output_tokens: 313
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y profundiza en los problemas comunes y soluciones para detectar workflows que devuelven 'success' sin ejecutar acciones, siendo altamente útil para la audiencia objetivo.

## Respuesta completa

En n8n, un workflow puede devolver `'success'` sin haber ejecutado ninguna acción real. Esto ocurre cuando todas las condiciones de un nodo **Switch** o **IF** resultan falsas, y no hay nodos alternativos configurados. El workflow termina "exitosamente", pero no se ejecuta ninguna operación útil.

Otro caso común: nodos configurados con **expresiones incompletas** o mal evaluadas. Por ejemplo, si un nodo HTTP Request depende de una variable que no existe o es `null`, puede no lanzar un error, pero tampoco hacer la llamada.

También puedes tener nodos **desactivados** accidentalmente, o workflows que empiezan con un **trigger manual** que no se dispara porque nadie lo activó.

Para detectar este tipo de situaciones:

1. **Revisa el log de ejecución**: busca nodos en gris (no ejecutados).
2. **Activa el modo Debug**: muestra todas las evaluaciones de expresiones.
3. **Usa el panel de métricas**: compara ejecuciones vacías vs. con resultados.
4. **Agrega nodos de logging o dummy**: para asegurarte de que el flujo pasa por donde debe.

Un workflow silencioso no siempre es un workflow inútil, pero puede serlo. Monitorea bien tus flujos — especialmente cuando todo parece “funcionar”, pero no ves cambios.