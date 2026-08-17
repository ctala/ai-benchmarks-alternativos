# Ling 3.0 Flash — structured_output/json_nested_complex

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 5.9 | quality: 5.0
- latency_total: 5.204s | tokens_per_second: 394.9
- input_tokens: 268 | output_tokens: 2055
- judge_score: 5 | justificación: La respuesta es precisa, relevante, clara y útil, con un formato JSON correcto y bien estructurado.

## Respuesta completa

```json
{
  "project": "Rediseno sitio web",
  "start_date": "2026-05-01",
  "end_date": "2026-06-30",
  "team": [
    {"name": "Ana García", "role": "Diseñadora UX/UI", "allocation_pct": 100},
    {"name": "Carlos López", "role": "Desarrollador Frontend", "allocation_pct": 100},
    {"name": "María Rodríguez", "role": "Desarrolladora Backend", "allocation_pct": 100},
    {"name": "Pedro Sánchez", "role": "Ingeniero QA", "allocation_pct": 80}
  ],
  "phases": [
    {
      "name": "Descubrimiento y Diseño",
      "start": "2026-05-01",
      "end": "2026-05-15",
      "tasks": [
        {"title": "Relevamiento de requisitos con stakeholders", "assignee": "Ana García", "hours": 16, "depends_on": null},
        {"title": "Auditoría de sitio actual y análisis de competencia", "assignee": "Ana García", "hours": 12, "depends_on": 1},
        {"title": "Wireframes de páginas clave", "assignee": "Ana García", "hours": 20, "depends_on": 2},
        {"title": "Diseño de interfaz (UI) en Figma", "assignee": "Ana García", "hours": 24, "depends_on": 3},
        {"title": "Prototipo interactivo y revisión con cliente", "assignee": "Ana García", "hours": 12, "depends_on": 4},
        {"title": "Ajustes finales de diseño", "assignee": "Ana García", "hours": 8, "depends_on": 5},
        {"title": "Definición de arquitectura técnica", "assignee": "Carlos López", "hours": 12, "depends_on": 1},
        {"title": "Selección de stack tecnológico", "assignee": "María Rodríguez", "hours": 8, "depends_on": 7}
      ]
    },
    {
      "name": "Desarrollo",
      "start": "2026-05-16",
      "end": "2026-06-10",
      "tasks": [
        {"title": "Configuración de repositorio y entorno de desarrollo", "assignee": "Carlos López", "hours": 8, "depends_on": null},
        {"title": "Desarrollo de componentes de UI (Frontend)", "assignee": "Carlos López", "hours": 40, "depends_on": 1},
        {"title": "Implementación de layouts responsivos", "assignee": "Carlos López", "hours": 24, "depends_on": 2},
        {"title": "Integración de API y endpoints REST", "assignee": "María Rodríguez", "hours": 32, "depends_on": null},
        {"title": "Modelado y migración de base de datos", "assignee": "María Rodríguez", "hours": 20, "depends_on": 4},
        {"title": "Implementación de autenticación y seguridad", "assignee": "María Rodríguez", "hours": 16, "depends_on": 5},
        {"title": "Integración frontend-backend", "assignee": "Carlos López", "hours": 16, "depends_on": 3},
        {"title": "Integración de servicios de terceros (email, analytics)", "assignee": "María Rodríguez", "hours": 12, "depends_on": 6}
      ]
    },
    {
      "name": "Testing y QA",
      "start": "2026-06-11",
      "end": "2026-06-25",
      "tasks": [
        {"title": "Pruebas funcionales end-to-end", "assignee": "Pedro Sánchez", "hours": 20, "depends_on": null},
        {"title": "Pruebas de compatibilidad cross-browser", "assignee": "Pedro Sánchez", "hours": 12, "depends_on": 1},
        {"title": "Pruebas de rendimiento y carga", "assignee": "Pedro Sánchez", "hours": 10, "depends_on": 2},
        {"title": "Pruebas de accesibilidad (WCAG)", "assignee": "Pedro Sánchez", "hours": 8, "depends_on": 3},
        {"title": "Reporte y registro de bugs", "assignee": "Pedro Sánchez", "hours": 8, "depends_on": 4},
        {"title": "Corrección de bugs críticos (devs)", "assignee": "Carlos López", "hours": 12, "depends_on": 5},
        {"title": "Corrección de bugs críticos (backend)", "assignee": "María Rodríguez", "hours": 10, "depends_on": 5},
        {"title": "Pruebas de regresión final", "assignee": "Pedro Sánchez", "hours": 8, "depends_on": 6}
      ]
    },
    {
      "name": "Despliegue y Lanzamiento",
      "start": "2026-06-26",
      "end": "2026-06-30",
      "tasks": [
        {"title": "Configuración de entorno de producción", "assignee": "María Rodríguez", "hours": 8, "depends_on": null},
        {"title": "Despliegue final y migración de datos", "assignee": "María Rodríguez", "hours": 8, "depends_on": 1},
        {"title": "Verificación post-despliegue", "assignee": "Pedro Sánchez", "hours": 6, "depends_on": 2},
        {"title": "Capacitación al equipo de contenido", "assignee": "Carlos López", "hours": 6, "depends_on": 3},
        {"title": "Lanzamiento oficial y monitoreo", "assignee": "Carlos López", "hours": 4, "depends_on": 4}
      ]
    }
  ],
  "budget": {
    "total": 25000,
    "breakdown": {
      "design": 5000,
      "development": 15000,
      "testing": 5000
    }
  }
}
```