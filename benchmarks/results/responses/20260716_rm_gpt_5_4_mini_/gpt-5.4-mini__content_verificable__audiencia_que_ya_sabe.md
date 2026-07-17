# GPT-5.4 Mini — content_verificable/audiencia_que_ya_sabe

- model_id: `gpt-5.4-mini`
- success: True  | final: 9.19 | quality: 10.0
- latency_total: 4.113s | tokens_per_second: 96.0
- input_tokens: 101 | output_tokens: 395
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando estrategias prácticas y detalladas para detectar workflows que devuelven 'success' sin realizar trabajo útil.

## Respuesta completa

En n8n, que un workflow termine en **success** no significa necesariamente que haya **hecho trabajo útil**. Significa, en muchos casos, que el grafo se ejecutó sin lanzar errores. Y eso deja una zona gris peligrosa: ejecuciones “verdes” que en realidad no movieron ni un dato.

El caso más común es el de los **nodos que reciben cero items**. Si un nodo anterior filtra todo, si una expresión devuelve vacío, si un IF manda la rama “correcta” pero sin payload, el resto del workflow puede seguir “bien” hasta el final, pero sin procesar nada. También pasa con ramas que terminan en nodos finales sin side effects, con merges que no encuentran pareja, o con transforms que generan estructuras vacías pero válidas.

¿Cómo detectarlo?

1. **Mide el volumen de entrada y salida por nodo.**  
   Si un workflow “funciona” pero siempre entra con 0, 1 o muy pocos items, algo está mal. No mires solo el estado; mira el conteo.

2. **Añade checks explícitos de no-op.**  
   Un IF o Code node que corte la ejecución cuando `items.length === 0` puede ahorrarte horas de debugging silencioso.

3. **Loguea intención, no solo resultado.**  
   Guarda en un Data Store, Slack o incluso en un execution note qué esperaba hacer el workflow: “procesar 42 leads”, “actualizar 18 invoices”. Si el número real es 0, salta la alarma.

4. **Diferencia éxito técnico de éxito funcional.**  
   “No hubo error” no es una métrica. “Se actualizaron X registros” sí.

La regla práctica: si no puedes responder en una línea **qué cambió** gracias a esa ejecución, entonces ese success probablemente fue solo decorativo.