# Claude Sonnet 4.6 (suscripción) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `claude-sonnet-4-6`
- success: True  | final: 6.91 | quality: 8.4
- latency_total: 54.193s | tokens_per_second: 42.5
- input_tokens: 3 | output_tokens: 2301

## Respuesta completa

## No le des. Hay un error de aritmética que cambia todo.

---

### El error: cómo calculaste el lifetime

Usaste 24 meses (2 años). Pero con **8% de churn mensual**, el lifetime promedio es:

**1 / tasa de churn = 1 / 0,08 = 12,5 meses**

No 24. Eso pasa cuando el churn anualizado se siente "manejable" pero el mensual destruye silenciosamente la base.

Para que el lifetime promedio fuera 24 meses necesitarías churn de ~4% mensual. Tienes el doble.

---

### Tus números reales

| Concepto | Tu cálculo | El real |
|---|---|---|
| Lifetime promedio | 24 meses | **12,5 meses** |
| LTV (ingresos brutos) | $840 | **$437** |
| LTV (con margen 70%) | — | **$306** |
| LTV/CAC (ingresos) | 2,9 | **1,51** |
| LTV/CAC (margen real) | — | **1,06** |

El LTV/CAC que importa usa margen, no ingresos brutos. Con margen: **1,06**. Estás recuperando el CAC y casi nada más.

---

### El número que más duele: payback period

Ganancia bruta mensual por cliente = $35 × 70% = **$24,50/mes**

Payback = $290 / $24,50 = **11,8 meses**

Tu cliente promedio dura 12,5 meses. Recuperas el CAC a los 11,8 meses. Margen de maniobra: **0,7 meses**. Cualquier variación en churn o conversión y estás en negativo.

---

### Qué pasa con los $10.000

$10.000 / $290 CAC = ~34 clientes nuevos

Ganancia bruta esperada sobre su lifetime: 34 × $306 = **$10.400**

Recuperas apenas lo invertido, sin contar overhead, tiempo tuyo, ni riesgo de que el CAC suba al escalar.

---

### Lo que necesitas antes de meter $10K

El modelo escala bien cuando LTV/CAC (con margen) es **≥ 3**. Para llegar ahí con tu precio y margen actuales:

LTV necesario = 3 × $290 = $870 (con margen)  
Lifetime necesario = $870 / $24,50 = **35,5 meses**  
Churn máximo = 1 / 35,5 = **2,8% mensual**

Tienes 8%. Necesitas llegar a menos de 3%.

**Las dos palancas reales:**

1. **Bajar churn de 8% a ~3-4%.** Ese es el problema central. A 4% de churn tu LTV/CAC con margen llega a 2,1 — todavía bajo, pero el negocio ya respira. A 3% llegas a 2,8, cerca del umbral.

2. **O subir precio.** Si subes a $49/mes con el mismo churn de 8%: LTV margen = $49 × 70% × 12,5 = $429. LTV/CAC = 1,48. Mejor, pero sigue sin justificar escalar con paid.

---

### Diagnóstico

Eres rentable porque ya tienes base instalada y no estás pagando CAC por todos. Pero el **motor de adquisición pagado está roto con estos números**. Meter $10K hoy es subsidiar crecimiento que no se sostiene.

Primero: entiende por qué el 8% de tus clientes se va cada mes. Ese número es el techo de todo lo demás.