# Gemini 3.5 Flash Lite — sales_outreach/campaign_optimization

- model_id: `google/gemini-3.5-flash-lite`
- success: True  | final: 7.45 | quality: 8.0
- latency_total: 5.774s | tokens_per_second: 238.5
- input_tokens: 291 | output_tokens: 1377

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

Aquí tienes el análisis detallado de tu campaña de Google Ads basado en los datos del último mes.

---

### 1. Métricas Clave por Campaña

Para calcular estas métricas usamos las siguientes fórmulas:
*   **CTR** (Click-Through Rate) = Clicks / Impresiones
*   **CPC** (Costo por Clic) = Costo / Clicks
*   **CPA** (Costo por Adquisición/Signup) = Costo / Signups
*   **CR** (Conversion Rate / Tasa de Conversión) = Signups / Clicks

| Métrica | Campaña A (Landing Principal) | Campaña B (Blog Content) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **Impresiones** | 50,000 | 120,000 | 15,000 |
| **Clicks** | 1,500 | 4,800 | 900 |
| **Signups** | 45 | 24 | 36 |
| **Costo** | $2,100 | $1,800 | $3,200 |
| **CTR** | **3.00%** | **4.00%** | **6.00%** |
| **CPC** | **$1.40** | **$0.38** | **$3.56** |
| **CPA** | **$46.67** | **$75.00** | **$88.89** |
| **CR (Clicks a Signup)**| **3.00%** | **0.50%** | **4.00%** |

---

### 2. ¿Cuál campaña escalar y cuál pausar?

*   **¿Cuál ESCALAR? Campaña A (Landing principal).**
    *   **Justificación:** Es tu campaña más eficiente en términos de adquisición de clientes con **el CPA más bajo ($46.67)** y una tasa de conversión sólida del 3%. Atrae tráfico con alta intención comercial ("software gestion inventario"). Aunque la Campaña C tiene mejor CR (4%), su costo por adquisición es casi el doble ($88.89).
*   **¿Cuál PAUSAR o REESTRUCTURAR? Campaña B (Blog content).**
    *   **Justificación:** Es la peor convertidora. Aunque tiene un CPC muy barato ($0.38) y atrae muchos clics, su **tasa de conversión es paupérrima (0.50%)** y su **CPA es alto ($75.00)** debido a que lasKeywords son informativas ("cómo gestionar...") y los usuarios no tienen intención de compra inmediata. Te hace gastar presupuesto en curiosos, no en compradores. 
    *   *Nota sobre Campaña C:* Aunque tiene el CPA más alto ($88.89), el tráfico de competidores es estratégicamente valioso. No la pauses por completo, pero reduce su presupuesto porque está sobrepreciada.

---

### 3. Redistribución del presupuesto ($5,000/mes)

Eliminaremos el desperdicio de la Campaña B y apostaremos fuerte por la rentabilidad de la A, manteniendo una presencia táctica en la C.

*   **Campaña A (Escalar): 65% del presupuesto = $3,250**
    *   *Por qué:* Es la que trae los clientes al menor costo ($46.67). Al meterle más dinero, busca saturar las keywords principales sin perder eficiencia.
*   **Campaña C (Mantener/Optimizar): 25% del presupuesto = $1,250**
    *   *Por qué:* Robarle clientes al competidor funciona (36 signups), pero debes ajustar las pujas para bajar ese CPC de $3.56 y mejorar el CPA.
*   **Campaña B (Reducir drásticamente / Experimentar): 10% del presupuesto = $500**
    *   *Por qué:* No la mates del todo si quieres branding, pero pásala a remarketing o cambia las keywords a una etapa más cercana a la compra. (Si prefieres ir a la segura, pásale todo este 10% a la Campaña A).

---

### 4. Sugerencias de A/B Tests para el próximo mes

Dado que el tráfico llega pero en algunas campañas no convierte, propongo estos tests:

1.  **A/B Test en Landing Page (Para Campaña A y C):**
    *   **Variable:** El CTA (Call to Action) principal y el formulario.
    *   **Test A (Control):** Botón "Registrarse gratis" con formulario largo (Nombre, email, tamaño de empresa, teléfono).
    *   **Test B (Variante):** Botón "Probar software ahora" con formulario ultra corto (Solo email y contraseña). *Hipótesis: Reducir fricción aumentará el 3% de conversión.*
2.  **A/B Test de Anuncios (Para Campaña C - Competidores):**
    *   **Variable:** Ángulo de la propuesta de valor frente al competidor.
    *   **Test A:** Anuncio basado en **Precio** ("¿[Competidor] es muy caro? Nuestra alternativa es 30% más económica").
    *   **Test B:** Anuncio basado en **Funcionalidad/Facilidad** ("La alternativa a [Competidor] que no se cuelga y es más fácil de usar").
3.  **A/B Test de Intención (Para Campaña B - Blog):**
    *   Si vas a dejar un pequeño presupuesto para el blog, cambia la oferta.
    *   **Test A:** Enviar al artículo del blog y poner un banner lateral de "Prueba nuestro software".
    *   **Test B:** Ofrecer un *Lead Magnet* gratuito en ese artículo (Ej: "Descarga la plantilla de Excel para inventarios gratis a cambio de tu email") para luego nutrirlos por email, en vez de mandar tráfico frío directo al software.