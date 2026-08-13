# Claude Opus 5 — business_audit/auditoria_pnl_error_plantado

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 29.326s | tokens_per_second: 69.8
- input_tokens: 272 | output_tokens: 2048

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

Los ingresos sí cierran (9.800 + 2.600 = 12.400). El problema está en el total de costos.

**Y el 40% sale de ahí.** Con costos de 7.400 el beneficio es 5.000 → 40,3%. Con los costos reales:

- Beneficio real: 12.400 − 9.150 = **3.250**
- Margen real: **26,2%**, no 40%

Antes de seguir necesitás encontrar esos 1.750: o hay una línea de costo que no está en la lista, o el total se arrastró mal de un mes anterior. No es un detalle: es el 14% de tu facturación.

## Con el margen real, la respuesta cambia

**Escenario A — el contratado es una suma (rol nuevo):**

$2.500 no son $2.500. Según tu jurisdicción y modalidad, cargas sociales, aguinaldo y provisiones suelen agregar 20–40%: costo real **$3.000–3.400/mes**.

- Beneficio: 3.250 → entre **250 y −150**
- Margen: 26,2% → **~2% o negativo**

Eso no es contratar, es transferir tu empresa a un empleado. Y una sola caída en cursos sueltos (línea claramente no recurrente) te deja pagando sueldo de tu bolsillo.

**Escenario B — el contratado reemplaza el freelance ($2.600):**

Acá el número casi funciona: cambiás 2.600 variables por 3.000–3.400 fijos. Costo incremental neto: **$400–800/mes**. Beneficio queda en ~2.500–2.850, margen ~20%.

Pero cambiás flexibilidad por rigidez. Si el mes viene flojo, al freelance no lo llamás; al empleado le pagás igual.

## Tres cosas que faltan y son decisivas

1. **¿Vos estás cobrando algo?** No veo compensación del dueño. Si esos 3.250 son tu ingreso personal, el escenario A lo reduce a cero.
2. **Publicidad = 3.900 = 31% de ingresos.** Es tu segundo costo más grande y el más frágil. ¿Cuántas suscripciones nuevas trajo? Sin ese dato no sé si tu negocio es rentable o si estás comprando ingresos a pérdida.
3. **Un mes no es una tendencia.** Necesito 3–6 meses, y ver churn de