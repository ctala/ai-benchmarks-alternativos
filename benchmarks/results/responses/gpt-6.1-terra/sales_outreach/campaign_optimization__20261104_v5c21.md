# GPT-6.1 Terra — sales_outreach/campaign_optimization

- model_id: `openai/gpt-6.1-terra`
- success: True  | final: 7.26 | quality: 8.0
- latency_total: 9.996s | tokens_per_second: 81.7
- input_tokens: 261 | output_tokens: 817

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

## 1. Métricas por campaña

La tasa de conversión es **signups ÷ clics** y el CPA es **costo ÷ signups**.

| Campaña | CTR | CPC | Conversión | CPA |
|---|---:|---:|---:|---:|
| **A — Landing principal** | 3,00% | $1,40 | 3,00% | $46,67 |
| **B — Blog** | 4,00% | $0,38 | 0,50% | $75,00 |
| **C — Competidor** | 6,00% | $3,56 | 4,00% | $88,89 |

El gasto del mes fue **$7.100**, es decir, $2.100 por encima del presupuesto mensual indicado.

## 2. Qué escalar y qué pausar

- **Escalar A gradualmente.** Tiene el CPA más bajo: $46,67 por signup, un **38% menor que B** y un **48% menor que C**. Convirtió el 3% de sus clics, frente al 0,5% de B.
- **Pausar B temporalmente** o reducirla a un presupuesto experimental mínimo. Aunque atrae clics baratos y tiene mejor CTR que A, solo convierte 1 de cada 200 clics. Su CPA de $75 es un 61% mayor que el de A.
- **Mantener C bajo control, sin escalarla todavía.** Tiene la mayor conversión y el mejor CTR, pero su CPC de $3,56 eleva el CPA a $88,89. Conviene conservarla solo si los signups de competidor generan clientes de suficiente calidad para justificar ese costo.

Esta recomendación se basa en **costo por signup**, no en rentabilidad: faltan datos sobre cuántos signups se convierten en clientes y su valor.

## 3. Redistribución de $5.000/mes

| Campaña | Presupuesto propuesto | Motivo |
|---|---:|---|
| A | **$3.500** | Priorizar la fuente con menor CPA. |
| B | **$0** | Pausarla hasta mejorar la conversión de las visitas del blog. |
| C | **$1.500** | Mantener presencia y medir la calidad de los signups. |
| **Total** | **$5.000** | |

Como referencia, si se mantuvieran exactamente los CPA actuales, esta distribución produciría aproximadamente **92 signups**: 75 de A y 17 de C. Es una proyección, no una garantía: al aumentar la inversión, A podría agotar su demanda o encarecerse.

## 4. A/B tests para el próximo mes

1. **Landing de A:** titular y propuesta de valor orientados a “gestión de inventario para pymes” frente al mensaje actual. Medir tasa de signup y CPA.
2. **Formulario de A:** versión actual frente a una con menos campos. Medir signups y también su calidad posterior.
3. **Anuncios de C:** mensaje centrado en diferenciadores frente a otro centrado en beneficios concretos, respetando las políticas de marcas de Google Ads. Medir CPC, tasa de conversión y CPA.
4. **Blog de B:** antes de reactivarla a escala, probar el CTA actual frente a uno contextual —por ejemplo, una plantilla de inventario o una demo— en una muestra controlada. Medir signups y su avance hacia cliente.

Ejecutaría primero los tests de **A y C**, cambiando una variable principal por prueba y evitando declarar ganadores con pocos datos. También revisaría el seguimiento de conversiones y añadiría métricas de **cliente adquirido y valor generado** para decidir el presupuesto del mes siguiente.