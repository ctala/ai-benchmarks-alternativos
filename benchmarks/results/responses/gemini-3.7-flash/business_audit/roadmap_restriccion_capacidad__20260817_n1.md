# Gemini 3.7 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.7-flash`
- success: True  | final: 8.81 | quality: 10.0
- latency_total: 11.783s | tokens_per_second: 129.8
- input_tokens: 242 | output_tokens: 1530

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

Tu presupuesto real no son 8 semanas: **tienes 160 horas de construcción** (8 semanas × 5 días × 4h). Eso equivale a solo **4 semanas de trabajo a tiempo completo estándar**. 

Con tu capacidad real, este es el diagnóstico implacable y el orden de ejecución:

---

### La realidad de la lista:
* **A) Reescribir la plataforma (3 meses FT = ~480h): DESCARTE TOTAL.** 
  Te llevaría 3 trimestres enteros a tu ritmo actual. Empezarla hoy es matar la empresa. La deuda técnica se tolera hasta que tengas ingresos para pagar ayuda.
* **C) Panel de métricas (3 semanas FT): BLOQUEADA.** 
  Depende de A, así que muere automáticamente junto con A.

Nos quedan **B** y **D**, que suman exactamente tu capacidad máxima sin margen de error.

---

### Tu plan de ejecución para las 8 semanas:

#### **Fase 1: Tapa la fuga del cubo (Semanas 1 y 2)**
* **Iniciativa B: Arreglar el flujo de alta.**
* **Tiempo asignado:** ~40 horas (2 semanas a 4h/día).
* **Por qué:** Tienes un 60% de caída en el paso 2. Meter tráfico hoy es tirar dinero y tiempo a la basura. Arreglar esto multiplica el valor de cada usuario que ya llega sin necesidad de marketing nuevo.

#### **Fase 2: Atrae gente al flujo arreglado (Semanas 3 a 6)**
* **Iniciativa D: 10 videos de contenido.**
* **Tiempo asignado:** ~80 horas (4 semanas a 4h/día).
* **Ajuste táctico:** No te bloquees grabando los 10 de golpe. Graba, edita y publica en lotes de 2 por semana. Si a la semana 4 ves que un formato no funciona, puedes pivotar los últimos 4 videos sin haber quemado todo el esfuerzo.

#### **Fase 3: Margen de supervivencia y optimización (Semanas 7 y 8)**
* **Tiempo asignado:** ~40 horas.
* **Qué hacer:** **Nada nuevo del backlog.**
* **Por qué:** Eres solo una persona. El soporte subirá cuando publiques los videos y arregles el alta. Estas dos semanas son tu colchón para:
  1. Absorber los retrasos inevitables de B y D.
  2. Atender picos de soporte.
  3. Iterar pequeñas fricciones que los nuevos usuarios reporten en el nuevo onboarding.

---

### Resumen ejecutivo:
1. **Semanas 1-2:** Haz **B**.
2. **Semanas 3-6:** Haz **D**.
3. **Semanas 7-8:** Margen / Soporte / Iteración.
4. **Congeladas (A y C):** Ni las mires hasta que el negocio justifique contratar a alguien o delegar la operación.