# Qwen 3.7 Flash — sales_outreach/campaign_optimization

- model_id: `qwen/qwen3.7-flash`
- success: True  | final: 9.18 | quality: 10.0
- latency_total: 29.524s | tokens_per_second: 117.5
- input_tokens: 309 | output_tokens: 3470

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

Aquí tienes el análisis detallado, optimizado para tomar decisiones basadas en datos:

### 1. Métricas clave por campaña
| Campaña | CTR | CPC | CVR (Tasa de conversión) | CPA (Costo por Signup) |
|---------|-----|-----|--------------------------|------------------------|
| **A** (Landing principal) | `3.0%` | `$1.40` | `3.0%` | `$46.67` |
| **B** (Blog content) | `4.0%` | `$0.38` | `0.5%` | `$75.00` |
| **C** (Competidor) | `6.0%` | `$3.56` | `4.0%` | `$88.89` |

*Cálculos:*  
`CTR = (Clicks / Impresiones) × 100` | `CPC = Costo / Clicks` | `CVR = (Signups / Clicks) × 100` | `CPA = Costo / Signups`

---

### 2. ¿Cuál escalar y cuál pausar? (Justificación numérica)

🔹 **ESCALAR: Campaña A**  
- **Mejor CPA** (`$46.67`) y el único con equilibrio entre volumen y eficiencia.  
- Palabras de **alta intención comercial** ("software gestión inventario", "inventario pymes").  
- CVR sólido (`3%`) + CPC bajo (`$1.40`). Es tu motor de crecimiento actual.

🟡 **REDUCIR / PAUSAR PARCIALMENTE: Campaña B**  
- Aunque tiene el CPC más barato (`$0.38`) y alto CTR (`4%`), su **CVR es muy bajo** (`0.5%`).  
- Las búsquedas son **educativas/top of funnel**: atraen curiosos, no compradores listos.  
- CPA (`$75`) es un 60% mayor que el de A. Si tu objetivo es signups directos, es ineficiente mantenerla al nivel actual.

🟠 **MANTENER CON LIMITES: Campaña C**  
- Mayor intención de compra (buscan alternativas directas), pero el **CPA es el más caro** (`$88.89`).  
- Puede ser rentable si tu LTV (valor de vida del cliente) lo justifica, pero **no es escalable sin optimizar** landing o propuesta de valor. Úsala como captura estratégica, no como motor principal.

> ⚠️ Nota: Tus costos reales suman `$7,100`, pero indicas un presupuesto de `$5,000`. El siguiente plan asume que debes operar dentro de esos `$5,000` este mes.

---

### 3. Redistribución recomendada del presupuesto (`$5,000/mes`)

| Campaña | Asignación | % | Razón |
|---------|------------|----|-------|
| **A** (Landing) | `$3,500` | 70% | Máxima eficiencia. Permite ~250 clicks adicionales manteniendo CPA estable. |
| **C** (Competidor) | `$1,000` | 20% | Captura intención transaccional. Monitorea CPA semanalmente; si sube de `$80`, reduce. |
| **B** (Blog) | `$500` o `PAUSAR` | 10% | Mantén solo si buscas creación de audiencia para remarketing. Si el KPI es solo signups, púsala en pausa y redirige ese gasto a A. |

**Regla de ajuste:** Revisa CPA cada 7 días. Si A mantiene CPA `< $50`, continúa escalando. Si supera `$60`, optimiza landing antes de aumentar presupuesto.

---

### 4. Pruebas A/B sugeridas para el próximo mes

| Área | Hipótesis | Métrica de éxito | Cómo ejecutar |
|------|-----------|------------------|---------------|
| **Landing Page** | Cambiar headline genérico por uno basado en dolor específico + formulario de 3 campos vs 5 campos | ↑ CVR ≥ 4% | Usa Google Optimize/Unbounce. Segmenta 50/50 del tráfico de A. |
| **Anuncios** | Incluir mención de "Prueba gratis 14 días" o precio mensual vs solo beneficios abstractos | ↑ CTR ≥ 3.5% + ↓ CPA ≤ $45 | Crea 2 variantes por grupo de palabras en Campaña A. Pausa la peor tras 7 días. |
| **Retargeting** | Crear audiencia con los 4,800 clicks de Campaña B y mostrarles caso de uso + testimonio de cliente real | ↑ CVR ≥ 2% | Usa lista de visitantes web (30 días). Presupuesto dedicado: `$300-$400`. |
| **Match Types** | En Campaña A, separar `Exact Match` vs `Phrase Match` y aplicar pujas diferenciadas | ↓ CPC en frase, ↑ CVR en exacto | Crea 2 grupos dentro de A. Pujar 20% más en Exacto si CPA es estable. |

---

### 🔍 Recomendación final
1. **Define tu CPA objetivo** según tu LTV. Si un signup vale `$150+`, incluso la Campaña C podría ser rentable. Si tu umbral es `$50`, enfócate 100% en A.
2. Implementa **conversion tracking avanzado** (signup → activation → pago) para medir ROI real, no solo leads fríos.
3. Revisa **palabras negativas** en Campaña B y C para eliminar tráfico "cómo funciona", "gratis", "descargar pdf" que inflan clicks sin intención de compra.

¿Quieres que te arme una plantilla de seguimiento semanal con alertas de CPA o un guion para las creatividades del A/B test?