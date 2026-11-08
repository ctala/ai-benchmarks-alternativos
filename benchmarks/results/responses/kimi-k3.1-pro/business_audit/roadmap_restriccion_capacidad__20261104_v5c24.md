# Kimi K3.1 Pro — business_audit/roadmap_restriccion_capacidad

- model_id: `moonshotai/kimi-k3.1-pro`
- success: True  | final: 6.43 | quality: 8.0
- latency_total: 174.33s | tokens_per_second: 25.0
- input_tokens: 388 | output_tokens: 4354

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

**Haría B → D. A y C quedan fuera del trimestre.** Primero tapas la fuga de altas; después traes más tráfico con contenido.

### Capacidad real

Asumiendo 5 días por semana:

- **4 h/día × 5 días × 8 semanas = 160 h brutas.**
- Reservaría un 20% para imprevistos: **~128 h planificables**.
- A, estimada en 3 meses a tiempo completo, te llevaría aproximadamente **6 meses a tu ritmo actual**. Empezarla ahora solo garantizaría una migración a medias.
- C está bloqueada por A, así que ni siquiera es una opción ejecutable.

### Plan del trimestre

| Semanas | Trabajo | Regla de alcance |
|---|---|---|
| **1–2** | **B: arreglar el alta** | Instrumenta el embudo, corrige el paso 2 con el cambio más pequeño posible y mide también el alta completa. Nada de rediseñar todo el flujo. |
| **3–6** | **D: producir los videos** | Timebox estricto. Graba por lotes y empieza a publicar antes de tener los 10; evita que la edición infle el proyecto. |
| **7–8** | **Colchón, medición e iteración** | Absorbe retrasos, revisa si B mejoró la conversión y haz ajustes pequeños. Si todo va bien, distribuye mejor el contenido o haz una segunda iteración acotada de B. |

Estoy interpretando conservadoramente las estimaciones de B y D como semanas equivalentes a tiempo completo: unas 2 y 4 semanas naturales a tu capacidad. **Si ya estaban estimadas a tus 4 h/día, las harás en 1 y 2 semanas y ganarás más colchón; el orden no cambia.**

**Lo que no haría:** usar el tiempo sobrante para “ir avanzando” A. Una reescritura inconclusa no aporta velocidad ni valor y sí añade riesgo operativo. A se replantea el próximo trimestre —preferiblemente como modernización incremental— y C solo se reevalúa si desaparece su dependencia.