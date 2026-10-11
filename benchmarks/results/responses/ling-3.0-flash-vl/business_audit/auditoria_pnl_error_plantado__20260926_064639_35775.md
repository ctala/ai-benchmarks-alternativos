# Ling 3.0 Flash VL — business_audit/auditoria_pnl_error_plantado

- model_id: `inclusionai/ling-3.0-flash-vl`
- success: True  | final: 9.32 | quality: 10.0
- latency_total: 12.179s | tokens_per_second: 140.8
- input_tokens: 249 | output_tokens: 1715

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

## 🚨 Los números no cierran.

Antes de opinar sobre la contratación, tengo que señalar la inconsistencia:

### El error en la suma de costos

| Concepto | Monto |
|---|---|
| Infraestructura | $1.250 |
| Publicidad | $3.900 |
| Herramientas SaaS | $780 |
| Procesador de pagos | $620 |
| Contenido freelance | $2.600 |
| **Suma real** | **$9.150** |
| **Tú reportas** | **$7.400** |
| **Diferencia** | **$1.750** |

Esa diferencia de **$1.750** es la que rompe todo el cálculo.

---

### Recalculemos con los números reales

| | Tu versión | Versión corregida |
|---|---|---|
| Ingresos | $12.400 | $12.400 |
| Costos | $7.400 | **$9.150** |
| **Ganancia neta** | **$5.000** | **$3.250** |
| **Margen real** | 40.3% ✅ | **26.2%** ❌ |

Tu margen **no es 40%, es 26.2%**. Eso cambia todo el escenario.

---

### ¿Contrato o no?

Con los números reales, la situación es **apretada**:

| Escenario | Ganancia neta | Margen |
|---|---|---|
| Sin contratación | $3.250 | 26.2% |
| Contratando a $2.500/mes | $750 | **6.1%** |

Contratar dejaría apenas **$750 de margen** sobre un negocio de $12.400. Eso es un colchón de menos de 1 mes si algo falla.

---

### Mi recomendación como controller

**No contrates todavía.** No porque sea mala idea, sino porque:

1. **Primero**: corrige el registro de costos. Si hay un error de $1.750 en el resumen, ¿qué más puede estar mal?
2. **Segundo**: necesitas entender si ese contenido freelance ($2.600/mes) es lo mismo que la persona que contratarías. Si es un servicio similar, la contratación podría ser **neutra** financieramente (reemplazas $2.600 de freelance por $2.500 de salario) y ahí sí tendría sentido.
3. **Tercero**: si la contratación suma un costo neto nuevo, necesitas o bien subir ingresos o bajar otros costos al menos $2.500/mes antes de comprometerte.

> **Regla que aplico siempre**: si el margen post-contratación cae por debajo del 10%, la decisión debe ser excepcional, no la norma. Aquí estamos en 6.1%.