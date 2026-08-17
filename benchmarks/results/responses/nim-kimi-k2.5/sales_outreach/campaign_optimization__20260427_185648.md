# Kimi K2.5 (NIM) — sales_outreach/campaign_optimization

- model_id: `moonshotai/kimi-k2.5`
- success: True  | final: 7.5 | quality: 9.72
- latency_total: 78.318s | tokens_per_second: 26.1
- input_tokens: 283 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

 Aquí tienes el análisis completo de tus campañas:

## 1. Métricas Calculadas

| Métrica | Campaña A (Principal) | Campaña B (Blog) | Campaña C (Competidor) |
|---------|----------------------|------------------|------------------------|
| **CTR** | 3.0% | **4.0%** | **6.0%** |
| **CPC** | $1.40 | **$0.38** | $3.56 |
| **Conv. Rate** | **3.0%** | 0.5% | **4.0%** |
| **CPA** | **$46.67** | $75.00 | $88.89 |
| **Signups/$1,000** | 21.4 | 13.3 | 11.3 |

## 2. Decisión: Escalar vs Pausar

### 🚀 **ESCALAR: Campaña A** 
**Justificación numérica:**
- **CPA más bajo** ($46.67 vs $75 y $88.89)
- **Mayor volumen de conversiones** (45 signups = 50% del total)
- **Eficiencia de escala**: Por cada $1,000 gastados genera 21.4 signups vs 13.3 y 11.3 de las otras
- Equilibrio perfecto entre volumen (50k impresiones) y calidad (3% conv rate)

### ⏸️ **PAUSAR/REDUCIR 70%: Campaña B**
**Justificación numérica:**
- **CPA 60% más caro** que la Campaña A ($75 vs $46.67)
- **Tasa de conversión extremadamente baja** (0.5% vs 3-4% de las otras)
- Aunque el CPC es barato ($0.38), el tráfico es de **intención informacional** ("cómo gestionar"), no transaccional
- Estás pagando por lectores, no compradores potenciales

### ⚠️ **MANTENER/OPTIMIZAR: Campaña C**
**Justificación numérica:**
- **Mejor intención de compra**: Keywords de comparación tienen 2-3x más probabilidad de conversión final
- **CTR más alto** (6%): Indica relevancia perfecta entre anuncio y búsqueda
- Aunque el CPA es alto ($88.89), el **LTV de estos usuarios** suele ser mayor (ya buscan activamente cambiar de proveedor)

## 3. Redistribución del Presupuesto ($5,000)

Propuesta basada en eficiencia y potencial de escala:

| Campaña | Presupuesto | % | Estrategia |
|---------|-------------|---|------------|
| **A** | **$3,000** | 60% | Escalar volumen. Aumentar bids en keywords con CPA <$40 |
| **C** | **$1,500** | 30% | Optimizar, no escalar. Buscar reducir CPC a <$3.00 |
| **B** | **$500** | 10% | Modo "testing". Cambiar objetivo a remarketing o nurturing, no signups directos |

**Proyección de resultados con esta distribución:**
- Signups estimados: ~78-85 (vs 105 actuales, pero con CPA promedio de $58 vs $71 actual)
- O mejor: mantener 105 signups pero gastando $5,000 en lugar de $7,100 (ahorro del 30%)

## 4. A/B Tests Sugeridos para el Próximo Mes

### Campaña A (Landing Principal):
1. **Test de Propuesta de Valor**: 
   - Control: "Software de Gestión de Inventario"
   - Variant: "Reduce pérdidas de inventario un 30% en 30 días"
   
2. **Social Proof vs. Features**:
   - Testear landing con testimonios de restaurantes vs. landing con lista de integraciones

3. **Formulario corto vs. Wizard**:
   - Actual (probablemente): Email + Password
   - Test: Solo Email → onboarding posterior

### Campaña C (Competidor):
1. **Comparación directa en landing**:
   - Tabla comparativa "Nosotros vs [Competidor]" vs. Landing genérica
   
2. **Descuento por migración**:
   - Anuncio: "Migración gratuita desde [Competidor]" vs. actual
   
3. **Test de precios**:
   - Landing con pricing transparente vs. "Solicitar demo" (para filtrar mejor)

### Campaña B (Reestructuración total):
**Cambio de estrategia**: No usar para signups directos
- **Test**: Ofrecer **Lead Magnet** (ebook "Guía de inventario para restaurant