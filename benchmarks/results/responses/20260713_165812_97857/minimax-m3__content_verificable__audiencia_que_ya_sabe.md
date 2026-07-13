# MiniMax M3 — content_verificable/audiencia_que_ya_sabe

- model_id: `minimax/minimax-m3`
- success: True  | final: 8.68 | quality: 10.0
- latency_total: 39.682s | tokens_per_second: 118.9
- input_tokens: 260 | output_tokens: 4717
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando soluciones prácticas y detalladas para un público experto.

## Respuesta completa

Esa sensación de ver "Success: true" en los logs y descubrir horas después que el workflow no hizo nada. Bienvenido al club.

En n8n, "success" solo significa que el último nodo no lanzó una excepción. Y eso abre varios huecos:

**Ramas silenciosas.** Tu IF tiene dos ramas y la "false" no va a ningún lado. Los datos caen ahí, el flujo muere sin error, y n8n lo marca como exitoso.

**Continue on Fail enmascarando fallos.** El nodo sigue río abajo con datos vacíos. La ejecución sale en verde aunque el HTTP Request haya devuelto 500.

**APIs que devuelven 200 con `[]`.** Funcionó, devolvió array vacío, y procesas cero registros sin error ni alerta.

**El último nodo trivial.** Terminas con un Set, NoOp o un IF cuyas ramas convergen en nada útil. n8n ejecuta eso y marca success.

**Cómo detectarlo:**

1. No te fíes del check verde. Abre "Data" en cada nodo de la ejecución. Si un nodo crítico procesó 0 items, ahí está tu problema.
2. Pon un Code node guardián al final que aserte que los datos esperados existen. Si no, `throw new Error()`.
3. Convierte "no hice nada" en error real. Cuando una rama del IF signifique "no se procesó", enrútala a un **Stop and Error** con mensaje claro.
4. Monitoriza item counts por nodo. Revisa si algún nodo central cae a 0 cuando no debería.
5. La respuesta del webhook no es el resultado. "Workflow executed successfully" solo confirma que terminó, no que hizo lo que querías.

Regla de oro: si el éxito puede ocurrir sin que tu intención se cumpla, no es éxito — es un fallo silencioso.