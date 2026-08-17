# DeepSeek V4 Flash (OpenRouter) — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v4-flash`
- success: True  | final: 8.4 | quality: 9.92
- latency_total: 54.72s | tokens_per_second: 58.2
- input_tokens: 272 | output_tokens: 3185
- judge_score: 5.0 | justificación: 

## Respuesta completa

### 1. Métricas calculadas por campaña

| Campaña | CTR | CPC | CPA | Tasa de conversión (CVR) |
|---------|-----|-----|-----|--------------------------|
| **A** (Landing principal) | 3% | $1.40 | $46.67 | 3% |
| **B** (Blog content) | 4% | $0.375 | $75.00 | 0.5% |
| **C** (Competidor) | 6% | $3.56 | $88.89 | 4% |

**Fórmulas:**
- CTR = (Clicks / Impresiones) × 100
- CPC = Costo / Clicks
- CPA = Costo / Signups
- CVR = (Signups / Clicks) × 100

---

### 2. ¿Qué campaña escalar y cuál pausar?

**Escalar: Campaña A**  
- Tiene el **CPA más bajo** ($46.67), un 38% más barato que B ($75) y un 47% más barato que C ($88.89).  
- Su tasa de conversión (3%) es sólida y su CPC ($1.40) es razonable.  
- Con $2,100 generó 45 registros; si se escala, se espera obtener más conversiones a un costo eficiente.

**Pausar: Campaña C**  
- Presenta el **CPA más alto** ($88.89) y un CPC elevado ($3.56), lo que la hace poco rentable.  
- Aunque su CVR (4%) es la mejor, el costo por clic es tan alto que cada registro cuesta casi el doble que en A.  
- Con $3,200 solo obtuvo 36 registros, mientras que A con $2,100 consiguió 45.

**Consideración sobre Campaña B**  
- Su CPA ($75) es intermedio, pero su **tasa de conversión es muy baja** (0.5%). Esto indica que los clics (4,800) no se traducen en registros, probablemente porque el contenido del blog no está optimizado para conversión.  
- Se recomienda **reducir su presupuesto drásticamente** o pausarla temporalmente hasta realizar mejoras.

---

### 3. Redistribución del presupuesto total ($5,000)

Basado en la eficiencia actual:

| Campaña | Presupuesto propuesto | Justificación |
|---------|----------------------|---------------|
| **A** | **$4,000** | Escalar la campaña más rentable. Con $2,100 actuales, se pueden aumentar las pujas y ampliar keywords similares para captar más tráfico de calidad. |
| **B** | **$1,000** | Mantener un presupuesto mínimo para realizar pruebas A/B y optimizar la conversión. Si no mejora en 2-3 semanas, pausar por completo. |
| **C** | **$0** | Pausar por completo. Su CPA alto no justifica la inversión, incluso con buena CVR. |

*Alternativa más agresiva:* Asignar los $5,000 completos a la campaña A si se confirma que no hay saturación (ej. aumento de CPC). Pero con los datos actuales, $4,000 es un incremento razonable para escalar.

---

### 4. Pruebas A/B para el próximo mes

**Campaña A (Landing principal)**  
- **Objetivo:** Mejorar aún más la tasa de conversión (actual 3%).  
- **Prueba 1:** Dos versiones de la landing page – una con formulario corto (solo email) vs. otra con formulario completo (nombre, empresa, teléfono).  
- **Prueba 2:** Cambiar el CTA principal: “Prueba gratis 14 días” vs. “Solicitar demo personalizada”.  
- **Prueba 3:** Añadir un video explicativo vs. mantener solo texto e imágenes.

**Campaña B (Blog content)**  
- **Objetivo:** Aumentar la tasa de conversión (actual 0.5%).  
- **Prueba 1:** Redirigir el tráfico del blog a una página de aterrizaje específica con un lead magnet (ej. “Guía gratuita para gestionar inventario en restaurantes”) en lugar de mantener el artículo completo.  
- **Prueba 2:** Probar anuncios con diferentes enfoques: “Problemas de inventario? Solución en 5 pasos” vs. “Software que resuelve el caos de tu inventario”.  
- **Prueba 3:** Incluir un pop-up con oferta de descarga condicional (con registro) vs. un banner estático al final del artículo.

**Campaña C (si se decide mantener)**  
- **Objetivo:** Reducir el CPA.  
- **Prueba:** Segmentar palabras clave más específicas (ej. “alternativa a [competidor] para pymes”) y probar anuncios que comparen directamente ventajas (precio, funcionalidades). También añadir palabras clave negativas para evitar tráfico de baja intención.

> **Nota:** Dado que se recomienda pausar C, las pruebas solo tendrían sentido si se reasigna un pequeño presupuesto para intentar mejorar su eficiencia antes de descartarla definitivamente.