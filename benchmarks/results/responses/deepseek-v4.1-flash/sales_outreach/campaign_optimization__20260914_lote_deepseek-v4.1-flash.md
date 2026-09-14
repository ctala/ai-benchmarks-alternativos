# DeepSeek V4.1 Flash — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 8.7 | quality: 10.0
- latency_total: 42.138s | tokens_per_second: 202.8
- input_tokens: 298 | output_tokens: 8544

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

Primero, ojo con un dato: los costos de las 3 campañas suman **$7,100**, no $5,000. Asumo que quieres reasignar **$5,000/mes** para el próximo mes.

## 1. Métricas por campaña

Fórmulas usadas:  
- CTR = Clicks / Impresiones  
- CPC = Costo / Clicks  
- CPA = Costo / Signups  
- Conversion Rate = Signups / Clicks  

| Campaña | Impresiones | Clicks | Signups | Costo | CTR | CPC | CPA | Conversion Rate |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A - Landing principal | 50,000 | 1,500 | 45 | $2,100 | **3.00%** | **$1.40** | **$46.67** | **3.00%** |
| B - Blog content | 120,000 | 4,800 | 24 | $1,800 | **4.00%** | **$0.38** | **$75.00** | **0.50%** |
| C - Competidor | 15,000 | 900 | 36 | $3,200 | **6.00%** | **$3.56** | **$88.89** | **4.00%** |

Totales: costo $7,100, signups 105, CPA global $67.62.

## 2. ¿Cuál escalar y cuál pausar?

### Escalar: Campaña A
- Tiene el **mejor CPA**: $46.67.
- Su conversion rate es sólido: **3.00%**.
- Aunque su CTR es menor que B y C, convierte bien y a un CPC razonable: $1.40.
- Es la campaña más eficiente para adquirir signups.

### Pausar como adquisición: Campaña B
- Tiene CTR alto: 4.00%.
- CPC muy bajo: $0.38.
- Pero su conversion rate es pésimo: **0.50%**.
- CPA: **$75.00**, más caro que A.
- Generó solo 24 signups con $1,800. A con $2,100 generó 45.
- B puede servir para contenido, remarketing o top-funnel, pero no como campaña principal de signups.

### Campaña C: no pausar necesariamente, pero no escalar todavía
- Tiene el mejor CTR: **6.00%**.
- Tiene el mejor conversion rate: **4.00%**.
- El problema es el CPC altísimo: **$3.56**.
- Eso hace que su CPA sea el peor: **$88.89**.
- Si el LTV/cliente justifica pagar más de $89 por signup, se puede mantener. Si no, hay que optimizarla o reducirla.

**Decisión resumida:** escalar A, pausar B como campaña de adquisición directa, y mantener C con presupuesto controlado para optimizar CPC/landing.

## 3. Redistribución de $5,000

Propuesta recomendada:

| Campaña | Presupuesto | % | Justificación |
|---|---:|---:|---|
| A - Landing principal | **$3,500** | 70% | Mejor CPA. Escalar gradualmente +67% vs mes pasado. |
| C - Competidor | **$1,500** | 30% | Mantener test de alta intención, pero limitar por CPA alto. |
| B - Blog content | **$0** | 0% | Pausar para adquisición. Solo reactivar para remarketing/nurture. |
| **Total** | **$5,000** | 100% |  |

Con CPA histórico, esto daría aproximadamente:
- A: $3,500 / $46.67 ≈ **75 signups**
- C: $1,500 / $88.89 ≈ **17 signups**
- Total estimado: **~92 signups**

Si A escala bien y mantiene CPA menor a $55, movería a:
- A: $4,000
- C: $1,000
- B: $0  
Estimado: **~97 signups**.

Si C logra bajar CPC de $3.56 a menos de $2.50 manteniendo 4% de conversion rate, su CPA bajaría a ~$62.50 y ahí sí subiría su presupuesto.

## 4. A/B tests sugeridos

### Campaña A
- Test de landing: “Prueba gratis” vs “Solicita demo”.
- Test de formulario: 3 campos vs 5 campos.
- Incluir calculadora de ROI vs video demo.
- Test de prueba social: testimonios, logos, casos de éxito.
- Separar keywords transaccionales vs más amplias:
  - “software gestion inventario”
  - “inventario pymes”
- Probar match exacto vs frase.

### Campaña B
- Si se mantiene, cambiar objetivo a engagement/remarketing, no signup directo.
- Test de lead magnet: plantilla Excel vs checklist vs guía.
- Contenido gated vs ungated.
- Exit-intent con oferta suave.
- Retargeting a quienes leyeron blog.

### Campaña C
- Landing comparativa: “[competidor] vs [nosotros]” con tabla de precios, features y migración.
- Test “alternativa a [competidor]” vs “[competidor] vs”.
- Oferta de migración gratis o onboarding asistido.
- Negativizar términos como: gratis, empleo, curso, salario, opiniones si no convierten.
- Probar pujas exactas vs frase y ajustes por dispositivo/horario.

### General
- Medir calidad de lead: signup, SQL, demo, activación y LTV por campaña.
- Probar tCPA vs maximizar conversiones.
- Escalar A en incrementos de 20-30% y vigilar CPA marginal.
- Revisar móvil vs desktop y ajustar pujas.
- Implementar negativos en B y C para evitar tráfico irrelevante.

En resumen: **A se escala, B se pausa como adquisición, C se mantiene limitada y optimizada.** Presupuesto sugerido: **A $3,500 / C $1,500 / B $0**.