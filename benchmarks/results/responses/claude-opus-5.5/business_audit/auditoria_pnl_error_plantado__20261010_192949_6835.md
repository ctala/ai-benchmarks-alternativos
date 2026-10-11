# Claude Opus 5.5 — business_audit/auditoria_pnl_error_plantado

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 8.22 | quality: 10.0
- latency_total: 15.815s | tokens_per_second: 88.2
- input_tokens: 274 | output_tokens: 1395

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

# Primero: los números no cierran

**El total de costos está mal sumado.**

| Concepto | Monto |
|---|---|
| Infraestructura | $1.250 |
| Publicidad | $3.900 |
| Herramientas SaaS | $780 |
| Procesador de pagos | $620 |
| Contenido freelance | $2.600 |
| **Total real** | **$9.150** |
| Total en tu resumen | $7.400 |
| **Diferencia** | **$1.750** |

Los ingresos sí cuadran: $9.800 + $2.600 = $12.400.

**Margen corregido:**
- Utilidad: $12.400 − $9.150 = **$3.250**
- Margen: $3.250 / $12.400 = **26,2%**, no 40%

El 40% sale de usar el total equivocado de $7.400. La diferencia de $1.750 no coincide con ninguna partida. Puede ser un error de fórmula, una fila que quedó fuera del rango de suma o un total copiado de otro mes. Conviene revisarlo.

# Ahora sí: ¿te da para contratar?

| | Sin contratar | Con contratación |
|---|---|---|
| Ingresos | $12.400 | $12.400 |
| Costos | $9.150 | $11.650 |
| **Utilidad** | **$3.250** | **$750** |
| **Margen** | 26,2% | **6,0%** |

**Con los números actuales, no da con holgura.** Te quedarían $750 al mes, y eso antes de considerar:

1. **El costo real de la persona.** Si es empleado, las cargas sociales, aportes y prestaciones suelen sumar entre 20% y 40% sobre el sueldo. Con $500 a $1.000 extra, quedas en cero o en pérdida.
2. **La variabilidad.** Esto es un solo mes. Si los ingresos bajan un 6% ($750), ya no cubres la contratación.
3. **Tu propio sueldo.** Si los $3.250 son también lo que tú te llevas, contratar significa dejar de pagarte casi por completo.

# Qué haría antes de decidir

- **Revisar los últimos 3 a 6 meses** con las sumas verificadas, para ver si 26% es lo normal o un mes atípico.
- **Definir qué hará esa persona.** Si va a generar ingresos (ventas, más cursos, retención de suscriptores), calcula cuánto tiene que aportar para pagarse. Si solo libera tu tiempo, el costo tiene que salir del margen actual, que no alcanza.
- **Mirar la publicidad.** Con $3.900 es tu mayor costo (31% de los ingresos). Si parte de ese gasto rinde poco, ahí puede estar el espacio para financiar la contratación.
- **Considerar un formato intermedio**, como medio tiempo o freelance por proyecto, hasta que el margen real se sostenga por encima del 35-40%.

**Conclusión:** la decisión se tomó sobre un margen que no existe. Con el 26% real, contratar a $2.500 deja al negocio sin colchón. Primero corrige la planilla y valida varios meses.