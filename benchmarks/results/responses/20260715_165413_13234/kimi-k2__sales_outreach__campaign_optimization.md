# Kimi K2 — sales_outreach/campaign_optimization

- model_id: `moonshotai/kimi-k2`
- success: True  | final: 8.65 | quality: 10.0
- latency_total: 39.792s | tokens_per_second: 44.9
- input_tokens: 284 | output_tokens: 1786
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando análisis detallados y recomendaciones prácticas para la optimización de campañas.

## Respuesta completa

Aquí tienes el análisis completo de tus campañas:

## 1. Métricas Calculadas

| Métrica | Campaña A (Principal) | Campaña B (Blog) | Campaña C (Competidor) |
|---------|----------------------|------------------|------------------------|
| **CTR** | 3.0% | 4.0% | 6.0% |
| **CPC** | $1.40 | $0.38 | $3.56 |
| **CPA** | **$46.67** ✅ | $75.00 | $88.89 |
| **Conv. Rate** | 3.0% | 0.5% ⚠️ | 4.0% ✅ |

## 2. Decisión: Escalar vs Pausar

**ESCALAR: Campaña A** 
- **Justificación**: Tiene el **CPA más bajo ($46.67)** y un conversion rate sólido (3%). Las keywords muestran intención de compra directa ("software", "pymes") y llevan a landing principal. Por cada $1,000 invertidos, obtienes ~21 signups vs solo 11-13 en las otras.

**OPTIMIZAR/REDUCIR: Campaña B**
- **Problema**: CPA de $75 con CVR de solo 0.5%. Aunque el CPC es barato ($0.38), estás pagando por tráfico de tope de embudo (investigación) que no convierte. Estás gastando $1,800 para 24 signups cuando esa misma plata en la Campaña A te daría ~38 signups.

**MANTENER: Campaña C**
- Aunque tiene el CPA más alto ($88.89), el CVR del 4% es excelente. Las keywords de competidor suelen ser caras pero cierran ventas. Es tu "quality over quantity".

## 3. Redistribución del Presupuesto ($5,000)

```
Campaña A (Principal):   $3,000 (60%)  ← Escalar volumen de keywords ganadoras
Campaña C (Competidor):  $1,500 (30%)  ← Optimizar para bajar ese CPC de $3.56
Campaña B (Blog):        $500  (10%)   ← Testing o pausar temporalmente
```

**Razonamiento**: Con $3,000 en Campaña A proyectarías ~64 signups/mes vs los 45 actuales. La Campaña B solo justifica $500 si la usas para remarketing o testing de ofertas de lead nurturing.

## 4. A/B Tests Sugeridos

**Para Campaña A (Principal):**
- **Landing**: Formulario corto (email solo) vs formulario completo (email+empresa+tamaño)
- **Headline**: "Software de Inventario" vs "Deja de perder stock" (dolor vs beneficio)
- **Keywords**: Agregar modificadores de precio ("software inventario precio", "inventario pymes barato")

**Para Campaña B (Si decides mantenerla):**
- **Oferta**: Cambiar CTA de "Sign up" a "Descargar checklist gratuito" → nurturar vía email
- **Landing**: Blog post vs Landing de captura dedicada
- **Audiencia**: Excluir visitantes que ya vieron página de precios (evitar pagar por usuarios calificados)

**Para Campaña C (Competidor):**
- **Ad Copy**: "Alternativa a [Competidor]" vs "[Competidor] vs Nosotros: Comparativa 2024"
- **Landing**: Comparativa lado a lado vs "Por qué migrar"
- **Horario**: Pujar más fuerte en horarios de oficina (9-18h) cuando toman decisiones

**Recomendación urgente**: La Campaña B está diluyendo tu eficiencia. Si en 2 semanas no baja el CPA a <$55 con los tests sugeridos, pausarla y redistribuir esos $1,300 a la Campaña A te daría ~28 signups adicionales mensuales.