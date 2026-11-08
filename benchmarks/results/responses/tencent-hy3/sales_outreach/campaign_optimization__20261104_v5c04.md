# Tencent Hy3 — sales_outreach/campaign_optimization

- model_id: `tencent/hy3`
- success: True  | final: 7.54 | quality: 8.0
- latency_total: 23.676s | tokens_per_second: 55.4
- input_tokens: 301 | output_tokens: 1311

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

Aquí tienes el análisis completo de tu cuenta de Google Ads basado en los datos proporcionados.

### 1. Métricas de cada campaña (Último mes)

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **CTR** (Clics/Impr.) | 3.0% | 4.0% | 6.0% |
| **CPC** (Costo/Clic) | $1.40 | $0.375 | $3.55 |
| **Conv. Rate** (Signups/Clics) | 3.0% | 0.5% | 4.0% |
| **CPA** (Costo/Signup) | **$46.67** | **$75.00** | **$88.89** |

*Cálculos rápidos:*
*   *A:* 1500/50000=3% | 2100/1500=$1.4 | 45/1500=3% | 2100/45=$46.67
*   *B:* 4800/120000=4% | 1800/4800=$0.375 | 24/4800=0.5% | 1800/24=$75
*   *C:* 900/15000=6% | 3200/900=$3.55 | 36/900=4% | 3200/36=$88.89

---

### 2. ¿Qué escalar y qué pausar?

**ESCALAR: Campaña A (Landing Principal)**
*   **Justificación:** Tiene el **mejor CPA ($46.67)** y una tasa de conversión sólida (3%). Aunque el CPC es más alto que el Blog, la intención de compra es alta ("software gestion inventario"). Es la campaña más eficiente para conseguir usuarios.

**PAUSAR (o reducir drásticamente): Campaña C (Competidor)**
*   **Justificación:** Tiene el **peor CPA ($88.89)**, casi el doble que la Campaña A. Aunque el CTR (6%) y la tasa de conversión (4%) son buenos, el CPC es excesivamente caro ($3.55) porque probablemente peleas subastas directas con marcas grandes. Estás gastando $3,200 para traer solo 36 leads.

**OPTIMIZAR: Campaña B (Blog)**
*   No se pausa totalmente porque es muy barata (CPC $0.37), pero es ineficiente en conversión (0.5%). Sirve para awareness, pero necesita cambios en la página de destino.

---

### 3. Redistribución del presupuesto ($5,000)

Mi sugerencia es mover dinero de la campaña ineficiente (C) a la eficiente (A) y mantener un test pequeño en B.

*   **Campaña A (Landing Principal): $3,500** (Sube de $2,100).
    *   *Proyección:* A $46.67 CPA, generarías ~75 signups (un 66% más que ahora).
*   **Campaña B (Blog): $800** (Baja de $1,800).
    *   *Proyección:* Mantienes tráfico barato para retargeting, pero dejas de quemar presupuesto en leads caros.
*   **Campaña C (Competidor): $700** (Baja de $3,200).
    *   *Proyección:* Solo para cubrir la palabra exacta del competidor, no amplias la red.

**Total gastado:** $5,000.
**Signups proyectados estimados:** ~95-100 (vs los 105 actuales pero a un costo mucho más equilibrado y con potencial de crecer en A).

---

### 4. A/B Tests sugeridos para el próximo mes

1.  **Test de Landing Page (Campaña A):**
    *   *Variable:* Botón de CTA y prueba social.
    *   *Hipótesis:* Si cambiamos el botón "Registrarse" por "Empezar prueba gratis 14 días" y añadimos logos de clientes, subiremos el Conv. Rate del 3% al 4.5%.

2.  **Test de Intención (Campaña B - Blog):**
    *   *Problema:* El blog trae clicks pero no signups.
    *   *Test:* Compara una página de blog con un *pop-up* de descarga de eBook vs. una página de blog con un banner fijo al final que lleva directo a la Landing A.
    *   *Objetivo:* Mejorar ese 0.5% de conversión.

3.  **Test de Match Type (Campaña C):**
    *   *Problema:* El CPC es muy alto ($3.55).
    *   *Test:* Cambiar keywords de "Broad" o "Phrase" a **"Exact Match"** solo para la marca del competidor + "alternativa". Esto filtrará clics curiosos y bajará el CPC.

4.  **Test de Audiencia (Retargeting):**
    *   Usa los usuarios de la Campaña B (que leyeron el blog) para hacer una campaña de *Remarketing* con un mensaje directo de venta (usando los creativos de la Campaña A). Esto aprovecha el tráfico barato de B para convertirlo en C.