# Ministral 14B — sales_outreach/campaign_optimization

- model_id: `mistralai/ministral-14b-2512`
- success: True  | final: 7.51 | quality: 8.0
- latency_total: 43.287s | tokens_per_second: 38.3
- input_tokens: 303 | output_tokens: 1656

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

Aquí tienes el análisis detallado de tus campañas de Google Ads, junto con recomendaciones basadas en métricas clave:

---

### **1. Métricas clave por campaña**
*(Fórmulas: CTR = (Clicks/Impresiones)*100; CPC = Costo/Clicks; CPA = Costo/Signups; Conversion Rate = Signups/Clicks*100)*

| **Campaña**       | **CTR**  | **CPC**  | **CPA**   | **Conversion Rate** |
|-------------------|----------|----------|-----------|--------------------|
| **Campaña A**     | 3.0%     | $1.40    | $46.67    | 3.0%               |
| **Campaña B**     | 4.0%     | $0.375   | $75.00    | 0.5%               |
| **Campaña C**     | 6.0%     | $3.55    | $88.89    | 4.0%               |

**Observaciones**:
- **Campaña C** tiene el **CTR más alto (6.0%)** y el **mejor CPA ($88.89)**, pero también el **CPC más caro ($3.55)**.
- **Campaña B** tiene el **CPC más bajo ($0.375)** y muchas impresiones, pero su **conversion rate es bajo (0.5%)** y su **CPA es alto ($75)**.
- **Campaña A** es equilibrada, con un **CPA moderado ($46.67)** y un **conversion rate decente (3.0%)**.

---

### **2. ¿Qué campaña escalar y cuál pausar?**
**Escalar**: **Campaña C** (Competidor)
- **Justificación**:
  - **CTR alto (6.0%)**: La audiencia está muy interesada (busca alternativas a tu competidor).
  - **CPA aceptable ($88.89)**: Aunque es el más alto, genera **4 signups por cada $100 gastado**, y las keywords son de **intención comercial alta** (comparativas).
  - **Traffic de calidad**: Los usuarios que buscan "alternativa a [competidor]" ya tienen un problema resuelto con tu producto.

**Pausar**: **Campaña B** (Blog content)
- **Justificación**:
  - **CTR bajo (4.0%)** para el volumen de impresiones (120K).
  - **CPA muy alto ($75)** y **conversion rate bajo (0.5%)**: Los usuarios que buscan "cómo gestionar inventario" están en fase de investigación, no de compra.
  - **Costo-efectividad**: Por $1,800 solo obtuviste 24 signups (1 signup cada ~$75), mientras que **Campaña A** generó 45 signups por $2,100 (1 signup cada ~$46.67).

**Campaña A**: Mantenerla como base, pero optimizar su presupuesto.

---

### **3. Redistribución del presupuesto ($5,000)**
**Propuesta**:
| **Campaña**       | **Presupuesto Actual** | **Nuevo Presupuesto** | **Justificación**                          |
|-------------------|-----------------------|-----------------------|--------------------------------------------|
| **Campaña C**     | $3,200                | **$3,500**            | Escalar por alto CTR y CPA "aceptable" para keywords de intención comercial. |
| **Campaña A**     | $2,100                | **$1,200**            | Reducir para enfocarse en optimizar (ej.: ajustar keywords o landing page). |
| **Campaña B**     | $1,800                | **$300** (o pausar)   | Presupuesto mínimo para testear cambios (ej.: cambiar keywords a "mejor software inventario pymes"). |

**Alternativa más agresiva** (si Campaña B no mejora):
- **Campaña C**: $4,000
- **Campaña A**: $1,000
- **Campaña B**: $0 (pausar).

**Nota**: Si el CPA de Campaña C sigue alto (>$100), considera **ajustar pujas** o **segmentar mejor** (ej.: excluir dispositivos móviles si el conversion rate es bajo ahí).

---

### **4. Pruebas A/B para el próximo mes**
**Prioridades**:
1. **Campaña C (Competidor)**:
   - **A/B Test 1**: **Landing Page**
     - **Variante A**: Landing actual (enfocada en features).
     - **Variante B**: Landing con **testimonios de clientes que migraron de [competidor]** + comparación directa (ej.: "Ahorra 30% vs [competidor]").
     - *Objetivo*: Reducir CPA al aumentar la percepción de valor.
   - **A/B Test 2**: **Keywords**
     - Añadir keywords como:
       - "mejor alternativa a [competidor] 2024".
       - "[competidor] opiniones reales".
     - *Objetivo*: Atraer tráfico más calificado.

2. **Campaña A (Landing principal)**:
   - **A/B Test 1**: **CTA (Call-to-Action)**
     - Variante A: "Prueba gratis 14 días".
     - Variante B: "Empieza con 30 días sin compromiso" (para reducir fricción).
   - **A/B Test 2**: **Extensión de anuncio**
     - Añadir **extensiones de enlace de sitio** con enlaces a casos de éxito o páginas de precios.
     - *Objetivo*: Aumentar clicks relevantes.

3. **Si reactivas Campaña B**:
   - **A/B Test**: **Keywords**
     - Cambiar de "cómo gestionar inventario" a **"software inventario para [industria específica]"** (ej.: "software inventario para restaurantes").
     - *Objetivo*: Reducir CPA al segmentar mejor.

**Herramientas para implementar**:
- **Google Optimize**: Para tests de landing page.
- **Google Ads Scripts**: Para automatizar rotación de variantes.
- **Heatmaps** (Hotjar): Analizar comportamiento en las landings.

---
### **Resumen de acciones clave**:
1. **Escalar Campaña C** (aumentar presupuesto a $3,500-$4,000).
2. **Reducir Campaña A** a $1,000-$1,200 y optimizar su landing/keywords.
3. **Pausar o reducir drásticamente Campaña B** (a menos que se ajusten las keywords).
4. **Enfocar tests en**:
   - Comparación con competidores (Campaña C).
   - Reducción de fricción en el funnel (Campaña A).
   - Segmentación por industria (si reactivas Campaña B).

**Resultado esperado**:
- Reducción del CPA general (pasar de ~$60 a ~$50-$60).
- Mayor enfoque en tráfico de intención comercial (Campañas A y C).
- Datos más claros para ajustes futuros.