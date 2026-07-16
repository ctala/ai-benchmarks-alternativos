# Qwen 3.6 Plus — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3.6-plus`
- success: True  | final: 8.59 | quality: 10.0
- latency_total: 73.948s | tokens_per_second: 54.7
- input_tokens: 309 | output_tokens: 4046
- judge_score: 5 | justificación: La respuesta es precisa, relevante, profunda, clara y extremadamente útil, proporcionando análisis detallados y recomendaciones estratégicas basadas en los datos de la campaña.

## Respuesta completa

Aquí tienes el análisis detallado y las recomendaciones estratégicas basadas en tus datos:

### 1. Cálculo de métricas por campaña
| Métrica | Campaña A | Campaña B | Campaña C |
|:---|:---:|:---:|:---:|
| **CTR** | 3.00% | 4.00% | 6.00% |
| **CPC** | $1.40 | $0.38 | $3.56 |
| **CPA** | $46.67 | $75.00 | $88.89 |
| **Conversion Rate (CVR)** | 3.00% | 0.50% | 4.00% |

*Fórmulas usadas:*  
`CTR = (Clicks/Impresiones)×100` | `CPC = Costo/Clicks` | `CPA = Costo/Signups` | `CVR = (Signups/Clicks)×100`

---

### 2. ¿Cuál escalar y cuál pausar? (Justificación numérica)
- ✅ **Escalar: Campaña A**  
  Tiene el **CPA más bajo ($46.67)** y un CVR saludable (3%). Sus keywords son de alta intención comercial (`software gestión inventario`, `inventario pymes`), lo que indica que los usuarios ya están en fase de evaluación/compra. Es la campaña más eficiente para generar signups al menor costo.

- ⚠️ **Mantener con ajuste: Campaña C**  
  CVR alto (4%), pero **CPA casi el doble que A ($88.89)** y CPC muy elevado ($3.56). Las keywords de competidor suelen tener subastas agresivas. Vale la pena conservarla para captar demanda madura, pero requiere optimización de pujas y palabras negativas para bajar el CPA.

- ❌ **Pausar (o redirigir): Campaña B**  
  Aunque tiene CTR alto (4%) y CPC bajo ($0.38), su **CVR es extremadamente bajo (0.5%)** y su CPA ($75) es ineficiente para adquisición directa. Estas keywords son de **conciencia/educación** (`como gestionar...`, `problemas...`). Funcionan mejor para SEO, remarketing o como entrada a un embudo con lead magnet, no para campañas de conversión directa.

> 📌 **Nota importante:** Tu gasto actual suma **$7,100**, pero tu presupuesto es **$5,000/mes**. La redistribución es obligatoria para alinearte al límite.

---

### 3. Redistribución recomendada del presupuesto ($5,000)
| Campaña | % Presupuesto | Monto | Signups estimados* |
|:---|:---:|:---:|:---:|
| **A (Principal)** | 70% | $3,500 | ~75 |
| **C (Competidor)** | 25% | $1,250 | ~14 |
| **B (Blog)** | 5% | $250 | ~3 |
| **Total** | 100% | $5,000 | **~92** |

\* *Estimación basada en CPA actual. En la práctica, al optimizar pujas y creatividades, el CPA de A podría bajar a ~$40, aumentando el volumen.*

**Por qué esta distribución:**
- **70% en A:** Maximiza volumen de signups al menor costo. Deja margen para escalar keywords exactas y ampliar audiences similares.
- **25% en C:** Reserva presupuesto para captar demanda de alta intención, pero con límite de gasto para evitar que el CPC dispare el CPA.
- **5% en B (o 0%):** Si la pausas, mueve ese 5% a A. Si la mantienes, úsala solo para alimentar listas de remarketing o pruebar un lead magnet. No la uses para conversión directa.

---

### 4. A/B Tests sugeridos para el próximo mes
| Test | Variantes | Métrica clave | Duración mínima |
|:---|:---|:---:|:---:|
| **1. Landing Page (Campaña A)** | Formulario corto (2 campos) vs. Largo (5 campos + testimonios) | CVR & CPA | 2-3 semanas o 500+ clicks/variante |
| **2. Propuesta de valor (Anuncios A)** | "Ahorra 30% en gestión de inventario" vs. "Implementación en 24h, sin código" | CTR & CVR | 14 días |
| **3. Pujas & Match Types (Campaña C)** | Exact match puro vs. Phrase match + lista de negativas agresiva | CPC & CPA | 21 días |
| **4. Lead Magnet (Campaña B, si se mantiene)** | Signup directo vs. Descarga gratuita "Checklist de inventario para restaurantes" | CVR & Costo por lead | 14-21 días |

**Cómo ejecutarlos correctamente:**
- Cambia **una sola variable** por test.
- Usa la función de "Experimentos" de Google Ads para evitar sesgos de temporada.
- Define significancia estadística (>95%) y volumen mínimo antes de tomar decisiones.
- Mide no solo el CPA, sino también **calidad del lead** (ej. % que activa la cuenta o solicita demo).

---

### 💡 Recomendación adicional
Implementa **pujas inteligentes** (tCPA o Maximize Conversions) en la Campaña A una vez tengas ±30 conversiones/mes consistentes. Google optimizará automáticamente hacia usuarios con mayor probabilidad de signup, reduciendo aún más tu CPA real.

¿Quieres que te ayude a estructurar la hoja de cálculo para trackear estos tests o a redactar las variantes de anuncios?