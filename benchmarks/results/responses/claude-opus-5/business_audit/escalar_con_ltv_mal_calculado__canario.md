# Claude Opus 5 — business_audit/escalar_con_ltv_mal_calculado

- model_id: `anthropic/claude-opus-5`
- success: True  | final: 8.1 | quality: 10.0
- latency_total: 32.187s | tokens_per_second: 63.6
- input_tokens: 295 | output_tokens: 2048

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

## Respuesta corta: no. Hay dos errores que se multiplican, y corregidos el plan queda en ~1,0x, no 2,9x.

---

### Error 1: 8% de churn mensual no son 2 años de vida

Con churn plano del 8%, la vida media es 1 / 0,08 = **12,5 meses**, no 24.

Curva de supervivencia: 0,92¹² = **37% vivo al año**. 0,92²⁴ = **13,5% vivo a los 2 años**. Los "2 años" no son la media, son la cola.

### Error 2: el LTV se calcula sobre margen bruto, no sobre precio

Cobras $35, pero solo te quedan $24,50 de contribución mensual. Los $10,50 de infra y procesador no pagan publicidad.

### Los números reales

| Concepto | Tu cálculo | Corregido |
|---|---|---|
| Vida media | 24 meses | 12,5 meses |
| Contribución mensual | $35 | $24,50 |
| **LTV** | **$840** | **$306** |
| **LTV / CAC** | **2,9x** | **1,06x** |
| Payback de CAC | — | **11,8 meses** |

Y el dato que cierra el caso: **payback (11,8 meses) ≈ vida media (12,5 meses)**. Recuperas el CAC justo cuando el cliente se va. Ganas $16 por cliente, sin descontar el dinero.

Nota aparte: 2,9 está *por debajo* de 3,