# GLM 5 — sales_outreach/campaign_optimization

- model_id: `z-ai/glm-5`
- success: True  | final: 8.64 | quality: 10.0
- latency_total: 31.594s | tokens_per_second: 52.2
- input_tokens: 272 | output_tokens: 1648

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

Aquí tienes un análisis detallado de tus campañas de Google Ads. Tienes datos muy interesantes, pero también oportunidades claras de optimización.

### 1. Cálculo de Métricas (CTR, CPC, CPA y Tasa de Conversión)

*Nota: Asumo que "Signups" es tu conversión principal (lead/registro).*

**Campaña A (Landing principal):**
*   **CTR (Click-Through Rate):** 3.00% *(1,500 / 50,000)*
*   **CPC (Costo Por Clic):** $1.40 *($2,100 / 1,500)*
*   **Tasa de Conversión:** 3.00% *(45 / 1,500)*
*   **CPA (Costo Por Adquisición):** $46.67 *($2,100 / 45)*

**Campaña B (Blog content):**
*   **CTR (Click-Through Rate):** 4.00% *(4,800 / 120,000)*
*   **CPC (Costo Por Clic):** $0.38 *($1,800 / 4,800)*
*   **Tasa de Conversión:** 0.50% *(24 / 4,800)*
*   **CPA (Costo Por Adquisición):** $75.00 *($1,800 / 24)*

**Campaña C (Competidor):**
*   **CTR (Click-Through Rate):** 6.00% *(900 / 15,000)*
*   **CPC (Costo Por Clic):** $3.56 *($3,200 / 900)*
*   **Tasa de Conversión:** 4.00% *(36 / 900)*
*   **CPA (Costo Por Adquisición):** $88.89 *($3,200 / 36)*

---

### 2. ¿Cuál escalar y cuál pausar? (Justificación)

*   **Escalar: Campaña A (Landing principal)**
    *   *Justificación:* Tiene el **CPA más bajo de todas ($46.67)**. Aunque su CTR es menor que la Campaña B o C, el tráfico que atrae es altamente comercial y con intención de compra. Su tasa de conversión de página (3%) es excelente para SaaS/Software. Es tu campaña más rentable.
*   **Pausar (o restringir fuertemente): Campaña B (Blog content)**
    *   *Justificación:* Aunque genera mucho tráfico barato (CPC $0.38), su **CPA es altísimo ($75.00)** y su tasa de conversión es casi nula (0.50%). Está actuando como una "llave abierta" que drena presupuesto sin generar negocio. El usuario que busca "cómo gestionar inventario" busca información gratuita, no necesariamente comprar software.
*   **Mantener pero optimizar: Campaña C (Competidor)**
    *   *Justificación:* No la pausaría del todo porque tiene el **CTR más alto (6%)** y una tasa de conversión buenísima (4%). El problema es que el CPC es carísimo ($3.56) y el CPA sube a $88.89. El usuario aquí está en el "bottom of funnel" comparando opciones. Se debe mantener, pero optimizando pujas para bajar el CPC.

---

### 3. Redistribución del presupuesto ($5,000/mes)

Actualmente gastaste $7,100 (asumo que es un periodo de más de un mes o que excediste el presupuesto). Para ajustarnos a tu tope de **$5,000 mensuales** y maximizar resultados, propongo esta distribución:

*   **Campaña A (Landing principal): $3,000/mes (60%)**
    *   *Razón:* Es tu máquina de leads. Con un CPA de $46.67, este presupuesto te daría aproximadamente **64 signups al mes**.
*   **Campaña C (Competidor): $1,500/mes (30%)**
    *   *Razón:* Con un CPA de $88.89, este presupuesto te daría unas **17 signups al mes**. Son leads de muy alta calidad (gente comparando).
*   **Campaña B (Blog content): $500/mes (10%)**
    *   *Razón:* En lugar de pausarla por completo, la dejamos con un presupuesto mínimo para mantener presencia de marca y captar tráfico de cola larga, pero evitando que consuma los recursos de las campañas principales. Si no puedes segmentarla por "palabras clave de marca" o retargeting, mejor pásala a una campaña de Display o pásala.

*Total estimado con esta distribución: 81 signups/mes a un CPA promedio de $61.72.*

---

### 4. A/B Tests sugeridos para el próximo mes

Para mejorar estos números el próximo mes, te sugiero los siguientes tests:

**Para la Campaña A (Escalar):**
*   **A/B Test de Landing Page:** Tienes un 3% de conversión, lo cual es bueno, pero se puede mejorar. Prueba dos versiones de la landing:
    *   *Versión A:* Enfoque en "Ahorro de tiempo" (Ej. "Reduce tu gestión de inventario a la mitad").
    *   *Versión B:* Enfoque en "Ahorro de dinero/pérdidas" (Ej. "Evita pérdidas de inventario con alertas automáticas").
*   **A/B Test de Anuncios:** Prueba diferentes llamados a la acción (CTA). "Agenda una demo" vs "Prueba gratis 14 días". En SaaS, esto cambia drásticamente el volumen y la calidad del lead.

**Para la Campaña C (Optimizar costos):**
*   **A/B Test de Pujas (Bidding):** Dado que el CPC está muy alto ($3.56), prueba cambiar de "Maximizar clics" o "Manual" a **"Maximizar conversiones"** o **"Target CPA" (CPA objetivo a $75)**. Esto le dirá al algoritmo de Google que busque clics más baratos dentro de ese público de intención comparativa.
*   **A/B Test de Extensiones/Assets:** Activa y prueba *Extensiones de enlace de sitio* (Sitelinks) con beneficios directos frente al competidor (Ej. "Más barato que [Competidor]", "Mejor soporte que [Competidor]"). Esto aumenta tu CTR, empuja a los competidores hacia abajo en la página y puede bajar tu CPC al mejorar tu Quality Score.

**Para la Campaña B (Rescatar el presupuesto):**
*   **A/B Test de Oferta en el Blog:** La gente del blog no se convierte porque buscan leer, no comprar. Pon un pop-up o banner en el medio del artículo con una oferta irresistible: "Descarga esta plantilla de Excel para inventario de restaurantes gratis" (Lead magnet). Captura el email allí, y luego nutre ese lead por correo electrónico para que compre. Esto subirá tu tasa de conversión del 0.5% a algo más aceptable.
*   **A/B Test de Exclusión:** Excluye palabras clave como "gratis", "excel", "tutorial", "qué es". Quien busca eso no va a pagar un software SaaS.