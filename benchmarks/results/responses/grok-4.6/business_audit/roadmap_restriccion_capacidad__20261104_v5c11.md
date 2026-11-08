# Grok 4.6 — business_audit/roadmap_restriccion_capacidad

- model_id: `x-ai/grok-4.6`
- success: True  | final: 6.93 | quality: 8.0
- latency_total: 47.306s | tokens_per_second: 54.7
- input_tokens: 443 | output_tokens: 2587

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

**Este trimestre: solo B, luego D. A y C fuera.**

Capacidad real: 8 semanas × ~4 h/día. Eso son ~160 h (5 días/semana) o el equivalente a **4 semanas a tiempo completo**. No hay más. El soporte de 2 h/día ya está descontado y no se va a ir.

- **A** pide ~3 meses a tiempo completo. Con tu ritmo real tardarías el doble o más y no entregas nada usable este trimestre. Es un rewrite completo: alto riesgo, cero valor hasta que esté 100 % listo, y mientras tanto el producto actual sigue perdiendo gente. No cabe. Ni siquiera “empezar un poco”.
- **C** depende explícitamente de que A esté terminado. Bloqueado. Fuera.
- **B** es 1 semana TC → ~2 semanas de tu calendario. Alto impacto inmediato (estás tirando el 60 % en el paso 2).
- **D** es 2 semanas TC → ~4 semanas de tu calendario. Medio impacto, no bloqueado.

**Orden concreto**

1. Semanas 1-2: **B**. Arregla el flujo de alta. Mide conversión antes/después. Esto es lo único que puede mover el negocio ahora mismo y posiblemente reducir un poco el soporte futuro.
2. Semanas 3-6: **D**. Los 10 videos. Contenido sobre un producto que ya no pierde al 60 % de la gente en el onboarding.
3. Semanas 7-8: buffer. Revisa números de B, itera si hace falta, o más contenido. No empieces A.

Eso cabe con margen. Cualquier otra combinación (meter A, hacer C, o paralelizar) te deja el trimestre sin nada entregable y con el mismo agujero de conversión.

El rewrite (A) se discute el próximo trimestre, cuando tengas datos reales de B y sepas si el producto actual aguanta o no. Hasta entonces no existe.