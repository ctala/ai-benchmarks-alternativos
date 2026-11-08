# Kimi K2.6 — business_audit/roadmap_restriccion_capacidad

- model_id: `moonshotai/kimi-k2.6`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 63.929s | tokens_per_second: 71.2
- input_tokens: 304 | output_tokens: 4552

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

 Aquí está tu trimestre, ordenado por capacidad real, no por deseos.

### La cuenta de la vieja
Tienes **8 semanas calendario**. A 4 horas reales de construcción al día, eso son **160 horas**, es decir, **4 semanas de trabajo a tiempo completo**. Eso es todo lo que cabe en el trimestre. El resto es fantasía.

---

### El orden

**1. B — Arreglar el flujo de alta (Semanas 1-2)**  
**2. D — Grabar los 10 videos (Semanas 3-6)**  
**3. Buffer / fixes críticos / deuda técnica menor (Semanas 7-8)**  
**A y C — Al congelador. No entran en este trimestre.**

---

### Por qué

**B es tu única prioridad 0.**  
Pierdes al 60% en el paso 2. Eso no es un "problema de conversión"; es una hemorragia. Todo lo que construyas (incluido el contenido de D) se multiplica por cero si el embudo está roto. Además, es la única iniciativa de "impacto alto" que cabe en tu caja de tiempo. Una semana de esfuerzo a tiempo completo = dos semanas a tu ritmo. Arregla esto primero, mide el nuevo funnel y no pases a otra cosa hasta ver que el paso 2 deja de matar usuarios.

**D es el siguiente porque cabe y desbloquea crecimiento.**  
Dos semanas a tiempo completo = cuatro semanas a tu ritmo. Si haces B primero, te queda tiempo justo para esto. Pero hágelo en bloques: guioniza 3-4 en un día, graba en otro. No alternes código y cámara todos los días; con 4 horas diarias el contexto switching te mata.

**A es una trampa de fundador solitario.**  
"3 meses a tiempo completo" son 6 meses a tu ritmo actual. Eso es más que todo tu año productivo. Si lo empiezas ahora, no entregas nada visible en 8 semanas, el negocio sigue sangrando por el paso 2 y probablemente descubras nuevos problemas a mitad de la reescritura. **No se reescribe sobre un embudo roto.** El framework actual, por feo que sea, solo necesita sobrevivir hasta que tengas ingresos o equipo para pagar la reescritura.

**C está bloqueada y es irrelevante mientras A no exista.**  
Si depende de A, y A no va, C no va. Punto. No gastes ni una hora pensando en ella.

---

### Plan de batalla semana a semana

- **Semanas 1-2:** B. Todo tu tiempo de construcción aquí. Arregla el paso 2, hazlo idiot-proof y mide.
- **Semanas 3-6:** D. 10 videos. Ritmo: 2-3 videos por semana en bloques de producción. Si terminas antes, mejor.
- **Semanas 7-8:** Buffer sagrado. Usa esto para:
  - Bugs que surgieron de B.
  - Pequeñas mejoras de onboarding (emails post-alta, tooltips).
  - Reducir deuda técnica que te quite sueño, pero sin tocar A.
  - Si el soporte/operación creció porque B trajo más usuarios, protege estas horas.

### Regla de oro para este trimestre
**Si no cabe en las 160 horas, no existe.**  
A y C son proyectos Q3 o Q4, y solo si ya tienes validado que el negocio funciona con el embudo arreglado y suficiente ingreso para justificar parar la línea.

Construye el embudo primero. Llena el embudo después. Sobrevive siempre.