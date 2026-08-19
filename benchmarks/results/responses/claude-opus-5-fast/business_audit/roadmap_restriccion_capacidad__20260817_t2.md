# Claude Opus 5 Fast — business_audit/roadmap_restriccion_capacidad

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.01 | quality: 10.0
- latency_total: 19.01s | tokens_per_second: 181.6
- input_tokens: 418 | output_tokens: 3453

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

## Primero, la matemática de capacidad

Esto es lo que decide casi todo:

- 4h/día × 5 días × 8 semanas = **160h brutas**
- Menos imprevistos, soporte que se desborda, un día malo por semana (~25%) = **~120h realmente planificables**

Y ojo con las estimaciones que me diste: están en "semanas ideales a tiempo completo". Traducidas a tu capacidad real:

| | Estimado FT | En tu calendario real | Veredicto |
|---|---|---|---|
| A) Reescritura | ~480h | ~24 semanas | 3× el trimestre. **Fuera.** |
| B) Alta / paso 2 | ~40h | ~2 semanas | Entra |
| C) Panel métricas | ~120h | ~6 semanas + depende de A | **Fuera.** |
| D) 10 videos | ~80h | ~4 semanas | Entra recortado |

B + D completos ya son 120h: consumen el trimestre entero sin un solo hueco de margen. Así que hay que recortar.

## Las tres decisiones difíciles

**A no se hace. Ni empezada.** Una reescritura a medias es lo peor de los dos mundos: mantienes dos sistemas y no entregas nada. Si en la semana 4 llevas el 15% y aparece un incidente, quedas atrapado. Además, "velocidad" es un síntoma, no un diagnóstico. Cambia A por un *spike de rendimiento*: 20h para medir qué es lento de verdad y arreglar los 2 peores puntos en el stack actual. Suele resolver el 70% del dolor por el 4% del costo.

**C está muerta por dependencia, pero la dependencia es sospechosa.** ¿Un panel de lectura de métricas de verdad necesita otro framework? Casi nunca. Y aun sin la dependencia, no la haría: impacto medio y no tienes evidencia de demanda. Válida antes de construir.

**B es lo único no negociable.** Pierdes 60% en el paso 2. Cada usuario que traigas con los videos (D) cae en ese mismo agujero. Hacer D antes que B es pagar por llenar un balde roto. B primero cambia el retorno de todo lo demás.

## El trimestre

| Semana | Foco | Entregable concreto |
|---|---|---|
| 1 | B – diagnóstico + primer fix | Instrumentar paso 2, ver 10 grabaciones de sesión, hablar con 5 que abandonaron. Shipear el fix más obvio. |
| 2 | B – shipear y medir | Fix en producción. Empieza la ventana de medición. |
| 3 | B – segunda iteración | Casi nunca se arregla un 60% de un tirón. Aquí atacas la segunda causa. **Meta: bajar de 60% a <35%.** |
| 4 | Spike de rendimiento (sustituto de A) | Medir los 3 endpoints/pantallas más lentos. Arreglar 2. Escribir una nota de una página: ¿esto justifica una reescritura o no? |
| 5–6 | D recortado: **4 videos, no 10** | 4 videos sobre el problema que resuelve tu producto, publicados. |
| 7 | C validada sin construir | Enviar a mano un reporte de métricas por email a 10 clientes. Ver quién lo abre, responde o pide más. |
| 8 | Buffer + cierre | Reservada. Si algo se atrasó (se va a atrasar), aquí se absorbe. Si no, mides y planeas el próximo trimestre. |

Reparto: B ~50h · spike ~20h · D ~30h · validación C ~10h · buffer ~10h.

## Por qué 4 videos y no 10

10 videos es un lote arbitrario. 4 te dan la misma señal sobre si el canal funciona, a la mitad del costo. Si dos de esos cuatro traen tráfico real, el trimestre que viene grabas 10 con evidencia. Si ninguno mueve nada, te ahorraste 40h.

## Qué cambiaría este orden

- **Si el spike de la semana 4 revela un cuello estructural real** (no lentitud molesta, sino algo que te bloquea vender o rompe con carga): A vuelve a la mesa para el próximo trimestre, pero como migración por partes, nunca como big bang.
- **Si en la semana 7 los 10 clientes piden el reporte manual**: C sube a prioridad 1 del próximo trimestre, construida en el stack actual.
- **Si B baja el abandono por debajo del 25% en la semana 3**: liberas ~15h. Mételas en reducir tus 2h/día de soporte, no en adelantar D. Eso compone.

## La pregunta que te devuelvo

Esas 2h/día de soporte son 80h del trimestre — más de lo que le vas a dedicar a B. ¿Cuáles son los 3 motivos que generan la mayoría de esos tickets? Si uno de ellos es "la gente se atasca en el alta", entonces B te devuelve capacidad además de conversión, y es todavía más obvia como primera pieza.