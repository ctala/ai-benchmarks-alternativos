# Muse Glimmer 30B — sales_outreach/campaign_optimization

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.57 | quality: 10.0
- latency_total: 48.598s | tokens_per_second: 62.2
- input_tokens: 309 | output_tokens: 3025
- judge_score: 5.0 | justificación: 

## Respuesta completa

**1. Métricas por campaña**

**Campaña A - Landing principal**
* CTR = Clicks / Impresiones = 1.500 / 50.000 = **3.0%**
* CPC = Costo / Clicks = 2.100 / 1.500 = **$1.40**
* Conversion Rate = Signups / Clicks = 45 / 1.500 = **3.0%**
* CPA = Costo / Signups = 2.100 / 45 = **$46.67**

**Campaña B - Blog content**
* CTR = 4.800 / 120.000 = **4.0%**
* CPC = 1.800 / 4.800 = **$0.38**
* Conversion Rate = 24 / 4.800 = **0.5%**
* CPA = 1.800 / 24 = **$75.00**

**Campaña C - Competidor**
* CTR = 900 / 15.000 = **6.0%**
* CPC = 3.200 / 900 = **$3.56**
* Conversion Rate = 36 / 900 = **4.0%**
* CPA = 3.200 / 36 = **$88.89**

### Resumen

| Campaña | CTR | CPC | CR Clicks | CPA |
|---------|-----|-----|-----------|-----|
| A Landing | 3.0% | $1.40 | 3.0% | $46.67 |
| B Blog | 4.0% | $0.38 | 0.5% | $75.00 |
| C Competidor | 6.0% | $3.56 | 4.0% | $88.89 |

**2. Qué escalar y qué pausar**

**Escalar: Campaña A**
Es la más eficiente en CPA. $46.67 por signup vs $75 y $88.89 de las otras. Tiene un buen equilibrio entre CPC moderado y CR 3.0%. Es tráfico de intención comercial alta: "software gestion inventario", "inventario pymes".

**Pausar / Eliminar: Campaña B**
Aunque tiene el CPC más barato $0.38 y CTR 4%, el tráfico es no cualificado. CR 0.5% y CPA $75. Es contenido informativo que no convierte. Estás pagando por clicks baratos que no se convierten.

**Mantener con optimización: Campaña C**
Tiene el mejor CTR 6% y mejor CR 4.0%, lo que confirma intención muy alta. El problema es el CPC $3.56 que empuja el CPA a $88.89. No se pausa, se optimiza. Es defensa de marca y captura de demanda existente.

**3. Redistribución del presupuesto $5.000/mes**

Actualmente gastaste $7.100 para 105 signups. Con $5.000 y la eficiencia de A puedes superar eso.

Propuesta conservadora y segura:
* **Campaña A: $3.500 = 70%** -> ~75 signups esperados a CPA actual
* **Campaña C: $1.500 = 30%** -> ~17 signups esperados a CPA actual
* **Campaña B: $0** -> Pausada

Signups proyectados ~92 con $5.000 vs 105 con $7.100 antes. Eficiencia +35%.

Alternativa agresiva si quieres maximizar volumen:
* Campaña A: $4.000 = 80%
* Campaña C: $1.000 = 20%
* Campaña B: $0

**4. A/B Tests para el próximo mes**

**Para Campaña A - Escalar con calidad**
* **A/B Landing:** Versión actual vs landing con prueba social + testimonios de pymes + CTA "Prueba gratis 14 días". Hipótesis: subir CR de 3% a 4%+.
* **A/B Anuncio:** Headline orientado a beneficio "Reduce faltantes de stock en 30 días" vs orientado a feature "Software de inventario para pymes". Test en RSA.

**Para Campaña C - Bajar CPC y CPA**
* **A/B Anuncio Competidor:** "Alternativa a [Competidor]" vs "[Competidor] vs Nosotros: Comparativa honesta". Test de intención y calidad de clic.
* **A/B Extensiones:** Con vs sin extensión de llamada y formulario. Los usuarios de competidor buscan decisión rápida.

**Para Campaña B - Solo si quieres rescatarla**
* **Destino del clic:** Blog actual vs Landing con lead magnet "Checklist inventario restaurante". Si el CR no sube por encima de 1.5%, confirmar pausa.
* **Palabras negativas:** Añadir lista de negativas de intención informativa: "gratis", "plantilla excel", "curso", "definición". Esto sube CPC pero baja CPA.

Métrica de control: Mantén CPA objetivo < $60. Si Campaña A mantiene CPA < $50, puedes moverle más presupuesto de C a A mes a mes.

¿Quieres que te modele el impacto en signups si bajas el CPC de C un 20% con mejora de Quality Score?