# GPT-6.1 Sol — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-6.1-sol`
- success: True  | final: 8.46 | quality: 10.0
- latency_total: 15.804s | tokens_per_second: 50.6
- input_tokens: 241 | output_tokens: 800

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

**Este trimestre: B primero, D después y A/C fuera del compromiso.** No intentaría encajar las cuatro.

### Tu capacidad real

Asumiendo 5 días de trabajo por semana:

**8 semanas × 5 días × 4 h de construcción = 160 horas.**

Eso equivale a **4 semanas a tiempo completo**, no a 8. Las otras 2 h diarias ya están comprometidas con soporte y operación.

Si los esfuerzos que das están estimados a tiempo completo —40 h/semana—, el encaje es:

| Iniciativa | Horas estimadas | Duración con tu disponibilidad | Decisión |
|---|---:|---:|---|
| **B. Mejorar el alta** | 40 h | 2 semanas | **Primera prioridad** |
| **D. Crear 10 videos** | 80 h | 4 semanas | **Segunda, por lotes** |
| **A. Reescribir plataforma** | ~480 h | ~24 semanas | **No este trimestre** |
| **C. Panel de métricas** | 120 h | 6 semanas, después de A | **Bloqueado; fuera del trimestre** |

### Calendario de las 8 semanas

**Semanas 1–2: arreglar el alta — B**
- Verifica dónde y por qué se pierde ese 60%; no asumas que todo se arregla cambiando la interfaz.
- Corrige la principal fricción del paso 2 en la plataforma actual.
- Deja medido el avance del paso 2 y la finalización del alta.

**Entregable:** una mejora publicada y medible, no un rediseño completo.

**Semanas 3–6: contenido — D, con una puerta de decisión**
- Empieza con **2–3 videos**, publícalos y observa si atraen usuarios relevantes.
- Completa los 10 si los primeros justifican seguir.
- Mientras llegan datos del alta, revisa si la mejora funciona. Si sigue habiendo una fricción importante y corregible, priorízala sobre terminar los videos.

**Semanas 7–8: margen protegido — 40 h**
- Errores, ajustes del alta, imprevistos y medición de resultados.
- Si sobra capacidad, amplía lo que haya mostrado resultados. **No abras otra iniciativa grande por tener unos días libres.**

### Qué aparcaría explícitamente

**A: no empezarla “a ratos”.** Consume aproximadamente tres veces toda tu capacidad de construcción del trimestre. “Mejorará todo lo futuro” es una hipótesis, no suficiente justificación para dejar sin atender una fuga actual del 60%. Solo reconsideraría esta decisión si hay un problema crítico de seguridad, continuidad o mantenimiento.

**C: no comprometerla.** Con la dependencia que has indicado, no cabe. Para recuperarla más adelante, primero comprobaría si una versión pequeña puede hacerse sin A; no usaría el panel como excusa para iniciar la reescritura.

**Objetivo del trimestre:** reducir la fuga del alta y probar un canal de captación, dejando margen para operar. **Compromete B; planifica D de forma condicional; no comprometas A ni C.**