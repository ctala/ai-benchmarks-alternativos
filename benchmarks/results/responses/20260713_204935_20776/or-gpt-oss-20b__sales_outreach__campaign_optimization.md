# GPT-OSS 20B — sales_outreach/campaign_optimization

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 9.26 | quality: 10.0
- latency_total: 19.015s | tokens_per_second: 107.7
- input_tokens: 320 | output_tokens: 2048
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando análisis detallados y recomendaciones prácticas para la optimización de campañas.

## Respuesta completa

## 1. Métricas clave (por campaña)

| Campaña | Impresiones | Clicks | Signups | Costo | **CTR %** | **CPC $** | **CPA $** | **CR %** |
|---------|-------------|--------|---------|-------|-----------|-----------|-----------|----------|
| **A – Landing principal** | 50 000 | 1 500 | 45 | 2 100 | **3.0 %** | **1.40 $** | **46.66 $** | **3.0 %** |
| **B – Blog content** | 120 000 | 4 800 | 24 | 1 800 | **4.0 %** | **0.38 $** | **75.00 $** | **0.50 %** |
| **C – Competidor** | 15 000 | 900 | 36 | 3 200 | **6.0 %** | **3.56 $** | **88.89 $** | **4.0 %** |

**Cálculos**  
- **CTR** = Clicks / Impresiones × 100  
- **CPC** = Costo / Clicks  
- **CPA** = Costo / Signups  
- **CR** (tasa de conversión) = Signups / Clicks × 100  

---

## 2. ¿Qué escalar y qué pausar?

| Campaña | Por qué es la mejor / peor |
|---------|---------------------------|
| **A – Landing principal** | 1️⃣ CPA más bajo (46.66 $) → coste más bajo por suscriptor. <br>2️⃣ CR moderada (3 %) y CTR decente. <br>3️⃣ Estrategia de palabras clave “software gestion inventario” está funcionando bien. |
| **B – Blog content** | 1️⃣ CPA alto (75 $) y CR muy baja (0.5 %) → poco retorno por clic. <br>2️⃣ El coste por clic es bajo (0.38 $), pero la conversión es insuficiente para justificar la inversión. <br>3️⃣ Los usuarios llegan a un blog, no a la landing de suscripción. |
| **C – Competidor** | 1️⃣ CPA alto (88.89 $), aunque la CR es la más alta (4 %) y CTR alto (6 %). <br>2️⃣ El coste por clic es elevado (3.56 $). <br>3️⃣ Si el objetivo es captar usuarios dispuestos a probar alternativas, vale la pena, pero es el más caro. |

**Decisión recomendada**  

| Acción | Campaña | Justificación numérica |
|--------|---------|------------------------|
| **Escalar** | **A – Landing principal** | CPA 46.66 $ es la más económica; al duplicar el presupuesto se obtendrá, en promedio, 45 × 2 ≈ 90 suscriptores por 4 200 $ → 46 $ por suscriptor. |
| **Mantener moderadamente** | **C – Competidor** | Aún produce la mayor CR, pero su CPA es 88.89 $; con un presupuesto menor se sigue generando suscriptores de calidad sin sobrecargar el coste. |
| **Pausar / reducir drásticamente** | **B – Blog content** | CPA 75 $ y CR 0.5 % indican que la conversión es insuficiente; el gasto de 1 800 $ solo genera 24 suscriptores. Si se mantiene, el ROI es bajo. Se recomienda detenerla o reducirla a 0 $ (reorientar la audiencia a las otras campañas). |

---

## 3. Redistribución del presupuesto ($5 000)

| Campaña | Presupuesto propuesto | Porcentaje |
|---------|-----------------------|------------|
| **A – Landing principal** | **$2 500** | 50 % |
| **C – Competidor** | **$1 500** | 30 % |
| **B – Blog content** | **$0 (o $500 mínimo)** | 0–10 % |

**Razones**  
1. **A**: El CPA más bajo y la buena conversión justifican el mayor share.  
2. **C**: La CR alta (4 %) y el CTR (6 %) indican que la audiencia está interesada, pero el coste es alto → presupuesto moderado.  
3. **B**: Se elimina el gasto que produce pocos suscriptores; los recursos se transfieren a A y C.  
4. **Total**: 2 500 $ + 1 500 $ = **$4 000**. Se deja un margen de **$1 000** para pruebas A/B (p. ej. nuevas palabras clave, versiones de anuncio) o para aumentar el presupuesto de A si los resultados son positivos.

---

## 4. A/B tests sugeridos para el próximo mes

| Área | Test | Objetivo | Métrica de éxito |
|------|------|----------|-------------------|
| **Landing principal (Campaña A)** | 1️⃣ Copia del anuncio: “Gestiona tu inventario en 30 seg” vs “Control total de inventario en tiempo real” | Mejorar CTR y CPA | CTR ↑ > +0.5 % y CPA ↓ > 10 % |
| | 2️⃣ Variantes de landing: “Formulario de 1 campo” vs “Formulario de 3 campos” | Reducir fricción | CR ↑ > +0.5 % |
| | 3️⃣ Extensiones de anuncio: “Testimonios” vs “Demo gratis” | Aumentar relevancia | CTR ↑ > +0.3 % |
| **Competidor (Campaña C)** | 1️⃣ Palabras clave: “alternativa a [competidor]” vs “[competidor] vs” | Mejorar calidad de clics | CPC ↓ > 5 % y CPA ↓ > 5 % |
| | 2️⃣ Extensiones de llamada y ubicación | Incrementar conversiones offline | CPA ↓ > 10 % |
| **Blog content (Campaña B)** | 1️⃣ Test de contenido: “Cómo gestionar inventario en restaurantes” vs “Errores comunes en inventario de pymes” | Mejorar retención | Tiempo en página ↑ > 20 % |
| | 2️⃣ CTA interno: “Descarga el checklist” vs “Suscríbete al webinar” | Aumentar conversiones | CR interna ↑ > 1 % |
| | 3️⃣ Reorientación a la landing de suscripción después de 3 min | Capturar leads | CAC interno ↓ > 15 % |

**Implementación**  
- **Duración**: 2‑4 semanas por test (según volumen de tráfico).  
- **Segmentación**: Igual para ambos grupos para asegurar comparabilidad.  
- **Herramientas**: Google Optimize o Experiments en Google Ads.  

---

### Resumen rápido

| Campaña | Decisión | Presupuesto |
|