# Ling 3.0 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 67.53s | tokens_per_second: 31.8
- input_tokens: 303 | output_tokens: 2145

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

## Tu trimestre, ordenado con honestidad

### Tu capacidad real: 160h de construcción (4h/día × 20 días hábiles)

---

### 🔴 Primero: B — Arreglar el flujo de alta (Semana 1)

**Por qué primero y sin discusión:** Estás perdiendo al 60% de la gente que ya te llega. Todo lo demás que construyas en el trimestre — contenido, paneles, reescritura — se lo come ese agujero. Arreglar el balde tiene más impacto que llenarlo.

- Esfuerzo: ~1 semana (~20h)
- Resultado: dejas de regalar >60% de tus leads
- **Si haces nada más este trimestre, haz esto**

---

### 🟡 Segundo: D — Grabar los 10 videos (Semanas 2-3)

**Por qué segundo:** Genera tráfico y prospectos. Pero solo tiene sentido *después* de que B esté arreglado, porque si gravas tráfico y tu web lo convierte al 40%, estás tirando dinero.

- Esfuerzo: ~2 semanas (~40h)
- Resultado: canal de adquisición activo para el próximo trimestre

---

### 🟢 Tercero: Semanas 4-8 — Lo que sobre (~5 semanas libres)

Aquí está la pregunta honesta. **No empieces A.** 3 meses a tiempo completo = ~240h. No cabes ni terminas. Empezar y abandonar a medias es peor que no empezar.

Usa esas 5 semanas así:

| Bloque | Qué hacer | Por qué |
|---|---|---|
| **Semanas 4-5** | Iterar y medir el fix de B. Testear variantes del paso 2. | Un fix sin optimización es dejar dinero sobre la mesa. |
| **Semana 6** | Preparar C sin tocar A. Diseñar las métricas, definir qué mostrar, hacer las queries sobre la base actual, bocetar el UI. | Cuando A termine (próximo trimestre), C arranca en días, no semanas. |
| **Semanas 7-8** | Terminar lo que sobre de D (distribuir los videos, responder comentarios, iterar). Y/o arrancar la documentación/plan de A para el próximo trimestre. | Aterrizar lo publicado. Preparar el siguiente trimestre. |

---

### ❌ Lo que NO haces este trimestre

**A (reescribir plataforma):** No cabe. No lo empieces. Planifícalo para el Q siguiente con un desglose real. Un framework nuevo no se rescata a medias.

**C (panel de métricas):** Bloqueado por A. Pero sí haces el trabajo preparatorio (diseño + definición + queries) para que sea un proyecto de 1 semana cuando A termine.

---

### Resumen visual del trimestre

```
Semana 1:  [B] ████████████████████
Semana 2:  [D] ████████████████████
Semana 3:  [D] ████████████████████
Semana 4:  [B+] ████████████████████  (optimizar el fix)
Semana 5:  [B+] ████████████████████  (optimizar el fix)
Semana 6:  [C-prep] ████████████████████  (diseño + queries, sin A)
Semana 7:  [D-distrib] ████████████████████
Semana 8:  [A-prep] ████████████████████  (planificar A para Q next)
```

**Regla que te puedes repetir:** *No pierdas lo que ya tengo arreglando lo que quiero tener.*