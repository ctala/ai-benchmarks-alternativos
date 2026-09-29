# Bonsai 2 27B — business_audit/roadmap_restriccion_capacidad

- model_id: `prism-ml/ternary-bonsai-2-27b`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 688.717s | tokens_per_second: 5.7
- input_tokens: 293 | output_tokens: 3934

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



Te lo ordeno con tu capacidad real, no con la capacidad de un equipo ideal:

## Orden del trimestre

### 1) B — Arreglar el flujo de alta  
**Semanas 1–1: 1 semana**

Esta va primero sin debate.

- Impacto: alto.
- Esfuerzo: bajo.
- No depende de nada.
- Si hoy pierdes al 60% en el paso 2, eso es dinero y usuarios que se van.
- Es la iniciativa con mejor relación impacto/esfuerzo.

**Objetivo:**  
Reducir el abandono del paso 2 de forma medible. No “mejorar un poco”. Buscar un cambio claro en la métrica.

Métrica clave:  
`% de abandonos en el paso 2`  
Ideal: bajar de 60% a 30–40% o menos.

Si B no termina en la primera semana, detienes D y terminas B.

---

### 2) D — Grabar 10 videos de contenido  
**Semanas 2–3: 2 semanas**

Esta va segunda.

- Impacto: medio.
- Esfuerzo: medio.
- No depende de A.
- Puede ayudarte a generar demanda, confianza o señales de mercado.
- Es más sostenible para un fundador solo que empezar una reescritura de plataforma.

Pero con una condición:  
**no lo hagas perfecto**.  
Hazlo suficiente para publicar y aprender.

Objetivo:  
10 videos listos y publicados. No una producción de agencia.

Si D empieza a consumirte más de 2 semanas, lo cortas y lo terminas.

---

### 3) A — Reescribir la plataforma en otro framework  
**No la ejecutes completa este trimestre.**

Aquí está la trampa.

A suena estratégica, pero con tu capacidad real no entra.

Tienes:

- 8 semanas.
- 4 horas reales al día para construir.
- Aproximadamente **160 horas** disponibles.

A está estimada en:

- 3 meses a tiempo completo.
- Eso, con 4 horas diarias, se convierte en **24 a 36 semanas**, dependiendo de cómo cuentes el tiempo completo.

Es decir:  
**A no cabe en este trimestre.**

Si A no es ineludible, no la toques este trimestre.

Si A sí es ineludible, no empieces la reescritura completa. Haz solo esto:

- 1 semana: investigación y decisión.
- 1 semana: POC o prueba de arquitectura.
- Resto del tiempo: no arrancas hasta que hayas validado que realmente vale.

Pero ojo:  
**eso no es A**. Eso es un gate de decisión.

---

### 4) C — Panel de métricas para clientes  
**No este trimestre.**

C depende de A.  
A no entra.  
Por lo tanto, C tampoco entra.

Además:

- Impacto: medio.
- Esfuerzo: 3 semanas.
- Depende de una decisión grande.
- No es urgente frente a B.
- No te da el retorno más rápido.

C queda para después, cuando A tenga una decisión clara y haya capacidad.

---

## Plan concreto de las 8 semanas

| Semana | Acción |
|---|---|
| 1 | B: arreglar flujo de alta |
| 2–3 | D: grabar y publicar 10 videos |
| 4 | A-light: investigación / decisión / POC, solo si A es ineludible |
| 5–8 | Buffer, mejoras derivadas de B y D, o A solo si el gate pasa |

Si A no es ineludible, las semanas 4–8 se usan para buffer y para ejecutar lo que B y D te estén mostrando.

---

## Veredicto final

### Haz ahora:
1. **B**
2. **D**

### No hagas ahora:
3. **A completa**
4. **C**

### Si A es ineludible:
Haz solo un **gate de decisión** de 1–2 semanas, no una reescritura.

La regla del trimestre es simple:

> Primero recupera lo que se te está fugando.  
> Luego genera demanda.  
> No empieces la reforma de la casa mientras la puerta principal se está rompiendo.