# DeepSeek V4 Pro — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v4-pro`
- success: True  | final: 8.55 | quality: 10.0
- latency_total: 19.174s | tokens_per_second: 79.0
- input_tokens: 272 | output_tokens: 1515

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

¡Excelente! Vamos a analizar tus campañas paso a paso.

---

## 1. Cálculo de métricas por campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---------|---------------------|------------------|------------------------|
| **CTR** | 1,500/50,000 = **3.00%** | 4,800/120,000 = **4.00%** | 900/15,000 = **6.00%** |
| **CPC** | $2,100/1,500 = **$1.40** | $1,800/4,800 = **$0.375** | $3,200/900 = **$3.56** |
| **CPA** | $2,100/45 = **$46.67** | $1,800/24 = **$75.00** | $3,200/36 = **$88.89** |
| **Conv. Rate** | 45/1,500 = **3.00%** | 24/4,800 = **0.50%** | 36/900 = **4.00%** |

**Gasto total actual:** $2,100 + $1,800 + $3,200 = **$7,100** (Excede tu presupuesto de $5,000)

---

## 2. ¿Cuál escalar y cuál pausar?

### ✅ **CAMPAÑA A — ESCALAR (Prioridad 1)**
- **CPA más bajo:** $46.67 (47% mejor que B, 90% mejor que C)
- **Conversion rate sólido:** 3.00% en landing principal
- **CTR decente:** 3% con keywords de alta intención comercial
- **Costo controlado:** CPC de $1.40 razonable para B2B/SaaS
- **Justificación:** Por cada $1,000 invertidos obtienes ~21.4 signups vs 13.3 de B y 11.2 de C. Es la máquina de conversión.

### ⚠️ **CAMPAÑA C — OPTIMIZAR, NO PAUSAR**
- **Mejor conversion rate:** 4.00% (tráfico ultra calificado)
- **Pero CPA alto:** $88.89 por el CPC elevado ($3.56)
- **Justificación:** El problema no es la campaña, es el costo por clic. Si logras bajar el CPC mejorando Quality Score, puede ser muy rentable. Las keywords de competidor suelen tener alto valor de cliente (mayor LTV).

### ❌ **CAMPAÑA B — PAUSAR O REESTRUCTURAR**
- **CPA más alto relativo a intención:** $75.00
- **Conversion rate bajísimo:** 0.50% (tráfico informativo, no transaccional)
- **Justificación:** Atrae 4,800 clicks pero solo 24 convierten. Son usuarios en etapa de awareness, no de decisión. El blog content funciona para SEO orgánico, no para Google Ads pago.

---

## 3. Redistribución del presupuesto de $5,000

| Campaña | Presupuesto actual | Nuevo presupuesto | Signups estimados |
|---------|-------------------|-------------------|-------------------|
| **A (Landing)** | $2,100 | **$3,000** | ~64 |
| **C (Competidor)** | $3,200 | **$1,500** | ~17 |
| **B (Blog)** | $1,800 | **$500** | ~7 |
| **TOTAL** | $7,100 | **$5,000** | **~88** |

**Resultado proyectado:**
- Con $7,100 obtenías 105 signups → 14.8 signups/$1,000
- Con $5,000 redistribuido obtendrías ~88 signups → 17.6 signups/$1,000
- **Mejora de eficiencia del 19%** y te ajustas al presupuesto

**Lógica:**
- **Campaña A recibe 60%:** Es tu caballo ganador. Escalar agresivamente con nuevas keywords relacionadas.
- **Campaña C recibe 30%:** Mantener presencia competitiva pero ajustando pujas y negativizando términos no rentables.
- **Campaña B recibe 10%:** Solo para Remarketing o RLSA (Remarketing Lists for Search Ads) sobre quienes visitaron el blog, con oferta más agresiva.

---

## 4. A/B Tests sugeridos para el próximo mes

### Para Campaña A (Landing Principal):
1. **Headline test:** "Software de Inventario" vs "Controla tu Inventario en Minutos" (beneficio vs funcionalidad)
2. **CTA button:** "Comenzar Prueba Gratis" vs "Ver Demo" vs "Comenzar Ahora"
3. **Social proof position:** Testimonios arriba del fold vs después de features
4. **Formulario:** 3 campos (nombre, email, empresa) vs 5 campos (agregar teléfono, empleados) — mide si baja conversión pero mejora calidad de lead

### Para Campaña C (Competidor):
5. **Landing page dedicada:** Página genérica vs página tipo "[Competidor] vs Nosotros" con tabla comparativa
6. **Oferta:** "Prueba gratis 14 días" vs "激Migra tus datos gratis + 30 días" (incentivo de switching)
7. **Ad copy angle:** "La alternativa #1 a [Competidor]" vs "¿Cansado de [Competidor]? Descubre [Nosotros]"

### Para Campaña B (Blog - si mantienes tráfico):
8. **Pop-up timing:** Exit-intent pop-up vs scroll 50% vs tiempo en página (30 segundos)
9. **Lead magnet:** "Guía PDF: 10 Errores de Inventario" vs "Plantilla Excel de Inventario Gratis" vs "Newsletter semanal"
10. **Remarketing:** Usuarios del blog que no convirtieron → impactarlos con anuncio de Campaña A con descuento especial

---

### Recomendación estratégica adicional:
Con el CPA de $46.67 de la Campaña A, calcula el LTV de un cliente. Si un cliente paga ≥$50/mes y se queda 6+ meses, tu ROAS es excelente y deberías considerar **aumentar el presupuesto total por encima de $5,000** si el flujo de caja lo permite.

¿Quieres que profundice en alguno de estos puntos?