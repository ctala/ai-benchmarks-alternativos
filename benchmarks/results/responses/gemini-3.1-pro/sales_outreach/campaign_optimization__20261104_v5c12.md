# Gemini 3.1 Pro — sales_outreach/campaign_optimization

- model_id: `google/gemini-3.1-pro-preview`
- success: True  | final: 6.74 | quality: 8.0
- latency_total: 41.267s | tokens_per_second: 86.3
- input_tokens: 291 | output_tokens: 3561

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

Aquí tienes un análisis detallado de tus campañas. 

*Nota inicial importante: El mes pasado gastaste un total de **$7,100** ($2,100 + $1,800 + $3,200). Como tu presupuesto objetivo es de **$5,000/mes**, necesitamos hacer recortes estratégicos para ajustarnos a tu presupuesto y maximizar la rentabilidad.*

---

### 1. Cálculos de KPIs (CTR, CPC, CPA y Conversion Rate)

Aquí están las métricas clave para cada campaña:

**Campaña A (Landing principal):**
*   **CTR:** 3.00% *(1,500 / 50,000)*
*   **CPC:** $1.40 *($2,100 / 1,500)*
*   **CPA:** **$46.67** *($2,100 / 45)*
*   **Conversion Rate (CR):** 3.00% *(45 / 1,500)*

**Campaña B (Blog content):**
*   **CTR:** 4.00% *(4,800 / 120,000)*
*   **CPC:** $0.38 *($1,800 / 4,800)*
*   **CPA:** $75.00 *($1,800 / 24)*
*   **Conversion Rate (CR):** **0.50%** *(24 / 4,800)*

**Campaña C (Competidor):**
*   **CTR:** **6.00%** *(900 / 15,000)*
*   **CPC:** $3.56 *($3,200 / 900)*
*   **CPA:** $88.89 *($3,200 / 36)*
*   **Conversion Rate (CR):** 4.00% *(36 / 900)*

---

### 2. ¿Cuál escalar y cuál pausar?

**✅ ESCALAR: Campaña A (Landing principal)**
*   **Justificación:** Es tu campaña más rentable. Tiene el **CPA más bajo ($46.67)**, lo que significa que adquieres clientes a casi la mitad del costo que en la Campaña C. Tiene un buen equilibrio entre volumen de clics, costo por clic ($1.40) y tasa de conversión (3%). Las palabras clave muestran una alta intención de compra ("software gestion", "inventario pymes").

**❌ PAUSAR: Campaña B (Blog content)**
*   **Justificación:** Aunque atrae muchísimo tráfico barato (CPC de $0.38) y tiene buen CTR (4%), **su tasa de conversión es terrible (0.50%)**. Las personas que buscan "cómo gestionar" están en una fase educativa (Top of Funnel), no están listas para comprar o registrarse (Bottom of Funnel). Esto eleva tu CPA a $75.00. Con un presupuesto limitado a $5,000, no puedes permitirte pagar por tráfico que no convierte.

**⚠️ OPTIMIZAR (No pausar, pero no escalar): Campaña C (Competidor)**
*   **Justificación:** Tiene la mejor tasa de conversión (4%) y el mejor CTR (6%), lo que demuestra que esta audiencia está lista para comprar. El problema es que **el CPC es altísimo ($3.56)**, lo que dispara tu CPA a $88.89 (el más caro). Debes mantenerla pero limitando su gasto o bajando las pujas (bids) para forzar un CPA más bajo.

---

### 3. Redistribución del presupuesto de $5,000

Dado que debes reducir tu gasto de $7,100 a $5,000, te sugiero esta distribución enfocada en maximizar los *signups*:

*   **Campaña A (Landing principal): $3,800 (76% del presupuesto)**
    *   *Proyección:* Al escalar esta campaña, el CPA podría subir ligeramente por la saturación, pero asumiendo un CPA conservador de $50, generarías unos **76 signups**.
*   **Campaña C (Competidor): $1,200 (24% del presupuesto)**
    *   *Estrategia:* Cambia la estrategia de puja a "CPA Objetivo" (Target CPA) y fíjalo en $60-$65, o pon un límite de CPC máximo. Al reducir el presupuesto, Google se verá obligado a buscar los clics más baratos dentro de esa audiencia.
    *   *Proyección:* Asumiendo que logras bajar el CPA a $70, generarías unos **17 signups**.
*   **Campaña B (Blog content): $0 (Pausada)**
    *   Redirigimos este dinero a la Campaña A.

**Resultado proyectado:** Con $5,000 conseguirías aproximadamente **93 signups** (CPA promedio de $53.70). 
*(El mes pasado gastaste $7,100 para 105 signups con un CPA promedio de $67.60. Esta nueva estructura es mucho más eficiente).*

---

### 4. A/B Tests sugeridos para el próximo mes

**Para la Campaña A (Tu motor principal):**
1.  **Test de Landing Page (Headline y CTA):** Ya tienes un 3% de conversión, lo cual es bueno, pero si lo subes al 4%, tu CPA bajará drásticamente. Prueba un título enfocado en el beneficio vs. uno enfocado en la característica. (Ej. *"Ahorra 10 horas a la semana en tu inventario"* vs *"El mejor software de inventario para Pymes"*).
2.  **Test de Extensiones de Anuncio:** Prueba agregar extensiones de imagen o de enlaces de sitio (sitelinks) específicos como "Precios", "Casos de éxito" o "Prueba gratis de 14 días" para intentar subir ese CTR del 3% al 4%.

**Para la Campaña C (Competidores):**
1.  **Test de Landing Page Comparativa:** Si actualmente los envías a tu landing principal, **crea una landing específica de "[Tu Marca] vs [Competidor]"**. Como el tráfico es muy caro, necesitas que la tasa de conversión suba del 4% al 6% o 7%. Muestra una tabla comparativa clara donde tu software gane en precio o funcionalidades clave.
2.  **Test de Ad Copy (Anuncios):** Prueba un anuncio agresivo en precio (Ej. *"50% más barato que [Competidor]"*) vs un anuncio agresivo en soporte/calidad (Ej. *"Migración gratuita desde [Competidor]"*). Esto puede mejorar tu Nivel de Calidad (Quality Score) y bajar ese CPC de $3.56.

**Para la Campaña B (Si decides reactivarla en el futuro):**
1.  **Test de Oferta (Lead Magnet vs Signup):** El error de esta campaña es pedir un "Signup" (alta fricción) a alguien que solo quiere leer un blog. Si la reactivas, cambia el objetivo: ofréceles una "Plantilla de Excel gratuita para inventarios" a cambio de su email. Tu tasa de conversión subirá enormemente, y luego puedes venderles el software a través de una secuencia de emails automatizada.