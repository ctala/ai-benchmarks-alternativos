# KAT Coder Air v2.5 — sales_outreach/campaign_optimization

- model_id: `kwaipilot/kat-coder-air-v2.5`
- success: True  | final: 7.58 | quality: 8.0
- latency_total: 10.352s | tokens_per_second: 197.8
- input_tokens: 309 | output_tokens: 2048

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



# 📊 Análisis de Campañas Google Ads - Último Mes

## 1. Métricas Calculadas

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---------|---------------------|------------------|------------------------|
| **CTR** | 3.00% | 4.00% | 6.00% |
| **CPC** | $1.40 | $0.38 | $3.56 |
| **CPA** | **$46.67** | $75.00 | $88.89 |
| **Conversion Rate** | 3.00% | 0.50% | 4.00% |
| **Signups/$** | 0.0214 | 0.0133 | 0.0113 |
| **Costo/100 signups** | $4,667 | $7,500 | $8,889 |

---

## 2. Recomendación: Escalar vs Pausar

### ✅ **ESCALAR: Campaña A (Landing Principal)**
- **CPA más bajo**: $46.67 (38% menos que B, 47% menos que C)
- **Mejor eficiencia de conversión**: 3% CVR con CPC razonable ($1.40)
- **Signups/$**: 0.0214 (mejor retorno por dólar)
- **Intención de compra alta**: Keywords transaccionales ("software gestión inventario")

### ⏸️ **PAUSAR: Campaña B (Blog Content)**
- **CPA más alto**: $75.00 (60% más caro que A)
- **CVR muy baja**: 0.5% (contenido informativo, no convierte)
- **Ineficiencia**: Gasta $1,800 para solo 24 signups
- **Uso adecuado**: El blog es para SEO orgánico, no para campañas de conversión directa

### ⚠️ **OPTIMIZAR (no pausar): Campaña C (Competidor