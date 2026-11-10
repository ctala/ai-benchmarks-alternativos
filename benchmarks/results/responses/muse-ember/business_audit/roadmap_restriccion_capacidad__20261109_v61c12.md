# Muse Ember — business_audit/roadmap_restriccion_capacidad

- model_id: `meta/muse-ember`
- success: True  | final: 9.01 | quality: 10.0
- latency_total: 7.224s | tokens_per_second: 427.8
- input_tokens: 265 | output_tokens: 3090

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

Con tu capacidad real, no caben 4 iniciativas. Caben 2, y una de las otras dos es una trampa.

### La matemática primero

Tú no tienes 6h/día para construir. Tienes **4h/día**.

En 8 semanas (5 días/semana) son **160h reales** de construcción, no 240h.

Recalculemos tus estimaciones "a tiempo completo" - asumiendo 6h enfocadas/día:

**A) Rewrite: ~3 meses FT = ~360h**
A 4h/día son **~18 semanas de calendario**. Ni siquiera cabe en el trimestre completo aunque no hicieras nada más. Si lo empiezas, cierras el trimestre con 0 entregado y la plataforma a medias.

**B) Flujo de alta: ~1 semana FT = ~30h**
A 4h/día son **1,5 semanas reales**. Cabe.

**C) Panel de métricas: ~3 semanas FT = ~90h**
A 4h/día son **4,5 semanas reales**, *más* depende de A. Como A no se termina, C está bloqueada todo el trimestre.

**D) 10 videos: ~2 semanas FT = ~60h**
A 4h/día son **3 semanas reales**. Cabe.

B + D = 90h. Te quedan 70h de colchón en 8 semanas. Para una persona sola, eso no es holgura, es obligatorio.

### Tu orden para el trimestre

**1. B - Arreglar el alta. Semanas 1-2 (con buffer hasta mitad de la 3)**
Es lo primero por multiplicación, no solo por esfuerzo.

Hoy pierdes al 60% en el paso 2. Todo lo que hagas después - videos, métricas, features - pierde el 60% de su valor antes de empezar. Si arreglar esto duplica la conversión, acabas de duplicar el retorno de D sin gastar más.

Hazlo, lánzalo pequeño y mide el lift antes de pasar a otra cosa.

**2. D - Grabar los 10 videos. Semanas 3 a 5**
Solo después de B. Grabar antes sería pagar por tráfico que luego tiras en el paso 2.

Bonus para ti: graba pensando también en soporte. Si esos videos responden las dudas que te comen 2h/día, te pueden devolver capacidad para el próximo trimestre.

**3. Semanas 6 a 8: Nada grande nuevo.**
No rellenes el calendario al 100%. Usa este tiempo para:
1. Medir si B funcionó e iterar
2. Recoger feedback de los usuarios que traigan los videos
3. Atacar esas 2h/día de soporte (FAQ, plantillas, automatizaciones) - es tu mayor palanca de capacidad futura
4. Decidir con datos si A merece la pena el *próximo* trimestre

### Qué NO hacer este trimestre

**A) No lo empieces.**
Impacto alto a 3 meses no es impacto este trimestre. Un rewrite sin terminar no acelera nada, no arregla el alta y te deja sin nada que enseñar al cierre. Aparcado hasta que B esté validado. Y antes de retomarlo, hay que validar si necesitas un rewrite entero o un refactor incremental.

**C) Fuera.**
Impacto medio + bloqueado por A = imposible. No intentes "hacer una versión pequeña mientras" o te comerá las 4,5 semanas que necesitas para B y D.

**Resumen: B > D >> A = C = 0 este trimestre.**

Si empiezas por A, tu trimestre es: plataforma rota, sin usuarios nuevos, sin nada entregado.