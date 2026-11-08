# Gemma 4 26B MoE (3.8B activos) — sales_outreach/campaign_optimization

- model_id: `google/gemma-4-26b-a4b-it`
- success: True  | final: 9.07 | quality: 10.0
- latency_total: 19.289s | tokens_per_second: 59.7
- input_tokens: 304 | output_tokens: 1151

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

Aquí tienes el análisis detallado de tus campañas. Primero, vamos a organizar los datos para poder tomar decisiones basadas en la eficiencia de cada dólar invertido.

### 1. Cálculos de Métricas Clave

| Métrica | Campana A (Landing) | Campana B (Blog) | Campana C (Competidor) |
| :--- | :--- | :--- | :--- |
| **CTR** (Clicks/Impresiones) | **3.00%** | **4.00%** | **6.00%** |
| **CPC** (Costo/Clicks) | **$1.40** | **$0.37** | **$3.55** |
| **CPA** (Costo/Signups) | **$46.67** | **$75.00** | **$88.88** |
| **Conv. Rate** (Signups/Clicks) | **3.00%** | **0.50%** | **4.00%** |

---

### 2. Diagnóstico: ¿Qué escalar y qué pausar?

**Escalar: Campana A (Landing Principal)**
*   **Justificación:** Es tu campaña más eficiente. Tiene el **CPA más bajo ($46.67)**, lo que significa que cada lead te cuesta casi la mitad que en la Campana C. Aunque su CTR es el más bajo, su **Tasa de Conversión (3%)** es excelente, lo que indica que el tráfico que atrae tiene una intención de compra muy alta y la landing page funciona bien.

**Pausar / Optimizar drásticamente: Campana B (Blog Content)**
*   **Justificación:** Aunque parece "barata" por su CPC de $0.37, es la que más dinero "desperdicia" en términos de conversión. Su **Tasa de Conversión es bajísima (0.50%)**. Estás pagando por curiosidad, no por intención de compra. El CPA de $75 es un 60% más caro que la Campana A.

**Mantener con cautela: Campana C (Competidor)**
*   **Justificación:** Es la campaña con mayor intención (CTR de 6% y Conv. Rate de 4%), pero es la más cara. El **CPC de $3.55** eleva el CPA a $88.88. No la pausaría porque los leads de competidores suelen ser de muy alta calidad, pero no es la prioridad de escalado debido al costo.

---

### 3. Redistribución del Presupuesto ($5,000/mes)

Actualmente gastas $7,100 (según tus datos), pero tu presupuesto real es de $5,000. Debemos optimizar para maximizar el número de Signups totales.

**Propuesta de distribución:**

1.  **Campana A (Prioridad 1): $3,000 (60%)**
    *   *Objetivo:* Capturar toda la demanda de intención directa. Es tu motor de crecimiento.
2.  **Campana C (Prioridad 2): $1,500 (30%)**
    *   *Objetivo:* Capturar usuarios que ya buscan soluciones. Al reducir el presupuesto aquí, evitas que el CPC alto agote tu caja, pero mantienes presencia en las búsquedas de la competencia.
3.  **Campana B (Prioridad 3): $500 (10%)**
    *   *Objetivo:* Mantener el "Top of Mind" y alimentar el embudo de retargeting, pero sin permitir que el bajo ratio de conversión consuma el presupuesto.

**Resultado esperado:** Al concentrar el dinero en la Campana A, bajarás tu CPA promedio global y aumentarás el volumen total de Signups.

---

### 4. Sugerencias de A/B Tests para el próximo mes

Para mejorar los resultados, no basta con mover dinero; hay que mejorar la eficiencia de cada campaña:

**Para la Campana A (Mejorar el CTR):**
*   **Test de Anuncios:** Prueba anuncios con "Social Proof" (ej: *"Más de 500 Pymes ya nos usan"*) vs. anuncios de "Beneficio Directo" (ej: *"Controla tu stock en tiempo real"*). El objetivo es subir ese 3% de CTR.

**Para la Campana B (Mejorar la Conversión):**
*   **Test de Lead Magnet:** El contenido de blog está atrayendo gente pero no convierte. En lugar de un botón de "Sign up" genérico, prueba un **"Template de Excel para Inventario Gratis"** a cambio del email. Esto convierte la "curiosidad" en "lead" de forma más natural.

**Para la Campana C (Mejorar el CPA):**
*   **Test de Landing Page Específica:** Si estás enviando el tráfico de "Alternativa a [Competidor]" a la landing principal, intenta crear una landing que diga: *"¿Cansado de [Competidor]? Descubre por qué somos la opción más ágil para Pymes"*. La relevancia reduce el CPC y aumenta la conversión.