# Seed 2.1 Turbo — business_audit/roadmap_restriccion_capacidad

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.31 | quality: 10.0
- latency_total: 101.339s | tokens_per_second: 72.2
- input_tokens: 302 | output_tokens: 7316

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

### Primero: cálculo de tu capacidad REAL (no la ideal, que es donde se equivocan el 90% de los fundadores solos)
Tienes 4h/día de construcción efectiva = 20h/semana. En 8 semanas son **160h brutas**.  
Le descontamos un 20% de buffer obligatorio (soporte que se pasa de las 2h, bugs urgentes, días de baja productividad, reuniones imprevistas): te quedan **128h útiles garantizadas** para todo el trimestre.

Además, tus estimaciones de esfuerzo son de tiempo completo (8h/día de construcción), así que los convertimos a TU ritmo: cada semana full-time = 40h = 2 semanas de tu trabajo. Ajustado:
- A: 3 meses full-time = 480h → **ni la terminas en 2 trimestres** trabajando solo a tu ritmo actual.
- B: 1 semana full-time = 40h → 2 semanas de tu tiempo.
- C: 3 semanas full-time = 120h → 6 semanas de tu tiempo, PERO depende de A → imposible en este trimestre.
- D: 2 semanas full-time = 80h → 4 semanas de tu tiempo.

---

### Descarte inicial de iniciativas no factibles (no son malas, pero no caben sin matar tu negocio)
❌ **A (reescritura de plataforma): No la hacemos en este trimestre**  
No solo no la terminas en 8 semanas: si dedicaras TODO tu tiempo de construcción a ella, solo avanzarías un 30%, sin entregar nada usable a clientes, sin generar ningún impacto en ingresos o conversión, y sin margen para imprevistos.  
Las reescrituras en equipos de una persona son la trampa número 1 de los fundadores técnicos: te sientes productivo escribiendo código, pero pasas meses sin generar valor, y te puedes quedar sin recursos antes de terminar.

❌ **C (panel de métricas): Pospuesto hasta el próximo trimestre**  
Depende de A, así que no hay forma de hacerlo ahora. Lo reevaluaremos cuando tengamos datos reales de si vale la pena invertir en la reescritura.

---

### Priorización de lo que SÍ caben, por impacto y sinergia
Quedan B y D, y ambas caben perfectamente (sumadas son 120h, te sobran 8h de margen). El orden no es arbitrario:
1.  **B primero (arreglo del flujo de alta): Impacto alto, esfuerzo bajo, y multiplica el impacto de todo lo demás que hagas después.**
    Si pasas de perder el 60% de usuarios en el paso 2 a perder, por ejemplo, el 30%, tu tasa de alta se duplica. Cualquier esfuerzo de adquisición que hagas después (como los videos) rendirá el doble.
2.  **D después (videos de contenido): Impacto medio, esfuerzo medio, y complementa a B.**
    Los videos traen más gente al alta, que ya se convierte mejor gracias a B. Si lo hicieras al revés, desperdiciarías el 60% del tráfico que generes.

---

### Plan semanal detallado del trimestre (con buffers y objetivos medibles)
Trabajas en UNA SOLA iniciativa a la vez (el costo de cambio de contexto para un fundador solo es altísimo, no mezcles proyectos).

#### Bloque 1: Arreglo del flujo de alta (Semanas 1 y 2, con 1 semana de reserva)
**Objetivo medible:** Reducir el abandono en el paso 2 de 60% a máximo 30%.
- Semana 1: Analiza datos reales de por qué se van los usuarios (¿bug? ¿formulario muy largo? ¿no entienden el siguiente paso?). Desarrolla la solución, prueba internamente.
- Semana 2: Lanza a producción, monitorea la tasa en tiempo real, ajusta pequeños detalles si no baja lo suficiente.
- Si terminas antes: No te adelantes a D. Usa el tiempo para hablar con 3-5 usuarios que pasaron por el nuevo alta para validar que no hay fricciones ocultas, y para escribir los guiones de los videos (así vas más rápido después).

#### Bloque 2: Grabación de 10 videos (Semanas 3 a 6, con 1 semana de reserva)
**Objetivo medible:** Publicar los 10 videos, que generen al menos [define un número realista según tu canal] visitas por semana, y que al menos el 10% de las visitas lleguen a tu página de alta.
- Semana 3: Escribe los 10 guiones, graba todas las tomas principales.
- Semana 4: Edita los primeros 5 videos, sube y programa los 3 primeros con sus llamados a la acción hacia el alta.
- Semana 5: Edita los últimos 5 videos, programa la publicación de todos los restantes.
- Semana 6: Optimiza los títulos/etiquetas de los videos que mejor rendimiento tengan, y añade enlaces en tu página de soporte a los videos de preguntas frecuentes (esto te reducirá el tiempo de soporte después).
- Si terminas antes: Graba 2 videos extra de consultas que te lleguen mucho por soporte: te ahorras tiempo de operación a futuro.

#### Bloque 3: Espacio de validación y preparación para el próximo trimestre (Semanas 7 y 8)
Este es tu margen de seguridad, no lo asignes a nada fijo. Lo usas para tres cosas en orden de prioridad:
1.  **Recoger datos de B y D:** Cuánto subió la conversión del alta, cuántos clientes nuevos trajeron los videos, cuánto aumentaron tus ingresos. Esto te dará la información para decidir si vale la pena invertir en A el próximo trimestre.
2.  **Hacer un spike (prueba técnica) de A de máximo 20h (1 semana):** No empieces la reescritura completa. Reescribe solo una parte muy pequeña de la plataforma (por ejemplo, el flujo de alta que acabas de arreglar) en el nuevo framework para responder:
    - ¿Realmente ganas tanta velocidad como crees?
    - ¿Hay problemas técnicos que no habías previsto?
    - ¿Cuánto te cuesta realmente hacer una funcionalidad sencilla en el nuevo framework?
    Esto te dará un estimado mucho más realista del esfuerzo total de A, sin mentirte.
3.  **Arreglar pequeños bugs o mejoras que hayan salido durante el trimestre.**

---

### ¿Qué pasa con A y C después de este trimestre?
Con los resultados de B y D, tendrás dos cosas que no tienes ahora:
1.  Más ingresos (por la mejora de conversión y el nuevo tráfico) para delegar parte del soporte y pasar de 4h/día a 5-6h/día de construcción.
2.  Datos reales del esfuerzo de A (por el spike) para decidir si vale la pena.

Si confimas que la reescritura te ahorra al menos el 50% del tiempo de desarrollo de nuevas funcionalidades, **no hagas un big bang**: ve reescribiendo partes de la plataforma una por una, cada una con valor para el cliente. Por ejemplo: empieza por reescribir el panel de métricas (C) en el nuevo framework, así entregas valor a tus clientes mientras avanzas en la reescritura. No pasas 6 meses sin entregar nada.

---

### Regla de oro para no desviarte
Si en medio del trimestre te dan ganas de empezar la reescritura, pregúntate: *¿Esto me genera más ingresos o más tiempo de construcción en los próximos 3 meses?* Si la respuesta es no, vuelve a lo que estabas haciendo. La reescritura es un objetivo de largo plazo, pero primero necesitas sobrevivir y crecer lo suficiente como para poder invertir en ella sin morir en el intento.