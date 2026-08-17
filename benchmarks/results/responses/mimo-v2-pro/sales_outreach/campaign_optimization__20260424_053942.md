# MiMo-V2-Pro — sales_outreach/campaign_optimization

- model_id: `xiaomi/mimo-v2-pro`
- success: True  | final: 7.15 | quality: 9.0
- latency_total: 37.162s | tokens_per_second: 55.1
- input_tokens: 548 | output_tokens: 2048
- judge_score: 4.6 | justificación: 

## Respuesta completa

# 📊 Análisis de Campañas Google Ads

---

## 1. Métricas Calculadas

| Métrica | **Campaña A** (Landing) | **Campaña B** (Blog) | **Campaña C** (Competidor) |
|---|---|---|---|
| **CTR** | 3.00% | 4.00% | 6.00% |
| **CPC** | $1.40 | $0.38 | $3.56 |
| **Tasa Conversión** | 3.00% | 0.50% | 4.00% |
| **CPA** | $46.67 | $75.00 | $88.89 |
| **Costo/Signup** | **$46.67** ✅ | $75.00 | $88.89 |

> 📌 **Dato clave:** Con tu presupuesto actual de $7,100 estás obteniendo **105 signups** totales. Tu presupuesto real es $5,000 → necesitas decidir dónde cortar.

---

## 2. Decisión: Escalar vs. Pausar

### ✅ ESCALAR → Campaña A (Landing principal)

```
CPA más bajo:     $46.67 vs $75.00 vs $88.89
Conversión alta:  3.00% (muy sólida para SaaS)
CPC razonable:    $1.40
```

**¿Por qué?** Es la mejor relación costo-resultado. Cada dólar adicional aquí rinde más signups que en cualquier otra campaña.

---

### ⚠️ OPTIMIZAR (no pausar todavía) → Campaña B (Blog)

```
CTR excelente:    4.00% (hay interés real)
CPC bajísimo:     $0.38 (mucho tráfico barato)
Pero conversión:  0.50% (1 de cada 200 clics)
CPA:              $75.00 (60% más caro que A)
```

**¿Por qué no pausar?** El tráfico es **informativo**, no transaccional. Pero es un embudo de topo de funnel valioso. El problema no es la campaña, es la **conversión del blog**.

---

### 🛑 PAUSAR → Campaña C (Competidor)

```
CPA más alto:     $88.89 (casi el doble que A)
CPC más caro:     $3.56 (2.5x más que A)
Costo total:      $3,200 para solo 36 signups
```

**¿Por qué pausar?**
- Convierte bien en porcentaje (4%), pero es **demasiado caro** por signup
- Con $3,200 en la Campaña A obtendrías **~68 signups** (vs. los 36 actuales)
- Estás perdiendo **32 signups potenciales** al mes por mantenerla

---

## 3. Redistribución del Presupuesto ($5,000/mes)

### Propuesta:

| Campaña | Presupuesto | % | Justificación |
|---|---|---|---|
| **A** (Landing) | **$3,200** | 64% | Escalar el ganador |
| **B** (Blog) | **$1,300** | 26% | Mantener topo de embudo |
| **C** (Competidor) | **$500** | 10% | Solo brand keywords muy específicas |
| **Total** | **$5,000** | 100% | |

### Proyección estimada:

```
                    Antes          Después
Signups Campaña A:    45      →     ~68  (+51%)
Signups Campaña B:    24      →     ~17  (-29%, pero más eficiente)
Signups Campaña C:    36      →     ~6   (solo keywords premium)
─────────────────────────────────────────────
TOTAL SIGNUPS:       105      →     ~91
COSTO TOTAL:       $7,100    →   $5,000  (-30%)
CPA PROMEDIO:       $67.62   →    $54.95 (-19%)
```

> 💡 **Resultado:** Pierdes ~14 signups, pero **ahorras $2,100/mes** y mejoras tu CPA un 19%. Es un trade-off inteligente.

---

## 4. A/B Tests Sugeridos para el Próximo Mes

### 🔬 Campaña A (Alta prioridad)

| Test | Variable | Hipótesis |
|---|---|---|
| **A1** | **Headline del anuncio** | "Gestiona tu inventario fácil" vs. "Ahorra 10h/semana en inventario" (beneficio cuantificado) |
| **A2** | **Landing page** | Página actual vs. versión con video demo arriba del fold |
| **A3** | **CTA del signup** | "Prueba gratis 14 días" vs. "Empieza ahora, sin tarjeta" |

### 🔬 Campaña B (Mejorar conversión)

| Test | Variable | Hipótesis |
|---|---|---|
| **B1** | **CTA en el blog** | Pop-up al 60% del artículo vs. banner sticky vs. inline CTA |
| **B2** | **Lead magnet** | Artículo normal vs. "Descarga checklist de gestión de inventario gratis" (captura email) |
| **B3** | **Retargeting** | Agregar audiencia de remarketing de visitantes del blog que no convirtieron |

### 