# Seed 2.0 Code — business_audit/roadmap_restriccion_capacidad

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 8.52 | quality: 10.0
- latency_total: 33.782s | tokens_per_second: 60.6
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


El usuario es un fundador solo, 6h/día totales, 2h en soporte/operaciones indelegables → 4h/día de construcción, 8 semanas de trimestre (ojo: 8 semanas = 40 días hábiles si es 5d/semana, pero mejor calcular por esfuerzo en semanas DE SU TIEMPO CONSTRUIDO: su "semana de construcción" es 4h/día *5d = 20h/semana. Ahora, hay que cruzar priorización por:

1. Capacidad real: Tiene 8 semanas DE CONSTRUCCIÓN? No: 8 semanas calendario, cada una le da 4h/día *5 = 20h semanales de construcción. Ahora, los esfuerzos de las iniciativas están en "tiempo completo"? O en su tiempo? Ojo, el usuario dice los esfuerzos como:
- A: ~3 meses TIEMPO COMPLETO → ¿cuánto es eso en su tiempo? Un mes tiempo completo es ~160h (40h/sem*4), 3 meses = 480h. Su capacidad de construcción por trimestre: 8 sem * 20h = 160h TOTALES. Así que A ES IMPOSIBLE AHORA, no entra ni de lejos.
- B: ~1 semana → ¿es semana de su tiempo? O tiempo completo? El usuario es fundador solo, así que probablemente cuando dice B es ~1 semana de SU TRABAJO (porque es arreglar flujo de alta, pequeño). Pero hay que confirmar por capacidad.
- C: ~3 semanas, DEPENDE DE A → como A no se hace, C se va por el momento.
- D: ~2 semanas, de su tiempo.

Pero además, priorización por VALOR vs ESFUERZO, y RIESGO, y DEPENDENCIAS, y CAPACIDAD REAL (no ideal).

Primero, calcular CAPACIDAD TOTAL DE CONSTRUCCIÓN DEL TRIMESTRE:
- 8 semanas calendario = 40 días hábiles (asumiendo 5d/semana, si es 6d ajustar, pero estándar 5)
- 4h/día de construcción → 40*4=160 HORAS TOTALES DE CONSTRUCCIÓN EN EL TRIMESTRE.

Ahora, traducir CADA INICIATIVA A HORAS (asumiendo que los esfuerzos que dice el usuario son en TIEMPO COMPLETO, salvo que diga lo contrario; o si son en su tiempo, pero mejor clarificar):
- A: 3 meses TIEMPO COMPLETO → 3*4 semanas =12 semanas *40h/sem=480 HORAS. ES MÁS DEL TRIPLE DE SU CAPACIDAD TOTAL DEL TRIMESTRE. NO SE PUEDE HACER AHORA, ni siquiera empezar de forma significativa.
- B: ~1 semana. Si es TIEMPO COMPLETO, 40h. Si es SU TIEMPO (4h/día*5=20h), 20h. En cualquier caso, PEQUEÑO ESFUERZO.
- C: ~3 semanas TIEMPO COMPLETO =120h, PERO DEPENDE DE A. Como A no se hace, C no se puede hacer AHORA (salvo que se pueda desacoplar? Pero el usuario dice que depende de A, así que asumimos que sí).
- D: ~2 semanas. Si tiempo completo:80h. Si su tiempo:40h.

AHORA, PRIORIZACIÓN POR MARCO RICE o VALOR/ESFUERZO, PERO AJUSTADO A FUNDADOR SOLO (lo más importante es: CERRAR CICLOS RÁPIDOS, GENERAR INGRESOS/RETENCIÓN PRONTO, NO EMPEZAR PROYECTOS LARGOS QUE NO ENTREGUEN VALOR EN EL TRIMESTRE).

Puntos clave del usuario:
- No puede delegar soporte/operaciones (2h/día) → capacidad de construcción FIJA: 4h/día = 20h/sem = 160h/trimestre.
- Objetivo del trimestre: ¿qué es lo que le va a dar más valor RÁPIDO, SIN DEPENDER DE PROYECTOS LARGOS?
- B es arreglar flujo de alta que pierde 60% en paso 2: eso es DIRECTAMENTE AUMENTAR ADQUISICIÓN/CONVERSIÓN A USUARIOS PAGOS (o al menos a usuarios activos), lo que genera ingresos más rápido, lo que le permite tal vez delegar soporte después. Es un "quick win" de ALTO IMPACTO, BAJO ESFUERZO.
- D es contenido: impacto medio, esfuerzo medio. Pero el contenido genera tráfico a largo plazo, pero no es tan inmediato como B. Pero ¿tiene capacidad después de B?
- A: NO SE PUEDE HACER AHORA. Es un proyecto de "deuda técnica" o "mejora de plataforma" que requiere 3x su capacidad total del trimestre. Además, los proyectos de reescritura SON RIESGOSÍSIMOS para fundadores solo: te quedas sin entregar valor al cliente durante meses, pierdes tracción, te olvidan los usuarios. NUNCA reescribas como fundador solo a menos que la plataforma esté MUERTA, y aquí dice que hay soporte diario, así que está funcionando.
- C: DEPENDE DE A, así que si A no se hace, C no se hace AHORA. Pero ¿podría desacoplar C? El usuario dice que depende de A, así que asumimos que no (por ejemplo, el panel de métricas necesita el nuevo framework para acceder a datos de forma escalable, etc.)

AHORA, CALCULAR EL ORDEN Y LA EJECUCIÓN EN EL TRIMESTRE (8 semanas = 40 días hábiles = 160h de construcción):

Paso 1: PRIMERO HACER B (ARREGLAR FLUJO DE ALTA)
- Esfuerzo: el usuario dice ~1 semana. Si es su tiempo (20h = 5 días *4h/día), lo hace en la PRIMERA SEMANA DEL TRIMESTRE.
- Por qué? Porque cada día que pasa sin arreglarlo, pierde 60% de los usuarios que llegan al paso 2. Si arreglaslo, por ejemplo, reduces la pérdida a 20%, eso es un aumento del 100% en usuarios que completan el alta (de 40% a 80%). Eso genera más usuarios, más soporte? Wait, no: el usuario ya tiene 2h/día de soporte indelegable, pero más usuarios pueden generar más soporte, pero SI ES USUARIOS PAGOS, eso le permite en el futuro delegar. Pero además, el flujo de alta es un cuello de botella DIRECTO en el embudo de adquisición: es el primer paso para que alguien use tu producto, así que sin eso, todo lo demás (contenido, panel de métricas) es inútil, porque la gente no entra.

Paso 2: LUEGO HACER D (GRABAR 10 VIDEOS DE CONTENIDO)
- Esfuerzo: ~2 semanas. Si es su tiempo (40h = 10 días *4h/día), lo hace en las SEMANAS 2 Y 3 DEL TRIMESTRE.
- Por qué? Porque después de arreglar el flujo de alta, necesitas TRAER MÁS GENTE A ESE FLUJO (ya que ahora convertirá más). El contenido es una forma de generar tráfico orgánico, que es sostenible. Además, el esfuerzo es medio, impacto medio, y no depende de nada más.
- Pero ojo: ¿los videos son de contenido de valor para atraer leads, o tutoriales de producto? El usuario dice "contenido", así que asumimos que es para atraer tráfico. Pero si fueran tutoriales de producto, también ayudarían a reducir el soporte (lo que le daría más horas de construcción), pero el usuario dice impacto medio, así que es para atraer.

Paso 3: ¿QUÉ HACER CON EL RESTO DEL TIEMPO?
El trimestre tiene 8 semanas. Hemos usado 1 (B) + 2 (D) = 3 semanas. Quedan 5 SEMANAS (100h de construcción). ¿Qué podemos hacer?
- Primero: NO EMPEZAR A (reescribir framework). Porque requiere 3 meses TIEMPO COMPLETO = 12 semanas, y le quedan 5. Además, los proyectos de reescritura