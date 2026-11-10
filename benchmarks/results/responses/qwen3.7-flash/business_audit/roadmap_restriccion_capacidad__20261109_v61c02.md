# Qwen 3.7 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.05 | quality: 10.0
- latency_total: 43.264s | tokens_per_second: 72.0
- input_tokens: 255 | output_tokens: 3115

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

Aquí tienes el orden y la planificación basada estrictamente en tu capacidad real, no en la ideal:

### 📊 Orden recomendado para el trimestre
**1. B → 2. D → 3. C (solo si se desvincula de A) → 4. A (cancelado/reprogramado)**

---

### 🔍 Análisis por iniciativa (con matemáticas reales)

| Iniciativa | Impacto | Esfuerzo estimado | Horas reales con tu ritmo (4h/día) | Veredicto |
|------------|---------|-------------------|-----------------------------------|-----------|
| **B) Arreglar alta** | Alto | ~1 semana | ~15-20h | ✅ **Hacerlo primero** |
| **D) 10 videos** | Medio | ~2 semanas | ~25-30h | ✅ **Hacerlo segundo** |
| **C) Panel métricas** | Medio | ~3 semanas | ~40-45h | ⚠️ **Posponer o reescalar** (depende de A) |
| **A) Reescribir plataforma** | Alto | ~3 meses TC | ~120-130h+ | ❌ **Cancelar para este trimestre** |

**Matemática de capacidad:**  
8 semanas × 5 días = 40 días laborables.  
4h/día × 40 = **160h brutas**. Restando cambios de contexto, pruebas y margen de error realista, operas con **~120h seguras**.  
B + D consumen ~45-50h. Te sobra holgura para ajustes, documentación o preparar el siguiente trimestre.

---

### 🗓️ Planificación semana a semana

**Semanas 1-2: Solo B**  
- Enfócate exclusivamente en identificar el cuello de botella en el paso 2, prototipar la solución, desplegar y medir conversión.  
- No hagas nada más hasta que veas datos post-lanzamiento (aunque sean 48h). El 60% de fuga suele ser un error de UX, validación o carga, no arquitectura.

**Semanas 3-5: Solo D**  
- Graba los 10 videos en 1-2 bloques intensivos. Usa edición asistida por IA o plantillas. Publica con frecuencia constante.  
- Al ser contenido, no compite por foco técnico. Puedes alternarlo con mantenimiento menor de B.

**Semanas 6-8: Evaluación + decisión sobre C/A**  
- Analiza métricas post-B. Si la conversión subió >15%, prioriza retención o upsell en lugar de rewrite.  
- Sobre **C**: Si depende estructuralmente del rewrite, cáncelo para este trimestre. Si solo necesita acceso a datos existentes, escópele como MVP sin dependencias técnicas pesadas (ej. tabla SQL + vista básica).  
- Sobre **A**: Un rewrite a mitad de tracción con equipo de 1 persona suele generar deuda técnica nueva, bugs de regresión y cero entrega de valor al cliente. Redúcelo a: *“optimizar queries lentas + parches de rendimiento”* o muévelo al Q2 solo si el tráfico lo justifica.

---

### 🛡️ Reglas de ejecución para tu realidad

1. **Protege las 4h como un contrato legal.** Bloqueos inquebrantables, notificaciones apagadas, sin Slack/email dentro de esas horas.
2. **No mezcles contexto.** Cambiar de código → videos → soporte cada día te cuesta ~20-30% de productividad por reconexión mental. Agrupa tareas por tipo.
3. **Desacopla dependencias artificiales.** Si C dice “necesita A”, pregunta: ¿qué exactamente? A menudo se puede entregar un 20% del valor con el 5% del esfuerzo actual.
4. **Mide antes de ampliar.** Tras arreglar B, espera 7-10 días de datos reales. Si la mejora es <10%, vuelve a diagnosticar. Si es >15%, considera que el problema ya no es la plataforma, sino distribución o pricing.
5. **Soporte ≠ operación delegable aún, pero sí reducible.** Documenta las 10 respuestas repetidas, crea macros, templates o un flujo automático básico. Cada minuto ahorrado aquí suma a tus 4h.

---

### ✅ Resultado esperado al cerrar el trimestre
- Fuga en alta reducida a <20% (impacto directo en crecimiento orgánico y CAC).
- Catálogo de 10 videos activos generando tráfico/autoridad.
- Plataforma estable, sin rewrite ni deuda técnica nueva.
- Métricas claras para decidir si C merece espacio en el próximo trimestre.

Si quieres, puedo ayudarte a desglosar B en un checklist de 5 pasos técnicos/UX para que lo ejecutes en 5 días sin distraerte.