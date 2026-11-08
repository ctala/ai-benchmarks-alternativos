# Muse Glimmer 30B — strategy/pricing_strategy

- model_id: `meta/muse-glimmer-30b`
- success: True  | final: 8.69 | quality: 10.0
- latency_total: 25.153s | tokens_per_second: 145.7
- input_tokens: 225 | output_tokens: 3665

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

Con esos números hoy estás muy sano pero con churn alto. El LTV que usas es bruto.

**1. LTV/CAC actual y con precio a $89**

Actual:
LTV bruto = 14 meses x $60 = $840
LTV neto = 14 x [$60 - $8] = 14 x $52 = $728
LTV/CAC bruto = 840 / 120 = **7.0**
LTV/CAC neto = 728 / 120 = **6.07**
Payback = CAC / margen mensual = 120 / 52 = 2.3 meses

Con $89 y sin cambio de churn:
LTV bruto = 14 x $89 = $1,246  -> LTV/CAC = 10.38
LTV neto = 14 x $81 = $1,134  -> LTV/CAC neto = 9.45
Payback = 120 / 81 = 1.48 meses

El problema es el churn. Con 7% mensual tu vida media real es 1/0.07 = 14.3 meses. Ya estás en el límite alto del SMB SaaS, benchmark 5-7% mensual.

**2. Impacto esperado de churn por subida de precio**

Una subida del +48.3% de $60 a $89 en SMB SaaS típicamente:
* Spike de cancelación en los 30-60 días siguientes: +15 a +40% sobre churn base
* Churn estabilizado +15 a +70% vs base según valor percibido y comunicación

Con tu churn base de 7% eso es 8% a 12% mensual estabilizado.

**3. Modelado 3 escenarios, CAC constante $120**

Asumo churn estabilizado y margen $81/mes.

**Optimista**
Churn 7.5% mensual +7%
Vida media = 1/0.075 = 13.33 meses
LTV bruto = 89 x 13.33 = $1,187
LTV/CAC = 1,187 / 120 = **9.89**
LTV neto = 81 x 13.33 = $1,080
MRR de la cohorte de 200 actuales tras 12 meses = 200 x 89 x 0.925^12 = $6,558 vs $5,016 sin subida

**Realista**
Churn 9.5% mensual +36%
Vida media = 1/0.095 = 10.53 meses
LTV bruto = 89 x 10.53 = $937
LTV/CAC = 937 / 120 = **7.81**
Con CAC +20% por menor conversión = $144 -> LTV/CAC = 6.51
LTV neto = 81 x 10.53 = $853
MRR cohorte tras 12 meses = 200 x 89 x 0.905^12 = $5,398

**Pesimista**
Churn 12% mensual +71%
Vida media = 1/0.12 = 8.33 meses
LTV bruto = 89 x 8.33 = $741
LTV/CAC = 741 / 120 = **6.18**
Con CAC +35% = $162 -> LTV/CAC = 4.57
LTV neto = 81 x 8.33 = $675
MRR cohorte tras 12 meses = 200 x 89 x 0.88^12 = $3,933

Incluso en pesimista sigues >3x, el umbral de salud es 3x y >5x es excelente.

**4. Recomendación con números**

Sí sube, pero no a todos a la vez. El realista te deja LTV/CAC ~6.5-7.8 y payback <2 meses, con margen bruto del 91% vs 86% actual.

El riesgo real no es el precio, es tu churn base de 7%. Con 7% anualizas al 58% de pérdida. Cada punto de churn que bajes vale más que la subida de precio.

Acción recomendada: sube a $89 para nuevos clientes ya y prueba $79 como precio de transición para existentes.

Si mantienes churn en 9.5% realista, cada 200 clientes nuevos te generan:
LTV total = 200 x $937 = $187,400
Costo adquisición = 200 x $144 = $28,800
Contribución neta = $158,600 vs $145,600 actuales.

**5. Estrategia de implementación**

No hagas hard cut. Con 200 clientes actuales:

* **Grandfather + precio nuevo:** Los 200 actuales quedan en $60 12 meses con plan Legacy. Nuevos clientes entran en $89 desde hoy. Comunicación de valor 30 días antes.
* **Escalera para existentes:** A los 12 meses ofrece migración voluntaria a $79 con 2 meses gratis si pagan anual. A los 18 meses $89.
* **Anclaje de valor:** Lanza 3 tiers ahora: Starter $49, Pro $89 con inventario multi-almacén y API, Business $149. El $60 actual se mapea a Pro legacy.
* **Mitigación de churn:** En los 60 días post anuncio activa plan de éxito: onboarding 1:1, reporte de uso, descuento anual 2 meses gratis para bloquear churn. Objetivo bajar churn spike < 10%.
* **Métricas de kill switch:** Si churn de la cohorte legacy sube >10% mensual durante 2 meses consecutivos o cancelaciones por precio >25% del churn, congela la subida y activa retención.

Con esto capturas el +48% de ARPU sin sacrificar la base y mantienes LTV/CAC >6x en el escenario realista.