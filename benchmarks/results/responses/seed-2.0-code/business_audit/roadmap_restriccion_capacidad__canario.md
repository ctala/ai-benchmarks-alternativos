# Seed 2.0 Code — business_audit/roadmap_restriccion_capacidad

- model_id: `bytedance-seed/seed-2.0-code`
- success: True  | final: 6.97 | quality: 8.0
- latency_total: 42.038s | tokens_per_second: 48.7
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


El usuario es fundador solo, con recursos MUY limitados: 4h/día de construcción, 8 semanas de trimestre (ojo, 8 semanas = ~40 días hábiles, PERO con 4h/día = 160 horas de construcción TOTALES, no más). Primero tengo que alinear cada iniciativa con su CAPACIDAD REAL, no con el esfuerzo "a tiempo completo" (porque el esfuerzo de A es 3 meses A TIEMPO COMPLETO, pero él tiene 4h/día, así que 3 meses TC = ~60 días TC = ~240h, que es MÁS que sus 160h totales del trimestre. Eso es clave: no usar esfuerzo TC, convertirlo a su capacidad.

Primero, calcular su capacidad total del trimestre:
- 8 semanas = asumo 5 días hábiles/semana = 40 días
- 4h/día de construcción = 40*4 = 160 HORAS TOTALES de trabajo de construcción en el trimestre.

Ahora, convertir cada iniciativa de "esfuerzo a tiempo completo" a HORAS DE SU TRABAJO (porque tiempo completo = 8h/día, así que su esfuerzo es el DOBLE del esfuerzo TC? Wait no: si algo tarda 1 semana TC (8h/día, 5 días = 40h TC), para él que trabaja 4h/día, tarda 2 semanas (porque 40h / 4h/día = 10 días = 2 semanas). OJO, el usuario probablemente dio los esfuerzos en "tiempo completo", pero él tiene mitad de horas diarias, así que hay que ajustar.

Wait, el usuario dijo:
- A: ~3 meses a tiempo completo. Tiempo completo = 4 semanas/mes = 12 semanas = 60 días = 480h TC. Para él, 480h / 4h/día = 120 días = 24 semanas, que es MÁS que las 8 semanas del trimestre. IMPOSIBLE hacer A en el trimestre.

- B: ~1 semana TC = 5 días *8h =40h TC. Para él: 40h /4h/día=10 días=2 semanas (pero wait, el usuario dijo "esfuerzo ~1 semana"—tal vez él lo medía en su propio tiempo? Wait no, mejor aclarar, pero primero confirmar: el usuario es solo, así que cuando dice "esfuerzo X", ¿es su esfuerzo o TC? El caso A dice "3 meses a tiempo completo", así que los demás son probablemente TC? Wait A especifica TC, los demás no. Oh, el usuario: A dice "~3 meses a tiempo completo", B: "~1 semana", C: "~3 semanas", D: "~2 semanas". Probablemente, A es TC, los demás son esfuerzo EN SU TIEMPO? No, mejor suponer que A es TC, y los demás son esfuerzo medido en "tiempo de trabajo de construcción" de él? Wait no, vamos a leer de nuevo el contexto del usuario:

Usuario:
- Tiene 6h/día enfocado, 2h en soporte/operación NO delegables → 4h/día CONSTRUCCIÓN.
- 8 semanas hasta cierre trimestre.
- Iniciativas:
  A) Reescribir framework: IMPACTO ALTO, ESFUERZO ~3 MESES A TIEMPO COMPLETO (especifica TC)
  B) Arreglar flujo alta: PIERDE 60% EN PASO 2 → IMPACTO ALTO, ESFUERZO ~1 SEMANA (no especifica TC, así que es SU esfuerzo? O TC? Wait, A es TC, los demás son probablemente esfuerzo en su propio tiempo, pero vamos a calcular capacidad REAL:

Capacidad de CONSTRUCCIÓN en el trimestre:
8 semanas = 5 días/semana = 40 días. 4h/día = 160 HORAS TOTALES de construcción. No más. No hay margen para imprevistos (soporte puede crecer, así que debemos dejar un colchón del 15-20% = ~32h, así que capacidad UTIL = ~128h).

Ahora, convertir ESFUERZOS a HORAS, usando la referencia de A:
A) 3 meses TC = 12 semanas TC = 60 días TC *8h/día = 480h TC. Para él, 480h TC = 960h de su trabajo? No, wait: Tiempo Completo es 8h/día. Él trabaja 4h/día de construcción, así que su "velocidad" es la MITAD de un trabajador TC. Así que:
- Esfuerzo TC → esfuerzo SUYO = esfuerzo TC * 2 (porque le toma el doble de días, o el doble de horas, para hacer lo que un TC hace en X)
Pero A es 3 meses TC → suyo = 6 meses. MÁS QUE 8 SEMANAS. IMPOSIBLE HACER A EN EL TRIMESTRE. Incluso empezar A no tiene sentido, porque no lo termina, y el impacto de A es FUTURO, no inmediato. Además, C depende de A → si no hacemos A, no hacemos C (porque C depende de A terminado, y A no se termina en el trimestre).

Ahora, las otras iniciativas: B, D (C se descarta por depender de A, que no se hace).

Primero, VALORACIÓN de cada iniciativa por:
1. IMPACTO INMEDIATO (porque es fundador solo, necesita cash/crecimiento RÁPIDO, no futuro):
   - B: Arreglar flujo de alta que pierde 60% en paso 2. Eso es CONVERSIÓN DIRECTA. Si hoy entra 100 personas, pasan 40. Si arreglas el paso 2, digamos que pasan 80 (doble), o al menos 60. Eso es CRECIMIENTO INMEDIATO, ingresos inmediatos si el alta es de pago o de usuario activo que monetiza. IMPACTO ALTO, INMEDIATO.
   - D: Grabar 10 videos. Impacto MEDIO, ya que el contenido de video tiene retardo en resultados (SEO, tráfico orgánico, confianza, pero no inmediato).
   - A: Impacto ALTO PERO FUTURO, no inmediato, y no se termina en el trimestre.
   - C: Depende de A, no se hace.

2. ESFUERZO AJUSTADO A SU CAPACIDAD:
   El usuario dijo B: ~1 semana. Si es su propio tiempo (4h/día), 1 semana = 5 días *4h =20h. D: ~2 semanas = 40h. Total de B + D =60h, lo que entra en su capacidad UTIL de 128h, y deja mucho colchón para imprevistos (soporte puede crecer, errores en B, etc.).

Pero wait, ¿el usuario dijo que C depende de A? Sí, explícitamente: "Depende de que A esté terminado". Así que si A no se hace (no se puede), C se descarta completamente.

Ahora, ORDEN: ¿por qué B PRIMERO, luego D, y A Y C FUERA DEL TRIMESTRE?

Razones clave que el usuario (fundador solo) necesita entender:
- CAPACIDAD REAL: A es 3 meses TC = 6 meses de su trabajo (porque 4h/día vs 8h/día TC). No lo puede empezar y terminar en 8 semanas, y empezarlo no tiene sentido porque no va a ver retorno en el trimestre, y le quita recursos a iniciativas de retorno inmediato.
- RETORNO INMEDIATO: B es el único que impacta directamente la conversión de alta, que es el embudo PRINCIPAL. Perder 60% en paso 2 es una filtración masiva: si gastas tiempo o dinero en traer tráfico, se va por ahí. Arreglarlo es "dinero en la mesa" que no estás cogiendo.
- COLCHÓN DE IMPREVISTOS: El usuario ya gasta 2h/día en soporte NO delegable. Ese tiempo puede crecer (si hay más usuarios por el arreglo de B, por ejemplo). Así que no podemos llenar toda su capacidad, debemos dejar margen.
- C DEPENDE DE A: No se hace, punto.
- D: Impacto medio, pero a largo plazo, y su esfuerzo es bajo. Después de arreglar B