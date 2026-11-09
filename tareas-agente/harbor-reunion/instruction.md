Eres el asistente de operaciones de un negocio chico. En `/app` tienes:

- `tablero.json` — el tablero de tareas como está hoy
- `reunion.md` — la transcripción de la reunión de socios
- `politica.md` — las reglas para actualizar el tablero. **Se cumplen todas.**

Actualiza el tablero con lo que se decidió y escribe el resultado en
`/app/tablero_actualizado.json`, con la misma forma que el original: cada tarea con `id`,
`titulo`, `estado` (`pendiente`, `en_curso` o `hecho`), `prioridad` (`alta`, `media` o
`baja`), `responsable` y `nota`.

Las tareas nuevas usan los ids que siguen (`T-07`, `T-08`, ...). Puedes agregar los campos
que consideres necesarios.
