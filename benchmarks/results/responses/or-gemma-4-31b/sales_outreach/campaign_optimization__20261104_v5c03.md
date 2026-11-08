# Gemma 4 31B — sales_outreach/campaign_optimization

- model_id: `google/gemma-4-31b-it`
- success: True  | final: 9.28 | quality: 10.0
- latency_total: 9.198s | tokens_per_second: 114.7
- input_tokens: 304 | output_tokens: 1055

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

Aquí tienes el análisis detallado de tus campañas. Primero, desglosamos las métricas clave para poder tomar decisiones basadas en datos.

### 1. Cálculo de Métricas

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
| :--- | :--- | :--- | :--- |
| **CTR** (Clicks/Impr) | **3.0%** | **4.0%** | **6.0%** |
| **CPC** (Costo/Clicks) | **$1.40** | **$0.37** | **$3.55** |
| **Conv. Rate** (Signups/Clicks) | **3.0%** | **0.5%** | **4.0%** |
| **CPA** (Costo/Signups) | **$46.67** | **$75.00** | **$88.89** |

---

### 2. Análisis: ¿Cuál escalar y cuál pausar?

**Campaña a ESCALAR: Campaña A (Landing Principal)**
Es tu campaña más eficiente. Aunque no tiene el CTR más alto ni el CPC más bajo, tiene el **CPA más bajo ($46.67)**. Esto significa que es la forma más barata de adquirir un usuario registrado. Además, tiene un Conversion Rate saludable (3%), lo que indica que la intención de búsqueda coincide perfectamente con la oferta.

**Campaña a PAUSAR (o pivotar): Campaña B (Blog Content)**
Es la campaña con peor rendimiento en términos de conversión. Aunque atrae mucho tráfico barato (CPC $0.37) y tiene buen CTR, el **Conversion Rate es bajísimo (0.5%)** y el **CPA es muy alto ($75.00)**. Estás pagando por tráfico informativo ("cómo hacer..."), pero esos usuarios no están listos para registrarse en un software; están buscando aprender, no comprar.

**Campaña a OPTIMIZAR/MANTENER: Campaña C (Competidor)**
Es la más cara en términos de CPC ($3.55) y CPA ($88.89). Sin embargo, tiene el **Conversion Rate más alto (4%)**. Esto indica que el tráfico es de altísima calidad (personas que ya usan un software y buscan cambiar). No la pausaría del todo porque es tráfico "caliente", pero no le daría la prioridad de presupuesto a la A.

---

### 3. Redistribución del Presupuesto ($5,000)

El objetivo es maximizar el número de *Signups* totales bajando el CPA promedio.

*   **Campaña A (60% - $3,000):** Al ser la más rentable, es donde cada dólar extra rinde más. Aumentamos el presupuesto para capturar más volumen de palabras clave transaccionales.
*   **Campaña C (30% - $1,500):** Mantenemos una presencia fuerte frente a la competencia, pero reducimos el gasto para evitar que el CPA tan alto drene el presupuesto.
*   **Campaña B (10% - $500):** No la elimino totalmente, pero la reduzco al mínimo. La usaría solo para captar leads mediante un "Lead Magnet" (ej. una plantilla de Excel gratuita) en lugar de intentar que se registren directamente al software.

**Resultado esperado:** Al mover dinero de la B $\rightarrow$ A, el número total de signups aumentará significativamente sin gastar más dinero.

---

### 4. Sugerencias de A/B Tests para el próximo mes

Para seguir bajando el CPA, sugiero estos experimentos:

**Para la Campaña A (Landing Principal):**
*   **Test de Oferta:** Probar "Prueba gratis 14 días" vs "Demo personalizada con un experto".
*   **Test de Formulario:** Reducir el número de campos del registro (ej. solo Email y Nombre) para ver si el Conversion Rate sube del 3%.

**Para la Campaña C (Competidor):**
*   **Test de Copy de Anuncio:** Probar un ángulo de "Ahorro de costos" (ej: "Más funciones que [Competidor] por mitad de precio") vs un ángulo de "Facilidad de uso" (ej: "Cámbiate a [Tu Software], migración en 1 click").

**Para la Campaña B (Blog):**
*   **Test de Conversión:** En lugar de enviar al usuario a la Landing de registro, crear una página de aterrizaje intermedia con un recurso gratuito (Ebook/Plantilla) a cambio del email. Luego, intentar convertir esos leads vía Email Marketing (nutrición).