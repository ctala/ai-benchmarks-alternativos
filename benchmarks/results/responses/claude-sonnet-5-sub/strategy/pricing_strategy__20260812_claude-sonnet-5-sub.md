# Claude Sonnet 5 (suscripción) — strategy/pricing_strategy

- model_id: `claude-sonnet-5`
- success: True  | final: 4.51 | quality: 5.0
- latency_total: 98.55s | tokens_per_second: 83.7
- input_tokens: 2 | output_tokens: 8244

## Entrada exacta (lo que recibió el modelo)

**user:**

Mi SaaS de gestion de inventario tiene estos datos:
- CAC actual: $120
- LTV promedio: $840 (14 meses * $60/mes)
- Churn mensual: 7%
- 200 clientes actuales
- Competidores cobran entre $29 y $149/mes
- Mi costo por usuario es ~$8/mes

Estoy considerando subir el precio de $60 a $89/mes.
Analiza:
1. Calcula el LTV/CAC ratio actual y como cambiaria
2. Estima el impacto en churn (usa benchmarks de la industria SaaS)
3. Modela 3 escenarios: optimista, realista, pesimista
4. Dame tu recomendacion con numeros concretos
5. Sugiere una estrategia de implementacion (grandfather, gradual, etc)


## Respuesta completa

# Análisis: subida de precio $60 → $89/mes

## 1. LTV/CAC actual vs. proyectado

Primero una corrección necesaria: el LTV de $840 que usas es **revenue bruto** (14.3 meses × $60), no profit. Para un ratio LTV/CAC que sirva para decidir, hay que restar el costo de servir ($8/mes).

| Métrica | Cálculo | Valor |
|---|---|---|
| Vida útil promedio (1/churn) | 1/0.07 | 14.3 meses |
| LTV revenue (bruto) | $60 × 14.3 | $857 |
| Margen de contribución/usuario | $60 − $8 | $52/mes |
| **LTV real (margen)** | $52 × 14.3 | **$743** |
| **LTV/CAC actual (real)** | $743 / $120 | **6.2x** |

6.2x ya está muy por encima del benchmark sano de SaaS (3x = saludable, 5x+ = excelente). Esto te dice algo importante: **tienes margen de sobra para subir precio antes de que el ratio se ponga en riesgo.**

Con $89/mes y el mismo churn (7%, hipotético — ver sección 2):

| Métrica | Cálculo | Valor |
|---|---|---|
| Margen de contribución/usuario | $89 − $8 | $81/mes |
| LTV real (margen) | $81 × 14.3 | $1,157 |
| LTV/CAC | $1,157 / $120 | **9.6x** |

## 2. Impacto en churn (benchmarks de la industria)

El aumento es de **+48.3%** ($60→$89). Esto es un salto grande, no una ajuste marginal. Benchmarks relevantes (Price Intelligently/ProfitWell, elasticidad SMB SaaS):

- Subidas de 10-15% bien comunicadas: churn adicional <5% one-time, impacto marginal en steady-state.
- Subidas de 30%+ sin grandfathering: pueden generar 15-25% de cancelaciones one-time en la base existente, más un incremento de 1-5pp en el churn mensual steady-state (herramientas SMB con baja fricción de switching son más elásticas que enterprise).
- Un dato a tu favor: $89 sigue dentro del rango competitivo ($29-$149), en el percentil ~60. No es un precio "fuera de mercado", pero sí es un salto porcentual fuerte desde tu ancla actual.

Con eso, modelo dos efectos separados: **shock churn** (cancelaciones únicas al momento del anuncio) y **churn steady-state nuevo** (la tasa mensual que queda instalada después).

## 3. Tres escenarios

| | Optimista | Realista | Pesimista |
|---|---|---|---|
| Churn steady-state | 7% → 8% (+1pp) | 7% → 9.5% (+2.5pp) | 7% → 12% (+5pp) |
| Shock inicial (cancelaciones one-time) | 5% | 12% | 25% |
| Clientes tras shock (de 200) | 190 | 176 | 150 |
| Revenue mensual (× $89) | $16,910 | $15,664 | $13,350 |
| Costo servir (× $8) | $1,520 | $1,408 | $1,200 |
| **Margen mensual** | **$15,390** | **$14,256** | **$12,150** |
| Margen actual (baseline $60) | $10,400 | $10,400 | $10,400 |
| **Delta de margen** | **+48%** | **+37%** | **+17%** |
| Vida útil nueva (1/churn) | 12.5 meses | 10.5 meses | 8.3 meses |
| LTV/CAC (real, con nuevo churn) | 8.4x | 7.1x | 5.6x |

El dato clave: **incluso en el escenario pesimista, el margen mensual sube 17% y el LTV/CAC se mantiene en 5.6x** (todavía muy por encima del piso de 3x). No hay escenario razonable donde este cambio destruya valor.

## 4. Recomendación

**Sube el precio. La matemática lo respalda con margen de sobra, incluso castigando fuerte el churn.**

Números que la sostienen:
- Ratio actual (6.2x) está sobrado — tienes espacio de pricing power que no estás capturando.
- El peor caso modelado (churn casi duplicado, 25% de shock) sigue dejando más margen absoluto que hoy.
- $89 no te saca del rango competitivo, te posiciona a media tabla, no en el extremo caro.

Lo que NO recomiendo es aplicar el salto completo de golpe a toda la base sin mitigación — no porque la matemática lo prohíba, sino porque el escenario pesimista (25% shock) es evitable con mejor ejecución, y evitarlo te deja más cerca del optimista que del pesimista.

## 5. Estrategia de implementación

**Grandfathering segmentado + validación por cohorte**, en este orden:

1. **Nuevos clientes → $89 inmediato.** Cero riesgo de churn shock porque no hay base que reaccionar. Esto te da una cohorte real para medir el churn steady-state verdadero (sección 2 es estimación, esto es dato) sin apostar tu base actual.

2. **Clientes actuales → grandfather con fecha de vencimiento.** Anuncia con 45-60 días de antelación: "tu precio actual se mantiene hasta [fecha], después pasa a $89". Esto reduce el shock churn drásticamente frente a un aumento sin aviso (la gente cancela por sorpresa, no por precio) y te da tiempo de mostrar valor antes del corte.

3. **Revisa a los 90 días con la cohorte nueva.** Si el churn real de los clientes que entraron a $89 está cerca del escenario optimista/realista (8-9.5%), aplica el mismo trato a la base grandfathered con confianza. Si se acerca al pesimista (12%+), ajusta: precio intermedio ($75) o refuerza el paquete de valor antes de subir.

4. **Considera fragmentar en vez de subir plano.** Si tu costo de $8/usuario permite margen, evalúa crear un tier "Pro" a $89 con 1-2 features adicionales reales (reportes avanzados, más usuarios, soporte prioritario) y dejar un tier básico a $60-69. Esto convierte la conversación de "me suben el precio" a "hay un upgrade", que reduce fricción psicológica de forma significativa — mismo revenue objetivo, menos resistencia.

5. **No toques el 30% de clientes de mayor riesgo de churn sin trato especial.** Si tienes visibilidad de qué cuentas están cerca de cancelar (uso bajo, tickets de soporte, etc.), no los metas en el mismo aumento — o los pierdes gratis y ensucias la medición de la cohorte.

El punto de decisión real no es "¿subo o no?" — con estos números, subes. Es **"¿grandfather con deadline o big-bang?"**, y el grandfather es estrictamente mejor: mismo precio final, menos riesgo, y datos reales de la cohorte nueva antes de apostar la base completa de 200 clientes.