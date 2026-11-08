# GPT-5.6 Sol — business_audit/roadmap_restriccion_capacidad

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 11.108s | tokens_per_second: 91.8
- input_tokens: 241 | output_tokens: 1020

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

### Capacidad real del trimestre

- 4 h/día × 5 días × 8 semanas = **160 horas**
- Equivale a **4 semanas a tiempo completo**
- Conviene comprometer como máximo unas **120 horas** y dejar 40 para imprevistos, soporte extra y ajustes.

## Orden recomendado

### 1. B) Arreglar el flujo de alta
**Semanas 1–2 — ~40 h**

Es el mayor impacto inmediato y ataca una pérdida ya demostrada: 60% en un punto concreto. Antes de cambiarlo, asegura medición por paso; después, compara activación y conversión.

### 2. D) Grabar los 10 videos
**Semanas 3–6 — ~80 h**

Es la siguiente iniciativa independiente que cabe en el trimestre. Trabaja por lotes: guiones, grabación, edición y publicación. No consideres “terminado” solo grabarlos; incluye distribución.

### 3. Margen y optimización
**Semanas 7–8 — ~40 h**

Úsalas para:

- Corregir problemas descubiertos en el nuevo onboarding.
- Hacer una segunda iteración si la conversión no mejora.
- Publicar y distribuir los videos.
- Absorber desviaciones sin romper el trimestre.

## Lo que no haría

### A) Reescritura
**No empezar este trimestre.**

Tres meses a tiempo completo son unas 480 h. Con 20 h/semana para construir, supone aproximadamente **24 semanas**, no 8. Empezarla ahora consumiría todo el trimestre sin entregar valor y bloquearía otras mejoras.

Antes de aprobarla, conviértela en problemas concretos y busca mejoras incrementales. “Todo será más rápido en el futuro” no basta para justificar seis meses de calendario.

### C) Panel de métricas
**Fuera del trimestre.**

Aunque dura unas 120 h —seis semanas a tu capacidad— depende de A, que no cabe. No tiene sentido comprometerlo.

## Plan resumido

1. **B: onboarding**
2. **D: contenido**
3. **Iterar y absorber imprevistos**
4. **A y C: no comprometidos**

El objetivo del trimestre sería: **reducir de forma medible la fuga del alta y publicar 10 piezas de contenido**, no iniciar cuatro frentes.