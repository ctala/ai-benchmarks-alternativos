# Claude Opus 5 (suscripción) — strategy/pricing_strategy

- model_id: `claude-opus-5`
- success: True  | final: 4.3 | quality: 5.0
- latency_total: 150.533s | tokens_per_second: 64.8
- input_tokens: 2 | output_tokens: 9751

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

# Análisis de pricing: $60 → $89

Antes de los números, una corrección que cambia todo el análisis.

## 0. Tu LTV está mal calculado (y eso ya te está costando dinero)

Estás usando **LTV = 14 × $60 = $840**, que es LTV sobre *ingreso*, no sobre *margen*. El estándar es margen bruto:

| Métrica | Cálculo | Valor |
|---|---|---|
| Margen bruto/usuario | $60 − $8 | **$52/mes (87%)** |
| Vida promedio | 1 / 0,07 | **14,3 meses** |
| LTV (ingreso) | $60 / 0,07 | $857 |
| **LTV (margen bruto)** | $52 / 0,07 | **$743** |

Los $840 que manejas son optimistas por ~13%. No es fatal, pero si estás decidiendo cuánto invertir en adquisición con ese número, estás sobrestimando tu capacidad.

---

## 1. LTV/CAC actual y proyectado

| Escenario | LTV (margen) | CAC | **LTV/CAC** | Payback CAC |
|---|---|---|---|---|
| Hoy ($60) | $743 | $120 | **6,2x** | **2,3 meses** |
| A $89 (churn igual) | $1.157 | $120 | 9,6x | 1,5 meses |
| A $89 (CAC +25% por menor conversión) | $1.157 | $150 | **7,7x** | 1,9 meses |

**El diagnóstico real no es que necesites subir el precio. Es que estás dramáticamente sub-invertido en adquisición.**

El benchmark sano de LTV/CAC es 3x. Tú estás en 6,2x. Eso no es "excelente", es una señal de alarma: significa que podrías gastar hasta **$247 de CAC** y seguir siendo saludable. Estás dejando crecimiento sobre la mesa por miedo o por falta de canales.

Payback de 2,3 meses es igual de revelador. El benchmark bueno es <12 meses, excelente <6. Tú recuperas el CAC en 10 semanas. Con esa economía, cada dólar que no metes en adquisición es un dólar que regalas.

**El precio bajo es un síntoma, no la enfermedad.** La enfermedad es un churn de 7% mensual (= **58% anual**). Eso es el doble del rango aceptable para B2B SMB (3-5% mensual).

---

## 2. Impacto esperado en churn

Benchmarks de la industria (ProfitWell/Paddle, Price Intelligently, datos de OpenView sobre subidas de precio en SaaS SMB):

| Magnitud de la subida | Churn shock esperado (90 días) | Efecto en churn steady-state |
|---|---|---|
| <10% | Despreciable (<2%) | Nulo |
| 20-30% | 3-8% | +0,3 a +0,8 pts |
| **40-50% (tu caso: +48%)** | **10-25%** | **+0,5 a +2 pts** |
| >75% | 25-40% | +2 a +4 pts |

Tres matices que importan más que el porcentaje:

**a) Clientes existentes y clientes nuevos son problemas distintos.** En los nuevos, el precio no afecta churn: afecta la tasa de conversión del funnel (o sea, sube el CAC). En los existentes es donde vive el churn shock. Modelarlos juntos es el error típico.

**b) $89 sigue estando en el medio de tu mercado.** Con competidores de $29 a $149, estás pasando del percentil ~25 al ~50. No estás saliéndote del rango; estás dejando de ser el barato. Y en software de inventario —donde un error de stock cuesta plata real— ser el más barato genera desconfianza, no ventaja.

**c) Antes de tocar el precio, descompón ese 7%.** En SaaS SMB, típicamente el **20-40% del churn es involuntario** (tarjetas rechazadas, no decisión del cliente). Si 2 de tus 7 puntos son fallos de pago, un sistema de dunning decente te devuelve ~1,5 puntos de churn en dos semanas, con riesgo cero. Eso vale más que la subida de precio y no molesta a nadie. Hazlo primero o en paralelo.

---

## 3. Tres escenarios (base actual de 200 clientes, horizonte 12 meses)

Supuestos: migración completa de la base a $89, costo de $8/usuario constante, sin clientes nuevos (aíslo el efecto sobre la base existente).

| | **Baseline $60** | **Optimista** | **Realista** | **Pesimista** |
|---|---|---|---|---|
| Churn shock (una vez) | — | 5% | 12% | 22% |
| Churn mensual post | 7% | 7% | 7,8% | 9% |
| Clientes tras el shock | 200 | 190 | 176 | 156 |
| **MRR inmediato** | $12.000 | **$16.910** | **$15.664** | **$13.884** |
| Δ MRR | — | +41% | +30,5% | +15,7% |
| Clientes a 12 meses | 84 | 80 | 66 | 50 |
| Ingreso acumulado 12m | $99.677 | $140.461 | $125.030 | $104.518 |
| **Margen bruto acum. 12m** | **$86.387** | **$127.836** | **$113.787** | **$95.129** |
| **Δ margen vs. baseline** | — | **+$41.449** | **+$27.400** | **+$8.742** |

### El número que decide todo

**Punto de equilibrio: puedes perder el 32,6% de tu base y quedar con el mismo MRR.** En margen bruto, aguantas hasta un **35,8%** de pérdida.

Necesitarías que 65 de tus 200 clientes se vayan de golpe para quedar igual que hoy. Los benchmarks dicen que perderás entre 10 y 25%. **Los tres escenarios son positivos, incluido el pesimista.**

Y el escenario pesimista está subestimando el upside: menos clientes en el tramo bajo también significa menos carga de soporte, menos infra y una base más comprometida. Los que se van por $29 suelen ser los que más tickets abren.

---

## 4. Recomendación

**Sube el precio. Pero no hagas solo eso, porque una subida plana de $60 a $89 es la versión pobre de la jugada.**

Tu problema real es que tienes **un solo precio para un mercado que va de $29 a $149**. Con un solo plano, estás cobrando lo mismo al que gestiona 300 SKUs en una bodega que al que gestiona 40.000 en cuatro. Al primero le sobra precio, al segundo le sobra valor gratis.

**Propuesta: tres planos en vez de un precio.**

| Plano | Precio | Para quién | Función |
|---|---|---|---|
| **Starter** | $49 | Límite en la métrica de valor (SKUs / bodegas / usuarios / órdenes-mes) | Convierte churn en downgrade. $49 > $0. Y te defiende del competidor de $29 |
| **Pro** | $89 | Tu feature set actual | El nuevo default. Aquí cae el 60-70% de tu base |
| **Business** | $169 | Multi-bodega, API, integraciones (ERP/e-commerce), soporte prioritario, SLA | Captura el segmento que hoy te paga $60 y pagaría $149 sin pestañear |

Números esperados con esta estructura sobre tu base de 200 (distribución conservadora 25/60/15, churn shock 10%):

- 180 clientes tras el shock → 45 Starter + 108 Pro + 27 Business
- MRR = (45×49) + (108×89) + (27×169) = 2.205 + 9.612 + 4.563 = **$16.380**
- **+36,5% de MRR con menos riesgo de churn que la subida plana**, porque el que no puede pagar $89 baja a $49 en vez de irse.

**Precio sobre una métrica de valor, no plano.** Software de inventario tiene métricas de valor obvias: SKUs, ubicaciones, órdenes procesadas. Eso te da expansion revenue automática: el cliente crece, tu factura crece, sin que vendas nada. Es la única forma de llegar a net revenue retention >100% y compensar el churn de logos.

**Y lo más importante: no te quedes el margen extra.** Con LTV/CAC en 7,7x post-subida, el destino correcto de esos ~$4.400/mes adicionales es adquisición. Tu límite sano de CAC pasa a ~$385. Si hoy gastas $120 y consigues X clientes, tienes espacio para triplicar la inversión y seguir con economía sana. Subir precio para engordar el margen y no crecer es cambiar una restricción por otra.

---

## 5. Estrategia de implementación

Ni grandfather eterno ni migración de golpe. Híbrido, en cuatro fases:

### Semana 1-2 — Datos antes de decidir
- Segmenta a los 200 por métrica de valor (SKUs, bodegas, usuarios, órdenes). Vas a descubrir que el top 20% está usando 5-10x lo que usa la mediana y pagando exactamente lo mismo. Ahí está tu plano Business.
- Descompón el churn: ¿cuánto es voluntario y cuánto es tarjeta rechazada? Activa dunning ya.
- 15-20 llamadas con clientes actuales. Van Westendorp o pregunta directa: "¿a qué precio te parecería caro pero aún lo comprarías?". Con 200 clientes no tienes volumen para A/B tests estadísticamente sólidos; vas a decidir con criterio + señales cualitativas, así que consigue buenas señales.

### Semana 2-3 — Cero riesgo: solo clientes nuevos
Sube a $89 en la web **solo para nuevos**. Hoy. No requiere anuncio, no toca a nadie, y en 30-45 días tienes la data que importa: cómo se movió la conversión de trial/demo. Si la conversión cae menos de 20%, la subida es claramente rentable (recuerda: aguantas CAC hasta $385).

### Mes 2 — Anuncio con fecha, no con sorpresa
A la base existente:
- **90 días de aviso.** El churn shock se dispara cuando la gente se entera por el cargo en la tarjeta.
- **Explica qué cambia**, no solo el precio. Si en esos 90 días entregas 2-3 mejoras que pidieron, la conversación pasa de "me subieron el precio" a "el producto avanzó".
- **La jugada clave: ofrece plan anual al precio viejo antes de migrar.** $720/año ($60×12) disponible solo hasta la fecha de corte. Efecto triple: (a) tus mejores clientes se quedan sin fricción, (b) entra caja por adelantado, (c) matas 12 meses de churn de golpe en ese segmento. El aumento lo capturas en la renovación del año 2. Con 7% de churn mensual, mover gente a anual es la palanca de retención más rápida que tienes, más que cualquier feature.
- **Escape hatch: Starter $49.** Al que no le da, baja de plano en vez de irse.

### Mes 3-4 — Migración y medición
- Migra a los que no tomaron anual ni bajaron.
- Concesiones caso a caso solo para cuentas grandes o de alto riesgo. Discrecional, no política pública.
- Mide separado: **churn shock** (primeros 90 días, one-time) vs. **churn steady-state** (mes 4 en adelante). Confundirlos te va a hacer creer que arruinaste el negocio cuando solo estás viendo el pico esperado.

### Lo que NO hacer

- **Grandfather indefinido.** Te deja con dos poblaciones para siempre, complica el soporte y en 3 años tienes clientes pagando la mitad. Grandfather con fecha de vencimiento, siempre.
- **Subir precio si el churn es de producto.** Si los 7 puntos son gente que se va porque falta una integración o porque hay bugs, subir el precio acelera la fuga. Verifica esto en las llamadas de la fase 1 antes de seguir adelante.
- **Guardarte el margen.** Ya lo dije y lo repito porque es donde más gente falla: el objetivo de esta subida es financiar crecimiento, no engordar el colchón.

---

## Resumen ejecutivo

| | |
|---|---|
| LTV/CAC real hoy | **6,2x** (no 7x) — estás sub-invirtiendo en adquisición |
| Payback CAC | **2,3 meses** — tienes espacio para gastar hasta $385 de CAC |
| Churn shock esperado | **10-25%** de la base en 90 días |
| Punto de equilibrio | **32,6%** de pérdida — tienes margen de sobra |
| Escenario realista | **+$27.400** de margen bruto en 12 meses, +30,5% MRR |
| Recomendación | Subir, pero a **3 planos ($49/$89/$169)** sobre métrica de valor, no a un precio plano |
| Riesgo mayor | Que el churn de 7% sea de producto, no de precio. **Verifícalo primero** |
| Palanca más grande que ignoraste | El churn de 58% anual. El precio se arregla en un mes; esto es el trabajo del trimestre |