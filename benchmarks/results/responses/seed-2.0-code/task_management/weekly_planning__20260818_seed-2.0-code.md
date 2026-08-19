# Seed 2.0 Code — task_management/weekly_planning

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 7.54 | quality: 8.6
- latency_total: 36.865s | tokens_per_second: 55.6
- input_tokens: 242 | output_tokens: 2048
- judge_score: 4.0 | justificación: La respuesta es precisa, relevante y ofrece una estructura útil para la planificación semanal, con claridad y profundidad adecuadas para un product manager.

## Entrada exacta (lo que recibió el modelo)

**user:**

Soy product manager. Mi semana tiene estas restricciones:
- Lunes: reunion de directivos 9-11 AM, almuerzo con cliente 1-2 PM
- Martes: libre todo el dia
- Miercoles: demo de producto 3-4 PM
- Jueves: entrevistas de hiring 10 AM - 1 PM
- Viernes: retrospectiva 4-5 PM

Necesito meter estas tareas en la semana:
1. Preparar presentacion para la demo (3 horas)
2. Revisar PRDs pendientes (2 horas)
3. Escribir OKRs Q3 (4 horas)
4. Responder emails de stakeholders (1 hora diaria)
5. Revisar metricas del producto (1 hora)
6. One-on-one con 3 reportes directos (30 min cada uno)

Crea un plan semanal detallado con bloques de tiempo especificos.


## Respuesta completa


El usuario es Product Manager, necesita un plan semanal detallado con sus restricciones y tareas. Primero, voy a listar TODAS las restricciones primero para no olvidarlas:

### RESTRICCIONES FIJAS (NO TOCAR):
- Lunes: 9-11h Directivos; 13-14h Almuerzo Cliente
- Martes: TODO LIBRE
- Miércoles: 15-16h Demo Producto
- Jueves: 10-13h Hiring Entrevistas
- Viernes: 16-17h Retrospectiva

### TAREAS A ASIGNAR (CON DURACIÓN Y REQUISITOS LÓGICOS QUE EL USUARIO NO DIJO PERO SON DE PM):
1. Preparar Demo (3h): **DEBE SER ANTES DEL MIÉRCOLES 15h** (porque es para la demo del miércoles). Mejor cerca de la demo pero no el mismo día por imprevistos.
2. Revisar PRDs (2h): Tarea de concentración, no después de reuniones muy intensas.
3. Escribir OKRs Q3 (4h): Tarea DE MUCHA CONCENTRACIÓN, necesita bloques largos (mejor 2h x 2 días, o un bloque de 4h si hay espacio). Martes es libre, pero hay que distribuir? O martes tiene espacio para bloques largos.
4. Responder emails stakeholders (1h DIARIA): Tarea reactiva, mejor al inicio o fin del día, no en bloques de concentración.
5. Revisar métricas (1h): Tarea estructurada, puede ser después de emails o antes de reuniones. Mejor viernes? O lunes para ver la semana anterior?
6. One-on-ones (3x30min = 1.5h): Mejor en días con reuniones, no en bloques de concentración. Cada uno 30min, puede ser seguidos o separados, pero mejor en horarios que no sean de concentración.

AHORA, VOY A ESTRUCTURAR CADA DÍA CON BLOQUES DE TIEMPO, USANDO UNA JORNADA LABORAL ESTÁNDAR DE PM: 8h30 a 18h (con almuerzo de 12h30 a 13h30? PERO OJO: LUNES TIENE ALMUERZO DE 13-14h, ASÍ QUE AJUSTAR EL ALMUERZO DE LOS OTROS DÍAS PARA SER COHERENTES, O PERMITIR FLEXIBILIDAD PERO MARCARLO.

PRIMERO, DEFINIR JORNADA BASE: 8:30 - 18:00. Almuerzo: 12:30 - 13:30, EXCEPTO LUNES (que tiene almuerzo cliente de 13-14, así que el almuerzo "libre" de lunes es ajustado).

AHORA, ASIGNAR EMAILS (1h DIARIA): Mejor al INICIO DEL DÍA (8:30-9:30) O AL FINAL (17:00-18:00), PERO:
- Lunes: 8:30-9:00 (porque 9-11 es reunión directivos, no puede ser 8:30-9:30) → ajustar emails de lunes a 8:30-9:00, y el resto? O tal vez algunos días al inicio, otros al fin, pero cumplir 1h por día.

TAREA CLAVE: PREPARAR DEMO (3h) ANTES DE MIÉRCOLES 15h. Mejor martes o miércoles por la mañana? Miércoles por la mañana es bueno porque está cerca de la demo, pero no el mismo día? O martes por la tarde para tener tiempo de ajustar.

OKRs Q3 (4h): NECESITA BLOQUES LARGOS DE CONCENTRACIÓN. Martes es TODO LIBRE, así que martes por la mañana y tarde? O martes 2h y jueves 2h? Pero jueves tiene 10-13h de hiring, así que jueves por la tarde es posible.

ONE-ON-ONES (3x30min): Mejor asignarlos en días con reuniones, no en bloques de concentración. Por ejemplo:
- Lunes después de almuerzo cliente (14-14:30, 14:30-15:00, 15:00-15:30) → 3 one-on-ones seguidos, perfecto porque lunes tiene reuniones, así que no rompe bloques de concentración.

REVISAR PRDs (2h): Bloque de concentración, por ejemplo jueves por la tarde después de hiring.

REVISAR MÉTRICAS (1h): Viernes por la mañana, antes de la retrospectiva, para ver las métricas de la semana y comentarlas en la retrospectiva? O lunes por la mañana para ver la semana anterior. Mejor viernes por la mañana, porque la retrospectiva es de equipo, así que puede traer las métricas.

AHORA, VAMOS A ARMAR CADA DÍA PASO A PASO, CON BLOQUES ESPECÍFICOS, Y JUSTIFICAR CADA ASIGNACIÓN POR QUÉ ESE HORARIO (PORQUE EL USUARIO ES PM, NECESITA VER LA LÓGICA DETRÁS, NO SOLO EL HORARIO).

PRIMERO, LISTAR REGLAS DE ASIGNACIÓN QUE USÉ (PARA QUE EL USUARIO LO ENTENDER):
1. **Tareas de alta concentración (OKRs Q3, preparar demo, revisar PRDs):** Asignadas a bloques de 2-3h sin interrupciones, preferentemente en días sin reuniones largas (Martes) o después de reuniones estructuradas (Jueves después de hiring).
2. **Tareas diarias (emails stakeholders):** Asignadas al inicio o fin del día para no romper bloques de concentración.
3. **Tareas ligadas a eventos (preparar demo):** Asignadas ANTES del evento (Miércoles 15h) con margen de seguridad (no el mismo día del evento para imprevistos).
4. **One-on-ones:** Asignados en bloque seguido en un día con reuniones ya programadas (Lunes) para no dispersar el tiempo de concentración de otros días.
5. **Revisar métricas:** Asignada el Viernes por la mañana para traer datos actualizados a la retrospectiva de equipo.

AHORA, ARMAR CADA DÍA CON HORARIOS ESPECÍFICOS, TAREA, DURACIÓN, Y JUSTIFICACIÓN (ESPECIAL PARA PM):

---

### PLAN SEMANAL DETALLADO (JORNADA LABORAL: 8:30 - 18:00 | ALMUERZO BASE: 12:30 - 13:30, AJUSTADO POR RESTRICCIONES)
#### **LUNES (RESTRICCIONES FIJAS: 9-11h Directivos | 13-14h Almuerzo Cliente)**
| Horario       | Tarea                                  | Duración | Justificación (PM)                                                                 |
|---------------|----------------------------------------|----------|-------------------------------------------------------------------------------------|
| 8:30 - 9:30   | Responder emails de stakeholders      | 1h       | Bloque inicial del día para limpiar bandeja ANTES de la reunión de directivos (no rompe concentración después) |
| 9:00 - 11:00  | REUNIÓN FIJA: Directivos              | 2h       | Restricción obligatoria                                                             |
| 11:00 - 12:30 | [Bloque libre para imprevistos]       | 1.5h     | Reuniones de directivos suelen generar tareas urgentes; margen de seguridad      |
| 12:30 - 13:00 | Almuerzo previo (rápido)              | 0.5h     | Ajuste por almuerzo cliente de 13-14h; no saltar comida                            |
| 13:00 - 14:00  | REUNIÓN FIJA: Almuerzo Cliente        | 1h       | Restricción obligatoria                                                             |
| 14:00 - 15:30  | One-on-one con 3 reportes directos    | 1.5h     | Bloque seguido después de reuniones ya programadas; no dispersa días de concentración