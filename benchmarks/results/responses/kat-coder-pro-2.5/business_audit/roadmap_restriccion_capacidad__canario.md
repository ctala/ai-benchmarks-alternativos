# KAT Coder Pro v2.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 18.16s | tokens_per_second: 112.8
- input_tokens: 255 | output_tokens: 2048

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



## Diagnóstico de capacidad

- **Horas reales de construcción:** 4 h/día × 40 días = **160 horas disponibles**.
- **Carga total estimada de las 4 iniciativas:** ~9 semanas a tiempo completo = **~360 horas**.
- **Déficit:** Más del doble de lo que puedes hacer. No es un problema de priorización, es un problema de realidad.

---

## Orden recomendado (y qué descartar)

### 1. **B - Arreglar el flujo de alta** (Semanas 1-2)
**Prioridad máxima.** Es la única iniciativa que convierte tráfico existente en ingresos sin necesidad de más marketing. Recuperar哪怕 una fracción de ese 60% de abandono tiene ROI inmediato y libera caja para todo lo demás. Esfuerzo bajo, impacto alto, independiente.

### 2. **D - Grabar 10 videos** (Semanas 3-4)
Una vez el embudo funciona, tiene sentido alimentar la parte superior. El contenido es acumulativo y sigue trabajando mientras duermes. Esfuerzo acotado y no bloquea a nadie.

### 3. **C - Panel de métricas** (Semanas 5-7, **solo si se puede hacer sin A**)
Impacto medio, pero **depende de A según tu propio análisis**. Aquí tienes dos opciones:
- **Opción realista:** Haz una versión "cutre pero funcional" del panel que no requiera la reescritura. Datos en una tabla, gráficos simples. 3 semanas bien usadas si retiene clientes.
- **Opción honesta:** Si el panel *realmente* requiere la nueva arquitectura, **sácalo del trimestre**. No intentes hacer A para llegar a C.

### 4. **A - Reescribir la plataforma** (❌ Fuera del trimestre)
**No cabe.** 3 meses a tiempo completo = 12 semanas de tu capacidad actual. Intentarlo significa no entregar B, ni D, ni C, y llegar a fin de trimestre con una plataforma a medias y el flujo de alta sigue roto.

La reescritura es una **trampa de fundador técnico**: pospones valor inmediato por una promesa de eficiencia futura. Solo hazla cuando:
- El producto actual te esté frenando *diariamente* (no "sería más rápido", sino "no puedo implementar X").
- Tengas ayuda o hayas automatizado el soporte.
- Puedas migrar incrementalmente, no en un big-bang.

---

## Plan de 8 semanas

| Semana | Iniciativa | Entregable |
|--------|-----------|------------|
| 1-2 | **B** | Flujo de alta arreglado y medido |
| 3-4 | **D** | 10 videos publicados |
| 5-7 | **C (MVP)** o iteración en B/D | Panel básico o mejora de conversión |
| 8 | Buffer / métricas / planificación siguiente trimestre | Revisión de números |

---

## Lo que no estás viendo pero deberías

1. **Esas 2h de soporte son una mina de oro.** Estás hablando directamente con usuarios. ¿Qué te piden? ¿Dónde se atascan? Esa información vale más que cualquier panel de métricas. Úsala para