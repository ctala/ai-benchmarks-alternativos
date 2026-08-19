# Seed 2.1 Turbo — business_audit/auditoria_pnl_error_plantado

- model_id: `bytedance-seed/seed-2-1-turbo`
- success: True  | final: 8.32 | quality: 10.0
- latency_total: 77.661s | tokens_per_second: 85.7
- input_tokens: 255 | output_tokens: 6658

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

### Primero: los números no cierran
La suma de los rubros de costos que enumeraste da **$9.150**, pero declaras un total de costos de $7.400 (una diferencia de $1.750). Por lo tanto, el margen del 40% que mencionas no es consistente con los datos detallados que compartiste.

Cálculo de la suma de costos detallados:
```
Infraestructura:      $1.250
Publicidad:           $3.900
Herramientas SaaS:      $780
Procesador de pagos:    $620
Contenido freelance:  $2.600
---------------------------
Total costos reales:  $9.150
```

Para responder tu pregunta, analizo los dos escenarios posibles según cuál sea el dato correcto:

---

## Escenario 1: Tu total de costos de $7.400 es correcto (margen del 40% real)
Si te equivocaste al escribir alguno de los rubros de costo (ej: publicidad o contenido freelance tienen un valor menor al que pusiste):
- Beneficio operativo mensual actual: `$12.400 - $7.400 = $5.000` (sí coincide con un margen de ~40%)
- Si contratas a alguien por $2.500/mes, el beneficio operativo se reduce a **$2.500/mes** (antes de impuestos y costos adicionales de contratación).

### Matices clave que cambian el cálculo:
1. **Costos adicionales de la contratación**: Si es personal en relación de dependencia, las cargas sociales (seguridad social, vacaciones, aguinaldo, indemnizaciones) suman entre un 20% y 50% extra del sueldo bruto, dependiendo de tu país. Es decir, $2.500 de sueldo pueden terminar costándote $3.000-$3.750 al mes, no $2.500. Si es freelance sin cargas, el costo se mantiene en $2.500, pero verifica que sea legal para el tipo de tarea que realice.
2. **Tu propio sueldo**: ¿Está incluido en los costos? Si no lo está, ese $5.000 de beneficio es en parte tu salario por trabajar en el negocio. Si contratas, te quedarían $2.500 (o menos si hay cargas) para ti antes de impuestos, lo que puede ser suficiente o no según tus necesidades.
3. **Impuestos a las ganancias**: El beneficio paga impuestos de entre el 15% y 35% según tu país. Por ejemplo, con un 25% de impuestos, el beneficio neto actual es $3.750, y después de contratar sería $1.875.
4. **Estabilidad y colchón de caja**: El 79% de tus ingresos son suscripciones (recurrentes y estables), pero los cursos sueltos pueden variar. Lo recomendable es tener al menos 3-6 meses de costos fijos ahorrados para cubrir el sueldo en meses de menores ingresos.

### Viabilidad en este escenario:
Sí es viable, siempre y cuando tengas en cuenta los costos adicionales y la contratación te libere tiempo para generar más ingresos o escalar el negocio (no solo para tareas que no agreguen valor).

---

## Escenario 2: Los rubros de costos que enumeraste son correctos (margen real ~26%)
Si te equivocaste en el total de costos y en el cálculo del margen:
- Beneficio operativo mensual actual: `$12.400 - $9.150 = $3.250`
- Margen real: `$3.250 / $12.400 = 26,2%` (no 40%)
- Si contratas a alguien por $2.500/mes, el beneficio operativo se reduce a **solo $750/mes** (antes de impuestos y cargas).

### Matices clave:
- Si hay cargas sociales por contratación en relación de dependencia, el costo total sube a $3.000-$3.750, lo que te generaría pérdidas de entre $500 y $1.250 por mes.
- Si tu sueldo no está incluido en los costos, prácticamente no te quedarás nada de dinero para ti, o incluso perderás plata.

### Viabilidad en este escenario:
No es recomendable a menos que la persona que contrates genere un aumento de ingresos de al menos $3.000/mes en el corto plazo (ej: si se encarga de ventas o contenido que escale el negocio). Tu margen de seguridad actual es muy bajo para asumir un costo fijo nuevo.

---

### Recomendación final
Primero corregí el error en los costos para confirmar tu situación real. Si el escenario 1 es el correcto, podés contratar siempre que tengas en cuenta los costos adicionales y tengas un colchón de caja mínimo. Si el escenario 2 es el correcto, primero enfocate en aumentar tu margen (ej: reducir costos de publicidad o aumentar ingresos de suscripciones) antes de asumir nuevos gastos fijos.