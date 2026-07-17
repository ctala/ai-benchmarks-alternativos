# MiniMax M2.7 Highspeed

- **model_id**: `MiniMax-M2.7-highspeed`
- **Total tests**: 4/4 exitosos (0 errores)
- **Score final**: 6.50
- **Calidad**: 5.00
- **Velocidad**: 46 tok/s
- **Latencia primera token**: 3.20s
- **Costo promedio por test**: $0.00036

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| tool_calling | 4 | 4 | 6.50 | 5.00 |

## Detalle por test

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 6.62 | 5.00 | - | 42 | 3.25s | OK |
| multi_tool_sequential | 6.70 | 5.00 | - | 59 | 3.74s | OK |
| tool_with_reasoning | 6.03 | 5.00 | - | 50 | 2.44s | OK |
| no_tool_needed | 6.66 | 5.00 | - | 32 | 3.37s | OK |

<details><summary><code>single_tool_calendar</code> — score 6.62</summary>

**Stats**: latencia 3.25s · 42 tok/s · 630→138 tokens · $0.00036

**Respuesta (preview 300 chars)**:

```
<think>
El usuario quiere crear un evento en el calendario con los siguientes detalles:
- Título: 'Sprint Planning Q2'
- Fecha: 15 de mayo de 2026
- Hora: 10:00 AM
- Duración: 60 minutos

Voy a usar la función create_calendar_event con estos parámetros.
</think>
```

</details>

<details><summary><code>multi_tool_sequential</code> — score 6.70</summary>

**Stats**: latencia 3.74s · 59 tok/s · 656→221 tokens · $0.00046

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pide hacer dos cosas:
1. Crear una tarea urgente con título 'Revisar contrato cliente ABC' con fecha límite 2026-05-10
2. Enviar un email a legal@empresa.com con asunto 'Contrato ABC - Revision urgente' explicando que necesitan revisión antes del 10 de mayo

Voy a ejecutar amba
```

</details>

<details><summary><code>tool_with_reasoning</code> — score 6.03</summary>

**Stats**: latencia 2.44s · 50 tok/s · 630→122 tokens · $0.00034

**Respuesta (preview 300 chars)**:

```
<think>
El usuario necesita dos cosas:
1. Crear un recordatorio/tarea para hoy a las 5 PM para repasar slides
2. Buscar en la web mejores prácticas para presentaciones ejecutivas

Voy a ejecutar ambas tareas en paralelo ya que son independientes.
</think>
```

</details>

<details><summary><code>no_tool_needed</code> — score 6.66</summary>

**Stats**: latencia 3.37s · 32 tok/s · 599→106 tokens · $0.00031

**Respuesta (preview 300 chars)**:

```
<think>
El usuario me pregunta cuál es la capital de Francia. Esta es una pregunta de conocimiento general que no requiere ninguna herramienta. Francia es un país muy conocido y su capital es París.
</think>

La capital de Francia es **París**. 🇫🇷

París es una de las ciudades más emblemáticas del m
```

</details>
