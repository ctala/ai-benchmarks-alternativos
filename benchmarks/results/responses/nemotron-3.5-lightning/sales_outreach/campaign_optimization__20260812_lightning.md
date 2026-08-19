# Nemotron 3.5 Lightning — sales_outreach/campaign_optimization

- model_id: `nvidia/nemotron-3.5-lightning`
- success: True  | final: 9.05 | quality: 10.0
- latency_total: 9.348s | tokens_per_second: 538.3
- input_tokens: 316 | output_tokens: 5032
- judge_score: 5.0 | justificación: 

## Respuesta completa

### 1. Métricas Calculadas

| Campaña | Impr. | Clics | Signups | Costo | CTR | CPC | CR (Signups/Clics) | CPA (Costo/Signups) |
|---------|-------|-------|---------|-------|-----|-----|---------------------|----------------------|
| **A**   | 50,000 | 1,500 | 45      | $2,100 | 3.0% | $1.40 | 3.0% | **$46.67** |
| **B**   | 120,000| 4,800 | 24      | $1,800 | 4.0% | $0.38 | 0.5% | **$75.00** |
| **C**   | 15,000 | 900   | 36      | $3,200 | 6.0% | $3.56 | 4.0% | **$88.89** |

**Notas:**
- **CTR** = Clics / Impresiones × 100
- **CPC** = Costo / Clics
- **CR** = Signups / Clics (tasa de conversión de clic a signup)
- **CPA** = Costo total / Signups
- **Presupuesto actual:** $2,100 + $1,800 + $3,200 = **$7,100** (estás $2,100 por encima de tu meta de $5,000/mes). Los cálculos siguientes asumen redistribuir un presupuesto total de **$5,000** optimizado.

---

### 2. ¿Qué campana escalar y cuál pausar?

**Análisis de eficiencia (signups por $100 invertido):**
- **Campaña A:** $100 → ~2.14 signups (mejor CPA)
- **Campaña B:** $100 → ~1.33 signups (CR muy baja, intención informacional)
- **Campaña C:** $100 → ~1.12 signups (mejor CR, pero CPA muy alto)

**Recomendación:**

| Campaña | Acción | Justificación numérica |
|---------|--------|------------------------|
| **A** | **Escalar (principal)** | Mejor relación costo-eficiencia (CPA $46.67). Palabras clave con intención de compra clara ("software gestión inventario", "inventario pymes"). CR del 3% es sólida para PPC. |
| **B** | **Pausar / Reducir al mínimo** | Aunque tiene el CPC más bajo ($0.38) y mucha exposición (120k impresiones), la CR es del 0.5% y el CPA sube a $75. Las keywords ("cómo gestionar inventario", "problemas inventario restaurante") son **informacionales**, no de compra. Gasto alto por poco retorno conversional. |
| **C** | **Pausar o testar con techo de CPA** | Mejor CR (4%) pero CPA $88.89 es casi el doble que la Campaña A. Palabras clave de comparación con competidor tienen alta intención, pero el volumen es bajo (900 clics) y el costo por adquisición es prohibitivo para un presupuesto de $5k. Solo valdría la pena si el LTV del cliente supera ampliamente los $90. |

**Veredicto:**  
- **Escalar la Campaña A** (aumentar inversión, mantener keywords, optimizar landing page).  
- **Pausar la Campaña B** para el objetivo de signups (puede mantenerse como campaña de "brand awareness" con presupuesto separado si el objetivo es reconocimiento de marca).  
- **Pausar o poner techo rígido a la Campaña C** hasta mejorar el CPC o validar que el LTV justifique el CPA.

---

### 3. Cómo redistribuir el presupuesto de $5,000

Basándonos en la eficiencia comprobada (signups por $100):

| Escenario | Campaña A | Campaña B | Campaña C | Inversión Total | Signups Esperados |
|-----------|-----------|-----------|-----------|-----------------|-------------------|
| **Conservador** | $3,000 | $500 | $1,500 | $5,000 | ~64 + 6 + 17 = **87** |
| **Óptimo (recomendado)** | $3,500 | $0 | $1,000 | $5,000 | ~75 + 0 + 11 = **86** |
| **Agresivo A** | $4,000 | $0 | $500 | $5,000 | ~86 + 0 + 5 = **91** |

**Plan recomendado (Óptimo):**
- **Campaña A: $3,500** (70% del presupuesto) → Espera ~75 signups. Aumentará el volumen de clics manteniendo el CPA ~$46.70. Invierte en ampliar el alcance de las keywords principales y mejorar la landing page.
- **Campaña C: $1,000** (20%) → Asigna solo si tests de optimización reducen el CPA a ≤$75. Si no, mejor mover ese $1k a A.
- **Campaña B: $500** (10%) → Solo para "monitoreo de marca" o para capturar variaciones de long-tail con intención comercial. Si después de 2 semanas no mejora el CR al ≥1%, pausar definitivamente.

**Por qué no invertir más en B:** A igualdad de condiciones, cada $100 en B genera 0.61 signups menos que en A. Reorientar ese dinero a A aumentaría tus signups en ~2-3 unidades por $100 movidos.

---

### 4. A/B Tests sugeridos para el próximo mes

**Campaña A (Landing principal):**
- **Test de formulario:** Variante A = formulario de 3 campos (nombre, email, empresa) vs Variante B = 1 solo campo (email). Mide impacto en CR y calidad de lead.
- **Test de headline/USP:** "Gestiona tu inventario en la nube" vs "Reduce errores de stock un 30% en 30 días". Prueba beneficio vs característica.
- **Test de prueba social:** Añadir logotipos de clientes reconocidos o "500+ pymes ya confían en nosotros" arriba del formulario.

**Campaña B (Blog / Contenido):**
- **Test de CTA dentro del post:** Botón "Descargar guía gratis" vs "Registrarse para prueba gratuita". El tráfico informacional suele convertir mejor con micro-commitments primero.
- **Test de palabras clave negativas:** Añadir negaciones como "gratis", "manual", "plantilla" para filtrar buscadores puramente informativos y subir el CR.
- **Test de formato de landing:** Landing page dedicada a cada artículo vs redirect directo al software. Mide si el usuario valora el contenido antes de comprometerse.

**Campaña C (Competidor):**
- **Test de copy de anuncio:** Formato "X vs [competidor]" vs "Alternativa a [competidor] - 20% de descuento". El incentivo directo suele bajar el CPC y subir el CR.
- **Test de landing page "Switcher":** Enfocarse en puntos de dolor de dejar al competidor (migración de datos, soporte, costo oculto) vs features generales.
- **Test de oferta de tiempo limitado:** "Prueba gratuita de 30 días + migración asistida" para reducir la barrera de cambio.

**Consejo general:**  
Implementa un solo test por campaña por semana, mide los resultados al día 7 y 14, y duplica lo que funcione. Dado que tu presupuesto es limitado, prioriza los tests que impacten directamente en el CPA (landing page, form length, offer) antes que cambios creativos menores.

---

**Resumen rápido:**  
- **Escalar A** (mejor CPA, intención de compra).  
- **Pausar B** (CR 0.5% muy baja para signups).  
- **Pausar/techo a C** (CPA $88.89 muy alto).  
- **Presupuesto $5k:** 70% A, 20% C (solo si optimiza), 10% B (test/minimal).  
- **Tests:** Formulario/headline en A; CTA/blog en B; offer/comparador en C.