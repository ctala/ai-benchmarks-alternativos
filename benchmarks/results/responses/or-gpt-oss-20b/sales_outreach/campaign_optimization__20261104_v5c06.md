# GPT-OSS 20B — sales_outreach/campaign_optimization

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.24 | quality: 10.0
- latency_total: 19.359s | tokens_per_second: 121.9
- input_tokens: 309 | output_tokens: 2360

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

**1. Métricas por campaña**

| Campaña | Impresiones | Clicks | Signups | Costo ($) | CTR | CPC ($) | CPA ($) | Tasa de conversión (signups/clk) |
|---------|-------------|--------|---------|-----------|-----|---------|---------|---------------------------------|
| **A – Landing principal** | 50 000 | 1 500 | 45 | 2 100 | **3 %** | **1,40** | **46,67** | **3 %** |
| **B – Blog content** | 120 000 | 4 800 | 24 | 1 800 | **4 %** | **0,38** | **75,00** | **0,5 %** |
| **C – Competidor** | 15 000 | 900 | 36 | 3 200 | **6 %** | **3,56** | **88,89** | **4 %** |

*(Se usan redondeos a dos decimales donde corresponde.)*

**2. ¿Qué escalar y qué pausar?**

| Campaña | Observaciones |
|---------|---------------|
| **A – Landing principal** | <br>• **CPA más bajo** ($46,67) – la mejor relación coste‑conversión.<br>• **CTR y tasa de conversión decentes** (3 %).<br>• **CPC razonable** ($1,40).<br>→ **Escalar la mayor parte del presupuesto**. |
| **B – Blog content** | <br>• **CPA alto** ($75) y **tasa de conversión muy baja** (0,5 %).<br>• **CPC bajo**, pero la mayor parte del gasto se pierde en clics que no se convierten.<br>→ **Pausar o reducir drásticamente** mientras se trabaja en la optimización (landing, copy, segmentación). |
| **C – Competidor** | <br>• **Tasa de conversión alta** (4 %) y **CTR alto** (6 %).<br>• Sin embargo **CPC y CPA muy altos** ($3,56 y $88,89).<br>• Puede ser valiosa para leads de alta intención, pero el coste por adquisición es mayor que A. <br>→ **Mantener un presupuesto mínimo** o usarlo solo si el margen por venta es significativamente mayor que en A. |

**3. Redistribución del presupuesto de $5 000**

Con el objetivo de maximizar conversiones y mantener un CPA bajo, la distribución recomendada es:

| Campaña | % del presupuesto | Monto ($) | Comentario |
|---------|-------------------|-----------|------------|
| **A – Landing principal** | **80 %** | **4 000** | Aporta la mayor cantidad de conversiones al menor coste. |
| **C – Competidor** | **15 %** | **750** | Se mantiene un pequeño “punto de ruptura” para captar leads de alta intención sin sobrecargar el coste. |
| **B – Blog content** | **5 %** | **250** | Se reserva una fracción mínima para seguir probando ideas sin comprometer el presupuesto. |

*Resultados esperados con esta asignación (suponiendo que las métricas actuales se mantengan sin deterioro):*

- Campaña A: 4 000 / 1,40 ≈ **2 857 clics → 86 conversiones**  
- Campaña C: 750 / 3,56 ≈ **211 clics → 8 conversiones**  
- Campaña B: 250 / 0,38 ≈ **658 clics → 3 conversiones**  

Total aproximado: **≈ 97 conversiones** – una mejora respecto a la actual (105 con 7 100 $) pero dentro del presupuesto de 5 000 $.

**4. Sugerencias de A/B tests para el próximo mes**

| Área | Test | Objetivo |
|------|------|----------|
| **Anuncios** | 1. Variar headlines con palabras clave de intención alta (“adquisición”, “mejor software de inventario”).<br>2. Probar llamadas a la acción (CTA) distintas: “Prueba gratis”, “Descarga demo”, “Solicita presupuesto”. | Mejorar CTR y la relevancia del anuncio. |
| **Landing page (Campaña A)** | 1. Formularios más breves (solo email + teléfono).<br>2. Incluir prueba social (testimonios de pymes).<br>3. Agregar video corto explicativo. | Aumentar la tasa de conversión (signups/clk). |
| **Landing page (Campaña C)** | 1. Comparativa visual de features frente al competidor.<br>2. Badge de “100% de satisfacción”. | Incrementar la percepción de valor y disminuir CPA. |
| **Landing page (Campaña B)** | 1. Rediseño con CTA visible en la parte superior.<br>2. Contenido de “lead magnet” (ebook, checklist). | Mejorar la tasa de conversión, convertir clics en leads cualificados. |
| **Segmentación** | 1. Test de audiencia look‑alike basada en los clientes actuales.<br>2. Excluir audiencias con baja conversión (p.ej., usuarios de dispositivos móviles sin conversión). | Reducir CPC y CPA al enfocarse en segmentos de mayor valor. |
| **Extensiones** | 1. Extensiones de llamada y de ubicación para campañas C.<br>2. Extensiones de enlace de sitio para B. | Incrementar impresiones de valor y CTR. |
| **Retargeting** | 1. Campañas de remarketing con mensajes personalizados.<br>2. Dinamización de anuncios según páginas visitadas. | Recuperar usuarios que ya mostraron interés. |

**Resumen ejecutivo**

- **Escala** la Campaña A; es la más eficiente en CPA y aporta la mayor cantidad de conversiones.  
- **Reduce** la Campaña B a un mínimo o pausa mientras se optimiza la landing y el copy.  
- **Conserva** una pequeña fracción de presupuesto en la Campaña C para captar leads de alta intención, pero con vigencia de CPA.  
- Redistribuye el presupuesto a **80 % A, 15 % C, 5 % B** para maximizar conversiones dentro de los 5 000 $.  
- Implementa los A/B tests propuestos para seguir reduciendo CPC y CPA, y mejorar la calidad de los leads.