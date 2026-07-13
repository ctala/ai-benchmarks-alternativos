# Claude Opus 4.6 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-4-6`
- success: True  | final: 6.91 | quality: 8.4
- latency_total: 29.587s | tokens_per_second: 45.6
- input_tokens: 239 | output_tokens: 1350

## Respuesta completa

# Revisión de Unit Economics: Los números no dicen lo que crees

## Tu cálculo tiene errores fundamentales

Vamos paso a paso.

---

## Error 1: La vida promedio del cliente no es 2 años

Con 8% de churn mensual, la vida promedio se calcula como:

$$\text{Vida promedio} = \frac{1}{\text{churn}} = \frac{1}{0.08} = 12.5 \text{ meses}$$

**No 24 meses. La mitad de lo que asumiste.**

Un churn del 8% mensual significa que cada mes pierdes 8 de cada 100 clientes. Eso es altísimo: al cabo de 12 meses solo retienes ~36% de una cohorte.

---

## Error 2: El LTV real es menos de la mitad de tu cifra

$$\text{LTV} = \frac{\text{Precio} \times \text{Margen bruto}}{\text{Churn}} = \frac{35 \times 0.70}{0.08} = \frac{24.50}{0.08} = \$306.25$$

| Concepto | Tu cálculo | Cálculo real |
|---|---|---|
| Vida del cliente | 24 meses | 12.5 meses |
| LTV (con margen bruto) | $840 | **$306.25** |
| CAC | $290 | $290 |
| **LTV/CAC** | **2.9x** | **1.06x** |

---

## Lo que significa un LTV/CAC de 1.06x

Significa que por cada $290 que gastas en adquirir un cliente, recuperas $306 de margen bruto a lo largo de toda su vida. Te quedan **$16.25 por cliente** para cubrir:

- Salarios (incluido el tuyo)
- Soporte al cliente
- Herramientas y software interno
- Costos legales, contables
- Cualquier otro gasto operativo

**Es prácticamente punto de equilibrio antes de gastos operativos.** Meter $10.000 en publicidad te trae ~34 clientes y ~$552 de margen total después de recuperar el CAC. No estás escalando, estás subsidiando crecimiento.

---

## El benchmark y por qué importa

La regla general para SaaS es **LTV/CAC ≥ 3x** para escalar con paid. Tú estás en 1.06x. Te faltan casi 3 veces de distancia.

---

## Qué mover antes de escalar con publicidad

Tienes tres palancas. Te muestro el impacto de cada una:

### Palanca 1 — Reducir churn (la más poderosa)

| Churn mensual | Vida (meses) | LTV | LTV/CAC |
|---|---|---|---|
| **8%** (actual) | 12.5 | $306 | 1.06x |
| 5% | 20 | $490 | 1.69x |
| 3% | 33 | $817 | 2.82x |
| **2.5%** | **40** | **$980** | **3.38x** ✅ |

**Bajar el churn de 8% a 2.5% multiplica tu LTV por 3.2x.** Esto es lo que separa un negocio escalable de uno que no lo es.

### Palanca 2 — Subir el precio

| Precio | LTV (churn 8%) | LTV/CAC |
|---|---|---|
| $35 (actual) | $306 | 1.06x |
| $50 | $437 | 1.51x |
| $70 | $612 | 2.11x |

Ayuda, pero con churn del 8% nunca llegas a 3x con precios razonables.

### Palanca 3 — Bajar el CAC

Difícil de hacer "a voluntad" en paid. Generalmente sube al escalar, no baja.

---

## Mi recomendación concreta

**No metas los $10.000 en publicidad todavía.** Invierte ese dinero y los próximos 2-3 meses en:

1. **Diagnosticar el churn del 8%.** Habla con los últimos 20-30 clientes que cancelaron. ¿Se van en el mes 1-2 (onboarding fallido) o después (falta de valor percibido)?
2. **Fijar un objetivo de churn ≤ 3-4%** antes de escalar paid.
3. **Evaluar si $35/mes es demasiado barato.** Un churn alto a veces indica que atraes clientes de bajo compromiso por precio bajo.

Cuando tengas churn ≤ 4% y LTV/CAC ≥ 3x, ahí sí: escala con toda la agresividad que quieras. Los números te van a respaldar en vez de hundirte.

**Tu negocio es rentable hoy probablemente porque creces orgánicamente con CAC bajo. Escalar con paid a estos unit economics convierte un negocio rentable en uno que quema caja.**