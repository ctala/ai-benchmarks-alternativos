# LFM-3 1.7B — sales_outreach/campaign_optimization

- model_id: `liquid/lfm-3-1.7b`
- success: True  | final: 7.59 | quality: 8.0
- latency_total: 18.832s | tokens_per_second: 314.2
- input_tokens: 280 | output_tokens: 5917

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

## 1️⃣ Métricas de cada campana (mes)

| Campana | Impresiones | Clicks | Costo | Sign‑ups | CTR (Impresiones→Clicks) | CPC (Costo→Clicks) | CPA (Costo→Sign‑ups) | Conversion Rate (Click→Sign‑ups) |
|--------|------------|-------|-------|----------|---------------------------|----------------------|----------------------|------------------------------------|
| **A – Landing principal** | 50 000 | 1 500 | $2 100 | 45 | **3.00 %** | **$1,40** | **$46,67** | **3,00 %** (45÷1 500) |
| **B – Blog content** | 120 000 | 4 800 | $1 800 | 24 | **4,00 %** | **$0,38** | **$75,00** | **0,50 %** (24÷4 800) |
| **C – Competidor** | 15 000 | 900 | $3 200 | 36 | **6,00 %** | **$3,56** | **$88,89** | **4,00 %** (36÷900) |

> **Fórmulas usadas**  
> • CTR = (Clicks / Impresiones) × 100%  
> • CPC = Costo total / Clicks  
> • CPA = Costo total / Sign‑ups  
> • Conversion Rate = Sign‑ups / Clicks × 100%  

---

## 2️⃣ ¿Qué escalar y cuál pausar?

### 📈 Tendencias claras

| Indicador | Campana A | Campana B | Campana C |
|-----------|-----------|-----------|-----------|
| **CPC** (más bajo = más barato por clic) | $1,40 | $0,38 (muy bajo) | $3,56 (alto) |
| **CPA** (más bajo = menos gasto por sign‑up) | $46,67 | $75,00 | $88,89 |
| **CTR** (visibilidad) | 3 % | 4 % | 6 % |
| **Conversión** (sign‑ups por clic) | 3 % (45/1 500) | 0,5 % (24/4 800) | 4 % (36/900) |
| **Coste total del mes** | $2 100 | $1 800 | $3 200 |

### Interpretación rápida
- **Campana A**: equilibrio perfecto entre CTR, CPC y mayor tasa de conversión. El CPA es el más bajo entre las tres.  
- **Campana B**: muy alto CTR y costo unitario de clic bajo, pero la proporción de conversiones al clic es muy baja (solo 0,5 %). Además, el coste por sign‑up ($75) es casi el doble que en A.  
- **Campana C**: aunque tiene el CTR más alto, el coste por clic y por sign‑up es disparado ($3,56 CPC y $88,89 CPA). También apunta a palabras clave de **competidores**, lo que sugiere que atrae clics “no‑conv” o a usuarios que buscan una alternativa ya existente.

### ✅ Recomendación

| Acción | Por qué |
|--------|--------|
| **Escalar Campana A** (y posiblemente añadirle 10‑20 % de presupuesto) | Mejor CPA, CTR sólido y tasa de conversión superior a B y C. Es el canal con mayor retorno por dólar invertido. |
| **Reducir o pausar Campana C** | Costos excesivos y mala eficiencia. Si se mantiene para competir, debe estar con un presupuesto mínimo (ej. $500–$1 000) y con un objetivo muy estricto de CPA. En su estado atual, mejor eliminarla. |
| **Mantener Campana B como canal secundario** | Aunque su conversión por clic es baja, tiene un CPC muy atractivo y un volumen de impresiones alto. Puede complementar A después de ajustar el objetivo de CPA. |

---

## 3️⃣ Redistribución del presupuesto mensual de **$5 000**

Supongamos que queremos mantener la exposición que ya teníamos, pero optimizar la inversión.

| Campana | Presupuesto mensual propuesto | Razón |
|---------|-------------------------------|-------|
| **A** | **$3 500** (≈ 70 % del total) | Prioridad máxima: buen CPA y CTR. Aumentar permite probar cambios creativos y crecer el tráfico. |
| **B** | **$1 500** (≈ 30 % del total) | Conserva un canal de contenido de blog; el CPC sigue bajo, aunque la conversión sea lenta. Se puede enfocar en optimización del texto del post y en llamadas a acción. |
| **C** | **$0 – $500** (opcional) | Eliminar por completo o poner en modo “mínimo” si se desea ahorrar. Si se decide mantener algo, usar solo $500 para intentar capturar clientes potenciales de los términos de competidores (alto riesgo). |

**Total:** $3 500 + $1 500 + $0 = **$5 000**.  

*(Si prefieres mantener un toque en C, simplemente movería los $500 restantes de B a C, quedando: A $3 500, B $1 000, C $500.)*

---

## 4️⃣ A/B Tests sugeridos para el próximo mes

| Experimento | Campana | Variable a probar | Métrica principal a monitorizar |
|-------------|---------|-------------------|-----------------------------------|
| **Variante de encabezado del landing A** | A | “Software de gestión de inventario” → “Gestión inteligente de stock”. | CTR & conversión (sign‑ups). |
| **Botón de llamada a la acción (CTA)** | A | “Sígnate ahora” vs. “Obtén tu cupo gratuito”. | Clicks → sign‑ups. |
| **Formulario de captación** | A | Número de campos (1 vs 3) y tipo (texto vs field de correo + número). | Completitud de formularios → conversión. |
| **Imagen vs. Copy en página de destino** | A | Foto de producto real vs. ilustración. | CTR y CPA. |
| **Test de bidding (manual CPC vs. Target CPA)** | Todos | Para B y C: cambiar bidding a “Target CPA” basado en $46 (meta del A). | Coste por sign‑up y tiempo para alcanzar objetivo. |
| **Ancho de título de blog (B)** | B | Preguntas (“Cómo gestionar inventario?”) vs. frases de solución directa (“Problemas de inventario en restaurantes”). | Clics y sign‑ups del enlace. |
| **Segmentación de audiencia (Look‑Alike)** | B y C | Usar Look‑Alike de clientes existentes vs. público general. | CPA y CTR. |
| **Horizonte temporal** | Todo | Ejecutar los nuevos bidgets durante la segunda semana del mes y comparar resultados diarios. | Ratio de coste por sign‑up (CPA) y reducción de CPA respecto a niveles anteriores. |

**Proceso sugerido**

1. **Diseñar dos versiones** (control vs. variante) con herramientas internas de Google Ads o con un editor de creatividades.  
2. **Seguir los métricas** durante 48 h o 72 h hasta lograr una señal estadísticamente significativa (Δ p ≥ 5 % en CTR o CPA).  
3. **Asignar el presupuesto provisionalmente** según el que supere en CPA o en conversión.  

---

### Resumen rápido

| Acción | Detalle |
|--------|---------|
| **Calcular métricas** | CTR ≈ 3 % (A), 4 % (B), 6 % (C); CPC ≈ $1,40 / $0,38 / $3,56; CPA ≈ $46,7 / $75 / $88,9; Conv. ≈ 3 %, 0,5 %, 4 %. |
| **Escalar** | Campana A (máx CPA bajo, CTR estable). |
| **Pausar/Minimizar** | Campana C (coste desequilibrado, alta competencia). Mantener B como respaldo ligero. |
| **Redistribuir $5 000** | A ≈ $3 500, B ≈ $1 500, C ≈ $0. |
| **Próximos AB tests** | Encabezados, CTA, formato, segmentación, bidding, títulos de blog, etc. |
| **Resultado esperado** | Reduce el CPA de A a los $46‑47, aumenta el volumen de sign‑ups sin gastar más de lo necesario, y libera recursos para experimentar con nuevos formatos de contenido. |

¡Éxito con la optimización! Si necesitas ayuda para configurar bidding o diseñar los nuevos anuncios, dime y lo armamos juntos. 🚀