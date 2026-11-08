# Gemini 4 Argon — sales_outreach/campaign_optimization

- model_id: `google/gemini-4-argon`
- success: True  | final: 6.77 | quality: 8.0
- latency_total: 44.091s | tokens_per_second: 37.8
- input_tokens: 319 | output_tokens: 1668

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

Aquí tienes el análisis completo de tus campañas de Google Ads, junto con las recomendaciones estratégicas basadas en los datos.

*(Nota inicial: El mes pasado gastaste un total de **$7,100** [$2,100 + $1,800 + $3,200], lo cual supera tu presupuesto objetivo de $5,000. El plan de redistribución ajustará esto).*

---

### 1. Métricas por Campaña

Fórmulas utilizadas:
*   **CTR (Click-Through Rate):** (Clicks / Impresiones) x 100
*   **CPC (Costo por Click):** Costo / Clicks
*   **CR (Conversion Rate):** (Signups / Clicks) x 100
*   **CPA (Costo por Adquisición/Signup):** Costo / Signups

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) | Total / Promedio |
| :--- | :--- | :--- | :--- | :--- |
| **Impresiones** | 50,000 | 120,000 | 15,000 | 185,000 |
| **Clicks** | 1,500 | 4,800 | 900 | 7,200 |
| **Signups** | 45 | 24 | 36 | 105 |
| **Costo** | $2,100 | $1,800 | $3,200 | $7,100 |
| **CTR** | **3.00%** | **4.00%** | **6.00%** | 3.89% |
| **CPC** | **$1.40** | **$0.375** | **$3.56** | $0.99 |
| **Conv. Rate (CR)**| **3.00%** | **0.50%** | **4.00%** | 1.46% |
| **CPA** | **$46.67** | **$75.00** | **$88.89** | $67.62 |

---

### 2. ¿Cuál campaña escalar y cuál pausar?

*   **ESCALAR: Campaña A (Landing principal).**
    *   **Justificación:** Es tu campaña más rentable. Tiene el **CPA más bajo ($46.67)**, casi la mitad que la campaña de competidores. Además, tiene una tasa de conversión muy saludable (3.00%) y un CPC moderado ($1.40). La intención de búsqueda es alta (usuarios buscando activamente una solución) y el volumen de búsquedas aún permite crecer sin encarecer demasiado la puja.
*   **PAUSAR (o reestructurar drásticamente): Campaña B (Blog content).**
    *   **Justificación:** Aunque trae tráfico muy barato (CPC $0.37) y tiene buen CTR (4%), su **tasa de conversión es pésima (0.50%)**, lo que dispara el **CPA a $75.00**. Las keywords ("cómo gestionar...") son informacionales (Top of Funnel). Estás pagando por usuarios que buscan aprender gratis, no comprar software. Con un presupuesto limitado de $5,000, no puedes darte el lujo de pagar tráfico de blog que no convierte directo, a menos que tengas un embudo de email marketing muy agresivo detrás.

*Nota sobre Campaña C (Competidor):* No se debe pausar porque tiene la mejor tasa de conversión (4%) y el mejor CTR (6%), pero su CPC ($3.56) infla el CPA a $88.89. Necesita optimización de costos, no eliminación.

---

### 3. Redistribución del Presupuesto ($5,000/mes)

Dado que debemos bajar el gasto de $7,100 a $5,000, debemos enfocar el dinero donde el retorno (Signups) sea mayor.

1.  **Campaña A (Landing Principal): $3,500 (70% del presupuesto)**
    *   *Proyección:* Si mantenemos el CPA de $46.67, obtendrás unos **75 signups** (30 más que el mes pasado).
2.  **Campaña C (Competidor): $1,200 (24% del presupuesto)**
    *   *Estrategia:* Reducir pujas para bajar el CPC o limitar las horas/días de publicación. Nos quedamos solo con las keywords exactas que mejor conviertan.
    *   *Proyección:* Asumiendo una leve mejora del CPA a ~$80 tras optimizar, obtendrás unos **15 signups**.
3.  **Campaña B (Transformada a Retargeting): $300 (6% del presupuesto)**
    *   *Estrategia:* Pausa las keywords del blog. Usa estos $300 para hacer **Remarketing (Display/Search)** a las 4,800 personas que visitaron el blog el mes pasado y a los que visitaron la Landing A pero no se registraron.
    *   *Proyección:* El retargeting suele tener un CPA bajo. Estimando un CPA de $30, lograrías **10 signups** adicionales.

**Resultado proyectado con $5,000:** ~100 Signups (Casi los mismos 105 del mes pasado, pero **ahorrando $2,100** y bajando el CPA promedio de $67.62 a **$50.00**).

---

### 4. A/B Tests sugeridos para el próximo mes

**Para la Campaña A (Escalamiento y eficiencia):**
*   **Test de Landing Page (CRO):** Prueba cambiar el "Hero" (la parte superior de la página).
    *   *Variante A (Control):* Tu página actual.
    *   *Variante B:* Un formulario de registro directo incrustado en el inicio (sin tener que hacer clic en un botón adicional) + Testimonios de PyMEs visibles sin hacer scroll. *Objetivo: Subir el CR del 3% al 4%.*

**Para la Campaña C (Reducción de CPA):**
*   **Test de Oferta en el Anuncio y Landing:** Como el CPC es muy caro ($3.56), necesitas que convierta aún más gente.
    *   *Variante A:* Landing genérica comparativa ("Por qué somos mejores que [Competidor]").
    *   *Variante B:* Oferta agresiva de "Robar cliente" ("¿Usas [Competidor]? Migra tus datos gratis en 24h y obtén 30% de descuento tus primeros 3 meses"). *Objetivo: Subir el CR del 4% al 6% para compensar el alto CPC.*

**Para la Campaña B (Si decides no pausarla del todo):**
*   **Test de "Lead Magnet" (Cambio de conversión):** El usuario del blog no está listo para un "Signup" del software.
    *   *Variante A:* Botón de "Prueba Gratis el Software" dentro del artículo.
    *   *Variante B:* Pop-up de intención de salida ofreciendo una "Plantilla de Excel gratis para inventario de restaurantes" a cambio de su correo (y luego los nutres por email para venderles el software).