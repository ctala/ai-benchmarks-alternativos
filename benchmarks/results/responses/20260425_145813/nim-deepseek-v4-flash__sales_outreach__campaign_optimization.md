# DeepSeek V4 Flash (NIM) — sales_outreach/campaign_optimization

- model_id: `deepseek-ai/deepseek-v4-flash`
- success: True  | final: 7.2 | quality: 9.72
- latency_total: 78.405s | tokens_per_second: 21.4
- input_tokens: 272 | output_tokens: 1674
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí tienes el análisis detallado de tus campañas de Google Ads, con cálculos, recomendaciones basadas en datos y una propuesta de redistribución del presupuesto.

---

### 1. Cálculo de métricas clave

| Campaña | Impresiones | Clics | Signups | Costo | **CTR** | **CPC** | **CPA** | **Tasa Conversión (CVR)** |
|---------|-------------|-------|---------|------|---------|---------|---------|----------------------------|
| **A** (Landing) | 50,000 | 1,500 | 45 | $2,100 | **3.0%** | **$1.40** | **$46.67** | **3.0%** |
| **B** (Blog) | 120,000 | 4,800 | 24 | $1,800 | **4.0%** | **$0.38** | **$75.00** | **0.5%** |
| **C** (Competidor) | 15,000 | 900 | 36 | $3,200 | **6.0%** | **$3.56** | **$88.89** | **4.0%** |

**Fórmulas usadas:**
- CTR = (Clics / Impresiones) * 100
- CPC = Costo / Clics
- CPA = Costo / Signups
- CVR = (Signups / Clics) * 100

---

### 2. ¿Cuál escalar y cuál pausar? Justificación numérica

#### ✅ **Escalar: Campaña A (Landing principal)**
- **CPA más bajo:** $46.67 (vs. $75 de B y $88.89 de C).
- **CVR más alta:** 3.0% (la segunda mejor después de C, pero con un costo 34% menor por conversión).
- **Costo total razonable:** Con $2,100 ya genera 45 signups. Si escalas a $3,000, proyectas ~64 signups (manteniendo mismo CPA).
- **CTR decente (3.0%):** Indica que el targeting y el anuncio son relevantes.

#### ⚠️ **Pausar o reducir drásticamente: Campaña C (Competidor)**
- **CPA más alto:** $88.89 (casi el doble que A).
- **Costo desproporcionado:** Representa el 64% del presupuesto total ($3,200 de $5,000) pero solo genera el 34% de los signups (36 de 105 totales).
- **CTR alto (6%) pero engañoso:** Atrae clics de usuarios comparando, no necesariamente comprando. La intención de conversión es baja (CVR 4% vs. 3% de A, pero con CPC 2.5x más caro).
- **ROI negativo relativo:** Por cada dólar invertido en C obtienes ~0.011 signups, mientras que en A obtienes ~0.021.

#### 🔄 **Mantener optimizando: Campaña B (Blog content)**
- **CPA aceptable ($75)** pero mejorable. Es útil para *awareness* y tráfico de bajo costo (CPC $0.38), pero la conversión es muy baja (0.5%).
- **No pausar del todo**, porque puede nutrir leads a largo plazo (remarketing, contenido). Pero reducir presupuesto.

---

### 3. Redistribución del presupuesto ($5,000/mes)

| Campaña | Presupuesto actual | **Propuesta** | Cambio | Justificación |
|---------|-------------------|---------------|--------|---------------|
| **A** (Landing) | $2,100 | **$3,200** | +$1,100 | Escalar la campaña con mejor CPA y CVR. |
| **B** (Blog) | $1,800 | **$1,200** | -$600 | Mantener presencia para tráfico informativo, pero reducir gasto en conversiones pobres. |
| **C** (Competidor) | $3,200 | **$600** | -$2,600 | Reducción drástica. Dejar solo para capturar intención muy específica (ej. "alternativa a X") con puja mínima. |
| **Total** | $7,100 (excede) | **$5,000** | - | Ajustado al límite real. |

**Nota:** Tu presupuesto actual sumado es $7,100, pero dices que el total es $5,000. Asumo que esos $7,100 eran el gasto real del mes (quizás excediste). La propuesta respeta el límite de $5,000.

---

### 4. A/B Tests sugeridos para el próximo mes

#### **Para Campaña A (Landing principal) – Escalar con inteligencia**

1. **Test de landing page:**
   - **Variante A (actual):** Página con formulario largo + explicación detallada.
   - **Variante B:** Página minimalista con un solo CTA ("Prueba gratis 14 días") y video de 30 segundos.
   - **Métrica:** CPA y CVR.

2. **Test de copy en anuncios:**
   - **Actual:** "Software gestión inventario para pymes"
   - **Variante:** "Ahorra 10h/semana en inventario – Prueba gratis"
   - **Métrica:** CTR y CPA.

#### **Para Campaña B (Blog) – Mejorar conversión**

3. **Test de oferta en página de blog:**
   - **Actual:** Banner genérico "Descarga nuestro software".
   - **Variante:** Lead magnet contextual (ej. "Guía gratuita: 5 errores de inventario en restaurantes").
   - **Métrica:** Tasa de conversión de visitantes a leads (no solo signups directos).

4. **Test de segmentación por dispositivo:**
   - **Actual:** Misma puja en móvil y desktop.
   - **Variante:** Aumentar puja en desktop un 20% y reducir en móvil un 30% (dado que el blog se lee más en desktop y la conversión puede ser mejor).
   - **Métrica:** CPA por dispositivo.

#### **Para Campaña C (Competidor) – Solo si mantienes $600**

5. **Test de palabras negativas:**
   - **Actual:** Pujas amplias en "[competidor] vs".
   - **Variante:** Añadir palabras negativas como "precio", "gratis", "alternativa barata" (atraen tráfico no calificado).
   - **Métrica:** CPA y calidad del lead.

---

### Resumen ejecutivo

- **Escalar A** porque tiene el mejor balance costo-conversión.
- **Pausar/reducir C** porque su CPA es casi el doble que A y consume demasiado presupuesto.
- **Redistribuir** enfocando el 64% del presupuesto en A, 24% en B y 12% en C.
- **Probar** cambios en landing, oferta y segmentación para mejorar aún más el rendimiento.

Con esta estrategia, podrías pasar de ~105 signups mensuales a ~130-140, manteniendo el mismo presupuesto.