# Inkling Small — strategy/pricing_strategy

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.58 | quality: 10.0
- latency_total: 71.448s | tokens_per_second: 114.5
- input_tokens: 183 | output_tokens: 8178

## Entrada exacta (lo que recibió el modelo)

**user:**

Mi SaaS de gestion de inventario tiene estos datos:
- CAC actual: $120
- LTV promedio: $840 (14 meses * $60/mes)
- Churn mensual: 7%
- 200 clientes actuales
- Competidores cobran entre $29 y $149/mes
- Mi costo por usuario es ~$8/mes

Estoy considerando subir el precio de $60 a $89/mes.
Analiza:
1. Calcula el LTV/CAC ratio actual y como cambiaria
2. Estima el impacto en churn (usa benchmarks de la industria SaaS)
3. Modela 3 escenarios: optimista, realista, pesimista
4. Dame tu recomendacion con numeros concretos
5. Sugiere una estrategia de implementacion (grandfather, gradual, etc)


## Respuesta completa

Aquí tienes el análisis completo con números concretos. **El resumen inicial:** tu LTV/CAC actual es excelente (7x), pero tu **churn mensual del 7% es el verdadero problema** (equivale a ~58% de pérdida anual). Subir el precio un 48% puede funcionar como “filtro de calidad”, pero si no lo haces con cuidado, destruirás tu base antes de que el beneficio se consolide.

---

### 1. LTV / CAC: Actual vs. con $89/mes

| Métrica | Actual ($60) | Nuevo ($89) – sin cambio de churn | Notas |
|---|---|---|---|
| **Precio** | $60 | $89 | +48,3% |
| **Costo/usuario** | ~$8 | ~$8 | Margen bruto: 87% → 91% |
| **Churn mensual** | 7% | *Variable* (ver 2) | Vida media = 1/0.07 ≈ **14,3 meses** |
| **Vida media** | ~14,3 meses | Depende del nuevo churn | Si sube a 11% → ~9 meses |
| **LTV bruto** (tu método) | **$840** (14×60) | **$1.246** (14×89) si se mantiene churn | Realista: **$809** (9×89) |
| **LTV/CAC** | **7,0x** ($840/$120) | **10,4x** (si churn se mantiene) | Realista (~11%): **6,7x** |
| **LTV/CAC con margen** (precio – $8) | **~6,2x** ($743/$120) | **~8,4x** (optimista) | Realista: **~6,1x** |

**Conclusión del punto 1:** Tienes colchón. Incluso si el churn sube a 11% (escenario realista), tu ratio se mantiene cerca del actual (~6,7x). **El riesgo no es el ratio, es la velocidad de quemado de tu base de clientes.**

---

### 2. Impacto en churn: benchmarks de la industria

Tu churn mensual de **7% es muy alto para SaaS B2B** (el “healthy” suele ser <2-3% mensual; >5% es zona de alerta).

**Cómo afecta una subida del 48% sin cambiar el producto:**
- **Regla de elasticidad B2B SaaS:** un salto de precio >30% sin aumento de valor percibido suele incrementar el churn absoluto en **2 a 5 puntos**.
- **Benchmark específico (inventario/ERP PYME):** los clientes de inventario son sensibles al precio (alternativas en $29-$149). Un salto de $60→$89 los empuja al límite superior del rango “básico” y al inferior del rango “pro”.
- **Efecto “filter”:** a veces un aumento de precio *reduce* el churn a largo plazo porque expulsas a clientes de baja rentabilidad (alto costo de soporte, baja adopción). Pero a corto plazo produce una **pérdida inmediata de 10-25% de la base** si no hay transición.

**Estimación de nuevo churn:**
- **Optimista:** 7% → **8-9%** (clientes de valor se quedan, pierdes solo los más sensibles).
- **Realista:** 7% → **10-11%** (el salto es fuerte, muchos evalúan competencia).
- **Pesimista:** 7% → **14-16%** (el producto no justifica el salto, empiezan a migrar a alternativas).

---

### 3. 3 escenarios modelados (200 clientes base, salto inmediato a $89)

Asumimos que todos los actuales reciben el nuevo precio hoy y luego operan con el nuevo churn.

| Métrica | **Actual** | **Optimista** ($89, 8%) | **Realista** ($89, 11%) | **Pesimista** ($89, 15%) |
|---|---|---|---|---|
| **MRR inicial** | $12.000 | **$17.800** (+48%) | **$17.800** (+48%) | **$17.800** (+48%) |
| **Churn mensual** | 7% | 8% | 11% | 15% |
| **Vida media** | 14,3 meses | 12,5 meses | 9,1 meses | 6,7 meses |
| **LTV bruto** | $840 | **$1.113** | **$809** | **$596** |
| **LTV / CAC** | 7,0x | **9,3x** | **6,7x** | **5,0x** |
| **Clientes mes 12** | ~84 | ~66 | ~44 | ~28 |
| **MRR mes 12** | $5.016 | $5.870 | $3.920 | $2.492 |
| **Ingresos acumulados 12m** | **~$100k** | **~$141k** (+41%) | **~$122k** (+22%) | **~$102k** (+2%) |

**Interpretación clave:**
- **Optimista:** Ganas dinero y mantienes salud. Perfecto.
- **Realista:** Ganas +22% en ingresos a 12 meses, **pero pierdes casi la mitad de tu base** (200 → 44). Eso destruye el valor del negocio si buscas levantar ronda o vender.
- **Pesimista:** A 12 meses ganas casi lo mismo ($102k vs $100k), pero tu empresa pasó de 200 a 28 clientes. **Es un desastre estratégico**, aunque el flujo de caja del primer año sea similar.

> **Regla de oro:** Puedes tolerar una pérdida inmediata de hasta ~18% de clientes (pasar de 200 a ~164) con churn 11% y aún así igualar tus ingresos acumulados a 12 meses. Si pierdes más de eso, la subida te perjudica a corto plazo.

---

### 4. Recomendación con números concretos

**No subas a $89 de golpe para todos.** Tu CAC ($120) y tu margen ($52) te permiten ser más inteligentes.

**Mi recomendación híbrida:**
1. **Nuevo precio para nuevos clientes:** **$79/mes** (subida del 32%, más defensible vs. competencia $149).
2. **Tier Pro a $89:** Lanza una versión “Pro” a **$89/mes** con 2-3 funciones nuevas (ej. integraciones con Shopify/QuickBooks, reportes de rotación de inventario, soporte prioritario). Así el salto no es “más caro por lo mismo”, es “más valor”.
3. **Grandfathering a existentes:** Mantén a los 200 actuales a **$60 por 6 meses** (o hasta que renueven), luego migración gradual a **$79** (no $89). Esto evita el shock de cancelación inmediata.
4. **Si insistes en $89:** Solo para nuevos, o con contrato anual a **$79/mes equivalente** ($948/año vs $1.068/año) para mejorar cash flow.

**Números de impacto si haces $79 (no $89) con churn 9%:**
- LTV bruto: $79 × 11,1 meses = **$876** → LTV/CAC = **7,3x**.
- MRR inicial: $15.800 (+32%).
- Ingresos 12m (churn 9%): ~$136k (+36%) con base de ~55 clientes al mes 12.
- **Es más seguro y menos arriesgado que $89.**

**Si vas directo a $89:** Asegúrate de que **el churn no supere 10%**. Cada punto de churn por encima de 10% te resta ~$89 de LTV y te acerca al escenario realista de destrucción de base.

---

### 5. Estrategia de implementación (paso a paso)

No hagas un “email de aumento de precio” universal.

| Fase | Acción | Detalle / Número |
|---|---|---|
| **Semana 1-2** | **Segmentar** | Divide los 200 clientes: los top 20% (que pagan a tiempo, usan más, pagan anual) vs. el 80%. Solo ofréceles el upgrade primero. |
| **Semana 3** | **Grandfathering** | Comunicá a los 200 actuales: “Tu precio se mantiene a $60 hasta [fecha, ej. 6 meses], luego $79 (o $89 si aceptan Pro)”. **No surprises.** |
| **Semana 4** | **Lanzar tier Pro a $89** | Creá una página de precios con 2 planes: Básico ($60/$79) y Pro ($89). Agregá 2 features que justifiquen el salto (ej. “multi-ubicación” o “API de inventario”). |
| **Mes 2** | **Oferta de upgrade con descuento anual** | Ofrecé a actuales: “Subí a $89 pero pagá anual y te cuesta $79/mes ($948/año)”. Esto mejora tu cash flow y reduce churn (compromiso anual). |
| **Mes 3-6** | **Subida gradual de nuevos** | Todos los nuevos entran a $79 o $89 según el plan. |
| **Mes 6-9** | **Migración de grandfathered** | Los que no migraron a $79 (o $89) reciben última oferta con descuento del 10% por 3 meses. Si no aceptan, permiten cancelación sin penalización (evita resentimiento y churn violento). |

**Táctica específica para inventario:** Como tu costo por usuario es ~$8 y tu precio actual es $60, **tienes margen para regalar 1 mes** o dar “2 meses al precio viejo” como incentivo al upgrade anual.

---

### Resumen ejecutivo para tu decisión

| Pregunta | Respuesta numérica |
|---|---|
| ¿El LTV/CAC mejora? | Sí, **si el churn no sube más de 2-3 puntos**. Si sube a 11%, se mantiene similar (6,7x). |
| ¿Gano más dinero a 12 meses? | **Sí**, incluso con churn 15% ganas +2% acumulado, pero con **mucho menos clientes**. |
| ¿Cuál es el riesgo real? | **Destrucción de la base**: pasar de 200 a 28-44 clientes. Eso mata el crecimiento futuro y tu valoración. |
| ¿Qué precio recomiendo? | **$79 para básico / $89 para Pro con features nuevas**, no $89 plano. |
| ¿Cuál es la implementación más segura? | **Grandfathering 6 meses + tier Pro + upgrade anual con descuento**. |

**Número final:** Si lográs que el churn mensual con el nuevo precio sea **≤10%**, la subida es ganadora (LTV/CAC ~7x, +22-41% ingresos acumulados). Si el churn salta a **>12%**, estás destruyendo tu activo de clientes por una ganancia de flujo de caja temporal. **Controla el churn primero, luego sube el precio con una historia de valor, no con un aumento de tarifa.**

¿Querés que te arme el modelo Excel de los 12 meses con tu base real de clientes (y el % que pagó anual vs. mensual)? Te paso la fórmula para que lo simules tú mismo con tu churn exacto por cohortes.