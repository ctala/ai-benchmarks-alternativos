# Inkling Small — sales_outreach/campaign_optimization

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.88 | quality: 10.0
- latency_total: 10.033s | tokens_per_second: 160.9
- input_tokens: 267 | output_tokens: 1614

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

Aquí tienes el análisis completo con los cálculos y la estrategia de redistribución.

---

### 1. Métricas por campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** | **3.0%** (1,500/50k) | **4.0%** (4,800/120k) | **6.0%** (900/15k) |
| **CPC** | **$1.40** ($2,100/1,500) | **$0.375** ($1,800/4,800) | **$3.56** ($3,200/900) |
| **Conv. Rate** | **3.0%** (45/1,500) | **0.5%** (24/4,800) | **4.0%** (36/900) |
| **CPA** | **$46.67** ($2,100/45) | **$75.00** ($1,800/24) | **$88.89** ($3,200/36) |

**Resumen rápido:**
- **A** es tu máquina de conversión más eficiente: mejor balance entre volumen y costo por signup.
- **B** genera mucho tráfico barato, pero convierte pésimo (0.5%). Es un “embudo roto” a nivel de landing/CTA.
- **C** tiene el CTR más alto (intención muy fuerte) y la mejor tasa de conversión, pero es **caro** ($3.56 CPC / $88.89 CPA) y con volumen limitado (solo 15k impresiones).

---

### 2. ¿Escalar o pausar?

**Escalar → Campaña A (Landing principal)**
- **Justificación:** CPA más bajo ($46.67), volumen de signups más alto (45) y un CTR decente (3%). Si duplicas su presupuesto, puedes capturar más demanda de alta intención sin romper la economía unitaria. Es tu único canal que combina **escala + eficiencia**.

**Pausar / Reestructurar → Campaña B (Blog content)**
- **Justificación:** Aunque el CPC es casi regalado ($0.375), el CPA es $75 (60% más caro que A) y solo generó 24 signups con 4,800 clicks. Eso indica que el tráfico de “cómo gestionar” o “problemas restaurante” no está listo para convertirse en tu producto. **No escales tráfico que no convierte.** Mejor pausa los grupos de anuncios de blog o redirige ese tráfico a una página de captura (lead magnet) en vez de pedir signup directo.

**Mantener / Ajustar → Campaña C (Competidor)**
- **Justificación:** No la pauses completamente porque el **4% de conversión** y los keywords de “alternativa a [competidor]” son oro puro (intención de compra alta). Pero **no escales agresivamente**: a $3.56 CPC, cada $1,000 extra te trae ~280 clicks y ~11 signups a $88.89 cada uno. Es rentable si tu LTV es alto, pero es tu canal más caro. Mantén un presupuesto de “defensa” para no perder ese tráfico, pero no lo conviertas en tu motor principal.

---

### 3. Redistribución propuesta ($5,000/mes)

Actualmente gastas $7,100 (estás sobre presupuesto o es un ejemplo acumulado). Con **$5,000** te sugiero esta división basada en eficiencia y volumen:

| Campaña | Presupuesto | % | Por qué |
|---|---|---|---|
| **A (Landing)** | **$2,800** | 56% | Escalar lo que funciona. A $46.67 CPA, esto debería traer ~60 signups. |
| **C (Competidor)** | **$1,200** | 24% | Mantener la defensa de marca/competidor. Debería traer ~13-14 signups. |
| **B (Blog)** | **$1,000** | 20% | No lo elimines, pero **cambiá el objetivo**: deja de pedir “signup” directo. Usa ese presupuesto para una campaña de remarketing / captación de emails (lead magnet: “Guía de inventario para restaurantes”) o para probar una landing intermedia. Si no mejora el CPA en 2 semanas, recorta a $500 y pasa a A. |

**Meta estimada con esta distribución:**
- A: ~$2,800 → ~60 signups
- C: ~$1,200 → ~13 signups
- B (reorientado): ~$1,000 → ~10-15 signups (si optimizas landing) o ~13 signups si mantienes (pero a mayor costo).

**Total estimado:** ~83-88 signups vs. los 105 actuales, pero con un **CPA promedio mucho más saludable** (~$57 vs. $67.6 actual) y sin desperdiciar dinero en tráfico frío que no convierte.

---

### 4. A/B Tests para el próximo mes

**En Campaña A (Landing principal) — tu caballo de batalla:**
- **Headline:** “Software de inventario para pymes” vs. “Reduce tu inventario en 30% sin contratar más personal”.
- **CTA:** “Empezar prueba gratis” vs. “Ver demo en 2 minutos”.
- **Social proof:** Añadir logos de clientes o “+200 pymes lo usan” vs. sin logos.
- **Form length:** 2 campos (email + empresa) vs. 4 campos. El objetivo es bajar el CPA de $46.67.

**En Campaña B (Blog) — para arreglar la conversión:**
- **No pidas signup directo.** Prueba una **landing intermedia** (lead magnet) con un PDF “Checklist de inventario para restaurantes” vs. la landing actual.
- **CTA en landing:** “Descargar guía” (micro-conversión) vs. “Crear cuenta”.
- **Audiencia:** Segmenta por “restaurante” vs. “manufactura/retail” para ver si un nichio convierte mejor.

**En Campaña C (Competidor) — para optimizar el CPC:**
- **Copy del anuncio:** “¿Cansado de [Competidor]? Prueba [Tu marca]” vs. “[Competidor] vs [Tu marca]: comparativa 2024”.
- **Landing:** Página “vs” con tabla comparativa (features/pricing) vs. landing genérica. El 4% de conversión puede subir si la landing responde exactamente a la búsqueda.
- **Keyword negación:** Asegúrate de excluir términos como “gratis”, “crack”, “descargar” si no aplican, para limpiar tráfico no calificado.

**Cross-campaign (estructura):**
- Prueba **audiencias de remarketing** de B (quienes visitaron el blog pero no se registraron) con anuncios de C o A para recuperar ese tráfico barato.

---

**Recomendación final:** No te dejes engañar por el CTR de B (4%) ni por el CPC barato. **El dinero está en A** porque convierte. Usa C para defender tu marca y B solo si logras convertir ese tráfico en una micro-conversión (email) antes de pedir el signup. Si en 2 semanas B no baja su CPA a menos de $60, corta su presupuesto y pásalo a A.