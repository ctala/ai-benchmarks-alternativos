# Qwen 3.7 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.06 | quality: 10.0
- latency_total: 29.148s | tokens_per_second: 97.9
- input_tokens: 255 | output_tokens: 2855

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

Como jefe de producto que gestiona tu propia capacidad real (no la ideal), aquí tienes el orden y el plan de acción. Lo escribo con la crudeza que requiere un equipo de 1 persona: **no hay margen para apuestas de largo plazo ni dependencias bloqueantes en este trimestre.**

### 🔹 Orden prioritario
1. **B** (Arreglar flujo de alta)
2. **D** (Grabar 10 videos)
3. **C** (Panel de métricas) → *solo si se desacopla de A*
4. **A** (Reescritura completa) → *posponer al siguiente trimestre*

---

### 🔍 Por qué este orden (con tus números reales)
| Iniciativa | Esfuerzo real (considerando contexto switching + pruebas + bugs) | Impacto en 8 sem | Dependencia | Decisión |
|------------|---------------------------------------------------------------|------------------|-------------|----------|
| **B**      | ~20h (1 semana enfocada)                                      | Alto (retiene usuarios que ya llegan) | Ninguna     | ✅ Hacer primero |
| **D**      | ~40h (2 semanas, trabajo por lotes)                           | Medio (genera leads/autoridad)        | Ninguna     | ✅ Hacer segundo |
| **C**      | ~60h (3 semanas)                                              | Medio                                     | Depende de A | ⚠️ Solo si se construye sobre la栈 actual o se pospone |
| **A**      | ~480h+ (3 meses a tiempo completo)                            | Alto a futuro                             | Bloquea C   | ❌ Posponer. No cabe en 160h del trimestre |

**Tu capacidad real:** 4h/día × 5 días = 20h/semana × 8 semanas = **160 horas totales**.  
La reescritura (A) se come más del triple de ese presupuesto. Además, como fundador solo, cada cambio de stack implica rehacer integraciones, tests y soporte. Sin valor entregado al usuario hasta la semana 12+, estás apostando el trimestre a ciegas.

---

### 📅 Plan de 8 semanas (20h/semana)
| Semanas | Enfoque | Detalle operativo |
|---------|---------|-------------------|
| **1-2** | **B**   | 100% dedicado a identificar el punto de fuga en paso 2, parchearlo, lanzar y monitorizar conversión. No añadas features nuevas. |
| **3-4** | **D**   | Grabación en lote (1 video/día). Edición básica. Publicar según calendario. Deja 2h/semana para monitorear impacto de B. |
| **5-6** | **D** + iteración | Terminar videos restantes. Si B mejoró <15%, invertir horas en micro-ajustes UX (copy, carga, validación campo). |
| **7-8** | **Decisión crítica** | Evaluar datos. Si la栈 actual permite un panel de métricas mínimo (ej: tabla exportable + gráficos simples con librería ligera), hazlo. Si no, cierra el trimestre sin C. A queda en backlog técnico con límite de 2h/semana para investigación, no desarrollo. |

---

### 🛑 Reglas de ejecución para fundador solo
1. **Nunca empieces A si impide enviar B.** El flujo de alta es tu garganta. Si sangra, todo lo demás es ruido.
2. **Desacopla C de A.** Las dependencias son veneno cuando eres una sola persona. Si necesitas métricas, entrégalas con la tecnología actual aunque sea “imperfecta”. La iteración posterior será más barata que esperar a A.
3. **Buffer del 20%.** De esas 4h diarias, reserva 45 min improductivos por día (imprevistos, errores de producción, llamadas de soporte que se alargan). Tu plan debe caber en 16h/semana netas.
4. **Critério de salida para A:** Solo retomarlo si después de B+C+D sigues teniendo latencia >2s en respuestas críticas o costos de infraestructura que escalan linealmente con usuarios. Si no, migra módulos aislados en pequeños sprints, no todo el sistema.

---

### ✅ Resumen ejecutivo
- **Semana 1-2:** Cierra la fuga (B). Sin esto, el trimestre es irrelevante.
- **Semana 3-6:** Genera activo digital (D). Trabajo predecible, baja fricción cognitiva.
- **Semana 7-8:** Decide sobre métricas (C) con datos reales. A queda fuera del cierre de trimestre.
- **Regla de oro:** Como equipo de 1, tu ventaja no es velocidad bruta, es **ciclos de entrega cortos + feedback rápido**. Los proyectos que no muestran resultado en ≤3 semanas están matando tu capital de atención.

Si quieres, te ayudo a desglosar B en tareas de máximo 2h cada una para que no pierdas ritmo con el cambio de contexto.