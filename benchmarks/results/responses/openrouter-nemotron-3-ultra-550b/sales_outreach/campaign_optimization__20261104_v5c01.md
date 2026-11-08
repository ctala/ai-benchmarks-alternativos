# Nemotron 3 Ultra 550B — sales_outreach/campaign_optimization

- model_id: `nvidia/nemotron-3-ultra-550b-a55b`
- success: True  | final: 7.27 | quality: 8.0
- latency_total: 15.201s | tokens_per_second: 163.7
- input_tokens: 316 | output_tokens: 2489

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

Aquí tienes el análisis completo con cálculos, recomendaciones estratégicas y plan de acción.

---

### 1. Cálculo de Métricas Clave

| Métrica | **Campaña A** (Landing Principal) | **Campaña B** (Blog Content) | **Campaña C** (Competidor) |
| :--- | :---: | :---: | :---: |
| **CTR** (Clicks / Impr.) | **3.00%** (1,500 / 50k) | **4.00%** (4,800 / 120k) | **6.00%** (900 / 15k) |
| **CPC** (Costo / Clicks) | **$1.40** ($2,100 / 1,500) | **$0.375** ($1,800 / 4,800) | **$3.56** ($3,200 / 900) |
| **Conversion Rate** (Signups / Clicks) | **3.00%** (45 / 1,500) | **0.50%** (24 / 4,800) | **4.00%** (36 / 900) |
| **CPA** (Costo / Signups) | **$46.67** ($2,100 / 45) | **$75.00** ($1,800 / 24) | **$88.89** ($3,200 / 36) |
| **Share de Presupuesto** | 42% | 36% | 64% |
| **Share de Conversiones** | 43% | 23% | 34% |

> **Nota:** El gasto actual total es **$7,100** (excede tu presupuesto de $5,000 en $2,100). La redistribución obligatoria es necesaria.

---

### 2. ¿Qué escalar y qué pausar? (Justificación numérica)

#### ✅ **ESCALAR: Campaña A (Landing Principal)**
*   **Mejor CPA ($46.67):** Es un **47% más barato** que la Campaña C y **38% más barato** que la B.
*   **Mejor eficiencia global:** Genera el **43% de las conversiones** consumiendo solo el **30% del gasto actual** ($2,100 de $7,100).
*   **Intención comercial alta:** Keywords de "fondo de embudo" (*bottom-funnel*): usuarios buscando comprar/contratar *ahora*.
*   **Márgen de escala:** Solo 50k impresiones. Si el *Impression Share* (cuota de impresiones) no es 100%, hay inventario barato por capturar.

#### ⏸️ **PAUSAR (o reducir drástico): Campaña C (Competidor)**
*   **Peor CPA ($88.89):** Casi **el doble de coste por cliente** que la Campaña A.
*   **CPC insostenible ($3.56):** Estás pagando una "prima de marca" altísima. Las keywords de competidor suelen tener Quality Score bajo, inflando el CPC.
*   **Volumen bajo:** Solo 36 signups/mes. Aunque la tasa de conversión es buena (4%), el coste de adquisición no compensa a menos que el LTV (Valor Vida Cliente) de estos usuarios sea drásticamente superior (ej. clientes enterprise que vienen de ese competidor).
*   **Acción:** Pausar **ya** para liberar $3,200. Reactivar solo si pruebas *ad copy* muy agresivas ("Migración gratis", "Importamos tus datos") y logras bajar CPA < $60.

#### ⚠️ **OPTIMIZAR (No pausar aún): Campaña B (Blog Content)**
*   **CTR alto (4%) + CPC muy bajo ($0.38):** Tráfico barato y relevante.
*   **Problema: Conversion Rate (0.50%):** Es **6x peor que A** y **8x peor que C**. El tráfico es "informacional" (TOFU), no transaccional.
*   **Potencial:** Si arreglas la conversión (ver tests abajo), podría ser tu canal de volumen barato. **Mantén presupuesto mínimo ($500-$800) solo para tests de CRO.**

---

### 3. Redistribución del Presupuesto ($5,000/mes)

**Estrategia:** *Maximizar conversiones inmediatas (Campaña A) + Comprar datos de CRO baratos (Campaña B).*

| Campaña | Presupuesto Asignado | % Total | Justificación |
| :--- | :---: | :---: | :--- |
| **A (Landing Principal)** | **$3,500** | **70%** | Motor principal. Con CPA ~$46, proyectas **~76 signups/mes** (vs 45 actuales). Asegura que *Impression Share* > 80-90% en keywords exactas. |
| **B (Blog / TOFU)** | **$1,000** | **20%** | Fondo de pruebas. Con CPC $0.38 = ~2,600 clicks/mes. Suficiente para testear *lead magnets*, pop-ups, retargeting audiences. **Objetivo: Llevar CR > 1.5% (CPA < $25).** |
| **C (Competidor)** | **$0** | **0%** | Pausada. Libera $3,200. |
| **Reserva / Tests Nuevos** | **$500** | **10%** | Para lanzar Campaña D (Retargeting / RLSA) o probar *Performance Max* solo para "New Customers". |

**Proyección de Resultados (Mes Siguiente):**
*   **Campaña A:** ~76 Signups (@ $46 CPA)
*   **Campaña B:** ~13 Signups (@ $75 CPA actual) → **Meta: 40+ Signups si logras CPA $25 via CRO**
*   **Total Estimado Conservador:** **~89 Signups** (vs 105 actuales, pero **ahorrando $2,100/mes**).
*   **Eficiencia:** CPA Blended objetivo **< $55** (Actual: $67.6).

---

### 4. A/B Tests para el Próximo Mes

#### Prioridad 1: Campaña A (Donde está el dinero) - *Optimización de Márgenes*
| Test | Hipótesis | Implementación |
| :--- | :--- | :--- |
| **Landing Page: "Above the Fold"** | El headline actual es genérico. Un headline centrado en *dolor específico* + *resultado cuantificado* sube CR. | **Control:** "Software de Gestión de Inventario para Pymes" <br> **Variante:** "Reduce mermas un 30% y ahorra 10h/semana en conteos: Inventario Automatizado para Pymes" |
| **Formulario: Longitud vs Calidad** | Pides muchos campos (Teléfono, Empresa, Tamaño...). Reducir fricción sube CVR, pero ¿baja calidad (MQL->SQL)? | **Control:** 5 campos. <br> **Variante:** 3 campos (Email, Nombre, "¿Cuál es tu mayor dolor hoy?"). Medir: Signups **Y** % SQL a 7 días. |
| **Ad Copy: Beneficio vs Característica** | Keywords "software gestion inventario" son commodities. Diferenciar por *outcome*. | **Control:** "Gestión de Inventario Fácil. Prueba Gratis." <br> **Variante:** "El único que sincroniza Tienda Física + Online en tiempo real. Demo 15 min." |

#### Prioridad 2: Campaña B (El mayor upside oculto) - *Conversión de Tráfico Frío*
| Test | Hipótesis | Implementación |
| :--- | :--- | :--- |
| **Lead Magnet "Content Upgrade"** | El blog da info gratis y el user se va. Dar un "checklist/plantilla" a cambio de email captura la demanda. | **Control:** CTA "Regístrate a nuestro newsletter" en sidebar. <br> **Variante:** Popup/Inline al 60% scroll: *"Descarga la 'Plantilla Excel: Conteo Cíclico Semanal' que usan 500+ restaurantes"* → Thank you page = Soft sell Demo. |
| **Retargeting (RLSA / Audiencias)** | El 99.5% no convierte en visita 1. Son baratos de "perseguir". | Crear audiencia "Visitors Blog 30d - No Signup". Campaña Search/Display separada ($300) con ads: *"¿Sigues contando a mano? Automatízalo hoy"*. |
| **Artículo "Best Of" / Comparativa** | Keywords "problemas inventario restaurante" buscan soluciones, no teoría. | Escribir/optimizar post: **"Top 5 Softwares Inventario Restaurantes 2024 (Comparativa Precios/Features)"**. Insertar tabla comparativa **tu producto vs 4 competidores** + CTA directo a Demo. |

#### Prioridad 3: Nueva Campaña (Bajo Riesgo / Alto ROI)
| Test | Hipótesis | Implementación |
| :--- | :--- | :--- |
| **Campaña D: Brand Defense / RLSA** | Tu marca tiene búsquedas. Competidores pujan por ti. Usuarios que visitaron web no convierten. | 1. **Brand Search:** $200/mes (CPC ~$0.50, CR > 15%). <br> 2. **RLSA (Search):** Bid +50% en Campaña A keywords para audiencia "Visitors 30d". <br> 3. **YouTube/Display Retargeting:** Video caso cliente (30s) a "Visitors Pricing Page / Demo Page". |

---

### Resumen Ejecutivo para tu Jefe/Cliente
> **"Recortamos gasto un 30% ($7.1k → $5k) manteniendo ~85% del volumen de leads (105 → ~89) y mejorando CPA blended un 19% ($67 → ~$55). Pausamos Campaña Competidor (CPA $89) por ineficiente. Apostamos fuerte por Landing Principal (CPA $46) y usamos Blog como laboratorio de CRO barato para crear 2do motor de crecimiento."**