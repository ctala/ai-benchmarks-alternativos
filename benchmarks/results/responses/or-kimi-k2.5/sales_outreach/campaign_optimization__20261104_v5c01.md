# Kimi K2.5 — sales_outreach/campaign_optimization

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 8.3 | quality: 10.0
- latency_total: 71.685s | tokens_per_second: 24.4
- input_tokens: 285 | output_tokens: 1749

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

## 1. Métricas por Campaña

| Métrica | Fórmula | Campaña A | Campaña B | Campaña C |
|---------|---------|-----------|-----------|-----------|
| **CTR** | Clicks/Impresiones | **3.0%** | **4.0%** | **6.0%** |
| **CPC** | Costo/Clicks | **$1.40** | **$0.375** | **$3.56** |
| **CPA** | Costo/Signups | **$46.67** | **$75.00** | **$88.89** |
| **Conv. Rate** | Signups/Clicks | **3.0%** | **0.5%** | **4.0%** |

### 📊 Visualización de KPIs clave

```
CPA (menor es mejor):     A ████████████████░░░░ $46.67  ✓ MEJOR
                          B ████████████████████████████ $75.00
                          C ████████████████████████████████ $88.89

Conv. Rate (mayor es mejor): C ████████████████████░░░░ 4.0%  ✓ MEJOR
                             A ███████████████░░░░░░░░░ 3.0%
                             B ██░░░░░░░░░░░░░░░░░░░░░░ 0.5%  ✗ PEOR
```

---

## 2. Decisión: Escalar vs Pausar

### 🚀 **ESCALAR: Campaña A** (Landing Principal)

| Argumento | Dato |
|-----------|------|
| **Mejor CPA** | $46.67 (47% más barata que B, 48% más barata que C) |
| **CPA dentro de benchmark** | Para B2B SaaS, CPA < $50 es saludable |
| **Equilibrio CTR + Conv. Rate** | 3% + 3% = intención de compra real |
| **Eficiencia de presupuesto** | Cada $1 en A genera 0.021 signups vs 0.013 en B, 0.011 en C |

**Intención de búsqueda:** "software gestion inventario" = **transaccional** (quiere comprar)

---

### ⏸️ **PAUSAR: Campaña B** (Blog Content)

| Problema | Dato |
|----------|------|
| **CPA inviable** | $75, **60% más caro** que A |
| **Conv. rate críticamente baja** | 0.5% = 1 signup cada 200 clicks |
| **Tráfico de baja calidad** | Alto volumen, cero intención de conversión |
| **Costo de oportunidad** | Esos $1,800 en A generarían **38 signups** extra |

**Intención de búsqueda:** "como gestionar inventario" = **informativa** (quiere aprender, no comprar)

> ⚠️ **No descartar el contenido**, pero no usar Google Ads para TOFU (Top of Funnel). Mejor distribución orgánica o redes sociales.

---

### ⚖️ **MANTENER/OPTIMIZAR: Campaña C** (Competidor)

| Ventaja | Desafío |
|---------|---------|
| **Mayor conv. rate** (4.0%) | CPA más alto ($88.89) |
| Intención de compra explícita | CPC prohibitivo ($3.56) |
| Usuarios en evaluación activa | Mercado limitado (15K impresiones) |

**Veredicto:** Nicho valioso pero **caro**. Optimizar antes de escalar.

---

## 3. Redistribución del Presupuesto ($5,000)

### Propuesta: Modelo 70-20-10

| Campaña | Asignación | Monto | Acción |
|---------|-----------|-------|--------|
| **A (Escalar)** | 70% | **$3,500** | Aumentar bids 20%, expandir keywords similares |
| **C (Optimizar)** | 20% | **$1,000** | Reducir 69%, testear landing pages específicas vs competidor |
| **Test/Reserva** | 10% | **$500** | Nuevas keywords de intención transaccional |

### Proyección de resultados (vs mes actual)

| Escenario | Signups Est. | CPA Promedio |
|-----------|-----------|--------------|
| **Actual** ($7,100 gastado) | 105 | $67.62 |
| **Nuevo** ($5,000 optimizado) | **92-98** | **$51-54** |

> 💡 **Con el mismo presupuesto reducido**, mantenemos ~90% de los signups pero con **CPA 24% menor**

### Keywords a expandir en A:
- "sistema inventario pymes"
- "control stock software"
- "programa inventario barato"
- "[competidor] alternativa" (mover desde C si funciona)

---

## 4. A/B Tests para Próximo Mes

### 🎯 **Prioridad Alta (Semana 1-2)**

| Test | Campaña | Hipótesis | Métrica de éxito |
|------|---------|-----------|------------------|
| **Landing: Demo vs. Free Trial** | A | Signups cualificados > volumen | CPA de *activación* (no solo signup) |
| **Formulario: 3 campos vs. 5 campos** | A | Reducir fricción aumenta conv. rate 0.5% | Conv. rate > 3.5% manteniendo CPA |
| **Headline específica vs. genérica** | C | "[Competidor] vs Nosotros: tabla comparativa" reduce bounce | Conv. rate > 5% |

### 📊 **Prioridad Media (Semana 3-4)**

| Test | Campaña | Hipótesis |
|------|---------|-----------|
| **Horario de puja** | A | Pymes buscan 9am-6pm, fines de semana desperdician 15% |
| **Device bid adjustment** | A | Mobile: -30% (B2B se decide en desktop) |
| **Ad copy: Precio vs. Sin precio** | A | Transparencia filtra clicks no calificados, mejora conv. rate |

### 🔬 **Prioridad Baja / Innovación**

| Test | Descripción |
|------|-------------|
| **Remarketing segmentado** | Usuarios de Campaña B (blog) → sequence de 3 anuncios educativos → landing de demo |
| **Campaña D: "Precio"** | Keywords "[software] precio", "cuanto cuesta" — test con $500 reserva |

---

## 📋 Dashboard de Decisión: Resumen Ejecutivo

```
┌─────────────────────────────────────────┐
│  ESCALA A        │  PAUSA B  │  AJUSTA C │
│  $3,500 (70%)    │  $0 (0%)  │  $1,000   │
│                  │           │  (20%)    │
├─────────────────────────────────────────┤
│  META MES 2: 90+ signups | CPA <$55   │
│  KPI NORTE: CPA de ACTIVACIÓN, no solo  │
│  signup (mide calidad real)             │
└─────────────────────────────────────────┘
```

### ¿Quieres que profundice en algún punto?
- Modelo de atribución para medir el "assisted" de la Campaña B
- Estrategia de remarketing para recuperar tráfico de blog
- Scripts automatizados de puja para Campaña C