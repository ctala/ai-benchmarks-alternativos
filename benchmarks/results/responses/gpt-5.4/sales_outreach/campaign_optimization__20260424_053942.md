# GPT-5.4 — sales_outreach/campaign_optimization

- model_id: `gpt-5.4`
- success: True  | final: 7.37 | quality: 9.64
- latency_total: 31.776s | tokens_per_second: 64.5
- input_tokens: 261 | output_tokens: 2048
- judge_score: 4.8 | justificación: 

## Respuesta completa

Aquí va el análisis claro y accionable.

---

# 1) Cálculo de métricas por campaña

Fórmulas:
- **CTR** = Clicks / Impresiones
- **CPC** = Costo / Clicks
- **Conversion Rate (CVR)** = Signups / Clicks
- **CPA** = Costo / Signups

## Campaña A — Landing principal
- Impresiones: 50,000
- Clicks: 1,500
- Signups: 45
- Costo: $2,100

### Métricas
- **CTR** = 1,500 / 50,000 = **3.0%**
- **CPC** = 2,100 / 1,500 = **$1.40**
- **CVR** = 45 / 1,500 = **3.0%**
- **CPA** = 2,100 / 45 = **$46.67**

---

## Campaña B — Blog content
- Impresiones: 120,000
- Clicks: 4,800
- Signups: 24
- Costo: $1,800

### Métricas
- **CTR** = 4,800 / 120,000 = **4.0%**
- **CPC** = 1,800 / 4,800 = **$0.38**
- **CVR** = 24 / 4,800 = **0.5%**
- **CPA** = 1,800 / 24 = **$75.00**

---

## Campaña C — Competidor
- Impresiones: 15,000
- Clicks: 900
- Signups: 36
- Costo: $3,200

### Métricas
- **CTR** = 900 / 15,000 = **6.0%**
- **CPC** = 3,200 / 900 = **$3.56**
- **CVR** = 36 / 900 = **4.0%**
- **CPA** = 3,200 / 36 = **$88.89**

---

# Resumen comparativo

| Campaña | CTR | CPC | CVR | CPA |
|---|---:|---:|---:|---:|
| A | 3.0% | $1.40 | 3.0% | **$46.67** |
| B | 4.0% | **$0.38** | 0.5% | $75.00 |
| C | **6.0%** | $3.56 | **4.0%** | $88.89 |

---

# 2) ¿Qué campaña escalar y cuál pausar?

## Campaña a escalar: **Campaña A**
### Justificación numérica
Es la mejor combinación de:
- **CPA más bajo**: $46.67
- **CVR sólido**: 3.0%
- **CPC razonable**: $1.40

Aunque la campaña C convierte mejor en porcentaje (**4.0% CVR**), su **CPC es muy alto**, lo que dispara el CPA a **$88.89**.  
La campaña B tiene tráfico barato y buen CTR, pero convierte muy mal (**0.5% CVR**), así que trae volumen pero no resultados eficientes.

### Conclusión
Si tu objetivo es **maximizar signups dentro de un presupuesto fijo**, **A es la campaña que más eficientemente convierte gasto en registros**.

---

## Campaña a pausar o reducir fuertemente: **Campaña C**
### Justificación numérica
- CPA más alto: **$88.89**
- Costo total más alto: **$3,200**
- Solo generó 36 signups

Comparación directa:
- A logra 45 signups con $2,100
- C logra 36 signups con $3,200

Es decir:
- **A genera más signups gastando $1,100 menos**
- El CPA de C es **90% más caro** que A aproximadamente  
  \[
  (88.89 - 46.67) / 46.67 \approx 90.5\%
  \]

### Matiz importante
No necesariamente la pausaría al 100% si:
- esos leads de competidor tienen **mayor calidad**
- cierran mejor en ventas
- tienen mayor LTV

Pero con los datos que diste, **C no se justifica por performance pura de adquisición**.

---

## ¿Y la Campaña B?
No la pausaría del todo antes de testear, porque:
- tiene **CTR alto (4%)**
- tiene **CPC muy bajo ($0.38)**
- eso indica que el problema no es atraer clics, sino **la intención del tráfico o el paso post-clic**

B parece una campaña de **top-of-funnel**.  
No está funcionando bien para signups directos, pero podría mejorar mucho con cambios de:
- oferta
- landing
- CTA
- segmentación de keywords

### Recomendación para B
- **Reducir presupuesto**, no necesariamente pausar
- Mantenerla como laboratorio de pruebas o remarketing assist

---

# 3) ¿Cómo redistribuiría el presupuesto de $5,000?

Actualmente gastaste:
- A: $2,100
- B: $1,800
- C: $3,200  
Total: **$7,100**

Pero tu presupuesto real objetivo es **$5,000/mes**, así que hay que recortar y reasignar.

## Opción recomendada: priorizar eficiencia
### Distribución propuesta
- **Campaña A: $3,200**
- **Campaña B: $1,200**
- **Campaña C: $600**

Total = **$5,000**

---

## Por qué así

### A — $3,200
Es tu mejor CPA.  
Si mantiene eficiencia similar:

\[
3200 / 46.67 \approx 68.6
\]

Esperarías **~68-69 signups**

---

### B — $1,200
La mantienes viva para:
- capturar tráfico barato
- probar nuevas landings y ofertas
- alimentar remarketing

Si sigue igual:

\[
1200 / 75 = 16
\]

Esperarías **~16 signups**

Pero el objetivo aquí no es solo volumen actual, sino mejorar CVR.

---

### C — $600
La dejaría en modo controlado:
- solo keywords más rentables
- exact match
- términos de alta intención
- revisar si ciertos competidores convierten mejor que otros

Si sigue igual:

\[
600 / 88.89 \approx 6.7
\]

Esperarías **~6-7 signups**

---

## Proyección total con esta distribución
- A: ~69 signups
- B: ~16 signups
- C: ~7 signups

**Total estimado: ~92 signups**

---

## Comparación contra una distribución más agresiva
Si fueras totalmente performance-driven y no te importara explorar:

- **A: $4,000**
- **B: $800**
- **C: $200**

Proyección:
- A: 4000 / 46.67 = ~86 signups
- B: 800 / 75 = ~11 signups
- C: 200 / 88.89 = ~2 signups

Total: **~99 signups**

Esta opción maximiza registros esperados, pero reduce aprendizaje.

---

# 4) A/B tests sugeridos para el próximo mes

Te los ordeno por impacto potencial.

---

## A. Tests para Campaña A — escalar lo que ya funciona
Como es tu mejor campaña, aquí conviene optimizar conversión.

### 1. Test de landing principal
**Hipótesis:** subir CVR de 3.0% a 4.0% o más

Probar:
- Headline orientado a beneficio  
  - Variante A: “Software de gestión de inventario para pymes”
  - Variante B: “Reduce quiebres de stock y controla tu inventario en tiempo real”
- CTA:
  - “Prueba gratis”
  - “Solicita demo”
  - “Empieza hoy”
- Formulario:
  - corto vs largo
  - email solo vs email + teléfono + empresa

### 2. Test de intención comercial
Separar keywords en grupos:
- “software gestion inventario”
- “inventario pymes”

Y crear anuncios/landings específicos para cada grupo.  
Esto mejora:
- relevancia
- Quality Score
- CVR

### 3. Test de oferta
- Demo gratis
- Prueba de 14 días
- Auditoría/consultoría gratis
- “Setup gratis”

---

## B. Tests para Campaña B — arreglar el problema de conversión
Aquí está el mayor potencial oculto.

### Problema principal
CTR y CPC son buenos, pero el tráfico casi no convierte.  
Eso sugiere:
- keywords informacionales
- desalineación anuncio → contenido → CTA
- oferta demasiado “de venta” para tráfico frío

### 1. Test de CTA según intención
No mandar todo a signup directo.

Probar dos rutas:
- **Ruta 1:** artículo → lead magnet
- **Ruta 2:** artículo → demo/signup

Ejemplos de lead magnet:
- plantilla de inventario
- checklist de control de stock
- guía para restaurantes
- calculadora de pérdidas por quiebre de stock

###