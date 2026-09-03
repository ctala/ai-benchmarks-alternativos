# Tencent Hy4 preview — sales_outreach/campaign_optimization

- model_id: `tencent/hy4-preview`
- success: True  | final: 8.39 | quality: 10.0
- latency_total: 70.586s | tokens_per_second: 66.6
- input_tokens: 290 | output_tokens: 4700

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

¡Excelente! Tienes un muy buen conjunto de datos para analizar. Antes de empezar, hay un **dato clave**: el gasto total del mes pasado fue de **$7,100** ($2,100 + $1,800 + $3,200), lo cual significa que te excediste de tu presupuesto de $5,000 por $2,100. Esto hace que la optimización sea urgente.

Aquí tienes el análisis completo y el plan de acción:

### 1. Cálculo de Métricas

Aquí están las métricas clave redondeadas a dos decimales para cada campaña:

**Campaña A (Landing principal - Alta intención)**
*   **CTR:** (1,500 / 50,000) * 100 = **3.00%**
*   **CPC:** $2,100 / 1,500 = **$1.40**
*   **CPA (Costo por Registro):** $2,100 / 45 = **$46.67**
*   **CVR (Tasa de Conversión):** (45 / 1,500) * 100 = **3.00%**

**Campaña B (Blog content - Intención informativa)**
*   **CTR:** (4,800 / 120,000) * 100 = **4.00%**
*   **CPC:** $1,800 / 4,800 = **$0.38**
*   **CPA (Costo por Registro):** $1,800 / 24 = **$75.00**
*   **CVR (Tasa de Conversión):** (24 / 4,800) * 100 = **0.50%**

**Campaña C (Competidor - Altísima intención)**
*   **CTR:** (900 / 15,000) * 100 = **6.00%**
*   **CPC:** $3,200 / 900 = **$3.56**
*   **CPA (Costo por Registro):** $3,200 / 36 = **$88.89**
*   **CVR (Tasa de Conversión):** (36 / 900) * 100 = **4.00%**

---

### 2. ¿Cuál escalar y cuál pausar? (Justificación)

*   **🚀 ESCALAR: Campaña A**
    *   *Justificación:* Es tu campaña más eficiente. Tiene el **CPA más bajo ($46.67)** y una tasa de conversión sólida (3%). Las keywords ("software gestion inventario") indican que el usuario tiene intención de compra directa. Es donde tu dinero rinde más.
*   **⏸️ PAUSAR (o limitar drásticamente): Campaña B**
    *   *Justificación:* Es una trampa de "tráfico barato". Aunque tiene el CPC más bajo ($0.38) y muy buen CTR (4%), su **Tasa de Conversión es pésima (0.50%)**. Esto dispara tu CPA a $75. Estás pagando por mucho tráfico de curiosos (top-of-funnel) que lee el blog pero no se registra.
*   **⚠️ OPTIMIZAR Y MANTENER (con menos presupuesto): Campaña C**
    *   *Justificación:* No la pausaría porque tiene el **mejor CTR (6%) y la mejor Tasa de Conversión (4%)**. El tráfico es oro puro (gente comparando activamente para cambiarse de software). Sin embargo, el **CPC es altísimo ($3.56)**, lo que hace que el CPA sea el más caro ($88.89). Hay que mantenerla pero trabajar para abaratar el clic.

---

### 3. Redistribución del Presupuesto ($5,000)

Como el mes pasado gastaste $7,100, vamos a recortar $2,100 para ajustarnos a tu límite mensual, priorizando la eficiencia:

*   **Campaña A: $3,000** *(Aumento desde $2,100)*
    Al ser la más rentable, se lleva el 60% del presupuesto. Al escalarla, el CPA podría subir un poco, pero seguirá siendo tu mejor canal de adquisición.
*   **Campaña C: $1,500** *(Reducción drástica desde $3,200)*
    Recortamos a la mitad para dejar de pagar clics tan caros. Al bajar el presupuesto, Google se verá obligado a mostrar tus anuncios a los usuarios más propensos a convertir para no gastar el dinero tan rápido, lo que debería ayudar a optimizar el CPC.
*   **Campaña B: $500** *(Reducción desde $1,800)*
    Le dejamos un presupuesto mínimo. Su CPC es tan barato ($0.38) que por $500 puedes generar mucho tráfico para hacer remarketing en el futuro o para mantener la marca presente, pero no podemos permitirnos gastar $1,800 para conseguir solo 24 registros. *(Si prefieres ser ultra agresivo con el ROI, puedes pausarla a $0 y pasar esos $500 a la Campaña A).*

---

### 4. Tests A/B sugeridos para el próximo mes

Para el próximo mes, te sugiero implementar estos tests para mejorar los números de las campañas que mantenemos activas:

1.  **Campaña A (Test en Landing Page):** Dado que el tráfico es bueno (CVR 3%), el problema puede estar en tu página. Prueba a **acortar el formulario de registro** (pide menos datos) o cambia el botón principal de acción (ej. prueba "Empezar Prueba Gratis" vs "Agendar una Demo").
2.  **Campaña C (Test en Anuncios / Palabras clave):** El CPC de $3.56 es muy alto. Crea variaciones de anuncios enfocadas en el "dolor" que tienen los clientes del competidor para mejorar tu Nivel de Calidad (Quality Score) en Google, lo que te ayudará a pagar menos por clic. Además, prueba a cambiar las keywords a "concordancia de frase" para encontrar búsquedas relacionadas más baratas.
3.  **Campaña B (Test de Oferta / CTA):** Dado que la gente que llega aquí está en modo "aprendizaje" (buscan "cómo gestionar..."), no les pidas un "Signup" directo. Prueba a añadir un formulario emergente (popup) que diga: *"Descarga nuestra Guía Definitiva de Inventarios en PDF"*. Así capturas su correo (lead) de forma más barata y luego los nutres por email.
4.  **Estrategia de Puja (Campaña A):** Si tienes suficiente historial de conversiones, prueba a cambiar la estrategia de puja de "Maximizar Clics" o "Manual" a **"CPA Objetivo (tCPA)"**. Ponle un objetivo de $50 y deja que el algoritmo de Google encuentre a los usuarios más baratos.