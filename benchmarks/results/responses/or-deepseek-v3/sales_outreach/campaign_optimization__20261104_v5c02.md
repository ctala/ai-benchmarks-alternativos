# DeepSeek V3 — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v3.2`
- success: True  | final: 8.83 | quality: 10.0
- latency_total: 34.094s | tokens_per_second: 36.5
- input_tokens: 272 | output_tokens: 1244

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

Vamos a analizar tus campañas paso a paso.  

---

## **1. Métricas calculadas**

Fórmulas:  
- **CTR** = Clicks / Impresiones  
- **CPC** = Costo / Clicks  
- **CPA** = Costo / Signups  
- **Conv. Rate** = Signups / Clicks × 100%  

### **Campaña A**  
Impresiones = 50,000 | Clicks = 1,500 | Signups = 45 | Costo = $2,100  
- CTR = 1,500 / 50,000 = **3.00%**  
- CPC = 2,100 / 1,500 = **$1.40**  
- CPA = 2,100 / 45 = **$46.67**  
- Conv. Rate = 45 / 1,500 = **3.00%**  

### **Campaña B**  
Impresiones = 120,000 | Clicks = 4,800 | Signups = 24 | Costo = $1,800  
- CTR = 4,800 / 120,000 = **4.00%**  
- CPC = 1,800 / 4,800 = **$0.375**  
- CPA = 1,800 / 24 = **$75.00**  
- Conv. Rate = 24 / 4,800 = **0.50%**  

### **Campaña C**  
Impresiones = 15,000 | Clicks = 900 | Signups = 36 | Costo = $3,200  
- CTR = 900 / 15,000 = **6.00%**  
- CPC = 3,200 / 900 = **$3.56**  
- CPA = 3,200 / 36 = **$88.89**  
- Conv. Rate = 36 / 900 = **4.00%**  

---

**Resumen de métricas**:

| Campaña | CTR   | CPC    | CPA    | Conv. Rate |
|---------|-------|--------|--------|-------------|
| A       | 3.00% | $1.40  | $46.67 | 3.00%       |
| B       | 4.00% | $0.375 | $75.00 | 0.50%       |
| C       | 6.00% | $3.56  | $88.89 | 4.00%       |

---

## **2. ¿Cuál escalar y cuál pausar?**

**Objetivo principal** = maximizar signups con presupuesto limitado → mirar **CPA** (menor es mejor) y **volumen potencial**.

- **Campaña A**: CPA más bajo ($46.67), conv. rate decente (3%), volumen de clicks bueno.  
- **Campaña B**: CPC muy bajo, pero conv. rate pésimo (0.5%) → CPA alto ($75), tráfico no cualificado para signups.  
- **Campaña C**: Conv. rate alto (4%), pero CPC muy alto y CPA más alto ($88.89), posiblemente búsquedas de marca de competidor, pero costoso.

**Pausar**: Campaña B (aunque da muchos clicks, la conversión es muy baja, el CPA es alto).  
**Escalar**: Campaña A (CPA más bajo, buen equilibrio entre volumen y costo).  
Campaña C puede mantenerse si hay margen para optimizar CPC o mejorar la landing page, pero no escalar fuerte por ahora.

---

## **3. Redistribución del presupuesto $5,000**

Actualmente gastas: $2,100 + $1,800 + $3,200 = $7,100 (supera tu presupuesto de $5k, así que ya hay que recortar).

Propuesta:  
1. **Pausar B** → ahorro $1,800.  
2. **Reducir C** a solo pruebas controladas, quizás $1,000 (en vez de $3,200) → ahorro $2,200.  
3. **Aumentar A** con más presupuesto.

Presupuesto resultante:  
- Campaña A: $3,500 (antes $2,100)  
- Campaña C: $1,500 (antes $3,200)  
- Total: $5,000  

---

## **4. A/B tests sugeridos**

### **Para Campaña A (escalada):**  
1. **Landing page**: probar dos versiones de formulario (corto vs largo con más info beneficios).  
2. **Keywords**: añadir nuevas palabras clave de intención comercial (“precio software inventario”, “software inventario gratis prueba”).  
3. **Copys de anuncio**: testear llamadas a la acción (“Prueba gratis” vs “Ver demo”).

### **Para Campaña C (competidor):**  
1. **Ajustar oferta en anuncio**: mencionar “Mejor que [competidor] – 30 días gratis”.  
2. **Pujar por keywords más genéricas** además de las de competidor para bajar CPC.

### **Para Campaña B (pausada, pero si se reactiva):**  
1. **Segmentar por audiencia** (solo empresas, no estudiantes/blogueros).  
2. **Landing page específica** para contenido educativo con formulario de demo al final del artículo.

---

**¿Te gustaría que preparemos una simulación de la proyección de signups con esta redistribución?**