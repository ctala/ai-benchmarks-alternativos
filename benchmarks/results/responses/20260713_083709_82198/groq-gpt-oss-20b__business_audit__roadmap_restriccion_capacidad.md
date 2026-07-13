# GPT-OSS 20B (Groq) — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 5.37 | quality: 4.8
- latency_total: 20.37s | tokens_per_second: 78.3
- input_tokens: 305 | output_tokens: 1596

## Respuesta completa

### Resumen rápido  
- **Tienes 160 h de “build time”** (4 h/día × 5 días × 8 semanas).  
- **A** (re‑escritura completa) requiere 480 h → **no se puede completar** en el trimestre.  
- **C** depende de **A**, por lo que tampoco es viable.  

Con eso queda **B** y **D** como proyectos que sí puedes terminar dentro del plazo.  
El resto del tiempo lo puedes usar para mantener la plataforma, refactorizaciones pequeñas, documentación y cualquier mejora de bajo esfuerzo que te ayude a seguir creciendo.

---

## Calendario del trimestre (8 semanas)

| Semana | Actividad | Horas estimadas | Comentarios |
|--------|-----------|-----------------|-------------|
| **1** | **B – Arreglar flujo de alta** | 20 h | 1 semana completa a tiempo completo. Impacto alto, retención directa. |
| **2‑3** | **D – 10 videos de contenido** | 40 h | 2 semanas a tiempo completo. Impacto medio, marketing y generación de leads. |
| **4‑8** | **Tiempo de buffer / mejoras incrementales** | 100 h | 4 semanas restantes: <br>• Refactorizaciones leves (por ej. módulos críticos de A que puedas arrancar).<br>• Añadir pruebas unitarias y cobertura.<br>• Documentación de API y de uso.<br>• Pequeñas optimizaciones de rendimiento.<br>• Soporte de bugs que surjan.<br>• Planificación de la próxima sprint/iteración. |

> **Nota**: Si sientes urgencia por mover la plataforma a un nuevo framework, puedes destinar parte de la fase 4‑8 a un *punto crítico* de A (por ej. migrar la capa de base de datos o el sistema de autenticación). Deja claro que esto es **solo una fase de “proof‑of‑concept”**; la re‑escritura completa seguirá en backlog.

---

## Por qué este orden

| Proyecto | Prioridad | Motivo |
|----------|-----------|--------|
| **B** | #1 | El flujo de alta es la puerta de entrada. Mejorarlo aumenta inmediatamente la conversión y la satisfacción del cliente. |
| **D** | #2 | Los videos son contenido evergreen que seguirá generando valor mucho después del trimestre. |
| **A** | #3 | Demasiado esfuerzo para el plazo; se mantiene como “big‑ticket” en backlog. |
| **C** | #4 | Depende de A; se pospone a la siguiente fase donde A esté completo. |

---

## Checklist de seguimiento

1. **Antes de la semana 1**  
   - Confirma la disponibilidad de 4 h/día (incluye soporte).  
   - Prepara un *minimum viable* para el flujo de alta (wireframes, tests, métricas).  
   - Lista de los 10 videos: guion, guías de grabación, presupuesto de edición.

2. **Durante la ejecución**  
   - Usa un tablero Kanban con *“Ready”*, *“In‑Progress”*, *“Done”* y *“Blocked”*.  
   - Revisa semanalmente (30 min) el progreso y ajusta el buffer si surge un bug crítico.

3. **Al cerrar la fase 1‑3**  
   - Genera métricas de éxito (tasa de conversión, tiempo de carga, views de videos).  
   - Documenta lecciones aprendidas para la próxima fase (posible re‑escritura parcial de A).

---

### Resumen de prioridades

| Orden | Proyecto | Estado |
|-------|----------|--------|
| 1 | **B** | Completar (1 semana) |
| 2 | **D** | Completar (2 semanas) |
| 3 | **A** | Postergar (3 meses) |
| 4 | **C** | Postergar (depende de A) |
| 5 | **Buffer** | Optimizaciones, pruebas, documentación |

Con este plan, terminarás dos iniciativas de alto impacto, tendrás un sólido material de marketing y un conjunto de mejoras de calidad que te prepararán para el siguiente trimestre. ¡Éxito!