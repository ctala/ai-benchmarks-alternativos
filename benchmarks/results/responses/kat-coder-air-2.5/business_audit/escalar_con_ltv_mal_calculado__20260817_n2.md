# KAT Coder Air v2.5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 9.12 | quality: 10.0
- latency_total: 7.54s | tokens_per_second: 188.9
- input_tokens: 217 | output_tokens: 1424

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



# No. Tus números están mal.

Voy a recalculártelos uno por uno.

---

## 1. El LTV que calculaste no existe

**Tu cálculo:** $35 × 24 meses = $840

**El problema:** Un cliente con 8% de churn mensual **no se queda 24 meses**.

La vida media real es: **1 / 0.08 = 12.5 meses**. No 24.

---

## 2. El LTV correcto

La fórmula es:

$$LTV = \frac{ARPU \times Margen\ Bruto}{Churn\ Mensual}$$

$$LTV = \frac{35 \times 0.70}{0.08} = \frac{24.50}{0.08} = \$306$$

---

## 3. El LTV/CAC real

$$LTV/CAC = \frac{306}{290} = 1.05$$

**No es 2.9. Es 1.05.**

---

## 4. Qué significa esto en la práctica

Con $10,000 en publicidad:

| Concepto | Número |
|---|---|
| Clientes que compras | 10,000 / 290 ≈ **34 clientes** |
| Ingreso bruto esperado de esos 34 | 34 × $306 = **$10,404** |
| Menos CAC | -$10,000 |
| **Margen bruto real** | **~$404** |

Casi **pierdes dinero** después de pagar la publicidad. Y eso es solo margen bruto, sin contar salarios, herramientas, operaciones...

---

## 5. Qué necesitas para que esto funcione

Para un LTV/CAC de **3x** (el mínimo que merece la pena):

| Variable | Necesitarías |
|---|---|
| CAC máximo | **$102** (con el LTV actual) |
| O bien, LTV mínimo | **$870** (con tu CAC actual) |

---

## 6. Qué puedes hacer

- **Bajar el CAC:** Mejora tu creatividad, targeting, landing pages. Un CAC de $290 con un precio de $35/mes es muy alto.
- **Subir el ARPU:** Mejora tu pricing, upsells, o reduce el churn (que con 8% mensual estás perdiendo clientes muy rápido).
- **No escale** hasta que el LTV/CAC sea al menos 3x.

---

**Resumen:** Con tus números actuales, cada cliente nuevo que compras con publicidad **casi no genera valor**. El plan de $10,000 en publicidad es una forma elegante de quemar dinero. No lo des.