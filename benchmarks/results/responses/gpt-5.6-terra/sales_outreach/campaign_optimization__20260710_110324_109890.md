# GPT-5.6 Terra — sales_outreach/campaign_optimization

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.24 | quality: 9.92
- latency_total: 23.599s | tokens_per_second: 118.1
- input_tokens: 261 | output_tokens: 2788
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando análisis detallados y recomendaciones prácticas para la optimización de campañas de marketing.

## Respuesta completa

## 1. Métricas por campaña

| Campaña | CTR (Clicks / Impresiones) | CPC (Costo / Clicks) | Conversion rate (Signups / Clicks) | CPA (Costo / Signups) |
|---|---:|---:|---:|---:|
| **A — Landing principal** | 1,500 / 50,000 = **3.0%** | $2,100 / 1,500 = **$1.40** | 45 / 1,500 = **3.0%** | $2,100 / 45 = **$46.67** |
| **B — Blog content** | 4,800 / 120,000 = **4.0%** | $1,800 / 4,800 = **$0.38** | 24 / 4,800 = **0.5%** | $1,800 / 24 = **$75.00** |
| **C — Competidor** | 900 / 15,000 = **6.0%** | $3,200 / 900 = **$3.56** | 36 / 900 = **4.0%** | $3,200 / 36 = **$88.89** |

### Lectura rápida

- **Mejor CTR:** Campaña C (6.0%)
- **CPC más bajo:** Campaña B ($0.38)
- **Mejor tasa de conversión:** Campaña C (4.0%)
- **Mejor CPA:** Campaña A ($46.67)
- **Peor CPA y peor conversión post-click:** Campaña B ($75 CPA, 0.5% de conversión)

> Nota: el gasto reportado suma **$7,100**, pero indicas un presupuesto de **$5,000/mes**. Asumo que los datos corresponden al rendimiento observado y que ahora hay que ajustar el presupuesto futuro a $5,000.

---

## 2. ¿Qué campaña escalar y cuál pausar?

### Escalar: Campaña A — Landing principal

Es la campaña más eficiente para generar signups:

- CPA de **$46.67**, el más bajo.
- Es **37.8% más barata por signup que B**:  
  - A: $46.67  
  - B: $75.00
- Es **47.5% más barata por signup que C**:  
  - A: $46.67  
  - C: $88.89
- Tiene una tasa de conversión sólida de **3.0%**.

Aunque su CTR no es el mayor, el tráfico que atrae convierte bien y a un costo sostenible. Para un objetivo de adquisición, esta debe ser la prioridad.

### Pausar o reducir drásticamente: Campaña B — Blog content

La campaña B consigue tráfico barato, pero ese tráfico tiene baja intención de compra:

- CPC muy bajo: **$0.38**
- Pero conversion rate de apenas **0.5%**
- CPA de **$75**, un **60.7% mayor que A**

En otras palabras, B genera muchos clics, pero pocos registros: 4,800 clics producen solo 24 signups. Esto sugiere una desconexión entre la intención de búsqueda informativa (“cómo gestionar inventario”) y una oferta orientada a registro/demo.

**Recomendación:** pausarla como campaña de adquisición directa, o dejar un presupuesto experimental muy limitado si el contenido tiene valor de awareness, remarketing o captación de leads superiores del funnel.

### Mantener, pero no escalar agresivamente: Campaña C — Competidor

La campaña C tiene señales positivas:

- Mejor CTR: **6.0%**
- Mejor conversión: **4.0%**
- 36 signups con solo 900 clics

Sin embargo, tiene un problema claro de costo:

- CPC de **$3.56**
- CPA de **$88.89**, casi el doble que A.

Esto suele ocurrir en keywords de competidores: hay alta intención, pero también alta competencia y CPC elevados.

**Recomendación:** mantenerla con presupuesto controlado y optimizarla, no escalarla todavía. Puede ser rentable si esos leads tienen mejor calidad —por ejemplo, mayor tasa de activación, cierre o LTV— que los de la Campaña A. Si todos los signups valen lo mismo, A es claramente superior.

---

## 3. Redistribución del presupuesto de $5,000

### Propuesta recomendada

| Campaña | Presupuesto mensual | % del presupuesto | CPA actual estimado | Signups estimados* |
|---|---:|---:|---:|---:|
| **A — Landing principal** | **$4,000** | **80%** | $46.67 | **~86** |
| **C — Competidor** | **$1,000** | **20%** | $88.89 | **~11** |
| **B — Blog content** | **$0** | **0%** | $75.00 | 0 |
| **Total** | **$5,000** | **100%** | — | **~97** |

\*Proyección simple suponiendo que el CPA se mantiene al aumentar presupuesto. En la práctica, el CPA puede subir al escalar por saturación de audiencia o keywords.

### Comparación con distribuir el presupuesto de forma uniforme

Si repartieras $5,000 en partes iguales entre las tres campañas (~$1,667 cada una), esperarías aproximadamente:

- A: $1,667 / $46.67 = **36 signups**
- B: $1,667 / $75 = **22 signups**
- C: $1,667 / $88.89 = **19 signups**
- Total: **~77 signups**

Con la propuesta de priorizar A y mantener C controlada, la estimación es de **~97 signups**, aproximadamente **20 más**.

### Alternativa si quieres seguir aprendiendo de B

Si necesitas preservar una pequeña inversión en contenido para probar mejoras:

- Campaña A: **$3,750** (75%)
- Campaña C: **$875** (17.5%)
- Campaña B: **$375** (7.5%, solo test)

Pero B debería tener un objetivo explícito: subir la conversión de 0.5% a al menos **1.0%–1.5%**. Con su CPC actual, una conversión del 1% llevaría su CPA a aproximadamente **$37.50**, mejor que A.

---

## 4. A/B tests sugeridos para el próximo mes

## Campaña A: optimizar la ganadora

Objetivo: conservar o mejorar el CPA de $46.67 mientras se escala.

### Test 1: Landing page enfocada en conversión
Probar dos versiones:

- **Versión A:** landing actual.
- **Versión B:** propuesta de valor más específica por segmento:
  - “Controla el inventario de tu pyme en tiempo real”
  - “Reduce quiebres de stock y pérdidas de inventario”
  - “Prueba gratis / agenda una demo”

Elementos a testear:

- CTA: “Prueba gratis”, “Solicitar demo”, “Ver cómo funciona”.
- Formulario corto vs. formulario actual.
- Prueba social: logos de clientes, número de usuarios, testimonios.
- Beneficios cuantificados: “Reduce faltantes de stock”, “Ahorra X horas por semana”.
- Mostrar precios o no mostrar precios, según modelo comercial.

**Métrica principal:** conversion rate y CPA.

### Test 2: Ads por intención de keyword
Separar grupos de anuncios:

- “software gestión inventario”
- “sistema inventario pyme”
- “control de stock”
- “programa para inventario”

Crear anuncios y landing pages con el mismo lenguaje de la búsqueda. Esto mejora relevancia, Quality Score, CTR y potencialmente CPC.

### Test 3: Tipos de concordancia y negativas
Probar:

- Concordancia de frase y exacta para los términos con mejor CPA.
- Reducir amplia si trae búsquedas irrelevantes.
- Agregar negativas como “plantilla”, “excel gratis”, “curso”, “definición”, “trabajo”, si no convierten.

---

## Campaña B: convertir tráfico informativo en tráfico útil

Objetivo: elevar conversion rate desde 0.5%.

### Test 1: Cambiar la oferta según intención informativa

Las búsquedas como “cómo gestionar inventario” no necesariamente buscan comprar software todavía. En lugar de enviar directamente a una landing de signup, probar:

- **Landing A:** registro/demo directo.
- **Landing B:** recurso descargable:
  - “Checklist gratuito para controlar inventario”
  - “Plantilla de inventario para restaurantes”
  - “Guía: 10 errores que causan pérdidas de stock”

Después, nutrir esos leads con email y remarketing hacia el signup o demo.

**Métrica:** costo por lead calificado y tasa de conversión de lead a signup, no solo CPA inicial.

### Test 2: Separar por vertical
“Problemas de inventario restaurante” merece una experiencia específica:

- Anuncio para restaurantes.
- Landing con dolores del sector: mermas, caducidad, desperdicio, falta de ingredientes.
- Casos de uso y testimonios de restaurantes.
- CTA adaptado: “Reduce mermas y evita faltantes”.

No mezclar esa keyword con búsquedas genéricas de pymes.

### Test 3: Remarketing
Crear audiencias de personas que:

- Leyeron un artículo.
- Visitaron una página de producto.
- Descargaron una guía.
- Empezaron el formulario pero no lo completaron.

Mostrarles anuncios de demo, prueba gratuita o caso de éxito. El remarketing debería tener mejor conversión que el tráfico frío de blog.

---

## Campaña C: reducir el CPA de competidores

Objetivo: mantener alta intención, pero bajar CPA desde $88.89.

### Test 1: Landing específica de comparación
No envíes tráfico de competidores a la landing genérica. Crear páginas como:

- “Alternativa a [Competidor]”
- “[Tu producto] vs. [Competidor]”
- “Comparativa de funcionalidades, precio, soporte e implementación”

Debe incluir:

- Tabla comparativa clara.
- Casos de uso donde tu producto es fuerte.
- Migración/importación de datos.
- Testimonios de clientes que cambiaron desde otra solución.
- CTA: “Ver comparativa”, “Hablar con un especialista”, “Migrar sin costo”.

### Test 2: Mensajes de anuncio
Probar dos enfoques:

- **Funcionalidad/valor:** “Más control de inventario, implementación rápida”.
- **Cambio/migración:** “Cámbiate desde [competidor] sin perder tus datos”.

Evita usar marcas de competidores en textos de anuncio si hay restricciones de políticas o marca registrada; revisa las normas de Google Ads y la legislación aplicable en tu mercado.

### Test 3: Control de CPC y segmentación
- Priorizar exact match en términos de competidor con conversiones.
- Excluir búsquedas de soporte, login, teléfono, empleo, manual, tutorial o precios si no generan leads de calidad.
- Ajustar por dispositivo, ubicación y horario según CPA.
- Aplicar límites de puja o usar una estrategia de CPA objetivo cuando haya suficiente volumen de conversiones.

---

## Decisión final

- **Escalar:** Campaña A.
- **Pausar/reformular:** Campaña B.
- **Mantener con presupuesto limitado y optimizar:** Campaña C.
- **Distribución inicial recomendada:** $4,000 en A, $1,000 en C y $0 en B, salvo un pequeño presupuesto de experimentación.
- Antes de escalar de forma definitiva, valida también la **calidad posterior del signup**: activación, demo agendada, oportunidad comercial y cliente cerrado. Una campaña con CPA más alto puede justificarse si genera clientes con mayor LTV.