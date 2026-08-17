# Claude Opus 5 — content_verificable/audiencia_que_ya_sabe

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.19 | quality: 10.0
- latency_total: 21.94s | tokens_per_second: 58.3
- input_tokens: 159 | output_tokens: 1280

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa

## El "success" verde que no hizo nada

Un workflow termina en verde cuando ningún nodo lanza un error. Eso es todo. No significa que haya escrito una fila, mandado un email ni tocado la API.

**Los sospechosos habituales:**

**Array vacío.** Si un nodo recibe cero items, los nodos siguientes no se ejecutan y la ejecución cierra en verde. Un Filter que descarta todo, un IF cuya rama conectada se queda sin items, un Get Many con un filtro mal formado: mismo resultado visual que un día de trabajo perfecto.

**Always Output Data.** Convierte "no hay nada" en `[{}]`. Ahora sí se ejecuta lo de abajo, con un item fantasma que escribe nulls en tu base de datos.

**HTTP 200 con error dentro.** GraphQL, endpoints batch, Composite de Salesforce: status 200, body con `errors[]`. Si no lo parseas, no existe.

**onError: continueRegularOutput.** Lo pusiste una vez para un caso puntual y ahora se come todo lo que pasa por ahí.

**Upsert sin match.** Matching column vacía o mal mapeada: 0 filas afectadas, sin queja alguna.

**Cómo detectarlo:**

Deja de confiar en el estado de la ejecución y afirma expectativas. Un Code node como checkpoint:

```js
const n = $input.all().length;
if (n === 0) throw new Error('Checkpoint vacío: 0 items tras Filter');
if (n < 10) throw new Error(`Solo ${n} items, esperaba ≥10`);
return $input.all();
```

Compara conteos punta a punta con `$('Nodo origen').all().length` frente al final. Valida los bodies, no solo el status. Y monitorea el efecto secundario, no el workflow: un dead-man's switch que revise "¿hay filas nuevas en las últimas 2 horas?" detecta más incidentes que cualquier alerta de fallo.

Verde no es evidencia. Es ausencia de excepciones.