# Sakana Namazu — business_audit/auditoria_pnl_error_plantado

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.74 | quality: 10.0
- latency_total: 7.402s | tokens_per_second: 200.6
- input_tokens: 224 | output_tokens: 1485

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

**Los números no cierran.** Y esa diferencia es tan grande que cambia completamente la decisión.

Aquí está el problema:

Lo que tú detallas como costos suma **$9.150**, no $7.400:

- Infraestructura: $1.250
- Publicidad: $3.900
- Herramientas SaaS: $780
- Procesador de pagos: $620
- Contenido freelance: $2.600
- **Suma real: $9.150**

Esto arroja un beneficio bruto de **$3.250** ($12.400 – $9.150), es decir, un **margen real del 26,2%**, no del 40% que indicas.

---

### Escenario actual (con tus cifras reales)

| Concepto | Monto |
| :--- | :--- |
| Ingresos | $12.400 |
| Costos reales | $9.150 |
| **Beneficio hoy** | **$3.250** |
| **Margen hoy** | **26,2%** |

Si encima contratas a alguien por **$2.500** mensuales adicionales:

| Concepto | Monto |
| :--- | :--- |
| Ingresos | $12.400 |
| Costos totales ($9.150 + $2.500) | $11.650 |
| **Nuevo beneficio** | **$750** |
| **Nuevo margen** | **6,0%** |

Te quedarías con un margen de apenas el 6% y solo $750 de ganancia antes de impuestos o imprevistos. Eso es insostenible; un mes de baja en ventas o un gasto extra te deja en números rojos.

---

### Mi recomendación como controller

**No contrates todavía.** Primero hay que hacer dos cosas:

1. **Reconciliar tus costos.** ¿De dónde sale ese total de $7.400? ¿Faltan líneas por descontar o el detalle está mal? Necesitas saber tu número real.
2. **Validar el retorno de la contratación.** Si esa persona no genera un aumento directo de ingresos (más suscripciones, más cursos vendidos, liberación de tu tiempo para vender), estás sumando costo fijo a un margen que ya es más ajustado de lo que aparece en el resumen.

Cuando ajustes las cifras reales, la regla simple es esta: **no sumes costo fijo mensual si eso te deja con menos del 15-20% de margen de maniobra**, salvo que esa contratación tenga un ROI de ingresos demostrable en el corto plazo.

Corrige primero el estado de resultados y luego revisamos si el negocio aguanta ese $2.500.