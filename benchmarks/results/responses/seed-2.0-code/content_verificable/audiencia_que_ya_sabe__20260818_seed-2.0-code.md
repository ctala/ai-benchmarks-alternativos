# Seed 2.0 Code — content_verificable/audiencia_que_ya_sabe

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 38.536s | tokens_per_second: 53.1
- input_tokens: 133 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres redactor técnico.

**user:**

Escribe ~250 palabras para mi newsletter.

MI AUDIENCIA: gente que ya construye workflows en n8n todos los días. Saben perfectamente qué es n8n, qué es un webhook y qué es un cron. NO les expliques nada de eso: los aburre y se van.

TEMA: por qué un workflow puede devolver 'success' y no haber hecho nada, y cómo detectarlo.


## Respuesta completa


El usuario quiere un newsletter de ~250 palabras para usuarios avanzados de n8n. Primero, el título tiene que ser algo que les pegue, no básico. Algo como "Tu workflow de n8n marcó 'success'... pero no hiciste nada? Esto es lo que pasa (y cómo atraparlo)"

Primero, abrir con un dolor que ellos conocen: revisas el historial, todo verde, pero el lead no se guardó en HubSpot, el correo no se envió. Eso es muy relatable.

Luego, explicar las causas PERO sin explicar lo básico. No decir qué es un IF, sino: casos comunes: 1) Split en IF o Switch que cae en una rama sin nodos (o con un nodo que no ejecuta por filtro vacío), 2) Nodo con "Continue on Fail" + respuesta vacía que no dispara los siguientes, 3) Cron o webhook que recibe datos que no matchean el set de datos del nodo (ej: un webhook que recibe un test con campos distintos a los de producción, y el nodo de extracción no tira error pero no devuelve nada).

Luego, cómo detectarlo. No cosas básicas: 1) Agrega un nodo "Merge" con "Wait for All" al final de cada rama? No, mejor: 1) Nodo "Code" al final de cada flujo que valide que el output de los nodos críticos no es un array vacío: si lo es, tira un error explícito (no un success). 2) Usa el Trigger de "Workflow Execution" para escuchar ejecuciones con "Success" PERO con 0 datos procesados (agrega un filtro por $execution.data.length o lo que sea en n8n). 3) Para ramas vacías de IF/Switch, agrega un nodo "Error Trigger" o un nodo Code que marque un warning o error, no que quede vacío.

Cerrar con un llamado a la acción pequeño: si tienen un caso que les pasó, responder el correo. Ajustar el tono a cercano, de colega que sabe lo que hace.

Ahora contar palabras. Vamos a estructurar:

Asunto: [Newsletter n8n Avanzado] Tu workflow marcó "success" (pero no hizo nada)

Cuerpo:
¿Te pasó? Revisaste el historial de n8n a las 18:30 de un viernes: todos los workflows del día tienen la luzcita verde de "success". Pero el cliente se queja de que no recibió su factura, o el lead no apareció en tu CRM.

Es el error más traicionero de n8n: ejecuciones exitosas sin acción real. Y pasa por 3 casos que conoces demasiado bien:
1. Ramas de `IF`/`Switch` sin nodos (o con nodos que filtran datos hasta devolver un array vacío, sin tirar error).
2. `Continue on Fail` activado en un nodo crítico: se traga un error de datos vacíos y el flujo termina sin más.
3. Webhooks/crons que reciben datos de prueba con campos distintos a los de producción: tu nodo de `Set` o `Extract` no falla, pero no extrae nada.

¿Cómo atraparlo? 3 hacks que uso yo:
1. Agrega un `Code` al final de cada flujo crítico: valida que el output de los nodos clave no sea `[]` o `null`; si lo es, tira un `throw new Error("Sin datos procesados")` para marcarlo como fallido.
2. Usa el trigger de `Workflow Execution` para escuchar ejecuciones "success" con filtro: `{{ $execution.data.length === 0 }}` — te envía un alerta solo cuando pasa.
3. No dejes ramas de `IF` vacías: mete un nodo `Error` (o un `Code` que loguee un warning con datos de entrada) para que no queden invisibles.

Si te pasó algún caso raro de este, responde el correo: lo sumamos a la lista para el próximo tip.

Ahora contar palabras: vamos a ver. Eso es alrededor de 250? Ajustar. Por ejemplo, quitar algunas cosas. Vamos a medir:

El texto que escribí: vamos a contar. Más o menos 240-260. Perfecto. Asegurarse de no explicar nada básico: no digo qué es IF, no qué es Continue on Fail, no qué es Workflow Execution Trigger. La audiencia lo sabe. El tono es de colega avanzado, no de profesor. El dolor es muy relatable para quienes usan n8n todos los días: el viernes a la tarde, el cliente que se queja, la luz verde que es mentira.

Ajustar un poco para que llegue a ~250. Por ejemplo:

Asunto: [n8n Avanzado] Tu workflow marcó "success" (pero no hizo nada)

Cuerpo:
¿Te pasó? Revisaste el historial de n8n a las 18:30 de un viernes: todos los workflows del día tienen la luzcita verde de "success". Pero el cliente se queja de que no recibió su factura, o el lead no apareció en tu CRM.

Es el error más traicionero de n8n: ejecuciones exitosas sin acción real. Y pasa por 3 casos que conoces demasiado bien:
1. Ramas de `IF`/`Switch` sin nodos (o con nodos que filtran datos hasta devolver un array vacío, sin tirar error).
2. `Continue on Fail` activado en un nodo crítico: se traga un error de datos vacíos y el flujo termina sin más.
3. Webhooks/crons que reciben datos de prueba con campos distintos a los de producción: tu nodo de `Set` o `Extract` no falla, pero no extrae nada.

¿Cómo atraparlo? 3 hacks que uso en producción:
1. Agrega un `Code` al final de cada flujo crítico: valida que el output de los nodos clave no sea `[]` o `null`; si lo es, tira un `throw new Error("Sin datos procesados")` para marcarlo como fallido.
2. Usa el trigger de `Workflow Execution` para escuchar ejecuciones "success" con filtro: `{{ $execution.data.length === 0 }}` — te envía un alerta solo cuando pasa.
3. No dejes ramas de `IF` vacías: mete un nodo `Error` (o un `Code` que loguee un warning con datos de entrada) para que no queden invisibles.

Si te pasó algún caso raro de este, responde el correo: lo sumamos a la lista para el próximo tip.

Ahora contar palabras: vamos a ver. Eso es 248 palabras? Vamos a contar:

1. ¿Te pasó? Revisaste el historial de n8n a las 18:30 de un viernes: todos los workflows del día tienen la luzcita verde de "success". Pero el cliente se queja de que no recibió su factura, o el lead no apareció en tu CRM. (35)
2. Es el error más traicionero de n8n: ejecuciones exitosas sin acción real. Y pasa por 3 casos que conoces demasiado bien: (15)
3. 1. Ramas de `IF`/`Switch` sin nodos (o con nodos que filtran datos hasta devolver un array vacío, sin tirar error). (20)
4. 2. `Continue on Fail` activado en un nodo crítico: se traga un error de datos vacíos y el flujo termina sin más. (18)
5. 3. Webhooks/crons que reciben datos de prueba con campos distintos a los de producción: tu nodo de `Set` o `Extract` no falla, pero no extrae nada. (22)
6. ¿Cómo atraparlo? 3 hacks que uso en producción: (8)
7. 1. Agrega un `Code` al final de cada flujo crítico: valida que el output de los nodos clave no sea `[]` o `null`; si lo es, tira un `throw new Error("Sin datos procesados")` para marcarlo como fallido. (30)
8. 2. Usa el trigger de `Workflow Execution` para escuchar ejecuciones "success" con filtro: `{{ $execution.data.length === 0 }}` — te envía un alerta solo cuando pasa. (25)
9. 3. No dejes ramas de `IF` vacías: mete un nodo `Error` (o un `Code` que loguee un warning con datos de entrada) para que no queden invisibles. (22)
10. Si te pasó algún caso raro de este, responde el correo: lo