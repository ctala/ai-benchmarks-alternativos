# Tencent Hy4 preview — strategy/pricing_strategy

- model_id: `tencent/hy4-preview`
- success: True  | final: 4.97 | quality: 5.0
- latency_total: 54.034s | tokens_per_second: 58.7
- input_tokens: 201 | output_tokens: 3172

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

## Análisis de Incremento de Precios: $60 → $89/mes

Primero, una corrección importante en tu LTV actual. Estás calculando LTV como **ingreso bruto** ($60 × 14 = $840), pero el LTV real debe usar **margen bruto**, no ingreso. Con costo de $8/usuario, tu margen es 86.7%.

---

## 1. LTV/CAC Ratio: Actual vs. Proyectado

### Situación Actual (Corregida)
```
ARPU:                    $60/mes
Margen Bruto:            ($60 - $8) / $60 = 86.67%
Gross Profit por usuario: $52/mes
Churn mensual:           7%
Vida promedio:           1 / 0.07 = 14.3 meses

LTV (correcto):          $52 / 0.07 = $742.86
CAC:                     $120
LTV/CAC Ratio:           6.19x
Tiempo de recuperación:  $120 / $52 = 2.3 meses
```

### Con Precio a $89 (asumiendo mismo churn)
```
ARPU:                    $89/mes
Margen Bruto:            ($89 - $8) / $89 = 91.01%
Gross Profit por usuario: $81/mes
Churn mensual:           7% (sin cambio)

LTV:                     $81 / 0.07 = $1,157
CAC:                     $120
LTV/CAC Ratio:           9.64x
Tiempo de recuperación:  $120 / $81 = 1.5 meses
```

**Mejora en LTV/CAC: de 6.19x a 9.64x (+56%)**

---

## 2. Impacto Estimado en Churn (Benchmarks SaaS)

Un aumento del **48.3%** ($60 → $89) es agresivo. Los benchmarks de la industria indican:

| Segmento | Aumento de Precio Típico | Impacto en Churn (corto plazo) | Impacto en Churn (largo plazo) |
|----------|-------------------------|-------------------------------|-------------------------------|
| SMB SaaS | 10-20% anual | +1.5-2x churn por 1-2 meses | +10-20% churn relativo |
| Mid-Market | 15-25% anual | +1.2-1.5x churn | +5-15% churn relativo |
| Enterprise | 5-15% anual | +1.1-1.3x churn | +3-10% churn relativo |

**Para tu caso (+48.3%):**

- **Corto plazo (meses 1-3):** Churn podría subir a **10-14% mensual** (vs. 7% actual)
- **Largo plazo (mes 6+):** Churn se estabiliza en **8.4-9.1% mensual** (+20-30% relativo)
- **Riesgo de churn inmediato:** 8-15% de clientes podrían cancelar al recibir el aviso

**Factores atenuantes:**
- Tu precio sigue dentro del rango competitivo ($29-$149)
- $89 está en el percentil 60 del mercado (no es el más caro)
- Costo de cambio (switching cost) para inventario es moderado-alto

---

## 3. Modelado de Escenarios

### Escenario Optimista (20% probabilidad)
**Supuestos:**
- Churn mensual: 7% → 8.4% (+20% relativo)
- 95% de clientes aceptan el aumento
- CAC se mantiene en $120

```
Nuevos Clientes:         200 × 0.95 = 190
ARPU:                    $89
Gross Profit:            $81/mes por usuario
Churn:                   8.4%
LTV:                     $81 / 0.084 = $964
LTV/CAC:                 8.03x

Ingreso Mensual:        190 × $89 = $16,910
vs. Actual ($12,000):   +$4,910/mes (+40.9%)

Ganancia Bruta Mensual: 190 × $81 = $15,390
vs. Actual ($10,400):   +$4,990/mes (+48%)
```

### Escenario Realista (55% probabilidad)
**Supuestos:**
- Churn mensual: 7% → 9.1% (+30% relativo)
- 85% de clientes aceptan
- CAC sube a $135 (más objeciones en ventas)

```
Nuevos Clientes:         200 × 0.85 = 170
ARPU:                    $89
Gross Profit:            $81/mes por usuario
Churn:                   9.1%
LTV:                     $81 / 0.091 = $890
LTV/CAC:                 6.59x

Ingreso Mensual:        170 × $89 = $15,130
vs. Actual ($12,000):   +$3,130/mes (+26.1%)

Ganancia Bruta Mensual: 170 × $81 = $13,770
vs. Actual ($10,400):   +$3,370/mes (+32.4%)

Payback:                 $135 / $81 = 1.7 meses
```

### Escenario Pesimista (25% probabilidad)
**Supuestos:**
- Churn mensual: 7% → 10.5% (+50% relativo)
- 70% de clientes aceptan
- CAC sube a $150

```
Nuevos Clientes:         200 × 0.70 = 140
ARPU:                    $89
Gross Profit:            $81/mes por usuario
Churn:                   10.5%
LTV:                     $81 / 0.105 = $771
LTV/CAC:                 5.14x

Ingreso Mensual:        140 × $89 = $12,460
vs. Actual ($12,000):   +$460/mes (+3.8%)

Ganancia Bruta Mensual: 140 × $81 = $11,340
vs. Actual ($10,400):   +$940/mes (+9%)

Payback:                 $150 / $81 = 1.85 meses
```

---

## 4. Recomendación con Números Concretos

### ✅ RECOMENDACIÓN: PROCEDER CON EL AUMENTO

**Valor Esperado (ponderado por probabilidad):**
```
Ingreso Mensual Esperado: (0.20 × $16,910) + (0.55 × $15,130) + (0.25 × $12,460)
                        = $3,382 + $8,322 + $3,115
                        = $14,819/mes

vs. Actual:            $12,000/mes
Incremento esperado:   +$2,819/mes (+23.5%)
Incremento anual:      +$33,828/año
```

**Razones clave:**

1. **Incluso el escenario pesimista es mejor que el status quo** (+$940/mes en ganancia bruta)
2. **LTV/CAC se mantiene saludable** en todos los escenarios (5.14x - 9.64x vs. benchmark de 3x)
3. **Payback period mejora** de 2.3 a 1.5-1.85 meses
4. **Margen bruto sube** de 86.7% a 91.0%

**Número crítico a monitorear:** Si el churn mensual supera **12.6%**, el LTV cae por debajo del actual ($742). Ese es tu punto de no retorno.

---

## 5. Estrategia de Implementación Recomendada

### Enfoque: **Grandfathering + Aumento Gradual para Nuevos**

#### Fase 1: Nuevos Clientes (Inmediato)
```
Día 1: Subir precio a $89 SOLO para nuevos clientes
       - Actualizar página de precios
       - Actualizar material de ventas
       - No comunicar a clientes actuales todavía
```

#### Fase 2: Grandfathering para Existentes (Mes 1-3)
```
Clientes actuales: Mantener $60/mes por 6 meses
Comunicación:     "Bloqueamos tu precio actual como agradecimiento"
                  "Renovación en [fecha]: tu precio se mantendrá en $60
                   hasta [fecha + 6 meses], luego será $89"

Oferta de upgrade: 3 meses gratis si cambian a plan anual a $89
                  (Incentiva compromiso y reduce churn)
```

#### Fase 3: Transición (Mes 6-9)
```
Mes 6:  Clientes grandfathered reciben aviso de 60 días
Mes 7:  Ofrecer $75/mes (precio intermedio) como opción de "lealtad"
Mes 8:  Aumento efectivo a $89 para quienes no tomaron anual
Mes 9:  Evaluar churn real vs. proyectado
```

#### Tácticas de Mitigación de Churn

| Táctica | Implementación | Impacto Esperado |
|---------|---------------|------------------|
| **Anual prepago** | 2 meses gratis ($890/año vs. $1,068) | Reduce churn 40-60% |
| **Plan intermedio** | $75/mes para indecisos | Retiene 15-25% de los que se irían |
| **Upgrade de features** | Añadir $20+ de valor percibido antes del aumento | Justifica precio, reduce objeciones |
| **Segmentación** | No aumentar a clientes con <3 meses o en riesgo | Protege cohortes nuevas |

#### Métricas de Seguimiento (Dashboard)
```
Semanal:
- Churn rate de clientes grandfathered vs. nuevos
- Tasa de conversión a planes anuales
- Nuevas ventas a $89 (¿cae el volumen?)

Mensual:
- LTV/CAC real (no proyectado)
- Net Revenue Retention (NRR)
- ARPU por cohorte
- CAC payback period
```

#### Plan de Contingencia
```
Si churn > 12% en mes 3:
→ Pausar grandfathering, ofrecer $75 a todos
→ Revertir nuevos clientes a $75 también

Si churn > 15% en mes 6:
→ Revertir a $69 (aumento del 15%, más aceptable)
→ Enfocarse en reducir CAC para compensar
```

---

## Resumen Ejecutivo

| Métrica | Actual | Proyectado (Realista) | Cambio |
|---------|--------|----------------------|--------|
| Precio | $60 | $89 | +48.3% |
| Clientes | 200 | 170 | -15% |
| Ingreso Mensual | $12,000 | $15,130 | +26.1% |
| Ganancia Bruta | $10,400 | $13,770 | +32.4% |
| LTV | $743 | $890 | +19.8% |
| LTV/CAC | 6.19x | 6.59x | +6.5% |
| Margen Bruto | 86.7% | 91.0% | +4.3pp |

**Decisión:** Sí, sube el precio. El valor esperado anual es **+$33,828** con riesgo controlado mediante grandfathering y monitoreo cercano del churn.