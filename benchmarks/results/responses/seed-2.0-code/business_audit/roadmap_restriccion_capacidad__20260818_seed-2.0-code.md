# Seed 2.0 Code — business_audit/roadmap_restriccion_capacidad

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 36.961s | tokens_per_second: 55.4
- input_tokens: 302 | output_tokens: 2048

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


El usuario es un fundador solo, 6h/día totales, 2h en soporte irrecusable, 4h/día reales de construcción. 8 semanas = 40 días hábiles? Wait, no, 8 semanas son 56 días pero hábiles son 40? Wait no, mejor calcular por semanas de trabajo efectivo para construcción: 4h/día = 0.5 FTE (porque un full time de construcción es 8h, pero él tiene 4h). Wait, primero, CONVERTIR TODOS LOS ESFUERZOS A SU CAPACIDAD REAL, NO A TIEMPO COMPLETO. Ese es el error clave que muchos cometen: los esfuerzos le dicen "a tiempo completo" pero él es 0.5 FTE de construcción (4h/día vs 8h/día full time).

Primero, calcular CAPACIDAD REAL DE CONSTRUCCIÓN EN 8 SEMANAS:
- 8 semanas = 40 días hábiles (asumiendo 5d/semana, sin vacaciones)
- 4h/día de construcción = 40*4 = 160 horas de construcción DISPONIBLES.

Ahora, CONVERTIR CADA INICIATIVA A HORAS DE SU TRABAJO (no tiempo completo):
- A: ~3 meses TIEMPO COMPLETO. Un mes full time = 160h (40h/semana *4), así que 3*160=480h FULL TIME. Pero él es 4h/día = 20h/semana de construcción (4h*5d). Entonces A le tomaría 480h / 20h/semana = 24 SEMANAS. PERO SOLO TIENE 8 SEMANAS. A es IMPOSIBLE en este trimestre, punto. Además, C depende de A, así que C también se pospone, PERO wait, el usuario dijo C depende de A, así que si A no se hace, C no se puede.

Ahora, B: ~1 semana TIEMPO COMPLETO. Full time semana = 40h. Él hace 20h/semana de construcción, así que B le tomaría 40h / 20h/semana = 2 SEMANAS? Wait no, wait: cuando alguien dice "esfuerzo ~1 semana a tiempo completo", es que una persona que trabaje 8h/día 5d lo hace en 1 semana. Él trabaja 4h/día, así que el doble de tiempo: 2 semanas de SU tiempo, o 40h de sus horas de construcción (que coincide con 40h full time).

D: ~2 semanas TIEMPO COMPLETO = 80h full time. Para él: 80h / 20h/semana = 4 SEMANAS, o 80h de sus horas.

Ahora, ver el ORDEN DE PRIORIDAD POR RIESGO, IMPACTO/CAPACIDAD, Y EL "TIEMPO A VALOR" (Time to Value, TTV), que es CRÍTICO para fundadores solo:

1. PRIMERO, DESCARTAR INICIATIVAS IMPOSIBLES O CON TTV MUY LARGO:
   - A: Reescribir framework. Esfuerzo 24 semanas, solo tiene 8. IMPOSIBLE. Además, es un "big bang" que no entrega valor hasta el final, riesgo altísimo (fundadores solo no pueden hacer big bangs, porque si se atascan, no hay valor en meses). También, el usuario dice "impacto alto por velocidad futura", pero los fundadores solo primero necesitan SOBREVIVIR: capturar más clientes HOY, no futuro.
   - C: Depende de A, así que si A no se hace, C se pospone al próximo trimestre (cuando tal vez tenga más capacidad o delegue soporte). PERO wait, ¿preguntar? No, el usuario dijo C depende de A, así que no hay discusión.

2. AHORA, LAS INICIATIVAS POSIBLES: B Y D. Ahora, ORDENAR POR TTV (tiempo para entregar valor) Y IMPACTO/CAPACIDAD:
   - B: Arreglar flujo de alta que pierde 60% en paso 2. IMPACTO ALTO, TTV CORTO (para él, 2 semanas, PERO wait: ¿podría ser incluso más rápido? Porque cuando un fundador solo arregla un flujo de alta que pierde mucho, tal vez no es un cambio de framework, sino un arreglo rápido: quitar un campo innecesario, arreglar un bug de carga, simplificar el paso. Pero el usuario dijo esfuerzo ~1 semana full time, así que para él 2 semanas. Pero el TTV es INMEDIATO: una vez que arregles el flujo, CADA NUEVO CLIENTE que llegue se queda más, así que ingresos inmediatos. Eso es CRÍTICO para un fundador solo, porque los ingresos permiten delegar soporte después, lo que libera más horas.
   - D: Grabar 10 videos de contenido. IMPACTO MEDIO, TTV MEDIO: los videos tardan en ser indexados, en generar tráfico, en convertir. No es valor inmediato. Además, esfuerzo 4 semanas para él.

3. CALCULAR SI CABEN AMBAS EN 8 SEMANAS:
   - B: 2 semanas (40h de sus horas)
   - D: 4 semanas (80h de sus horas)
   - Total horas usadas: 120h. Tiene 160h disponibles. ¿Qué hacer con las 40h restantes (2 semanas)?
     - Opción 1: Hacer un "prototipo rápido" de A? No, porque A es un reescribir completo, prototipo no entrega valor.
     - Opción 2: Mejorar B aún más (ej: testear dos versiones del flujo, medir la tasa de conversión después del arreglo, ajustar)
     - Opción 3: Preparar para delegar soporte (ej: crear una base de conocimientos, automatizar respuestas comunes) para liberar esas 2h/día en el próximo trimestre, lo que le daría 6h/día de construcción, permitiendo empezar A o C.
     - Opción 4: Hacer 2 videos más de D? No, D es medio impacto, mejor enfocarse en lo que genera ingresos inmediatos o libera capacidad.

4. TAMBIÉN, TENER EN CUENTA EL RIESGO DE SOPORTE: el usuario gasta 2h/día en soporte, así que debe dejar un margen de seguridad en su capacidad. Por ejemplo, si dedica 140h en lugar de 160h, deja 20h para imprevistos de soporte.

AHORA, ESTRUCTURAR EL ORDEN DEL TRIMESTRE (8 SEMANAS = 2 MESES, 8 SEMANAS EXACTAS):

PRIMERO, DESCARTAR INICIATIVAS IMPOSIBLES:
- A: No se hace en este trimestre. Esfuerzo 24 semanas (su tiempo), solo tiene 8. Además, es un big bang sin valor intermedio, riesgo mortal para un fundador solo.
- C: Depende de A, así que se pospone al trimestre siguiente (cuando A se empiece, o cuando cambie la dependencia si es posible).

LUEGO, ORDEN DE EJECUCIÓN DE LAS POSIBLES (B Y D), CON MARGEN DE SEGURIDAD:

SEMANAS 1-2: INICIATIVA B (Arreglar flujo de alta)
- Por qué: Impacto ALTO, TTV INMEDIATO. Cada día que pasa con el flujo roto pierdes 60% de los clientes que llegan. Es "dinero en la mesa" que te estás perdiendo.
- ¿Cómo ajustar a su capacidad? Como es 4h/día, dedica TODAS esas 4h/día a B en estas 2 semanas (no a D ni nada más). Al finalizar, medir la tasa de conversión del alta: si pasa de 40% (porque pierde 60%) a 60% o más, es un éxito inmediato.
- Marge de seguridad: Si se atrasa 1 semana (por soporte), tiene margen en las semanas siguientes.

SEMANAS 3-6: INICIATIVA D (Grabar 10 videos de contenido)
- Por qué: Impacto MEDIO, TTV MEDIO, pero después de asegurar los ingresos inmediatos (B), es bueno construir un canal de adquisición a largo plazo.
- ¿