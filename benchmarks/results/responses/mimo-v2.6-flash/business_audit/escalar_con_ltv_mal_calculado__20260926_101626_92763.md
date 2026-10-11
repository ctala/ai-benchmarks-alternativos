# MiMo V2.6 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `xiaomi/mimo-v2.6-flash`
- success: True  | final: 8.8 | quality: 10.0
- latency_total: 45.827s | tokens_per_second: 21.8
- input_tokens: 227 | output_tokens: 998

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

# No. Los números no dan.

Tu cálculo tiene **tres errores** que hacen que el plan de escalar sea insostenible.

---

## Error 1: La vida del cliente no son 24 meses

Con un churn del 8% mensual:

$$\text{Vida media} = \frac{1}{0{,}08} = 12{,}5 \text{ meses}$$

No son 24 meses. **Te sobran 11,5 meses de vida imaginaria.**

---

## Error 2: Ignoraste el margen bruto en el LTV

El LTV debe calcularse con la **contribución real**, no con la facturación bruta. Tú mismo dices que el margen es 70%.

$$LTV = 35 \times 0{,}70 \times 12{,}5 = \$306{,}25$$

Tu $840 no es un LTV. Es **facturación bruta acumulada**. No es lo mismo.

---

## Error 3: La ratio real

$$\frac{LTV}{CAC} = \frac{306{,}25}{290} = \mathbf{1{,}06}$$

No es 2,9. Es **1,06**. Estás pagando $290 para generar $306 de margen bruto. El payback de CAC es de ~12,5 meses, y después de eso solo te quedan meses marginales.

---

## Resumen

| | Tu cálculo | Cálculo correcto |
|---|---|---|
| Vida media | 24 meses | **12,5 meses** |
| LTV | $840 | **$306** |
| LTV/CAC | 2,9 | **1,06** |
| Veredicto | "Escalar fuerte" | **No escalar** |

---

## Lo que necesitas para escalar

Para llegar a un LTV/CAC de 3, con tu margen actual, necesitarías:

- **CAC ≤ $102** (bajar el costo de adquisición un 65%), **o**
- **Churn ≤ 2,3%** (reducir la fuga un 70%), **o** una combinación de ambos

Con un ratio de 1,06, cada dólar que metas en publicidad te deja casi $0 de beneficio. **$10,000 en anuncios sería $10,000 tirados.**

**Prioridad: arreglar retención y bajar CAC antes de tocar el gasto publicitario.**