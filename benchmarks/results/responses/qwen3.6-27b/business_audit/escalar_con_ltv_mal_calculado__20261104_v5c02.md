# Qwen 3.6 27B base (OpenRouter FP8) — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 8.56 | quality: 10.0
- latency_total: 41.532s | tokens_per_second: 58.1
- input_tokens: 217 | output_tokens: 2414

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

**Respuesta corta: No. No metas ese dinero.**

Tu cálculo parte de tres errores aritméticos que, en conjunto, invierten completamente la rentabilidad del modelo. Escalar con estos números no es crecimiento, es acelerar la quema de caja.

### 🔍 Dónde falla tu aritmética

| Concepto | Tu cálculo | Cálculo correcto | Por qué importa |
|----------|------------|------------------|-----------------|
| **Vida media del cliente** | 24 meses | `1 / churn mensual = 1 / 0.08 = 12.5 meses` | Un churn del 8% mensual elimina ~60% de la base en 12 meses. No hay base matemática para 24. |
| **LTV** | `$35 × 24 = $840` | `(ARPU × Margen Bruto) / Churn = ($35 × 0.70) / 0.08 = $306` | El LTV se mide en **ganancia neta por cliente**, no en facturación. Además, el churn decae el valor exponencialmente. |
| **LTV/CAC** | `840 / 290 ≈ 2.9` | `306 / 290 ≈ 1.06` | Un ratio < 1.5 significa que cada cliente recuperado te deja en negativo. Estás perdiendo ~$20 por cada adquisición. |

### 📉 Implicaciones reales de escalar así
- **Periodo de recuperación del CAC:** `CAC / Ganancia mensual por cliente = $290 / $24.50 ≈ 11.8 meses`. Con un ciclo de vida de 12.5 meses, apenas recuperas la inversión antes de que el cliente se vaya.
- **Flujo de caja:** Si metes $10k en ads, necesitarás ~34 nuevos clientes. En 6 meses, la mitad ya se habrá ido. Tu caja se comerá el CAC sin ver el retorno completo.
- **"Ya soy rentable"**: Probablemente lo eres por volumen bajo, subsidio de otros ingresos, o costos fijos aún no escalados. A escala, la unit economics negativa se multiplica.

### ✅ Qué hacer antes de tocar el botón de "Publicar campaña"
1. **Baja el churn** (prioridad #1): Un 5% mensual vs 8% duplica tu LTV real (`$24.5 / 0.05 = $490`).
2. **Sube el precio o el margen**: $35/mes con 70% de margen deja poco colchón. Prueba tiering, annual billing, o elimina fricciones operativas que comen margen.
3. **Optimiza el CAC**: $290 para un ticket de $35/mes es agresivo. Si no puedes bajarlo a < $150, el modelo no escala con paid ads.
4. **Valida con cohortes reales**: No uses promedios. Mira cuánto generan realmente tus clientes mes 1, 3, 6, 12. La realidad suele ser más dura que la fórmula.

### 🚦 Veredicto
**LTV/CAC = 1.06 → No es escalable.** 
Escalar ahora es financiar pérdidas unitarias con capital propio. Corriges el modelo, o cambias de canal de adquisición (orgánico, partnerships, referrals), o ajustas precios/márgenes. Cuando el LTV/CAC real esté ≥ 3 y el payback ≤ 9 meses, entonces sí: metes los $10k y duplicas el presupuesto.

¿Quieres que modele escenarios concretos? Dame: churn por cohorte, distribución de pagos (mensual/anual), y costo real de soporte/éxito del cliente. Te devuelvo el punto de inflexión exacto.