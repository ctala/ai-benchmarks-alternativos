# Nemotron 3 Ultra 550B — sales_outreach/campaign_optimization

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 8.44 | quality: 9.74
- latency_total: 17.804s | tokens_per_second: 188.9
- input_tokens: 316 | output_tokens: 3364

## Respuesta completa

Aquí tienes el análisis completo con cálculos, decisiones estratégicas y plan de acción.

---

### 1. Cálculo de KPIs Principales

| Métrica | **Campaña A (Landing Principal)** | **Campaña B (Blog/TOFU)** | **Campaña C (Competidor)** |
| :--- | :---: | :---: | :---: |
| **CTR** (Clicks / Impr.) | **3.00%** (1,500 / 50k) | **4.00%** (4,800 / 120k) | **6.00%** (900 / 15k) |
| **CPC** (Costo / Clicks) | **$1.40** ($2,100 / 1,500) | **$0.38** ($1,800 / 4,800) | **$3.56** ($3,200 / 900) |
| **Conversion Rate** (Signups / Clicks) | **3.00%** (45 / 1,500) | **0.50%** (24 / 4,800) | **4.00%** (36 / 900) |
| **CPA** (Costo / Signups) | **$46.67** ($2,100 / 45) | **$75.00** ($1,800 / 24) | **$88.89** ($3,200 / 36) |
| **Share de Signups** | 43% | 23% | 34% |
| **Share de Gasto** | 30% | 26% | 44% |

---

### 2. ¿Qué escalar y qué pausar? (Justificación numérica)

#### ✅ **ESCALAR: Campaña A (Landing Principal)**
*   **Es el motor rentable:** Tiene el **CPA más bajo ($46.67)**, un 60% más eficiente que la siguiente mejor (C).
*   **Equilibrio sano:** Buen CTR (3%), CPC controlado ($1.40) y CR sólido (3%). Las keywords ("software gestión inventario") son *high intent* (fondo de embudo).
*   **Oportunidad:** Solo tiene 50k impresiones. Si el *Impression Share* < 80-90%, hay inventario barato por comprar.

#### ⚠️ **OPTIMIZAR (No pausar aún): Campaña C (Competidor)**
*   **El problema es el CPC ($3.56), no la conversión:** Tiene el **mejor CR (4%)**. La gente que busca "alternativa a [competidor]" está lista para comprar.
*   **CPA alto ($88.89)** por guerra de pujas. No pausar: **bajar pujas manuales / Target CPA** para forzar CPC ~$2.50. Si logras CPC $2.50 → CPA ~$62.50 (viable).
*   **Volumen bajo:** Solo 15k impresiones. Es una campaña de "cereza del pastel", no de volumen base.

#### 🛑 **PAUSAR / REESTRUCTURAR RADICALMENTE: Campaña B (Blog/TOFU)**
*   **Quema presupuesto:** Se lleva **$1,800 (36% del gasto)** para traer solo **24 signups (23% del total)**.
*   **CPA $75 es ineficiente** para tráfico frío de blog. El CR del **0.50%** confirma *intent mismatch*: la gente quiere leer "cómo gestionar inventario", no comprar software *ahora*.
*   **Acción:** **Pausar búsqueda pura**. Mover ese presupuesto a:
    1.  **Campaña A** (capturar demanda existente).
    2.  **Performance Max / Display / YouTube** para *retargeting* de esos 4,800 clicks baratos (audiencias de 30/90 días).
    3.  **Lead Magnets en el Blog:** Cambiar el CTA de "Regístrate" a "Descarga Checklist Gratis" → Nutrir por email → Vender después.

---

### 3. Redistribución del Presupuesto ($5,000/mes)

**Estrategia:** "Doblar la apuesta por lo que funciona (A), arreglar el CPC de lo que convierte bien (C), y convertir el gasto basura (B) en audiencia para retargeting".

| Campaña | Presupuesto Anterior | **Nuevo Presupuesto** | % Total | Lógica |
| :--- | :---: | :---: | :---: | :---: |
| **A (Principal)** | $2,100 | **$2,800** | **56%** | Escalable. A $46.67 CPA → **~60 signups/mes** (vs 45 actuales). |
| **C (Competidor)** | $3,200 | **$1,700** | **34%** | Recorte forzado para bajar CPC. Meta: CPC <$2.50 → **~27 signups/mes** (vs 36, pero rentables). |
| **B (Blog → Retargeting)** | $1,800 | **$500** | **10%** | Solo para alimentar audiencias (Display/YouTube/Discovery) + Test Lead Magnet. **Cero gasto en Búsqueda directa.** |
| **TOTAL** | **$7,100** | **$5,000** | **100%** | **Ahorro neto: $2,100/mes** manteniendo/o subiendo volumen de leads cualificados. |

**Proyección de Resultados Nuevo Mix:**
*   **Signups Estimados:** 60 (A) + 27 (C) + ~5 (Retargeting B) = **~92 Signups/mes**.
*   **CPA Blended Estimado:** $5,000 / 92 = **$54.35** (vs $77.78 actual).
*   **Resultado:** **+45% más leads** por **$2,100 menos de gasto**.

---

### 4. A/B Tests Sugeridos para Próximo Mes

#### **Campaña A (Prioridad Alta - Volumen Principal)**
| Test | Variante A (Control) | Variante B (Challenger) | Hipótesis / KPI a mover |
| :--- | :--- | :--- | :--- |
| **Landing Page** | Formulario largo (8-10 campos) + Texto genérico | **Formulario corto (Email + Empresa) + Video Demo 60s + Logos clientes** | **Subir CR 3% → 4.5%**. Reducir fricción inicial; video califica mejor el lead. |
| **Ad Copy (RSA)** | Beneficios genéricos ("Gestiona tu stock") | **Dolor específico + Número**: "Reduce mermas 30% en 2 semanas. Prueba gratis 14 días." | **Subir CTR 3% → 4.5%** y pre-cualificar clic (mejora CR posterior). |
| **Extensión de Formulario** | Sin extensión | **Lead Form Asset (nativo de Google)** | Testear costo/lead nativo vs landing. A veces CPA nativo es 20-30% menor. |

#### **Campaña C (Prioridad Media - Eficiencia)**
| Test | Variante A (Control) | Variante B (Challenger) | Hipótesis / KPI a mover |
| :--- | :--- | :--- | :--- |
| **Landing Page** | Landing genérica "Alternativa a [Competidor]" | **Tabla Comparativa Interactiva** (Checklist features: "Nosotros Sí / Competidor No") | **Subir CR 4% → 5.5%**. Justificar el CPC alto demostrando valor visual inmediato. |
| **Estrategia de Puja** | Manual CPC / Max Clicks | **Target CPA = $65** (o Max Conversions con límite CPA) | **Bajar CPC $3.56 → $2.50**. Dejar que el algoritmo apague horas/días caros. |
| **Keywords** | "Alternativa a [Comp]", "[Comp] vs" | **Añadir: "[Comp] precio", "[Comp] problemas", "Cancelar [Comp]"** | Capturar usuario *más abajo* en el funnel (frustrado/listo a cambiar), no solo comparando. |

#### **Campaña B / Retargeting (Nueva Estrategia)**
| Test | Concepto | Detalle |
| :--- | :--- | :--- |
| **Lead Magnet (Search/Display)** | **Checklist: "Auditoría de Inventario en 10 pasos (PDF)"** | En el blog, cambiar CTA "Prueba Gratis" → "Descarga Checklist". Costo/Lead objetivo <$10. Nutrir 5 emails → Demo. |
| **Audiencia Retargeting (YouTube/Display)** | **Video Testimonial Cliente (30s)** vs **Video Demo Producto (60s)** | Segmentar: Visitantes Blog (TOFU) vs Visitantes Pricing (BOFU). Medir *View-through Conversions* a 30 días. |
| **Performance Max (PMax)** | **Asset Group: "Blog Readers"** | Señales: Visitantes URLs Blog + Customer List (excluir clientes). Meta: CPA < $60 asistido. |

---

### Resumen Ejecutivo para tu Jefe/Cliente
> *"Recortamos gasto innecesario en tráfico informacional (Campaña B: -$1,800) que convertía a $75/lead. Reinyectamos en la campaña transaccional (A) y optimizamos pujas en Competidor (C) para bajar CPA de $89 a ~$65. **Proyectamos 92 leads/mes a $54 CPA blended (vs 105 leads a $78 CPA actual), ahorrando $2,100/mes.** Próximo mes testeamos Landing Pages de alta conversión en A y Comparativas en C para romper la barrera de $50 CPA."*