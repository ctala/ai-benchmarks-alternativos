# GPT-OSS 20B (Groq) — sales_outreach/campaign_optimization

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 8.13 | quality: 9.36
- latency_total: 2.495s | tokens_per_second: 742.4
- input_tokens: 326 | output_tokens: 1852
- judge_score: 4.6 | justificación: 

## Respuesta completa

## 1. Métricas de cada campaña  

| Campaña | Impresiones | Clicks | Signups | Costo ($) | **CTR** | **CPC** | **CPA** | **CR** |
|---------|-------------|--------|---------|-----------|---------|---------|---------|--------|
| **A – Landing principal** | 50 000 | 1 500 | 45 | 2 100 | **3 %** | **$1.40** | **$46.67** | **3 %** |
| **B – Blog content** | 120 000 | 4 800 | 24 | 1 800 | **4 %** | **$0.38** | **$75.00** | **0.5 %** |
| **C – Competidor** | 15 000 | 900 | 36 | 3 200 | **6 %** | **$3.56** | **$88.89** | **4 %** |

*Fórmulas*  
- **CTR** = Clicks ÷ Impresiones  
- **CPC** = Costo ÷ Clicks  
- **CPA** = Costo ÷ Signups  
- **CR** = Signups ÷ Clicks  

---

## 2. ¿Qué campaña escalar y cuál pausar?  

| Campaña | CPA | CR | Comentario |
|---------|-----|----|------------|
| **A** | **$46.67** | 3 % | Mejor relación costo‑acquisición y buena tasa de conversión. |
| **B** | $75.00 | 0.5 % | Muy bajo CR, aunque CPC bajo → gran desperdicio de presupuesto. |
| **C** | $88.89 | 4 % | Alta tasa de conversión, pero CPC y CPA muy altos → menos rentable. |

**Recomendación**  
- **Escalar**: *Campaña A* (la más rentable).  
- **Pausar**: *Campaña B* (pérdida de presupuesto con conversiones mínimas).  
- *Campaña C* se mantiene con un presupuesto reducido; solo si quieres seguir aprovechando la alta CTR y la audiencia de competidores, pero no a plena capacidad.

---

## 3. Redistribución del presupuesto de $5 000  

| Campaña | Presupuesto propuesto | Razón |
|---------|----------------------|-------|
| **A – Landing principal** | **$3 500** | 70 % del total → maximiza la campaña más rentable. |
| **C – Competidor** | **$1 500** | 30 % restante → sigue captando a la audiencia interesada en el competidor, pero con menor gasto. |
| **B – Blog content** | **$0** | Pausada (costo de adquisición demasiado alto). |

**Total**: $3 500 + $1 500 = $5 000.

> *Nota:* Si decides mantener un pequeño test de contenido, podrías asignar $300‑$500 a una nueva variante de la Campaña B (o a un nuevo grupo de anuncios) y usar el resto para A.

---

## 4. A/B tests sugeridos para el próximo mes  

| Área | Test | Objetivo |
|------|------|----------|
| **Landing Page** | 1️⃣ Variar la llamada a la acción (CTA) – “¡Regístrate ahora!” vs “Descarga la demo” | Mejorar la tasa de conversión (CR). |
| | 2️⃣ Cambiar el encabezado principal (focus en “Gestión de inventario” vs “Ahorra tiempo y dinero”) | Aumentar relevancia y CTR. |
| **Anuncios** | 1️⃣ Prueba de diferentes titulares (foco en beneficio vs en solución de dolor) | Elevar CTR y disminuir CPC. |
| | 2️⃣ Añadir extensiones de llamada y de enlace de sitio | Incrementar la interacción y la calidad del anuncio. |
| **Segmentación** | 1️⃣ Crear un grupo de anuncios específico para “pymes” con palabras clave “software gestion inventario pymes” | Mejorar relevancia y reducir CPA. |
| | 2️⃣ Prueba de remarketing a visitantes del blog (Campaña B) con ofertas especiales | Mejorar la conversión de usuarios que ya mostraron interés. |
| **Oferta** | 1️⃣ Prueba de un descuento por tiempo limitado (10 % de descuento) | Aumentar el valor percibido y la tasa de conversión. |
| | 2️⃣ Ofrecer una prueba gratuita de 30 días | Reducir la barrera de entrada y mejorar la tasa de registro. |

### Cómo medir los resultados  
- **KPIs primarios**: CPA y CR.  
- **KPIs secundarios**: CTR y CPC.  
- **Duración del test**: mínimo 2 semanas o 200 clics por variante para asegurar significancia estadística.  

---

### Resumen rápido

| Acción | Resultado esperado |
|--------|--------------------|
| Escalar Campaña A | Mayor número de signups con menor CPA |
| Pausar Campaña B | Ahorro de presupuesto que se puede reinvertir |
| Reducir Campaña C | Mantener captación de competidores con menor costo |
| A/B tests | Optimizar landing, anuncios y segmentación para mejorar CTR, CR y CPA |

Con esta redistribución y los tests propuestos deberías ver un aumento sustancial en el retorno de inversión (ROI) de tu presupuesto de Google Ads. ¡Éxitos en el próximo mes!