# GPT-5.6 Sol — sales_outreach/campaign_optimization

- model_id: `openai/gpt-5.6-sol`
- success: True  | final: 7.85 | quality: 10.0
- latency_total: 77.653s | tokens_per_second: 36.3
- input_tokens: 261 | output_tokens: 2819
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y altamente útil, proporcionando análisis detallados y recomendaciones prácticas para la optimización de la campaña.

## Respuesta completa

## 1. Métricas por campaña

Fórmulas:

- **CTR** = clics / impresiones
- **CPC** = costo / clics
- **CPA** = costo / signups
- **Conversion rate** = signups / clics

| Campaña | CTR | CPC | Conversion rate | CPA |
|---|---:|---:|---:|---:|
| **A – Landing principal** | 1,500 / 50,000 = **3.0%** | $2,100 / 1,500 = **$1.40** | 45 / 1,500 = **3.0%** | $2,100 / 45 = **$46.67** |
| **B – Blog content** | 4,800 / 120,000 = **4.0%** | $1,800 / 4,800 = **$0.38** | 24 / 4,800 = **0.5%** | $1,800 / 24 = **$75.00** |
| **C – Competidor** | 900 / 15,000 = **6.0%** | $3,200 / 900 = **$3.56** | 36 / 900 = **4.0%** | $3,200 / 36 = **$88.89** |

### Lectura rápida

- **A** tiene el mejor CPA y una conversión saludable.
- **B** genera tráfico muy barato, pero convierte muy poco.
- **C** tiene el mejor CTR y conversion rate, pero el CPC elevado hace que tenga el peor CPA.

---

## 2. Qué campaña escalar y cuál pausar

### Escalar: Campaña A

Es la mejor campaña para adquisición:

- CPA de **$46.67**, el menor de las tres.
- Es aproximadamente **38% más barata que B** por signup.
- Es aproximadamente **48% más barata que C** por signup.
- Conversion rate de **3%**, seis veces superior al de B.

La escalaría progresivamente, vigilando que el CPA marginal no aumente demasiado al ampliar presupuesto o keywords.

### Pausar o limitar fuertemente: Campaña C

Aunque sus señales de intención son buenas:

- CTR: **6%**
- Conversion rate: **4%**

Su CPC de **$3.56** hace que el CPA llegue a **$88.89**, el peor resultado. La pausaría como campaña activa de escala y la mantendría solo como experimento controlado si las conversiones provenientes de competidores tienen mayor calidad o valor comercial.

### Mantener y optimizar: Campaña B

B no debería escalarse todavía, pero tampoco necesariamente eliminarse:

- Tiene el CPC más bajo: **$0.38**
- Su CPA de **$75** es mejor que el de C
- El problema está después del clic: solo convierte **0.5%**

Esto sugiere una desconexión entre intención informativa y oferta. Puede funcionar como canal de remarketing o nutrición, pero necesita mejores CTAs y una transición más clara desde el contenido hacia el producto.

> Importante: los costos reportados suman **$7,100**, aunque indicas que el presupuesto es de **$5,000/mes**. Eso supone $2,100 por encima del presupuesto, o un 42% adicional. Conviene revisar períodos, presupuestos diarios y reglas de gasto.

---

## 3. Redistribución del presupuesto de $5,000

### Propuesta principal

| Campaña | Presupuesto | Porcentaje |
|---|---:|---:|
| **A – Landing principal** | **$3,750** | **75%** |
| **B – Blog content** | **$1,250** | **25%** |
| **C – Competidor** | **$0** | **0%** |
| **Total** | **$5,000** | **100%** |

Si los CPA se mantuvieran constantes:

- A: $3,750 / $46.67 ≈ **80 signups**
- B: $1,250 / $75 ≈ **17 signups**
- Total estimado: **97 signups**
- CPA combinado estimado: aproximadamente **$51.55**

Esto es una proyección lineal. Al aumentar A de $2,100 a $3,750, probablemente su CPA suba por saturación, menor volumen de búsquedas de alta intención o expansión hacia términos menos eficientes.

### Implementación prudente

No subiría A directamente a $3,750:

1. Subir de $2,100 a aproximadamente **$3,000**.
2. Evaluar durante 1–2 semanas el **CPA incremental**.
3. Si sigue dentro del objetivo, llevarla gradualmente a $3,750.
4. Si B no mejora su conversion rate, trasladar parte de sus $1,250 hacia A.

Si es estratégico mantener presencia en búsquedas de competidores, reservaría como máximo **$300–$500** para C, financiados desde B, pero solo con keywords exactas, límites de CPC y una landing específica.

---

## 4. A/B tests para el próximo mes

### Campaña A: mejorar el 3% de conversión

**Test 1: propuesta de valor en la landing**

- Variante A: mensaje general de gestión de inventario.
- Variante B: mensaje específico para pymes, por ejemplo:  
  **“Reduce faltantes y exceso de stock con inventario en tiempo real.”**

Métrica principal: conversion rate de visita a signup.

**Test 2: CTA**

- “Crear cuenta”
- “Probar gratis”
- “Ver mi inventario en acción” o “Solicitar demo”

**Test 3: formulario**

- Formulario actual.
- Formulario corto con email y contraseña, dejando el resto para el onboarding.

Medir no solo signups, sino también activaciones posteriores para evitar registros de baja calidad.

**Test 4: landing por keyword**

Crear mensajes separados:

- Para “software gestión inventario”: enfoque en funcionalidades.
- Para “inventario pymes”: enfoque en facilidad, precio y rápida implementación.

---

### Campaña B: resolver la baja conversión del 0.5%

**Test 1: CTA dentro del contenido**

- CTA solo al final del artículo.
- CTA contextual después de explicar el problema, además de uno al final.

**Test 2: oferta directa vs recurso intermedio**

- “Prueba el software”.
- “Descarga una plantilla/checklist de inventario” y luego nutrir el lead.

Para búsquedas informativas, una oferta intermedia probablemente tenga menos fricción.

**Test 3: landing puente**

En lugar de enviar directamente desde el blog al registro:

- Control: artículo → signup.
- Variante: artículo → página “Cómo nuestro software resuelve este problema” → signup.

**Test 4: CTA específico por contenido**

Para “problemas inventario restaurante”, probar una landing y CTA específicos para restaurantes, con ejemplos de mermas, ingredientes, múltiples ubicaciones y alertas de stock.

---

### Campaña C: si se reactiva

**Test 1: landing genérica vs comparativa**

- Landing general del producto.
- Landing específica: “[Tu producto] como alternativa a [competidor]”, con comparación de precio, funcionalidades, soporte y migración.

**Test 2: oferta**

- Prueba gratuita.
- Demo con migración o configuración asistida.

**Test 3: control de tráfico**

No es un A/B test puro, pero aplicaría:

- Concordancia exacta y de frase.
- Keywords negativas.
- Límites de CPC.
- Segmentación por dispositivo, ubicación y horario.
- Exclusión de búsquedas de soporte, login, empleo o navegación del competidor.

---

## Prioridad recomendada

1. Escalar A gradualmente.
2. Pausar C hasta reducir su CPC o demostrar mayor calidad de signup.
3. Optimizar B para subir su conversión de **0.5% a al menos 1%**. Con el mismo CPC, duplicar su conversión reduciría su CPA aproximadamente de **$75 a $37.50**.
4. Evaluar también el costo por **signup activado, oportunidad o cliente**, no únicamente por registro. Una campaña con CPA alto podría justificarse si produce clientes con mayor tasa de cierre o LTV.