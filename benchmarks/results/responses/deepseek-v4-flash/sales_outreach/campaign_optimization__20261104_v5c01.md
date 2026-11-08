# DeepSeek V4 Flash (OpenRouter) — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 7.7 | quality: 8.0
- latency_total: 29.283s | tokens_per_second: 55.1
- input_tokens: 272 | output_tokens: 1613

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

Aquí tienes el análisis detallado de tu campaña de Google Ads, basado en los datos proporcionados.

---

## 1. Cálculo de KPIs para cada campaña

### Fórmulas:
- **CTR** = (Clicks / Impresiones) × 100  
- **CPC** = Costo / Clicks  
- **CPA** = Costo / Signups  
- **Conversion Rate (CR)** = (Signups / Clicks) × 100  

### Campaña A (Landing principal)
- CTR = (1,500 / 50,000) × 100 = **3.0%**  
- CPC = $2,100 / 1,500 = **$1.40**  
- CPA = $2,100 / 45 = **$46.67**  
- CR = (45 / 1,500) × 100 = **3.0%**

### Campaña B (Blog content)
- CTR = (4,800 / 120,000) × 100 = **4.0%**  
- CPC = $1,800 / 4,800 = **$0.38**  
- CPA = $1,800 / 24 = **$75.00**  
- CR = (24 / 4,800) × 100 = **0.5%**

### Campaña C (Competidor)
- CTR = (900 / 15,000) × 100 = **6.0%**  
- CPC = $3,200 / 900 = **$3.56**  
- CPA = $3,200 / 36 = **$88.89**  
- CR = (36 / 900) × 100 = **4.0%**

---

## 2. ¿Cuál escalar y cuál pausar?

### Análisis:

| Campaña | CTR | CPC | CPA | CR | Eficiencia |
|---------|-----|-----|-----|----|------------|
| A | 3.0% | $1.40 | **$46.67** | 3.0% | ✅ **Mejor CPA** |
| B | 4.0% | $0.38 | $75.00 | 0.5% | ❌ CPA alto, CR muy bajo |
| C | 6.0% | $3.56 | $88.89 | 4.0% | ❌ CPA más alto, volumen bajo |

### Recomendación:

- **Escalar Campaña A**:  
  - Tiene el **CPA más bajo ($46.67)** y un CR sólido (3%).  
  - Aunque el CTR es menor que B y C, el costo por conversión es el mejor.  
  - Con más presupuesto podrías aumentar impresiones y clicks manteniendo un CPA competitivo.

- **Pausar Campaña B**:  
  - A pesar de tener el CPC más bajo ($0.38) y buen CTR (4%), su **CR es solo 0.5%**.  
  - Esto significa que el tráfico es barato pero de **muy baja intención** (lectores de blog, no compradores).  
  - El CPA ($75) es 60% más caro que la campaña A.

- **Pausar o reestructurar Campaña C**:  
  - Tiene el CTR más alto (6%) y buen CR (4%), pero el **CPA es el peor ($88.89)** debido al alto CPC ($3.56).  
  - El volumen es bajo (solo 36 signups con $3,200).  
  - Podrías mantenerla solo si consigues reducir el CPC (ej. mejorando el Quality Score o ajustando pujas).

---

## 3. Redistribución del presupuesto ($5,000/mes)

### Propuesta:

| Campaña | Presupuesto actual | Propuesto | Cambio | Justificación |
|---------|-------------------|-----------|--------|---------------|
| A | $2,100 | **$3,500** | +$1,400 | Mejor CPA, escalable |
| B | $1,800 | **$0** | -$1,800 | Pausar por CR muy bajo |
| C | $3,200 | **$1,500** | -$1,700 | Reducir, solo si se optimiza |

**Total**: $3,500 + $1,500 = $5,000

### Explicación:
- **Campaña A**: Recibe el 70% del presupuesto. Con $3,500, manteniendo el mismo CPA, podrías obtener ~75 signups (vs 45 actuales).  
- **Campaña C**: Se reduce a $1,500 para mantener presencia en búsquedas de competidores, pero solo si trabajas en bajar el CPC (ej. ajustando pujas a manual, mejorando anuncios).  
- **Campaña B**: Se pausa completamente. El dinero se redirige a A.

---

## 4. A/B Tests sugeridos para el próximo mes

### Para Campaña A (Landing principal):
1. **Test de landing page**:  
   - Versión A: Actual (genérica)  
   - Versión B: Página específica para "software inventario pymes" con testimonial y demo gratuita.  
   - **Métrica**: CR y CPA.

2. **Test de título de anuncio**:  
   - Versión A: "Software de Inventario para Pymes"  
   - Versión B: "Prueba Gratis - Gestiona tu Inventario en Minutos"  
   - **Métrica**: CTR y CPC.

### Para Campaña C (Competidor):
1. **Test de palabras clave negativas**:  
   - Añadir términos como "gratis", "tutorial", "precio" para filtrar tráfico de baja intención.  
   - **Métrica**: CPA y CR.

2. **Test de llamado a la acción (CTA)**:  
   - Versión A: "Compara [competidor] vs [tu producto]"  
   - Versión B: "Descubre por qué [tu producto] es mejor"  
   - **Métrica**: CTR y tasa de conversión.

### Opcional (si reactivas Campaña B):
- **Test de oferta en blog**:  
   - Versión A: Lead magnet (ebook "Guía de inventario para restaurantes")  
   - Versión B: Webinar gratuito  
   - **Métrica**: CR de signups.

---

## Resumen ejecutivo

| Decisión | Campaña | Motivo principal |
|----------|---------|------------------|
| ✅ Escalar | A | Mejor CPA ($46.67) y CR (3%) |
| ❌ Pausar | B | CR muy bajo (0.5%) a pesar de bajo CPC |
| ⚠️ Reducir | C | CPA alto ($88.89), solo mantener si se optimiza |

**Presupuesto final**:  
- Campaña A: $3,500  
- Campaña C: $1,500  
- Campaña B: $0 (pausada)

**Próximo paso**: Implementar A/B tests en landing page y anuncios de la campaña A para mejorar aún más el CPA.