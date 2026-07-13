# MiniMax M2.7 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `minimax/minimax-m2.7`
- success: True  | final: 7.52 | quality: 8.4
- latency_total: 35.63s | tokens_per_second: 34.1
- input_tokens: 186 | output_tokens: 1215

## Respuesta completa

# Hay un error aritmético que cambia todo

Tu LTV no es $840. Es **$306**.

---

## Dónde se rompe tu cálculo

**Tu error**: usar 24 meses como vida del cliente.

**La realidad**: con 8% churn mensual, la vida promedio es **1 / 0.08 = 12.5 meses**.

Esto no es arbitrario. Es la definición de vida promedio con churn exponencial.

---

## LTV corregido

| Concepto | Tu cálculo | Corrección |
|---|---|---|
| Revenue por mes | $35 | $35 |
| × Margen bruto | 70% | 70% |
| = Profit por mes | — | **$24.50** |
| × Vida del cliente | 24 meses | **12.5 meses** |
| **LTV (profit)** | **$840** ❌ | **$306** |

---

## LTV/CAC real

```
$306 / $290 = 1.06
```

No 2.9.

---

## El campaign de $10,000

```
Clientes adquiridos:  $10,000 / $290 = ~34 clientes

Profit total en vida:  34 × $306 = $10,404

ROI del campaign:     ($10,404 - $10,000) / $10,000 = +4%
```

Ganas $404. Eso si no hay varianza en el CAC.

---

## El problema de fondo: payback de 12 meses

```
$290 de CAC / $24.50/mes = 11.8 meses para recuperar
```

Te quedan ~0.7 meses de profit neto por cliente. El margen de error es **cero**.

---

## Mi recomendación

**No metes los $10,000 todavía.**

Pero no porque el unit economics esté destruido — está justo en equilibrio. El problema es que estás demasiado expuesto a:

- Aumento de churn al escalar (más usuarios = más segmento mixto)
- CAC real superior a $290 bajo volumen mayor
- Cualquier decremento en margen te lleva a pérdida

**Qué hacer en su lugar**:

1. **Test con $2,000** — valida que el CAC se mantiene en $290 o menos bajo condiciones reales
2. **Baja el churn primero** — si lo reduces a 5%, el LTV sube a $490 y el LTV/CAC a 1.69. Eso te da margen para escalar
3. **Sube el precio** — $45/mes con el mismo churn te da LTV de $551 y LTV/CAC de 1.9. Más buffer

El plan de crecimiento muere en la aritmética, sí. Pero también muere si escalas sin buffer. Con LTV/CAC de 1.06, un mes malo te quebra.