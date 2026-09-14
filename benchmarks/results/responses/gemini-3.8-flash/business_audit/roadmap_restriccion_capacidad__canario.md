# Gemini 3.8 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.5 | quality: 10.0
- latency_total: 18.241s | tokens_per_second: 99.5
- input_tokens: 242 | output_tokens: 1815

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

Hagamos números reales antes de tocar una sola línea de código. 

Tu capacidad neta este trimestre es de **160 horas** (8 semanas × 5 días × 4 horas). Los estimados de un fundador solo siempre se quedan cortos por imprevistos. Tus 160 horas rinden, en la práctica, como 120-130 horas de desarrollo puro.

Con esa realidad, **la iniciativa A y la C quedan descartadas de inmediato**. Intentar reescribir la plataforma (A) te llevaría 6 meses a tu ritmo actual de 4h/día; congelarías el negocio, no entregarías valor y quemarías el trimestre a un tercio del camino. Como C depende de A, C no existe este trimestre.

El orden táctico del trimestre es el siguiente:

---

### Semanas 1 a 2: Iniciativa B (Arreglar el flujo de alta)
* **Por qué primero:** Tienes un balde roto. El 60% de la gente se te va en el paso 2. Meter tráfico o funciones nuevas ahora es quemar dinero y tiempo.
* **Ajuste de tiempo:** Dices "1 semana". Asigna **2 semanas (40 horas)**. Eso te da margen para medir, corregir errores en producción y asegurarte de que la fuga se cerró de verdad sin que te coma el soporte.
* **Objetivo de salida:** Subir la conversión de ese paso y dejar el camino listo para recibir volumen.

---

### Semanas 3 a 5: Iniciativa D (10 videos de contenido)
* **Por qué segundo:** Una vez que el embudo ya no pierde el 60% de los usuarios, tiene sentido traer gente nueva.
* **Ajuste de tiempo:** Dices "2 semanas". Asigna **3 semanas (60 horas)**. Escribir, grabar, editar y distribuir 10 piezas de contenido siendo una sola persona es agotador mentalmente.
* **Regla:** Graba en lote (*batching*). Si te pones a hacer un video por día, la fricción de armar set y editar te destruirá las 4 horas de foco.

---

### Semanas 6 a 8: "Iniciativa E" oculta (Atacar el soporte) o Iterar
Te quedan 3 semanas (~60 horas). **No empieces C ni A.**
Dedica este bloque a una de estas dos cosas:

1. **Reducir tus 2 horas diarias de soporte:** Automatiza respuestas, crea documentación o arregla los 3 bugs que más preguntas generan. Si bajas el soporte de 2h a 1h diaria, ganas 5 horas a la semana para siempre. Esa es la verdadera reescritura que tu negocio necesita hoy.
2. **Iterar sobre el onboarding:** Si los datos de B muestran que el cuello de botella se movió al paso 3, arréglalo antes de inventar cosas nuevas.

---

### Resumen del trimestre:
* **Semana 1-2:** B (Tapar la fuga del onboarding).
* **Semana 3-5:** D (Atraer usuarios al embudo ya reparado).
* **Semana 6-8:** Reducir fricción operativa / soporte (para comprarte más de 4h/día el próximo trimestre).
* **Papelera:** A (trampa mortal técnica) y C (bloqueada por A).