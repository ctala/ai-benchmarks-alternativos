# Claude Opus 5 — business_audit/auditoria_pnl_error_plantado

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.07 | quality: 10.0
- latency_total: 36.913s | tokens_per_second: 66.7
- input_tokens: 272 | output_tokens: 2461

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

Sumé los costos línea por línea:

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

Los ingresos sí cierran (9.800 + 2.600 = 12.400). El problema está en costos.

**No sé de qué lado está el error**, y eso importa:
- Si el total de 7.400 está mal → tu margen real es otro (ver abajo).
- Si una línea está mal cargada → por ejemplo, si publicidad fueran 2.150 en vez de 3.900, el total de 7.400 sería correcto.

No hay ninguna combinación de líneas que sume exactamente 1.750, así que no es un rubro olvidado en el total: es un error de tipeo o de suma. **Contrastalo contra el extracto bancario antes de seguir.**

## Con los números como están cargados

Margen real: (12.400 − 9.150) / 12.400 = **26,2%**, no 40%.

En dinero: **3.250 de utilidad mensual.**

## La respuesta: no, no da — así planteado

Un sueldo no se paga con el margen porcentual, se paga con los pesos absolutos.

- Utilidad hoy: 3.250
- Contratación: −2.500
- Queda: **750/mes → margen 6%**

Ese sueldo se come el **77% de tu utilidad**. Y 2.500 es el costo si es un contractor con factura. Si es relación de dependencia, sumale cargas sociales, aguinaldo/bonos, licencias de software y equipo: en la mayoría de jurisdicciones el costo real está entre 3.200 y 3.500. **Con eso quedás en pérdida.**

## Dónde sí puede dar

Hay un dato que salta a la vista: **Contenido freelance = 2.600**, casi exactamente el sueldo que querés pagar.

Si la persona que contratás **absorbe ese trabajo**, el costo incremental no es 2.500 — es cerca de cero, y probablemente ganás capacidad. Esa es una decisión completamente distinta y bastante razonable.

La pregunta correcta no es "¿me da el margen?" sino **"¿esta contratación reemplaza gasto existente o se apila encima?"**

## Antes de firmar, verificá tres cosas

1. **Reconciliá los 1.750.** No se decide un compromiso fijo mensual sobre un P&L que no suma.
2. **Mirá 3 a 6 meses, no uno.** Publicidad es 31% de tus ingresos: si ese gasto es lo que sostiene las suscripciones, tu utilidad es más frágil de lo que parece. Necesito ver churn de suscripciones para opinar sobre la estabilidad de los 9.800 recurrentes.
3. **Colchón de caja.** Un sueldo es un costo fijo; tus ingresos no lo son. Sin 3 a 6 meses de sueldo en reserva, la contratación te vuelve dependiente de que ningún mes salga mal.

**Resumen:** como costo adicional, no. Como reemplazo del rubro freelance, probablemente sí — pero recién después de que el P&L cierre.