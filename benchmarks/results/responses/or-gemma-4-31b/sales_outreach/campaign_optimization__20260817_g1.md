# Gemma 4 31B — sales_outreach/campaign_optimization

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 7.51 | quality: 8.0
- latency_total: 21.786s | tokens_per_second: 48.5
- input_tokens: 304 | output_tokens: 1057

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

Aquí tienes el análisis detallado de tus campañas. Primero, desglosamos las métricas para tener una base objetiva de decisión.

### 1. Cálculo de Métricas

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **CTR** (Clicks/Impr) | **3.00%** | **4.00%** | **6.00%** |
| **CPC** (Costo/Clicks) | **$1.40** | **$0.37** | **$3.55** |
| **CPA** (Costo/Signups) | **$46.66** | **$75.00** | **$88.88** |
| **Conv. Rate** (Signups/Clicks) | **3.00%** | **0.50%** | **4.00%** |

---

### 2. Análisis: ¿Qué escalar y qué pausar?

**Campaña a ESCALAR: Campaña A (Landing Principal)**
*   **Justificación:** Es la más equilibrada y eficiente. Tiene el **CPA más bajo ($46.66)**, lo que significa que es la forma más barata de conseguir un cliente. Aunque el CTR es menor que en la C, la tasa de conversión es saludable (3%) y el costo por click es moderado. Es tráfico de "alta intención de compra".

**Campaña a PAUSAR (o pivotar): Campaña B (Blog Content)**
*   **Justificación:** Aunque es la más barata en términos de CPC ($0.37) y atrae mucho tráfico, tiene una **tasa de conversión bajísima (0.50%)**. Estás pagando por tráfico informativo, no transaccional. El CPA es muy alto ($75) comparado con la Campaña A. Estás gastando presupuesto en personas que quieren "aprender", no necesariamente en personas que quieren "comprar".

**Campaña a OPTIMIZAR (Mantener con cautela): Campaña C (Competidor)**
*   **Justificación:** Tiene la mejor tasa de conversión (4%) y el mejor CTR (6%), lo que indica que la oferta es muy atractiva. Sin embargo, el **CPC es prohibitivo ($3.55)**, lo que dispara el CPA a $88.88. No se puede escalar agresivamente porque el costo del click mataría la rentabilidad.

---

### 3. Redistribución del Presupuesto ($5,000)

El objetivo es maximizar el número de Signups totales bajando el CPA promedio.

| Campaña | Presupuesto Sugerido | Justificación |
| :--- | :--- | :--- |
| **Campaña A** | **$3,000** (60%) | Es tu "caballo ganador". Al subir el presupuesto aquí, capturas más demanda de alta intención al costo más eficiente. |
| **Campaña C** | **$1,500** (30%) | Mantienes la presencia frente a la competencia y capturas leads calificados, pero limitas el gasto para que el CPA alto no afecte el promedio general. |
| **Campaña B** | **$500** (10%) | No la elimines totalmente, pero redúcela al mínimo. Úsala solo para alimentar el top-of-funnel (Remarketing) o para keywords muy específicas. |

---

### 4. Sugerencias de A/B Tests para el próximo mes

Para bajar el CPA y subir la conversión, implementaría lo siguiente:

**Para Campaña A (Landing Principal):**
*   **Test de Copy en CTA:** Probar "Prueba Gratis Ahora" vs "Empezar Gestión de Inventario Gratis".
*   **Test de Formulario:** Comparar un formulario de 5 campos vs uno de 3 campos (solo email y nombre) para ver si el aumento en signups compensa la calidad del lead.

**Para Campaña B (Blog):**
*   **Test de "Lead Magnet":** En lugar de intentar que se registren al software (signup), ofrece un "Template de Inventario en Excel Gratis" a cambio del email. Luego, convierte esos emails en usuarios del software mediante email marketing (estos leads son demasiado fríos para una landing de registro directo).

**Para Campaña C (Competidor):**
*   **Test de Propuesta de Valor:** Probar un anuncio que diga "Más barato que [Competidor]" vs uno que diga "Más funciones que [Competidor]". Necesitas saber qué es lo que hace que la gente quiera cambiar de software para bajar la resistencia al precio.