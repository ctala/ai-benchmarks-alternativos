# Claude Fable 5 (suscripción) — sales_outreach/campaign_optimization

- model_id: `claude-fable-5`
- success: True  | final: 7.22 | quality: 10.0
- latency_total: 37.744s | tokens_per_second: 72.6
- input_tokens: 2 | output_tokens: 2741

## Respuesta completa

# Análisis de campañas Google Ads

## 1. Métricas por campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** | 1,500/50,000 = **3.0%** | 4,800/120,000 = **4.0%** | 900/15,000 = **6.0%** |
| **CPC** | $2,100/1,500 = **$1.40** | $1,800/4,800 = **$0.38** | $3,200/900 = **$3.56** |
| **Conversion rate** | 45/1,500 = **3.0%** | 24/4,800 = **0.5%** | 36/900 = **4.0%** |
| **CPA** | $2,100/45 = **$46.67** | $1,800/24 = **$75.00** | $3,200/36 = **$88.89** |

⚠️ **Ojo:** gastaste $7,100 contra un presupuesto de $5,000. Hay un sobregiro de 42% que conviene revisar antes que cualquier optimización.

## 2. Cuál escalar, cuál pausar

**Escalar: Campaña A.**
- CPA más bajo ($46.67), casi la mitad de C.
- Conversion rate sólido (3%) con intención transaccional ("software gestión inventario" = ya buscan comprar).
- Genera el 43% de los signups (45/105) con solo el 30% del gasto.

**Pausar (como está hoy): Campaña B.**
- 4,800 clicks y solo 24 signups: conversion rate de 0.5%, 6x peor que A y 8x peor que C.
- El problema es la intención: "cómo gestionar inventario" es búsqueda informacional. Esa gente quiere aprender, no comprar. Estás pagando $0.38 por clicks que no convierten.
- No la mates del todo: ese tráfico barato sirve para **retargeting** (más abajo).

**Campaña C: mantener pero optimizar, no escalar todavía.**
- Tiene el mejor conversion rate (4%) y el mejor CTR (6%) — la intención es excelente.
- El problema es el CPC de $3.56 (2.5x el de A). Antes de escalar, hay que bajar ese costo: mejorar Quality Score, ajustar pujas, probar landing dedicada de comparación.
- Si bajas el CPC a ~$2.50, el CPA cae a ~$62 y ahí sí vale escalar.

## 3. Redistribución de los $5,000

| Campaña | Antes | Propuesta | Razón |
|---|---|---|---|
| A (Landing) | $2,100 | **$2,800** | Mejor CPA, escalar gradual (+33%, no duplicar de golpe — al escalar el CPA suele subir) |
| C (Competidor) | $3,200 | **$1,600** | Recortar a la mitad mientras optimizas CPC. Volumen limitado (15K impresiones = nicho pequeño) |
| B reconvertida → Retargeting | $1,800 | **$600** | Retargeting a visitantes del blog + lead magnet para capturar emails |
| **Total** | $7,100 | **$5,000** | |

**Proyección con la nueva distribución:**
- A: $2,800 / ~$47 CPA ≈ 60 signups (asumiendo CPA estable)
- C: $1,600 / ~$75 CPA optimizado ≈ 21 signups
- Retargeting: ~8-12 signups (típicamente CPA 30-50% menor que cold)
- **Total estimado: ~90 signups con $5,000** vs 105 con $7,100 actuales

Eficiencia: pasas de 14.8 a ~18 signups por cada $1,000. Menos volumen absoluto, pero 22% más eficiente y dentro de presupuesto.

**Dato que falta y necesitas:** ¿cuánto vale un signup? Si tu LTV por cliente pagado es $500 y convierte 20% de signups a pago, un CPA de $88 sigue siendo rentable y la respuesta cambia. Calcula CPA máximo aceptable = (LTV × conversion signup→pago) antes de cortar nada definitivamente.

## 4. A/B tests para el próximo mes

**Campaña A (la que escala — prioridad alta):**
1. **Headline de landing:** beneficio genérico vs cifra concreta ("Reduce 30% las pérdidas de inventario" vs "Software de gestión de inventario").
2. **Formulario de signup:** largo actual vs versión mínima (solo email). Con 3% de conversión hay espacio para llegar a 4-5%.

**Campaña C (optimizar CPC y conversión):**
3. **Landing dedicada de comparación** ("[Tu producto] vs [Competidor]: tabla comparativa") vs landing genérica actual. Quien busca "alternativa a X" quiere ver la comparación, no tu home. Esto sube Quality Score → baja CPC.
4. **Ad copy:** mencionar precio/diferenciador directo vs copy genérico.

**Campaña B reconvertida:**
5. **Lead magnet en el blog:** plantilla gratuita de inventario (Excel/Sheets) vs trial directo. La intención informacional convierte mejor a email que a signup. Luego nutres por email hacia el producto.

**Regla para los tests:** uno a la vez por campaña, mínimo 2 semanas o ~100 conversiones por variante antes de declarar ganador. Con tus volúmenes actuales (24-45 signups/mes por campaña), los tests de landing van a necesitar 3-4 semanas — paciencia, no cortes a la semana.