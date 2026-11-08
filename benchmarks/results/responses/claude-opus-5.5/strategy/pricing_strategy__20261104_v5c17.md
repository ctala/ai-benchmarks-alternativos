# Claude Opus 5.5 — strategy/pricing_strategy

- model_id: `anthropic/claude-opus-5.5`
- success: True  | final: 7.97 | quality: 10.0
- latency_total: 51.93s | tokens_per_second: 97.1
- input_tokens: 290 | output_tokens: 5040

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

# Análisis de subida de precio: $60 → $89/mes

## 1. LTV/CAC actual y proyectado

Tu LTV de $840 usa **ingresos**. Para decidir conviene usar **margen bruto**, porque tu costo de $8/usuario no es despreciable.

| Métrica | Actual ($60) | Con $89 (mismo churn) |
|---|---|---|
| Margen por cliente/mes | $52 (86.7%) | $81 (91.0%) |
| Vida promedio (1/churn) | 14.3 meses | 14.3 meses |
| LTV ingresos | $857 | $1,271 |
| **LTV margen bruto** | **$743** | **$1,157** |
| LTV/CAC (ingresos) | 7.1x | 10.6x |
| **LTV/CAC (margen)** | **6.2x** | **9.6x** |
| Payback del CAC | 2.3 meses | 1.5 meses |

**Lectura:** el benchmark sano es 3x. Un 6x con payback de 2 meses suele indicar dos cosas: **estás cobrando poco** o **estás invirtiendo poco en adquisición**. Probablemente ambas.

La columna "mismo churn" es irreal. Los escenarios del punto 3 ajustan el churn y el CAC.

## 2. Impacto esperado en churn (benchmarks)

Primero, un problema que pesa más que el precio. **Un churn mensual del 7% es alto.** Equivale a perder ~58% de la base al año (0.93¹² = 0.42 retenido). Los benchmarks de SaaS B2B para SMB están en 3–5% mensual, y por debajo de 2% en mid-market.

Qué suele pasar con subidas de precio en SaaS SMB, según referencias de ProfitWell/Paddle, OpenView y casos públicos:

- **Pico único de cancelaciones** al anunciar: típicamente 3–15% de la base afectada. Llega al 20–30% si la subida es grande y mal comunicada.
- **Aumento del churn estructural:** +0.5 a +2 puntos mensuales en clientes nuevos, sobre todo en los primeros 3 meses.
- **Caída de conversión** trial→pago: 5–25% con aumentos del 30–50%. Esto encarece el CAC.
- Tu subida es de **+48%**, en el rango alto. Pero a $89 sigues **en la mitad** del rango de competidores ($29–$149), no en el extremo.

Son rangos orientativos, no leyes. Tu resultado real depende de cuánto valor perciben tus clientes.

## 3. Tres escenarios

### Supuestos

| | Optimista | Realista | Pesimista |
|---|---|---|---|
| Pérdida única de base al anunciar | 5% (10 clientes) | 12% (24) | 25% (50) |
| Churn mensual posterior | 7.5% | 8.5% | 10% |
| CAC (por menor conversión) | $125 | $140 | $165 |

### Resultados

| Métrica | Actual | Optimista | Realista | Pesimista |
|---|---|---|---|---|
| Clientes tras el anuncio | 200 | 190 | 176 | 150 |
| MRR | $12,000 | $16,910 (+41%) | $15,664 (+31%) | $13,350 (+11%) |
| Margen bruto mensual | $10,400 | $15,390 (+48%) | $14,256 (+37%) | $12,150 (+17%) |
| LTV margen (cliente nuevo) | $743 | $1,080 | $953 | $810 |
| LTV/CAC (margen) | 6.2x | 8.6x | 6.8x | 4.9x |
| **Margen acumulado 12 meses de la base actual*** | **$86,380** | **$124,685 (+44%)** | **$109,957 (+27%)** | **$87,185 (+1%)** |

*Base actual decayendo con su churn, sin contar clientes nuevos.

### Punto de equilibrio

- Para mantener el **MRR actual** a $89 necesitas 135 clientes. **Puedes perder hasta 65 (33%)**.
- Para mantener el **margen bruto actual** necesitas 129 clientes. **Puedes perder hasta 71 (36%)**.

**Conclusión clave:** incluso el escenario pesimista empata con tu situación actual a 12 meses. El riesgo a la baja es limitado y el potencial al alza es grande.

## 4. Recomendación

**Sí, sube el precio. Pero no como un cambio plano de $60 a $89 para todos.**

1. **Clientes nuevos: $89 desde ya.** Aquí no hay riesgo de enojar a nadie.
2. **Pasa a precios por niveles** para capturar todo el rango del mercado:
   - **Básico $49:** límite de SKUs/usuarios. Es la red de seguridad para quien se iría por precio.
   - **Pro $89:** el plan actual más alguna mejora visible.
   - **Business $149+:** multi-almacén, integraciones, API, soporte prioritario.
3. **Clientes actuales: migración gradual con incentivo anual** (detalle en el punto 5).
4. **Tu mayor palanca es el churn, no el precio:**

| Churn a $89 | LTV margen | vs. hoy |
|---|---|---|
| 8.5% | $953 | +28% |
| 5% | $1,620 | +118% |

   Bajar el churn de 7% a 5% vale más que la subida de precio por sí sola. Invierte parte del margen nuevo en onboarding y customer success.

**Meta concreta a 6 meses:** MRR de ~$15,500+, churn ≤7%, y al menos 30% de la base en plan anual.

## 5. Estrategia de implementación

### Fase 0 (semanas 1–2): preparación
- Segmenta a los 200 clientes por antigüedad, uso y salud de la cuenta. Identifica a los ~20–30 de mayor riesgo y a los de mayor uso, que son los más dispuestos a pagar.
- Lanza o empaqueta 1–2 mejoras visibles para justificar el "Pro".
- Define tus métricas de alerta (abajo).

### Fase 1 (semana 3): nuevos clientes
- Precio nuevo activo. Mide la conversión trial→pago durante 6–8 semanas.
- Con tu volumen, los datos tienen mucho ruido: 7% de 200 son ~14 bajas al mes, ±4. **No reacciones a un solo mes.**

### Fase 2 (semana 4): anuncio a clientes actuales, con 60 días de aviso
Ofrece tres opciones:

| Opción | Condición | Objetivo |
|---|---|---|
| **A. Anual bloqueado** | $65/mes pagado anual ($780) durante 12 meses | Fijar ingresos y reducir churn drásticamente |
| **B. Mensual escalonado** | $60 → $75 (mes 3) → $89 (mes 9) | Suavizar el impacto |
| **C. Downgrade a Básico** | $49 | Retener a quien es sensible al precio |

- **Grandfathering completo** solo para clientes con más de 18 meses o casos estratégicos. Debe ser una excepción.
- En la comunicación, enfatiza las mejoras recientes y las que vienen, y explica el motivo con transparencia. Que nunca parezca una sorpresa.
- **Llama personalmente a los 20 clientes de mayor riesgo** antes de enviar el email masivo.

### Fase 3 (meses 3–9): monitoreo
**Alertas para pausar o ajustar:**
- Churn mensual mayor a 10% durante 2 meses seguidos.
- Conversión trial→pago cae más de 25% respecto a la línea base.
- Más del 15% de cancelaciones citan el precio como motivo principal. Agrega una encuesta de salida obligatoria.

**Si se activa una alerta:** prueba un plan Pro a $79 antes de revertir por completo.

---

**Resumen:** tus unit economics aguantan holgadamente la subida. El peor caso razonable te deja igual que hoy y el caso realista te da ~+30% de MRR. El verdadero cuello de botella de tu negocio es el churn del 7%. Usa el margen extra para atacarlo.