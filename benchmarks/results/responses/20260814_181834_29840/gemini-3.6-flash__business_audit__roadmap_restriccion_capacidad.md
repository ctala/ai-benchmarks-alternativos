# Gemini 3.6 Flash — business_audit/roadmap_restriccion_capacidad

- model_id: `google/gemini-3.6-flash`
- success: True  | final: 8.62 | quality: 10.0
- latency_total: 10.51s | tokens_per_second: 192.5
- input_tokens: 242 | output_tokens: 2023

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

Como tu Jefe de Producto (y la voz de la razón pragmática para un solo founder), voy a ser muy directo. 

Primero, **la matemática de tu realidad**:
* Te quedan 8 semanas. 
* A 4h/día reales = 20 horas/semana de construcción.
* Tu presupuesto total de desarrollo para este trimestre es de **160 horas**.

Aquí tienes la priorización sin rodeos y basada en impacto/esfuerzo real:

---

### El Veredicto (Qué hacer y qué matar)

#### 1. PRIORIDAD ABSOLUTA: Opción B (Arreglar el flujo de alta)
* **Esfuerzo:** 1 semana (20h).
* **Por qué:** Tienes un cubo con un agujero enorme. Perder el 60% en el paso 2 es tirar tu trabajo anterior a la basura. Arreglar esto multiplica el rendimiento de todo lo demás sin añadir más clientes al funnel.
* **Cuándo:** **Semanas 1 y 2.** (Te doy 2 semanas de calendario porque seguro saldrán imprevistos en el paso 2 o necesitarás ajustar el copy/diseño).

#### 2. SEGUNDA PRIORIDAD: Opción D (Grabar 10 videos)
* **Esfuerzo:** 2 semanas (40h).
* **Por qué:** Una vez que arregles la conversión (B), necesitas meter gente al flujo. El contenido alimentará el nuevo flujo de alta que ya no pierde gente.
* **Cuándo:** **Semanas 3 y 4.**

#### 3. MATAR / CONGELAR: Opción A (Reescribir la plataforma)
* **Esfuerzo:** 3 meses a tiempo completo (~480 horas).
* **Por qué:** Tienes 160 horas este trimestre. Intentar la opción A es el suicidio clásico del fundador en solitario. Pasarás 6 meses sin lanzar valor, el soporte te comerá vivo y el producto actual morirá desangrado por el flujo de alta roto. **Prohibido tocar la reescritura este trimestre.**

#### 4. BLOQUEADA: Opción C (Panel de métricas)
* **Esfuerzo:** 3 semanas.
* **Por qué:** Depende de A. Como A está muerta, C no se hace. *(Nota: Si en el futuro descubres cómo hacer un panel "sucio/low-code" para clientes en 3 días sin reescribir la plataforma, lo reevaluamos. Hoy, no).*

---

### Tu Calendario Real para las 8 Semanas

* **Semana 1-2:** Arreglar el paso 2 del alta (Opción B) + Medir que la caída baje del 60% al menos al 20-30%.
* **Semana 3-4:** Grabar y editar los 10 videos (Opción D) para atraer tráfico al flujo ya optimizado.
* **Semana 5-6:** **Reducir tu soporte diario.** Usa estas 40h para automatizar las 2h/día de soporte que te están quitando vida (documentación, bots simples, arreglar los bugs que generan más tickets). *Tu objetivo es ganar 1h/día extra para el próximo trimestre.*
* **Semana 7-8:** **Colchón de margen / Iteración.** Ningún plan sobrevive al contacto con la realidad. Usa estas semanas para arreglar lo que se rompa de B y D, o descansar.

### Tu regla de oro para este trimestre:
> *"No construyo nada nuevo para un producto que hoy pierde al 60% de sus usuarios en la puerta de entrada."* 

Empieza hoy mismo con la **B**.