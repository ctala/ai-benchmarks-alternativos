# Gemini 3.7 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 6.02 | quality: 6.0
- latency_total: 13.579s | tokens_per_second: 107.8
- input_tokens: 242 | output_tokens: 1464

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

Hagamos los números reales primero:
* **Capacidad real:** 8 semanas × 5 días × 4h = **160 horas de construcción** (equivalente a solo **4 semanas a tiempo completo**).
* La iniciativa **A** te tomaría ~480 horas (3 meses a tiempo completo). A tu ritmo actual te tomaría **24 semanas (medio año)** sin hacer nada más. 

Con los números sobre la mesa, la reescritura es inviable y suicida para este trimestre. Y como **C depende de A**, ambas quedan descartadas de inmediato.

Aquí tienes el orden de tu trimestre:

---

### 1. Semanas 1 y 2: Iniciativa B (Arreglar el flujo de alta)
* **Por qué:** Tienes un balde con un agujero gigante (60% de fuga). Llevar tráfico o crear contenido antes de arreglar esto es tirar tu tiempo a la basura.
* **Ajuste realista:** Te llevará 2 semanas reales a 4h/día (40 horas). Deja el flujo simple, sin florituras, enfocado solo en eliminar la fricción del paso 2.

### 2. Semanas 3 a 5: Iniciativa D (Grabar 10 videos)
* **Por qué:** Ahora que el balde ya retiene agua (alta optimizada), tiene sentido meterle usuarios arriba del embudo.
* **Ajuste realista:** 2 semanas a tiempo completo son **3 semanas a tu ritmo de 4h/día** (guiones, grabación, edición mínima y publicación).

### 3. Semanas 6 y 7: Reducir las 2h diarias de soporte (Iniciativa no listada pero urgente)
* **Por qué:** Tu mayor cuello de botella no es el framework, es que el 33% de tu tiempo se va en soporte. 
* **Qué hacer:** Con 40 horas libres aquí, documenta FAQs, crea emails automáticos de bienvenida que resuelvan dudas típicas o implementa un chatbot básico. Si reduces el soporte a 1h/día, ganas un 25% más de capacidad de desarrollo para el próximo trimestre.

### 4. Semana 8: Buffer y estabilización
* **Por qué:** Como solo-founder, te vas a enfermar, saldrá un bug crítico o soporte te comerá días enteros. No planifiques features para la última semana.

---

### Resumen de descartes:
* **A (Reescritura): DESCARTADA.** No se reescribe código en fase de supervivencia a menos que el sistema esté literalmente caído 24/7.
* **C (Métricas): DESCARTADA.** Depende de A. Si tus clientes te lo exigen a gritos, dáselas manualmente en un Google Sheet o Notion una vez por semana antes de picar código.