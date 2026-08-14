Sos el asistente de operaciones de un negocio chico. En `/app` están el tablero de tareas
(`tablero.json`) y la transcripción de la reunión de socios de hoy (`reunion.md`).

Actualizá el tablero con lo que se decidió en la reunión y escribí el resultado en
`/app/tablero_actualizado.json`, con la misma forma que el original:

```json
{
  "proyecto": "...",
  "socios": ["..."],
  "tareas": [
    {"id": "T-01", "titulo": "...", "estado": "pendiente|en_curso|hecho",
     "prioridad": "alta|media|baja", "responsable": "...", "nota": "..."}
  ]
}
```

Las tareas nuevas usan los ids que siguen (`T-07`, `T-08`, ...). Podés agregar los campos
que consideres necesarios.
