# GPT-OSS 20B — sales_outreach/campaign_optimization

- model_id: `openai/gpt-oss-20b`
- success: True  | final: 7.69 | quality: 8.0
- latency_total: 24.672s | tokens_per_second: 94.8
- input_tokens: 322 | output_tokens: 2339

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

## 1. Métricas clave por campaña

| Campaña | Impresiones | Clicks | Signups | Costo (USD) | **CTR** | **CPC** | **CPA** | **CR (Conversion Rate)** |
|---------|-------------|--------|---------|--------------|--------|--------|--------|--------------------------|
| **A – Landing principal** | 50 000 | 1 500 | 45 | 2 100 | **3 %** | **$1,40** | **$46,67** | **3 %** |
| **B – Blog content** | 120 000 | 4 800 | 24 | 1 800 | **4 %** | **$0,38** | **$75,00** | **0,5 %** |
| **C – Competidor** | 15 000 | 900 | 36 | 3 200 | **6 %** | **$3,56** | **$88,89** | **4 %** |

> **Leyenda**  
> *CTR* = Clicks ÷ Impresiones  
> *CPC* = Costo ÷ Clicks  
> *CPA* = Costo ÷ Signups  
> *CR* = Signups ÷ Clicks  

---

## 2. ¿Qué escalar y qué pausar?  

| Campaña | Comentario | Decisión |
|---------|------------|----------|
| **A – Landing principal** | • CPA muy bajo ($46,67) – la adquisición más barata.<br>• CR de 3 % es sólido.<br>• CPC moderado, no consume demasiado presupuesto. | **Escalar** |
| **B – Blog content** | • CTR alto (4 %) y CPC bajo, pero CR apenas 0,5 % y CPA alto ($75).<br>• La mayor parte del gasto no convierte en sign‑ups.<br>• Ideal para awareness, pero no para generación directa de leads. | **Pausar / Reducir drásticamente** |
| **C – Competidor** | • Mejor CR (4 %) y CTR (6 %) que A, pero CPA muy alto ($88,89).<br>• El coste por clic es muy elevado (≈ $3,56).<br>• Si el cliente que llega es de mayor valor (ej. empresas vs pymes), podría justificar el coste, pero con el presupuesto limitado no es la opción más eficiente. | **Reducir** (mantener una fracción mínima) |

### Justificación numérica  
- **CPA**: A < B < C ⇒ A es la más rentable.  
- **CR**: C > A > B ⇒ C convierte mejor, pero a gran coste.  
- **CPC**: B < A < C ⇒ C es la más cara.  

Con un presupuesto de **$5 000** y un gasto actual de **$7 100**, la única forma de ajustarse es **eliminar la campaña B** (que ya no aporta valor en términos de CPA) y redistribuir su dinero a A y C.

---

## 3. Redistribución sugerida del presupuesto $5 000

| Campaña | Presupuesto sugerido (USD) | % del total | Comentario |
|---------|---------------------------|-------------|------------|
| **A – Landing principal** | **$3 200** | 64 % | Asegura más clics / leads con el CPA más bajo. |
| **C – Competidor** | **$1 200** | 24 % | Mantener una fracción para capturar los leads de mayor calidad (CR 4 %) sin sobrecargar el coste. |
| **B – Blog content** | **$600** | 12 % | Reducción drástica, solo para pruebas de alcance y generación de tráfico de interés. |
| **Total** | **$5 000** | 100 % | |

### Por qué esa distribución  
1. **Maximiza el número de sign‑ups** con el menor coste posible.  
2. **Conserva la audiencia de alta conversión** de la campaña C, pero limitando su gasto a un nivel que siga siendo rentable.  
3. **Permite seguir probando** el contenido del blog (B) sin comprometer el ROI global.

---

## 4. A/B tests recomendados para el próximo mes

| Área | Idea de test | Métrica objetivo |
|------|--------------|------------------|
| **Anuncios (copy & extensiones)** | • Variante 1: “Gestión de inventario sin complicaciones” vs Variante 2: “Control total de inventario en 3 pasos”<br>• Añadir extensiones de llamada y de sitio web. | CTR, CPC |
| **Landing page** (Campaña A) | • Variante 1: Video testimonial + CTA claro.<br>• Variante 2: Formulario simplificado (solo email) + botón “Más información”. | CR, duración de sesión |
| **Landing page** (Campaña C) | • Variante 1: Comparador visual vs Variante 2: Lista de ventajas con iconos.<br>• Añadir botón “Solicitar demo” en lugar de “Registrarse”. | CR, número de leads cualificados |
| **Landing page** (Campaña B) | • Variante 1: Blog + formulario de newsletter.<br>• Variante 2: Blog + contenido descargable (PDF) con CTA “Descargar”. | CR, conversiones a leads |
| **Segmentación** | • Test de audiencias: “Pymes” vs “Restaurantes” vs “Distribuidores”.<br>• Test de horarios: 08‑12 vs 13‑18 vs 19‑23. | CPA, ROAS |
| **Estrategia de puja** | • CPA objetivo (si el objetivo es generación de leads) vs Maximizar clics.<br>• Test de pujas automática vs manual. | CPA, presupuesto gastado |
| **Palabras clave** | • Añadir palabras clave de intención de compra “comprar software de inventario” vs “software de inventario demo”.<br>• Añadir exclusiones (palabras negativas). | CPC, CTR, CPA |

### Cómo medir el éxito  
- **CTR**: > 5 % en los anuncios A/B.  
- **CR**: > 4 % en las landing pages de A y C.  
- **CPA**: Reducir al menos un 10 % respecto a la campaña actual.  
- **ROAS**: Si se dispone de datos de ingresos, buscar > 3:1 en las campañas A y C.

---

### Resumen rápido

1. **Escala la Campaña A** (CPA más bajo).  
2. **Reduce drásticamente la Campaña B** (alto CPA, baja conversión).  
3. **Mantén una fracción de la Campaña C** (alta conversión, pero alto coste).  
4. Redistribuye el presupuesto a **$3 200 / $1 200 / $600** respectivamente.  
5. Ejecuta A/B tests en copy, landing pages, segmentación y pujas para seguir mejorando CTR, CR y CPA.

Con esta estrategia deberías maximizar el número de sign‑ups con el presupuesto disponible y, al mismo tiempo, mantener la capacidad de captar leads de mayor valor (Campaña C) sin comprometer la rentabilidad. ¡Éxito en el próximo mes!