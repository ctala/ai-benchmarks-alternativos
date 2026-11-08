# Muse Spark 1.3 — strategy/pricing_strategy

- model_id: `meta/muse-spark-1.3`
- success: True  | final: 8.41 | quality: 10.0
- latency_total: 43.987s | tokens_per_second: 120.4
- input_tokens: 177 | output_tokens: 5294

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

Tu aumento planteado es de **$60 a $89 = +48.3%**. No es un ajuste, es un reposicionamiento. Con tus números sí tiene sentido, pero no lo hagas de golpe.

Aquí va el análisis completo:

### 1. LTV/CAC actual vs. nuevo

Tu cálculo de LTV es correcto en lógica:
Vida esperada = 1 / Churn = 1 / 0.07 = **14.29 meses**

**Actual ($60):**
LTV ingresos = 14.29 * $60 = **$857** (tu dices $840, diferencia por redondeo)
LTV bruto real = (60-8) * 14.29 = 52 * 14.29 = **$743**
LTV/CAC ingresos = 857 / 120 = **7.14**
LTV/CAC bruto = 743 / 120 = **6.19**

Benchmark SaaS: >3 es bueno, >5 es excelente. Estás sobrado. Tu CAC payback es de solo 120/52 = **2.3 meses**. Eso grita *underpricing*.

**Si subes a $89 y el churn NO cambiara:**
Vida = 14.29 meses
LTV ingresos = 14.29 * 89 = **$1,271**
LTV bruto = (89-8) * 14.29 = 81 * 14.29 = **$1,157**
LTV/CAC ingresos = 1,271 / 120 = **10.6**
LTV/CAC bruto = 1,157 / 120 = **9.64**
Payback bajaría a 120/81 = **1.48 meses**

El problema: el churn SÍ va a subir. La pregunta es cuánto.

Hay un número crítico que debes memorizar:
**Churn de break-even = 0.07 * (89/60) = 10.38%**

Si tu churn mensual nuevo queda por debajo de **10.38%**, el LTV sube. Si queda por encima, destruyes valor aunque cobres más.

Otro número crítico para el corto plazo:
Para no perder MRR el día 1, necesitas retener: 60/89 = **67.4%** de clientes.
Puedes permitirte perder hasta **32.6% de logos de golpe** y seguir con el mismo MRR ($12,000).

### 2. Impacto estimado en churn (benchmarks)

Tu churn de 7% mensual ya es alto.
Benchmarks 2023-2024 (OpenView, ChartMogul, Baremetrics, Paddle/ProfitWell):
- SMB SaaS como el tuyo: 6-8% mensual logo churn. Estás en el límite alto.
- Mid-Market: 3-4%
- Enterprise: 1.5-2.5%
- Retención anual de logos implícita tuya: 0.93^12 = 41.9%. O sea, pierdes 58% de clientes al año. Best-in-class SMB retiene 65-75%.

Qué pasa con subidas de precio según ProfitWell/Paddle:
- Subida <20% + comunicación de valor: +0.5 a +1pp de churn
- Subida 20-30% sin nada nuevo: +1.5 a +2.5pp de churn
- Subida >40% sin grandfather ni features nuevas: spike inmediato de 15-25% de cancelaciones + churn permanente 2-4pp más alto

Tu caso es +48.3% en gestión de inventario (producto sticky, con costo de cambio medio-alto, pero con competidores de $29). Elasticidad típica SMB B2B: -1.0 a -1.5.

Mi estimación: tu churn permanente pasará de 7% a **9-10%** si lo comunicas bien, a **12-13%** si lo haces mal.

Por eso no recomiendo el salto directo.

### 3. Modelo de 3 escenarios (cohorte actual de 200 clientes, 12 meses)

MRR actual: 200 * 60 = **$12,000**
Ingreso 12 meses cohorte actual sin subida: 60*200*(1-0.93^12)/0.07 = **$99,660**

| Escenario | Supuesto Churn Nuevo | Vida (meses) | LTV ingresos | LTV/CAC | Ingreso 12m cohorte | vs Base |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Optimista** | 7% -> **8.5%** (+1.5pp). Añades valor, grandfather, comunicas perfecto. | 11.76 | $1,047 | 8.72 | **$138,002** | +38.5% |
| **Realista** | 7% -> **10.0%** (+3pp). Lo normal para +48% según ProfitWell. | 10.0 | $890 | 7.42 | **$127,727** | +28.2% |
| **Pesimista** | 7% -> **13.0%** (+6pp). Subida brusca, sin aviso, competidor $29 te canibaliza. | 7.69 | $685 | 5.70 | **$111,179** | +11.6% |

Incluso en el pesimista ganas más caja en 12 meses, **pero destruyes la base**: terminas el año con 38 clientes de los 200 iniciales vs. 84 si no hacías nada. Y tu adquisición nueva también caerá 20-30% en conversión por el precio más alto.

En LTV bruto (descontando $8 costo):
Optimista: 7.94, Realista: 6.75, Pesimista: 5.19. Todos >3, por eso el negocio aguanta, pero el realista/pesimista te deja con un churn de 10-13% que es insostenible a largo plazo.

### 4. Mi recomendación con números

**No hagas $60 -> $89 para todos el día 1. Haz $60 -> $89 solo para nuevos + arquitectura de 3 planes.**

Tu precio de $89 te pone en el percentil 65 del mercado ($29-$149). Es defendible si eres mejor que el de $29, pero necesitas justificarlo. El salto de 48% activa "price shock".

Recomendación concreta:

**Fase 1 (Día 1-180): Price fence**
1. Crea 3 tiers: **Starter $49 (limitado), Pro $89 (tu producto actual completo), Business $149 (multi-sucursal + API + soporte prioritario)**
2. Nuevos clientes: entran directo a $49 / $89 / $149.
3. Clientes actuales (200): grandfather a $60 por 6 meses. MRR se mantiene en $12,000.

**Fase 2 (Mes 7): Migración incentivada**
Ofrece: quédate en Pro $89 mensual O congela $69/mes si pagas anual por adelantado ($828/año). Es un +15% para ellos, no +48%, y mejoras tu cash.

Si el 70% acepta anual a $69 y 30% se va a $89 o se va (churn):
MRR equivalente: 140 clientes * $69 + 30 clientes * $89 = $9,660 + $2,670 = $12,330 con solo 170 clientes. Ya superas tu MRR actual con menos soporte. Y tu churn realista se queda en ~8.5-9% en vez de 10-13%.

Mi proyección con esta estrategia: **+$28k a +$38k de ARR incremental en 12 meses** con churn contenido en 8.5-9.5%, LTV/CAC ~7.5-8.0 y payback <2 meses. Te permite reinvertir en adquisición.

Si insistes en $89 plano para todos sin tiers: espera perder 40-60 logos en los primeros 60 días (20-30%). MRR mes 1: 150*89 = $13,350 (+11%). Ganas MRR pero pierdes NPS y referrals, que con CAC $120 son tu motor.

### 5. Estrategia de implementación (90 días)

No uses "subida gradual de $2 al mes". Usa **Grandfather + Value + Choice**:

**Días 1-30: Preparar valor**
No puedes subir 48% sin dar nada. Empaqueta 1-2 features que te cuesten poco ($8 de costo te da margen) pero con alta percepción: reportes de stock bajo por WhatsApp, multi-usuario, exportación contable. Esas van SOLO a Pro $89. El plan $49 no las tiene. Creas arrepentimiento por no subir.

Haz 15-20 llamadas Jobs-to-be-Done: "¿A qué precio sería tan barato que dudarías de la calidad? ¿Tan caro que no lo considerarías?" (Van Westendorp). Valida que $89 no esté fuera.

**Días 31-60: Test solo en nuevos**
Cambia pricing page a $49/$89/$149 solo para 50% del tráfico. Mide: conversión trial->pago y CAC. Si tu conversión cae >35%, tu $89 está mal posicionado. Mi apuesta: caerá 15-20%, aceptable porque ARPA sube 48%.

**Día 61: Anuncio con 60 días de aviso**
Email + in-app + llamada a top 20 cuentas. Guion: no hables de costos. Habla de: "En 12 meses lanzamos X, Y, Z. Para seguir invirtiendo, Pro pasa a $89 desde [fecha +60 días]. Como cliente fundador, tienes 6 meses a $60 y luego puedes bloquear $69 anual de por vida si renuevas antes de [fecha]."

**Día 61-120: Ventana de grandfather**
Dashboard con cuenta regresiva. Ofrece migración asistida al anual. Tu objetivo: convertir >60% de base a anual $69 antes del mes 6. El anual mata el churn mensual.

**KPIs a vigilar semanal:**
1. Logo churn mensual (alarma si >11% dos meses seguidos -> pausa migración)
2. Revenue churn vs. Expansion (quieres Net Revenue Retention >95% aun con churn)
3. Trial conversion nuevos (alarma si cae de, ej, 12% a <8%)
4. Tickets "precio/cancelar" y NPS
5. CAC payback nuevos (debería mantenerse <3 meses)

Regla de kill-switch: Si pierdes >25% de base en 30 días post-migración, extiende grandfather 3 meses más y ofrece $79 intermedio.

En resumen: tu unit economics te permite subir. El math dice que hasta con churn de 10% ganas. Pero con churn base de 7% ya alto, un salto de 48% sin tiers es imprudente. Ve a $89 para nuevos mañana, protege a los 200 actuales con 6 meses de grandfather + anual a $69, y crea un $49 como parachoques contra el competidor de $29.