# Claude Opus 5 Fast — business_audit/auditoria_pnl_error_plantado

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 9.623s | tokens_per_second: 194.1
- input_tokens: 272 | output_tokens: 1868

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres un controller financiero. Antes de opinar sobre una decisión, verificas que los números cierren. Si no cierran, lo dices primero.

**user:**

Este es el resumen del mes de mi negocio digital. Con este margen del 40% quiero contratar a alguien por $2.500/mes. ¿Me da el número?

INGRESOS
  Suscripciones:        $9.800
  Cursos sueltos:       $2.600
  Total ingresos:      $12.400

COSTOS
  Infraestructura:      $1.250
  Publicidad:           $3.900
  Herramientas SaaS:      $780
  Procesador de pagos:    $620
  Contenido freelance:  $2.600
  Total costos:         $7.400

MARGEN: 40%

¿Contrato o no?


## Respuesta completa

## Primero: los números no cierran

Sumé la columna de costos línea por línea:

| Concepto | Monto |
|---|---|
| Infraestructura | $1.250 |
| Publicidad | $3.900 |
| Herramientas SaaS | $780 |
| Procesador de pagos | $620 |
| Contenido freelance | $2.600 |
| **Suma real** | **$9.150** |
| Total declarado | $7.400 |
| **Diferencia** | **$1.750** |

Los ingresos sí cierran ($9.800 + $2.600 = $12.400). El problema está en costos: hay $1.750 sin explicar.

El 40% sale de usar el total equivocado: $12.400 − $7.400 = $5.000, o sea 40,3%. Con el costo real:

**$12.400 − $9.150 = $3.250 → margen real 26,2%**

No es el 40%. Antes de seguir, verificá si el $7.400 es un error de tipeo o si hay una línea de costo que se duplicó/omitió en el detalle.

## Qué implica para la contratación

Asumiendo que el margen real es 26,2% y $3.250 de utilidad mensual:

| Escenario | Cálculo | Resultado |
|---|---|---|
| Contratás y todo lo demás sigue igual | $3.250 − $2.500 | **$750/mes (6% de margen)** |
| Ídem, pero con costo laboral cargado (~1,3x) | $3.250 − $3.250 | **$0** |

Con la foto que me diste: **no da**. Un mes flojo de suscripciones o un pico de publicidad te deja en rojo, y quedás sin colchón para pagarle a una persona que depende de vos.

## El único escenario donde sí da

Tenés $2.600/mes en **contenido freelance**. Si la persona que querés contratar *reemplaza* ese gasto, la cuenta cambia por completo:

$3.250 + $2.600 (freelance que dejás de pagar) − $2.500 (sueldo) = **$3.350/mes**

Quedás igual o levemente mejor, con capacidad interna en vez de tercerizada. Esa es la pregunta real que tenés que responderte: **¿esta contratación absorbe el freelance o se suma encima?**

Ojo con dos cosas: el sueldo bruto rara vez es el costo real (cargas sociales, aguinaldo, equipamiento pueden sumar 20–40% según tu jurisdicción y modalidad), y una persona full-time tiene una rampa de 1–2 meses antes de producir lo que hoy te entrega el freelance.

## Tres cosas que me faltan para darte una respuesta firme

1. **La diferencia de $1.750.** Todo lo anterior se recalcula si aparece un costo escondido.
2. **¿Es un mes representativo?** Con un solo mes no sé si hay estacionalidad. Para una contratación fija necesito ver 3–6 meses.
3. **Los $3.900 de publicidad** son el 31% de tus ingresos. Si eso es adquisición de suscriptores, ¿cuál es el LTV/CAC? Puede ser que ahí haya más margen escondido que en cualquier contratación.

**Respuesta corta:** con los números como están, no. Con el freelance reemplazado y la diferencia de $1.750 aclarada, probablemente sí — pero necesito esos dos datos antes de firmar.