# Claude Sonnet 5 — sales_outreach/campaign_optimization

- model_id: `anthropic/claude-sonnet-5`
- success: True  | final: 8.18 | quality: 10.0
- latency_total: 40.285s | tokens_per_second: 86.9
- input_tokens: 393 | output_tokens: 3499

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

# Análisis de Performance - Google Ads

## 1. Métricas por Campaña

| Métrica | Campaña A (Landing) | Campaña B (Blog) | Campaña C (Competidor) |
|---|---|---|---|
| **CTR** | 3.0% | 4.0% | 6.0% |
| **CPC** | $1.40 | $0.38 | $3.56 |
| **CPA** | **$46.67** | $75.00 | $88.89 |
| **Conv. Rate** | 3.0% | **0.5%** ⚠️ | 4.0% |

⚠️ **Alerta importante**: Estás gastando $2,100 + $1,800 + $3,200 = **$7,100**, pero tu presupuesto es $5,000. Ya estás **42% sobre presupuesto**. Esto hay que corregirlo de inmediato, independiente de la redistribución.

---

## 2. Qué escalar y qué pausar

### 🟢 Escalar: Campaña A
- **CPA más bajo ($46.67)** con conversion rate saludable (3%)
- Keywords de intención transaccional clara ("software gestión inventario")
- Es tu campaña más eficiente en costo/resultado

### 🟡 Mantener con cautela: Campaña C
- CPA alto ($88.89), pero tiene el mejor CTR (6%) y mejor conv. rate (4%)
- Tráfico de "competidor vs" suele traer usuarios en decisión final de compra → **posible LTV más alto** (dato que no tenemos, pero deberíamos medir)
- No pausar sin antes ver LTV/CAC — si el LTV promedio es >3x el CPA, vale la pena aunque sea caro

### 🔴 Pausar o reestructurar: Campaña B
- **Conversion rate de 0.5% es una señal de fondo del funnel roto**, no de mala campaña
- Generas 4,800 clicks (el mayor volumen) pero solo 24 signups
- El problema: keywords informacionales ("cómo gestionar inventario") mandan tráfico de **awareness** directo a un formulario de signup, sin nurturing intermedio
- Esto no es un problema de presupuesto, es un problema de **mismatch entre intención de búsqueda y oferta de landing**

---

## 3. Redistribución de $5,000

| Campaña | Presupuesto anterior | Nuevo presupuesto | % del total | Razón |
|---|---|---|---|---|
| A | $2,100 | **$2,600** | 52% | Escalar el CPA más eficiente |
| C | $3,200 | **$1,600** | 32% | Reducir volumen, mantener solo si LTV lo justifica |
| B | $1,800 | **$800** | 16% | Presupuesto mínimo para testear fix de funnel, no para escalar clicks |

**Total: $5,000** ✅

Si en 2-3 semanas B sigue con conv rate <1% después del test de landing, mover ese $800 completo a A.

---

## 4. A/B Tests sugeridos

**Campaña A (optimizar el ganador):**
- Test de headline: enfoque en "ahorro de tiempo" vs "control de stock en tiempo real"
- CTA: "Prueba gratis" vs "Ver demo" vs "Empieza ahora"
- Prueba social: agregar testimonios/logos de clientes arriba del fold vs abajo

**Campaña B (arreglar el funnel, no el ad):**
- **Test crítico**: en vez de mandar a signup directo, mandar a una landing con lead magnet (ej. "Checklist gratis: 5 errores de inventario en restaurantes") → capturar email → nutrir por email antes de pedir signup
- Separar keywords informacionales puras ("cómo gestionar inventario") de las con intención comercial ("problemas inventario restaurante") — probablemente necesiten landings distintas
- Medir signup rate del funnel con lead magnet vs funnel directo actual

**Campaña C (validar si vale el costo):**
- Landing tipo "batalla" con tabla comparativa vs tu landing genérica actual
- Test de formulario: reducir fricción (menos campos) ya que el usuario ya viene "convencido"
- **Lo más importante**: instrumentar tracking de LTV por campaña — sin esto, no sabes si $88.89 de CPA es carísimo o barato

**Transversal:**
- Test de estrategia de puja: Manual CPC vs Target CPA en las 3 campañas
- Medir signup → activación real (no solo el signup, sino cuántos usan el producto) para validar si el conv rate está capturando el KPI correcto