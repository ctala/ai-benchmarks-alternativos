# GPT-5.6 Luna — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-5.6-luna`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 17.194s | tokens_per_second: 34.6
- input_tokens: 101 | output_tokens: 595
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

## Cuando `success` significa “no explotó”, no “funcionó”

En n8n, una ejecución puede terminar en `success` aunque el workflow no haya producido ningún efecto. El estado describe la ejecución técnica: no hubo una excepción no gestionada. No valida que se haya enviado el email, actualizado el CRM o creado el registro esperado.

Los falsos positivos más comunes:

- Un `IF` toma la rama equivocada y la otra queda sin ejecutar.
- Un nodo recibe cero items y, por tanto, no hace nada.
- `continueOnFail` convierte errores en datos que el flujo sigue procesando.
- Una API responde `2xx`, pero el body contiene `ok: false` o un error de negocio.
- Una expresión devuelve `undefined`, un array vacío o un valor por defecto que oculta el problema.
- El workflow dispara una operación asíncrona y termina antes de que exista confirmación real.

La solución es tratar el efecto esperado como una **invariante**, no como una suposición.

Añade validaciones explícitas después de cada operación crítica:

```js
const result = $input.first().json;

if (result.ok !== true || !result.id) {
  throw new Error(`Operación no confirmada: ${JSON.stringify(result)}`);
}

return $input.all();
```

Antes de un nodo de escritura, valida también que el número de items sea el esperado. Si cero elementos es un error, hazlo fallar deliberadamente; no permitas que un flujo vacío parezca saludable.

Para detectar regresiones, devuelve y registra un resultado estructurado: `processed`, `created`, `updated`, `skipped`, `errors`. Después, añade métricas o alertas sobre valores anómalos, no solo sobre ejecuciones fallidas.

Y revisa los datos de ejecución: un `success` sin nodos de efecto ejecutados es una señal, no una confirmación. La pregunta correcta no es “¿terminó bien?”, sino “¿qué evidencia tengo de que ocurrió lo que debía ocurrir?”.