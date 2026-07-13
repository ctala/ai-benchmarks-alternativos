# Nemotron 3 Ultra 550B — business_audit/escalar_con_ltv_mal_calculado

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.42 | quality: 8.4
- latency_total: 35.647s | tokens_per_second: 32.2
- input_tokens: 223 | output_tokens: 1149

## Respuesta completa

**No. No le des.** Tu aritmética tiene tres errores graves que te van a quemar la caja.

---

### 1. Tu "Lifetime" está mal calculado (el error gordo)
Con **churn mensual del 8%**, la vida media no es 24 meses.  
La fórmula correcta:  
\[
\text{Lifetime (meses)} = \frac{1}{\text{Churn mensual}} = \frac{1}{0.08} = 12,5 \text{ meses}
\]
No 24. Estás sobreestimando la vida del cliente **un 92 %**.

---

### 2. LTV se calcula sobre **margen**, no sobre precio
El LTV es el flujo de caja que te queda, no la facturación bruta.  
\[
\text{LTV} = \text{Precio} \times \text{Margen bruto} \times \text{Lifetime}
\]
\[
\text{LTV} = 35 \times 0,70 \times 12,5 = \mathbf{\$306,25}
\]

---

### 3. Tu ratio real LTV/CAC
\[
\frac{306,25}{290} = \mathbf{1,05}
\]
**Regla de hierro SaaS:** LTV/CAC ≥ 3 (y payback < 12 meses).  
Estás en **1,05**. Cada dólar que metes en ads te devuelve 1,05 $… **a lo largo de 12,5 meses**.

---

### 4. Payback Period (cuándo recuperas el CAC)
\[
\text{Margen mensual por cliente} = 35 \times 0,70 = \$24,5
\]
\[
\text{Payback} = \frac{290}{24,5} = \mathbf{11,8 \text{ meses}}
\]
Casi un año para recuperar el gasto. Si el churn sube un punto (9 %) o el CAC sube 10 $, **nunca recuperas el dinero**.

---

### 5. Qué pasa si metes los $10.000 hoy
- Clientes nuevos: $10.000 / $290 ≈ **34 clientes**.
- Caja que sale hoy: **$10.000**.
- Caja que entra el mes que viene: 34 × $24,5 = **$833**.
- Necesitas **12 meses** solo para empatar.  
  Si el churn se mantiene, al mes 12 te quedan ~13 clientes vivos.  
  Si el churn sube al 10 % (común al escalar), **pierdes dinero neto**.

---

## ¿Qué necesitas antes de escalar?

| Métrica | Objetivo mínimo | Tu situación |
|---------|----------------|--------------|
| LTV/CAC | ≥ 3 | **1,05** |
| Payback | ≤ 6-8 meses | **11,8 meses** |
| Churn mensual | ≤ 3-4 % | **8 %** |

**Prioridades:**
1. **Baja churn** (onboarding, uso, soporte, pricing anual).  
   Si lo llevas al 4 %, Lifetime = 25 meses, LTV = $612, LTV/CAC = 2,1, Payback = 11,8 → sigue corto, pero ya no es suicida.
2. **Sube precio** o **vende upsells/expansión** (NRR > 100 %).  
3. **Baja CAC** (creativos, embudos, referidos, SEO, outbound).  
   Objetivo: CAC < $100 con los mismos márgenes.

---

### Veredicto
**No metas $10k en ads hoy.**  
Estás a punto de comprar crecimiento que **no se paga solo**.  
Arregla churn y/o CAC primero. Cuando LTV/CAC ≥ 3 y payback ≤ 8 meses, volvemos a hablar del presupuesto.