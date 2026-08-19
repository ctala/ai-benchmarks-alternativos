# MiniMax M2.7 (directo) — sales_outreach/campaign_optimization

- model_id: `MiniMax-M2.7`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 36.179s | tokens_per_second: 56.6
- input_tokens: 291 | output_tokens: 2048

## Entrada exacta (lo que recibió el modelo)

**user:**

Tengo estos resultados de mi campana de Google Ads del ultimo mes:

Campana A (Landing principal):
- Impresiones: 50,000 | Clicks: 1,500 | Signups: 45 | Costo: $2,100
- Keywords: "software gestion inventario", "inventario pymes"

Campana B (Blog content):
- Impresiones: 120,000 | Clicks: 4,800 | Signups: 24 | Costo: $1,800
- Keywords: "como gestionar inventario", "problemas inventario restaurante"

Campana C (Competidor):
- Impresiones: 15,000 | Clicks: 900 | Signups: 36 | Costo: $3,200
- Keywords: "alternativa a [competidor]", "[competidor] vs"

Mi presupuesto total es $5,000/mes.

1. Calcula CTR, CPC, CPA, y conversion rate de cada campana
2. Cual campana debo escalar y cual pausar? Justifica con numeros
3. Como redistribuiria el presupuesto de $5,000?
4. Que A/B tests sugeririas para el proximo mes?


## Respuesta completa

# Análisis de Campañas Google Ads

## 1. Métricas Calculadas

| Métrica | Campaña A | Campaña B | Campaña C |
|---------|-----------|-----------|-----------|
| **CTR** | 3.00% | 4.00% | 6.00% |
| **CPC** | $1.40 | $0.375 | $3.56 |
| **CPA** | **$46.67** | $75.00 | $88.89 |
| **Conv. Rate** | 3.00% | 0.50% | 4.00% |
| **Signups/mes** | 45 | 24 | 36 |

> **Fórmula:** CTR = Clics/Impresiones | CPC = Costo/Clics | CPA = Costo/Signups | Conv. Rate = Signups/Clics

---

## 2. Escalar vs. Pausar

### 🚀 **ESCALAR: Campaña A**
| Razón | Dato |
|-------|------|
| **CPA más bajo** | $46.67 vs $75 y $88.89 |
| **Mayor volumen absoluto** | 45 signups (38% del total) |
| **Costo controlado** | $1.40 CPC con intención comercial clara |
| **Keywords de alta intención** | "software gestion inventario", "inventario pymes" = compradores listos |

### ⏸️ **PAUSAR: Campaña B**
| Razón | Dato |
|-------|------|
| **Conversion rate paupérrimo** | 0.5% (6x peor que A) |
| **El blog atrae researchers, no buyers** | Keywords informativos vs transaccionales |
| **Desperdicia presupuesto** | 4,800 clics → solo 24 signups |
| **CPA elevado** | $75 por signup en contenido educativo |

### 🔍 **MANTENER con testeo: Campaña C**
| Razón | Dato |
|-------|------|
| **Conv. rate competitivo** | 4.00% (mejor que A) |
| **Keywords de alto valor** | Buscadores de [competidor] = clientes insatisfechos = switchers |
| **Problema: CPC inflado** | $3.56 - demasiado caro para escalar ciego |
| **Volumen muy bajo** | Solo 900 clics |

---

## 3. Redistribución del Presupuesto ($5,000)

### Escenario Recomendado:

| Campaña | Actual | Propuesto | Cambio |
|---------|--------|-----------|--------|
| **A (Landing)** | $2,100 (42%) | **$3,500 (70%)** | +$1,400 |
| **B (Blog)** | $1,800 (36%) | **$500 (10%)** | -$1,300 |
| **C (Competidor)** | $3,200 (64%) | **$1,000 (20%)** | -$2,200 |

### Lógica:

```
Campaña A → Escalar agresivamente
├── Es el motor de signups
├── Probablemente aún no alcanzó el límite de impresiones
└── Duplicar inversión = duplicar resultados (testear 2x)

Campaña B → Reducir a retargeting mínimo
├── Ya tienes 120k impresiones de marca
└── Redirigir presupuesto a funnel inferior

Campaña C → Probar con presupuesto controlado
├── Reducir CPC objetivos con ajustes de puja
└── Si CPA baja de $70, entonces escalar
```

### Proyección de resultados:

| | Ahora | Con redistribución (estimado) |
|--|-------|-------------------------------|
| **Signups totales** | 105 | **130-150** |
| **CPA promedio** | $71.43 | **$55-$65** |

---

## 4. A/B Tests para el Próximo Mes

### 🔵 Campaña A - Optimizar Conversión

**Test 1: Landing Page**
```
Variante A: Current → Demo gratuita
Variante B: "Trial 14 días sin tarjeta" + CTAs de urgencia
Hipótesis: Reducir fricción aumenta signups un 15-25%
```

**Test 2: Formulario de Signup**
```
Variante A: Formulario de 5 campos
Variante B: Formulario de 2 campos (email + empresa)
Hipótesis: Menos campos = mayor completion rate
```

**Test 3: Copy en Anuncios**
```
Variante A: "Software de inventario para pymes"
Variante B: "Gestiona 10,000+ productos en 5 min"
Hipótesis: Claim específico > genérico
```

---

### 🟢 Campaña B - Rescatar el Blog

**Test 4: Remarketing vs. Nuevos Clics**
```
Variante A: Continuar igual
Variante B: 100% del budget a remarketing (usuarios que leyeron blog)
Hipótesis: Remarketing tiene 3-5x mejor conversión
```

---

### 🟡 Campaña C - Reducir CPC

**Test 5: Palabras Clave Competidoras**
```
Variante A: Broad match "[competidor] vs"
Variante B: Exact match "alternativa a [competidor]"
Hipótesis: Keywords exactas = menor CPC + mejor intención
```

**Test 6: Strategia de Puja**
```
Variante A: CPC manual actual
Variante B: Target CPA (configurar $70 como objetivo)
Hipótesis: Google optimiza hacia conversiones automáticamente
```

---

### 📊 Priorización Sug