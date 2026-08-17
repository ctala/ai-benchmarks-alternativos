# Claude Opus 5 Fast — business_audit/auditoria_pnl_error_plantado

- model_id: `anthropic/claude-opus-5-fast`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 9.833s | tokens_per_second: 194.5
- input_tokens: 272 | output_tokens: 1913

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

Sumé las partidas de costos línea por línea:

| Concepto | Monto |
|---|---|
| Infraestructura | 1.250 |
| Publicidad | 3.900 |
| Herramientas SaaS | 780 |
| Procesador de pagos | 620 |
| Contenido freelance | 2.600 |
| **Suma real** | **9.150** |
| Total declarado | 7.400 |
| **Diferencia** | **1.750** |

El "Total costos: $7.400" no corresponde a las partidas listadas. Y el margen del 40% sí es coherente con ese 7.400 erróneo (12.400 − 7.400 = 5.000 → 40,3%), así que el error se arrastró al indicador.

**Números reales:**
- Beneficio: 12.400 − 9.150 = **$3.250**
- Margen: **26,2%**, no 40%

Antes de seguir, necesitás encontrar esos $1.750: o falta una partida, o hay un monto mal cargado, o la suma se hizo mal. No es un detalle menor: es el 14% de tu facturación.

## Segundo: la respuesta depende de una pregunta que no hiciste

**Si la contratación es adicional** (se suma a los $2.600 de freelance):

3.250 − 2.500 = **$750/mes**. Margen del 6%. Un mes flojo de conversión y estás en rojo. No da.

**Si la persona reemplaza el contenido freelance:**

3.250 + 2.600 − 2.500 = **$3.350/mes**. Prácticamente neutro, incluso levemente positivo. Ahí sí da — y además convertís gasto variable en capacidad propia.

## Tercero: dos cosas que faltan en el resumen

**No veo tu sueldo.** Si no te estás pagando, esos $3.250 *son* tu ingreso. Contratar en modo aditivo te deja con $750 para vos. Eso no es una decisión de negocio, es un recorte del 77% a tu propio sueldo.

**$2.500 no es el costo real.** Según la figura contractual, sumá cargas, herramientas, y 1-2 meses de rampa antes de que la persona produzca. Presupuestá entre $2.750 y $3.200 efectivos.

## Mi lectura

**No contrates todavía.** No porque el negocio no aguante, sino porque estás decidiendo sobre un margen inflado 14 puntos.

Orden de trabajo:

1. Reconciliá los $1.750. Sin eso, cualquier decisión es a ciegas.
2. Definí si el rol reemplaza el freelance o se suma. Es la variable que decide.
3. Mirá 3 meses, no uno. Con $3.900 de publicidad (31% de ingresos) tu facturación depende de campañas; un mes no te dice si $12.400 es el piso o el techo.
4. Confirmá que tenés 3-4 meses del costo del contratado en caja antes de firmar.

Si al reconciliar aparece que el margen real es mejor, o si el rol absorbe el freelance, la contratación se sostiene. Pasame los números corregidos y lo reviso.