# Tencent Hy4 preview — sales_outreach/campaign_optimization

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 29.17s | tokens_per_second: 54.2
- input_tokens: 293 | output_tokens: 1581

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

Aquí tienes un análisis completo de tus campañas. Para evaluar correctamente el rendimiento, no solo hay que ver cuántos registros (signups) se consiguen, sino **a qué costo (CPA)** y con qué intención de compra.

Aquí están los cálculos y la estrategia recomendada:

### 1. Métricas por Campaña
*(Fórmulas: CTR = Clicks/Impresiones | CPC = Costo/Clicks | CVR = Signups/Clicks | CPA = Costo/Signups)*

**Campaña A (Landing Principal - Alta Intención)**
*   **CTR:** 3.0% (1,500 / 50,000)
*   **CPC:** $1.40 ($2,100 / 1,500)
*   **Tasa de Conversión (CVR):** 3.0% (45 / 1,500)
*   **CPA (Costo por Adquisición):** **$46.66** ($2,100 / 45)

**Campaña B (Blog Content - Descubrimiento)**
*   **CTR:** 4.0% (4,800 / 120,000)
*   **CPC:** $0.37 ($1,800 / 4,800)
*   **Tasa de Conversión (CVR):** 0.5% (24 / 4,800)
*   **CPA (Costo por Adquisición):** **$75.00** ($1,800 / 24)

**Campaña C (Competidor - Alta Intención)**
*   **CTR:** 6.0% (900 / 15,000)
*   **CPC:** $3.55 ($3,200 / 900)
*   **Tasa de Conversión (CVR):** 4.0% (36 / 900)
*   **CPA (Costo por Adquisición):** **$88.88** ($3,200 / 36)

---

### 2. ¿Cuál escalar y cuál pausar?

**⭐ ESCALAR: Campaña A (Landing Principal)**
*   **Justificación:** Es la clara ganadora. Tiene el **CPA más bajo ($46.66)** y una excelente tasa de conversión (3%). Las búsquedas ("software gestion inventario") indican que el usuario tiene una necesidad inmediata y busca una solución activamente. Aquí es donde debes poner la mayor parte de tu dinero.

**🛑 PAUSAR (o reducir drásticamente): Campaña C (Competidor)**
*   **Justificación:** Aunque tiene la mejor Tasa de Conversión (4%) y el mejor CTR (6%), tiene el **CPA más alto ($88.88)**. Te está costando casi el doble que la Campaña A para conseguir un registro. Esto se debe a un CPC muy elevado ($3.55) porque las palabras clave de competidores suelen ser subastas muy caras y agresivas.

**⚠️ MANTENER PERO OPTIMIZAR: Campaña B (Blog Content)**
*   **Justificación:** Su CPA es alto ($75), pero el tráfico es muy barato ($0.37 por clic) y el volumen de impresiones es gigante (120,000). No la pauses, pero cámbiale el objetivo. El problema es que el tráfico de "Blog" es de gente buscando aprender (top of funnel), no comprar.

---

### 3. Redistribución del Presupuesto ($5,000/mes)

El objetivo es maximizar el presupuesto en el CPA más barato (Campaña A) y experimentar con el volumen barato de la Campaña B.

Aquí tienes una propuesta de distribución mensual:

*   **$3,500 a Campaña A (70%):** Al tener el CPA más bajo, aquí es donde generarás el volumen real de negocio. Con $3,500 a un CPA de $46, deberías generar unos **75-80 signups**.
*   **$1,000 a Campaña B (20%):** Mantenemos una porción para seguir atrayendo tráfico de descubrimiento barato. El objetivo de este mes será intentar bajar su CPA mediante optimizaciones (ver sección 4).
*   **$500 a Campaña C (10%):** No la apagues del todo, pero ponla a "dieta". Limita el presupuesto diario. A veces, los usuarios que comparan competidores son los que tienen el LTV (Lifetime Value) más alto una vez que retienes. Usa estos $500 para quedarte solo con las palabras clave exactas que generaron los 36 signups y pausa el resto.

---

### 4. A/B Tests sugeridos para el próximo mes

Para mejorar estos números, no basta con mover el dinero, hay que probar cosas nuevas:

**Para la Campaña A (La que estás escalando):**
*   **Test de Landing Page:** Prueba una variante de la página de destino. Por ejemplo, cambia el título principal (H1) para que sea más directo o cambia el color del botón de registro (CTA). Mide si el CVR sube del 3% al 3.5%.
*   **Test de Concordancia (Match Types):** Asegúrate de usar "Concordancia de frase" y "Exacta". Si estás usando "Concordancia amplia", es probable que gastes dinero en búsquedas irrelevantes.

**Para la Campaña B (La que tiene tráfico barato pero no convierte):**
*   **Test de Oferta (Lead Magnet):** Los usuarios de blogs no quieren "registrarse" todavía. Cambia el CTA de "Regístrate gratis" a **"Descarga nuestra Guía de Inventario"** o "Calculadora de mermas en PDF". Captura su correo y luego nutrelo por email. Esto debería disparar el CVR del 0.5%.
*   **Test de Públicos (Remarketing):** Crea una audiencia en Google Ads con las 120,000 personas que vieron el blog y muestra un anuncio de la Campaña A solo a ellos. Es más probable que conviertan ahora que ya te conocen.

**Para la Campaña C (La de Competidores):**
*   **Test de Mensaje en el Anuncio:** Si el competidor es caro, tu anuncio debe resaltar el precio o la facilidad de uso. Prueba dos textos: uno enfocado en "Precio justo" y otro en "Mejor soporte técnico que [Competidor]".
*   **Test de Palabras Clave Negativas:** Revisa los términos de búsqueda. Es muy común que en campañas de competidores pagues por búsquedas de "soporte técnico de [competidor]" o "como cancelar [competidor]". Asegúrate de negativizar esas palabras para ahorrar presupuesto.