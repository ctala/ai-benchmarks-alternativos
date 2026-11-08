# Claude Opus 5.5 — strategy/pricing_strategy

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 6.19 | quality: 7.5
- latency_total: 64.164s | tokens_per_second: 93.0
- input_tokens: 290 | output_tokens: 5968

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

# Análisis de subida de precio: de $60 a $89/mes (+48%)

## 0. Correcciones a tus métricas base

**El LTV debería calcularse sobre margen, no sobre ingresos.** Tu LTV de $840 es de ingresos. Lo que realmente recuperas por cliente es el margen bruto:

| Métrica | Fórmula | Valor |
|---|---|---|
| Margen por cliente | $60 − $8 | $52/mes (86.7%) |
| Vida media | 1 / 7% | 14.3 meses |
| **LTV (margen)** | $52 / 0.07 | **$743** |
| LTV (ingresos) | $60 / 0.07 | $857 |
| **LTV/CAC (margen)** | $743 / $120 | **6.2x** |
| CAC payback | $120 / $52 | 2.3 meses |

**Diagnóstico:**
- **Un ratio de 6.2x y un payback de 2.3 meses indican que estás cobrando poco o invirtiendo poco en adquisición.** Lo sano es 3x–5x; por encima de 5x suele haber dinero sobre la mesa.
- **Tu churn del 7% mensual es tu problema real.** Equivale a perder el 58% de la base cada año. El benchmark para SaaS SMB es de 3–5% mensual, y lo ideal está por debajo del 3%.

---

## 1. LTV/CAC actual vs. con precio de $89

A $89 el margen por cliente sube a **$81/mes (91%)**, un 56% más de margen por cliente.

**Con el churn y el CAC actuales (caso teórico):**
- LTV (margen) = $81 / 0.07 = **$1,157**
- LTV/CAC = **9.6x** (antes 6.2x)

Pero el churn y el CAC no se quedarán iguales. Por eso hacen falta escenarios.

**Puntos de equilibrio clave:**
- **Churn máximo tolerable:** con CAC igual, el LTV se mantiene mientras el churn no supere el **10.9%**.
- **Clientes que puedes perder:** el MRR actual se mantiene aunque pierdas hasta **65 clientes (32%)** de golpe ($12,000 / $89 = 135 clientes).

El margen de seguridad es amplio.

---

## 2. Impacto estimado en churn (benchmarks)

Estos rangos son aproximados. Provienen de datos publicados por ProfitWell/Paddle, OpenView y casos públicos de SaaS SMB, no de una ley exacta:

| Tamaño del aumento | Pérdida inmediata de la base | Aumento del churn continuo |
|---|---|---|
| 10–20% | 1–3% | +0–0.5 pp |
| 20–35% | 3–8% | +0.5–1 pp |
| **40–50% (tu caso)** | **5–20%** | **+0.5–3.5 pp** |

**Factores que te protegen:**
- Los sistemas de inventario son "sticky": migrar datos y procesos cuesta.
- $89 sigue en la mitad del rango del mercado ($29–$149).

**Factores de riesgo:**
- Un churn del 7% sugiere que parte de tus clientes ya duda del valor. Esos se irán primero.
- Si tus clientes son muy pequeños, los competidores de $29 son una alternativa real.

**El precio también afecta a la adquisición.** Espera una caída de la conversión trial→pago del 10–35%, lo que sube tu CAC efectivo.

---

## 3. Tres escenarios

### Supuestos

| | Optimista | Realista | Pesimista |
|---|---|---|---|
| Pérdida inmediata | 5% (10 clientes) | 10% (20) | 20% (40) |
| Churn mensual nuevo | 7.5% | 8.5% | 10.5% |
| CAC nuevo | $132 (+10%) | $150 (+25%) | $180 (+50%) |

### Unit economics

| Métrica | Actual ($60) | Optimista | Realista | Pesimista |
|---|---|---|---|---|
| Vida media | 14.3 m | 13.3 m | 11.8 m | 9.5 m |
| LTV (margen) | $743 | $1,080 | $953 | $771 |
| **LTV/CAC** | **6.2x** | **8.2x** | **6.4x** | **4.3x** |

### Impacto en la base actual (200 clientes, sin grandfathering)

| Métrica | Actual | Optimista | Realista | Pesimista |
|---|---|---|---|---|
| Clientes | 200 | 190 | 180 | 160 |
| MRR | $12,000 | $16,910 | $16,020 | $14,240 |
| Δ MRR | — | **+41%** | **+34%** | **+19%** |
| Margen bruto mensual | $10,400 | $15,390 | $14,580 | $12,960 |
| Ingresos a 12 meses de la base actual* | $99,670 | $136,990 | $123,560 | $99,790 |

*Ingresos acumulados de los clientes actuales durante 12 meses, aplicando el churn de cada escenario y sin contar clientes nuevos.

**Lectura clave:** en el escenario pesimista los ingresos a 12 meses quedan prácticamente iguales a los actuales ($99.8K vs. $99.7K). **El peor caso razonable es quedarte igual, y el caso realista te da unos +$24K/año solo con la base actual.** El riesgo está acotado y el potencial es grande.

---

## 4. Recomendación

**Sube el precio, pero no a todos por igual ni de golpe.** Mi recomendación concreta:

**A. Clientes nuevos: $89 desde ya, con estructura de planes.**

| Plan | Precio | Para quién |
|---|---|---|
| Starter | $49 | Captura a quienes comparan con competidores de $29–$49. Funcionalidades limitadas (1 almacén, X SKUs). |
| **Pro** | **$89** | Plan ancla, el que quieres vender. |
| Business | $149 | Multi-almacén, integraciones, API, soporte prioritario. |

El plan Starter reduce el riesgo del escenario pesimista porque no pierdes a los sensibles al precio, solo los reubicas.

**B. Clientes actuales: subida escalonada a $79.** No los lleves a $89 directamente.
- Con un 6% de pérdida: 188 × $79 = **$14,852 MRR (+24%)** con mucho menos riesgo.
- Llévalos a $89 a los 12 meses, idealmente acompañado de mejoras visibles del producto.

**C. Ataca el churn en paralelo. Vale tanto como la subida de precio.**
- Bajar el churn del 7% al 5% a $60 lleva el LTV de $743 a $1,040 (+40%).
- Las dos cosas juntas ($89 y 5% de churn) dan un LTV de **$1,620**, más del doble del actual.

---

## 5. Estrategia de implementación

### Fase 1: Validación (semanas 1–4)
- Segmenta los 200 clientes por uso, antigüedad y engagement. Identifica tus 20–30 clientes más activos; son los menos sensibles al precio.
- Pon $89 solo para nuevos registros y mide la conversión trial→pago frente a tu histórico.
- Entrevista a 10 clientes: ¿qué valor obtienen?, ¿cuánto les ahorra el producto?, ¿a qué alternativa irían?

### Fase 2: Lanzamiento a nuevos clientes (mes 2)
- Publica la estructura de tres planes.
- Ofrece plan anual con 2 meses gratis ($890/año en Pro). Es clave para reducir churn.

### Fase 3: Comunicación a clientes actuales (mes 2–3)
- Avisa con **60–90 días de antelación**, por email personal (no automático) y explicando el valor añadido.
- Dales tres opciones:
  1. **Bloquear el precio actual pagando un año por adelantado** ($720/año). Esto convierte a los clientes en riesgo en anuales y elimina su churn mensual durante 12 meses.
  2. Pasar a $79/mes como "precio de cliente fundador".
  3. Bajar al plan Starter de $49 si les sobra funcionalidad.
- Llama personalmente a tus 20 cuentas más grandes.

### Fase 4: Ejecución y monitoreo (meses 4–12)

| Métrica | Umbral de alerta | Acción |
|---|---|---|
| Conversión trial→pago | Cae más del 30% | Revisar el precio de Pro o reforzar Starter |
| Churn mensual | Más del 9% durante 2 meses seguidos | Pausar la subida a $89 para la base antigua |
| Pérdida inmediata tras el aviso | Más del 15% | Ofertas de retención |
| Adopción del plan anual | Menos del 15% | Mejorar el incentivo |

---

## Resumen

| | Hoy | Con la estrategia (realista) |
|---|---|---|
| MRR | $12,000 | ~$15,000–16,000 |
| LTV (margen) | $743 | ~$950–1,100 |
| LTV/CAC | 6.2x | ~6.5–7.5x |
| Riesgo en el peor caso | — | Ingresos iguales a 12 meses |

**Conclusión:** estás infravalorado. La subida tiene un riesgo acotado y un potencial de +25–40% de MRR. Sin embargo, la palanca más grande a largo plazo es reducir el churn del 7%. Si solo pudieras hacer una cosa, haz las dos: la subida de precio te da la caja para invertir en retención.