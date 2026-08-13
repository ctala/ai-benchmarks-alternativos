# Tencent Hy3 — business_audit/roadmap_restriccion_capacidad

- model_id: `tencent/hy3`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 35.322s | tokens_per_second: 76.2
- input_tokens: 302 | output_tokens: 2693

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

Como jefe de producto de tu empresa de una sola persona, mi trabajo es ser brutalmente honesto con los números y proteger tu tiempo. No priorizamos sueños, priorizamos capacidad real.

Aquí está el diagnóstico y el orden de batalla para tus próximas 8 semanas.

### 1. El filtro de realidad (Matemáticas primero)
Tu capacidad real de construcción este trimestre es:
**8 semanas × 5 días × 4 horas = 160 horas enfocadas.**

*   **Iniciativa A (Reescribir plataforma):** Requiere ~3 meses a tiempo completo (unas 480+ horas). Aunque trabajaras 8h/día no llegas; con tus 4h/día te llevaría más de 6 meses. **Es matemáticamente imposible este trimestre. Córtala de la lista ya.**
*   **Iniciativa C (Panel de métricas):** Depende de A. Como A no entra, C es un espejismo. **Se pospone al próximo trimestre.**

### 2. Lo que sí vas a construir (B y D)
Te quedan dos iniciativas viables que suman ~120 horas de esfuerzo (B: ~40h, D: ~80h). Caben perfecto en tus 160h, dejándote un colchón de 40h para imprevistos de soporte o fatiga mental.

### 3. Orden del trimestre (Cronograma)

**Semanas 1 y 2: INICIATIVA B (Arreglar el flujo de alta)**
*   **Por qué primero:** Tienes un agujero en el cubo. Si pierdes al 60% en el paso 2, cualquier esfuerzo en marketing (como los videos D) será tirar agua a un cubo roto. Es alto impacto y bajo esfuerzo. Hazlo inmediatamente y métrico el cambio.
*   **Meta:** Cerrar la fuga de conversiones.

**Semanas 3 a 6: INICIATIVA D (Grabar 10 videos de contenido)**
*   **Por qué segundo:** Una vez tapado el agujero (B), necesitas tráfico. 10 videos en 4 semanas a 4h/día es realista (2.5 videos/semana, incluyendo guion, grabación y edición básica). Impacto medio, pero alimenta el embudo de ventas que acabas de arreglar.
*   **Meta:** Generar un motor de adquisición de bajo coste.

**Semanas 7 y 8: BUFFER Y PREPARACIÓN**
*   No llenes este espacio con trabajo ficticio. Usa esas ~40 horas libres para:
    1.  Absorber picos de soporte que seguro aparecerán.
    2.  Iterar sobre B si los números no mejoran lo esperado.
    3.  Documentar y maquetar el futuro rewrite (A) para que el próximo trimestre arranques con ventaja.

**Resumen para el fundador:** Mata A y C por ahora. Ejecuta B, luego D. Protégete con el buffer. No te castigues por no reescribir la plataforma; tu trabajo hoy es sobrevivir y crecer con lo que tienes, no construir la catedral perfecta.