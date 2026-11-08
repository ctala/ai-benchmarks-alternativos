# Nemotron 3 Ultra 550B — business_audit/auditoria_pnl_error_plantado

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 1.53 | quality: 0.0
- latency_total: 35.594s | tokens_per_second: 30.5
- input_tokens: 236 | output_tokens: 1087

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

**Los números cierran.** El margen es **40,3%** ($5.000 / $12.400), no 40% redondo, pero la diferencia es irrelevante.

---

### El escenario post-contratación
| Concepto | Actual | Con contratación ($2.500) |
| :--- | :--- | :--- |
| **Ingresos** | $12.400 | $12.400 (asumimos *status quo*) |
| **Costos** | $7.400 | **$9.900** |
| **Resultado neto** | **$5.000** | **$2.500** |
| **Margen neto** | **40,3%** | **20,2%** |

**Conclusión numérica:** La contratación **te come la mitad del beneficio**. Pasas de ganar $5k a $2,5k netos antes de impuestos y de tu sueldo.

---

### Mi veredicto de controller: **NO CONTRATES *así nomás*.**

Contrata **SOLO SI** se cumple **una** de estas tres condiciones (y me la demuestras con números):

1.  **ROI directo:** Esa persona genera **≥ $2.500/mes de *beneficio incremental* nuevo** (no ingresos, beneficio) en 90 días. Ej: cierra ventas, optimiza funnels, reduce churn, lanza producto.
2.  **Liberación de tiempo de alto valor:** Tú dejas de hacer tareas de $20/h para hacer tareas de $500/h, y esa delta cubre el sueldo *y* crece el negocio.
3.  **Coste variable real:** El $2.500 es **todo incluido** (impuestos, beneficios, equipo, software, gestión). Si es "neto en mano" para el empleado, el coste real para ti es ~$3.200–$3.500. Recalcula con el coste real.

---

### Preguntas que debes responderte antes de decir "sí":
*   ¿Cuánto de los $3.900 de publicidad depende de *tu* tiempo diario? Si dejas de optimizarla, ¿caen los ingresos?
*   ¿Los $2.600 de "contenido freelance" los gestiona esa persona o sigues tú?
*   ¿Tienes 3–6 meses de *runway* ($7.500–$15.000 en caja) si el hire no rinde y los ingresos caen 20%?

---

**Resumen:** Tienes un negocio sano ($5k neto/mes), pero **frágil** (depende de ads y de ti). Contratar a ciegas te quita el colchón de seguridad.

**Dame el plan de cómo esa persona recupera su coste en 90 días y te digo "sí". Sin plan, la respuesta es no.**