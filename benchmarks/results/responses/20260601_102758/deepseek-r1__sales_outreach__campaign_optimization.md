# DeepSeek R1 (reasoning) — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-r1`
- success: True  | final: 7.2 | quality: 9.56
- latency_total: 154.086s | tokens_per_second: 25.8
- input_tokens: 273 | output_tokens: 3983
- judge_score: 5.0 | justificación: 

## Respuesta completa

### Respuesta Detallada

---

#### **1. Cálculo de CTR, CPC, CPA y Tasa de Conversión**
**Fórmulas utilizadas**:
- **CTR** = (Clicks / Impresiones) × 100  
- **CPC** = Costo / Clicks  
- **CPA** = Costo / Signups  
- **Tasa de Conversión** = (Signups / Clicks) × 100  

**Resultados**:

| Campaña        | CTR     | CPC    | CPA      | Tasa de Conversión |
|----------------|---------|--------|----------|---------------------|
| **A (Principal)** | 3.00%   | $1.40  | $46.67   | 3.00%              |
| **B (Blog)**     | 4.00%   | $0.38  | $75.00   | 0.50%              |
| **C (Competidor)** | 6.00%   | $3.56  | $88.89   | 4.00%              |

---

#### **2. ¿Qué campaña escalar y cuál pausar? Justificación con números**
- **Escalar: Campaña A (Principal)**  
  - **CPA más bajo ($46.67)**: Genera registros a menor costo vs. B ($75) y C ($88.89).  
  - **Tasa de conversión sólida (3.00%)**: Indica que la landing page y las keywords son efectivas.  
  - **CPC razonable ($1.40)**: Balancea volumen y calidad.  

- **Pausar: Campaña B (Blog)**  
  - **Tasa de conversión muy baja (0.50%)**: A pesar de muchos clicks (4,800), solo genera 24 registros.  
  - **CPA alto ($75.00)**: El segundo más alto, con baja eficiencia en ventas.  
  - **Keywords problemáticas**: "Cómo gestionar inventario" atrae tráfico informativo, no de compra.  

- **Mantener/revisar: Campaña C (Competidor)**  
  - **Alta tasa de conversión (4.00%)**: Sugiere que las keywords de competidores atraen público decidido.  
  - **CPA alto ($88.89)**: Costoso, pero optimizable (ej: ajustar pujas o mejorar landing page).  

**Justificación clave**:  
- **Campaña A es 60% más eficiente en CPA** que la Campaña B y 48% más que la C.  
- **Campaña B desperdicia presupuesto**: Necesita 3,125 clicks para 1 registro (vs. 33 clicks en A).  

---

#### **3. Redistribución del presupuesto de $5,000**
**Estrategia propuesta**:  
- **Pausar Campaña B**: Libera $1,800 (su bajo rendimiento no justifica inversión).  
- **Reducir Campaña C**: Limitar a $1,000 (para probar optimizaciones sin alto riesgo).  
- **Escalar Campaña A**: Asignar $4,000 (maximizar eficiencia con su CPA bajo).  

**Nueva asignación**:  
| Campaña | Presupuesto Asignado |  
|---------|----------------------|  
| A       | $4,000 (80% del total) |  
| C       | $1,000 (20% del total) |  
| B       | $0 (pausada)         |  

**Proyección de registros** (asumiendo mismos KPIs):  
- **Campaña A**: $4,000 / $46.67 ≈ **86 registros** (vs. 45 originales).  
- **Campaña C**: $1,000 / $88.89 ≈ **11 registros** (vs. 36 originales).  
**Total estimado**: **97 registros** (vs. 105 originales), pero con **20% menos costo total** ($5,000 vs. $7,100).  

---

#### **4. A/B Tests sugeridos para el próximo mes**
**Campaña A (Principal)**:  
- **Test de landing page**:  
  - Variante A: Landing actual (control).  
  - Variante B: Nueva versión con formulario simplificado + testimonios.  
  - **Métrica clave**: Tasa de conversión (meta: aumentar del 3% al 4.5%).  

- **Test de keywords**:  
  - Agrupar "software gestión inventario" (alto intento comercial) en campaña separada.  
  - Excluir palabras genéricas como "pymes" si atraen tráfico de baja calidad.  

**Campaña C (Competidor)**:  
- **Test de copy de anuncios**:  
  - Variante A: "Alternativa a [competidor] - Precios 40% más bajos".  
  - Variante B: "[Competidor] vs Nosotros - Comparativa en tiempo real".  
  - **Métrica clave**: CTR (meta: superar 6%) y CPA (meta: reducir a $70).  

**Campaña B (Blog) - Si se reactiva**:  
- **Test de oferta**:  
  - Variante A: Descarga guía PDF (lead magnético).  
  - Variante B: Prueba gratuita de 7 días (para captar leads más calificados).  
  - **Métrica clave**: Tasa de conversión (meta: superar 1.5%).  

**Tests transversales**:  
- **Horarios y dispositivos**:  
  - Redistribuir presupuesto a horarios con mayor conversión (ej: tardes vs. mañanas).  
  - Ajustar pujas para móviles si la tasa de conversión es mayor en ese dispositivo.  
- **Exclusiones de audiencia**:  
  - Excluir usuarios que rebotan en 5 segundos para mejorar calidad de tráfico.  

---

### Resumen Ejecutivo  
- **Escalar Campaña A**: Máxima eficiencia en CPA y conversiones.  
- **Pausar Campaña B**: Bajo retorno a pesar de alto volumen.  
- **Optimizar Campaña C**: Potencial si se reduce CPA.  
- **Redistribución**: $4,000 a A, $1,000 a C, $0 a B.  
- **A/B Tests**: Enfocados en mejorar landing pages, copy y segmentación para incrementar registros con el mismo presupuesto.