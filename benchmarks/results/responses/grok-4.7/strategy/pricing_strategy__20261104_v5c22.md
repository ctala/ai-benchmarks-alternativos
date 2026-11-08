# Grok 4.7 — strategy/pricing_strategy

- model_id: `x-ai/grok-4.7`
- success: True  | final: 8.06 | quality: 10.0
- latency_total: 201.554s | tokens_per_second: 52.4
- input_tokens: 1410 | output_tokens: 10570

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

La subida tiene sentido en clientes nuevos. Forzarla ya sobre los 200 actuales es una apuesta con poca ventaja y mucha varianza. El cuello de botella no es el precio: es un churn del 7% mensual.

## 1. LTV/CAC actual y con $89

Tu LTV de $840 usa 14 meses × $60. Con churn del 7%, la vida media exacta es 1/0.07 = 14,3 meses, así que el LTV de ingreso es $857. La diferencia es pequeña. Lo útil es mirar también margen, porque tu costo es ~$8/usuario.

| Métrica | Hoy ($60) | A $89, mismo churn 7% | A $89, churn 9% |
|---|---:|---:|---:|
| Margen de contribución | $52 (87%) | $81 (91%) | $81 (91%) |
| LTV ingreso | $857 | $1.271 | $989 |
| LTV margen | $743 | $1.157 | $900 |
| LTV/CAC ingreso | **7,1x** | **10,6x** | **8,2x** |
| LTV/CAC margen | **6,2x** | **9,6x** | **7,5x** |
| Payback | 2,3 meses | 1,5 meses | 1,5 meses |

Con tu método (14 × $60 / $120) el ratio actual es **7,0x**.

Benchmark habitual de SaaS: >3x es viable, >5x es fuerte, payback <12 meses es sano y <6 meses es muy bueno en SMB. Tus unit economics de adquisición ya son buenos. El precio no está “roto”.

Lo que sí está roto es la retención: 7% mensual equivale a **~58% de churn anual** y una retención bruta de ~42%. En SMB self-serve, 3–5% mensual ya es alto; por debajo de 3% es más sano. En B2B con algo de switching cost, una retención bruta anual de 80–90% es la zona razonable. Tú estás muy por debajo de eso.

MRR actual: 200 × $60 = **$12.000** ($144k ARR). Pierdes ~14 clientes y ~$840 de MRR al mes solo por churn.

## 2. Impacto esperado en churn

$60 → $89 es **+48%**, no un ajuste chico. $89 cae justo en el punto medio del rango de competidores ($29–$149), así que el precio absoluto es defendible. El salto porcentual, sobre todo para quien ya paga $60, no lo es.

Rangos de planificación (no son leyes; en SMB elástico y con alternativa a $29, usa el lado pesimista):

- Subida del 10–20% con mensaje de valor: a menudo +0–2 puntos de churn mensual, o casi nada si hay grandfather.
- Subida del 25–35% forzada sobre la base: pérdida incremental típica del 8–15% de logos en el trimestre del cambio.
- Subida ~50% forzada, sin más valor y con sustitutos baratos: pérdida del 15–30%+ en el primer mes, y churn estructural 1–4 puntos más alto después.
- Clientes nuevos: no “churnean” el alza; lo que cae es la conversión. Una elasticidad moderada implica −10% a −25% de altas y, por tanto, CAC más alto si el gasto de adquisición no baja.

Regla práctica de ProfitWell y de pricing de SaaS: la mayoría cobra de menos, y un alza moderada casi no mata retención si el valor está claro. +48% sobre la base instalada está fuera de esa zona segura.

Punto de equilibrio solo de MRR, si mañana todos pasaran a $89: puedes perder hasta **33% de clientes** (quedarte con 135) y empatar los $12.000. En margen puedes perder hasta ~36%. Eso parece holgado, pero es un foto única: no incluye CAC más alto, ni churn que se queda elevado, ni que esos logos no vuelven.

## 3. Tres escenarios a 12 meses

Supuesto explícito, porque no diste altas: para tener la base plana en 200 con 7% de churn, hoy entran **~14 clientes/mes**. Todos los escenarios parten de ahí.

**Optimista.** $89 solo para nuevos. Conversión −5% (13 altas/mes), churn de nuevos 6%, CAC ~$126. Los 200 actuales siguen a $60 y al 7%.

- LTV/CAC de nuevos: ~11,8x
- Mes 12: ~84 legacy + ~114 nuevos
- MRR mes 12: ~$5.000 + ~$10.100 = **~$15.100 (+26%)**

**Realista.** Grandfather 12 meses. Nuevos a $89, altas −15% (12/mes), churn de nuevos 7,5%, CAC ~$140.

- LTV ingreso nuevo = $89 / 0,075 = $1.187
- LTV/CAC ≈ **8,4x** (sigue por encima del 7,1x actual)
- Payback ≈ 1,7 meses
- Mes 12: ~84 legacy a $60 + ~97 nuevos a $89
- MRR mes 12: **~$13.700 (+14%)**
- Ingreso del año: ~$164k vs $144k del status quo, **+$20k**, con poco riesgo de un shock en la base

**Pesimista.** $89 obligatorio el mes 1 para todos. Se va ~35% en el primer mes, churn posterior 10–11%, altas −35% (9/mes), CAC ~$185, churn de nuevos 10%.

- LTV/CAC de nuevos ≈ 4,8x (aún >3x, pero el negocio se encoge)
- Mes 12: ~41 legacy + ~65 nuevos, todos a $89
- MRR mes 12: **~$9.400 (−22%)**

Incluso en el pesimista de clientes nuevos, el ratio no se destruye. Lo que destruye valor es empujar la base actual de golpe.

Sensibilidad si el CAC no se mueve ($120) y solo sube el churn al precio nuevo: a 10% mensual el LTV/CAC sigue en ~7,4x; a 12%, ~6,2x; a 15%, ~4,9x. El colchón existe. Se acaba si la conversión cae más de ~40% (CAC hacia $200+) y el churn de nuevos pasa de 10%.

## 4. Recomendación

**Sí sube el precio de lista a $89, solo para clientes nuevos, esta semana. No toques a los 200 actuales durante 12 meses.**

Números que justifican esa decisión, no la subida forzosa:

- Hoy: LTV/CAC 7,1x, payback 2,3 meses, MRR $12.000.
- Caso realista a 12 meses: LTV/CAC de nuevos ~8,4x, payback ~1,7 meses, MRR ~$13.700, unos **+$20k de ingreso en el año**, sin apostar el 33% de la base.
- El caso forzado solo gana de verdad si pierdes menos del ~20% de logos. Con +48% y competidores a $29, no apostaría a eso.
- Si en 4–6 semanas la conversión de nuevos cae más de 20–25%, no insistas: baja el lista a **$79** (+32%). A $79 y churn 7,5%, LTV ≈ $1.053 y el ratio sigue cómodo, con menos elasticidad.
- No bajes hacia $29. A $29 el LTV de ingreso con 7% de churn es ~$414 y el LTV/CAC cae a ~3,5x antes de contar un CAC peor. El piso del mercado no es tu estrategia.

La palanca mayor no es el precio. Bajar el churn de 7% a 5% alarga la vida de 14 a 20 meses y sube el LTV de $60 de $857 a $1.200 (ratio ~10x) sin perder un logo por precio. Un plan anual con 15–20% de descuento suele ser la forma más limpia de comprar esa retención.

## 5. Cómo implementarlo

1. **Grandfather 12 meses** a los 200 a $60. Cero mail de “te subimos el precio” ahora. Es la opción de menor riesgo y ya captura la mayor parte del upside.
2. **Precio nuevo mañana** en la web y en el checkout. Si tienes tráfico, testea 2 semanas $79 vs $89 vs $99 antes de grabar $89 en piedra. Mira conversión a pago y objeción “está caro”, no solo visitas.
3. **Empaqueta valor**, no solo cambies el número. Un solo plan a $89 frente a competidores de $29–$149 se siente arbitrario. Mejor tres planos: algo cerca de $49 para el segmento que si no se va al de $29, $89 como plan principal, $149 si hay multiusuario, sucursales o reportes. Así el salto no es “el mismo producto, 48% más caro”.
4. **Mes 9–12, no antes:** a la base antigua, oferta de plan anual a un efectivo de **$69–$75** (subida del 15–25%, dentro de la zona que la industria suele absorber), con 60–90 días de aviso y una razón concreta (nuevos módulos, límites, soporte). No saltes esa cohorte directo a $89. A $75 puedes perder hasta 20% y empatar MRR; apunta a perder menos del 10%.
5. **Comunicación, si algún día migras legacy:** qué cambió en el producto, qué pasa si no aceptan, fecha, y una salida anual más barata. Sin disculpas vagas ni “por inflación” como único argumento.
6. **Mide 8 semanas antes de cualquier otra decisión:** conversión a pago, CAC realizado, churn de la cohorte nueva a día 30/60, y % de altas que eligen anual. Si el CAC pasa de ~$180 o el churn de nuevos pasa de 9%, el precio de lista está alto para tu diferenciación actual.

No tienes un problema de LTV/CAC. Tienes un balde con un agujero del 7% mensual y espacio para cobrar más a quien aún no ancló su referencia en $60. Cobra $89 a los nuevos, protege a los actuales, y usa los próximos dos trimestres en retención, no en una subida general.