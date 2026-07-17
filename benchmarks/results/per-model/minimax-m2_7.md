# MiniMax M2.7 (directo)

- **model_id**: `MiniMax-M2.7`
- **Total tests**: 4/4 exitosos (0 errores)
- **Score final**: 6.61
- **Calidad**: 5.00
- **Velocidad**: 64 tok/s
- **Latencia primera token**: 2.63s
- **Costo promedio por test**: $0.00038

> Tests evaluados con Phi-4 (Microsoft, 14B, MIT) via Ollama local — scoring 30% auto + 70% juez.

## Resumen por suite

| Suite | Tests | OK | Score promedio | Calidad promedio |
|-------|-------|----|----|----|
| tool_calling | 4 | 4 | 6.61 | 5.00 |

## Detalle por test

### Agentes y Operaciones

#### tool_calling

| Test | Final | Calidad | Judge | tok/s | Latencia | Estado |
|------|-------|---------|-------|-------|----------|--------|
| single_tool_calendar | 6.90 | 5.00 | - | 85 | 1.86s | OK |
| multi_tool_sequential | 6.69 | 5.00 | - | 83 | 2.84s | OK |
| tool_with_reasoning | 5.86 | 5.00 | - | 37 | 4.04s | OK |
| no_tool_needed | 6.97 | 5.00 | - | 53 | 1.78s | OK |

<details><summary><code>single_tool_calendar</code> — score 6.90</summary>

**Stats**: latencia 1.86s · 85 tok/s · 642→158 tokens · $0.00038

**Respuesta (preview 300 chars)**:

```
<think>El usuario quiere agendar una reunión con los siguientes detalles:
- Título: 'Sprint Planning Q2'
- Fecha: 15 de mayo de 2026
- Hora: 10:00 AM
- Duración: 60 minutos

Voy a usar la función create_calendar_event con los parámetros proporcionados.
</think>
```

</details>

<details><summary><code>multi_tool_sequential</code> — score 6.69</summary>

**Stats**: latencia 2.84s · 83 tok/s · 668→236 tokens · $0.00048

**Respuesta (preview 300 chars)**:

```
<think>El usuario necesita que realice dos acciones:
1. Crear una tarea urgente con título 'Revisar contrato cliente ABC' y fecha límite 2026-05-10
2. Enviar un email a legal@empresa.com con asunto 'Contrato ABC - Revision urgente'

Ambas acciones son independientes entre sí, así que puedo ejecutarl
```

</details>

<details><summary><code>tool_with_reasoning</code> — score 5.86</summary>

**Stats**: latencia 4.04s · 37 tok/s · 647→148 tokens · $0.00037

**Respuesta (preview 300 chars)**:

```
<think>El usuario necesita:
1. Crear un recordatorio (tarea) para hoy a las 5 PM para repasar slides
2. Buscar en la web mejores prácticas para presentaciones ejecutivas

Voy a hacer ambas cosas en paralelo ya que son independientes.
</think>
```

</details>

<details><summary><code>no_tool_needed</code> — score 6.97</summary>

**Stats**: latencia 1.78s · 53 tok/s · 611→94 tokens · $0.00030

**Respuesta (preview 300 chars)**:

```
<think>El usuario me está preguntando cuál es la capital de Francia. Esta es una pregunta de conocimiento general muy básica que no requiere ninguna herramienta especial. La respuesta es simple: París.
</think>

La capital de Francia es **París**. Es una de las ciudades más famosas y visitadas del m
```

</details>
