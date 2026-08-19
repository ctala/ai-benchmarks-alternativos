# Inkling Small — business_audit/escalar_con_ltv_mal_calculado

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.2 | quality: 10.0
- latency_total: 252.235s | tokens_per_second: 22.5
- input_tokens: 194 | output_tokens: 5672
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando una evaluación detallada y correcta de la situación financiera del emprendedor.

## Respuesta completa

**No. No metas los $10.000. La aritmética te mata antes de que la publicidad respire.**

Tu cálculo tiene tres errores fatales. Vamos a recalcular con sangre fría.

---

### 1. La vida del cliente no es 2 años
Churn mensual = 8%.  
**Vida media = 1 / 0.08 = 12.5 meses** (no 24).

A 8% mensual, al año solo te queda el **36.7%** de la cohorte:
`(1 - 0.08)^12 = 0.367`. El resto se fue.

---

### 2. El LTV no se calcula con el precio, sino con el margen bruto
Tu margen bruto es 70%.  
**Margen mensual por cliente = $35 × 0.70 = $24.50.**

LTV correcto (fórmula SaaS estándar):
```
LTV = (ARPU × Margen Bruto) / Churn
LTV = $24.50 / 0.08 = $306.25
```

Tu “$840” era ingreso bruto, no ganancia. Y con 24 meses inventados.

---

### 3. Tu LTV/CAC real es 1.05x, no 2.9x
```
LTV / CAC = $306.25 / $290 = 1.05
```

Estás **en el límite de la rentabilidad** (1:1), no en 3:1.

---

### El payback es peor de lo que parece
Simple: `CAC / Margen mensual = $290 / $24.50 ≈ 11.8 meses`.

Pero eso ignora el churn. Como el 8% se va cada mes, la recuperación real es exponencialmente más lenta. En expectativa, recuperas:

- **Mes 12:** ~$194 (te faltan $96; el 63% del cohort murió).
- **Mes 24:** ~$265.
- **Mes 36:** recién cruzas los $290.

**Necesitas ~3 años para recuperar el CAC de un cliente que, en promedio, se va a los 12.5 meses.** Eso es un agujero de caja disfrazado de “rentable”.

---

### Qué pasa si metes los $10.000 hoy
- A $290 CAC: compras **~34 clientes**.
- Gastas **$10.000 ahora**.
- En el mes 1 recibes ~**$845** de margen bruto (34 × $24.50).
- En el mes 2: ~$777.
- En el mes 12: apenas ~$310 de la cohorte original.

No recuperas la inversión en meses; la recuperas (si acaso) en años, y solo porque unos pocos sobrevivientes pagan por los que se fueron.

---

### La regla para escalar con ads pagados
Para meter dinero fuerte en publicidad, necesitas:

| Métrica | Tu número | Lo que necesitas |
|---|---|---|
| **LTV/CAC** | **1.05x** | **> 3x** |
| **Payback real** | **~36 meses** | **< 12 meses** |
| **Churn mensual** | **8%** | **< 3-5%** |

Con 8% de churn, tu negocio es un **bote con fuga**. Escalar con ads es como llenar una bañera con el desagüe abierto.

---

### Veredicto
**No apruebes el plan. No metas los $10.000.**

Tu rentabilidad actual probablemente viene de clientes orgánicos o de baja adquisición, no de ads a $290. Si escalas así, estás comprando dinero con descuento.

**Haz esto primero:**
1. **Baja el churn.** 8% mensual es brutal. Si lo bajas a 4%, tu LTV salta a $612 y tu ratio a **2.1x**.
2. **Sube el precio o el margen.** O reduce CAC por debajo de $100.
3. Cuando `LTV / CAC > 3` y el payback esté bajo 12 meses, vuelve con los $10.000.

**Muchos planes mueren en la aritmética. El tuyo está en 1.05x. No es 2.9x. Corrige la fuga antes de abrir la llave.**