# Qwen 3.6 27B base (OpenRouter FP8) — business_audit/retention_sobre_100_interpretacion

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 5.62 | quality: 6.0
- latency_total: 62.83s | tokens_per_second: 51.7
- input_tokens: 143 | output_tokens: 3250

## Respuesta completa

No, tu interpretación no es correcta. Esa métrica es casi seguro **Net Revenue Retention (NRR)**, y aunque 114% es una cifra positiva, esconde una realidad estructural que no puedes ignorar si quieres escalar de forma sostenible.

### 🔍 Qué mide realmente el 114%
El NRR no mide cuántos clientes se quedan, sino **cuánto ingresos conservas y generas desde tu base existente**, independientemente de las bajas o altas. La fórmula es:
`NRR = (MRR inicial + Expansiones - Downgrades - MRR perdido por churn) / MRR inicial`

En tu caso:
- Perdiste 4 de 40 clientes → **10% de churn mensual de clientes**.
- Los que se quedaron subieron de plan → generaron un +14% de ingresos adicionales.
- El resultado neto: `100% - 10% + 14% = 114%`.

El 114% es un **efecto compensación**, no una medida de fidelización.

### 📉 Retención de clientes vs. Retención de ingresos
| Métrica | Tu caso | Qué dice realmente |
|--------|---------|-------------------|
| **Retención de clientes** | 36/40 = **90%** | Pierdes 1 de cada 10 cuentas al mes |
| **NRR (Retención de ingresos)** | **114%** | Tus expansiones cubren las pérdidas y sobran |
| **GRR (Gross Revenue Retention)** | *No calculado* | Ingresos que se quedan sin contar upsells. Probablemente <90% |

Son métricas distintas. Una base puede encogerse en número de cuentas mientras los ingresos crecen, pero eso tiene límites físicos y estratégicos.

### ⚠️ ¿Puedes dejar de preocuparte por el churn y solo captar?
**No. Y aquí está el porqué, con números:**

1. **Un churn mensual del 10% es insostenible.** Compuesto, equivale a perder ~72% de tu base en un año: `(1 - 0.10)^12 ≈ 28%`. Si no cierras fugas, dentro de 12 meses solo tendrás ~10 de esos 40 clientes originales.
2. **La expansión tiene techo.** No puedes seguir subiendo de plan a los mismos usuarios indefinidamente. Cuando el NRR depende casi exclusivamente de upsells para tapar churn, es crecimiento con máscara.
3. **El CAC se diluye.** Cada euro invertido en adquisición se desperdicia si el 10% de la base se renueva. Tu LTV/CAX se degrada silenciosamente, aunque el panel muestre crecimiento.
4. **La próxima fase lo revelará.** Cuando las expansiones se agoten o el mercado se sature, el NRR caerá por debajo del 100% y el crecimiento se frenará en seco. Captar más sin cerrar fugas es como llenar una cubeta con agujeros: gastas más en agua sin subir el nivel real.

### 🛠️ Qué deberías hacer ahora
- **Calcula tu GRR:** `(MRR inicial - Churn MRR - Downgrade MRR) / MRR inicial`. Si está bajo el 90%, tu producto, onboarding o pricing tiene fugas reales.
- **Segmenta el churn:** ¿Salieron por precio, por falta de uso, por soporte, por competencia? Los 4 clientes que se fueron no son un bloque homogéneo.
- **Equilibra la ecuación:** Un SaaS sano apunta a `NRR > 110-120%` **y** `GRR > 90-95%`. Hasta que el churn mensual de clientes no baje del 3-5%, tu esfuerzo debe ser ~60% retención/activación y ~40% adquisición.
- **No confundas “crecer” con “escalar bien”.** El NRR >100% es excelente, pero solo es saludable cuando el grueso proviene de renovación, no solo de expansiones que compensan salidas.

El 114% es una buena noticia, pero es una métrica de “efecto compensación”, no de salud estructural. Si ignoras el churn de clientes, estarás pagando por crecimiento ilusorio. 

¿Quieres que te ayude a desglosar cómo calcular tu GRR con tus datos reales o a mapear un framework rápido para identificar por qué se van ese 10% mensual?