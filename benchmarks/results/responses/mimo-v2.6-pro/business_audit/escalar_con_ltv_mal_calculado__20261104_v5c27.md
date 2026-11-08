# MiMo V2.6 Pro — business_audit/escalar_con_ltv_mal_calculado

- model_id: `xiaomi/mimo-v2.6-pro`
- success: True  | final: 8.66 | quality: 10.0
- latency_total: 40.625s | tokens_per_second: 36.2
- input_tokens: 227 | output_tokens: 1470

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

# No le des. Tu plan muere en dos líneas de aritmética.

## Error 1: El lifetime está mal

Un churn mensual del 8% no significa "2 años de permanencia". El tiempo de vida esperado es:

**LTV en meses = 1 / churn = 1 / 0,08 = 12,5 meses** (no 24)

Comprobación rápida: solo el 13,5% de tus clientes llega a los 2 años (0,92²⁴ ≈ 0,135). Estás pagando publicidad por una permanencia promedio que casi nadie entrega.

## Error 2: Olvidaste el margen bruto

El LTV no es ingreso bruto, es margen. Un cliente no te deja $35/mes, te deja $35 × 70% = **$24,50/mes**.

## El número real

**LTV = (Precio × Margen) / Churn = ($35 × 0,70) / 0,08 = $306,25**

| Métrica | Tu cálculo | Real |
|---|---|---|
| Lifetime | 24 meses | 12,5 meses |
| LTV | $840 | **$306** |
| CAC | $290 | $290 |
| **LTV/CAC** | 2,9 | **1,06** |

No estás "por encima de 3 más o menos". Estás en 1,06: cada $1 invertido te devuelve $1,06 *en toda la vida del cliente*, en 12 meses. Eso no es rentabilidad escalable, es casi empate contable (y si suben los CPMs por la competencia en subastas, estás en pérdidas).

## Qué pasa con tus $10.000

- Clientes ganados: $10.000 / $290 ≈ **34 clientes**
- Recuperación total esperada: 34 × $306 ≈ **$10.400**
- **Payback del CAC: $290 / $24,50 ≈ 11,8 meses**

Quemas $10.000 hoy para recuperarlos en ~1 año, con margen de error de ~4%. Y el problema no es solo la métrica: con churn de 8%/mes, cada cliente que escalas se fuga antes de amortizar la adquisición. Escalar publicidad sobre un balde con fugas multiplica la fuga, no el crecimiento.

## Palancas, en orden de impacto

1. **Bajar churn a 4%** → LTV = $612, LTV/CAC ≈ 2,1 (payback ~6 meses)
2. **Bajar CAC a $150** (mejor creativo/oferta/segmentación) → LTV/CAC ≈ 2,0
3. **Subir precio a $50** (probablemente subestimado) → LTV = $437, LTV/CAC ≈ 1,5

Cualquier combinación de dos de estas te acerca a 3x.

## Plan revisado para este mes

- **No metas $10.000.** Destina **$1.000–1.500 a un test controlado** (2-3 ángulos de anuncio) solo para validar si puedes bajar el CAC de $290.
- **Dedica el resto del mes a churn:** entrevistas de cancelación, onboarding, señal de valor en las primeras 2 semanas (el churn del mes 1 suele concentrar el problema).
- **Regla de decisión:** escalar solo cuando LTV/CAC ≥ 3 y payback ≤ 6 meses con CAC estable en test repetidos.

Rentable hoy no es lo mismo que rentable a escala pagada. Con 1,06x, escalar es multiplicar un problema. Arregla el churn primero y la publicidad se convierte en una máquina; hoy es un agujero lento.