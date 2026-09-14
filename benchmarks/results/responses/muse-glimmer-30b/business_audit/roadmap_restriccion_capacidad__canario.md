# Muse Glimmer 30B — business_audit/roadmap_restriccion_capacidad

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.67 | quality: 10.0
- latency_total: 29.206s | tokens_per_second: 61.7
- input_tokens: 266 | output_tokens: 1801

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

Con 4h/día reales de construcción tienes ~20h/semana, 160h en 8 semanas.

No es un problema de impacto, es de capacidad real y dependencias.

**Capacidad ajustada a tu realidad:**
* **A Reescribir plataforma:** 3 meses full time ≈ 480h. Para ti son 24 semanas. No entra en trimestre y te dejaría sin soporte.
* **B Arreglar flujo de alta:** 1 semana full time ≈ 40h. Para ti son 2 semanas reales.
* **C Panel de métricas:** 3 semanas full time ≈ 120h. Para ti son 6 semanas reales. **Y depende de A terminado.** No es viable.
* **D 10 videos de contenido:** 2 semanas full time ≈ 80h. Para ti son 4 semanas reales.

### Orden recomendado para el trimestre

**1. B - Arreglar el flujo de alta. Semanas 1-2**
Impacto alto, esfuerzo bajo, sin dependencias. Pierdes el 60% en el paso 2, es fuga de revenue directa.
Haz un fix quirúrgico: mide conversión antes/después, reduce fricción, test A/B del paso 2. Es lo único que te paga el trimestre.

**2. D - Grabar 10 videos de contenido. Semanas 3-6**
Impacto medio y te da palanca de adquisición sin tocar código. Con 4h/día puedes grabar/editar 2-3 videos por semana.
Deja 2 semanas de buffer para soporte que siempre se come tiempo.

**3. A y C - Pausar**
A Reescribir es la trampa clásica de founder solo. Alto impacto futuro pero te quita todo el trimestre y no entregas valor al mercado. Si la plataforma no está muriendo, no la reescribas ahora.
C depende de A, por lo tanto automáticamente se cae. No tiene sentido planificarlo.

### Trimestre realista

* **Semana 1-2:** B. Objetivo: bajar la caída del paso 2 de 60% a <30%.
* **Semana 3-6:** D. 10 videos listos y publicados.
* **Semana 7-8:** Buffer de soporte + medir impacto de B + documentar qué parte de A realmente duele hoy. Si quieres tocar tecnología, haz refactors aislados de 2-4h que reduzcan tu soporte diario, no un rewrite.

Con 4h/día no puedes construir el futuro y arreglar el presente. Este trimestre gana el presente: cierra el embudo y genera tracción con contenido. A y C se revisan en el próximo trimestre con datos de conversión reales.