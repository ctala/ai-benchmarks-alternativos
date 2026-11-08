# Mistral Large 4.0 — sales_outreach/campaign_optimization

- model_id: `mistralai/mistral-large-4-0`
- success: True  | final: 7.21 | quality: 8.0
- latency_total: 24.444s | tokens_per_second: 161.8
- input_tokens: 261 | output_tokens: 3956

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

Aquí tienes el análisis completo con los cálculos exactos y recomendaciones accionables:

## 1. Métricas calculadas por campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---------|---------------------|------------------|------------------------|
| **CTR** | 3.00% (1,500/50,000) | 4.00% (4,800/120,000) | 6.00% (900/15,000) |
| **CPC** | **$1.40** ($2,100/1,500) | $0.38 ($1,800/4,800) | $3.56 ($3,200/900) |
| **CPA** | **$46.67** ($2,100/45) | $75.00 ($1,800/24) | $88.89 ($3,200/36) |
| **CVR** (Click→Signup) | 3.00% (45/1,500) | 0.50% (24/4,800) | 4.00% (36/900) |
| **Costo por 1,000 imp.** | $42.00 | $15.00 | $213.33 |

**Observación crítica:** Estás gastando $7,100 vs tu presupuesto de $5,000 (42% sobre presupuesto). Necesitas recortar urgentemente.

---

## 2. ¿Cuál escalar y cuál pausar?

### ✅ **ESCALAR: Campaña A**
- **Mejor CPA del portfolio ($46.67)** — 47% más barato que B y 90% más barato que C
- Intención comercial alta: las keywords ("software gestión inventario") buscan solución, no información
- Balance óptimo entre volumen y conversión (45 signups con solo $2,100)

### ❌ **PAUSAR: Campaña C** (o reducir a $0)
- **CPA inaceptable ($88.89)** a menos que tu LTV (valor de vida del cliente) sea >$267 (para mantener ROAS 3:1)
- El CPC de $3.56 es 2.5x más caro que A porque las keywords de competidor tienen CPC inflado por la puja agresiva
- Aunque tiene buena CVR (4%), pagas demasiado por entrar al funnel
- **Excepción:** Si tu producto es B2B enterprise con contratos anuales >$1,000, mantén un presupuesto mínimo de $500 solo con concordancia exacta estricta

### ⚠️ **OPTIMIZAR (no pausar): Campaña B**
- Tráfico barato ($0.38 CPC) pero **conversión nefasta (0.5%)**
- Las keywords informativas ("cómo gestionar", "problemas...") atraen curiosos, no compradores
- **No busques signups aquí**, úsala como fuente de remarketing

---

## 3. Redistribución recomendada de los $5,000

| Campaña | Asignación | % | Proyección mensual | Justificación |
|---------|-----------|---|-------------------|---------------|
| **A - Escalar** | **$3,000** | 60% | ~64 signups (a CPA constante) o ~70 si optimizas | Multiplica lo que funciona. A este ritmo, generarás 64-70 leads calificados |
| **B - Reconvertir** | **$1,000** | 20% | No busques signups directos | Cambia objetivo a "tiempo en página >2min" o "clic en CTA interno". Usa estos visitantes para **remarketing** en Display/YouTube |
| **Reserva Test** | **$1,000** | 20% | 10-15 signups adicionales | Nueva campaña de **Remarketing** (visitantes de B que no convirtieron) + testear **DSA** (Dynamic Search Ads) o YouTube |
| **C - Pausada** | **$0** | 0% | - | Reasigna ese dinero a A. Si el LTV justifica, máximo $500 con concordancia exacta |

**Resultado esperado:** ~75-85 signups vs los 105 actuales, pero con un **CPA promedio de ~$62** (vs $79 actual) y mejor calidad de lead (más de A, menos de B/C).

---

## 4. A/B Tests sugeridos para el próximo mes

### 🎯 **Para Campaña A (prioridad alta)**
1. **Formulario de landing:**
   - Test A: Solo email + nombre (2 campos)
   - Test B: Email + nombre + teléfono + empresa (4 campos)
   - *Hipótesis:* Menos fricción = más conversiones, pero ¿la calidad baja?

2. **Propuesta de valor en anuncios (RSA):**
   - Test A: "Gestiona tu inventario en minutos" (beneficio tiempo)
   - Test B: "Evita pérdidas de $X al mes" (beneficio económico)
   - Test C: "El software que usan +500 PYMES" (prueba social)

3. **CTA del botón:**
   - "Prueba gratis 14 días" vs "Ver demo en vivo" vs "Calcular mi ahorro"

4. **Audiencias:**
   - Crear **Similar Audiences (1-3%)** basadas en los 45 signups actuales
   - Testear **In-market audiences**: "Software de gestión empresarial"

### 📝 **Para Campaña B (cambio de estrategia)**
No testees signups directos (ya vimos que no funcionan). En su lugar:
1. **Test de contenido:** Guía paso a paso (texto largo) vs Infografía descargable vs Video de 2 min
2. **CTA interno:** "Ver cómo lo resolvemos" (lleva a demo de A) vs "Descargar checklist" (captura email para nurturing)
3. **Landing de blog:** Agregar widget de "Calculadora de costos de inventario" como micro-conversión

### 🔄 **Tests transversales (con la reserva de $1,000)**
1. **Remarketing de "calentamiento":** Anuncios en Display a quienes visitaron el blog B pero no hicieron signup en A (mensaje: "Aún puedes probarlo gratis")
2. **YouTube TrueView:** Video de 30s explicando el problema del inventario manual → Landing A
3. **DSA (Dynamic Search Ads):** Dejar que Google genere anuncios basados en el contenido de tu sitio (bueno para captar keywords long-tail que no estás cubriendo)

### ⚡ **Quick win inmediato:**
Antes de gastar los $5,000, verifica en Google Analytics si los 45 signups de A son **leads calificados** (¿cuántos pidieron demo o compraron?). Si la tasa de cierre es <10%, tu CPA real es infinito y necesitas ajustar la campaña A para atraer menos volumen pero más calidad (ej: agregar "+precio" o "demo" a las keywords para filtrar curiosos).

**Resumen ejecutivo:** Pon el 60% en A, convierte B en embudo de remarketing, y elimina C salvo que vendas contratos enterprise.