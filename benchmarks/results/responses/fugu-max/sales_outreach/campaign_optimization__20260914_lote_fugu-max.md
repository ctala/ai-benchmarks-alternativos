# Fugu Max — sales_outreach/campaign_optimization

- model_id: `sakana/fugu-max`
- success: True  | final: 8.11 | quality: 10.0
- latency_total: 125.674s | tokens_per_second: 65.6
- input_tokens: 426 | output_tokens: 8250

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

## 1. Métricas calculadas

Usé estas fórmulas:  
- **CTR** = Clicks / Impresiones  
- **CPC** = Costo / Clicks  
- **CPA** = Costo / Signups  
- **Tasa de conversión** = Signups / Clicks  

| Campaña | CTR | CPC | CPA | Tasa de conversión |
|---|---:|---:|---:|---:|
| **A. Landing principal** | 3.00% | $1.40 | $46.67 | 3.00% |
| **B. Blog content** | 4.00% | $0.38 | $75.00 | 0.50% |
| **C. Competidor** | 6.00% | $3.56 | $88.89 | 4.00% |

Nota: actualmente la inversión total suma **$7,100**, aunque tu presupuesto objetivo es **$5,000**. Estás $2,100 por encima.

---

## 2. ¿Cuál escalar y cuál pausar?

### ✅ Escalar: Campaña A — Landing principal

Justificación numérica:

- Tiene el **mejor CPA: $46.67** por signup.
- Convierte al **3%**, es decir, 3 de cada 100 clicks se registran.
- Es **60.7% más barata por signup** que la Campaña B:  
  $75.00 vs $46.67
- Es **90.5% más barata por signup** que la Campaña C:  
  $88.89 vs $46.67

Aunque su CTR no es el más alto, su combinación de CPC moderado, conversión decente y CPA bajo la hace la más eficiente para conseguir signups.

### ❌ Pausar: Campaña B — Blog content

Justificación numérica:

- CPC muy barato: **$0.38**, pero convierte muy mal: **0.5%**.
- Solo generó **24 signups** con 4,800 clicks.
- CPA alto: **$75.00**, mucho peor que la Campaña A.
- Tiene CTR de 4%, pero el tráfico no se está convirtiendo en registros.

Para objetivo directo de signups, **la Campaña B no se justifica con estos números**.

### ⚠️ Campaña C — Competidor: no escalar todavía

- Tiene el mejor CTR: **6%**.
- Tiene la mejor tasa de conversión: **4%**.
- Pero su CPC es muy alto: **$3.56**, lo que dispara el CPA a **$88.89**.

No la pausaría de inmediato porque captura tráfico de alta intención desde búsquedas de competidores, pero no la escalaría hasta bajar su CPC o mejorar su CPA. Hoy es casi el doble de cara que la Campaña A por cada signup.

---

## 3. Redistribución de presupuesto de $5,000

Propuesta base:

| Campaña | Presupuesto actual | Nuevo presupuesto | % del total | Proyección de signups |
|---|---:|---:|---:|---:|
| **A. Landing principal** | $2,100 | $3,500 | 70% | ~75 |
| **C. Competidor** | $3,200 | $1,500 | 30% | ~17 |
| **B. Blog content** | $1,800 | $0 | 0% | 0 |
| **Total** | $7,100 | $5,000 | 100% | ~92 |

Con esta redistribución proyectamos:

- **~92 signups** mensuales.
- CPA promedio estimado: **$5,000 / 92 ≈ $54.42**.

Eso mejora el CPA global actual, que hoy es:  
$7,100 / 105 signups = **$67.62**.

### Ajuste alternativo más eficiente

Si la Campaña A puede absorber más presupuesto sin perder eficiencia, usaría:

- **A:** $4,000
- **C:** $1,000
- **B:** $0

Esto proyectaría unos **97 signups** y un CPA promedio de **$51.57**, asumiendo que el CPA de A se mantiene estable.

La clave es monitorear que al escalar A no empiece a subir mucho su CPA. Si el CPA de A sube por encima de ~$50–55, hay que frenar el escalado o ajustar anuncios, keywords y landing.

---

## 4. A/B tests sugeridos para el próximo mes

### 1. Landing principal — Campaña A

Test A/B:

- Versión actual.
- Versión con prueba gratis o demo más visible, logos de clientes, beneficios arriba y CTA arriba.

Métrica principal: **signups y CPA**.

Objetivo: mejorar el 3% de conversión actual.

### 2. Copys de anuncios — Campaña A

Probar:

- Anuncio orientado a dolor:  
  *“Controla tu inventario en tiempo real”*
- Anuncio orientado a beneficio:  
  *“Reduce quiebres de stock y ahorra horas”*
- Anuncio con prueba gratuita:  
  *“Prueba gratis 14 días, sin tarjeta”*

Métrica: **CTR y tasa de conversión**.

### 3. Keywords y concordancia — Campaña A

Probar:

- Concordancia exacta en *“software gestión inventario”* e *“inventario pymes”*.
- Revisar términos de búsqueda y agregar negativas para eliminar clics baratos pero irrelevantes.

Métrica: **CPC, CPA y tasa de conversión**.

### 4. Campaña C — Competidor

Probar:

- Landing de comparación:  
  *“[Competidor] vs nosotros”* con tabla comparativa.
- Landing principal normal.

Métrica: **signups y CPA**.

También probar ads:

- *“Alternativa a [competidor]”*
- *“Migra desde [competidor]”*
- *“Clientes que eligieron cambiarse”*

Esto puede ayudar a bajar CPC o mejorar conversión.

### 5. Campaña B — si decides no pausarla del todo

Si quieres mantener contenido/awareness, probaría:

- CTA a un lead magnet: *“Descarga plantilla de inventario”*
- CTA directo a signup.

Métrica: **conversión a lead/email**.

Pero con presupuesto limitado y foco en signups, yo pausaría B.

---

### Recomendación final corta

- **Escalar A**: mejor CPA y buena conversión.
- **Pausar B**: tráfico barato pero no convierte en signups.
- **Mantener C controlada**: alta intención, pero cara; optimizar antes de escalar.
- **Redistribuir $5,000**: 70% A, 30% C, 0% B como base.

Así maximizas signups y mejoras el CPA global.