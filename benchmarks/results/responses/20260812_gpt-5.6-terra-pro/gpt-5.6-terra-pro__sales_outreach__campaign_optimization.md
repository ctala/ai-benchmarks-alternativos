# GPT-5.6 Terra Pro — sales_outreach/campaign_optimization

- model_id: `openai/gpt-5.6-terra-pro`
- success: True  | final: 8.19 | quality: 10.0
- latency_total: 41.885s | tokens_per_second: 233.2
- input_tokens: 12003 | output_tokens: 9767

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

| Campaña | CTR | CPC | Conversion rate (signup/click) | CPA |
|---|---:|---:|---:|---:|
| **A – Landing principal** | 1,500 / 50,000 = **3.0%** | $2,100 / 1,500 = **$1.40** | 45 / 1,500 = **3.0%** | $2,100 / 45 = **$46.67** |
| **B – Blog content** | 4,800 / 120,000 = **4.0%** | $1,800 / 4,800 = **$0.38** | 24 / 4,800 = **0.5%** | $1,800 / 24 = **$75.00** |
| **C – Competidor** | 900 / 15,000 = **6.0%** | $3,200 / 900 = **$3.56** | 36 / 900 = **4.0%** | $3,200 / 36 = **$88.89** |

> El gasto actual total es **$7,100**, por encima de tu nuevo límite de **$5,000/mes**.

---

## 2. Qué escalar y qué pausar

### Escalar: Campaña A

Es la campaña más eficiente en el objetivo principal: conseguir signups.

- Tiene el **CPA más bajo: $46.67**
- Convierte al **3.0%**
- Por cada $1,000 invertidos, generaría aproximadamente:

\[
1,000 / 46.67 = 21.4 \text{ signups}
\]

Además, aunque su CTR (3%) no es el mayor, eso no es un problema: atrae tráfico suficientemente cualificado y convierte bien una vez llega a la landing.

### Mantener, pero optimizar y limitar: Campaña B

La campaña B tiene tráfico muy barato y el CTR más sólido después de C:

- CPC de solo **$0.38**
- CTR de **4.0%**

Sin embargo, su conversión es muy baja:

- Conversion rate de solo **0.5%**
- CPA de **$75**, un **61% peor** que A:

\[
(75 / 46.67 - 1) \times 100 = 60.7\%
\]

No la pausaría por completo todavía, porque puede ser útil para capturar demanda informacional y alimentar remarketing. Pero no la escalaría sin mejorar la transición entre el contenido del blog y el signup.

### Pausar o reducir fuertemente: Campaña C

Aunque C tiene las mejores métricas de interacción:

- CTR de **6.0%**
- Conversion rate de **4.0%**

Es la menos eficiente económicamente:

- CPC de **$3.56**
- CPA de **$88.89**, casi el doble que A:

\[
88.89 / 46.67 = 1.9x
\]

Por cada $1,000 invertidos:

- Campaña A: ~**21.4 signups**
- Campaña B: ~**13.3 signups**
- Campaña C: ~**11.3 signups**

**Decisión:** pausaría C inicialmente, salvo que esos leads tengan una tasa de activación, conversión a pago o LTV significativamente superior a los de A y B. Si los usuarios de términos de competidores se convierten más tarde en clientes de mayor valor, entonces podría justificarse un CPA mayor; pero eso debe comprobarse en el CRM, no solo con el dato de signup.

---

## 3. Redistribución del presupuesto de $5,000

### Propuesta recomendada

| Campaña | Presupuesto mensual | % del total | CPA actual | Signups estimados* |
|---|---:|---:|---:|---:|
| **A – Landing principal** | **$4,000** | **80%** | $46.67 | ~86 |
| **B – Blog content** | **$1,000** | **20%** | $75.00 | ~13 |
| **C – Competidor** | **$0** | **0%** | $88.89 | 0 |
| **Total** | **$5,000** | **100%** | — | **~99 signups** |

\*Estimaciones asumiendo que los CPA actuales se mantienen al aumentar o reducir inversión.

Con el gasto anterior de $7,100 conseguiste 105 signups en total:

\[
45 + 24 + 36 = 105
\]

Con esta nueva distribución podrías obtener aproximadamente **99 signups con $5,000**, en vez de gastar $7,100. Es decir: casi el mismo volumen de registros usando alrededor de **30% menos presupuesto**.

### Alternativa más conservadora

Si te preocupa que el CPA de A suba al escalar, puedes empezar durante dos semanas con:

- A: **$3,500**
- B: **$1,000**
- C: **$500** como experimento controlado de competidores

Pero, con los datos actuales, la distribución **$4,000 para A / $1,000 para B / $0 para C** es la más orientada a eficiencia.

---

## 4. A/B tests recomendados para el próximo mes

### Campaña A: mejorar la landing y escalar sin deteriorar CPA

El objetivo es mantener o elevar el 3% de conversion rate mientras incrementas inversión.

**Tests de landing page:**

1. **Propuesta de valor en el titular**
   - Variante A: “Software de gestión de inventario para pymes”
   - Variante B: “Reduce faltantes y controla tu inventario en tiempo real”
   - Variante C: “Ahorra horas cada semana gestionando tu inventario”

2. **CTA**
   - “Crear cuenta gratis”
   - “Probar gratis”
   - “Solicitar demo”
   - “Ver cómo funciona”

   Si el producto es self-service, “Crear cuenta gratis” puede reducir fricción. Si requiere venta consultiva, “Solicitar demo” puede filtrar mejor la calidad.

3. **Formulario**
   - Formulario corto: email + contraseña.
   - Formulario extendido: email + empresa + industria + tamaño de negocio.
   
   Medir no solo signups, sino la calidad posterior: activación, demo agendada o cliente de pago.

4. **Prueba social**
   - Incluir logos de clientes.
   - Añadir testimonios.
   - Mostrar métricas: “Más de X negocios gestionan su inventario con…”
   - Añadir reseñas o puntuaciones.

5. **Landing por intención de keyword**
   No enviar todas las búsquedas a la misma página:
   - “software gestión inventario” → landing enfocada en software y funcionalidades.
   - “inventario pymes” → landing enfocada en problemas específicos de pequeñas empresas: stock, compras, alertas y reportes.

---

### Campaña B: aumentar el conversion rate del 0.5%

Aquí está la oportunidad más clara de optimización. El tráfico es barato, pero los usuarios probablemente están en etapa informacional, no listos para registrarse inmediatamente.

**Tests recomendados:**

1. **CTA dentro del contenido**
   - CTA genérico: “Prueba gratis”.
   - CTA contextual: “Descarga la plantilla de control de inventario”.
   - CTA de valor: “Calcula cuánto te cuesta el sobrestock”.
   - CTA por problema: “Evita quedarte sin stock con alertas automáticas”.

2. **Lead magnet antes del signup**
   En vez de pedir un registro directo desde un artículo, probar:
   - Plantilla de inventario en Excel.
   - Checklist de auditoría de inventario.
   - Calculadora de costo por quiebres de stock.
   - Guía para restaurantes o comercios.

   Después, usar email o remarketing para llevar esos leads al signup.

3. **Landing específica por artículo**
   Para la keyword “problemas inventario restaurante”, usar una página enfocada en restaurantes:
   - Control de mermas.
   - Gestión de ingredientes.
   - Alertas de stock.
   - Costeo de insumos.

4. **Segmentar keywords por intención**
   Separar:
   - Keywords educativas: “cómo gestionar inventario”.
   - Keywords de problema: “problemas inventario restaurante”.
   - Keywords con intención de software: “software para inventario restaurante”.

   Las keywords educativas pueden tener un CPA peor, pero sirven para audiencias de remarketing; las de software deberían tener una landing y pujas más agresivas.

5. **Negativas y concordancias**
   Revisar términos de búsqueda y excluir consultas poco comerciales, por ejemplo:
   - “curso”
   - “definición”
   - “pdf”
   - “trabajo”
   - “gratis excel”, si no tienes una oferta relacionada
   - “ejemplos escolares”

---

### Campaña C: si decides reactivarla en el futuro

No la reactivaría sin un test específico para bajar el CPA.

1. **Landing comparativa dedicada**
   No enviar tráfico de competidores a la landing general. Crear una página del tipo:
   - “Alternativa a [competidor]”
   - Comparativa de funcionalidades.
   - Tabla de precios, soporte, facilidad de migración e integraciones.
   - CTA: “Migrar gratis” o “Ver comparativa”.

2. **Test de mensaje**
   - “Alternativa más simple a [competidor]”
   - “Migra desde [competidor] sin perder datos”
   - “Mejor control de inventario para pymes que [competidor]”

3. **Pujar solo por búsquedas de mayor intención**
   Priorizar:
   - “alternativa a [competidor]”
   - “[competidor] vs [tu marca]”
   - “[competidor] precio”
   - “cambiar de [competidor]”

   Reducir o excluir consultas de investigación muy amplia.

---

## Prioridad operativa para el próximo mes

1. **Escalar A de forma gradual**, vigilando que el CPA no supere aproximadamente $55–60.
2. **Mantener B con presupuesto controlado** y probar mejoras de CTA, lead magnets y landings por industria/intención.
3. **Pausar C** hasta validar si sus signups tienen mejor calidad o hasta crear una landing comparativa específica.
4. Medir no solo signup, sino también:
   - activación del producto,
   - solicitud de demo,
   - usuario activo,
   - conversión a cliente de pago,
   - CAC y LTV por campaña.

La decisión final debe optimizarse por **CPA de cliente pagador**, no únicamente por CPA de signup.