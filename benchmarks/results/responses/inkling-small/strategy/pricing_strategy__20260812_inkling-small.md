# Inkling Small — strategy/pricing_strategy

- model_id: `thinkingmachines/inkling-small`
- success: True  | final: 8.29 | quality: 10.0
- latency_total: 160.252s | tokens_per_second: 46.7
- input_tokens: 183 | output_tokens: 7488

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

Tu caso es interesante porque **el precio no es el problema principal: el churn de 7% mensual sí lo es** (equivale a ~58% anual). Eso significa que, de tus 200 clientes, en 12 meses solo quedarán ~84 si no mejoras retención.

Sin embargo, la matemática de subir a **$89** es favorable si haces la transición con inteligencia.

---

### 1. LTV/CAC Actual vs. Nuevo Precio

Usaré tu fórmula (LTV = ARPU × Vida media) y luego el margen bruto.

| Métrica | Actual ($60) | Nuevo ($89) – Churn 7% | Nuevo ($89) – Churn 10% | Nuevo ($89) – Churn 12% |
|---|---|---|---|---|
| **ARPU** | $60 | $89 | $89 | $89 |
| **Churn mensual** | 7% | 7% | 10% | 12% |
| **Vida media** | 14.3 mes | 14.3 mes | 10.0 mes | 8.3 mes |
| **LTV (Ingresos)** | **$840** | **$1,271** | **$890** | **$742** |
| **LTV/CAC** | **7.0x** | **10.6x** | **7.4x** | **6.2x** |
| **Margen bruto/mes** | $52 ($60-$8) | $81 ($89-$8) | $81 | $81 |
| **LTV (Margen)** | ~$743 | ~$1,156 | ~$810 | ~$673 |
| **LTV/CAC (Margen)** | **6.2x** | **9.6x** | **6.8x** | **5.6x** |

**Insight clave:**  
Para que tu LTV **baje** respecto al actual ($840), tu churn mensual debe saltar de **7% a más de 10.6%**. Es decir, puedes permitirte que el churn suba **3.6 puntos porcentuales absolutos** y aún así ganar más valor por cliente.

---

### 2. Impacto Estimado en Churn (Benchmarks SaaS B2B)

- **Tu posición de mercado:** $60 está en el 25% inferior del rango de competidores ($29-$149). $89 te coloca en el percentil ~60-70. No eres el más caro, pero dejas de ser barato.
- **Elasticidad:** En SaaS B2B de nicho (inventario), si el cliente usa el producto diariamente, la demanda es **inelástica**. Una subida del 48% suele aumentar el churn absoluto en **1.5 a 3.5 puntos** si no hay valor añadido; si solo es "subida de precio", puede ser **3 a 6 puntos**.
- **Tu riesgo real:** Con 7% ya existente (muy alto para B2B), tu base es sensible. Un shock de precio podría acelerar la salida de clientes que ya estaban "en la cuerda floja".

**Regla práctica:**  
Si subes 48% sin añadir valor, espera que el churn mensual suba a **9-11%**. Si subes 48% **y lanzas un tier Pro con nuevas funciones**, puedes contenerlo en **7-8.5%**.

---

### 3. Modelado: 3 Escenarios (Base de 200 clientes)

Asumo un **"choque inicial"** (clientes que cancelan inmediatamente por la noticia del aumento) y luego el churn mensual estabilizado.

| Escenario | Shock inicial | Churn mensual | Clientes Mes 1 | Clientes Mes 6 | Ingresos Mes 6 | LTV | LTV/CAC | vs. Actual Mes 6* |
|---|---|---|---|---|---|---|---|---|
| **Optimista** | -5% (10 clientes) | 6.5% | 190 | ~135 | **$12,015** | $1,371 | 11.4x | **+43%** |
| **Realista** | -15% (30 clientes) | 9.5% | 170 | ~104 | **$9,256** | $936 | 7.8x | **+10%** |
| **Pesimista** | -30% (60 clientes) | 14.0% | 140 | ~66 | **$5,874** | $635 | 5.3x | **-30%** |

*\*Actual (sin cambio): 200 clientes → ~140 clientes mes 6 por churn 7% → $8,400/mes.*

**Interpretación:**
- **Optimista:** El filtro de precio atrae clientes más serios; mejoras soporte con el flujo extra; el churn baja.
- **Realista:** Pierdes 30 clientes de golpe, pero los 170 restantes pagan 48% más. En mes 6 ganas un 10% de ingresos totales con menos clientes (más margen, menos soporte).
- **Pesimista:** El shock es brutal (60 clientes) y el churn se dispara. El LTV ($635) cae por debajo del actual. **Esto pasa si subes el precio sin explicar el valor ni ofrecer alternativas.**

---

### 4. Recomendación con Números Concretos

**Sí, sube a $89, pero no de golpe y no para todos al mismo tiempo.**

**Por qué es seguro hacer la subida:**
1. **Margen de seguridad alto:** Puedes soportar que el churn suba hasta **10.6%** sin perder LTV.
2. **Posición de mercado:** $89 está dentro del rango competitivo y por debajo del techo ($149).
3. **Margen bruto:** De $52 a $81 por cliente (+55%). Eso te da $29/mes adicionales para invertir en retención (soporte, onboarding, integración).
4. **CAC bajo:** $120 es muy recuperable. Incluso en el escenario pesimista ($635 LTV) sigues con 5.3x.

**Pero:** Tu churn de 7% es una emergencia. Si subes precios y no mejoras retención, estás acelerando la fuga.

**Plan de acción concreto:**
- **Nuevo precio objetivo:** $89/mes (o $79 con un "upgrade" a $89).
- **Objetivo de retención:** Que tu churn mensual no supere **9%** en los primeros 6 meses tras el cambio.
- **Inversión del incremento:** Usa los $29 extra/cliente para:
  - Un onboarding de 1 hora con el cliente.
  - Una integración rápida (ej. con su ERP o tienda online).
  - Un descuento anual del 20% ($71/mes equivalente) para bajar el churn.

---

### 5. Estrategia de Implementación (Recomendada: Híbrida "Grandfather + Tier")

No uses un "grandfather eterno" (dejas a 200 clientes a $60 para siempre y destruyes tu unidad económica). Usa este plan de 6 meses:

#### Fase 1: Lanzar el tier "Pro" (Mes 1)
- **Nuevo plan "Pro":** $89/mes. Incluye 2-3 funciones que no tiene el actual (ej. reportes de rotación de inventario, integración con Shopify/QuickBooks, soporte prioritario por chat).
- **Plan actual:** Se renombra a "Basic" y se mantiene a **$60**, pero **no recibe las nuevas funciones**.
- **Regla:** Nuevos clientes solo pueden elegir Pro ($89) o Basic ($60) con limitaciones claras.

#### Fase 2: Migración escalonada de los 200 actuales (Mes 2-4)
- **Opción A (recomendada):** "Mantén tu precio de $60 si pagas 12 meses por adelantado hoy". Esto te da **cash flow inmediato** y retiene al cliente.
- **Opción B:** "Migra a Pro a $89 con 20% de descuento los primeros 3 meses" (paga $71/mes temporalmente).
- **Opción C (para los que no quieren pagar más):** Ofrecer subir a $69 primero (subida del 15%), luego a $79 en mes 4, y finalmente a $89 en mes 7.

#### Fase 3: Subida obligatoria con fecha límite (Mes 6-9)
- Comunica: "El plan Basic pasa a $79/mes a partir del 1 de enero de 2026" (o la fecha que corresponda).
- Ofrece un **descuento anual del 20%**: $89 → **$71.20/mes equivalente** ($855/año). Esto reduce el churn y mejora tu flujo de caja.

#### Fase 4: Optimizar con los ingresos extra (Paralelo)
- Usa los $29 adicionales por cliente retenido para **reducir tu churn de 7% a 5%**:
  - Automatiza alertas de inventario bajo.
  - Añade un "customer success" de 30 min al mes para los clientes con >$89.
  - Si logras bajar el churn a 5%, tu LTV a $89 salta a **$1,780** (ratio 14.8x).

---

### Resumen Ejecutivo para tu decisión

| Pregunta | Respuesta |
|---|---|
| ¿Subo a $89? | **Sí**, pero con un tier nuevo y migración escalonada. |
| ¿Cuál es el límite de churn que puedo tolerar? | **10.6% mensual** (si pasa de eso, pierdes valor). |
| ¿Cuál es el escenario más probable? | **Realista:** Pierdes 15-20% de la base inicial, pero los que se quedan generan +48% de ingresos; tu LTV sube a ~$936. |
| ¿Qué hago primero? | **No subas sin lanzar una función o beneficio nuevo** (integración, soporte, reportes). Si subes solo por "inflación", entrarás al escenario pesimista. |
| ¿Cuál es la métrica de éxito en 6 meses? | **Ingresos totales >$14,000/mes** (vs $12,000 actual) con **>130 clientes activos** y **churn <9%**. |

**Tu mayor riesgo no es el precio; es que con 7% de churn mensual tu negocio pierde el 58% de sus clientes cada año.** Usa esta subida de precio como excusa para mejorar el producto y retener, no solo para cobrar más.