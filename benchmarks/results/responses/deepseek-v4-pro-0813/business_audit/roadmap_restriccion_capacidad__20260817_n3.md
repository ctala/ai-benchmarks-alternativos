# DeepSeek V4 Pro (0813) — business_audit/roadmap_restriccion_capacidad

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 50.002s | tokens_per_second: 47.4
- input_tokens: 343 | output_tokens: 2368

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

Como jefe de producto unipersonal, lo primero es aterrizar la capacidad real y descartar lo que no cabe.

**Capacidad real del trimestre**
- 4 h/día reales para construir.
- 8 semanas × 5 días laborables = 40 días.
- Total disponible: **160 horas**.

**Esfuerzo convertido a tu capacidad real**
- **A) Reescribir plataforma:** ~3 meses a tiempo completo ≈ 480 h.  
  Con tus 4 h/día reales, te tomaría ~24 semanas. **No cabe en el trimestre.**
- **B) Arreglar flujo de alta:** ~1 semana ≈ 40 h → **2 semanas calendario** para ti.  
  Cabe perfectamente.
- **C) Panel de métricas:** ~3 semanas ≈ 120 h → **6 semanas calendario** para ti.  
  Además depende de A terminado, por lo que queda bloqueada.
- **D) 10 videos de contenido:** ~2 semanas ≈ 80 h → **4 semanas calendario** para ti.  
  Cabe perfectamente.

**Lo que haría en tu lugar**

### Orden del trimestre

1. **Semanas 1-2 — Iniciativa B: arreglar el flujo de alta.**  
   Es el único “quick win” claro: impacto alto, esfuerzo bajo y ataca directamente una pérdida del 60% en el paso 2.  
   Entrégalo primero, mide conversión y asegura que el funnel mejora. No toques nada más durante estas dos semanas.

2. **Semanas 3-6 — Iniciativa D: grabar 10 videos de contenido.**  
   Impacto medio, esfuerzo medio y no depende de A.  
   Te da material reutilizable para adquisición, soporte y educación de clientes. Puedes grabar en lotes para no romper el ritmo.

3. **Semanas 7-8 — Buffer + iteración o preparación.**  
   Guarda ~40 h para imprevistos, ajustes de B según datos reales, edición/ publicación de D, o para preparar el siguiente trimestre.  
   No comprometas estas horas con una iniciativa nueva grande.

### Lo que NO haría

- **No reescribir la plataforma (A) ahora.**  
  Es un proyecto de ~6 meses con tu capacidad real. Meterlo en 8 semanas solo te dejaría a medias, con deuda técnica nueva y sin impacto visible.
- **No intentar C este trimestre.**  
  Aunque fuera valioso, depende de A y A no se va a completar. Si quieres avanzar en C, primero valida si se puede hacer una versión mínima sin reescribir todo, pero no a costa de B o D.

### Resumen visual

| Iniciativa | Esfuerzo real | Semanas calendario | ¿Se hace? |
|---|---|---|---|
| A | 480 h | 24 semanas | No |
| B | 40 h | 2 semanas | Sí |
| C | 120 h | 6 semanas | No (bloqueada por A) |
| D | 80 h | 4 semanas | Sí |
| Buffer | 40 h | 2 semanas | Sí |

**Prioridad del trimestre: B → D → buffer.**  
Enfócate en resultados visibles y medibles. La reescritura puede esperar.