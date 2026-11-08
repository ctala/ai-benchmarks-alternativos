# GPT-5.5 — sales_outreach/campaign_optimization

- model_id: `gpt-5.5`
- success: True  | final: 6.64 | quality: 8.0
- latency_total: 29.524s | tokens_per_second: 81.3
- input_tokens: 261 | output_tokens: 2400

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

## 1) Métricas por campaña

| Campaña | Impresiones | Clicks | Signups | Costo | CTR | CPC | Conversion Rate | CPA |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A - Landing principal** | 50,000 | 1,500 | 45 | $2,100 | **3.0%** | **$1.40** | **3.0%** | **$46.67** |
| **B - Blog content** | 120,000 | 4,800 | 24 | $1,800 | **4.0%** | **$0.38** | **0.5%** | **$75.00** |
| **C - Competidor** | 15,000 | 900 | 36 | $3,200 | **6.0%** | **$3.56** | **4.0%** | **$88.89** |

### Fórmulas usadas

- **CTR** = Clicks / Impresiones
- **CPC** = Costo / Clicks
- **Conversion Rate** = Signups / Clicks
- **CPA** = Costo / Signups

---

## 2) ¿Qué campaña escalar y cuál pausar?

### Campaña a escalar: **Campaña A - Landing principal**

Es la campaña con mejor eficiencia de adquisición.

- CPA más bajo: **$46.67**
- Conversion rate saludable: **3.0%**
- CPC razonable: **$1.40**
- Genera más signups que las otras: **45 signups**

Comparada con B y C:

- A es **38% más barata que B** en CPA:  
  $46.67 vs $75
- A es **48% más barata que C** en CPA:  
  $46.67 vs $88.89

Además, las keywords de A tienen intención comercial clara:

- “software gestion inventario”
- “inventario pymes”

Son búsquedas más cercanas a una decisión de compra o evaluación de solución.

---

### Campaña a pausar o reducir fuerte: **Campaña C - Competidor**

Aunque tiene el mejor CTR y conversion rate, es la más cara.

- CTR: **6.0%**, el mejor
- Conversion rate: **4.0%**, el mejor
- Pero CPA: **$88.89**, el peor
- CPC: **$3.56**, muy alto

Esto indica que el tráfico es relevante, pero demasiado costoso. Puede ser útil mantenerla si esos leads tienen mucho mayor calidad o mejor tasa de cierre en ventas, pero con los datos actuales de signups, no es eficiente.

No la pausaría completamente si hay capacidad de medir calidad de lead o pipeline, pero sí reduciría presupuesto significativamente.

---

### Campaña B: mantener, pero optimizar

B tiene un rol distinto. Genera muchísimo tráfico barato:

- CPC: **$0.38**, el más bajo
- CTR: **4.0%**, bueno
- Pero conversion rate muy bajo: **0.5%**
- CPA: **$75.00**

El problema no es atraer clicks, sino convertirlos. Las keywords son más informativas:

- “como gestionar inventario”
- “problemas inventario restaurante”

Estos usuarios probablemente están en una etapa más temprana del funnel. No necesariamente están listos para registrarse.

Recomendación: no pausarla del todo, pero usarla más como campaña de awareness/remarketing y optimizar la conversión.

---

## 3) Redistribución recomendada del presupuesto de $5,000/mes

Actualmente gastaste:

- A: $2,100
- B: $1,800
- C: $3,200
- Total: $7,100

Como el presupuesto futuro es **$5,000**, hay que priorizar eficiencia.

### Propuesta de redistribución

| Campaña | Presupuesto recomendado | % del total | Justificación |
|---|---:|---:|---|
| **A - Landing principal** | **$3,000** | **60%** | Mejor CPA y keywords con intención comercial |
| **B - Blog content** | **$1,250** | **25%** | Tráfico barato, útil para remarketing y nurturing |
| **C - Competidor** | **$750** | **15%** | Mantener presencia limitada, pero controlar CPA alto |
| **Total** | **$5,000** | **100%** |  |

---

### Estimación de signups si se mantienen los mismos CPA

| Campaña | Presupuesto | CPA actual | Signups estimados |
|---|---:|---:|---:|
| **A** | $3,000 | $46.67 | **64 signups** |
| **B** | $1,250 | $75.00 | **17 signups** |
| **C** | $750 | $88.89 | **8 signups** |
| **Total** | $5,000 | — | **89 signups aprox.** |

Con esta asignación, el CPA promedio esperado sería:

**$5,000 / 89 = $56.18 aprox.**

Es mejor que el CPA combinado actual:

- Gasto actual total: $7,100
- Signups totales: 105
- CPA actual promedio: **$67.62**

La redistribución baja el CPA promedio estimado de **$67.62 a $56.18**, una mejora aproximada del **17%**.

---

## 4) A/B tests sugeridos para el próximo mes

### Para Campaña A - Landing principal

Objetivo: escalar manteniendo CPA bajo.

#### Test 1: Landing page orientada a beneficio vs funcionalidad

**Variante A:**  
“Software de gestión de inventario para pymes”

**Variante B:**  
“Reduce quiebres de stock y errores de inventario en minutos”

Medir:

- Conversion rate
- CPA
- Tiempo en página
- Signups completados

---

#### Test 2: CTA directo vs CTA de bajo compromiso

**Variante A:**  
“Empieza gratis”

**Variante B:**  
“Ver demo gratuita”

Si el signup requiere fricción, “Ver demo” puede convertir mejor porque reduce la sensación de compromiso.

---

#### Test 3: Segmentación por industria

Crear landing específica para:

- Retail
- Restaurantes
- E-commerce
- Pymes generales

Ejemplo:

“Software de inventario para restaurantes: controla insumos, mermas y compras”

Esto puede aumentar relevancia y Quality Score.

---

### Para Campaña B - Blog content

Objetivo: mejorar conversión del tráfico informativo.

#### Test 4: Blog con CTA contextual vs CTA genérico

**Variante A:** CTA genérico al final:  
“Regístrate gratis”

**Variante B:** CTA contextual dentro del artículo:  
“Descarga la plantilla gratuita para controlar tu inventario”

La campaña B probablemente necesita una conversión intermedia, no solo un signup directo.

---

#### Test 5: Lead magnet vs signup directo

**Variante A:** Mandar tráfico al blog con CTA a signup

**Variante B:** Mandar tráfico a una landing de recurso:

- Plantilla de inventario en Excel
- Checklist para evitar quiebres de stock
- Guía para gestionar inventario en restaurantes
- Calculadora de costos de inventario

Luego hacer remarketing a quienes descargan el recurso.

---

#### Test 6: Remarketing para usuarios de blog

Crear audiencia de usuarios que llegaron por la campaña B y no convirtieron.

Anuncios de remarketing:

- “¿Aún gestionas inventario en Excel?”
- “Automatiza tu inventario y evita pérdidas”
- “Prueba gratis el software de inventario para pymes”

Esto puede convertir tráfico barato en signups posteriormente.

---

### Para Campaña C - Competidor

Objetivo: bajar CPC/CPA y mejorar eficiencia.

#### Test 7: Comparativa directa vs alternativa genérica

**Variante A:**  
“Alternativa a [competidor] para gestión de inventario”

**Variante B:**  
“Software de inventario más simple para pymes”

Cuidado con políticas de marca y uso de nombres de competidores en el copy. Las keywords pueden estar bien, pero el anuncio debe revisarse según normas de Google Ads y temas legales/marca.

---

#### Test 8: Landing de comparación

En vez de enviar a landing general, crear una página específica:

- “[Tu software] vs [competidor]”
- Tabla de funcionalidades
- Diferencias de precio
- Casos de uso
- Migración fácil
- Testimonios

Esta campaña tiene intención muy alta, pero CPC caro. Necesita una landing ultra relevante para justificar el gasto.

---

#### Test 9: Ajustar pujas por CPA objetivo

Como el CPA actual es **$88.89**, pondría un CPA objetivo inicial más bajo, por ejemplo:

- tCPA de **$65-$70**

Si no hay volumen, subir gradualmente. Si sigue sin funcionar, mantenerla en presupuesto bajo.

---

## Recomendaciones adicionales

### 1. Separar conversión primaria y secundaria

Para B, medir no solo signups, sino también:

- Descargas de recursos
- Scroll profundo
- Tiempo en página
- Clicks en CTA
- Visitas a páginas de pricing
- Usuarios añadidos a remarketing

Así no evalúas una campaña informativa solo con una conversión de cierre.

---

### 2. Revisar términos de búsqueda

Especialmente en B, agregar negativas como:

- gratis
- plantilla gratis, si no te interesa ese tráfico
- definición
- ejemplos académicos
- pdf
- curso
- empleo
- trabajo

Pero si usas lead magnets, algunas keywords tipo “plantilla” pueden ser útiles.

---

### 3. Optimizar por calidad del signup, no solo cantidad

Si tienes datos de CRM, revisa por campaña:

- % de signups que activan cuenta
- % que piden demo
- % que pasan a oportunidad
- % que pagan
- LTV estimado

Puede que C tenga CPA alto, pero si los leads cierran mucho mejor, podría justificar más presupuesto. Con los datos actuales, A gana claramente.

---

## Resumen ejecutivo

1. **Mejor campaña:** A  
   - CPA más bajo: **$46.67**
   - Buen conversion rate: **3.0%**

2. **Campaña a reducir o pausar:** C  
   - CPA más alto: **$88.89**
   - CPC muy caro: **$3.56**

3. **Campaña B:** mantener con menor presupuesto y optimizar funnel  
   - CPC bajo: **$0.38**
   - Pero baja conversión: **0.5%**

4. **Presupuesto recomendado:**
   - A: **$3,000**
   - B: **$1,250**
   - C: **$750**

5. **Prioridad del próximo mes:**
   - Escalar A
   - Convertir B con lead magnets y remarketing
   - Reducir C y probar landing específica de comparación