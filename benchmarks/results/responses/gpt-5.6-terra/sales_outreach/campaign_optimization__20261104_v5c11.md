# GPT-5.6 Terra — sales_outreach/campaign_optimization

- model_id: `openai/gpt-5.6-terra`
- success: True  | final: 8.35 | quality: 10.0
- latency_total: 22.49s | tokens_per_second: 116.6
- input_tokens: 261 | output_tokens: 2622

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

| Campaña | CTR | CPC | Conversion Rate | CPA |
|---|---:|---:|---:|---:|
| **A: Landing principal** | 1,500 / 50,000 = **3.0%** | $2,100 / 1,500 = **$1.40** | 45 / 1,500 = **3.0%** | $2,100 / 45 = **$46.67** |
| **B: Blog content** | 4,800 / 120,000 = **4.0%** | $1,800 / 4,800 = **$0.38** | 24 / 4,800 = **0.5%** | $1,800 / 24 = **$75.00** |
| **C: Competidor** | 900 / 15,000 = **6.0%** | $3,200 / 900 = **$3.56** | 36 / 900 = **4.0%** | $3,200 / 36 = **$88.89** |

### Totales actuales

- **Inversión total:** $7,100
- **Signups totales:** 105
- **CPA medio:** $7,100 / 105 = **$67.62**
- **Conversion rate global:** 105 / 7,200 clics = **1.46%**

> Nota: actualmente estás gastando $7,100, pero tu presupuesto máximo es $5,000. Debes recortar $2,100 mensuales.

---

## 2. Qué campaña escalar y cuál pausar

### Escalar: Campaña A — Landing principal

Es claramente la campaña más eficiente para generar registros:

- **CPA más bajo:** $46.67
- **Conversion rate sólido:** 3.0%
- CPC razonable: $1.40
- Genera **45 signups**, el mayor volumen de las tres campañas.

Comparada con las demás:

- Es **38% más barata por signup** que B: $46.67 vs. $75.
- Es **48% más barata por signup** que C: $46.67 vs. $88.89.

**Conclusión:** A debe recibir la mayor parte del presupuesto incremental, siempre vigilando que su CPA no aumente al escalar.

---

### Reducir fuertemente o pausar: Campaña C — Competidor

Aunque C tiene excelentes métricas de intención:

- Mejor CTR: **6.0%**
- Mejor conversion rate: **4.0%**

su problema es económico:

- CPC muy alto: **$3.56**
- CPA más alto: **$88.89**
- Consume $3,200 para generar solo 36 signups.

La campaña C cuesta:

- **90% más por signup que A**.
- **19% más por signup que B**.

**Recomendación:** no necesariamente pausarla al 100% si esos leads tienen mejor calidad o mayor tasa de cierre. Las búsquedas de competidores suelen tener alta intención comercial. Sin embargo, sin evidencia de que esos registros cierren mucho mejor, debes **reducirla drásticamente** o pausarla temporalmente.

Para justificar mantener C, sus leads deberían tener un valor claramente superior. Por ejemplo, si el CPA de A es $46.67 y el de C es $88.89, un lead de C tendría que convertir a cliente aproximadamente:

\[
88.89 / 46.67 = 1.9x
\]

más que uno de A para justificar el costo.

---

### Mantener, pero optimizar: Campaña B — Blog content

B tiene tráfico barato y buen CTR:

- CTR: **4.0%**
- CPC: **$0.38**, el más bajo.

Pero el tráfico convierte muy mal:

- Conversion rate: **0.5%**
- CPA: **$75**

Esto indica una posible desalineación entre la intención de búsqueda y la oferta. Quienes buscan “cómo gestionar inventario” pueden estar en fase informativa, no necesariamente listos para registrarse.

**No la escalaría en su formato actual.** La mantendría con presupuesto limitado para:

1. Capturar demanda de awareness.
2. Construir audiencias de remarketing.
3. Probar landings y CTAs orientados al contenido educativo.
4. Separar términos informativos de búsquedas con intención comercial.

---

## 3. Redistribución del presupuesto de $5,000

### Distribución recomendada inicial

| Campaña | Presupuesto mensual | % del total | Motivo |
|---|---:|---:|---|
| **A: Landing principal** | **$3,200** | **64%** | Mejor CPA y buen volumen. Principal fuente de adquisición. |
| **B: Blog content** | **$1,200** | **24%** | Mantener para optimización y remarketing, sin escalar hasta elevar CVR. |
| **C: Competidor** | **$600** | **12%** | Mantener solo los términos/competidores más rentables para validar calidad. |
| **Total** | **$5,000** | **100%** | — |

### Proyección aproximada con el rendimiento actual

Si las métricas se mantuvieran al redistribuir presupuesto:

| Campaña | Presupuesto | CPA actual | Signups estimados |
|---|---:|---:|---:|
| A | $3,200 | $46.67 | ~69 |
| B | $1,200 | $75.00 | ~16 |
| C | $600 | $88.89 | ~7 |
| **Total** | **$5,000** | — | **~92 signups** |

CPA total estimado:

\[
\$5,000 / 92 \approx \$54.35
\]

Esto mejoraría tu CPA global desde **$67.62** a aproximadamente **$54.35**, una reducción cercana al **20%**.

### Alternativa más agresiva hacia eficiencia

Si C no demuestra leads de calidad claramente superior, podrías usar:

- A: **$3,600**
- B: **$1,400**
- C: **$0** o solo remarketing/search muy controlado

Proyección:

- A: ~$3,600 / $46.67 = **77 signups**
- B: ~$1,400 / $75 = **19 signups**
- Total: **~96 signups**
- CPA estimado: **~$52.08**

---

## 4. A/B tests recomendados para el próximo mes

## Campaña A: Landing principal

Objetivo: escalar sin deteriorar el CPA.

### Test 1: Propuesta de valor en el titular
Probar mensajes distintos según el principal dolor del usuario:

- Variante A: “Controla tu inventario en tiempo real.”
- Variante B: “Reduce pérdidas y quiebres de stock.”
- Variante C: “Software de inventario para pymes en minutos.”

Métrica principal: conversion rate de landing y CPA.

### Test 2: CTA
Comparar:

- “Crear cuenta gratis”
- “Probar gratis durante 14 días”
- “Solicitar una demo”
- “Ver cómo funciona”

Si el producto requiere más confianza o tiene ticket alto, “Solicitar demo” podría atraer menos registros, pero de mayor calidad.

### Test 3: Formulario corto vs. formulario largo
- Versión corta: email, nombre, empresa.
- Versión larga: añadir teléfono, tamaño de empresa, sector.

Mide no solo signups, sino también activación, asistencia a demo y cierre comercial. Un formulario corto puede aumentar volumen, pero reducir calidad.

### Test 4: Prueba social
Probar una landing con:

- Logos de clientes.
- Testimonios.
- Número de negocios usuarios.
- Casos de uso por industria.
- Calificaciones o reseñas.

---

## Campaña B: Blog content

Objetivo: mejorar el conversion rate desde 0.5% hacia al menos 1%–1.5%.

### Test 1: Landing educativa vs. landing de producto
El usuario de blog tiene intención informativa. En lugar de enviarlo directo a una página de signup, prueba:

- Variante A: landing de producto / registro directo.
- Variante B: guía descargable: “Plantilla gratuita para control de inventario”.
- Variante C: checklist o calculadora de pérdidas por mala gestión de stock.
- Variante D: artículo optimizado con CTA contextual hacia demo o prueba.

Después, nutre a los leads educativos por email y remarketing.

### Test 2: CTA contextual por keyword
No uses el mismo anuncio y landing para todas las consultas.

Ejemplos:

- Para “cómo gestionar inventario”:  
  CTA: “Descarga la guía para gestionar inventario”.
- Para “problemas inventario restaurante”:  
  CTA: “Evita faltantes y desperdicio en tu restaurante”.
- Para “inventario pymes”:  
  CTA: “Prueba un sistema de inventario para pymes”.

### Test 3: Añadir keywords de intención comercial
Crea grupos de anuncios separados para términos como:

- “software de inventario para pymes”
- “sistema de control de inventario”
- “programa para inventario”
- “app para control de stock”
- “software inventario restaurante”

Estas búsquedas deberían convertir mejor que las puramente educativas.

### Test 4: Negativas y segmentación de tráfico
Revisa términos de búsqueda y añade negativas para consultas informativas sin intención de compra, por ejemplo:

- “gratis” si no ofreces una versión gratuita real.
- “excel” si no quieres atraer personas buscando plantillas.
- “curso”, “definición”, “ejemplos”, “pdf”, “tarea”, etc.

Hazlo solo tras revisar datos reales de conversiones: algunas búsquedas “informativas” pueden alimentar un embudo rentable de remarketing.

---

## Campaña C: Competidor

Objetivo: bajar CPC y CPA, manteniendo solo tráfico con intención alta.

### Test 1: Separar keywords por competidor
No agrupes todos los competidores en una sola campaña o grupo.

Para cada competidor, mide:

- CTR
- CPC
- conversion rate
- CPA
- calidad del lead
- tasa de activación o cierre

Pausa competidores con CPA alto y baja calidad. Mantén los que generen oportunidades reales.

### Test 2: Mensaje de comparación
Prueba anuncios como:

- “Una alternativa simple a [Competidor]”
- “Compara [Tu marca] vs. [Competidor]”
- “Menor complejidad, mayor control de inventario”
- “Migración fácil desde [Competidor]”

Evita afirmaciones no verificables como “mejor” o “más barato” sin respaldo.

### Test 3: Landing específica de comparación
No envíes estas búsquedas a la landing general. Crea una página:

- “[Tu producto] vs. [Competidor]”
- Tabla de funcionalidades.
- Casos de uso.
- Proceso de migración.
- Prueba social.
- CTA claro a demo o prueba.

Esto debería mejorar el conversion rate actual de 4% y compensar parcialmente el CPC alto.

### Test 4: Concordancias y pujas
- Usa concordancia de frase y exacta para términos de competidor.
- Limita broad match si trae búsquedas irrelevantes.
- Reduce pujas en términos con CPA alto.
- Excluye búsquedas de soporte, login, empleo, precios no relevantes, tutoriales y descargas del competidor.

---

## Prioridades prácticas para el próximo mes

1. **Sube inversión en A** y monitorea el CPA semanalmente.
2. **Reduce C a un presupuesto de prueba**, salvo que ventas confirme que sus leads cierran mucho mejor.
3. **No escales B todavía**: primero trabaja el desajuste entre contenido informativo y signup.
4. Mide calidad post-signup: activación, demo agendada, oportunidad creada, cliente cerrado y CAC real.
5. Define un CPA objetivo basado en tu LTV, margen y tasa de cierre; sin ese dato, A es la ganadora por eficiencia de adquisición, pero no necesariamente por rentabilidad final.