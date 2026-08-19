# MiniMax M2.7 (directo) — sales_outreach/campaign_optimization

- model_id: `MiniMax-M2.7`
- success: True  | final: 7.3 | quality: 8.0
- latency_total: 29.824s | tokens_per_second: 66.0
- input_tokens: 291 | output_tokens: 1968

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

# 📊 Análisis Completo: Campañas Google Ads

---

## 1. MÉTRICAS CALCULADAS

| Métrica | Campaña A | Campaña B | Campaña C |
|---|---|---|---|
| **CTR** | 1,500/50,000 = **3.0%** | 4,800/120,000 = **4.0%** | 900/15,000 = **6.0%** |
| **CPC** | $2,100/1,500 = **$1.40** | $1,800/4,800 = **$0.38** | $3,200/900 = **$3.56** |
| **CPA** | $2,100/45 = **$46.67** | $1,800/24 = **$75.00** | $3,200/36 = **$88.89** |
| **Conv. Rate** | 45/1,500 = **3.0%** | 24/4,800 = **0.5%** | 36/900 = **4.0%** |
| **Costo/Signup** | $46.67 | $75.00 | $88.89 |

---

## 2. ESCALAR vs. PAUSAR

```
🏆 GANADORA CLARA → Campaña A (Landing principal)
❌ EN TERRENO GRIS → Campaña B (Blog content)
⏸️ PAUSAR → Campaña C (Competidor)
```

### Justificación numérica:

**🔴 PAUSAR Campaña C:**
- Tiene el **CPA más alto** ($88.89) → 90% más caro que la Campaña A
- Tiene el **CPC más alto** ($3.56) → 2.5x más caro que la A
- Gastó **$3,200** (64% del presupuesto) y solo generó **36 signups**
- Las búsquedas por marca de competidor son **intención baja** (muchos son curiosos, no compradores)

**🟡 Campaña B — No pausar, pero sí optimizar:**
- CTR alto (4%) pero **conversión pésima (0.5%)** → el tráfico es relevante, el problema está en el funnel
- CPG más barato ($0.38) pero solo 24 signups
- Invierte **$1,800** y retorna menos de la mitad que la A

**🟢 Campaña A — ESCALAR:**
- CPA más bajo ($46.67) = **el doble de eficiente** que la C
- Conversion rate del 3.0% (6x mejor que la B)
- Keywords con **intención transactiva** ("software gestión inventario")
- El público ya sabe lo que quiere

---

## 3. REDISTRIBUCIÓN DEL PRESUPUESTO ($5,000)

```
DISTRIBUCIÓN ACTUAL:
  A: $2,100  (42%) → 36 signups
  B: $1,800  (36%) → 24 signups
  C: $3,200  (64%) → 36 signups
  ──────────────────────────
  Total: $5,000       → 96 signups  |  CPA promedio: $52.08
```

```
NUEVA DISTRIBUCIÓN PROPUESTA:
  A: $3,500  (70%) → ~75 signups estimados
  B: $1,000  (20%) → pruebas de optimización
  C: $500    (10%) → mantener MINIMO (datos históricos)
  ──────────────────────────
  Total: $5,000       → ~85-100+ signups | CPA estimado: ~$40-50
```

### Lógica:

| Campaña | Cambio | Razón |
|---|---|---|
| **A → +$1,400** | Subir ставки + duplicar tráfico | CPA más bajo, keywords transactivas |
| **B → -$800** | Reducir pero mantener | Probar nuevos landing pages antes de matar |
| **C → -$2,700** | Reducir a 10% | Datos históricos insuficientes para justificar el gasto |

> **Nota:** Si tras 2 semanas la Campaña A mantiene CPA bajo $50, entonces reasignar el 20% restante a B para tests.

---

## 4. A/B TESTS RECOMENDADOS PARA EL PRÓXIMO MES

### 🧪 Test 1 — Campaña A (Prioridad ALTA)
```
Hipótesis: "¿Un trial gratuito de 14 días vs. demo en vivo mejora conversión?"

  Variante A: "Prueba gratis 14 días" (control actual)
  Variante B: "Agenda una demo personalizada"
  Variante C: "Ver plan precios + prueba gratis"
```
**Métrica de éxito:** Conversion rate > 3.5%

---

### 🧪 Test 2 — Campaña B (Prioridad ALTA)
```
Problema: 0.5% de conversión = el tráfico llega pero NO convierte.
Hipótesis: "El problema no es el anuncio, es la landing."

  Variante A: Landing de blog (control actual)
  Variante B: Redirigir a landing de producto con CTA claro
  Variante C: Popup de lead magnet ("Guía gratuita de inventario")
```
**Métrica de éxito:** Conversion rate > 2%

---

### 🧪 Test 3 — Campaña C (Prioridad MEDIA)
```
"Si insistes en mantener competitor keywords, prueba esto:"

  Variante A: "Guía de migración desde [competidor]" (lead magnet)
  Variante B: "Compara + pide demo gratis"
  Variante C: Restringir a audiencias que visitaron tu web (remarketing)
```
**Métrica de éxito:** CPA < $60

---

### 🧪 Test 4 — Campaña B (Segmentación)
```
Probar audiencias lookalike basadas en los 45 signups de la Campaña A.

  Segmento 1: Remarketing (visitaron tu web)
  Segmento 2: Lookalike 1% de compradores
  Segmento 3: Audiencias in-market "Business Management Software"
```
**Métrica de éxito:** CPA < $50 en audiencias optimizadas

---

## RESUMEN EJECUTIVO

```
┌─────────────────────────────────────────────────────────┐
│  ACCIÓN INMEDIATA                                       │
│  • Campaña C → PAUSAR o reducir a $500                  │
│  • Campaña A → ESCALAR un 67% más (es tu motor de ventas)│
│  • Campaña B → REDUCIR y hacer test de landing          │
│                                                          │
│  META PARA EL PRÓXIMO MES:                              │
│  • Mantener CPA Campaña A bajo $50                      │
│  • Elevar Conv. Rate Campaña B de 0.5% a 2%+           │
│  • Target global: 100+ signups con CPA < $45            │
└─────────────────────────────────────────────────────────┘
```

El dato más valioso que tienes es claro: **la intención de búsqueda transactiva (Campaña A) te cuesta la mitad que la educativa (Campaña B) y un tercio menos que las competidoras (Campaña C).** Enfócate donde el usuario ya sabe que tiene un problema y busca solución.