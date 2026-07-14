# MiniMax M2.5 — sales_outreach/campaign_optimization

- model_id: `minimax/minimax-m2.5`
- success: True  | final: 8.75 | quality: 10.0
- latency_total: 33.377s | tokens_per_second: 61.4
- input_tokens: 291 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente util, proporcionando un análisis detallado y recomendaciones prácticas basadas en métricas.

## Respuesta completa

# Análisis Completo de Campañas Google Ads

## 1. Métricas Calculadas

| Métrica | Campaña A | Campaña B | Campaña C |
|---------|-----------|-----------|-----------|
| **CTR** | 1,500 / 50,000 = **3.0%** | 4,800 / 120,000 = **4.0%** | 900 / 15,000 = **6.0%** |
| **CPC** | $2,100 / 1,500 = **$1.40** | $1,800 / 4,800 = **$0.375** | $3,200 / 900 = **$3.56** |
| **CPA** | $2,100 / 45 = **$46.67** | $1,800 / 24 = **$75.00** | $3,200 / 36 = **$88.89** |
| **Conv. Rate** | 45 / 1,500 = **3.0%** | 24 / 4,800 = **0.5%** | 36 / 900 = **4.0%** |

### Tabla Resumen Visual

```
                    A (Landing)    B (Blog)      C (Competidor)
CTR                 ███████░░░    █████████░    ████████████  6%
CPC                 █████░░░░░    ██░░░░░░░░    ███████░░░░  $
CPA                 █████████░    ████████████  █████████████ $$$

Conv. Rate          ███████░░░    ██░░░░░░░░    ████████████  %
```

---

## 2. Recomendación: Escalar vs. Pausar

### 🟢 **ESCALAR: Campaña A**
```
Costo por signup: $46.67  ← EL MÁS BAJO
Tasa conversión:  3.0%    ← ACEPTABLE
Volumen:          45 signups/mes
```

**Justificación numérica:**
- Si duplicamos presupuesto a $4,200 → proyectamos **~90 signups**
- ROI proyectado: **$46.67 por cliente** (muy eficiente)
- Keywords con intención directa = usuarios calificados

### 🔴 **PAUSAR: Campaña B**
```
Costo por signup: $75.00  ← 60% más caro que A
Tasa conversión:  0.5%    ← CRÍTICAMENTE BAJA
Volumen:          24 signups/mes
```

**Justificación numérica:**
- 4,800 clics pero solo 24 conversiones
- Cada signup cuesta $75 vs $46.67 de A
- **Diferencia: $28.33 extra por cada signup** ($680 desperdiciados en el mes)

### 🟡 **MANTENER/MONITOREAR: Campaña C**
```
Costo por signup: $88.89  ← EL MÁS ALTO
Tasa conversión:  4.0%    ← LA MÁS ALTA
Volumen:          36 signups/mes
```

**Justificación:**
- El alto CTR (6%) indica que los competidores son relevantes
- Conversión del 4% confirma calidad del tráfico
- **Pregunta clave:** ¿El valor de vida del cliente justifica $88.89?

---

## 3. Redistribución del Presupuesto ($5,000)

### Nueva Asignación Propuesta

| Campaña | Presupuesto Actual | Nuevo Presupuesto | Cambio |
|---------|-------------------|-------------------|--------|
| A (Landing) | $2,100 (42%) | **$3,200 (64%)** | +$1,100 |
| B (Blog) | $1,800 (36%) | **$300 (6%)** | -$1,500 |
| C (Competidor) | $3,200 (64%) | **$1,500 (30%)** | -$1,700 |

### Proyección de Resultados

```
CAMPANA A (escalada):
  $3,200 / $46.67 = 68-69 signups (vs. 45 actuales)
  +52% incremento en conversiones

CAMPANA B (reducida al mínimo):
  $300 / $0.375 = 800 clics de prueba
  Mantener para收集 datos de test A/B

CAMPANA C (reducida, sin pausar):
  $1,500 / $88.89 = 16-17 signups
  Mantener presencia en búsquedas de competencia
```

### Diagrama de Redistribución

```
ANTES                          DESPUÉS
┌─────────────────────┐       ┌─────────────────────┐
│ A ████████████ 42%  │       │ A ██████████████ 64%│
│ B ████████    36%  │       │ B █              6% │
│ C █████████████ 64% │       │ C ██████        30% │
└─────────────────────┘       └─────────────────────┘
```

---

## 4. A/B Tests para el Próximo Mes

### 🔬 Test Prioritarios (orden de impacto)

#### TEST 1: Campaña B - Landing Page
```
HIPÓTESIS: "La baja conversión (0.5%) se debe a desconexión 
            entre contenido del blog y el signup"

Variante A: [Control]  → Landing actual
Variante B:           → Landing con "problemas de inventario" 
                        como headline + testimonials específicos
```

| Elemento | Control | Variante B |
|----------|---------|------------|
|