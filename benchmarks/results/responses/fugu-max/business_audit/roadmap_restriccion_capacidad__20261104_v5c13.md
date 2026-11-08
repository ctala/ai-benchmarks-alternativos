# Fugu Max — business_audit/roadmap_restriccion_capacidad

- model_id: `sakana/fugu-max`
- success: True  | final: 5.57 | quality: 6.0
- latency_total: 21.329s | tokens_per_second: 99.2
- input_tokens: 332 | output_tokens: 2115

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

Asumiendo 5 días laborables por semana, tienes **unas 160 horas** antes del cierre: 20 horas semanales, equivalentes a solo **4 semanas de trabajo a tiempo completo**.

| Iniciativa | Esfuerzo a tu ritmo | Decisión |
|---|---:|---|
| **A. Reescritura** | ~24 semanas | **No hacerla este trimestre.** |
| **B. Alta** | ~2 semanas | **Primera prioridad.** |
| **C. Panel** | ~6 semanas, además de A | **Posponer.** |
| **D. Videos** | ~4 semanas | **Segunda, si el canal de distribución ya funciona.** |

### Plan para las 8 semanas

- **Semanas 1–2: B.** Dedica unas 40 horas a confirmar dónde y por qué se pierde la gente, corregir el paso 2 con el cambio más pequeño posible y comprobar la conversión tras el lanzamiento.
- **Semanas 3–6: D, con una condición.** Haz los 10 videos solo si ya sabes dónde se publicarán y tienes señales de que ese canal atrae clientes. Si no, prueba primero con 1–2 videos; no comprometas cuatro semanas de trabajo basándote solo en que el contenido podría funcionar.
- **Semanas 7–8: margen para imprevistos y resultados.** Úsalo para iterar en el alta según los datos y evaluar si el contenido generó resultados. Si B se alarga, recorta o aplaza D antes de sacrificar la mejora del alta.

**A la lista de espera:** 3 meses a tiempo completo son aproximadamente 24 semanas a tu capacidad actual. No empezaría una reescritura grande por una promesa genérica de velocidad futura; identifica primero qué limitación concreta te está frenando y si se puede resolver con cambios puntuales.

**C tampoco cabe de forma realista:** depende de A y requiere unas 6 semanas de tu capacidad actual una vez terminada. Si quieres validar la demanda del panel, hazlo sin construirlo todavía: por ejemplo, con una maqueta o un informe manual para algunos clientes.