# DeepSeek V4 Pro (0813) — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v4-pro-0813`
- success: True  | final: 8.28 | quality: 10.0
- latency_total: 180.162s | tokens_per_second: 58.9
- input_tokens: 351 | output_tokens: 10608

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

Asumo que el objetivo principal es conseguir **signups/registros** con el presupuesto de **$5,000/mes**.

> ⚠️ Ojo: los costos que reportas suman **$7,100** ($2,100 + $1,800 + $3,200), no $5,000. Hay un exceso de **$2,100** respecto al presupuesto mensual.

---

## 1. Métricas por campaña

| Métrica | Campaña A: Landing principal | Campaña B: Blog content | Campaña C: Competidor |
|---|---:|---:|---:|
| Impresiones | 50,000 | 120,000 | 15,000 |
| Clics | 1,500 | 4,800 | 900 |
| CTR | **3.00%** | **4.00%** | **6.00%** |
| CPC | **$1.40** | **$0.38** | **$3.56** |
| Signups | 45 | 24 | 36 |
| Tasa de conversión | **3.00%** | **0.50%** | **4.00%** |
| CPA | **$46.67** | **$75.00** | **$88.89** |

### Totales actuales

- Inversión total: **$7,100**
- Clics totales: **7,200**
- Signups totales: **105**
- CTR promedio: **3.89%**
- CPC promedio: **$0.99**
- CPA promedio: **$67.62**
- Tasa de conversión promedio: **1.46%**

---

## 2. ¿Qué campaña escalar y cuál pausar?

### ✅ Escalar: Campaña A — Landing principal

Justificación con números:

- Tiene el **CPA más bajo**: **$46.67**.
- Su CPA es **31% mejor** que el CPA promedio actual de $67.62.
- Tiene buena tasa de conversión: **3.00%**.
- Generó **45 signups** con $2,100.
- Comparada con C: A gastó menos y generó más signups:
  - A: $2,100 → 45 signups.
  - C: $3,200 → 36 signups.
- Es la campaña más eficiente para conseguir registros.

### ❌ Pausar: Campaña B — Blog content

Justificación con números:

- Tasa de conversión muy baja: **0.50%**.
- CPA de **$75.00**, muy superior al de A.
- Generó solo **24 signups** con $1,800.
- Aunque su CPC es barato ($0.38) y su CTR aceptable (4%), el tráfico parece informativo y no está convirtiendo.
- Con $1,800 en B obtuviste 24 signups; con $2,100 en A obtuviste 45 signups. Es decir, A gastó solo $300 más, pero generó **87.5% más registros**.

### ⚠️ Campaña C — Competidor: no escalar todavía, optimizar

- Tiene el mejor CTR: **6.00%**.
- Tiene la mejor tasa de conversión: **4.00%**.
- Pero su CPC es muy alto: **$3.56**.
- Su CPA es el peor: **$88.89**.
- Tiene intención de compra competitiva interesante, pero actualmente es cara. Conviene mantenerla con menor presupuesto y optimizar antes de escalar.

---

## 3. Redistribución sugerida de $5,000/mes

Mi distribución inicial sería:

| Campaña | Presupuesto sugerido | Porcentaje | Acción |
|---|---:|---:|---|
| A — Landing principal | **$3,500** | 70% | Escalar gradualmente |
| B — Blog content | **$0** | 0% | Pausar o reestructurar |
| C — Competidor | **$1,500** | 30% | Mantener/reducir y optimizar |

### Proyección con CPA actual

- A: $3,500 / $46.67 ≈ **75 signups**
- C: $1,500 / $88.89 ≈ **17 signups**
- Total estimado: **92 signups**
- CPA promedio estimado: $5,000 / 92 ≈ **$54.35**

Comparado con el mes actual:

- Actual: 105 signups con $7,100 → CPA $67.62.
- Propuesta: 92 signups con $5,000 → CPA $54.35.

Esperas menos volumen total porque reduces inversión, pero mejoras bastante la eficiencia.

> Si la Campaña A no puede absorber $3,500 sin subir mucho el CPA por límites de búsqueda, sube gradualmente y destina el excedente a C o a remarketing.

---

## 4. A/B tests sugeridos para el próximo mes

### Para Campaña A — Landing principal

1. **Headline principal**:  
   - “Controla tu inventario en tiempo real”  
   - vs. “Deja de perder ventas por quiebre de stock”.

2. **CTA**:  
   - “Prueba gratis 14 días”  
   - vs. “Agendar demo”.

3. **Formulario de signup**:  
   - Formulario corto: solo email.  
   - vs. Formulario con email + empresa + teléfono.

4. **Prueba social**:  
   - Testimonios arriba del CTA.  
   - vs. Testimonios abajo del CTA.

5. **Visual**:  
   - Screenshot del software.  
   - vs. Video corto explicativo.

### Para Campaña C — Competidor

1. **Landing específica**:  
   - Página “Nosotros vs [Competidor]”.  
   - vs. Página genérica de “Alternativa a [Competidor]”.

2. **Headline**:  
   - “La alternativa #1 a [Competidor]”.  
   - vs. “Migrar de [Competidor] a nosotros es fácil”.

3. **Oferta para migrar**:  
   - “Importación de datos gratis”.  
   - vs. “Descuento por cambio desde [Competidor]”.

4. **Prueba social**:  
   - Logos de clientes migrados.  
   - vs. Video testimonial de migración.

### Para Campaña B — Blog content, si decides no pausarla

1. **CTA del blog**:  
   - “Descargar guía práctica”.  
   - vs. “Probar software gratis”.

2. **Ubicación del CTA**:  
   - CTA inline al final del artículo.  
   - vs. Pop-up o banner lateral.

3. **Landing de destino**:  
   - Artículo/blog.  
   - vs. Landing page del software.

4. **Tipo de contenido**:  
   - Lead magnet descargable.  
   - vs. Acceso directo a demo.

---

### Recomendación final resumida

- **Escalar A** gradualmente: es la más rentable.  
- **Pausar B**: tráfico barato pero no convierte.  
- **No escalar C todavía**: buena intención, pero CPA muy alto.  
- **Redistribuir $5,000** priorizando A y dejando C con presupuesto controlado.  
- **Hacer A/B tests** enfocados en mejorar conversión y reducir CPA.