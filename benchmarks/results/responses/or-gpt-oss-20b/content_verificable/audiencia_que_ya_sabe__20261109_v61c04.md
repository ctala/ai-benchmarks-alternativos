# GPT-OSS 20B — content_verificable/audiencia_que_ya_sabe

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.4 | quality: 10.0
- latency_total: 6.944s | tokens_per_second: 130.3
- input_tokens: 165 | output_tokens: 905

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

En un flujo ya “establecido” en n8n, el estado *Success* suele ser sinónimo de “todo marchó bien”. Sin embargo, existen varios motivos por los que un workflow puede marcar esa condición sin haber ejecutado efectivamente la acción esperada, y reconocerlo a tiempo evita sorpresas en producción.

1. **Condición “If” que corta la cadena**  
   Cuando la entrada al nodo *If* evalúa a `false`, la rama “No” se ejecuta y los siguientes nodos se omiten. El flujo sigue siendo *Success* aunque el trabajo real no se haya disparado.

2. **Nodos *Noop* o *Set* vacíos**  
   Un *Noop* simplemente pasa los datos sin modificarlos. Si todo el trabajo se hace en esa rama, el resultado final será un objeto idéntico al de entrada, pero el workflow habrá “terminado” sin efectos colaterales.

3. **`continueOnFail:true` en nodos de error**  
   Si un nodo falla pero está configurado para continuar, el flujo completo sigue a *Success*. La falla queda oculta a menos que se verifique explícitamente el estado del nodo.

4. **Ausencia de datos de entrada**  
   Un webhook con una carga vacía o un trigger cron que no produce datos puede lanzar el flujo con `{{$json}}` vacío. El siguiente nodo procesará nada y el estado seguirá siendo *Success*.

### Cómo detectarlo

- **Añade un nodo *Set* al principio** que añada una marca (`"flowStart": true`). Luego, en la rama final, comprueba su existencia con un nodo *If*. Si falta, se lanza una alerta.
- **Usa `{{$node["NombreNodo"].json}}`** en nodos de *Set* para registrar la salida de cada paso clave. Con esto podrás comparar en el log si algo cambió.
- **Activa `continueOnFail:false`** en los nodos críticos. Así, cualquier fallo saldrá como *Failed* y no se perderá la pista.
- **Revisa los logs de ejecución** (`n8n logs`) y habilita la opción *Workflow Logging* para ver el flujo completo, incluso cuando no se produce ninguna acción externa.

Implementar estas verificaciones convierte un *Success* “falso” en un punto de control claro, garantizando que cuando el workflow indique éxito, haya de hecho hecho algo.