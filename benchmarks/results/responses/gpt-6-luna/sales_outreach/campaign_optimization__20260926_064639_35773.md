# GPT-6 Luna — sales_outreach/campaign_optimization

- model_id: `openai/gpt-6-luna`
- success: True  | final: 9.02 | quality: 10.0
- latency_total: 15.759s | tokens_per_second: 124.7
- input_tokens: 261 | output_tokens: 1965

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

Asumo que cada signup es una conversión y que los costos están en la misma moneda.

### 1. Métricas por campaña

| Campaña | CTR | CPC | CPA por signup | Tasa de conversión (signups/clicks) |
|---|---:|---:|---:|---:|
| **A — Landing principal** | 3,0% | $1,40 | **$46,67** | 3,0% |
| **B — Blog content** | 4,0% | **$0,38** | $75,00 | 0,5% |
| **C — Competidor** | **6,0%** | $3,56 | $88,89 | **4,0%** |

### 2. Qué escalar y qué pausar

- **Escalaría A gradualmente:** tiene el CPA más bajo ($46,67), así que es la campaña más eficiente para generar signups. Conviene aumentar su presupuesto por etapas y comprobar que el CPA no se deteriore.
- **Pausaría B en su configuración actual:** consigue tráfico barato, pero convierte solo el 0,5% de los clics y su CPA ($75) es bastante peor que el de A. La retomaría como prueba con otra propuesta de conversión, no simplemente con más presupuesto.
- **Mantendría C con presupuesto controlado:** tiene la mejor tasa de conversión (4%), pero también el CPC más caro y el CPA más alto ($88,89). Puede captar búsquedas de alta intención, pero no la escalaría antes de mejorar su costo.

### 3. Propuesta para distribuir los $5.000

Una distribución inicial, priorizando eficiencia y dejando margen para aprender:

| Campaña | Presupuesto propuesto |
|---|---:|
| A — Landing principal | **$3.500** |
| B — Blog content, solo como prueba revisada | **$500** |
| C — Competidor | **$1.000** |
| **Total** | **$5.000** |

Los $500 de B serían un test limitado, no una continuación automática de la campaña actual. Si el objetivo es maximizar signups a corto plazo y no se quiere experimentar, usaría una opción más conservadora: **$4.000 en A, $1.000 en C y $0 en B**.

Como referencia muy aproximada, aplicar los CPA históricos al primer reparto implicaría alrededor de **93 signups**. No es una predicción garantizada: al aumentar o reducir presupuestos, los CPA pueden cambiar.

**Importante:** el gasto reportado suma **$7.100** ($2.100 + $1.800 + $3.200), por encima del presupuesto mensual de $5.000. Antes de implementar la distribución, revisaría si el presupuesto indicado corresponde a otro período o si hubo gasto adicional.

### 4. A/B tests para el próximo mes

- **Campaña A — Landing:** probar un titular orientado al beneficio frente a uno centrado en funcionalidades; también comparar formulario corto frente a formulario actual. Medir CPA y calidad de los signups.
- **Campaña B — Contenido:** comparar un CTA a “Solicitar demo” frente a una oferta de menor compromiso, como una guía o checklist. También probar una landing específica por tema en lugar de enviar todo el tráfico a una página general.
- **Campaña C — Competidor:** comparar anuncios centrados en “alternativa” frente a “comparativa”, y probar una landing que destaque diferencias concretas frente a una landing genérica. Evitar sugerir afiliación con el competidor.
- **En todas:** cambiar una variable a la vez y evaluar principalmente **CPA y calidad del signup**, no solo CTR. Asegurarse de que la medición de conversiones sea consistente entre campañas.