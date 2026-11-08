# Claude Sonnet 5.5 — strategy/pricing_strategy

- model_id: `anthropic/claude-sonnet-5.5`
- success: True  | final: 6.43 | quality: 7.5
- latency_total: 59.449s | tokens_per_second: 126.6
- input_tokens: 290 | output_tokens: 7524

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

# Análisis de aumento de precio: $60 → $89/mes

## 0. Observaciones sobre tus datos

- **Tu LTV de $840 es sobre ingresos, no sobre margen.** Con churn de 7%, la vida media es 1/0.07 = 14.3 meses. El LTV correcto usa margen bruto: ($60 − $8) × 14.3 = **$743**.
- **Un churn de 7% mensual es alto.** Equivale a ~58% de churn anual (solo ~42% de los clientes sobrevive 12 meses). Para SaaS SMB, lo saludable ronda 3-5%. Esto importa mucho para la decisión.
- **Un LTV/CAC de ~7x está por encima del 3x que se considera sano.** Probablemente estás subinvirtiendo en adquisición, o tu CAC no incluye todos los costos (salarios de ventas, herramientas, tiempo tuyo). Conviene verificarlo.

---

## 1. LTV/CAC actual y proyectado

| Métrica | Actual ($60) | Con $89 (churn sin cambio, 7%) |
|---|---|---|
| Margen por usuario/mes | $52 | $81 (+56%) |
| Vida media | 14.3 meses | 14.3 meses |
| LTV (margen) | $743 | $1,157 |
| LTV/CAC (CAC $120) | **6.2x** | **9.6x** |
| Payback del CAC | 2.3 meses | 1.5 meses |
| MRR | $12,000 | $17,800 |

Este es el techo teórico, si nadie reacciona al aumento. Lo realista es que el churn suba y el CAC también, porque baja la conversión.

**Churn de equilibrio:** con $89 el LTV iguala al actual ($743) si el churn llega a **10.9%**. Por debajo de eso, cada cliente nuevo vale más que hoy.

---

## 2. Impacto estimado en churn

No hay un dato universal. Estas son heurísticas de benchmarks SaaS SMB, no mediciones sobre tu producto:

- Aumentos de 20-50% suelen generar un **pico de cancelación de 3-10%** en la base existente (más alto si el aviso es abrupto).
- El churn recurrente suele subir **10-30% en términos relativos** (de 7% a ~7.7-9%).
- La conversión de trial a pago suele caer **10-25%**, lo que sube el CAC efectivo en la misma proporción.
- El riesgo es mayor si tu producto es commodity, si los competidores de $29-49 ofrecen funciones similares, o si tus clientes son micro-negocios. Es menor si guardas datos críticos (inventario histórico) y los costos de cambio son altos.

Tu precio de $89 queda en la zona media-alta del rango de competidores ($29-$149), así que es defendible sin ser un outlier.

---

## 3. Tres escenarios

**Supuestos:** el presupuesto de adquisición se mantiene (~$1,680/mes, que hoy trae 14 clientes/mes y mantiene los 200 clientes estables). Los clientes actuales pasan a $89.

| | Actual | Optimista | Realista | Pesimista |
|---|---|---|---|---|
| Cancelación inmediata (base actual) | – | 3% (6) | 8% (16) | 20% (40) |
| Clientes tras el ajuste | 200 | 194 | 184 | 160 |
| Churn mensual nuevo | 7% | 7.5% | 8.5% | 11% |
| Vida media | 14.3 m | 13.3 m | 11.8 m | 9.1 m |
| CAC efectivo | $120 | $126 | $140 | $165 |
| LTV (margen) | $743 | $1,080 | $953 | $736 |
| **LTV/CAC** | 6.2x | **8.6x** | **6.8x** | **4.5x** |
| Payback | 2.3 m | 1.6 m | 1.7 m | 2.0 m |
| Clientes nuevos/mes (mismo presupuesto) | 14 | 13.3 | 12 | 10.2 |
| Clientes en estado estable | 200 | 178 | 141 | 93 |

### Impacto en utilidad (margen bruto − gasto de adquisición)

| | Actual | Optimista | Realista | Pesimista |
|---|---|---|---|---|
| **Mes 1** (margen bruto) | $10,400 | $15,700 (+51%) | $14,900 (+43%) | $13,000 (+25%) |
| **Acumulado 12 meses** | ~$105k | ~$163k (+56%) | ~$144k (+37%) | ~$107k (+3%) |
| **Estado estable mensual** | $8,720 | $12,700 (+46%) | $9,700 (+12%) | $5,900 (−33%) |

**Lectura clave:** el escenario pesimista parece aceptable el primer año, porque el alza de precio compensa la pérdida de clientes, pero **destruye valor a largo plazo**. Es una trampa: los números del mes 1 engañan.

**Punto de quiebre inmediato:** necesitarías perder ~36% de los clientes (71 de 200) de golpe para que el margen bruto del mes 1 quede por debajo del actual. Es muy improbable, pero el riesgo real está en el churn recurrente, no en el pico inicial.

---

## 4. Recomendación

**Sí, sube el precio, pero no a $89 de golpe para todos.** Los números respaldan el movimiento: en 2 de 3 escenarios mejoras claramente, y el pesimista se puede evitar con monitoreo y reversión. Pero tu verdadero problema es el churn de 7%.

**Plan concreto:**

1. **Clientes nuevos: $89 desde ya.** Es el menor riesgo, porque no hay anclaje previo ni cancelaciones por enojo. Mide la conversión de trial a pago durante 6-8 semanas.
2. **Clientes existentes: paso intermedio a $75 (+25%)**, y a $89 a los 6-9 meses si las métricas aguantan.
   - Con $75 el margen es $67 (+29%), y el riesgo de churn es bastante menor que con +48%.
3. **Ofrece plan anual a ~$74/mes equivalente ($890/año, "2 meses gratis").** Un cliente anual no puede irse en el mes 3, y es la palanca más fuerte contra tu churn de 7%. Si 30% de la base lo toma, recibes ~$53k de caja por adelantado.
4. **Ataca el churn en paralelo.** Bajar de 7% a 5% (vida de 20 meses) con $89 da un LTV de $1,620, un 40% más que el escenario base de $89, sin tocar el precio otra vez.

**Reglas de decisión (guardrails):**

| Señal (primeros 60-90 días) | Acción |
|---|---|
| Churn de la cohorte nueva ≤ 8.5% y conversión cae < 15% | Continuar, pasar a $89 para todos |
| Churn 8.5-10% o conversión cae 15-25% | Mantener en $75-79, mejorar onboarding/valor |
| Churn > 10% o conversión cae > 25% | Revertir a $75 para nuevos |

---

## 5. Estrategia de implementación

**Semanas 0-3: preparación**
- Segmenta la base por uso, antigüedad y NPS. Los clientes con alto uso del producto toleran mejor el aumento.
- Lanza o empaqueta algo que justifique el valor (reportes, integraciones, alertas de stock). Un aumento con mejora visible baja mucho la fricción.
- Considera una estructura de 3 planes, por ejemplo Starter $39-49 (limitado), **Pro $89** y Business $149. Así el $89 se ve como el plan "del medio" y no como un salto, y capturas a los sensibles al precio en lugar de perderlos.

**Semana 3: clientes nuevos a $89** (o con la nueva estructura de planes).
- Aviso: con ~14 altas al mes no puedes hacer un A/B estadísticamente válido. Compara cohortes secuenciales y mira indicadores adelantados (conversión de trial, cancelaciones en los primeros 30 días).

**Semana 4-12: clientes existentes**
- Avisa con **45-60 días** de anticipación, por email personal (idealmente del fundador), no un banner genérico.
- Estructura del mensaje: agradecimiento → qué has mejorado → nuevo precio → fecha → opción anual con descuento.
- **Grandfathering parcial:** los clientes de más de 12 meses o con alto uso mantienen $60-65 por 6 meses más y luego pasan a $75. Es una recompensa barata que protege a tu base más estable.
- Para clientes en riesgo de cancelar por precio, ten una oferta de retención (ej. 2-3 meses a precio intermedio o pasar al plan Starter) y no la anuncies.

**Mes 6-9: segundo paso a $89** para quienes están en $75, si los guardrails se cumplen.

**Qué medir semanalmente:** churn por cohorte (antes/después del aviso), conversión trial→pago, tasa de downgrade, tickets de soporte relacionados con precio, MRR neto y % de adopción del plan anual.

---

**Resumen:** el aumento tiene un caso numérico sólido (+37% de utilidad a 12 meses en el escenario realista), pero el riesgo está en que el churn recurrente supere ~10%. Escalonar el aumento, empujar el plan anual y reducir el churn de base convierte un escenario "realista" en uno "optimista". Antes de ejecutar, valida tu CAC completo y tu churn por segmento, porque los promedios pueden esconder que un grupo pequeño de clientes concentra la cancelación.