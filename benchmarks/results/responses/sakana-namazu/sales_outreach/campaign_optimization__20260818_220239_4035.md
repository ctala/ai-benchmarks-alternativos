# Sakana Namazu — sales_outreach/campaign_optimization

- model_id: `sakana/sakana-namazu`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 35.718s | tokens_per_second: 163.3
- input_tokens: 359 | output_tokens: 5832

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

Aquí tienes el análisis completo de tus campañas.

---

### 1. Métricas calculadas

| Campaña | CTR | CPC | CPA | Conversion Rate |
|:---|:---|:---|:---|:---|
| **A (Landing Principal)** | **3.00%** | **$1.40** | **$46.67** | **3.00%** |
| **B (Blog Content)** | 4.00% | $0.375 | $75.00 | 0.50% |
| **C (Competidor)** | 6.00% | $3.56 | $88.89 | 4.00% |

**Observaciones clave:**
*   **A** es tu campaña más eficiente: menor CPA y buen volumen de conversiones (45).
*   **B** genera mucho tráfico barato ($0.37/click) pero con muy baja intención de conversión (0.5%).
*   **C** tiene el mejor CTR (6%) y un CVR alto (4%), pero el tráfico es muy caro ($3.56 CPC), inflando el CPA a $88.89.

---

### 2. ¿Cuál escalar y cuál pausar?

**✅ Escalar: Campaña A**
*   **Justificación:** Tiene el **CPA más bajo ($46.67)**, un 38% más barato que B y un 47% más barato que C. Además, ya demuestra que puede generar volumen (45 signups, el 42% del total). Su combinación de intención comercial directa ("software gestion inventario") + landing principal la hace altamente predecible y escalable.

**⏸️ Pausar (o reducir drásticamente): Campaña B**
*   **Justificación:** Aunque el CPC es bajísimo ($0.375), su **CVR es solo 0.5%**. Esto significa que necesitas **200 clics** para generar 1 signup, vs solo **33 clics** en la Campaña A. Para un presupuesto ajustado de $5,000/mes, no puedes permitirte mantener una campaña de *awareness* que consume el 25% del presupuesto ($1,800 de $7,100 actuales) para aportar solo el **23% de las conversiones** (24 de 105). Es tráfico de *top of funnel* que no está rentabilizándose en signups directos.

**⚠️ Nota sobre Campaña C:**
No la pauses aún, pero **optimízala**. Aunque su CPA es el más alto ($88.89), las keywords de competidor tienen alta intención de compra. El problema es el CPC ($3.56). Si mejoras la relevancia anuncio-keyword-landing, puedes bajar ese CPC y acercar el CPA a niveles aceptables.

---

### 3. Redistribución del presupuesto ($5,000/mes)

Actualmente estás gastando **$7,100/mes**, un 42% por encima de tu presupuesto. Para ajustarte a **$5,000** y maximizar signups:

| Campaña | Presupuesto Mes Próximo | % del Budget | Signups Estimados* |
|:---|:---|:---|:---|
| **A (Landing Principal)** | **$3,200** | 64% | ~68 |
| **C (Competidor)** | **$1,200** | 24% | ~13 |
| **B (Blog Content)** | **$600** | 12% | ~8 |
| **TOTAL** | **$5,000** | 100% | **~89** |

*\*Estimaciones basadas en CPA y CVR actuales. Asumen escala lineal.*

**Lógica:**
*   **A:** Incrementa presupuesto un ~52%. Es tu mejor motor de crecimiento.
*   **C:** Reduce un 62% ($3,200 → $1,200). Mantén las keywords más específicas (ej. "[competidor] vs" suele convertir mejor que "alternativa a [competidor]"). Pausa las keywords genéricas de esta campaña.
*   **B:** Reduce un 67% ($1,800 → $600). Usa este presupuesto mínimo exclusivamente para **testear** si puedes mejorar el CVR (ver tests abajo). Si no mejora, pausar completamente el mes siguiente.

**Comparativa de escenarios con $5,000:**
*   Si mantuvieras la proporción actual reducida a $5,000: generarías ~**74 signups**.
*   Con la redistribución propuesta: generarías ~**89 signups**.
*   **Diferencia: +20% más de conversiones** con el mismo presupuesto.

---

### 4. A/B Tests sugeridos para el próximo mes

#### **Campaña A (Prioridad Alta)**
1.  **Landing Page:** Testea tu landing actual vs. una versión con **comparativa visual** (tu software vs. Excel/manual) o una calculadora de ahorro de tiempo/dinero arriba del *fold*.
2.  **Copy de anuncios:** Actual (enfocado en características) vs. **"Gestión de inventario sin comisiones / Prueba gratis 14 días"** (enfocado en bajo riesgo y precio).
3.  **Formulario:** Landing con formulario largo vs. **campos mínimos** (solo email + contraseña) para reducir fricción.

#### **Campaña C (Prioridad Alta)**
1.  **Landing específica:** Testea enviar tráfico a tu home genérica vs. una landing de **"Migración gratis desde [Competidor]"** o una página de comparación lado a lado.
2.  **Extensiones de sitelink:** Agrega links directos a funcionalidades que el competidor no tiene (ej. "Soporte en español 24/7", "Sin límite de usuarios").
3.  **Keywords negativas:** Agrega términos como "gratis", "open source" o el nombre de planes gratuitos del competidor si tu producto es pago.

#### **Campaña B (Prioridad Media - Solo con $600 de test)**
1.  **Destino del clic:** En lugar de enviar al blog post, prueba enviar a un **lead magnet** (ej: "Template gratis para gestionar inventario en Excel" o "Guía: 5 errores de inventario en restaurantes") con captura de email *antes* de acceder al contenido.
2.  **Optimización de blog:** Si mantienes el blog, testea un **sticky banner** o **inline CTA** dentro del artículo ofreciendo la demo del software, no solo el contenido.
3.  **Remarketing:** Usa la lista de visitantes de esta campaña para hacer **remarketing** en Campaña A (configura en Google Ads una regla: "visitantes de URLs /blog/ que NO se hayan registrado").

#### **A nivel de cuenta**
*   **Estrategia de puja:** Si usas puja manual, testea **"Maximizar conversiones"** con un CPA objetivo de $50-$55 en Campaña A.
*   **Segmentación por dispositivo:** Revisa si los CPCs en mobile son más baratos en Campaña A; si es así, ajusta *bid modifiers* (+20% desktop si convierte mejor, -30% mobile si no).

---

**Resumen de la jugada:** Usa a Campaña A como tu caballo de batalla (64% del presupuesto), reduce C para proteger tu margen mientras optimizas el CPC, y convierte a B en un laboratorio de bajo presupuesto para ver si el tráfico de contenido puede convertir con otro tipo de oferta (lead magnet).