# Nemotron 3 Super — business_audit/roadmap_restriccion_capacidad

- model_id: `nvidia/nemotron-3-super-120b-a12b`
- success: True  | final: 7.44 | quality: 8.0
- latency_total: 33.143s | tokens_per_second: 89.1
- input_tokens: 266 | output_tokens: 2953

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres jefe de producto de una empresa de una sola persona. Priorizas con la capacidad real del equipo, no con la ideal.

**user:**

Soy fundador solo. Tengo 6 horas al día de trabajo enfocado y ya gasto 2 de esas 6 en soporte y operación diaria que no puedo delegar todavía. Me quedan ~4h/día reales para construir. Quedan 8 semanas hasta el cierre del trimestre.

Tengo cuatro iniciativas y quiero saber qué hago:

A) Reescribir la plataforma en otro framework. Impacto estimado: alto (velocidad y todo lo futuro). Esfuerzo: ~3 meses a tiempo completo.
B) Arreglar el flujo de alta, que hoy pierde al 60% de la gente en el paso 2. Impacto: alto. Esfuerzo: ~1 semana.
C) Añadir un panel de métricas para mis clientes. Impacto: medio. Esfuerzo: ~3 semanas. Depende de que A esté terminado.
D) Grabar 10 videos de contenido. Impacto: medio. Esfuerzo: ~2 semanas.

Ordename el trimestre.


## Respuesta completa

**Resumen de recursos disponibles**

| Concepto | Valor |
|----------|-------|
| Jornadas de trabajo enfocado por día | 4 h |
| Días laborables por semana | 5 |
| Horas disponibles por semana | 4 h × 5 = 20 h |
| Semanas hasta el cierre del trimestre | 8 |
| **Horas totales disponibles** | 20 h × 8 = **160 h** |

**Esfuerzo estimado (en horas)**  

| Iniciativa | Esfuerzo (full‑time) | Horas aproximadas* |
|------------|----------------------|--------------------|
| A) Reescribir plataforma | 3 meses ≈ 12 sem FT | 12 sem × 40 h = **≈ 480 h** |
| B) Arreglar flujo de alta | 1 semana | 5 d × 4 h = **20 h** |
| C) Panel de métricas | 3 semanas (depende de A) | 3 sem × 20 h = **60 h** |
| D) 10 videos de contenido | 2 semanas | 2 sem × 20 h = **40 h** |

\*Se asume que tu tiempo productivo es 4 h/día (20 h/semana).  

**Conclusión rápida**  
- **A** no cabe en el trimestre si lo intentas terminar de una vez (necesitarías ~480 h y solo tienes 160 h).  
- **B** y **D** son de alto/medio impacto y bajo esfuerzo; se pueden hacer completo.  
- **C** depende de **A**, así que no puede iniciarse hasta que tengas al menos una versión usable de la nueva plataforma.  
- La mejor estrategia es **hacer B y D primero**, y **usar el tiempo restante para avanzar lo máximo posible en A** (de forma incremental), dejando **C** para el próximo trimestre cuando la base esté lista.

---

## Plan trimestral (semana a semana)

| Semana | Horas disponibles | Actividad principal | Detalle de la tarea | Horas usadas | Comentario / Estado al final |
|--------|-------------------|---------------------|---------------------|--------------|------------------------------|
| **1** | 20 h | **B** – Arreglar flujo de alta | - Diagnóstico del paso 2 (2 h) <br> - Rediseño y corrección (12 h) <br> - Tests y despliegue (4 h) <br> - Documentación breve (2 h) | 20 h | Flujo de alta recuperado (se espera subir conversión del 40 % al ~80 %). |
| **2‑3** | 40 h | **D** – 10 videos de contenido | - Guion y storyboard (4 h) <br> - Grabación (20 h) <br> - Edición ligera (12 h) <br> - Publicación y SEO básico (4 h) | 40 h | Biblioteca de videos lista; se pueden usar en onboarding, marketing y soporte. |
| **4‑8** | 100 h | **A** – Reescritura incremental de la plataforma | **Objetivo:** entregar un *core* funcional en el nuevo framework que permita iniciar el panel de métricas (C) en el próximo trimestre. <br> **Semana 4** – Spike de arquitectura (8 h) + setup del repositorio y CI/CD (12 h). <br> **Semana 5** – Módulo de autenticación y usuarios (20 h). <br> **Semana 6** – Módulo de facturación / suscripciones (20 h). <br> **Semana 7** – API pública y endpoints críticos (20 h). <br> **Semana 8** – Tests de integración, documentación de migración y plan de corte a producción (20 h). | 100 h (20 h/semana) | No se logra la reescritura completa, pero se tiene una base estable (auth, facturación y API) que permite: <br> • Ejecutar pruebas de carga y validar mejoras de velocidad. <br> • Empezar a trabajar en el panel de métricas (C) en el siguiente trimestre. <br> • Reducir el riesgo de un “big‑bang” al poder hacer un despliegue por fases (feature‑flag o strangler‑fig). |
| **Post‑trimestre** | — | **C** – Panel de métricas | Se iniciará cuando el core de A esté lo suficientemente estable (al menos auth + API). Se estima 3 semanas FT (≈ 60 h) → 3 semanas de tu tiempo productivo (≈ 15 días). | — | Queda para el próximo trimestre. |

### Por qué este orden es óptimo

| Criterio | A | B | C | D |
|----------|---|---|---|---|
| **Impacto** | Alto (futuro) | Alto (inmediato) | Medio (depende de A) | Medio (marketing/educación) |
| **Esfuerzo** | Muy alto (no cabe) | Muy bajo | Medio (pero bloqueado por A) | Bajo |
| **Dependencia** | Ninguna | Ninguna | **Depende de A** | Ninguna |
| **Valor esperado por hora** | Bajo (porque no se termina) | **Muy alto** | Medio (solo después de A) | Medio‑alto |
| **Riesgo** | Alto (big‑bang, posible retraso) | Bajo | Medio (depende de entrega de A) | Bajo |

1. **B** se hace primero porque entrega el mayor retorno inmediato con el menor coste.  
2. **D** sigue porque también es rápido, independiente y genera contenido que puede aprovecharse inmediatamente (mejora de adquisición y reducción de tickets de soporte).  
3. **A** se aborda en bloques de 20 h/semana (tu capacidad productiva). Al trabajar de forma incremental y enfocarse en los módulos más críticos (auth, facturación, API) se consigue: <br>‑ Un avance medible que justifica la inversión de tiempo. <br>‑ La base técnica necesaria para iniciar **C** en el próximo trimestre. <br>‑ La posibilidad de ir desplegando por partes (feature‑flag o strangler‑fig) y así mitigar el riesgo de un lanzamiento fallido.  
4. **C** se pospone porque, sin una plataforma estable en el nuevo framework, cualquier esfuerzo en el panel de métricas sería propenso a re‑trabajo y a generar deuda técnica. Cuando el núcleo de A esté listo, el panel podrá construirse en un tiempo razonable y con pleno beneficio.

---

## Qué hacer si surge algún imprevisto

| Situación | Acción recomendada |
|-----------|--------------------|
| **Un bug crítico en producción consume más de 2 h/día de soporte** | Reduce temporalmente el tiempo dedicado a A (por ejemplo, a 10 h/semana) y recupera esas horas en la siguiente semana si el soporte se estabiliza. |
| **Los videos de D toman más tiempo de lo esperado (por edición o guiones)** | Prioriza los videos que tengan mayor impacto (por ejemplo, los 5 primeros) y deja los restantes para el próximo trimestre; el tiempo sobrante se puede volver a destinar a A. |
| **Descubres que el nuevo framework no es tan veloz como esperabas** | Después de la semana 4 (spike) evalúa si continuar con el cambio o si un *refactor incremental* del framework actual sería suficiente. Si decides cambiar de dirección, re‑asigna las horas restantes de A a mejoras de rendimiento en el stack actual (todavía de alto impacto). |
| **Un cliente solicita urgentemente una funcionalidad que depende del panel de métricas** | Evalúa si se puede entregar un “MVP” muy ligero del panel usando la versión actual (aunque sea menos ideal) y posponer la versión completa al próximo trimestre; de esta forma no detienes el flujo de ingresos. |

---

### Tabla de resumen rápido (horas acumuladas)

| Semana | B | D | A (acumulado) | Total usado | Horas restantes |
|--------|---|---|---------------|------------|-----------------|
| 1 | 20 | 0 | 0 | 20 | 140 |
| 2 | 20 | 20 | 0 | 40 | 120 |
| 3 | 20 | 40 | 0 | 60 | 100 |
| 4 | 20 | 40 | 20 | 80 | 80 |
| 5 | 20 | 40 | 40 | 100 | 60 |
| 6 | 20 | 40 | 60 | 120 | 40 |
| 7 | 20 | 40 | 80 | 140 | 20 |
| 8 | 20 | 40 | 100 | 160 | 0 |

Al final del trimestre habrás:

- **Recuperado** gran parte del flujo de alta (B).  
- **Generado** una biblioteca de 10 videos de valor medio‑alto (D).  
- **Avanzado** significativamente en la reescritura (A) con los componentes críticos listos para comenzar el panel de métricas (C) en el siguiente trimestre.  
- **Dejado** C para cuando la base técnica esté preparada, evitando trabajo desperdiciado y riesgos de integración.

¡Éxitos en la ejecución! Si necesitas una plantilla de seguimiento (tipo Kanban o burndown) para visualizar este plan, avísame y te la preparo. 🚀