# GPT-6.1 Sol — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 7.03 | quality: 8.0
- latency_total: 17.568s | tokens_per_second: 51.3
- input_tokens: 241 | output_tokens: 902

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

**Este trimestre: B primero, D después en lotes pequeños. A y C quedan fuera.** No intentaría encajar las cuatro.

### Tu capacidad real

Asumiendo 5 días de trabajo por semana:

- **Construcción:** 4 h/día × 5 días × 8 semanas = **160 horas**.
- Reservaría **40 horas de margen** para imprevistos, correcciones y picos de soporte.
- Comprometería **120 horas**, no las 160.

Para hacer comparables los esfuerzos, asumo que “una semana” significa 40 horas. Si tus estimaciones ya eran a 4 h/día, el calendario se acorta; **el orden no cambia**.

### Prioridad

| Iniciativa | Decisión | Motivo |
|---|---|---|
| **B. Arreglar el alta** | **Primera** | Impacto alto, esfuerzo acotado y una fuga concreta que puedes medir. |
| **D. Grabar contenido** | **Segunda, por lotes** | Cabe después de B y no tiene dependencias. Pero diez videos no deben ser un compromiso ciego. |
| **A. Reescribir plataforma** | **Fuera del trimestre** | Tres meses a tiempo completo equivalen aproximadamente a seis meses con tu capacidad de construcción. No cabe ni trabajando sin margen. |
| **C. Panel de métricas** | **Bloqueada; fuera del trimestre** | Depende de A. No es una opción ejecutable este trimestre tal como está definida. |

### Calendario de las 8 semanas

**Semanas 1–2: B — arreglar el alta, unas 40 h**
- Verificar que la caída del paso 2 esté bien medida.
- Identificar la causa y entregar el cambio más pequeño que la ataque.
- Medir conversión antes y después, y comprobar que los nuevos usuarios llegan a activarse.

**Criterio de cierre:** mejora observable del flujo, no rediseño completo del onboarding.

**Semanas 3–6: D — contenido, hasta 80 h**
- Primero prepara, graba y publica **2–3 videos**.
- Incluye distribución y medición en el esfuerzo: grabarlos sin conseguir que lleguen a alguien no completa el trabajo.
- Continúa hacia los diez si el proceso es sostenible y aparecen señales útiles —visitas cualificadas, altas o conversaciones comerciales—. Si no, ajusta antes de producir el resto.

**Semanas 7–8: margen, medición y consolidación — 40 h**
- Absorber retrasos e incidencias.
- Corregir lo aprendido del alta.
- Evaluar resultados y decidir el siguiente trimestre.

Ese margen **no es capacidad libre para empezar A o C**.

### Qué haría con A y C mientras tanto

- **A:** pediría evidencia concreta de qué bloquea el framework actual. “Mejorará todo lo futuro” no basta para justificar meses sin entregar valor. Si hay un bloqueo real, buscaría una intervención localizada antes que una reescritura.
- **C:** validaría la necesidad en conversaciones de clientes que ya tengas. Si existe demanda fuerte, comprobaría si una versión mínima puede funcionar sin A; no la metería en este trimestre sin retirar otra cosa.

**Objetivo del trimestre:** recuperar usuarios que hoy pierdes en el alta y probar un canal de adquisición, sin comprometerte a una migración que no puedes terminar.