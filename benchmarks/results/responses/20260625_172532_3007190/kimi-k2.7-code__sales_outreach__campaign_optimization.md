# Kimi K2.7 Code — sales_outreach/campaign_optimization

- model_id: `moonshotai/kimi-k2.7-code`
- success: True  | final: 6.66 | quality: 8.64
- latency_total: 105.224s | tokens_per_second: 29.4
- input_tokens: 284 | output_tokens: 3094
- judge_score: 4.6 | justificación: 

## Respuesta completa

Aquí tienes el análisis con las métricas y la recomendación de presupuesto.

## 1. Métricas por campaña

| Campaña | CTR | CPC | CPA | Conversion Rate |
|---|---|---|---|---|
| **A – Landing principal** | 3,0 % | **$1,40** | **$46,67** | 3,0 % |
| **B – Blog content** | 4,0 % | $0,38 | $75,00 | 0,5 % |
| **C – Competidor** | 6,0 % | $3,56 | $88,89 | 4,0 % |

**Cálculos:**
- **CTR** = Clicks / Impresiones
- **CPC** = Costo / Clicks
- **CPA** = Costo / Signups
- **Conv. Rate** = Signups / Clicks

---

## 2. ¿Cuál escalar y cuál pausar?

### ✅ Escalar: Campaña A
- Tiene el **CPA más bajo ($46,67)**, casi la mitad que C.
- Generó la mayor cantidad de signups (45) con un costo razonable.
- Su combinación de CPC bajo ($1,40) + Conversion Rate alto (3 %) la hace la más eficiente.

### ⚠️ Reducir o pausar: Campaña B
- Aunque tiene el **CPC más barato ($0,38)** y buen CTR (4 %), su **Conversion Rate es muy bajo (0,5 %)**.
- Esto eleva su CPA a **$75**, superior al de A.
- Las keywords son de intención informativa (*“cómo gestionar inventario”*), por lo que el tráfico no está listo para comprar/registrarse.

### 🔧 Mantener con optimización: Campaña C
- Tiene el **mejor CTR (6 %)** y el **mejor Conversion Rate (4 %)** → el tráfico es de muy alta intención.
- El problema es el **CPC muy alto ($3,56)**, que encarece el CPA a **$88,89**.
- No conviene escalarla agresivamente hasta bajar ese CPC o confirmar que esos usuarios valen mucho más (LTV alto).

---

## 3. Redistribución del presupuesto de $5,000

Propuesta: **máxima eficiencia sin depender 100 % de una sola campaña.**

| Campaña | Presupuesto | % | Signups esperados* |
|---|---|---|---|
| **A – Landing principal** | $2,750 | 55 % | ~59 |
| **C – Competidor** | $1,250 | 25 % | ~14 |
| **B – Blog content** | $1,000 | 20 % | ~13 |
| **Total** | **$5,000** | 100 % | **~86 signups** |

\* *Asumiendo que las métricas se mantienen constantes.*

**Racional:**
- **A recibe la mayor parte** porque es la que más signups genera por dólar.
- **C conserva presupuesto** porque, aunque cara, tiene la intención más fuerte. Se puede optimizar CPC/CPA.
- **B se reduce drásticamente** y se usa solo para testear mejoras (ver punto 4).

> En el último mes gastaste **$7,100** para **105 signups** (CPA promedio $67,62).  
> Con esta nueva distribución de **$5,000** esperarías **~86 signups** (CPA promedio **~$58**), es decir, más eficiente con menos presupuesto.

---

## 4. A/B tests recomendados para el próximo mes

### Campaña A (escalar)
- **Headline de la landing:** propuesta de valor directa vs. beneficio cuantificado (*“Reduce pérdidas de inventario un 30 %”*).
- **Formulario:** cantidad de campos (email solo vs. nombre + email + empresa).
- **CTA:** *“Empezar gratis”* vs. *“Crear cuenta gratis”* vs. *“Ver demo”*.
- **Prueba social:** agregar logos de clientes, testimonios o número de usuarios.
- **Precios:** mostrar planes desde la landing vs. ocultarlos.

### Campaña B (optimizar antes de escalar)
- **Lead magnet vs. signup directo:** ofrecer una plantilla o checklist en vez de pedir registro inmediato.
- **Landing dedicada vs. artículo de blog:** llevar el tráfico a una página de captura en lugar del post.
- **Popup de salida** con descargable gratuito.
- **Segmentación de keywords:** separar en dos grupos: informativo puro vs. problemas específicos de nicho (*restaurante, retail, etc.*).

### Campaña C (competidor)
- **Página de comparación:** *“[Tu producto] vs [Competidor]”* vs. *“Alternativa a [Competidor]”*.
- **Mensaje de cambio:** *“Migra gratis”* / *“Sin contrato de permanencia”* / *“Onboarding gratis”*.
- **Testimonios de ex-clientes del competidor** si los tienes.
- **Tabla comparativa** arriba del fold vs. abajo.

### A nivel general
- **Audiencias:** probar remarketing para visitantes de la landing A que no se registraron.
- **RLSA (Remarketing Lists for Search Ads):** en B y C para pujar más alto por usuarios que ya visitaron el sitio.
- **Estrategia de puja:** en A probar *Maximizar conversiones con CPA objetivo* ($45–$50).

---

### Resumen ejecutivo
- **Escala A** (mejor CPA y buen volumen).
- **Reduce/pausa B** hasta mejorar su Conversion Rate.
- **Mantén C con presupuesto controlado** y optimiza su CPC.
- Redistribuye como **55 % A / 25 % C / 20 % B** para maximizar signups dentro de los $5,000.