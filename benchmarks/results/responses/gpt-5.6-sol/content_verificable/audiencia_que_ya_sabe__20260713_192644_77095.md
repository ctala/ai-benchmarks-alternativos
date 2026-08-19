# GPT-5.6 Sol — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.42 | quality: 10.0
- latency_total: 9.51s | tokens_per_second: 52.2
- input_tokens: 101 | output_tokens: 496
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil para expertos en n8n, proporcionando soluciones prácticas y detalladas para detectar falsos positivos en workflows.

## Respuesta completa

### “Success” no significa “trabajo hecho”

En n8n, una ejecución puede terminar en verde aunque el resultado operativo sea exactamente cero. “Success” solo confirma que ningún nodo lanzó un error no gestionado; no demuestra que el workflow haya cumplido su objetivo.

Los falsos positivos más comunes:

- **Consultas que devuelven 0 items**: el flujo termina limpiamente, pero ninguna rama posterior se ejecuta.
- **Filtros que descartan todo** por un cambio de esquema, una fecha mal normalizada o una condición demasiado estricta.
- **APIs que responden `200`** con un error funcional en el body: `success: false`, una lista vacía o un estado inesperado.
- **`Continue On Fail` / salida de error** que transforma fallos reales en datos y permite que la ejecución siga verde.
- **Upserts o updates sin efecto**: la operación fue válida, pero `affectedRows`, `modifiedCount` o equivalente es `0`.
- **Loops parciales**: el workflow finaliza, aunque procesó menos elementos de los previstos.

La solución es tratar el resultado esperado como una **invariante verificable**, no como una suposición.

Añade checkpoints explícitos:

1. Captura métricas: items recibidos, filtrados, procesados, descartados y fallidos.
2. Valida respuestas por contenido, no solo por status HTTP.
3. Compara `expected_count` con `processed_count`.
4. Si una condición mínima no se cumple, lanza un error deliberado desde un Code node o enruta a una rama de alerta.
5. Registra un identificador de operación para comprobar efectos externos e idempotencia.
6. Distingue entre `success`, `no-op` y `partial_success`; no metas los tres estados en el mismo verde.

La prueba definitiva no es “¿terminó?”, sino “¿qué evidencia dejó?”. Si el workflow debía crear 50 registros, su contrato de salida debería demostrar que creó 50 —o explicar, de forma observable, por qué no.