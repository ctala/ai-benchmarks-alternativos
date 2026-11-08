# DeepSeek V4.1 Flash — sales_outreach/campaign_optimization

- model_id: `deepseek/deepseek-v4.1-flash`
- success: True  | final: 7.48 | quality: 8.0
- latency_total: 16.288s | tokens_per_second: 93.2
- input_tokens: 272 | output_tokens: 1518

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

# Análisis de Campañas Google Ads

## 1. Métricas por Campaña

| Métrica | Campaña A | Campaña B | Campaña C |
|---|---|---|---|
| **CTR** | 1,500/50,000 = **3.00%** | 4,800/120,000 = **4.00%** | 900/15,000 = **6.00%** |
| **CPC** | $2,100/1,500 = **$1.40** | $1,800/4,800 = **$0.375** | $3,200/900 = **$3.56** |
| **CPA** | $2,100/45 = **$46.67** | $1,800/24 = **$75.00** | $3,200/36 = **$88.89** |
| **Conversion Rate** | 45/1,500 = **3.00%** | 24/4,800 = **0.50%** | 36/900 = **4.00%** |

**Observaciones clave:**
- **Campaña C** tiene el mejor CTR (6%) y mejor conversion rate (4%), pero el CPC más caro ($3.56) → CPA más alto.
- **Campaña B** tiene CPC baratísimo ($0.375) pero conversion rate pésimo (0.5%) → el tráfico no califica.
- **Campaña A** es la más equilibrada: CPA más bajo ($46.67) y conversión sólida (3%).

---

## 2. ¿Escalar o pausar?

### ✅ ESCALAR: Campaña A
- **CPA más bajo ($46.67)** — es la más eficiente en costo por adquisición.
- Conversion rate del 3% con intención comercial clara ("software gestión inventario").
- CTR del 3% es saludable para keywords transaccionales.
- Hay margen: solo gasta $2,100 de un presupuesto de $5,000.

### ⚠️ REVISAR/OPTIMIZAR (no pausar aún): Campaña C
- Mejor conversion rate (4%) y CTR (6%) → **el mensaje y la audiencia funcionan**.
- El problema es el **CPC ($3.56)**: keywords de competidor son caras por la puja.
- CPA de $88.89 es alto pero **puede mejorar** con negative keywords, ajustes de puja por hora/dispositivo y landing específica de comparación.
- **No pausar**: es tu mejor fuente de conversión cualitativa. Optimizar, no matar.

### 🔴 PAUSAR O REESTRUCTURAR: Campaña B
- **Conversion rate 0.5%** → 200 clicks por signup. El tráfico es informacional, no comprador.
- CPA de $75 con un CPC de $0.375 significa que **el volumen no compensa la calidad**.
- 4,800 clicks generaron solo 24 signups vs. 1,500 clicks de A que dieron 45.
- **Recomendación:** pausar como campaña de adquisición directa. Si quieres mantener contenido, muévelo a **remarketing/lead magnet** (descarga de guía, newsletter) en vez de signup de software.

---

## 3. Redistribución de $5,000/mes

Propuesta basada en eficiencia (CPA) y potencial de escala:

| Campaña | Presupuesto actual | Propuesto | % | Justificación |
|---|---|---|---|---|
| **A (Landing principal)** | $2,100 | **$2,800** | 56% | Mejor CPA, escalar con margen |
| **C (Competidor)** | $3,200 | **$1,500** | 30% | Reducir hasta optimizar CPA; mantener presencia |
| **B (Blog)** | $1,800 | **$400** | 8% | Solo remarketing/lead magnet, no adquisición |
| **Reserva / tests** | $0 | **$300** | 6% | A/B tests y experimentos |

**Lógica:**
- A absorbe el grueso porque es la más rentable y tiene espacio para escalar (aún con CPA estable).
- C se recorta pero no se elimina: su conversion rate alto sugiere que con optimización de CPC puede volverse rentable.
- B se reduce drásticamente: el contenido no convierte a signup; redirigirlo a captura de email.
- Reserva para experimentos evita "quemar" presupuesto en tests sin control.

> **Nota:** si al escalar A el CPA sube por encima de ~$60, conviene frenar y reevaluar. Monitorea semanalmente.

---

## 4. A/B Tests sugeridos para el próximo mes

### Campaña A (prioridad alta)
1. **Landing page:** versión actual vs. versión con prueba social (logos, testimonios, "X pymes ya lo usan").
2. **CTA:** "Prueba gratis" vs. "Solicita demo" vs. "Empieza gratis en 2 min".
3. **Formulario:** signup completo vs. versión corta (solo email) para medir caída de fricción.
4. **Anuncios:** incluir precio o "sin tarjeta de crédito" en el headline.

### Campaña C
5. **Landing comparativa dedicada** ([competidor] vs. tú) con tabla de features — probablemente sube el conversion rate del 4%.
6. **Negative keywords** para filtrar búsquedas de soporte/tutoriales del competidor (gente que no compra).
7. **Ajuste de puja por hora/dispositivo** para reducir CPC en franjas de bajo rendimiento.

### Campaña B (si se mantiene como lead magnet)
8. **Oferta de contenido:** guía descargable vs. plantilla vs. webinar → medir costo por email capturado (no por signup).
9. **Remarketing** a quienes visitaron el blog pero no convirtieron, con oferta de demo.

### Transversal
10. **Test de concordancia de keywords** en A (exacta vs. frase) para controlar calidad de tráfico y sostener el CPA al escalar.

---

**Resumen ejecutivo:** A es tu motor → escálala. C es valiosa pero cara → optimízala, no la mates. B no convierte a signup → reestructúrala como captura de leads o pausa. Redistribuye hacia A con reserva para tests y monitorea el CPA semanalmente al escalar.