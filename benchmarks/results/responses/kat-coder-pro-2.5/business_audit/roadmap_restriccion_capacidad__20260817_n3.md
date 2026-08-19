# KAT Coder Pro v2.5 — business_audit/roadmap_restriccion_capacidad

- model_id: `kwaipilot/kat-coder-pro-v2.5`
- success: True  | final: 8.61 | quality: 10.0
- latency_total: 19.361s | tokens_per_second: 63.1
- input_tokens: 255 | output_tokens: 1222

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



**Veredicto directo: Solo B y D entran este trimestre. A y C se quedan fuera.**

Aquí está el porqué, sin adornos:

---

### Tu capacidad real del trimestre

| | Horas disponibles |
|---|---|
| 4h/día × 5 días × 8 semanas | **~160 horas de construcción** |

| Iniciativa | Horas necesarias | ¿Cabe? |
|---|---|---|
| A | ~480h (3 meses full-time) | ❌ Imposible. Es el triple de tu capacidad total. |
| B | ~40h | ✅ |
| C | ~120h + depende de A | ❌ Bloqueada |
| D | ~80h | ✅ |

---

### El orden que ejecuto

**Semanas 1-2 → B (Arreglar el alta)**

Esto es lo único no negociable. Estás perdiendo al 60% de la gente en el paso 2. Cada día que pasa sin arreglarlo es revenue que se escapa y usuarios que nunca vuelven. Es el ROI más alto de toda la lista: 1 semana de esfuerzo, impacto inmediato en conversión, y no depende de nada.

**Semanas 3-5 → D (Videos de contenido)**

Una vez que el embudo no gotea, tiene sentido atraer más gente. 10 videos en 2-3 semanas es realista con tu ritmo.

**Semanas 6-8 → Iteración, descubrimiento y deuda pequeña**

Te sobran ~5 semanas. No las llenes con A. Úsalas para:
- Medir si B funcionó y iterar sobre el flujo de alta.
- Hablar con usuarios (esto siempre debería ser tiempo protegido).
- Arreglar bugs y fricciones pequeñas que vayan saliendo.
- Si sobra energía, avanzar en C de forma desbloqueada (¿realmente necesita A terminado, o puedes hacer un panel básico sin reescribir?).

---

### Lo que NO haces este trimestre

**A (Reescribir)** — La trampa clásica del fundador técnico. Suena a "inversión en el futuro", pero en la práctica es un agujero de 6 meses donde no shippeas nada. Si el stack actual te permite hacer B y D, no es el cuello de botella. Posponlo hasta que tengas evidencia concreta de que la tecnología actual impide algo que sí importa.

**C (Panel de métricas)** — Muerto por dependencia. Si C depende de A y A no existe, C tampoco. Si puedes desbloquearlo (hacer un panel simple sin reescribir), reconsideralo para el próximo trimestre.

---

### Una pregunta que deberías hacerte

¿Por qué A está en la lista? ¿Es una necesidad real o es postergación disfrazada de productividad? Reescribir se siente como construir, pero a menudo es evitar hablar con usuarios o tomar decisiones difíciles sobre el producto actual.

**Resumen en una línea:** Arregla la fuga (B), luego alimenta el embudo (D), y deja de perseguir la reescritura perfecta (A) hasta que el negocio actual te lo exija con datos.