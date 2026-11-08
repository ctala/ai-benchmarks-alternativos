# Kimi K2 — business_audit/roadmap_restriccion_capacidad

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 7.22 | quality: 8.0
- latency_total: 18.273s | tokens_per_second: 36.6
- input_tokens: 305 | output_tokens: 669

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

## Tu realidad en números

- **Capital disponible:** 4h/día × 5 días × 8 semanas = **160 horas de construcción**
- **Lo que pides:** ~21 semanas de trabajo (A=12s + B=1s + C=3s + D=2s, con C bloqueada por A)

---

## Orden de prioridad (cruel pero necesario)

### 1. **B) Arreglar el flujo de alta — Semana 1**
**40h de tu presupuesto**

Estás perdiendo 6 de cada 10 personas que intentan pagarte. Esto es sangrado activo. No importa qué construyas después si nadie llega vivo al final.

> *"Fix the leak before you paint the boat"*

---

### 2. **D) 10 videos de contenido — Semanas 2-3**
**80h restantes → 40h aquí**

Con el flujo arreglado, necesitas **más gente entrando** para validar que funciona. El contenido escala sin tu tiempo posterior. Es tu única palanca de crecimiento que no requiere código.

---

### 3. **A) Reescribir la plataforma — NO ESTE TRIMESTRE**

3 meses a tiempo completo = **~500h**. Tienes 80h. Ni siquiera empieces.

La excusa de "velocidad futura" es una trampa clásica de fundadores solos. Tu velocidad actual está limitada por **tus 4h, no por el framework**.

---

### 4. **C) Panel de métricas — NO ESTE TRIMESTRE**

Depende de A, y A no va. Además: ¿tus clientes *realmente* lo piden, o es tu ansiedad de "parecer profesional"?

---

## Tu trimestre real

| Semana | Qué haces | Horas |
|--------|-----------|-------|
| 1 | B (fix onboarding) | 40h |
| 2-3 | D (contenido) | 40h |
| 4-8 | **Buffer crítico** | 80h |

Ese buffer es sagrado. Será para: bugs de B, iteración de D, o la inevitable "emergencia" que aparece.

---

## La pregunta incómoda

¿Por qué A está en tu lista? 

Si la respuesta es "el código actual me da vergüenza" — eso es ego, no estrategia. Si es "no puedo implementar X" — ¿cuál es X específicamente? A veces hay atajos de 2 semanas en lugar de reescrituras de 3 meses.

¿Hay algo que crees que **solo** es posible con el nuevo framework? Puede que haya una versión mínima viable de eso en el actual.