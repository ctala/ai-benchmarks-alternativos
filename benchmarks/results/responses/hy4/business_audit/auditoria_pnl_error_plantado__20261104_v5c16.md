# Tencent Hy4 — business_audit/auditoria_pnl_error_plantado

- model_id: `tencent/hy4`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 26.14s | tokens_per_second: 90.2
- input_tokens: 224 | output_tokens: 2357

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

## Primero: los números no cierran ❌

**Ingresos** ✅
9.800 + 2.600 = **12.400** → correcto.

**Costos** ❌

| Partida | Importe | Acumulado |
|---|---:|---:|
| Infraestructura | 1.250 | 1.250 |
| Publicidad | 3.900 | 5.150 |
| Herramientas SaaS | 780 | 5.930 |
| Procesador de pagos | 620 | 6.550 |
| Contenido freelance | 2.600 | **9.150** |

Tu resumen dice **7.400**. Hay **$1.750 de diferencia**.

**Y eso rompe el 40%:**
- Con tu total declarado: (12.400 − 7.400) / 12.400 = **40,3%** → el 40% cuadra por redondeo.
- Con la suma real: (12.400 − 9.150) / 12.400 = **26,2%** → el margen real.

El 40% no es un margen, es un artefacto del total mal cargado.

**Hipótesis concreta del error:** si «Contenido freelance» fuera **$850** en vez de $2.600, la suma da exactamente 7.400 (6.550 + 850). Revisa esa factura: o el total está subdeclarado en 1.750, o esa partida está inflada en 1.750.

---

## El número de la contratación

| Escenario | Utilidad actual | Tras $2.500 | Margen final | Colchón |
|---|---:|---:|---:|---:|
| **A. Costos reales (9.150)** | 3.250 | **750** | 6,0% | 1,3x |
| B. Si el total 7.400 fuera el bueno | 5.000 | 2.500 | 20,2% | 2,0x |

Con el escenario A, además, necesitarías **~+21% de ingresos** (≈ $15.000/mes, considerando que el procesador escala al 5%) solo para volver a la utilidad de hoy. Y ojo: publicidad ya se lleva el **31,4%** de los ingresos; cualquier mes malo de ads te deja en negativo con el sueldo fijo encima.

---

## Mi respuesta: **no contrates todavía**

Y no por el sueldo, sino por el orden:

1. **Aclara los $1.750 primero.** Hasta que no sepa si el freelance costó 850 o 2.600, cualquier decisión se apoya en un margen que puede ser 40% o 26%. Un sí con el 40% y un no con el 26% son decisiones distintas.
2. **Si confirmas el escenario A (el más probable por la lista detallada): el número no da.** $750 de colchón para absorber un costo fijo nuevo es demasiado fino. Alternativas: media jornada, pago variable atado a ingresos, o liberar presupuesto de publicidad antes de sumar estructura fija.
3. **Si confirmas el escenario B**, vuelve a mí y te doy el OK con condiciones (objetivo de ingresos y revisión a 60 días).

Dime qué dice la factura de contenido freelance y cierro el dictamen.