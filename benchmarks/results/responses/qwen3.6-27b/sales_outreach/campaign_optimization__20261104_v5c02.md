# Qwen 3.6 27B base (OpenRouter FP8) — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3.6-27b`
- success: True  | final: 8.45 | quality: 10.0
- latency_total: 45.302s | tokens_per_second: 44.5
- input_tokens: 311 | output_tokens: 2017

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

Aquí tienes el análisis detallado de tus campañas, los cálculos métricos y la estrategia recomendada para optimizar tu presupuesto de $5,000.

### 1. Cálculo de Métricas (CTR, CPC, CPA, Conversion Rate)

Para facilitar la comparación, he calculado las siguientes métricas clave:
*   **CTR (Click-Through Rate):** Clicks / Impresiones
*   **CPC (Costo Por Clic):** Costo / Clicks
*   **CR (Tasa de Conversión):** Signups / Clicks
*   **CPA (Costo Por Adquisición/Signup):** Costo / Signups

| Métrica | Campaña A (Landing Principal) | Campaña B (Blog Content) | Campaña C (Competidor) |
| :--- | :---: | :---: | :---: |
| **Impresiones** | 50,000 | 120,000 | 15,000 |
| **Clicks** | 1,500 | 4,800 | 900 |
| **Signups** | 45 | 24 | 36 |
| **Costo Total** | $2,100 | $1,800 | $3,200 |
| **CTR** | **3.00%** | **4.00%** | **6.00%** |
| **CPC** | **$1.40** | **$0.375** | **$3.55** |
| **Conversion Rate (CR)** | **3.00%** | **0.50%** | **4.00%** |
| **CPA** | **$46.67** | **$75.00** | **$88.89** |

---

### 2. ¿Cuál campaña escalar y cuál pausar? Justificación con números

#### 🚀 **Escalar: Campaña A (Landing Principal)**
*   **Justificación:** Es la campaña más eficiente en términos de costo por adquisición (**CPA más bajo: $46.67**).
*   Aunque tiene un CTR menor que B y C, su tasa de conversión (3%) es sólida y su CPC es razonable ($1.40).
*   Genera casi el doble de signups que la Campaña B con un costo similar, y más del doble que la Campaña C con menos de la mitad del gasto.
*   **Conclusión:** Es tu motor de crecimiento rentable. Deberías invertir más aquí para obtener más volumen a un buen precio.

#### ⚠️ **Revisar/Pausar Parcialmente: Campaña C (Competidor)**
*   **Justificación:** Tiene el **CPA más alto ($88.89)**, lo que significa que te cuesta casi el doble adquirir un cliente aquí que en la Campaña A.
*   Sin embargo, tiene el **CTR más alto (6%)** y una buena tasa de conversión (4%). Esto indica que el tráfico es de alta intención (gente buscando alternativas), pero el CPC es muy caro ($3.55).
*   **Decisión:** No la pauses completamente si puedes permitirla como "marca blanca" o defensa competitiva, pero **no la escalas**. Su ROI es el peor de las tres. Si necesitas maximizar el número total de signups con presupuesto limitado, esta es la primera candidata a recorte severo o pausa.

#### ❌ **Pausar o Reestructurar Urgentemente: Campaña B (Blog Content)**
*   **Justificación:** Aunque tiene un CPC muy bajo ($0.375) y mucho tráfico, su **tasa de conversión es terrible (0.5%)** y su **CPA es alto ($75)**.
*   Estás pagando por clics baratos, pero esos usuarios no están listos para convertirse. El contenido del blog probablemente atrae a personas en etapa de investigación ("cómo gestionar"), no de compra.
*   Con $1,800 solo obtuviste 24 signups. Si hubieras invertido ese mismo dinero en la Campaña A, habrías obtenido ~38 signups (calculado inversamente: $1,800 / $46.67 ≈ 38.5).
*   **Conclusión:** Esta campaña está desperdiciando presupuesto. O bien la landing page/blog no convierte bien, o la intención de búsqueda es demasiado fría.

> **Resumen de decisión:**
> *   **Escalar:** Campaña A
> *   **Mantener (con cuidado):** Campaña C (solo si el valor de vida del cliente LTV justifica un CPA de $89)
> *   **Pausar/Reestructurar:** Campaña B

---

### 3. Redistribución del Presupuesto de $5,000

Dado que el objetivo implícito es maximizar signups de forma eficiente, redistribuiría el presupuesto así:

| Campaña | Presupuesto Anterior | Nuevo Presupuesto | % del Total | Razonamiento |
| :--- | :---: | :---: | :---: | :--- |
| **A (Principal)** | $2,100 | **$3,200** | 64% | Escalar la campaña más eficiente. Esperamos obtener ~68 signups adicionales ($3,200 / $46.67). |
| **C (Competidor)** | $3,200 | **$1,000** | 20% | Mantener presencia defensiva pero limitar pérdidas. Esperamos ~11 signups ($1,000 / $88.89). |
| **B (Blog)** | $1,800 | **$800** | 16% | No pausar del todo para mantener visibilidad en búsquedas informativas, pero reducir drásticamente. Se puede usar para nutrir leads fríos mediante retargeting. |
| **Total** | $7,100* | **$5,000** | 100% | *Nota: Tu gasto anterior superaba el presupuesto actual.* |

> **Proyección estimada de signups con nueva distribución:**
> *   Campaña A: ~68 signups
> *   Campaña C: ~11 signups
> *   Campaña B: ~10 signups (si mejora ligeramente) o ~10-12 si se mantiene igual
> *   **Total estimado: ~89-91 signups/mes** vs los actuales 105 signups con $7,100.
>
> *Nota:* Aunque el número total de signups podría bajar ligeramente al ajustar al presupuesto real de $5k, el **CPA promedio global mejorará significativamente**, y estarás operando dentro de tu límite financiero. Además, al pausar B, podrías reinvertir esos $800 en mejorar la landing page de A o en retargeting.

---

### 4. Sugerencias de A/B Tests para el Próximo Mes

#### ✅ Para la Campaña A (La ganadora):
1.  **Test de Landing Page:** Prueba una versión con un formulario más corto (ej. solo email + nombre) vs. uno más largo. Objetivo: aumentar la CR del 3% al 4%.
2.  **Test de Anuncio:** Prueba anuncios con enfoque en "beneficio económico" vs. "ahorro de tiempo". Mide cuál tiene mayor CTR y mantiene el CPA bajo.

#### ✅ Para la Campaña B (La problemática):
1.  **Test de Intención de Búsqueda:** Cambia las keywords de "como gestionar inventario" (informativo) a "mejor software inventario gratis prueba" (transaccional). Esto podría mejorar la CR del 0.5% al 1.5%+.
2.  **Test de Contenido:** En lugar de enviar al blog general, envía a una página específica con una guía descargable (lead magnet) para capturar emails antes de vender.

#### ✅ Para la Campaña C (Competidor):
1.  **Test de Negativa:** Agrega palabras clave negativas genéricas que atraigan tráfico irrelevante (ej. "gratis", "descargar") para bajar el CPC sin perder relevancia.
2.  **Test de Oferta Especial:** En el anuncio, ofrece un descuento exclusivo para usuarios que vienen del competidor (ej. "Migra desde [Competidor] y obtén 20% off"). Esto puede mejorar la CR y justificar el CPC alto.

---

### 💡 Recomendación Final
Tu mayor problema no es el tráfico, sino la **calidad del tráfico en la Campaña B** y el **costo excesivo en la Campaña C**. 
Enfócate en **escalar la Campaña A** y considera convertir la Campaña B en una estrategia de **nutrición por email** (capturar leads con contenido gratuito y luego venderles por correo) en lugar de intentar vender directamente desde el blog.