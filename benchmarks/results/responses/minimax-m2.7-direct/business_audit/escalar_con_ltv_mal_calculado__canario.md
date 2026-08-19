# MiniMax M2.7 (directo) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `MiniMax-M2.7`
- success: True  | final: 8.64 | quality: 10.0
- latency_total: 35.534s | tokens_per_second: 35.9
- input_tokens: 186 | output_tokens: 1274

## Entrada exacta (lo que recibió el modelo)

**system:**

Eres analista de unit economics. Antes de aprobar un plan de crecimiento, recalculas los números del fundador. Muchos planes mueren en la aritmética.

**user:**

Ya soy rentable y quiero escalar fuerte con publicidad pagada. Mis números:

- Precio: $35/mes por cliente.
- Churn mensual: 8%.
- Margen bruto: 70% (después de infraestructura y procesador de pagos).
- Mi costo de adquirir un cliente con publicidad (CAC): $290.

Mi cálculo: como un cliente se queda unos 2 años, el LTV es 35 × 24 = $840. Contra un CAC de $290, eso me da LTV/CAC = 2,9, que está por encima de 3 más o menos. Así que voy a meter $10.000 en publicidad este mes.

¿Le doy?


## Respuesta completa

# No le das. Tu aritmética tiene dos errores que cambian todo.

---

## Error 1: Sobreestimas la vida del cliente

Dices que el cliente se queda 2 años. Eso no es lo que dice tu churn.

Con un churn mensual del 8%:

```
Vida promedio del cliente = 1 / 0.08 = 12.5 meses
```

No 24 meses. El churn compuesto hace que la mayoría de tus clientes se vayas antes. Tu cálculo asume que todos duran exactamente 24 meses, lo cual es incorrecto.

---

## Error 2: No aplicas tu margen bruto al LTV

Tu LTV debe medirse en **margen**, no en ingreso bruto.

```
LTV correcto = $35 × 12.5 meses × 70% = $306 por cliente
```

No $840. Estás contando el ingreso completo cuando tu margen real por cliente es $24.50/mes.

---

## Tu LTV/CAC real

```
LTV/CAC = $306 / $290 = 1.06
```

No 2.9.

---

## Lo que eso significa para tus $10,000

| | Tu cálculo | Realidad |
|---|---|---|
| Clientes nuevos | 34 | 34 |
| LTV por cliente | $840 | $306 |
| Valor total generado | $28,560 | $10,404 |
| Costo de la campaña | $10,000 | $10,000 |
| **Ganancia neta** | **$18,560** | **$404** |

Estás arriesgando $10,000 para ganar $404 si tus números son exactos.

---

## ¿Qué necesitas para que esto funcione?

Con LTV/CAC de 3x (el umbral mínimo para escalar con margen de seguridad):

| palanca |现在的位置| Necesitas |
|---|---|---|
| CAC | $290 | $102 o menos |
| Churn | 8% mensual | 2.3% o menos |
| Margen bruto | 70% | 100% |
| Precio | $35/mes | $102/mes |

O una combinación de los anteriores.

---

## Mi recomendación

**No metas $10k.** No por falta de rentabilidad teórica, sino porque con 1.06x tienes casi cero margen de error. Si el CAC sube un 10%, si el churn sube a 9%, si hay fraude o errores de tracking, **pierdes dinero**.

Lo que sí puedes hacer:

1. **Prueba $1,000-2,000** y mide si el CAC real coincide con $290
2. **Concéntrate en bajar el churn primero.** Cada punto de churn baja de 8% a 6% te da 4 meses más de vida útil por cliente
3. **Revisa si hay palancas de LTV** que no estás contando: upsells, renewals anuales con descuento, expansión natural

Cuéntame qué palanca te parece más viable y recalculamos.