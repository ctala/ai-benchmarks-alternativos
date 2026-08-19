# Qwen 3.8 2.4T (A95B) — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3.8-2.4t-a95b`
- success: True  | final: 8.14 | quality: 10.0
- latency_total: 89.991s | tokens_per_second: 174.5
- input_tokens: 351 | output_tokens: 15700

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



Antes de empezar: los costos que compartes suman **$7,100**, no $5,000. Asumiré que el dato histórico es válido para estimar rendimiento, pero que ahora quieres operar con **presupuesto mensual de $5,000**.

---

## 1) Métricas por campaña

Fórmulas:

- **CTR** = Clicks / Impresiones
- **CPC** = Costo / Clicks
- **Conversion rate / CVR** = Signups / Clicks
- **CPA** = Costo / Signups

| Campaña | Impresiones | Clicks | Signups | Costo | CTR | CPC | CVR | CPA |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| **A – Landing principal** | 50,000 | 1,500 | 45 | $2,100 | **3.00%** | **$1.40** | **3.00%** | **$46.67** |
| **B – Blog content** | 120,000 | 4,800 | 24 | $1,800 | **4.00%** | **$0.38** | **0.50%** | **$75.00** |
| **C – Competidor** | 15,000 | 900 | 36 | $3,200 | **6.00%** | **$3.56** | **4.00%** | **$88.89** |

Resumen rápido:

- **A** tiene el mejor CPA: **$46.67 por signup**.
- **B** trae clicks baratos, pero convierte mal: CVR de **0.50%**.
- **C** tiene el mejor CTR y mejor CVR, pero el CPC es muy alto: **$3.56**, lo que genera el peor CPA: **$88.89**.

También puedes verlo como signups por cada $100 gastados:

| Campaña | Signups por cada $100 |
|---|---:|
| A | **2.14 signups / $100** |
| B | 1.33 signups / $100 |
| C | 1.13 signups / $100 |

La campaña A es claramente la más eficiente para generar signups directos.

---

## 2) ¿Qué campaña escalar y cuál pausar?

### Recomendación principal

- **Escalar: Campaña A**
- **Pausar como campaña de conversión directa: Campaña B**
- **No escalar Campaña C; mantenerla solo como test controlado**

---

### Por qué escalar la Campaña A

La Campaña A tiene el mejor costo por signup:

- CPA A: **$46.67**
- CPA B: **$75.00**
- CPA C: **$88.89**

Comparado con A:

- B es **60.7% más cara** por signup.
- C es **90.5% más cara** por signup.

Además, A convierte bien tanto en click como en costo:

- CVR A: **3.00%**
- CPC A: **$1.40**
- CPA A: **$46.67**

Con $5,000, si A mantuviera su CPA actual, podría generar aproximadamente:

\[
5000 / 46.67 = 107 \text{ signups}
\]

Obviamente, esto asume que A puede escalar sin saturarse y sin subir demasiado el CPC.

---

### Por qué pausar o reestructurar la Campaña B

La Campaña B parece atractiva por CTR y CPC:

- CTR: **4.00%**
- CPC: **$0.38**

Pero el problema es la conversión:

- CVR: **0.50%**
- CPA: **$75.00**

Es decir, el tráfico es barato, pero no está convirtiendo en signups. Probablemente las keywords informativas como:

- “como gestionar inventario”
- “problemas inventario restaurante”

atraen usuarios en etapa temprana, no necesariamente listos para registrarse o comprar.

Mi recomendación: **pausarla como campaña de adquisición directa**. No la eliminaría definitivamente si puedes medir conversiones asistidas, remarketing o valor de contenido, pero con presupuesto limitado y objetivo de signups inmediatos, no debería llevarse una parte importante del presupuesto.

---

### Qué hacer con la Campaña C

La Campaña C tiene señales positivas:

- CTR: **6.00%**
- CVR: **4.00%**

Eso indica que el público tiene intención y la landing convierte relativamente bien. El problema es el costo:

- CPC: **$3.56**
- CPA: **$88.89**

Para que C sea competitiva, necesitaría bajar mucho el CPC o subir mucho el CVR.

Por ejemplo, si tu objetivo fuera un CPA de $50:

Con CVR actual de 4%, el CPC máximo debería ser:

\[
CPA objetivo \times CVR = 50 \times 0.04 = \$2.00
\]

Hoy el CPC es $3.56, así que tendría que bajar aproximadamente **44%**.

Por eso no la escalaría de inmediato. La dejaría solo con un presupuesto pequeño de prueba, enfocada en términos de competidor muy exactos y con una landing comparativa fuerte.

Si no logra bajar CPC a alrededor de **$2.00-$2.40** o subir CVR a **6%-7%**, entonces debería pausarse también.

---

## 3) Redistribución del presupuesto de $5,000

### Propuesta principal: maximizar signups con control

| Campaña | Presupuesto | % del presupuesto | Rol |
|---|---:|---:|---|
| **A – Landing principal** | **$4,000** | 80% | Escalar la campaña más eficiente |
| **C – Competidor** | **$1,000** | 20% | Test controlado de alta intención |
| **B – Blog** | **$0** | 0% | Pausada para conversión directa |

Total: **$5,000**

---

### Resultado estimado si se mantienen las métricas actuales

#### Campaña A con $4,000

- CPC estimado: $1.40
- Clicks estimados:

\[
4000 / 1.40 = 2,857
\]

- CVR: 3%
- Signups estimados:

\[
2,857 \times 0.03 = 85.7
\]

Aproximadamente: **86 signups**

#### Campaña C con $1,000

- CPC estimado: $3.56
- Clicks estimados:

\[
1000 / 3.56 = 281
\]

- CVR: 4%
- Signups estimados:

\[
281 \times 0.04 = 11.2
\]

Aproximadamente: **11 signups**

#### Total estimado

| Presupuesto | Signups estimados | CPA estimado |
|---:|---:|---:|
| $5,000 | **97 signups** | **$51.55** |

Esto sería mejor que mantener una mezcla menos eficiente, siempre que la Campaña A pueda absorber más presupuesto sin subir demasiado el CPC.

---

### Presupuesto alternativo si quieres mantener un test de blog

Si crees que el blog puede tener valor de largo plazo o conversiones asistidas, podrías usar una versión más experimental:

| Campaña | Presupuesto | Rol |
|---|---:|---|
| A | $3,500 | Escalar la principal |
| C | $1,000 | Test de competidor |
| B | $500 | Test de blog con landing/lead magnet |

Estimado con métricas actuales:

- A: $3,500 / $46.67 = **75 signups**
- C: $1,000 / $88.89 = **11 signups**
- B: $500 / $75.00 = **7 signups**

Total aproximado: **93 signups**

CPA promedio:

\[
5000 / 93 = \$53.76
\]

Es un poco menos eficiente, pero te deja aprender si el contenido puede funcionar mejor con una oferta distinta, por ejemplo:

- guía descargable
- plantilla de inventario
- checklist para restaurantes
- webinar
- demo guiada

---

## 4) A/B tests sugeridos para el próximo mes

Yo priorizaría 3-4 tests, no demasiados, porque con $5,000 de presupuesto necesitas suficiente volumen para aprender.

---

### Test 1: Landing de Campaña A — CTA y fricción del formulario

**Hipótesis:**  
Si reduces fricción o haces más claro el valor, puedes subir el CVR de 3% a 3.5%-4% sin aumentar CPC.

**Variantes posibles:**

- Variante A: formulario corto, solo email.
- Variante B: formulario con nombre, empresa y tamaño.
- Variante C: CTA “Prueba gratis” vs “Solicitar demo”.
- Variante D: “Empieza en 5 minutos” vs “Agenda una demo”.

**Métrica principal:**  
Conversion rate de signup.

**Métrica de control:**  
Calidad del signup, si luego tienes datos de activación o pago.

**Objetivo:**  
Bajar CPA de $46.67 a menos de $40 o mantener CPA estable mientras escalas.

Ejemplo: si mantienes CPC de $1.40:

- CVR 3.0% → CPA $46.67
- CVR 3.5% → CPA $40.00
- CVR 4.0% → CPA $35.00

Este es uno de los tests más rentables porque la Campaña A ya funciona bien.

---

### Test 2: Mensaje del anuncio en Campaña A

**Hipótesis:**  
Si el anuncio conecta mejor con la búsqueda, puedes mejorar CTR, Quality Score y CPC.

**Variantes posibles:**

- Anuncio actual vs anuncio con dolor específico:
  - “Evita quiebres de stock”
  - “Controla tu inventario en tiempo real”
  - “Software de inventario para pymes”
  - “Reduce pérdidas por inventario desactualizado”

**Métricas:**

- CTR
- CPC
- CVR
- CPA

**Objetivo:**  
Mantener o mejorar CTR de 3% y lograr CPC máximo de $1.50 con CPA objetivo de $50.

Para CPA objetivo de $50 con CVR de 3%:

\[
CPC máximo = 50 \times 0.03 = \$1.50
\]

Hoy estás en $1.40, así que hay poco margen. Si el CVR sube, el margen mejora.

---

### Test 3: Campaña C — Control de CPC y landing comparativa

**Hipótesis:**  
La campaña C tiene buena intención, pero el CPC es demasiado alto. Hay que mejorar eficiencia o pausar.

**Opciones de test:**

1. **Test de puja:**
   - Estrategia actual vs límite de CPC manual de $2.00-$2.40.

2. **Test de keywords:**
   - Broad/phrase vs exact match.
   - Solo términos de alta intención:
     - “[competidor] alternativa”
     - “[competidor] precios”
     - “[competidor] opiniones”
     - “cambiar de [competidor]”

3. **Test de landing:**
   - Landing genérica vs página de comparación directa.
   - Incluir tabla comparativa.
   - Incluir oferta de migración.
   - Incluir prueba gratis o demo.

**Métrica principal:**  
CPA.

**Métricas secundarias:**  
CPC, CTR, CVR.

**Objetivo mínimo:**  
Bajar CPA de $88.89 a menos de $60.

Para lograr CPA $60 con CVR de 4%:

\[
CPC máximo = 60 \times 0.04 = \$2.40
\]

Para lograr CPA $50:

\[
CPC máximo = 50 \times 0.04 = \$2.00
\]

Si no puedes bajar CPC a ese rango ni mejorar CVR, la campaña C no debería recibir más presupuesto.

---

### Test 4: Campaña B — Intención y oferta, solo si decides mantenerla

Si decides no pausarla del todo, yo no la dejaría enviando tráfico al blog sin más. El problema es que la intención parece informativa.

**Hipótesis:**  
El tráfico de blog puede convertir mejor si se envía a una oferta intermedia, no directamente a signup de software.

**Variantes:**

- Blog original vs landing de lead magnet.
- Oferta:
  - “Descarga la guía de gestión de inventario”
  - “Plantilla gratis de control de inventario”
  - “Checklist para inventario de restaurantes”
  - “Calculadora de costo de inventario”
- Luego, remarketing a esos leads con oferta de software.

**Métrica principal:**  
CVR de signup o lead calificado.

**Objetivo mínimo para que B sea razonable:**

Con CPC actual de $0.38, para lograr CPA de $50:

\[
CVR necesaria = CPC / CPA = 0.38 / 50 = 0.76\%
\]

Hoy B convierte a 0.50%, así que necesita mejorar CVR aproximadamente **50%-60%** para ser competitiva.

Si no llega a ese nivel, mejor pausarla o usarla solo para remarketing/awareness.

---

## Recomendación final práctica

Si tu objetivo es maximizar signups con $5,000 al mes, yo haría esto:

### Distribución inmediata

| Campaña | Presupuesto | Acción |
|---|---:|---|
| A | $4,000 | Escalar |
| C | $1,000 | Test con control de CPC |
| B | $0 | Pausar para conversión directa |

### Condiciones para mantener cada campaña

**Mantener/escalar A si:**

- CPA se mantiene cerca de $45-$50.
- CPC no sube demasiado al aumentar presupuesto.
- CVR se mantiene en 3% o más.

**Mantener C solo si:**

- CPC baja a $2.00-$2.40.
- CPA baja a menos de $60.
- CVR se mantiene en 4% o más.

**Reactivar B solo si:**

- Demuestra conversiones asistidas.
- Se envía a una landing de lead magnet.
- CVR sube a por lo menos 0.75%-0.80%.
- CPA baja a menos de $50-$60.

En resumen: **A es tu campaña para escalar, B debería pausarse como campaña de signups directos, y C debe mantenerse pequeña y optimizada hasta que demuestre que puede bajar su CPA.**