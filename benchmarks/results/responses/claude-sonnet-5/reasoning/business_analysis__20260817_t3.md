# Claude Sonnet 5 — reasoning/business_analysis

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 7.96 | quality: 9.8
- latency_total: 55.917s | tokens_per_second: 94.1
- input_tokens: 254 | output_tokens: 5264
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando análisis detallados y acciones concretas basadas en los datos.

## Entrada exacta (lo que recibió el modelo)

**user:**

Analiza estos datos de mi SaaS:

Enero: 1,200 usuarios, $18,000 MRR, 45 churns, CAC $85, LTV $420
Febrero: 1,350 usuarios, $20,250 MRR, 52 churns, CAC $92, LTV $415
Marzo: 1,480 usuarios, $22,200 MRR, 68 churns, CAC $78, LTV $408

Necesito:
1. Calcula las metricas clave (churn rate, growth rate, LTV/CAC ratio, net revenue retention)
2. Identifica tendencias preocupantes
3. Sugiere 3 acciones concretas basadas en los datos
4. Proyecta abril si las tendencias continuan


## Respuesta completa

# Análisis de Métricas SaaS - Q1

## 1. Métricas Clave Calculadas

### Tabla resumen

| Métrica | Enero | Febrero | Marzo |
|---|---|---|---|
| ARPU (MRR/usuarios) | $15.00 | $15.00 | $15.00 |
| Churn Rate* | — | 4.33% | 5.04% |
| Growth Rate (usuarios) | — | 12.5% | 9.63% |
| Growth Rate (MRR) | — | 12.5% | 9.63% |
| Nuevos usuarios brutos | — | 202 | 198 |
| LTV/CAC Ratio | 4.94x | 4.51x | 5.23x |
| NRR (aproximado)** | — | ~95.7% | ~95.0% |

*Churn rate calculado como: churns del mes / usuarios al inicio del mes (usuarios fin del mes anterior). No pude calcular el churn de enero por falta de dato de diciembre.

**NRR es una **aproximación**, no el cálculo real. El NRR verdadero requiere saber cuánto MRR se perdió específicamente de clientes que cancelaron vs. cuánto se ganó por upsells/expansión de clientes existentes. Asumí ARPU constante ($15) para estimar el MRR perdido por churn. **Recomiendo trackear esto directamente** — es una de tus métricas más importantes y actualmente es un punto ciego.

---

## 2. Tendencias Preocupantes 🚩

### 🔴 Crítica: Adquisición estancada + Churn creciente
Los usuarios nuevos brutos se mantienen casi iguales (202 → 198) mientras el churn crece agresivamente (52 → 68, +30%). Esto significa que **tu crecimiento neto se está desacelerando por dos frentes simultáneamente**: no consigues más clientes nuevos, Y pierdes más de los que tienes.

### 🟠 LTV en declive constante
420 → 415 → 408. Caída sostenida de ~$6-7/mes. Esto usualmente indica:
- Clientes de menor calidad/fit entrando
- Erosión de precio o downgrades
- Producto perdiendo "sticky-ness"

### 🟡 El LTV/CAC "mejorado" es una ilusión
El ratio subió a 5.23x en marzo, pero **no por buena salud del negocio** — subió porque el CAC bajó (posiblemente canal más barato pero de menor calidad) mientras el LTV también cayó. Es un ratio "mejorando" mientras ambos componentes se deterioran. Esto es más preocupante que alentador.

### 🟡 Churn rate acelerando más rápido que el crecimiento
El churn rate crece +0.71pp mes a mes mientras el growth rate de usuarios decrece -2.87pp. Si esta tijera continúa, en pocos meses el churn absoluto podría superar a los nuevos usuarios, generando **crecimiento negativo**.

---

## 3. Acciones Concretas

### Acción 1: Auditoría inmediata de cohortes por canal de adquisición
Cruza el CAC de febrero (más alto, $92) y marzo (más bajo, $78) contra el churn de esos mismos clientes en los meses siguientes. **Hipótesis**: el canal más barato de marzo está trayendo usuarios de menor calidad que churnean más rápido. Si se confirma, el "ahorro" en CAC es falso — estás comprando churn futuro.

### Acción 2: Implementar entrevistas de cancelación estructuradas (exit surveys)
Con 68 churns en marzo (vs 45 en enero), necesitas data cualitativa YA. Pregunta específicamente: (a) razón de cancelación, (b) tiempo desde signup hasta churn, (c) qué feature esperaban vs. obtuvieron. Esto te dirá si el problema es onboarding, producto, o precio.

### Acción 3: Crear un programa de "save" para clientes en riesgo
Dado que no tienes tracking de NRR real, implementa un health score básico (uso del producto, login frequency, tickets de soporte) para identificar clientes en riesgo ANTES de que cancelen. Con el ARPU actual ($15) y el volumen de churn, cada punto porcentual de churn evitado representa aproximadamente $220-300 en MRR retenido mensualmente.

---

## 4. Proyección Abril (si tendencias continúan)

**Supuestos usados:**
- Nuevos usuarios brutos: tendencia plana/decreciente (202→198), proyecto ~194
- Churn rate: incremento lineal de +0.71pp mensual → ~5.75%
- ARPU: se mantiene constante en $15 (patrón muy consistente en los 3 meses)
- LTV: continúa declive lineal de ~-7/mes

| Métrica | Proyección Abril |
|---|---|
| Churns absolutos | ~85 |
| Nuevos usuarios brutos | ~194 |
| Usuarios totales | **~1,589** |
| MRR | **~$23,835** |
| Growth rate usuarios | ~7.4% (sigue desacelerando) |
| LTV proyectado | ~$401 |
| CAC | Incierto (volátil: 85→92→78) — usar $85 como estimado conservador |
| LTV/CAC proyectado | ~4.7x |

### ⚠️ Nota de honestidad estadística
Esta proyección usa solo 3 puntos de datos, lo cual es **estadísticamente frágil**. El CAC en particular es demasiado volátil para proyectar con confianza — necesitas al menos 6 meses de datos para identificar si hay estacionalidad o si es ruido genuino. Tómalo como un escenario direccional, no una predicción precisa.

**El mensaje central de abril**: si nada cambia, seguirás creciendo, pero cada mes un poco más lento, con menos usuarios nuevos entrando y más saliendo por la puerta de atrás. La ventana para actuar sobre el churn es AHORA, antes de que la tijera se cierre completamente.