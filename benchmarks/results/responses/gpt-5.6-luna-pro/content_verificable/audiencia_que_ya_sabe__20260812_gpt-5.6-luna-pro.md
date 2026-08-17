# GPT-5.6 Luna Pro — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-5.6-luna-pro`
- success: True  | final: 8.92 | quality: 10.0
- latency_total: 14.341s | tokens_per_second: 152.6
- input_tokens: 3613 | output_tokens: 2189

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## Cuando `success` es una mentira útil

En n8n, una ejecución marcada como `success` solo significa que el workflow no lanzó una excepción no controlada. No significa que haya producido el efecto esperado.

Algunos casos habituales:

- Un `IF` toma la rama falsa y termina correctamente.
- Un nodo HTTP recibe un `204` o un `200` con un payload inesperado.
- `Continue On Fail` convierte un error operativo en datos que nadie valida.
- Un nodo devuelve cero items y los siguientes simplemente no ejecutan nada.
- Se dispara un proceso asíncrono, pero nunca se comprueba su estado final.
- La escritura en una API responde “aceptado”, aunque el registro no exista después.

La solución es dejar de validar “que el nodo terminó” y empezar a validar postcondiciones.

Después de cada operación crítica, añade una comprobación explícita:

- ¿Se procesó exactamente el número esperado de items?
- ¿La respuesta contiene el identificador generado?
- ¿El estado final coincide con `completed`, no solo con `accepted`?
- ¿La consulta posterior confirma que el registro existe?
- ¿El resultado conserva invariantes básicas: totales, claves, checksum, versión?

Si una condición falla, fuerza el workflow a fallar. Un `Code` node que lance un error con contexto suele ser suficiente:

```js
if (!$json.id || $json.status !== 'completed') {
  throw new Error(`Postcondición inválida: ${JSON.stringify($json)}`);
}
return $input.all();
```

También conviene registrar métricas de negocio, no solo el estado técnico: items recibidos, enviados, descartados y confirmados. Y tratar `Continue On Fail` como una decisión que exige una rama de manejo, no como una estrategia de resiliencia.

La pregunta operativa no es “¿terminó el workflow?”, sino: **“¿qué evidencia tengo de que ocurrió lo que debía ocurrir?”**