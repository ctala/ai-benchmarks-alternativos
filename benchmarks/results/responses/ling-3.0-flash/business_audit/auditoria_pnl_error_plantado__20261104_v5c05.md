# Ling 3.0 Flash — business_audit/auditoria_pnl_error_plantado

- model_id: `inclusionai/ling-3.0-flash`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 42.957s | tokens_per_second: 41.5
- input_tokens: 249 | output_tokens: 1784

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

## ⚠️ Primero: los números no cierran

Antes de opinar, tengo que señalar la inconsistencia:

**La suma de tus costos listados es $9.150, no $7.400.**

| Concepto | Monto |
|---|---|
| Infraestructura | $1.250 |
| Publicidad | $3.900 |
| Herramientas SaaS | $780 |
| Procesador de pagos | $620 |
| Contenido freelance | $2.600 |
| **Suma real** | **$9.150** |
| **Total que reportas** | **$7.400** |
| **Diferencia** | **$1.750** |

Con los costos reales de $9.150, tu margen es **26,2%**, no 40%.

> $12.400 − $9.150 = $3.250 → $3.250 / $12.400 = **26,2%**

---

## Ahora, el análisis con los números corregidos

Con margen real del 26,2% y ganancia neta de **$3.250/mes**:

| | Monto |
|---|---|
| Ganancia neta actual | $3.250 |
| Costo de contratación | $2.500 |
| **Sobrante** | **$750** |

### Mi recomendación: **No contrates todavía.**

**Razones:**

1. **El colchón es de solo $750/mes** (23% de tu utilidad actual). Cualquier imprevisto —una subida de tarifas, una devolución, una campaña que baje— te pone en rojo.

2. **No está claro que el contratado reemplace el $2.600 de contenido freelance.** Si lo hace, tu costos bajan $2.600 y el nuevo costo neto es solo $2.500 → ahí sí tendrías un ahorro de $100. Pero eso habría que confirmarlo.

3. **Faltan costos del empleado:** cargas sociales, seguridad social, posibles beneficios. El costo real de un empleado de $2.500 suele ser entre $2.800–$3.200 dependiendo de tu país. Eso ya rompe completamente el presupuesto.

### Lo que sí haría:
- **Corre el número** de costos y confirma si $7.400 o $9.150 es el real.
- **Define si el contratado reemplaza** el trabajo freelance de $2.600.
- **Calcula el costo total del empleado** (no solo el salario).
- Si al final el costo neto nuevo queda por debajo de tu utilidad actual, podrías avanzar —pero con un colchón de emergencia de al menos 2-3 meses de gastos operativos.