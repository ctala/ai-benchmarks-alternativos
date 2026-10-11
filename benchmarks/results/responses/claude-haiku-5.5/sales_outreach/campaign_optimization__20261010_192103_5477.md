# Claude Haiku 5.5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-haiku-5.5`
- success: True  | final: 8.91 | quality: 10.0
- latency_total: 17.128s | tokens_per_second: 202.9
- input_tokens: 395 | output_tokens: 3475

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

## 1. Métricas por campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** (Clicks / Impresiones) | 3.00% | 4.00% | 6.00% |
| **CPC** (Costo / Clicks) | $1.40 | $0.38 | $3.56 |
| **CPA** (Costo / Signups) | **$46.67** | $75.00 | $88.89 |
| **Conversion rate** (Signups / Clicks) | 3.00% | 0.50% | **4.00%** |

**Totales:** 185,000 impresiones, 7,200 clicks, 105 signups, CPA promedio de $67.62.

**Advertencia:** tu gasto total es de **$7,100**, pero tu presupuesto es de **$5,000**. Necesitas recortar al menos $2,100 o revisar si ese gasto excedió el presupuesto por algún motivo.

## 2. Qué escalar y qué pausar

**Escalar: Campaña A.** Tiene el CPA más bajo ($46.67), es un 30-50% más barato por signup que las otras dos y mantiene una conversion rate sólida (3%). Es la campaña más eficiente en dinero.

**Campaña C: mantener, pero controlar.** Tiene la mejor conversion rate (4%) y el CTR más alto, lo que indica intención de compra muy alta. Su problema es el CPC de $3.56. Es buena calidad de tráfico, pero cara. Conviene mantenerla con un tope de gasto y optimizarla para bajar el CPC.

**Campaña B: reestructurar antes de pausar.** Atrae mucho tráfico barato ($0.38 CPC), pero su conversion rate es de solo 0.5%, lo que significa que el problema está en el embudo y no en los anuncios. Probablemente los lectores buscan información y no están listos para registrarse. Antes de pausarla, revisa:
- Si la página del blog tiene un CTA claro hacia el registro.
- Si el tráfico incluye estudiantes o usuarios sin intención comercial (agrega negativos).
- En GA4, si la campaña aporta conversiones asistidas, que no se ven en el último clic.

Si en el próximo mes sigue por debajo de 1% de conversion, pausarla o reducirla drásticamente.

**Advertencia de muestra:** con 24 a 45 signups por campaña, las diferencias pueden tener margen de error considerable. Las conclusiones son direccionales, no definitivas.

## 3. Redistribución del presupuesto de $5,000

| Campaña | Actual | Propuesta | Razón |
|---|---|---|---|
| **A (Landing)** | $2,100 | **$2,300** | Mejor CPA. Escalar con cuidado, porque el CPA suele subir con más inversión. |
| **C (Competidor)** | $3,200 | **$1,700** | Alta calidad pero CPA alto. Reducir y optimizar CPC. |
| **B (Blog)** | $1,800 | **$1,000** | Presupuesto de prueba para mejorar la conversión, no para escalar. |
| **Total** | $7,100 | **$5,000** | |

**Resultado esperado** (asumiendo que los CPA se mantienen, lo cual es optimista):
- A: ~49 signups
- C: ~19 signups
- B: ~13 signups
- **Total: ~81 signups con CPA promedio de ~$62**

Obtendrás menos signups en total porque tienes menos presupuesto, pero el costo por signup mejora. Si mantienes $7,100, probablemente no cambies tu volumen de signups, solo lo pagas más caro.

## 4. A/B tests para el próximo mes

**Campaña A (Landing):**
- **Formulario:** versión corta (solo email) vs. versión actual con más campos. Mide conversión y calidad de los leads.
- **Titular de la landing:** enfocado en beneficio ("Controla tu inventario sin errores") vs. enfocado en funcionalidad.
- **Estrategia de puja:** Maximizar conversiones vs. CPA objetivo (~$45), una vez que tengas más datos.

**Campaña B (Blog):**
- **CTA dentro del artículo:** botón genérico de "Regístrate" vs. lead magnet específico (ej. "Plantilla gratuita de control de inventario para restaurantes").
- **Destino del clic:** artículo completo vs. artículo con banner de registro sticky.
- **Negativos:** agregar términos como "definición", "ejemplo", "gratis excel" para filtrar tráfico sin intención.

**Campaña C (Competidor):**
- **Página de destino:** página de comparación ("Tú vs. [competidor]") vs. landing general con oferta de prueba.
- **Copy del anuncio:** enfocado en precio/ahorro vs. enfocado en funcionalidades diferenciadoras.
- **Match type:** probar frase vs. exacta para reducir clics irrelevantes y bajar el CPC.

**Consejo de medición:** para significancia estadística necesitas aproximadamente 100 conversiones por variante. Con tus volúmenes actuales, cada test puede tomar varias semanas. Si es posible, usa un solo test por campaña a la vez para no contaminar los resultados.