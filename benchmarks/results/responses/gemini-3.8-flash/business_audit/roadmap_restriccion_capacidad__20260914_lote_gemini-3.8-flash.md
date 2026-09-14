# Gemini 3.8 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.8-flash`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 14.171s | tokens_per_second: 119.2
- input_tokens: 242 | output_tokens: 1689

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

Tu presupuesto real de construcción para este trimestre no son 8 semanas: son **160 horas** (8 semanas × 5 días × 4h). Eso equivale a solo **1 mes de trabajo a tiempo completo**. 

Con esa restricción matemática, este es tu plan para el trimestre:

---

### 1. Lo que vas a hacer (y en este orden)

#### **Semanas 1 y 2: B) Arreglar el flujo de alta (Onboarding)**
* **Por qué primero:** Estás perdiendo al 60% de la gente en la puerta de entrada. Cualquier esfuerzo de marketing o producto futuro se tira a la basura si el balde está pinchado. 
* **Cálculo real:** Si te toma "1 semana a tiempo completo", a tu ritmo de 4h/día te llevará **2 semanas de calendario** (40 horas).
* **Meta de éxito:** Reducir la caída del paso 2 al menos a la mitad antes de tocar cualquier otra cosa.

#### **Semanas 3 a 6: D) Grabar los 10 videos de contenido**
* **Por qué segundo:** Con el embudo arreglado, ahora sí tiene sentido meter tracción. Además, grabar y editar solo consume muchísima energía mental; distribuir 10 videos en 4 semanas (2-3 videos por semana en bloques de 4h) es sostenible sin descuidar el soporte.
* **Cálculo real:** 2 semanas a tiempo completo equivalen a **4 semanas de tu calendario** (80 horas).

#### **Semanas 7 y 8: Buffer / Margen de seguridad**
* **No agregues ninguna iniciativa nueva aquí.**
* En una empresa de una sola persona, el soporte aumentará (los videos atraerán gente y el nuevo onboarding retendrá más), te vas a enfermar un par de días, o la edición de video se complicará. Esas últimas **40 horas son tu seguro** para cerrar el trimestre habiendo cumplido el 100% de lo prometido.

---

### 2. Lo que NO vas a hacer (descartadas)

* **A) Reescribir la plataforma (ELIMINADA):** 
  Es una trampa mortal clásica de fundador técnico. Dices que toma 3 meses a tiempo completo: a tu capacidad real de media jornada, **te tomaría 6 meses sin hacer absolutamente nada más** (ni marketing, ni mejoras, acumulando deuda de soporte). No se reescribe nada hasta que la facturación te permita contratar a alguien o pagar para sacarte el soporte de encima.
* **C) Panel de métricas (ELIMINADA):** 
  Depende de A, por lo que muere automáticamente. Incluso si pudieras hacerla sobre la base actual: un panel de métricas no salva un producto que pierde al 60% de sus usuarios en el registro.

### Resumen ejecutivo
Terminas el trimestre con **el embudo reparado (B)**, **motor de adquisición encendido (D)** y **cero frustración por proyectos a medio terminar**. Vuelve a evaluar la arquitectura el próximo trimestre solo si el sistema actual se está cayendo a pedazos.