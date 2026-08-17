# Kimi K2.7 Code — strategy/pricing_strategy

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 5.58 | quality: 7.59
- latency_total: 853.549s | tokens_per_second: 9.6
- input_tokens: 204 | output_tokens: 8192
- judge_score: 4.4 | justificación: 

## Respuesta completa

 Aquí tienes un análisis completo, con números concretos y una recomendación práctica.

---

## 1. LTV/CAC actual y con el nuevo precio

### Métricas actuales
- **ARPU:** \$60/mes
- **Costo por usuario:** \$8/mes
- **Margen bruto por usuario:** \$52/mes (86,7%)
- **Churn mensual:** 7% → vida media = 1/0,07 = **14,3 meses**
- **LTV (revenue):** \$60 × 14,3 = **\$840**
- **LTV/CAC actual:** \$840 / \$120 = **7,0x**
- **LTV/CAC ajustado por margen:** \$52 / 0,07 = \$743 → **6,2x**

> **Nota importante:** como tienes un costo por usuario (\$8), el ratio más preciso para decisiones es el **LTV/CAC ajustado por margen bruto**. El ratio “revenue-based” sobrestima la rentabilidad real.

### Si subes a \$89/mes
- **Nuevo ARPU:** \$89/mes
- **Nuevo margen bruto por usuario:** \$81/mes (91%)
- **Payback de CAC actual:** \$120 / \$52 = **2,3 meses**
- **Nuevo payback de CAC:** \$120 / \$81 = **1,5 meses**

Si el churn **se mantuviera en 7%**:
- Nuevo LTV (revenue) = \$89 / 0,07 = **\$1.271**
- Nuevo LTV/CAC (revenue) = **10,6x**
- Nuevo LTV/CAC (margen) = \$81 / 0,07 = \$1.157 → **9,6x**

**Pero el churn no se quedará igual.** Un aumento de precio del 48% casi siempre aumenta la rotación, al menos temporalmente.

---

##