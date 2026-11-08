# Claude Haiku 5.5 — business_audit/auditoria_pnl_error_plantado

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 9.15 | quality: 10.0
- latency_total: 7.886s | tokens_per_second: 185.1
- input_tokens: 274 | output_tokens: 1460

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

**No, con estos números no contrataría.** Antes de evaluar la decisión, hay un error en el resumen.

**1. Los costos no suman.** Sumando las líneas:

| Concepto | Monto |
|---|---|
| Infraestructura | $1.250 |
| Publicidad | $3.900 |
| Herramientas SaaS | $780 |
| Procesador de pagos | $620 |
| Contenido freelance | $2.600 |
| **Total real** | **$9.150** |

El resumen dice $7.400, así que faltan **$1.750**.

**2. El margen real es ~26%, no 40%.**
- Margen real: ($12.400 − $9.150) / $12.400 = **26,2%**
- El 40% sale de usar el total erróneo de $7.400.

**3. Con el margen real, el contrato no cierra.**
- Utilidad actual: $3.250/mes
- Después de contratar a $2.500: **$750/mes**, es decir, un margen de ~6%.
- Y eso es sin contar las cargas sociales, impuestos o beneficios del empleado, que normalmente suben el costo real por encima del salario bruto.
- Un mes malo (menos suscripciones, un pico de publicidad) y quedas en negativo.

**Antes de decidir, revisa:**
- ¿Falta alguna línea de costo, o el total de $7.400 es de otro período o está mal calculado? Si tienes un gasto que no aparece, el margen puede ser aún menor.
- ¿Cuánto de los $9.800 de suscripciones es recurrente y confiable (churn, cancelaciones)? Los cursos sueltos son ingreso menos predecible.
- La publicidad es el 31% de tus ingresos. Si su eficiencia baja, el margen se va abajo rápido.

**Una regla simple para contratar:** que la utilidad después del salario (con cargas incluidas) siga siendo al menos el 20% de tus ingresos, con colchón para dos meses malos. Con tus costos actuales, eso requiere ingresos de unos **$14.500/mes**, un ~17% más que hoy. Si llegas a ese nivel de forma recurrente durante 3 meses seguidos, la contratación ya es razonable.

Si me pasas el detalle de cuál es el costo que falta y el costo total del empleado (salario más cargas), puedo recalcular el escenario.