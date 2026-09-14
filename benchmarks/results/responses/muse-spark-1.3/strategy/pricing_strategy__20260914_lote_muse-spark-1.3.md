# Muse Spark 1.3 — strategy/pricing_strategy

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.47 | quality: 10.0
- latency_total: 35.719s | tokens_per_second: 113.9
- input_tokens: 176 | output_tokens: 4067

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

Tu subida de $60 a $89 es un +48.3%. Es agresiva, pero con tus números tienes muchísimo margen de seguridad. Vamos por partes.

### 1. LTV/CAC actual vs. nuevo

Tu cálculo actual es LTV bruto (sin costos):

**Actual:**
LTV = $60 x 14.29 meses (1 / 7% churn) = ~$857. Tú usas $840, lo mantenemos.
LTV/CAC = 840 / 120 = **7.0**

Eso es excelente. El benchmark SaaS sano es >3.0. Estás muy por encima.

Payback CAC: 120 / (60-8) = **2.3 meses**. Brutal, lo normal es 5-12 meses.

**Si subes a $89 SIN que suba el churn:**
Nuevo LTV = $89 x 14.29 = $1,271
Nuevo LTV/CAC = 1,271 / 120 = **10.6**

Pero eso nunca pasa. El churn SIEMPRE sube. Lo importante es calcular el LTV *neto* (con tu costo de $8):

LTV Neto = (ARPA - Costo) / Churn

Actual Neto = (60-8) / 0.07 = 52 / 0.07 = **$742.8**
Ratio Neto = 742.8 / 120 = **6.19**

Punto de equilibrio: Para que el LTV neto no empeore necesitas:
81 / Churn_nuevo > 742.8 => **Churn_nuevo < 10.9%**

Mientras tu churn no pase de 10.9%, ganas dinero con la subida aunque pierdas vida útil del cliente.

### 2. Impacto estimado en churn

Benchmarks industria (ProfitWell, ChartMogul, OpenView para SMB SaaS):

1.  Churn mensual 7% ya es alto. Promedio SMB es 5-7%, SaaS mid-market bueno es 2-3%. Estás en el límite alto, lo que indica sensibilidad al precio o falta de stickiness.
2.  Elasticidad SaaS SMB: por cada 10% de subida de precio, espera +0.5 a +1 punto porcentual de churn logo en los 3 meses siguientes si no agregas valor.
3.  Subida de +48% sin justificación de valor = típicamente +2 a +5pp de churn y 15-30% de pérdida de logo base.

Tu posicionamiento te ayuda: Competidores $29 - $149. Estás en $60 (tercio bajo). Ir a $89 te pone justo en el medio-premium, no te saca del mercado.

Mi estimación para ti:
Optimista: 7% -> 8%
Realista: 7% -> 9.5-10%
Pesimista: 7% -> 12%+

### 3. Modelo de 3 escenarios (a 90 días)

Base actual: 200 clientes x $60 = **$12,000 MRR / $144,000 ARR**
Profit mensual actual: 200 x (60-8) = **$10,400**

| Escenario | Churn nuevo | Clientes que se van | Clientes finales | Nuevo MRR | LTV bruto / Ratio | Profit mensual |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Optimista** | 8.0% (vida 12.5m) | -10 (5%) | 190 | **$16,910 (+40.9%)** | $1,112 / 9.27 | **$15,390 (+48%)** |
| **Realista** | 10.0% (vida 10m) | -30 (15%) | 170 | **$15,130 (+26.1%)** | $890 / 7.42 | **$13,770 (+32.4%)** |
| **Pesimista** | 12.0% (vida 8.3m) | -60 (30%) | 140 | **$12,460 (+3.8%)** | $741 / 6.18 | **$11,340 (+9%)** |

Dato clave: **Tu break-even es 135 clientes.**
12,000 / 89 = 134.8. Puedes perder hasta **65 clientes (32.5%)** y seguir facturando lo mismo, pero con menos costos de soporte.

Incluso en el pesimista, tu LTV/CAC sigue siendo 6.18 (>3) y ganas +$940/mes extra de profit.

Ojo con el CAC: a $89 convertirás peor. Si tu conversión cae 20%, tu CAC efectivo sube de $120 a ~$150. Aún así en escenario realista: 890 / 150 = 5.93. Sigues sano.

### 4. Mi recomendación con números

**SÍ, sube. Pero NO a $89 plano para todos. Haz $89 para nuevos y $79 transitorio para actuales.**

Por qué: Una subida de 48% de golpe a tu base con 7% de churn es provocar al churn. El riesgo no es el MRR, es la reputación y reviews.

Mi jugada concreta:
1.  Precio nuevo oficial: **$89/mes pago mensual, $69/mes pago anual ($828/año)**
2.  Esperando el escenario realista: pasas de $12,000 a **~$15,130 MRR**. Son **+$3,130 MRR / +$37,560 ARR** al año, atendiendo a 30 clientes menos.
3.  Tu LTV/CAC neto pasaría de 6.19 a 6.75. No es espectacular, pero tu payback baja a 1.48 meses y liberas caja.

No hagas un solo plan de $89. Lanza 3 tiers Good-Better-Best para capturar a los que se iban a ir:
Starter $49 (limita usuarios/almacenes), Pro $89 (tu plan actual), Plus $149 (multi-sucursal, API). El 70% se quedará en Pro, pero retienes al segmento sensible en $49 en vez de perderlos a un competidor de $29.

### 5. Estrategia de implementación (90 días)

No hagas subida directa. Haz **Grandfather Temporal + Ancla Anual.**

**Días 1-30: Valida sin riesgo**
1.  Sube a $89 SOLO para clientes nuevos desde mañana. Mide conversión trial->pago durante 3 semanas. Si cae >25%, tu precio es $79, no $89.
2.  Envía encuesta Van Westendorp a 30 clientes top: "¿A qué precio sería caro pero lo pagarías?"

**Días 31-60: Comunica (60 días de aviso)**
Email + in-app, nunca solo factura. Fórmula:
> "En 12 meses lanzamos X, Y, Z [tienes que lanzar 1 feature real de inventario]. Para seguir invirtiendo, Pro pasa de $60 a $89 el [Fecha +60 días]. Como cliente fundador, tienes 2 opciones..."

Opción A (retención): Quédate en $60 por 12 meses más si pasas a plan anual hoy ($720 por adelantado). Mejoras tu cash-flow y bloqueas churn por un año.
Opción B (transición): Paga $79/mes durante 6 meses, luego $89.

Esto convierte una subida del 48% en dos subidas psicológicamente aceptables: 31% y luego 12%.

**Días 61-90: Migra**
1.  Aplica grandfather automático de 6 meses a $79. No pidas que hagan clic para aceptarlo.
2.  Monitorea diario: Churn logo, tickets con palabra "precio/cancelar", NPS. Si el churn mensual supera 11% en la semana 2, pausa y extiende el grandfather a 12 meses.
3.  A tu equipo de soporte dale un script con descuento de salvamento: ofrecer 3 meses a $60 para quien amenace con irse. Es más barato que perderlos.

Lo que NO debes hacer: grandfather de por vida. Te crea deuda técnica de facturación y castigas a tus mejores clientes nuevos. 6-12 meses es suficiente para que el enojo pase.

**TL;DR:** Tienes colchón para perder 1 de cada 3 clientes y aún así empatar. El escenario más probable te da +26% MRR. Lanza $89 para nuevos ya, y migra a los actuales con grandfather de 6 meses a $79 + opción anual a $69.