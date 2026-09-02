# Tencent Hy4 preview — business_audit/roadmap_restriccion_capacidad

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.37 | quality: 10.0
- latency_total: 98.225s | tokens_per_second: 52.9
- input_tokens: 291 | output_tokens: 5193

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

Como Product Manager, mi trabajo es protegerte de la realidad y de ti mismo. Los fundadores solos suelen cometer dos errores clásicos: sobreestimar su capacidad real y enamorarse de soluciones técnicas (código) en lugar de problemas de negocio (fugas de usuarios).

Vamos a hacer los números en frío y luego ordenamos tu trimestre.

### 1. El Reality Check de Capacidad (Los Números)
*   **Tu capacidad real:** 4 horas/día x 5 días a la semana = **20 horas/semana**. (Asumo 5 días porque si trabajas 7, te quemarás antes de terminar el trimestre).
*   **Tu capacidad trimestral:** 20 horas x 8 semanas = **160 horas totales**.
*   **Traducción a tiempo completo:** 160 horas equivalen a **exactamente 4 semanas (1 mes) de trabajo a tiempo completo (FTE)**.

### 2. El Veredicto de tus Iniciativas
Con solo 4 semanas de tiempo completo real, esto es lo que dicta la priorización:

*   **A) Reescribir la plataforma (Descartada):** Requiere 3 meses a tiempo completo (unas 480 horas). A tu ritmo real de 20h/semanales, **esto te tomaría 6 meses (24 semanas)**. Es matemáticamente imposible este trimestre. Es la clásica "trampa de reescritura" (Rewrite Trap). Es cambiar las tuberías de cobre por oro en un edificio que se está incendiando.
*   **C) Panel de métricas (Bloqueada/Descartada):** Depende de A, que ya está descartada. Además, es una iniciativa de retención. No tiene sentido dar métricas a usuarios que ni siquiera logran registrarse.
*   **B) Arreglar el flujo de alta (Prioridad 1):** Toma 1 semana (~20h). Impacto altísimo. Detiene una hemorragia del 60%. Es el ROI más alto de tu empresa hoy.
*   **D) Videos de contenido (Prioridad 2):** Toman 2 semanas (~40h). Impacto medio. Atraen tráfico.

---

### 3. Tu Trimestre Ordenado (El Plan de Ataque de 8 Semanas)

No puedes hacer todo. Vas a enfocarte en **tapar el agujero y luego llenar el cubo**.

#### Fase 1: Tapar la hemorragia (Semanas 1 y 2)
*   **Qué hacer:** **Iniciativa B** (Arreglar el flujo de alta).
*   **Por qué:** De nada sirve que te mates grabando videos (D) para traer tráfico nuevo si el 60% se va a ir por el desagüe en el paso 2. Arreglando esto, vas a multiplicar el valor de todo el esfuerzo de marketing que hayas hecho hasta hoy sin escribir una sola línea de código nuevo.
*   **Entregable:** Flujo de alta arreglado y en producción al final de la semana 2.

#### Fase 2: Llenar el embudo (Semanas 3 a 5)
*   **Qué hacer:** **Iniciativa D** (Grabar y publicar los 10 videos).
*   **Por qué:** Ahora que el "cubo" ya no pierde agua, es hora de echar más. Te doy **3 semanas en lugar de 2** para esto. ¿Por qué? Porque grabar, editar y distribuir buen contenido siempre toma el doble de lo que un fundador estima. 
*   **Entregable:** 10 videos publicados y distribuidos.

#### Fase 3: Iterar, Medir y Buffer (Semanas 6 a 8)
*   **Qué hacer:** Medir el impacto real de la Iniciativa B, iterar sobre ella y tener un colchón (buffer) de tiempo.
*   **Por qué:** Eres un equipo de una sola persona. Ese soporte diario de 2 horas va a tener días malos que te comerán tus 4 horas de construcción. Necesitas tiempo muerto para no colapsar.
*   **El elefante en la habitación (Iniciativa A):** Si el framework actual te está matando la velocidad, **no lo reescribas**. Usa un par de horas de esta fase para leer sobre el **Patrón Strangler Fig** (migración gradual por módulos). Si es absolutamente necesario, el próximo trimestre empiezas a migrar una pequeña parte, no el sistema completo.

**Resumen de PM:** Tienes un problema de negocio (conversión), no un problema de tecnología (framework). Olvida el código elegante este trimestre. Tapa la fuga, trae tráfico y asegura la supervivencia.