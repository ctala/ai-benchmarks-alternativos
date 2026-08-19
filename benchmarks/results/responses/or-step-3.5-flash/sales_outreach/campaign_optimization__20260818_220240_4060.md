# Step 3.5 Flash — sales_outreach/campaign_optimization

- model_id: `stepfun/step-3.5-flash`
- success: True  | final: 7.38 | quality: 8.0
- latency_total: 75.735s | tokens_per_second: 69.6
- input_tokens: 280 | output_tokens: 5273

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

### 1. Cálculo de métricas

**Campaña A (Landing principal):**
- **CTR** = (1,500 / 50,000) × 100 = **3.0%**
- **CPC** = $2,100 / 1,500 = **$1.40**
- **CPA** = $2,100 / 45 = **$46.67**
- **Tasa de conversión** = (45 / 1,500) × 100 = **3.0%**

**Campaña B (Blog content):**
- **CTR** = (4,800 / 120,000) × 100 = **4.0%**
- **CPC** = $1,800 / 4,800 = **$0.375**
- **CPA** = $1,800 / 24 = **$75.00**
- **Tasa de conversión** = (24 / 4,800) × 100 = **0.5%**

**Campaña C (Competidor):**
- **CTR** = (900 / 15,000) × 100 = **6.0%**
- **CPC** = $3,200 / 900 ≈ **$3.56**
- **CPA** = $3,200 / 36 ≈ **$88.89**
- **Tasa de conversión** = (36 / 900) × 100 = **4.0%**

---

### 2. Campaña a escalar y pausar (justificación numérica)

- **Escalar: Campaña A**  
  Tiene el **CPA más bajo ($46.67)** y una **tasa de conversión sólida (3.0%)**. Es la más eficiente en costo por adquisición y ya genera la mayor cantidad de signups (45) con un presupuesto moderado. Su CPC ($1.40) es razonable y su CTR (3.0%) es aceptable. Al escalar, es probable que mantenga su eficiencia relativa.

- **Pausar: Campaña B**  
  A pesar de tener el **CTR más alto (4.0%)** y el **CPC más bajo ($0.375)**, su **tasa de conversión es extremadamente baja (0.5%)**, lo que resulta en un **CPA alto ($75.00)**. Esto indica que el tráfico (proveniente de keywords de blog) no está calificado para la conversión actual. Invertir aquí es ineficiente: se pagan muchos clics que no se convierten.

- **Campaña C**  
  Tiene una **buena tasa de conversión (4.0%)** y el **CTR más alto (6.0%)**, pero un **CPC muy elevado ($3.56)** que dispara su **CPA ($88.89)**. Es la campaña más cara por conversión. Podría optimizarse (ej. ajustando keywords o landing page), pero con los datos actuales es menos eficiente que A. **Recomendación: pausar temporalmente** para redistribuir presupuesto a A, y reconsiderarla solo si se logra reducir el CPC significativamente.

---

### 3. Redistribución del presupuesto de $5,000

**Propuesta óptima (maximizar signups):**
- **Campaña A: $5,000 (100%)**  
  Asumiendo que el CPA se mantiene en ~$46.67, con $5,000 se obtendrían aproximadamente **107 signups** (5,000 / 46.67).  
  *Nota:* Al escalar, el CPA podría aumentar ligeramente por saturación de audiencia, pero aún así debería superar a las otras opciones.

**Por qué no incluir B o C:**
- Si se asignara $500 a C (CPA $88.89) generaría ~5.6 signups, y $4,500 a A generaría ~96.4 signups. **Total: ~102 signups**, menos que los 107 de poner todo en A.
- B es inviable por su alto CPA.

**Alternativa conservadora (si se desea diversificar):**  
- Campaña A: $4,000 → ~86 signups  
- Campaña C: $1,000 → ~11 signups  
- **Total: ~97 signups** (peor que la opción anterior).  
**Conclusión:** Concentrar en A es la estrategia más rentable.

---

### 4. A/B tests sugeridos para el próximo mes

**Para Campaña A (la escalada):**
1. **Landing page:**  
   - Variante A: Enfoque en beneficios y características técnicas.  
   - Variante B: Enfoque en testimonios y casos de éxito.  
   - **Métrica objetivo:** Mejorar tasa de conversión (actual 3.0%).

2. **Oferta de valor:**  
   - Variante A: Trial gratuito de 14 días.  
   - Variante B: Demo personalizada con consultor.  
   - **Métrica:** CPA y tasa de conversión.

3. **Copy de anuncio:**  
   - Variante A: Mensaje orientado a "ahorro de tiempo".  
   - Variante B: Mensaje orientado a "precisión y control".  
   - **Métrica:** CTR y tasa de conversión.

**Para Campaña B (si se reactiva tras optimizar):**
1. **Objetivo de landing page:**  
   - Variante A: Signup directo para software (actual).  
   - Variante B: Oferta de contenido descargable (ej. "Guía de gestión de inventario") para captar leads en etapa de investigación.  
   - **Métrica:** Tasa de conversión (actual 0.5%).

2. **Keywords:**  
   - Probar long-tail con intención comercial (ej. "software gestión inventario para pymes precio").

**Para Campaña C (si se reconsidera):**
1. **Mensaje competitivo:**  
   - Variante A: "Alternativa más económica a [competidor]".  
   - Variante B: "Más integraciones que [competidor]".  
   - **Métrica:** CPC y CPA.

2. **Landing page comparativa:**  
   - Variante A: Página centrada en diferencias técnicas.  
   - Variante B: Página con tabla comparativa visual.  
   - **Métrica:** Tasa de conversión (actual 4.0%).

**Tests transversales (todas las campañas):**
- Extensiones de anuncio: probar extensiones de ubicación, llamada y snippets estructurados.
- Segmentación por dispositivo: ajustar pujas para móvil vs. escritorio.
- Horarios: identificar y pujar más en franjas de mayor conversión.

---

### Resumen ejecutivo:
1. **Métricas:** A es la más eficiente (CPA $46.67), B es ineficiente (CPA $75), C es cara (CPA $88.89).
2. **Acción:** Escalar A, pausar B y C.
3. **Presupuesto:** $5,000 íntegros a A (proyección: ~107 signups).
4. **Tests:** Optimizar A en landing page, oferta y copy. Si se retoman B/C, tests específicos para sus problemas (B: contenido educativo; C: mensaje competitivo).