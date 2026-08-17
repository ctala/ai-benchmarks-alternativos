# Claude Opus 5 Fast — business_audit/auditoria_pnl_error_plantado

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.21 | quality: 10.0
- latency_total: 9.445s | tokens_per_second: 193.2
- input_tokens: 272 | output_tokens: 1825

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

La suma de costos está mal. Sumando las líneas que listaste:

| Concepto | Monto |
|---|---|
| Infraestructura | $1.250 |
| Publicidad | $3.900 |
| Herramientas SaaS | $780 |
| Procesador de pagos | $620 |
| Contenido freelance | $2.600 |
| **Total real** | **$9.150** |

Declaraste $7.400. Hay **$1.750 sin contabilizar**. Los ingresos sí cierran correctamente ($9.800 + $2.600 = $12.400).

## El margen real

- **Con tu cálculo:** $12.400 − $7.400 = $5.000 → 40%
- **Real:** $12.400 − $9.150 = **$3.250 → 26,2%**

Tu 40% es internamente consistente con el total equivocado, así que probablemente arrastraste el error desde la planilla, no lo calculaste aparte. Vale la pena encontrar de dónde salieron esos $1.750 antes de seguir: o falta una línea de costo en tu resumen, o el total está mal tipeado.

## Qué implica para la contratación

Contratando a $2.500/mes contra un excedente real de $3.250:

**Quedan $750/mes. Margen del 6%.**

Y eso asumiendo que $2.500 es el costo total. Si es relación de dependencia, hay que sumar cargas sociales, aguinaldo, vacaciones — según jurisdicción eso puede llevar el costo real a $3.250–$3.750/mes, lo que te pone **en pérdida**. Si es contractor, $2.500 puede ser el número final.

## La pregunta que cambia todo

**¿Esta persona reemplaza los $2.600 de contenido freelance?**

- **Si sí:** el costo incremental neto es prácticamente cero (−$100/mes) y probablemente ganás capacidad y consistencia. La decisión pasa a ser buena, siempre que el costo laboral cargado no exceda mucho los $2.500.
- **Si no, es capacidad adicional:** estás apostando $2.500/mes de un colchón de $3.250 sin haber definido qué ingreso incremental tiene que generar.

## Mi recomendación

**No con los números como están.** No porque el negocio no dé, sino porque tomarías la decisión sobre un margen que creés que es 40% y en realidad es 26%.

Antes de contratar:

1. **Resolvé los $1.750.** Es la diferencia entre "me sobra cómodo" y "voy justo".
2. **Definí si reemplaza o suma** al freelance de contenido. Cambia la respuesta por completo.
3. **Pedí el costo laboral cargado real**, no el bruto.
4. **Un mes no es tendencia.** Publicidad en 31% de ingresos es alta — si ese gasto es el que sostiene las suscripciones, tu margen es más frágil de lo que parece. Mirá los últimos 3–6 meses antes de asumir un costo fijo.
5. **Verificá tu colchón de caja.** Un contrato de $2.500/mes es un compromiso que no se apaga con un clic si cae un mes.

Si al revisar resulta que la persona reemplaza el freelance y el margen real se sostiene en 26% varios meses, la contratación tiene sentido. Con la foto actual, no la haría todavía.