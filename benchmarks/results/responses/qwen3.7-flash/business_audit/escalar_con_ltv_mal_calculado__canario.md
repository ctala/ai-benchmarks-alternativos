# Qwen 3.7 Flash — business_audit/escalar_con_ltv_mal_calculado

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.19 | quality: 10.0
- latency_total: 29.733s | tokens_per_second: 110.8
- input_tokens: 217 | output_tokens: 3295

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

**No. No lo apruebo.** Tu cálculo de LTV tiene dos errores estructurales que invierten completamente la rentabilidad del plan. Vamos a limpiar la aritmética antes de mover un solo dólar.

### 🔍 Recálculo objetivo
| Concepto | Tu dato | Realidad matemática |
|----------|---------|---------------------|
| Precio (ARPU) | $35/mes | ✅ |
| Margen bruto | 70% | ✅ → `$35 × 0.70 = $24,50` de beneficio bruto mensual por cliente |
| Churn mensual | 8% | ✅ → Vida media = `1 / 0.08 = 12,5 meses` (no 24) |
| **LTV correcto** | `$35 × 24 = $840` ❌ | `(Margen bruto mensual) / Churn` = `$24,50 / 0.08 = **$306,25**` |
| **LTV/CAC real** | `840 / 290 ≈ 2,9` ❌ | `306,25 / 290 ≈ **1,06**` ✅ |

Un LTV/CAC de **1,06** significa que apenas cubres el costo de adquirir al cliente con su beneficio bruto. Sin contar soporte, ventas, ops, impuestos ni tu tiempo, **estás perdiendo dinero con cada nueva baja**. El umbral mínimo para escalar con paid media es **≥3**. Con 1,06, el crecimiento quema caja linealmente.

### ⚠️ Otros riesgos que tu modelo oculta
1. **Payback period**: `$290 / $24,50 ≈ 11,8 meses`. En publicidad pagada, recuperar la inversión en casi un año es insostenible si quieres reinvertir o buscar financiación. Lo saludable es `<6-8 meses`.
2. **El CAC no es fijo**: Al subir el gasto de $0 a $10k/mes, las pujas suben, el público se satura y el CAC suele crecer un 20-40%. Es muy probable que pase de $290 a $350-$400 en el mismo mes.
3. **Flujo de caja negativo**: Pagas $290 upfront, recibes $24,50/mes durante ~12 meses. Cada cliente nuevo genera un hueco de caja inicial que debe ser financiado. $10k/mes equivalen a ~$34 clientes nuevos; necesitas liquidez para cubrir ~$83k en gaps mensuales hasta que empiecen a pagar.

### 🛠 Qué cambiar para que el plan sea aprobable
Necesitas mover al menos una palanca hasta alcanzar **LTV ≥ $870** (con CAC=$290, ratio 3x). Opciones reales:
| Palanca | Acción concreta | Impacto esperado |
|---------|----------------|------------------|
| **Bajar churn** | Onboarding estructurado, webinars de éxito, pricing por uso, detección temprana de fricción | 8% → 4% duplica LTV a ~$612 |
| **Reducir CAC** | Creative testing riguroso, retargeting de visitors, referral program, partnerships, SEO/blogs | $290 → $100-120 mejora ratio directo |
| **Subir margen/ARPU** | Upsell a tier superior, eliminar features costosas, renegociar infraestructura, precio a $45 | Margen 70% → 80% o ARPU $35→$45 eleva LTV proporcionalmente |

### ✅ Veredicto analista
**Rechazo el despliegue de $10.000/mes.** 
Haz un test controlado de **$1.000-$2.000/mes**, mide LTV real a los 3 y 6 meses, y verifica si el CAC se mantiene o el churn se estabiliza. Solo cuando el modelo cruce **LTV/CAC ≥ 3** y **payback < 8 meses**, autorizo el apalancamiento.

La aritmética no perdona. Escalar pérdidas es solo acelerar el cierre. ¿Quieres que te arme un dashboard de seguimiento para el test de $1.5k?