# Grok 4.3 — sales_outreach/campaign_optimization

- model_id: `x-ai/grok-4.3`
- success: True  | final: 8.57 | quality: 9.74
- latency_total: 13.488s | tokens_per_second: 101.1
- input_tokens: 385 | output_tokens: 1363

## Respuesta completa

**1. Métricas calculadas**

| Campaña | CTR | CPC | Conv. Rate | CPA |
|---------|-----|-----|------------|-----|
| **A**   | 3.0% | $1.40 | 3.0% | **$46.67** |
| **B**   | 4.0% | $0.38 | **0.5%** | $75.00 |
| **C**   | **6.0%** | $3.56 | 4.0% | $88.89 |

**2. Qué escalar y pausar**

- **Escalar: Campaña A**  
  Es claramente la más eficiente. Tiene el **CPA más bajo** ($46.67) y una tasa de conversión 6x superior a la B. Además, las keywords son de alta intención comercial.

- **Pausar o reducir drásticamente: Campaña B**  
  Aunque tiene el CPC más barato y mucho volumen, su tasa de conversión es muy baja (0.5%). Está generando tráfico poco cualificado. El CPA de $75 es 60% más caro que A.

- **Campaña C**: Está en zona gris. Tiene buen CTR y conversión, pero el CPA es el más alto ($88.89) y el CPC es muy caro. Solo la mantendría si el LTV del cliente justifica pagar más por estas conversiones (tráfico de competidor suele convertir bien a largo plazo).

**3. Redistribución del presupuesto ($5,000)**

Recomendación:

| Campaña | Presupuesto sugerido | % | Justificación |
|---------|----------------------|---|---------------|
| **A**   | $2,800              | 56% | Mejor CPA + intención alta |
| **C**   | $1,400              | 28% | Buena conversión, pero controlar CPC |
| **B**   | $800                | 16% | Solo para mantener algo de volumen/top of funnel |
| **Total** | **$5,000**        | 100% | - |

Alternativa más agresiva: Pausar B completamente y repartir $3,200 a A y $1,800 a C.

**4. A/B Tests sugeridos (próximo mes)**

**Campaña A (prioridad alta):**
- Headline del landing: "Software de inventario para pymes" vs "Control de inventario simple y rápido"
- CTA del formulario: "Probar gratis 14 días" vs "Ver demo de 10 minutos"
- Extensión de llamada vs WhatsApp

**Campaña C:**
- Copy de anuncio: "Mejor alternativa a [Competidor]" vs "[Competidor] vs Nuestra solución (comparativa real)"
- Página de destino: Landing específica vs página de comparativa

**General:**
- Probar **Smart Bidding (Maximize Conversions o Target CPA)** vs CPC manual en A y C.
- Testear remarketing a usuarios que llegaron desde B pero no convirtieron.

**Resumen rápido:** Enfócate en A, reduce fuerte B, y usa C de forma controlada.